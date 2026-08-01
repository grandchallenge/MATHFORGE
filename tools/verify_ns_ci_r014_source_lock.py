from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SOURCE_SPECS = (
    {
        "source_id": "NS-CI-R014-S1",
        "versioned_id": "2605.01875v3",
        "pdf_name": "2605.01875v3.pdf",
        "tex_name": "2605.01875v3.eprint",
    },
    {
        "source_id": "NS-CI-R014-S2",
        "versioned_id": "2605.01873v2",
        "pdf_name": "2605.01873v2.pdf",
        "tex_name": "2605.01873v2.eprint",
    },
    {
        "source_id": "NS-CI-R014-S3",
        "versioned_id": "2605.09797v2",
        "pdf_name": "2605.09797v2.pdf",
        "tex_name": "2605.09797v2.eprint",
    },
    {
        "source_id": "NS-CI-R014-S4",
        "versioned_id": "2606.07869v1",
        "pdf_name": "2606.07869v1.pdf",
        "tex_name": "2606.07869v1.eprint",
    },
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def detect_container(path: Path) -> str:
    prefix = path.read_bytes()[:512]
    if prefix.startswith(b"\x1f\x8b"):
        return "gzip"
    if prefix.startswith(b"PK\x03\x04"):
        return "zip"
    if prefix.startswith(b"BZh"):
        return "bzip2"
    if prefix.startswith(b"\xfd7zXZ\x00"):
        return "xz"
    if len(prefix) >= 265 and prefix[257:262] == b"ustar":
        return "tar"
    if b"\\documentclass" in prefix or b"\\begin{document}" in prefix:
        return "tex"
    return "unknown_binary_or_text"


def pdf_page_count(path: Path) -> int | None:
    try:
        completed = subprocess.run(
            ["pdfinfo", str(path)],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None
    match = re.search(r"^Pages:\s+(\d+)\s*$", completed.stdout, re.MULTILINE)
    return int(match.group(1)) if match else None


def load_record(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--record", required=True, type=Path)
    args = parser.parse_args()

    record = load_record(args.record)
    record_sources = {item["source_id"]: item for item in record["sources"]}
    errors: list[str] = []
    results: list[dict[str, Any]] = []

    for spec in SOURCE_SPECS:
        source_id = spec["source_id"]
        expected = record_sources.get(source_id)
        if expected is None:
            errors.append(f"record missing {source_id}")
            continue

        expected_versioned_id = f"{expected['arxiv_id']}v{expected['version']}"
        if expected_versioned_id != spec["versioned_id"]:
            errors.append(
                f"{source_id}: ledger version {expected_versioned_id} != verifier {spec['versioned_id']}"
            )

        pdf_path = args.input_dir / spec["pdf_name"]
        tex_path = args.input_dir / spec["tex_name"]
        for path in (pdf_path, tex_path):
            if not path.is_file() or path.stat().st_size == 0:
                errors.append(f"missing or empty acquisition: {path}")

        if not pdf_path.is_file() or not tex_path.is_file():
            continue

        pdf_bytes = pdf_path.read_bytes()
        pdf_header_valid = pdf_bytes.startswith(b"%PDF-")
        pdf_eof_present = b"%%EOF" in pdf_bytes[-4096:]
        if not pdf_header_valid:
            errors.append(f"{source_id}: PDF header invalid")
        if not pdf_eof_present:
            errors.append(f"{source_id}: PDF EOF marker absent")

        actual_pdf_sha = sha256(pdf_path)
        actual_tex_sha = sha256(tex_path)
        page_count = pdf_page_count(pdf_path)
        if page_count is not None and page_count != expected["page_count"]:
            errors.append(
                f"{source_id}: page count {page_count} != ledger {expected['page_count']}"
            )

        expected_pdf_sha = expected.get("pdf_sha256")
        expected_tex_sha = expected.get("tex_sha256")
        if expected_pdf_sha is not None and actual_pdf_sha != expected_pdf_sha:
            errors.append(f"{source_id}: PDF digest mismatch")
        if expected_tex_sha is not None and actual_tex_sha != expected_tex_sha:
            errors.append(f"{source_id}: TeX/e-print digest mismatch")

        results.append(
            {
                "source_id": source_id,
                "versioned_arxiv_id": spec["versioned_id"],
                "pdf": {
                    "url": f"https://arxiv.org/pdf/{spec['versioned_id']}",
                    "sha256": actual_pdf_sha,
                    "bytes": pdf_path.stat().st_size,
                    "page_count": page_count,
                    "header_valid": pdf_header_valid,
                    "eof_marker_present": pdf_eof_present,
                    "matches_committed_digest": (
                        expected_pdf_sha is not None and actual_pdf_sha == expected_pdf_sha
                    ),
                },
                "tex_eprint": {
                    "url": f"https://arxiv.org/e-print/{spec['versioned_id']}",
                    "sha256": actual_tex_sha,
                    "bytes": tex_path.stat().st_size,
                    "container": detect_container(tex_path),
                    "matches_committed_digest": (
                        expected_tex_sha is not None and actual_tex_sha == expected_tex_sha
                    ),
                },
            }
        )

    committed_digests_complete = all(
        item.get("pdf_sha256") is not None and item.get("tex_sha256") is not None
        for item in record["sources"]
    )
    report = {
        "schema_version": "1.0.0",
        "record_id": "MF-NS-CI-R014-SOURCE-ACQUISITION",
        "generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "subject_record": str(args.record),
        "sources": results,
        "committed_digests_complete": committed_digests_complete,
        "source_bytes_locked": committed_digests_complete and not errors,
        "errors": errors,
        "claim_boundary": (
            "This report authenticates exact arXiv PDF and TeX/e-print byte identities only. "
            "It does not validate a proof step, clear an analytic obligation, change Programme "
            "theorem status, authorize MATHCERT, or promote a Navier--Stokes regularity claim."
        ),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
