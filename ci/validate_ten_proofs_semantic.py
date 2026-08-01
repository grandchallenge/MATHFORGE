#!/usr/bin/env python3
"""Validate OTP-SEMANTIC-WP01 tranche-one audit records."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
AUDIT_DIR = ROOT / "sources" / "OPENAI-TEN-PROOFS-001" / "semantic_audits"
SCHEMA_PATH = ROOT / "schemas" / "ten_proofs_semantic_audit.schema.json"
DOCUMENT_PATH = AUDIT_DIR / "README.md"

EXPECTED = {
    "OTP-F-EHRHART": {
        "path": "OTP-F-EHRHART.json",
        "challenge_blob": "915f4d4230c36581fb0123763c30fd329ac5aeb8",
        "solution_blob": "312c65cbdd80b4b6db39ce0ce73de128a8584a9d",
        "config_blob": "374e80eca19e6265508843a76a51710f9d32f94c",
        "theorems": {
            "Ehrhart.Volume.ehrhart_volume_inequality_for_sets",
            "Ehrhart.SimplexVolume.exists_centeredBody_sharp",
            "Ehrhart.SimplexVolume.barycenter_centeredSimplex",
            "Ehrhart.SimplexVolume.normalizedVolume_centeredSimplex",
        },
    },
    "OTP-J1-COMPACTNESS": {
        "path": "OTP-J1-COMPACTNESS.json",
        "challenge_blob": "0e9c50d24422cc1016e1621b88bece204056ce33",
        "solution_blob": "39fc24a0060b335475af960944baf6b85c3add98",
        "config_blob": "c484ab6f83edebc64c660c06d2ddb7263380084f",
        "theorems": {
            "CompactnessConjecture.quantitativeCompactnessCounterexample",
            "CompactnessConjecture.compactnessCounterexample_bigO",
            "CompactnessConjecture.not_erdos_180",
        },
    },
    "OTP-J2-TWO-DEGENERATE": {
        "path": "OTP-J2-TWO-DEGENERATE.json",
        "challenge_blob": "dd22ce141dd0a860ecdccfda291c0f3a480a1d70",
        "solution_blob": "39fc24a0060b335475af960944baf6b85c3add98",
        "config_blob": "d8a542b5ce620b686cb24a6756360e76c5d2b1c1",
        "theorems": {
            "TwoDegenerateGraphs.twoDegenerateExtremalCounterexample",
            "TwoDegenerateGraphs.not_erdos_146",
        },
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_records() -> dict[str, dict[str, Any]]:
    return {
        path.name: load_json(path)
        for path in sorted(AUDIT_DIR.glob("*.json"))
    }


def validation_errors(
    records: dict[str, dict[str, Any]] | None = None,
    document: str | None = None,
) -> list[str]:
    if records is None:
        records = load_records()
    if document is None:
        document = DOCUMENT_PATH.read_text(encoding="utf-8")

    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []

    expected_paths = {item["path"] for item in EXPECTED.values()}
    if set(records) != expected_paths:
        errors.append(
            f"OTP-SEMANTIC-WP01: record set drift; expected {sorted(expected_paths)}, found {sorted(records)}"
        )

    seen_families: set[str] = set()
    for filename, record in records.items():
        for error in sorted(validator.iter_errors(record), key=lambda item: list(item.path)):
            errors.append(f"{filename}: {error.json_path}: {error.message}")

        family = record.get("result_family")
        if family in seen_families:
            errors.append(f"OTP-SEMANTIC-WP01: duplicate result family {family}")
        seen_families.add(str(family))
        expected = EXPECTED.get(str(family))
        if expected is None:
            errors.append(f"OTP-SEMANTIC-WP01: unexpected result family {family}")
            continue
        if filename != expected["path"]:
            errors.append(f"{filename}: path does not match result family {family}")

        lean = record.get("lean", {})
        for field, expected_value in (
            ("challenge_blob", expected["challenge_blob"]),
            ("solution_blob", expected["solution_blob"]),
            ("comparator_config_blob", expected["config_blob"]),
        ):
            if lean.get(field) != expected_value:
                errors.append(f"{filename}: exact Lean identity drift in {field}")
        if set(lean.get("theorem_names", [])) != expected["theorems"]:
            errors.append(f"{filename}: theorem target set drift")

        disposition = record.get("disposition", {})
        activation = record.get("activation", {})
        route = record.get("route_effect", {})
        if disposition.get("source_gate_before_activation") != "not_clear":
            errors.append(f"{filename}: source gate cleared before protected activation")
        if disposition.get("source_gate_after_activation") != "clear":
            errors.append(f"{filename}: protected activation does not yield bounded source clearance")
        if activation.get("head_change_requires_reapproval") is not True:
            errors.append(f"{filename}: head change does not require reapproval")
        if route.get("may_route_before_activation") is not False:
            errors.append(f"{filename}: route opened before activation")
        if route.get("aggregate_route_permitted") is not False:
            errors.append(f"{filename}: aggregate route was permitted")
        if route.get("mathcert_adjudication_authorized") is not False:
            errors.append(f"{filename}: MATHCERT adjudication was self-authorized")

        nonvacuity = record.get("nonvacuity", {})
        if nonvacuity.get("state") != "clear" or not nonvacuity.get("witness_theorems"):
            errors.append(f"{filename}: nonvacuity lacks a checked witness theorem")

        if family in {"OTP-C-PERMANENT", "OTP-H-GAPCVP"}:
            errors.append(f"{filename}: blocked repair lane cannot appear in candidate-clear tranche")

    if seen_families != set(EXPECTED):
        errors.append("OTP-SEMANTIC-WP01: tranche family set is incomplete")

    for token in (
        "OTP-F-EHRHART",
        "OTP-J1-COMPACTNESS",
        "OTP-J2-TWO-DEGENERATE",
        "candidate_clear_pending_independent_review",
        "No handoff opens on this branch",
        "Permanent",
        "GapCVP",
        "All.lean",
    ):
        if token not in document:
            errors.append(f"OTP-SEMANTIC-WP01 document: missing token {token}")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors))
        return 1
    print(
        "validated OTP-SEMANTIC-WP01 tranche-one source, Lean, Comparator, nonvacuity, activation, and route boundaries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
