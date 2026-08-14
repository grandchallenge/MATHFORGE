#!/usr/bin/env python3
"""Validate the cleared OTP-C-PERMANENT fresh family replay."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/replays/OTP-C-PERMANENT/replay_record.json"
SCHEMA_PATH = ROOT / "schemas/openai_ten_proofs_permanent_replay_record.schema.json"
REPAIR_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/repairs/OTP-C-PERMANENT/repair_manifest.json"

EXPECTED_ROOT = "e62211d28e3a9131950c89caa6542cfe5eff3bca"
EXPECTED_TREE = "2f8e7ac5ae7f157b6b1de636c2c343b1c7a7e365"
EXPECTED_ARCHIVE = "3022e62ffbed8f5f74d232034a703dc645e6b301879dff1e87df72979914294f"
EXPECTED_BOUNDARY = "PERMANENT_FORMULA_LOWER_BOUNDS_ONLY__CIRCUIT_THEOREM_NOT_ENCODED"
EXPECTED_TARGETS = [
    "PermanentFormulaLowerBound.permanent_divisionFree_formula_logarithmic_lower_bound",
    "PermanentFormulaLowerBound.permanent_rational_formula_logarithmic_lower_bound",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record: dict[str, Any] | None = None, repair: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    record = load_json(RECORD_PATH) if record is None else record
    repair = load_json(REPAIR_PATH) if repair is None else repair
    schema = load_json(SCHEMA_PATH)

    for error in sorted(Draft202012Validator(schema).iter_errors(record), key=lambda e: list(e.path)):
        errors.append(f"replay schema: {error.json_path}: {error.message}")

    predecessor = record.get("predecessor", {})
    protected = record.get("protected_source", {})
    prior = record.get("prior_failed_reacquisition", {})
    carrier = record.get("source_carrier", {})
    replay = record.get("successful_replay", {})
    inventory = replay.get("target_inventory", {})
    disposition = record.get("disposition", {})
    routes = record.get("route_controls", {})

    if predecessor.get("family_boundary") != EXPECTED_BOUNDARY:
        errors.append("replay predecessor boundary drift")
    if protected.get("historical_commit") != EXPECTED_ROOT:
        errors.append("protected historical root drift")
    if protected.get("tree") != EXPECTED_TREE:
        errors.append("protected tree drift")
    if protected.get("deterministic_archive_sha256") != EXPECTED_ARCHIVE:
        errors.append("protected archive drift")
    if protected.get("later_upstream_revision_substituted") is not False:
        errors.append("later upstream revision substituted")

    if prior.get("superseded_by_content_addressed_reassertion") is not True:
        errors.append("prior reacquisition blocker not explicitly superseded")
    if prior.get("compiler_or_theorem_failure_inferred") is not False:
        errors.append("prior source-fetch failure promoted to compiler/theorem failure")

    if carrier.get("repository") != "grandchallenge/MATHFORGE":
        errors.append("replay source carrier is not GCL-controlled")
    if carrier.get("immutable") is not True:
        errors.append("replay source carrier is mutable")
    if carrier.get("asset_digest") != f"sha256:{EXPECTED_ARCHIVE}":
        errors.append("GCL archival carrier digest drift")
    if carrier.get("content_identity_matches_protected_source") is not True:
        errors.append("GCL carrier not bound to protected content identity")

    required_success = (
        "archive_download_verified",
        "permanent_family_file_identities_verified",
        "comparator_inventory_verified",
        "locked_dependency_cache_fetched",
        "permanent_solution_module_built",
        "permanent_challenge_elaborated",
        "clearance_marker_emitted",
    )
    for key in required_success:
        if replay.get(key) is not True:
            errors.append(f"required replay stage not clear: {key}")
    if replay.get("lean_toolchain") != "leanprover/lean4:v4.32.0":
        errors.append("Lean toolchain drift")
    if inventory.get("targets") != EXPECTED_TARGETS or inventory.get("target_count") != 2:
        errors.append("Permanent Comparator target inventory drift")
    if inventory.get("circuit_target_count") != 0:
        errors.append("circuit target inserted into replay")
    if inventory.get("formula_targets_conditional") is not True:
        errors.append("formula target conditionality lost")

    if disposition.get("state") != "FRESH_FAMILY_REPLAY_CLEAR__SEMANTIC_AUDIT_NOT_YET_PERFORMED":
        errors.append("replay disposition drift")
    if disposition.get("fresh_family_replay_clear") is not True:
        errors.append("fresh family replay not clear")
    if disposition.get("source_reacquisition_blocker_cleared") is not True:
        errors.append("source reacquisition blocker not cleared")
    if disposition.get("semantic_nonvacuity_audit_may_be_governed_next") is not True:
        errors.append("next governed semantic audit lane not exposed")
    if disposition.get("semantic_nonvacuity_audit_performed") is not False:
        errors.append("semantic audit falsely represented as performed")

    for key, value in routes.items():
        if value is not False:
            errors.append(f"downstream authority inflated: {key}")

    if repair.get("proposed_family_boundary") != EXPECTED_BOUNDARY:
        errors.append("protected repair boundary mismatch")
    authority = repair.get("authority", {})
    if authority.get("official_lean_root") != EXPECTED_ROOT or authority.get("official_lean_tree") != EXPECTED_TREE:
        errors.append("repair/replay protected source identity mismatch")
    coverage = repair.get("coverage_disposition", {})
    if coverage.get("encoded_formula_target_count") != 2 or coverage.get("encoded_circuit_target_count") != 0:
        errors.append("protected repair target inventory drift")
    if coverage.get("circuit_lower_bound_coverage") is not False:
        errors.append("protected repair circuit coverage inflated")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated OTP-C-PERMANENT fresh family replay clear from exact GCL archival carrier; semantic/nonvacuity audit remains unperformed and unauthorized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
