#!/usr/bin/env python3
"""Validate the candidate OTP-C-PERMANENT semantic/nonvacuity audit fail closed."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-C-PERMANENT/semantic_audit_record.json"
SCHEMA_PATH = ROOT / "schemas/openai_ten_proofs_permanent_semantic_audit_record.schema.json"
WITNESS_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-C-PERMANENT/PermanentFormulaNonvacuity.lean"
REPAIR_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/repairs/OTP-C-PERMANENT/repair_manifest.json"
REPLAY_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/replays/OTP-C-PERMANENT/replay_record.json"
REVISION_AUDIT_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/source_revision_audits/OTP-TRANCHE-001.json"

EXPECTED_BOUNDARY = "PERMANENT_FORMULA_LOWER_BOUNDS_ONLY__CIRCUIT_THEOREM_NOT_ENCODED"
EXPECTED_ROOT = "e62211d28e3a9131950c89caa6542cfe5eff3bca"
EXPECTED_TREE = "2f8e7ac5ae7f157b6b1de636c2c343b1c7a7e365"
EXPECTED_ARCHIVE = "3022e62ffbed8f5f74d232034a703dc645e6b301879dff1e87df72979914294f"
EXPECTED_CHALLENGE_BLOB = "ca71c280479f12a4249b0dc63b6e1af27bdb32ff"
EXPECTED_CHALLENGE_SHA256 = "fc97578bcbb072ff82383e4c903107130ba3dd1a2209235ab32270c7df37f83d"
EXPECTED_HISTORICAL_PDF_SHA256 = "f318c6508c9d49ef876a5a26cd73928705f96c07bb43e92a0cb35bd3f666ea53"
EXPECTED_HISTORICAL_PDF_BYTES = 2266052
EXPECTED_ORIGINAL_URL = "https://cdn.openai.com/pdf/ten-proofs-oai-original.pdf"
EXPECTED_WITNESS_RUN = 31799810487
EXPECTED_WITNESS_JOB = 94764884248
EXPECTED_WITNESS_BLOB = "e756c8476bac1795f3fb8ca0b7235d3a4a5c59ea"
EXPECTED_DISPOSITION = "PERMANENT_FORMULA_VARIABLE_LEAF_BOUNDS__SEMANTIC_AND_NONVACUITY_CLEAR__CIRCUIT_AND_GATE_BOUNDS_NOT_ENCODED"
EXPECTED_TARGETS = [
    "PermanentFormulaLowerBound.permanent_divisionFree_formula_logarithmic_lower_bound",
    "PermanentFormulaLowerBound.permanent_rational_formula_logarithmic_lower_bound",
]
EXPECTED_COORDINATES = [
    "quantified_objects",
    "ambient_algebraic_structure",
    "computational_formula_model",
    "representation_predicate",
    "validity_predicate",
    "dimension_threshold",
    "complexity_size_measure",
    "numerical_lower_bound_expression",
    "logarithm_convention_base",
    "source_side_conditions",
    "finite_n_scope",
    "nonvacuity_existence",
]
EXPECTED_WITNESS_THEOREMS = [
    "PermanentFormulaLowerBound.Nonvacuity.formula_eval_surjective",
    "PermanentFormulaLowerBound.Nonvacuity.formulaToRational_valid",
    "PermanentFormulaLowerBound.Nonvacuity.formulaToRational_eval",
    "PermanentFormulaLowerBound.Nonvacuity.formulaToRational_variableLeaves",
    "PermanentFormulaLowerBound.Nonvacuity.permanent_divisionFree_formula_nonvacuous",
    "PermanentFormulaLowerBound.Nonvacuity.permanent_rational_formula_nonvacuous",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def validation_errors(
    record: dict[str, Any] | None = None,
    repair: dict[str, Any] | None = None,
    replay: dict[str, Any] | None = None,
    revision_audit: dict[str, Any] | None = None,
    witness_text: str | None = None,
) -> list[str]:
    errors: list[str] = []
    record = load_json(RECORD_PATH) if record is None else record
    repair = load_json(REPAIR_PATH) if repair is None else repair
    replay = load_json(REPLAY_PATH) if replay is None else replay
    revision_audit = load_json(REVISION_AUDIT_PATH) if revision_audit is None else revision_audit
    witness_text = WITNESS_PATH.read_text(encoding="utf-8") if witness_text is None else witness_text
    schema = load_json(SCHEMA_PATH)

    for error in sorted(Draft202012Validator(schema).iter_errors(record), key=lambda e: list(e.path)):
        errors.append(f"semantic schema: {error.json_path}: {error.message}")

    if record.get("family_boundary") != EXPECTED_BOUNDARY:
        errors.append("Permanent semantic family boundary drift")

    predecessors = record.get("predecessors", {})
    expected_predecessors = {
        "repair_merge": "40c38eb6a716acb10145ba42f0c9c768490a7e71",
        "source_reassertion_merge": "8696665805a776b537d7b469a24b88e887152466",
        "fresh_replay_merge": "e6bfb856ec9aa6a43601e2ea6eb4047cb84ce297",
        "reviewed_replay_head": "397338ea77f7617cc80745be2f612f10a4bdeff4",
        "fresh_replay_run": 31793518288,
        "fresh_replay_job": 94745449727,
    }
    if predecessors != expected_predecessors:
        errors.append("protected predecessor identity drift")

    protected = record.get("protected_lean_source", {})
    if protected.get("historical_commit") != EXPECTED_ROOT:
        errors.append("protected Lean historical root drift")
    if protected.get("tree") != EXPECTED_TREE:
        errors.append("protected Lean tree drift")
    if protected.get("deterministic_archive_sha256") != EXPECTED_ARCHIVE:
        errors.append("protected Lean archive drift")
    if protected.get("challenge_git_blob_sha1") != EXPECTED_CHALLENGE_BLOB:
        errors.append("protected Permanent challenge blob drift")
    if protected.get("challenge_sha256") != EXPECTED_CHALLENGE_SHA256:
        errors.append("protected Permanent challenge SHA256 drift")
    if protected.get("lean_toolchain") != "leanprover/lean4:v4.32.0":
        errors.append("Lean toolchain drift")
    if protected.get("later_upstream_revision_substituted") is not False:
        errors.append("later upstream Lean revision substituted")

    manuscript = record.get("manuscript_source", {})
    historical = manuscript.get("historical_admitted_revision", {})
    locus = manuscript.get("permanent_theorem_locus_pin_candidate", {})
    if historical.get("sha256") != EXPECTED_HISTORICAL_PDF_SHA256 or historical.get("byte_length") != EXPECTED_HISTORICAL_PDF_BYTES:
        errors.append("historical admitted manuscript metadata drift")
    if historical.get("retained_bytes_available") is not False:
        errors.append("historical admitted manuscript bytes falsely represented as retained")
    if locus.get("url") != EXPECTED_ORIGINAL_URL:
        errors.append("Permanent theorem-locus source URL drift")
    if locus.get("chapter") != 5 or locus.get("theorems") != ["Theorem 1.2", "Theorem 1.3"]:
        errors.append("Permanent theorem-locus identity drift")
    if locus.get("official_original_endpoint_reacquired") is not True or locus.get("load_bearing_text_parsed") is not True:
        errors.append("official-original Permanent theorem locus not reacquired and parsed")
    if locus.get("byte_identity_to_historical_admitted_revision_verified") is not False:
        errors.append("unverified historical PDF byte identity inflated")
    if locus.get("whole_document_semantic_equivalence_to_historical_admitted_revision_established") is not False:
        errors.append("unverified whole-document semantic equivalence inflated")
    if manuscript.get("historical_whole_document_byte_equivalence_established") is not False:
        errors.append("historical whole-document byte equivalence inflated")
    if manuscript.get("historical_whole_document_semantic_equivalence_established") is not False:
        errors.append("historical whole-document semantic equivalence inflated")

    admitted = revision_audit.get("admitted_manuscript", {})
    if admitted.get("sha256") != EXPECTED_HISTORICAL_PDF_SHA256 or admitted.get("bytes") != EXPECTED_HISTORICAL_PDF_BYTES:
        errors.append("semantic record disagrees with protected source-revision audit manuscript identity")
    if admitted.get("retained_bytes_available") is not False:
        errors.append("source-revision audit no longer preserves missing historical PDF bytes")

    witness = record.get("nonvacuity_witness", {})
    if witness.get("git_blob_sha1") != EXPECTED_WITNESS_BLOB:
        errors.append("nonvacuity witness blob record drift")
    actual_blob = git_blob_sha1(witness_text.encode("utf-8"))
    if actual_blob != EXPECTED_WITNESS_BLOB:
        errors.append("nonvacuity witness file content drift")
    if witness.get("lean_run") != EXPECTED_WITNESS_RUN or witness.get("lean_job") != EXPECTED_WITNESS_JOB:
        errors.append("exact nonvacuity replay identity drift")
    if witness.get("lean_version") != "4.32.0" or witness.get("exact_replay_clear") is not True:
        errors.append("exact Lean nonvacuity replay not clear")
    if witness.get("all_dimensions") is not True:
        errors.append("nonvacuity witness scope weakened below all dimensions")
    if witness.get("division_nodes_introduced_by_embedding") is not False:
        errors.append("rational nonvacuity witness unexpectedly introduces division")
    if witness.get("theorems") != EXPECTED_WITNESS_THEOREMS:
        errors.append("nonvacuity witness theorem inventory drift")
    lowered = witness_text.lower()
    if "sorry" in lowered or "admit" in lowered:
        errors.append("nonvacuity witness contains sorry/admit")
    if "permanent_divisionFree_formula_nonvacuous" not in witness_text or "permanent_rational_formula_nonvacuous" not in witness_text:
        errors.append("required Permanent nonvacuity theorem missing from witness")
    if "| .div" in witness_text or "RationalFormula.div" in witness_text:
        errors.append("formula-to-rational embedding contains a division constructor")

    targets = record.get("targets", [])
    if [target.get("target") for target in targets] != EXPECTED_TARGETS:
        errors.append("Permanent semantic target inventory drift")
    expected_constants = [("Theorem 1.2", 128, 256), ("Theorem 1.3", 192, 384)]
    for index, expected in enumerate(expected_constants):
        if index >= len(targets):
            continue
        target = targets[index]
        theorem, leaf_constant, gate_constant = expected
        if (target.get("source_theorem"), target.get("source_variable_leaf_constant"), target.get("source_gate_constant")) != expected:
            errors.append(f"source constants/theorem drift for target {index + 1}")
        if target.get("encoded_gate_bound") is not False:
            errors.append(f"source gate bound falsely encoded for {theorem}")
        if target.get("encoded_total_leaves_or_vertices_consequence") is not False:
            errors.append(f"total leaves/vertices consequence falsely encoded for {theorem}")
        coordinates = target.get("coordinates", [])
        if [coordinate.get("name") for coordinate in coordinates] != EXPECTED_COORDINATES:
            errors.append(f"12-coordinate inventory drift for {theorem}")
        prohibited = {"UNRESOLVED_SEMANTIC_GAP", "DISQUALIFYING_MISMATCH"}
        if any(coordinate.get("classification") in prohibited for coordinate in coordinates):
            errors.append(f"candidate clear target contains unresolved/disqualifying coordinate for {theorem}")
        if target.get("source_conclusion_projection", {}).get("classification") != "JUSTIFIED_WEAKENING":
            errors.append(f"source conclusion projection is not explicit justified weakening for {theorem}")
        if target.get("state_before_activation") != "SEMANTIC_PARTIAL__CHARACTERIZED_GAPS":
            errors.append(f"pre-activation semantic state inflated for {theorem}")
        if target.get("candidate_exit_state_after_activation") != "SEMANTIC_AND_NONVACUITY_CLEAR":
            errors.append(f"post-activation candidate state drift for {theorem}")
        if leaf_constant not in (128, 192) or gate_constant not in (256, 384):
            errors.append("internal validator constant error")

    activation = record.get("activation", {})
    for key in (
        "requires_exact_head_forge_ci",
        "requires_exact_head_gcl_conformance",
        "requires_exact_head_codeql",
        "requires_non_author_approved_review",
        "requires_human_steward_disposition",
        "head_change_requires_reapproval",
    ):
        if activation.get(key) is not True:
            errors.append(f"activation gate disabled: {key}")

    if record.get("candidate_family_disposition") != EXPECTED_DISPOSITION:
        errors.append("candidate family disposition drift")

    routes = record.get("route_controls", {})
    for key, value in routes.items():
        if value is not False:
            errors.append(f"claim or downstream authority inflated: {key}")

    if repair.get("proposed_family_boundary") != EXPECTED_BOUNDARY:
        errors.append("semantic audit disagrees with protected repair boundary")
    repair_authority = repair.get("authority", {})
    if repair_authority.get("official_lean_root") != EXPECTED_ROOT or repair_authority.get("official_lean_tree") != EXPECTED_TREE:
        errors.append("semantic audit disagrees with protected repair Lean identity")
    coverage = repair.get("coverage_disposition", {})
    if coverage.get("encoded_formula_target_count") != 2 or coverage.get("encoded_circuit_target_count") != 0:
        errors.append("protected repair target inventory drift")
    if coverage.get("circuit_lower_bound_coverage") is not False:
        errors.append("protected repair circuit coverage inflated")

    replay_protected = replay.get("protected_source", {})
    if replay_protected.get("historical_commit") != EXPECTED_ROOT or replay_protected.get("tree") != EXPECTED_TREE:
        errors.append("semantic audit disagrees with protected replay Lean identity")
    replay_inventory = replay.get("successful_replay", {}).get("target_inventory", {})
    if replay_inventory.get("targets") != EXPECTED_TARGETS or replay_inventory.get("circuit_target_count") != 0:
        errors.append("semantic audit disagrees with protected replay target inventory")

    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        "validated OTP-C-PERMANENT candidate semantic/nonvacuity clearance: exact witness clear; "
        "official-original Chapter 5 theorem-locus pin pending protected activation; historical PDF byte equivalence and circuit/gate coverage remain false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
