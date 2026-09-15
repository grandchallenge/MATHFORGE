#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "tools" / "audit_vgse_arxiv_source_archive.py"
SPEC = importlib.util.spec_from_file_location("vgse_source_archive_audit", AUDIT_PATH)
assert SPEC and SPEC.loader
AUDIT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDIT)

ASSIGNMENT_RE = re.compile(r"(?::=|(?<![<>])=(?!=))")
NUMERIC_RE = re.compile(r"(?:\\frac\{|(?<![A-Za-z])\d+(?:\.\d+)?(?![A-Za-z]))")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()


def token_sides(text: str, pattern: re.Pattern[str], split_at: int, split_end: int) -> tuple[bool, bool]:
    left = text[:split_at]
    right = text[split_end:]
    return bool(pattern.search(left)), bool(pattern.search(right))


def classify_line(line: str, line_number: int) -> dict | None:
    stripped = line.strip()
    assignment = ASSIGNMENT_RE.search(stripped)
    if assignment is None:
        return None
    if not (AUDIT.WEIGHT_TOKEN_RE.search(stripped) or AUDIT.MEAS_TOKEN_RE.search(stripped) or AUDIT.GAMMA_TOKEN_RE.search(stripped)):
        return None

    weight_left, weight_right = token_sides(stripped, AUDIT.WEIGHT_TOKEN_RE, assignment.start(), assignment.end())
    meas_left, meas_right = token_sides(stripped, AUDIT.MEAS_TOKEN_RE, assignment.start(), assignment.end())
    gamma_left, gamma_right = token_sides(stripped, AUDIT.GAMMA_TOKEN_RE, assignment.start(), assignment.end())
    lhs = stripped[: assignment.start()].strip()
    rhs = stripped[assignment.end() :].strip()
    rhs_numeric_tokens = NUMERIC_RE.findall(rhs)

    if meas_left or meas_right:
        classification = "measurement_relation"
    elif weight_left:
        classification = "weight_definition_candidate"
    elif weight_right:
        classification = "weight_reference_on_rhs"
    else:
        classification = "other_graph_relation"

    return {
        "line": line_number,
        "line_sha256": sha256_text(stripped),
        "assignment_token": assignment.group(0),
        "lhs_sha256": sha256_text(lhs),
        "rhs_sha256": sha256_text(rhs),
        "classification": classification,
        "weight_token_on_lhs": weight_left,
        "weight_token_on_rhs": weight_right,
        "measurement_token_on_lhs": meas_left,
        "measurement_token_on_rhs": meas_right,
        "gamma_token_on_lhs": gamma_left,
        "gamma_token_on_rhs": gamma_right,
        "rhs_numeric_token_count": len(rhs_numeric_tokens),
        "numeric_rhs": bool(rhs_numeric_tokens),
    }


def build_record(source_archive: Path) -> dict:
    archive_sha, members = AUDIT.load_members(source_archive)
    text_cache: dict[str, str] = {}
    for name, data in members:
        if PurePosixPath(name).suffix.lower() not in AUDIT.TEXT_EXTS:
            continue
        text = AUDIT.decode_text(data)
        if text is not None:
            text_cache[name] = text

    source_windows: dict[str, tuple[int, int]] = {}
    figure_refs: list[dict] = []
    for name, text in text_cache.items():
        lines = text.splitlines()
        for idx, line in enumerate(lines):
            for target in AUDIT.INCLUDE_RE.findall(line):
                if not AUDIT.VARC_TARGET_RE.search(target):
                    continue
                lo = max(0, idx - 100)
                hi = min(len(lines), idx + 101)
                previous = source_windows.get(name)
                source_windows[name] = (min(previous[0], lo), max(previous[1], hi)) if previous else (lo, hi)
                figure_refs.append({"source_file": name, "line": idx + 1, "target": target})

    relations: list[dict] = []
    for name, (lo, hi) in source_windows.items():
        lines = text_cache[name].splitlines()
        for idx in range(lo, hi):
            record = classify_line(lines[idx], idx + 1)
            if record is not None:
                relations.append({"source_file": name, **record})

    summary = {
        "measurement_relation_lines": [r["line"] for r in relations if r["classification"] == "measurement_relation"],
        "weight_definition_candidate_lines": [r["line"] for r in relations if r["classification"] == "weight_definition_candidate"],
        "numeric_weight_definition_candidate_lines": [r["line"] for r in relations if r["classification"] == "weight_definition_candidate" and r["numeric_rhs"]],
        "weight_reference_on_rhs_lines": [r["line"] for r in relations if r["classification"] == "weight_reference_on_rhs"],
    }
    return {
        "schema_version": "1.0.0",
        "audit_id": "VGSE-VARCHENKO-WEIGHT-SEMANTICS-AUDIT-001",
        "campaign_id": "VGSE-001",
        "source": {"arxiv_id": "2410.09574v2", "archive_sha256": archive_sha},
        "varchenko_figure_references": figure_refs,
        "relations": relations,
        "summary": summary,
        "interpretation": {
            "source_prose_emitted": False,
            "source_bytes_committed": False,
            "mathematical_certification_performed": False,
            "classification_rule": "measurement token on either equality side => measurement_relation; otherwise weight token on lhs => weight_definition_candidate; otherwise weight token on rhs => weight_reference_on_rhs",
            "c06_reopening_effect": "none_until_provider evidence is reviewed against the protected reopening condition",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-archive", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    record = build_record(args.source_archive)
    text = json.dumps(record, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
