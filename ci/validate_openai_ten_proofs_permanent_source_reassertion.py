#!/usr/bin/env python3
"""Validate OTP-C-PERMANENT content-addressed source reassertion evidence."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/reassertions/OTP-C-PERMANENT/source_reassertion_record.json"
SCHEMA_PATH = ROOT / "schemas/openai_ten_proofs_permanent_source_reassertion_record.schema.json"
REPAIR_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/repairs/OTP-C-PERMANENT/repair_manifest.json"

EXPECTED_COMMIT = "e62211d28e3a9131950c89caa6542cfe5eff3bca"
EXPECTED_TREE = "2f8e7ac5ae7f157b6b1de636c2c343b1c7a7e365"
EXPECTED_ARCHIVE = "3022e62ffbed8f5f74d232034a703dc645e6b301879dff1e87df72979914294f"
EXPECTED_BOUNDARY = "PERMANENT_FORMULA_LOWER_BOUNDS_ONLY__CIRCUIT_THEOREM_NOT_ENCODED"
EXPECTED_FILES = {
    "Permanent.lean": ("11cc89429a7c630688d1510c9a6600fde08ab0b0", "3bd469c20bc2277a13be3f9353ce47ad0c2070a330355daa78a9e59f1ca1d3c6"),
    "ComparatorChallenges/C_PermanentFormulaLowerBound.lean": ("ca71c280479f12a4249b0dc63b6e1af27bdb32ff", "fc97578bcbb072ff82383e4c903107130ba3dd1a2209235ab32270c7df37f83d"),
    "ComparatorChallenges/C_PermanentFormulaLowerBound.json": ("662595032dced7ea0bb4d0ee43c3b1d20ecb4c2b", "f80482f4a163041e036e26bb687690559cc36504e347b0ea3df0d626cfb965bb"),
    "lean-toolchain": ("94b9f495baff80fd9cb44aad8f4762cb3b2066fe", "2773c517aa90b66ea8a2c52bddddf84393157797f8341be0df45294fff7fd32e"),
    "lake-manifest.json": ("6b9fc4f8f8f7fc389016af602b459ea916e52904", "a6faf8302fe77f77f499446c27b8829b1af8dbc7847298b682556baa2a0b135e"),
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record: dict[str, Any] | None = None, repair: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    record = load_json(RECORD_PATH) if record is None else record
    repair = load_json(REPAIR_PATH) if repair is None else repair
    schema = load_json(SCHEMA_PATH)

    for error in sorted(Draft202012Validator(schema).iter_errors(record), key=lambda e: list(e.path)):
        errors.append(f"source reassertion schema: {error.json_path}: {error.message}")

    provenance = record.get("historical_provenance", {})
    recovery = record.get("recovery_source", {})
    verification = record.get("verification", {})
    carrier = record.get("gcl_archival_carrier", {})
    routes = record.get("route_controls", {})

    if provenance.get("commit") != EXPECTED_COMMIT:
        errors.append("historical commit drift")
    if provenance.get("tree") != EXPECTED_TREE:
        errors.append("historical tree drift")
    if provenance.get("deterministic_archive_sha256") != EXPECTED_ARCHIVE:
        errors.append("historical archive digest drift")
    if recovery.get("retrieved_commit") != EXPECTED_COMMIT or recovery.get("retrieved_tree") != EXPECTED_TREE:
        errors.append("recovery source content identity drift")
    if recovery.get("authority_basis") != "content_addressed_identity_only" or recovery.get("mirror_name_creates_authority") is not False:
        errors.append("recovery mirror promoted to provenance authority")

    if verification.get("commit_match") is not True or verification.get("tree_match") is not True or verification.get("archive_match") is not True:
        errors.append("content identity verification is not fully clear")
    if verification.get("archive_sha256") != EXPECTED_ARCHIVE:
        errors.append("reconstructed archive mismatch")

    files = record.get("permanent_family_files", [])
    observed = {item.get("path"): (item.get("git_blob_sha1"), item.get("sha256")) for item in files}
    if observed != EXPECTED_FILES:
        errors.append("Permanent-family file identity inventory drift")

    source_asset = carrier.get("source_asset", {})
    if carrier.get("repository") != "grandchallenge/MATHFORGE":
        errors.append("archival carrier is not GCL-controlled")
    if carrier.get("immutable") is not True:
        errors.append("archival release is not immutable")
    if source_asset.get("digest") != f"sha256:{EXPECTED_ARCHIVE}":
        errors.append("GCL source asset digest does not equal protected archive")
    if source_asset.get("byte_length") != verification.get("archive_byte_length"):
        errors.append("GCL source asset byte length mismatch")

    if record.get("candidate_disposition") != "PROTECTED_SOURCE_BITSET_REASSERTED_ON_GCL_ARCHIVAL_CARRIER__NO_SEMANTIC_CHANGE":
        errors.append("source reassertion disposition drift")
    if record.get("governed_admission_status") != "pending_exact_head_review":
        errors.append("source reassertion admission state drift")
    if routes.get("fresh_family_replay_may_begin") is not True:
        errors.append("verified source does not permit fresh replay")
    for key in (
        "fresh_family_replay_clear",
        "semantic_nonvacuity_audit_authorized",
        "solve_handoff_authorized",
        "cert_route_authorized",
        "mathcert_adjudication_authorized",
        "cert_output_authorized",
        "mathematical_target_proved",
        "aggregate_authority_permitted",
    ):
        if routes.get(key) is not False:
            errors.append(f"downstream authority inflated: {key}")

    if repair.get("proposed_family_boundary") != EXPECTED_BOUNDARY:
        errors.append("protected Permanent repair boundary drift")
    authority = repair.get("authority", {})
    if authority.get("official_lean_root") != EXPECTED_COMMIT or authority.get("official_lean_tree") != EXPECTED_TREE:
        errors.append("repair/source reassertion identity mismatch")
    coverage = repair.get("coverage_disposition", {})
    if coverage.get("encoded_formula_target_count") != 2 or coverage.get("encoded_circuit_target_count") != 0:
        errors.append("Permanent repair target inventory drift")
    if coverage.get("circuit_lower_bound_coverage") is not False:
        errors.append("circuit coverage inflation")

    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"Permanent source reassertion validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("validated OTP-C-PERMANENT protected source bitset reassertion; fresh replay may begin, all semantic/Solve/Cert authority remains closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
