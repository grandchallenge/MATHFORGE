#!/usr/bin/env python3
"""Validate OTP-C-PERMANENT bounded repair/reclassification evidence."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/repairs/OTP-C-PERMANENT/repair_manifest.json"
SCHEMA_PATH = ROOT / "schemas/openai_ten_proofs_permanent_repair_manifest.schema.json"
MATRIX_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/theorem_intake_matrix.json"

EXPECTED_BOUNDARY = "PERMANENT_FORMULA_LOWER_BOUNDS_ONLY__CIRCUIT_THEOREM_NOT_ENCODED"
EXPECTED_BASE = "5b463c09f984fb5a821882e62de27324e7c51d19"
EXPECTED_ROOT = "e62211d28e3a9131950c89caa6542cfe5eff3bca"
EXPECTED_TREE = "2f8e7ac5ae7f157b6b1de636c2c343b1c7a7e365"
EXPECTED_ARCHIVE = "3022e62ffbed8f5f74d232034a703dc645e6b301879dff1e87df72979914294f"
EXPECTED_MATRIX_BLOB = "2d8b24c32c804c4f5ca0f5f5ad1185199d35664b"
EXPECTED_MANUSCRIPT = "f318c6508c9d49ef876a5a26cd73928705f96c07bb43e92a0cb35bd3f666ea53"
EXPECTED_TARGETS = [
    "PermanentFormulaLowerBound.permanent_divisionFree_formula_logarithmic_lower_bound",
    "PermanentFormulaLowerBound.permanent_rational_formula_logarithmic_lower_bound",
]
EXPECTED_CLAIMS = {
    "OTP-C-PERMANENT-CIRCUIT": {
        "theorem": "Theorem 1.1",
        "claim_class": "arithmetic_circuit_lower_bound",
        "encoded_target_status": "absent",
        "encoded_target": None,
        "dimension_domain": "n >= 2^16",
        "coverage": False,
    },
    "OTP-C-PERMANENT-DIVISION-FREE-FORMULA": {
        "theorem": "Theorem 1.2",
        "claim_class": "division_free_formula_lower_bound",
        "encoded_target_status": "present_conditional",
        "encoded_target": EXPECTED_TARGETS[0],
        "dimension_domain": "n >= 32",
        "coverage": True,
    },
    "OTP-C-PERMANENT-RATIONAL-FORMULA": {
        "theorem": "Theorem 1.3",
        "claim_class": "rational_formula_lower_bound",
        "encoded_target_status": "present_conditional",
        "encoded_target": EXPECTED_TARGETS[1],
        "dimension_domain": "n >= 32",
        "coverage": True,
    },
}
REQUIRED_HYPOTHESIS_MARKERS = {
    "OTP-C-PERMANENT-DIVISION-FREE-FORMULA": [
        "32 <= n",
        "Formula (Fin n × Fin n) ℂ",
        "Formula.eval f = permanentPolynomial n",
    ],
    "OTP-C-PERMANENT-RATIONAL-FORMULA": [
        "32 <= n",
        "RationalFormula (Fin n × Fin n) ℂ",
        "RationalFormula.Valid f",
        "RationalFormula.eval f =",
    ],
}
EXPECTED_ROUTE_CONTROLS = {
    "semantic_clearance_authorized": False,
    "solve_handoff_authorized": False,
    "cert_route_authorized": False,
    "mathcert_adjudication_authorized": False,
    "cert_output_authorized": False,
    "aggregate_authority_permitted": False,
    "mathematical_target_proved": False,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(
        f"blob {len(data)}\0".encode("ascii") + data,
        usedforsecurity=False,
    ).hexdigest()


def validation_errors(
    manifest: dict[str, Any] | None = None,
    matrix: dict[str, Any] | None = None,
    matrix_blob: str | None = None,
) -> list[str]:
    errors: list[str] = []
    manifest = load_json(MANIFEST_PATH) if manifest is None else manifest
    schema = load_json(SCHEMA_PATH)

    for error in sorted(
        Draft202012Validator(schema).iter_errors(manifest),
        key=lambda e: list(e.path),
    ):
        errors.append(f"repair schema: {error.json_path}: {error.message}")

    if manifest.get("result_family") != "OTP-C-PERMANENT":
        errors.append("another result family inserted")
    if manifest.get("repair_strategy") != "bounded_reclassification":
        errors.append("repair strategy drift")
    if manifest.get("proposed_family_boundary") != EXPECTED_BOUNDARY:
        errors.append("family boundary drift")

    authority = manifest.get("authority", {})
    expected_authority = {
        "implementation_base": EXPECTED_BASE,
        "official_lean_root": EXPECTED_ROOT,
        "official_lean_tree": EXPECTED_TREE,
        "deterministic_archive_sha256": EXPECTED_ARCHIVE,
    }
    for key, value in expected_authority.items():
        if authority.get(key) != value:
            errors.append(f"authority identity drift: {key}")
    if authority.get("tracker_issue") != "https://github.com/grandchallenge/MATHFORGE/issues/59":
        errors.append("tracker authority drift")
    if authority.get("diagnostic_comment_id") != 5291141426:
        errors.append("diagnostic authority drift")
    if authority.get("activation_comment_id") != 5291306737:
        errors.append("activation authority drift")
    if authority.get("theorem_intake_matrix") != {
        "path": "sources/OPENAI-TEN-PROOFS-001/theorem_intake_matrix.json",
        "git_blob_sha1": EXPECTED_MATRIX_BLOB,
    }:
        errors.append("theorem intake matrix reference drift")
    if authority.get("admitted_manuscript") != {
        "sha256": EXPECTED_MANUSCRIPT,
        "byte_length": 2266052,
    }:
        errors.append("admitted manuscript identity drift")

    observation = manifest.get("non_authoritative_current_upstream_observation", {})
    if observation.get("repins_protected_authority") is not False:
        errors.append("current upstream observation promoted to protected authority")
    if observation.get("repository") != "openai/ten-proofs":
        errors.append("upstream observation repository drift")
    if observation.get("observed_head") != "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6":
        errors.append("upstream observation head drift")

    claims = manifest.get("advertised_claims", [])
    claim_map = {
        item.get("claim_id"): item
        for item in claims
        if isinstance(item, dict)
    }
    if len(claims) != 3 or set(claim_map) != set(EXPECTED_CLAIMS):
        errors.append("advertised claim inventory drift")
    for claim_id, expected in EXPECTED_CLAIMS.items():
        item = claim_map.get(claim_id)
        if not isinstance(item, dict):
            continue
        if item.get("source_locus") != {"chapter": 5, "theorem": expected["theorem"]}:
            errors.append(f"{claim_id}: source theorem locus drift")
        if item.get("claim_class") != expected["claim_class"]:
            errors.append(f"{claim_id}: claim class substitution")
        if item.get("encoded_target_status") != expected["encoded_target_status"]:
            errors.append(f"{claim_id}: encoded target status drift")
        if item.get("encoded_target") != expected["encoded_target"]:
            errors.append(f"{claim_id}: encoded target substitution")
        if item.get("dimension_domain") != expected["dimension_domain"]:
            errors.append(f"{claim_id}: asymptotic/dimension domain drift")
        if item.get("representation_premise_required") is not True:
            errors.append(f"{claim_id}: representation conditionality removed")
        if item.get("coverage_after_reclassification") is not expected["coverage"]:
            errors.append(f"{claim_id}: reclassification coverage drift")

        markers = REQUIRED_HYPOTHESIS_MARKERS.get(claim_id)
        if markers:
            hypotheses = "\n".join(item.get("required_hypotheses", []))
            for marker in markers:
                if marker not in hypotheses:
                    errors.append(f"{claim_id}: required condition removed: {marker}")

    inventory = manifest.get("encoded_target_inventory", {})
    if inventory.get("comparator_config") != "ComparatorChallenges/C_PermanentFormulaLowerBound.json":
        errors.append("Comparator config substitution")
    if inventory.get("solution_module") != "Permanent":
        errors.append("solution module substitution")
    if inventory.get("targets") != EXPECTED_TARGETS:
        errors.append("encoded Permanent target inventory drift")
    if inventory.get("target_count") != 2:
        errors.append("target-count inflation or deletion")
    if inventory.get("circuit_target_count") != 0:
        errors.append("invented circuit target coverage")

    coverage = manifest.get("coverage_disposition", {})
    expected_coverage = {
        "advertised_claim_count": 3,
        "encoded_formula_target_count": 2,
        "encoded_circuit_target_count": 0,
        "formula_targets_conditional": True,
        "targets_construct_representing_formula": False,
        "circuit_lower_bound_coverage": False,
        "may_advertise_circuit_lower_bound_coverage": False,
        "reclassified_advertised_result": "Permanent formula lower bounds only",
        "repair_outcome": "restricted_family_reclassification_candidate",
    }
    if coverage != expected_coverage:
        errors.append("coverage disposition drift or promotion")
    if manifest.get("route_controls") != EXPECTED_ROUTE_CONTROLS:
        errors.append("route, adjudication, aggregate, or proof authority inserted")

    acceptance = manifest.get("acceptance_criteria", {})
    if not all(value is True for value in acceptance.values()):
        errors.append("repair acceptance criterion weakened")
    activation = manifest.get("activation", {})
    required_gates = {
        "exact-head Forge checks",
        "GCL conformance",
        "non-author complexity/algebra specialist APPROVED review",
        "separate Human Steward exact-head disposition",
    }
    if set(activation.get("required_before_protected_merge", [])) != required_gates:
        errors.append("protected merge gate drift")
    if activation.get("head_change_requires_reapproval") is not True:
        errors.append("head-change reapproval disabled")

    matrix = load_json(MATRIX_PATH) if matrix is None else matrix
    matrix_blob = git_blob_sha1(MATRIX_PATH) if matrix_blob is None else matrix_blob
    if matrix_blob != EXPECTED_MATRIX_BLOB:
        errors.append("protected theorem-intake matrix blob drift")
    source = matrix.get("source_identity", {})
    if source.get("current_official_root") != EXPECTED_ROOT:
        errors.append("matrix official Lean root drift")
    if source.get("current_tree") != EXPECTED_TREE:
        errors.append("matrix official Lean tree drift")
    if source.get("deterministic_archive_sha256") != EXPECTED_ARCHIVE:
        errors.append("matrix official archive drift")
    if source.get("official_manuscript", {}).get("sha256") != EXPECTED_MANUSCRIPT:
        errors.append("matrix admitted manuscript drift")

    family_rows = [
        item for item in matrix.get("result_families", [])
        if isinstance(item, dict) and item.get("result_id") == "OTP-C-PERMANENT"
    ]
    if len(family_rows) != 1:
        errors.append("matrix Permanent family membership drift")
    else:
        row = family_rows[0]
        if row.get("comparator_config") != "ComparatorChallenges/C_PermanentFormulaLowerBound.json":
            errors.append("matrix Permanent comparator drift")
        if row.get("solution_module") != "Permanent":
            errors.append("matrix Permanent solution-module drift")
        if row.get("theorem_names") != EXPECTED_TARGETS:
            errors.append("matrix Permanent encoded-target drift")
        if row.get("replay_gate") != "clear":
            errors.append("matrix replay observation drift")
        if row.get("source_gate") != "blocked":
            errors.append("matrix Permanent source blocker removed")
        if row.get("may_route_to_solve") is not False:
            errors.append("matrix Permanent route prohibition removed")
        relation = str(row.get("source_statement_relation", ""))
        if "circuit lower bound is absent" not in relation:
            errors.append("matrix missing-circuit diagnosis lost")
        nonvacuity = str(row.get("nonvacuity_status", ""))
        if "conditional on a formula representing the permanent" not in nonvacuity:
            errors.append("matrix formula conditionality diagnosis lost")

    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"Permanent repair validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(
        "validated OTP-C-PERMANENT bounded reclassification candidate: "
        "two conditional formula targets retained; circuit lower-bound coverage remains false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
