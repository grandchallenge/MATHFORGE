#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pdfinfo(path: Path) -> dict[str, str]:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return {
        key.strip(): value.strip()
        for line in output.splitlines()
        if ":" in line
        for key, value in [line.split(":", 1)]
    }


def extracted_text(path: Path) -> str:
    with tempfile.TemporaryDirectory() as directory:
        output = Path(directory) / "source.txt"
        subprocess.run(["pdftotext", "-layout", str(path), str(output)], check=True)
        return output.read_text(encoding="utf-8")


def normalize(text: str) -> str:
    text = re.sub(r"arXiv:2410\.09574v2 \[hep-th\] 3 Jun 2026", "", text)
    text = re.sub(r"June [34], 2026", "June DATE, 2026", text)
    return re.sub(r"\s+", "", text, flags=re.UNICODE)


def verify_pdf(path: Path, expected: dict[str, object]) -> dict[str, object]:
    info = pdfinfo(path)
    actual = {
        "sha256": sha256(path),
        "byte_length": path.stat().st_size,
        "pages": int(info["Pages"]),
        "pdf_version": info["PDF version"],
    }
    for key, value in actual.items():
        if value != expected[key]:
            raise AssertionError(f"{path}: {key} expected {expected[key]!r}, found {value!r}")
    return actual


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--author-pdf", type=Path, required=True)
    parser.add_argument("--arxiv-pdf", type=Path, required=True)
    parser.add_argument("--record", type=Path, required=True)
    args = parser.parse_args()
    record = json.loads(args.record.read_text(encoding="utf-8"))
    acquisition = record["acquisition"]
    author = verify_pdf(args.author_pdf, acquisition["author_pdf"])
    arxiv = verify_pdf(args.arxiv_pdf, acquisition["arxiv_v2_pdf"])

    author_normalized = normalize(extracted_text(args.author_pdf))
    arxiv_normalized = normalize(extracted_text(args.arxiv_pdf))
    if author_normalized != arxiv_normalized:
        raise AssertionError("author PDF and arXiv v2 normalized text differ")
    normalized_digest = hashlib.sha256(author_normalized.encode("utf-8")).hexdigest()
    expected_digest = record["revision_concordance"]["normalized_text_sha256"]
    if normalized_digest != expected_digest:
        raise AssertionError(
            f"normalized text digest expected {expected_digest}, found {normalized_digest}"
        )
    required = ["ExampleB.1", "PropositionB.2", "ExampleB.3", "RemarkB.4", "Figure16"]
    for token in required:
        if token not in author_normalized:
            raise AssertionError(f"required Appendix B token absent: {token}")

    print(json.dumps({
        "record_id": record["record_id"],
        "author_pdf": author,
        "arxiv_v2_pdf": arxiv,
        "byte_identical": author["sha256"] == arxiv["sha256"],
        "normalized_text_identical": True,
        "normalized_text_sha256": normalized_digest,
        "claim_boundary": "source identity and revision concordance only; no mathematical certification or admission",
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
