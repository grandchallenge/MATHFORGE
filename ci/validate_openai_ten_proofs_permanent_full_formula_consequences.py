#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-C-PERMANENT-FULL-FORMULA-CONSEQUENCES/audit_record.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_permanent_full_formula_consequences_audit.schema.json"

EXPECTED = {
    "threshold": 32,
    "log_base": 2,
    "division_free": (128, 128, 128, 256),
    "rational": (192, 192, 192, 384),
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record=None):
    record = load(RECORD) if record is None else record
    schema = load(SCHEMA)
    errors = [e.message for e in Draft202012Validator(schema).iter_errors(record)]
    projection = record.get("source_projection", {})
    if projection.get("dimension_threshold") != EXPECTED["threshold"]:
        errors.append("dimension threshold drift")
    if projection.get("log_base") != EXPECTED["log_base"]:
        errors.append("log base drift")
    for key in ("division_free", "rational"):
        part = projection.get(key, {})
        observed = (
            part.get("variable_leaf_constant"),
            part.get("leaf_count_constant"),
            part.get("vertex_count_constant"),
            part.get("internal_gate_constant"),
        )
        if observed != EXPECTED[key]:
            errors.append(f"{key} source constants drift")
    replay = record.get("exact_overlay_replay", {})
    for field in ("lean_default_kernel", "nanoda_kernel", "comparator"):
        if replay.get(field) != "accepted":
            errors.append(f"replay acceptance lost: {field}")
    if replay.get("immutable_archive_modified") is not False:
        errors.append("immutable archive mutation asserted")
    coverage = record.get("coverage", {})
    if coverage.get("theorem_1_2_full_formula_consequences") is not True or coverage.get("theorem_1_3_full_formula_consequences") is not True:
        errors.append("full formula consequence coverage missing")
    for field in (
        "source_theorem_1_1_circuit_complexity",
        "historical_pdf_byte_equivalence",
        "solve_handoff_for_new_targets",
        "mathcert_route_for_new_targets",
        "adjudication",
        "cert_output",
        "mathematical_target_proved_promoted",
        "aggregate_ten_proofs_authority",
    ):
        if coverage.get(field) is not False:
            errors.append(f"prohibited authority enabled: {field}")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Permanent full-formula consequences audit validates fail-closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
