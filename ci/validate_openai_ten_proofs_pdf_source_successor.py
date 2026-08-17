#!/usr/bin/env python3
import json
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/pdf_source_successors/OTP-SOURCE-PDF-SUCCESSOR-002.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_pdf_source_successor.schema.json"
HIST = ROOT / "sources/OPENAI-TEN-PROOFS-001/recovery/OTP-SOURCE-PDF-HISTORICAL-RECOVERY-001/recovery_record.json"
FORMAL = ROOT / "sources/OPENAI-TEN-PROOFS-001/formal_source_successors/OTP-FORMAL-SOURCE-SUCCESSOR-002.json"

EXPECTED_FAMILIES = {
    "OTP-A-SPHERE-PACKING", "OTP-B1-BINARY-CODES", "OTP-B2-SPHERICAL-CODES",
    "OTP-D-NON-SOFIC", "OTP-E-CONNES-RIGIDITY",
    "OTP-G-QUANTUM-PARALLEL-REPETITION", "OTP-H-GAPCVP", "OTP-I-RAMSEY",
}


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_record(record):
    schema = load(SCHEMA)
    jsonschema.Draft202012Validator(schema).validate(record)
    hist = load(HIST)
    formal = load(FORMAL)
    assert record["predecessor"]["byte_length"] == hist["historical_identity"]["byte_length"]
    assert record["predecessor"]["sha256"] == hist["historical_identity"]["sha256"]
    assert record["predecessor"]["immutable"] is True
    assert record["formal_subject"]["root"] == formal["successor"]["root"]
    assert record["formal_subject"]["tree"] == formal["successor"]["tree"]
    families = [x["family"] for x in record["family_loci"]]
    assert len(families) == len(set(families)) == 8
    assert set(families) == EXPECTED_FAMILIES
    effect = record["authority_effect"]
    assert effect == {
        "semantic_source_identity_after_protected_merge": "current_pdf_loci_only",
        "family_semantic_clearance": False,
        "solve_authority": False,
        "cert_authority": False,
        "whole_document_equivalence": False,
        "aggregate_authority": False,
    }
    return True


def main():
    validate_record(load(RECORD))
    print("OTP-SOURCE-PDF-SUCCESSOR-002: VALID")


if __name__ == "__main__":
    main()
