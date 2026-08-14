#!/usr/bin/env python3
"""Validate the characterized OTP-C-PERMANENT replay blocker."""
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
EXPECTED_ERROR = f"fatal: remote error: upload-pack: not our ref {EXPECTED_ROOT}"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(
    record: dict[str, Any] | None = None,
    repair: dict[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []
    record = load_json(RECORD_PATH) if record is None else record
    repair = load_json(REPAIR_PATH) if repair is None else repair
    schema = load_json(SCHEMA_PATH)

    for error in sorted(
        Draft202012Validator(schema).iter_errors(record),
        key=lambda e: list(e.path),
    ):
        errors.append(f"replay schema: {error.json_path}: {error.message}")

    predecessor = record.get("predecessor", {})
    protected = record.get("protected_source", {})
    reassert = protected.get("archival_reassertion_policy", {})
    attempt = record.get("attempt", {})
    audit = record.get("reacquisition_audit", {})
    disposition = record.get("disposition", {})
    routes = record.get("route_controls", {})

    if predecessor.get("family_boundary") != EXPECTED_BOUNDARY:
        errors.append("replay predecessor boundary drift")
    if protected.get("commit") != EXPECTED_ROOT:
        errors.append("protected historical replay root drift")
    if protected.get("tree") != EXPECTED_TREE:
        errors.append("protected replay tree drift")
    if protected.get("deterministic_archive_sha256") != EXPECTED_ARCHIVE:
        errors.append("protected replay archive drift")
    if protected.get("silent_repin_permitted") is not False:
        errors.append("silent upstream repin enabled")

    expected_reassert = {
        "permitted": True,
        "new_carrier_commit_identity_permitted": True,
        "historical_provenance_must_be_preserved": True,
        "protected_tree_must_match": True,
        "deterministic_archive_sha256_must_match": True,
        "later_upstream_revision_substitution_permitted": False,
    }
    if reassert != expected_reassert:
        errors.append("archival reassertion policy drift")

    if attempt.get("fetch_attempt_count") != 3:
        errors.append("fetch attempt count drift")
    if attempt.get("fetch_result") != "failure":
        errors.append("failed source reacquisition represented as success")
    if attempt.get("fetch_error") != EXPECTED_ERROR:
        errors.append("source fetch diagnostic drift")
    for key in (
        "source_checkout_completed",
        "toolchain_install_reached",
        "solution_build_reached",
        "challenge_elaboration_reached",
    ):
        if attempt.get(key) is not False:
            errors.append(f"replay stage falsely promoted: {key}")

    if audit.get("retained_deterministic_archive_bytes_found") is not False:
        errors.append("unretained archive represented as recovered")
    if audit.get("later_upstream_head_substituted") is not False:
        errors.append("later upstream substitution recorded")

    if disposition.get("state") != "OPEN_WITH_CHARACTERIZED_REPLAY_BLOCKER":
        errors.append("replay blocker state drift")
    if disposition.get("blocker_class") != "protected_source_bitset_reacquisition":
        errors.append("replay blocker class drift")
    if disposition.get("fresh_family_replay_clear") is not False:
        errors.append("fresh replay falsely cleared")
    if disposition.get("source_reassertion_operation_may_begin") is not True:
        errors.append("content-addressed source reassertion improperly closed")
    if disposition.get("semantic_audit_may_begin") is not False:
        errors.append("semantic audit opened before replay clearance")

    expected_route_keys = {
        "source_reassertion_authorized",
        "semantic_clearance_authorized",
        "semantic_nonvacuity_audit_authorized",
        "solve_handoff_authorized",
        "cert_route_authorized",
        "mathcert_adjudication_authorized",
        "cert_output_authorized",
        "mathematical_target_proved",
        "aggregate_authority_permitted",
    }
    if set(routes) != expected_route_keys:
        errors.append("replay route-control key set drift")
    if routes.get("source_reassertion_authorized") is not True:
        errors.append("content-addressed source reassertion authority removed")
    for key in expected_route_keys - {"source_reassertion_authorized"}:
        if routes.get(key) is not False:
            errors.append(f"replay route or claim authority inflated: {key}")

    requirements = record.get("reopening_requirements", [])
    if len(requirements) != 5:
        errors.append("reopening requirement count drift")
    joined = "\n".join(requirements)
    for marker in (EXPECTED_ROOT, EXPECTED_TREE, EXPECTED_ARCHIVE, "GCL-controlled archival carrier", "later upstream revision"):
        if marker not in joined:
            errors.append(f"reopening requirements missing marker: {marker}")

    if repair.get("proposed_family_boundary") != EXPECTED_BOUNDARY:
        errors.append("protected repair boundary no longer matches replay record")
    if repair.get("authority", {}).get("official_lean_root") != EXPECTED_ROOT:
        errors.append("repair/replay historical root identity mismatch")
    if repair.get("authority", {}).get("official_lean_tree") != EXPECTED_TREE:
        errors.append("repair/replay tree identity mismatch")
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
        print(f"Permanent replay validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(
        "validated OTP-C-PERMANENT protected-bitset reacquisition blocker; "
        "content-addressed archival reassertion is allowed, fresh replay and semantic/nonvacuity audit remain closed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
