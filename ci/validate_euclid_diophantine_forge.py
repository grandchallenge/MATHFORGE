#!/usr/bin/env python3
"""Fail-closed validator for the EUCLID-DIOPHANTINE-E2E-002 Forge package."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_PATH = ROOT / "sources" / "EUCLID-DIOPHANTINE-E2E-002" / "forge_package.json"
SCHEMA_PATH = ROOT / "schemas" / "euclid_diophantine_forge_package.schema.json"
REQUIRED_RISKS = {f"DIO-{index:03d}" for index in range(1, 11)}
EXPECTED_COMMITS = {
    "forge": "3622bac82a39cdb9e82ec463919d9e6927c1ec0e",
    "solve": "3a8493aa322f0e640c921b8824c4d7f88a8c057d",
    "cert": "78b69e6a3461a83f4893d61c421b1570c08a9ba6",
    "programme": "183ff2a0adfbe5bd0ffd5f2e638089b94b868c54",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def semantic_errors(package: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(package, dict):
        return ["package must be an object"]

    problem = package.get("problem_card", {})
    statement = str(problem.get("normalized_statement", ""))
    if "(a,b) != (0,0)" not in statement:
        errors.append("normalized statement must retain the not-both-zero precondition")
    if "gcd(|a|,|b|) divides |c|" not in statement:
        errors.append("normalized statement must retain absolute-value gcd divisibility")
    contract = problem.get("input_contract", {})
    if contract.get("excluded") != ["a = 0 and b = 0"]:
        errors.append("only the exact (0,0) coefficient case must remain excluded")
    if "x = 0 and y = 0" not in str(contract.get("zero_target_policy", "")):
        errors.append("zero-target solution policy must remain explicit")

    reuse = package.get("protected_stage1_reuse", {})
    for key, expected in EXPECTED_COMMITS.items():
        if reuse.get(key, {}).get("merge_commit") != expected:
            errors.append(f"protected Stage 1 {key} merge identity drifted")
    policy = str(reuse.get("reuse_policy", ""))
    if "do not introduce a competing gcd definition" not in policy:
        errors.append("Stage 1 reuse policy must prohibit competing gcd definitions")

    sources = package.get("source_map", [])
    pending = next((item for item in sources if isinstance(item, dict) and item.get("source_id") == "EUCLID-BOOK-VII-CONTEXT-PENDING"), None)
    if pending is None or pending.get("status") != "deferred_pending_exact_source_lock":
        errors.append("historical context must remain deferred pending exact source lock")
    if pending and "does not support verbatim attribution" not in str(pending.get("support_scope", "")):
        errors.append("historical source record must prohibit verbatim modern attribution")

    ledger = package.get("reconnaissance_ledger", {})
    positive = ledger.get("positive_exemplar", {})
    if positive.get("inputs") != {"a": 252, "b": 105, "c": 84}:
        errors.append("positive exemplar inputs drifted")
    if positive.get("protected_gcd") != 21 or positive.get("scale_factor") != 4:
        errors.append("positive exemplar gcd or scale factor drifted")
    base = positive.get("protected_bezout", {})
    solution = positive.get("candidate_solution", {})
    if (base.get("x"), base.get("y")) != (-2, 5):
        errors.append("protected Bézout coefficients drifted")
    if (solution.get("x"), solution.get("y")) != (-8, 20):
        errors.append("scaled constructive witness drifted")
    if solution.get("x") * 252 + solution.get("y") * 105 != 84:
        errors.append("constructive witness equation is false")
    if solution.get("x") != positive.get("scale_factor") * base.get("x") or solution.get("y") != positive.get("scale_factor") * base.get("y"):
        errors.append("constructive witness is not the recorded scale of the protected witness")
    divisibility = positive.get("divisibility", {})
    if divisibility != {"absolute_target": 84, "quotient": 4, "remainder": 0}:
        errors.append("positive divisibility record drifted")

    negative = ledger.get("negative_exemplar", {})
    if negative.get("inputs") != {"a": 252, "b": 105, "c": 20} or negative.get("protected_gcd") != 21:
        errors.append("negative exemplar inputs or gcd drifted")
    obstruction = negative.get("divisibility_obstruction", {})
    q, r = obstruction.get("quotient"), obstruction.get("remainder")
    if not isinstance(q, int) or not isinstance(r, int) or 20 != q * 21 + r:
        errors.append("negative quotient-remainder equation is false")
    if not isinstance(r, int) or not 0 < r < 21:
        errors.append("negative obstruction remainder must satisfy 0 < r < d")
    if ledger.get("theorem_effect") != "none_until_independent_check_and_formal_certification":
        errors.append("Forge reconnaissance must retain no theorem effect")

    risk_ids = {item.get("risk_id") for item in package.get("failure_risks", []) if isinstance(item, dict)}
    if risk_ids != REQUIRED_RISKS:
        errors.append("failure-risk ledger must contain exactly DIO-001 through DIO-010")

    handoff = package.get("solve_handoff", {})
    if handoff.get("target_issue") != 103 or handoff.get("state") != "candidate_pending_protected_forge_merge":
        errors.append("Solve handoff issue or state drifted")
    if handoff.get("required_output", {}).get("authority_state") != "candidate_only":
        errors.append("Solve output authority must remain candidate_only")
    forbidden = set(handoff.get("forbidden_claims", []))
    if "unsatisfiable because search failed" not in forbidden:
        errors.append("timeout or failed search must not be accepted as unsatisfiability")
    cases = handoff.get("cases", [])
    expected_cases = {
        "DIO-POS-252-105-84": ({"a": 252, "b": 105, "c": 84}, "constructive_solution"),
        "DIO-NEG-252-105-20": ({"a": 252, "b": 105, "c": 20}, "divisibility_obstruction"),
    }
    actual_cases = {item.get("case_id"): (item.get("inputs"), item.get("required_evidence")) for item in cases if isinstance(item, dict)}
    if actual_cases != expected_cases:
        errors.append("Solve handoff cases drifted")

    cert = package.get("certification_route_sketch", {})
    if cert.get("issue") != 89 or "must not import or execute" not in str(cert.get("independence_requirement", "")):
        errors.append("independent certification route drifted")

    boundary = package.get("claim_boundary", {})
    for key in (
        "certifies_mathematics", "certifies_constructive_witness", "certifies_unsatisfiable_obstruction",
        "claims_arbitrary_diophantine_completeness", "claims_novelty", "claims_priority",
        "claims_historical_verbatim_equivalence",
    ):
        if boundary.get(key) is not False:
            errors.append(f"claim boundary {key} must be false")

    expected_sequence = ["source_lock", "historical_modern_concordance", "semantic_web_reader", "edition_record_and_native_plates", "atomic_manifest_admission"]
    documentary = package.get("chaidez_documentary_contract", {})
    if documentary.get("edition_sequence") != expected_sequence:
        errors.append("Chaidez documentary sequence drifted")
    if documentary.get("pedagogical_only_surfaces") != ["future illuminated plates"]:
        errors.append("illuminated plates must remain pedagogical only")
    return errors


def validate_package(package: Any, schema: Any) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [f"{error.json_path}: {error.message}" for error in sorted(validator.iter_errors(package), key=lambda item: list(item.path))]
    errors.extend(semantic_errors(package))
    return errors


def main() -> int:
    errors = validate_package(load_json(PACKAGE_PATH), load_json(SCHEMA_PATH))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"EUCLID-DIOPHANTINE-E2E-002 Forge validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("EUCLID-DIOPHANTINE-E2E-002 theorem lock, Stage 1 reuse, exemplars, handoff boundary, and Chaidez sequence are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
