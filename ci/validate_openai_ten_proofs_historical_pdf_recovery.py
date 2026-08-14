#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/recovery/OTP-SOURCE-PDF-HISTORICAL-RECOVERY-001/recovery_record.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_historical_pdf_recovery_record.schema.json"

EXPECTED_SHA = "f318c6508c9d49ef876a5a26cd73928705f96c07bb43e92a0cb35bd3f666ea53"
EXPECTED_BYTES = 2266052


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record=None):
    record = load(RECORD) if record is None else record
    schema = load(SCHEMA)
    errors = [e.message for e in Draft202012Validator(schema).iter_errors(record)]
    if record.get("historical_identity", {}).get("sha256") != EXPECTED_SHA:
        errors.append("historical digest drift")
    if record.get("historical_identity", {}).get("byte_length") != EXPECTED_BYTES:
        errors.append("historical byte-length drift")
    gate = record.get("acceptance_gate", {})
    if gate.get("required_sha256") != EXPECTED_SHA or gate.get("required_byte_length") != EXPECTED_BYTES:
        errors.append("acceptance gate no longer binds exact historical identity")
    if record.get("exit_state") != "OPEN_WITH_CHARACTERIZED_HISTORICAL_PDF_RECOVERY_BLOCKER":
        errors.append("unsupported recovery promotion")
    if record.get("known_source_drift", {}).get("may_substitute_for_historical_payload") is not False:
        errors.append("later source substitution enabled")
    independence = record.get("downstream_independence", {})
    for field in (
        "invalidates_protected_lean_source",
        "invalidates_permanent_semantic_nonvacuity_clearance",
        "blocks_routing_of_already_cleared_variable_leaf_targets",
        "creates_whole_document_semantic_equivalence",
    ):
        if independence.get(field) is not False:
            errors.append(f"invalid downstream authority: {field}")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("historical PDF recovery blocker record validates fail-closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
