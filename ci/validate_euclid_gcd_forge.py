#!/usr/bin/env python3
"""Fail-closed validator for the EUCLID-GCD-E2E-001 Forge package."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_PATH = ROOT / "sources" / "EUCLID-GCD-E2E-001" / "forge_package.json"
SCHEMA_PATH = ROOT / "schemas" / "euclid_gcd_forge_package.schema.json"

REQUIRED_RISKS = {f"EGR-{index:03d}" for index in range(1, 11)}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def semantic_errors(package: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(package, dict):
        return ["package must be an object"]

    problem = package.get("problem_card", {})
    contract = problem.get("input_contract", {}) if isinstance(problem, dict) else {}
    if "a = 0 and b = 0" not in contract.get("excluded", []):
        errors.append("unsupported (0,0) case must remain excluded")
    normalized = str(problem.get("normalized_statement", ""))
    if "not both zero" not in normalized:
        errors.append("normalized statement must retain the not-both-zero precondition")

    sources = package.get("source_map", [])
    pending = next(
        (item for item in sources if isinstance(item, dict) and item.get("source_id") == "EUCLID-BOOK-VII-CONTEXT-PENDING"),
        None,
    )
    if pending is None or pending.get("status") != "deferred_pending_exact_source_lock":
        errors.append("historical context must remain deferred pending exact source lock")
    if pending and "does not support attribution" not in str(pending.get("support_scope", "")):
        errors.append("historical source record must prohibit unsupported modern attribution")

    ledger = package.get("reconnaissance_ledger", {})
    instance = ledger.get("instance", {}) if isinstance(ledger, dict) else {}
    if instance != {"a": 252, "b": 105, "candidate_d": 21}:
        errors.append("canonical instance must remain exactly (252,105,21)")
    trace = ledger.get("euclidean_trace", []) if isinstance(ledger, dict) else []
    expected_links = [(252, 105), (105, 42), (42, 21)]
    if len(trace) != 3:
        errors.append("canonical trace must contain exactly three steps")
    else:
        for index, step in enumerate(trace):
            if not isinstance(step, dict):
                errors.append(f"trace step {index} must be an object")
                continue
            dividend = step.get("dividend")
            divisor = step.get("divisor")
            quotient = step.get("quotient")
            remainder = step.get("remainder")
            if (dividend, divisor) != expected_links[index]:
                errors.append(f"trace step {index} input linkage drifted")
            if not all(isinstance(value, int) for value in (dividend, divisor, quotient, remainder)):
                errors.append(f"trace step {index} fields must be integers")
                continue
            if dividend != quotient * divisor + remainder:
                errors.append(f"trace step {index} division equation is false")
            if remainder < 0 or remainder >= divisor:
                errors.append(f"trace step {index} remainder bound is false")
            if index < 2 and remainder <= 0:
                errors.append(f"trace step {index} must have a positive remainder")
            if index == 2 and remainder != 0:
                errors.append("terminal trace step must end in zero")
        if trace[1].get("dividend") != trace[0].get("divisor") or trace[1].get("divisor") != trace[0].get("remainder"):
            errors.append("trace step 1 does not continue step 0")
        if trace[2].get("dividend") != trace[1].get("divisor") or trace[2].get("divisor") != trace[1].get("remainder"):
            errors.append("trace step 2 does not continue step 1")

    witness = ledger.get("bezout_witness", {}) if isinstance(ledger, dict) else {}
    x, y = witness.get("x"), witness.get("y")
    if not isinstance(x, int) or not isinstance(y, int) or x * 252 + y * 105 != 21:
        errors.append("Bézout witness does not establish -2*252 + 5*105 = 21")
    if ledger.get("theorem_effect") != "none_until_independent_check_and_formal_certification":
        errors.append("candidate computation must not acquire theorem effect in Forge")

    risks = package.get("failure_risks", [])
    risk_ids = {item.get("risk_id") for item in risks if isinstance(item, dict)}
    if risk_ids != REQUIRED_RISKS:
        errors.append("failure-risk ledger must contain exactly EGR-001 through EGR-010")

    handoff = package.get("solve_handoff", {})
    if handoff.get("state") != "candidate_pending_protected_forge_merge":
        errors.append("Solve handoff must remain candidate pending protected Forge merge")
    if handoff.get("inputs") != {"a": 252, "b": 105}:
        errors.append("Solve handoff input drift")
    if handoff.get("required_output", {}).get("authority_state") != "candidate_only":
        errors.append("Solve output authority must remain candidate_only")

    boundary = package.get("claim_boundary", {})
    for key in (
        "certifies_mathematics",
        "certifies_candidate_witness",
        "claims_novelty",
        "claims_priority",
        "claims_historical_verbatim_equivalence",
    ):
        if boundary.get(key) is not False:
            errors.append(f"claim boundary {key} must be false")

    documentary = package.get("chaidez_documentary_contract", {})
    expected_sequence = [
        "source_lock",
        "historical_modern_concordance",
        "semantic_web_reader",
        "edition_record_and_native_plates",
        "atomic_manifest_admission",
    ]
    if documentary.get("edition_sequence") != expected_sequence:
        errors.append("Chaidez documentary sequence drifted")
    if documentary.get("pedagogical_only_surfaces") != ["future illuminated plates"]:
        errors.append("illuminated plates must remain pedagogical only")

    return errors


def validate_package(package: Any, schema: Any) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(package), key=lambda item: list(item.path))
    ]
    errors.extend(semantic_errors(package))
    return errors


def main() -> int:
    package = load_json(PACKAGE_PATH)
    schema = load_json(SCHEMA_PATH)
    errors = validate_package(package, schema)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"EUCLID-GCD-E2E-001 Forge validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("EUCLID-GCD-E2E-001 Forge package, candidate trace, handoff boundary, and Chaidez sequence are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
