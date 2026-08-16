#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
RECORD_PATH = ROOT / "sources" / "OPENAI-TEN-PROOFS-001" / "formal_source_successors" / "OTP-FORMAL-SOURCE-SUCCESSOR-002.json"
SCHEMA_PATH = ROOT / "schemas" / "openai_ten_proofs_formal_source_successor.schema.json"
MATRIX_PATH = ROOT / "sources" / "OPENAI-TEN-PROOFS-001" / "theorem_intake_matrix.json"
PROVIDER_PATH = ROOT / "provider_manifests" / "OPENAI-TEN-PROOFS-001.json"
ADAPTER_PATH = ROOT / "ci" / "otp_landrun_argv_adapter.sh"

EXPECTED_PREDECESSOR = {
    "root": "e62211d28e3a9131950c89caa6542cfe5eff3bca",
    "tree": "2f8e7ac5ae7f157b6b1de636c2c343b1c7a7e365",
    "deterministic_archive_sha256": "3022e62ffbed8f5f74d232034a703dc645e6b301879dff1e87df72979914294f",
    "matrix_blob": "2d8b24c32c804c4f5ca0f5f5ad1185199d35664b",
    "provider_blob": "fe1dab478e4ef9d6ddfe1b94a289fe7b51f58472",
}
EXPECTED_SUCCESSOR = {
    "root": "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6",
    "tree": "174289e4d4958cb0509874e6e53400e098213de7",
    "archive": "64534bbf7e1a5cc5f8c902d81657fb67c3dd9991d01f8a8b9e6803b163f3f532",
    "toolchain_blob": "94b9f495baff80fd9cb44aad8f4762cb3b2066fe",
    "lakefile_blob": "f29d6b0307597932154b34b97e37fe07ec3356de",
    "manifest_blob": "046e8de7f46832fbf092e3fb815efae01e4a2129",
    "lean_commit": "8c9756b28d64dab099da31a4c09229a9e6a2ef35",
    "mathlib_commit": "81a5d257c8e410db227a6665ed08f64fea08e997",
    "comparator_commit": "07bc4ea40f2266dcb861820a2ec1fa3244ed307f",
    "lean4export_commit": "4e7915201d3f9f04470d9eae002fa695f7cdc589",
    "lean4checker_commit": "b7398199245524275543dec6113229c9bb4902e5",
}
EXPECTED_REPLAY = {
    "evidence_head": "f8a0b92da39052ab726de12aad13c201243b6ebe",
    "run_id": 31945652355,
    "source_lock_job_id": 95161096598,
    "family_jobs": {
        "OTP-A-SPHERE-PACKING": 95161117046,
        "OTP-B1-BINARY-CODES": 95161117069,
        "OTP-B2-SPHERICAL-CODES": 95161117118,
        "OTP-D-NON-SOFIC": 95161117044,
        "OTP-E-CONNES-RIGIDITY": 95161117059,
        "OTP-G-QUANTUM-PARALLEL-REPETITION": 95161117041,
        "OTP-H-GAPCVP": 95161117067,
        "OTP-I-RAMSEY": 95161117103,
    },
    "permitted_axioms": ["propext", "Classical.choice", "Quot.sound"],
    "tcb": {
        "landrun_source_commit": "811cfff51ceaf3d9843708aa6d22e9b84ccac8b4",
        "landrun_binary_sha256": "a4ba9ed1b6b53f9cfd57b9fb1e4f8f3c3ab69cf6a0147764ff70303a8306f858",
        "lean4export_source_commit": "4e7915201d3f9f04470d9eae002fa695f7cdc589",
        "lean4export_binary_sha256": "e57369980b0b81228580ce08066fb9bd738e717e002673a143f4956d217266b0",
        "nanoda_source_commit": "ddfac2bf5a7b56cb46e141494427ff3dd55963c7",
        "nanoda_binary_sha256": "60cc30add2758abce965f122b4e85f1fdd7c23607ea67680cec6721aa2ef23f0",
        "landrun_argv_adapter_git_blob_sha1": "c283f58d7779c8dabca8d86adca2006899abfd74",
        "landrun_argv_adapter_sha256": "84d900d75bdc76c2c4168484a929e448be36fca20d093c42cac15ed923fe3f1d",
    },
}
EXPECTED_FAMILIES = [
    {
        "family_id": "OTP-A-SPHERE-PACKING",
        "config": ("ComparatorChallenges/A_SpherePacking.json", "46b2e7b49da43fb17a7efa88652f8ee1adc01cbe"),
        "challenge": ("ComparatorChallenges/A_SpherePacking.lean", "2477846e1883534837340c636fd928b091509783"),
        "solution": ("SpherePacking.lean", "e6117934a80142a8249356fdafa797eba030e920"),
        "theorems": ["PackingBounds.FullMain.exact_limit", "PackingBounds.FullMain.exact_binary_exponent", "PackingBounds.PackingBridge.sphere_packing_sharp_asymptotic_upper", "PackingBounds.sharpFullCohnElkiesManuscriptConclusions"],
        "definitions": [],
        "drift": "target_membership_stable_current_root_dependency_path_requires_reaudit",
        "semantic_state": "blocked_pending_current_root_dependency_and_source_locus_audit",
    },
    {
        "family_id": "OTP-B1-BINARY-CODES",
        "config": ("ComparatorChallenges/B_BinaryCodes.json", "b530b77972c83396c1f2aed2deccda3a12fb6cab"),
        "challenge": ("ComparatorChallenges/B_BinaryCodes.lean", "c9e93b1944e6806802068cf593fa6557e4267bb1"),
        "solution": ("MetricCodes.lean", "51628c0db81bd6cb9a79777fa601306c9d64cbc5"),
        "theorems": ["MetricCodes.Hamming.binaryRate_lt_classicalRate", "MetricCodes.Hamming.exists_binaryRate_improvement", "MetricCodes.Johnson.binaryRate_le_combinedVariationalRate", "MetricCodes.MRRW.strict_mrrw2", "MetricCodes.Johnson.binaryRate_lt_mrrw", "MetricCodes.Johnson.exists_binaryRate_mrrw_improvement"],
        "definitions": [],
        "drift": "target_membership_stable",
        "semantic_state": "not_clear",
    },
    {
        "family_id": "OTP-B2-SPHERICAL-CODES",
        "config": ("ComparatorChallenges/B_SphericalCodes.json", "b343dca9c0373f80c6304f30f261b81b371661c3"),
        "challenge": ("ComparatorChallenges/B_SphericalCodes.lean", "5f2bcda432b7091097ae8753cac24c08d0c10f6c"),
        "solution": ("MetricCodes.lean", "51628c0db81bd6cb9a79777fa601306c9d64cbc5"),
        "theorems": ["MetricCodes.Johnson.main_binary_theorem", "MetricCodes.Spherical.HigherHierarchy.main_general", "MetricCodes.Spherical.HigherHierarchy.strict_hierarchy", "MetricCodes.Spherical.HigherHierarchy.NumericalMaximum.eventually_kissingNumber_lt_published"],
        "definitions": [],
        "drift": "explicit_replacement_of_predecessor_seven_target_surface_with_four_current_targets",
        "semantic_state": "not_clear_target_surface_drift_requires_family_audit",
    },
    {
        "family_id": "OTP-D-NON-SOFIC",
        "config": ("ComparatorChallenges/D_NonSoficGroup.json", "af023106a83552d7fafb4f0d122f121a095f802c"),
        "challenge": ("ComparatorChallenges/D_NonSoficGroup.lean", "158d97224fbd51c203ff07a2f74041ffa2c6013b"),
        "solution": ("NonSoficGroup.lean", "dd1f8e63960300c8674fcd491007d2a628fbc6fe"),
        "theorems": ["SoficGroups.SourceTopLevelCompressionFinal.exists_finitelyPresented_nonsofic_group"],
        "definitions": [],
        "drift": "target_membership_stable",
        "semantic_state": "not_clear",
    },
    {
        "family_id": "OTP-E-CONNES-RIGIDITY",
        "config": ("ComparatorChallenges/E_ConnesRigidity.json", "f5d2964be6b1a154bc12b38a0f99f0960960a2d9"),
        "challenge": ("ComparatorChallenges/E_ConnesRigidity.lean", "9425edabd79319cbe2943888c6ece107bdd81dfb"),
        "solution": ("ConnesRigidity.lean", "81cf03e3f7ccdc66815cc00c9969bcfd2341c8d6"),
        "theorems": ["ConnesRigidity.exists_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors", "ConnesRigidity.exists_infinite_pairwise_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors"],
        "definitions": [],
        "drift": "explicit_declaration_identity_change_from_ConnesRigidity2_namespace_no_alias_inferred",
        "semantic_state": "not_clear_declaration_identity_drift_requires_family_audit",
    },
    {
        "family_id": "OTP-G-QUANTUM-PARALLEL-REPETITION",
        "config": ("ComparatorChallenges/G_QuantumParallelRepetition.json", "c7dd59e9df9ae5d90b35f76a9d958943d8e94770"),
        "challenge": ("ComparatorChallenges/G_QuantumParallelRepetition.lean", "8257e7726643a8f8c08c7e91584e003ab204c589"),
        "solution": ("QuantumParallelRepetition.lean", "887c4378f124a5d81a3f2624b6dc34867ec409c4"),
        "theorems": ["QuantumParallelRepetition.distributionUniformExponential", "QuantumParallelRepetition.standardQuantumParallelRepetition"],
        "definitions": [],
        "drift": "target_membership_stable",
        "semantic_state": "not_clear",
    },
    {
        "family_id": "OTP-H-GAPCVP",
        "config": ("ComparatorChallenges/H_GapCVP.json", "fdba0e774acc6c2bd6fd450ee155975c0eda1833"),
        "challenge": ("ComparatorChallenges/H_GapCVP.lean", "770e202350a5c94d3f6516428ff01092cb8f8cb4"),
        "solution": ("GapCVP.lean", "47f3a395e4d9ec3e2892664860f26ed63421b0c9"),
        "theorems": ["GapCVP.Comparator.gapCVP400IsNPHard", "GapCVP.Comparator.binaryNearestCodewordIsNPHard", "GapCVP.Comparator.binarySyndromeDecodingIsNPHard", "GapCVP.Comparator.finitePNormGapCVPIsNPHard"],
        "definitions": ["GapCVP.Comparator.gapCVP400Promise", "GapCVP.Comparator.binaryNearestCodewordPromise", "GapCVP.Comparator.binarySyndromeDecodingPromise", "GapCVP.Comparator.finitePGapCVPPromise"],
        "drift": "four_predecessor_definition_holes_are_now_explicit_definition_bodies_but_disjointness_and_theorem_challenge_placeholders_remain",
        "semantic_state": "blocked_structural_interfaces_present_semantic_obligations_open",
    },
    {
        "family_id": "OTP-I-RAMSEY",
        "config": ("ComparatorChallenges/I_MulticolorTriangleRamsey.json", "ce67db0653e18a2de68f471c00b9f892b789f806"),
        "challenge": ("ComparatorChallenges/I_MulticolorTriangleRamsey.lean", "6a9e42d686720f4b74ddc2001006b0b7a20f11aa"),
        "solution": ("MulticolorTriangleRamsey.lean", "24b55f531a4d36347cd2277b1b9c7d784d91ae35"),
        "theorems": ["ErdosProblems.MulticolourTriangleRamsey.erdos_183", "ErdosProblems.MulticolourTriangleRamsey.erdos_problem_183_explicit", "ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_sharp_coefficients", "ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_isTheta"],
        "definitions": [],
        "drift": "target_membership_stable",
        "semantic_state": "not_clear",
    },
]
EXPECTED_AUTHORITY = {
    "formal_source_successor_pending_until_protected_merge": True,
    "semantic_clearance_created": False,
    "nonvacuity_clearance_created": False,
    "solve_handoff_created": False,
    "mathcert_route_created": False,
    "adjudication_created": False,
    "cert_output_created": False,
    "mathematical_target_proved": False,
    "other_family_mutation_authorized": False,
    "aggregate_ten_proofs_authority_created": False,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def schema_errors(instance: Any) -> list[str]:
    schema = load_json(SCHEMA_PATH)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [f"schema: {'/'.join(str(p) for p in err.absolute_path)}: {err.message}" for err in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))]


def validation_errors(record: Any | None = None, *, check_files: bool = True) -> list[str]:
    data = copy.deepcopy(load_json(RECORD_PATH) if record is None else record)
    errors = schema_errors(data)
    if not isinstance(data, dict):
        return errors

    if data.get("governance") != {
        "issue": 87,
        "human_steward_authorization_comment": 5307217849,
        "protected_base": "20a4cb716dba2586931e3eaebb079890c66044bd",
        "publication_state": "candidate_until_protected_merge",
    }:
        errors.append("governance authority drifted")

    pred = data.get("predecessor", {})
    if pred.get("root") != EXPECTED_PREDECESSOR["root"] or pred.get("tree") != EXPECTED_PREDECESSOR["tree"]:
        errors.append("predecessor root/tree drifted")
    if pred.get("deterministic_archive_sha256") != EXPECTED_PREDECESSOR["deterministic_archive_sha256"]:
        errors.append("predecessor archive drifted")
    if pred.get("theorem_matrix", {}).get("git_blob_sha1") != EXPECTED_PREDECESSOR["matrix_blob"]:
        errors.append("predecessor theorem matrix binding drifted")
    if pred.get("provider_manifest", {}).get("git_blob_sha1") != EXPECTED_PREDECESSOR["provider_blob"]:
        errors.append("predecessor provider binding drifted")
    if pred.get("history_immutable") is not True:
        errors.append("predecessor history must remain immutable")

    succ = data.get("successor", {})
    if succ.get("root") != EXPECTED_SUCCESSOR["root"] or succ.get("tree") != EXPECTED_SUCCESSOR["tree"]:
        errors.append("successor root/tree substitution")
    if succ.get("deterministic_archive_sha256") != EXPECTED_SUCCESSOR["archive"]:
        errors.append("successor archive substitution")
    toolchain = succ.get("lean_toolchain", {})
    if toolchain.get("git_blob_sha1") != EXPECTED_SUCCESSOR["toolchain_blob"] or toolchain.get("lean_commit") != EXPECTED_SUCCESSOR["lean_commit"]:
        errors.append("Lean toolchain identity drifted")
    if succ.get("lakefile", {}).get("git_blob_sha1") != EXPECTED_SUCCESSOR["lakefile_blob"]:
        errors.append("lakefile identity drifted")
    manifest = succ.get("lake_manifest", {})
    expected_manifest = {
        "git_blob_sha1": EXPECTED_SUCCESSOR["manifest_blob"],
        "mathlib_commit": EXPECTED_SUCCESSOR["mathlib_commit"],
        "comparator_commit": EXPECTED_SUCCESSOR["comparator_commit"],
        "lean4export_commit": EXPECTED_SUCCESSOR["lean4export_commit"],
        "lean4checker_commit": EXPECTED_SUCCESSOR["lean4checker_commit"],
    }
    for key, value in expected_manifest.items():
        if manifest.get(key) != value:
            errors.append(f"lake manifest {key} drifted")

    replay = data.get("replay", {})
    for key in ("evidence_head", "run_id", "source_lock_job_id"):
        if replay.get(key) != EXPECTED_REPLAY[key]:
            errors.append(f"replay {key} drifted")
    if replay.get("mode") != "isolated_family_comparator_not_All.lean":
        errors.append("aggregate All.lean substitution is prohibited")
    if replay.get("required_family_count") != 8 or replay.get("outcome") != "clear_8_of_8":
        errors.append("eight-family isolated replay census drifted")
    if replay.get("family_jobs") != EXPECTED_REPLAY["family_jobs"]:
        errors.append("family replay job bindings drifted")
    if replay.get("permitted_axioms") != EXPECTED_REPLAY["permitted_axioms"]:
        errors.append("permitted theorem-level axiom set drifted")
    if replay.get("tcb") != EXPECTED_REPLAY["tcb"]:
        errors.append("replay TCB drifted")

    families = data.get("families", [])
    if len(families) != len(EXPECTED_FAMILIES):
        errors.append("family count must remain exactly eight")
    else:
        for actual, expected in zip(families, EXPECTED_FAMILIES):
            if actual.get("family_id") != expected["family_id"]:
                errors.append("family order/membership drifted")
                continue
            for field in ("config", "challenge", "solution"):
                expected_path, expected_blob = expected[field]
                bound = actual.get(field, {})
                if bound.get("path") != expected_path or bound.get("git_blob_sha1") != expected_blob:
                    errors.append(f"{expected['family_id']}: {field} identity drifted")
            if actual.get("theorem_names") != expected["theorems"]:
                errors.append(f"{expected['family_id']}: hidden theorem addition/removal/substitution")
            if actual.get("definition_names") != expected["definitions"]:
                errors.append(f"{expected['family_id']}: definition surface drifted")
            if actual.get("enable_nanoda") is not True or actual.get("replay") != "comparator_lean_kernel_nanoda_accept":
                errors.append(f"{expected['family_id']}: checker acceptance surface drifted")
            if actual.get("drift") != expected["drift"]:
                errors.append(f"{expected['family_id']}: governed drift classification changed")
            if actual.get("semantic_state") != expected["semantic_state"]:
                errors.append(f"{expected['family_id']}: semantic state promoted or changed")

    mirrors = data.get("prospective_mirrors", {})
    if mirrors != {
        "theorem_matrix_mode": "successor_overlay_only",
        "provider_manifest_mode": "successor_overlay_only",
        "predecessor_matrix_path": "sources/OPENAI-TEN-PROOFS-001/theorem_intake_matrix.json",
        "predecessor_provider_path": "provider_manifests/OPENAI-TEN-PROOFS-001.json",
        "successor_record_path": "sources/OPENAI-TEN-PROOFS-001/formal_source_successors/OTP-FORMAL-SOURCE-SUCCESSOR-002.json",
    }:
        errors.append("matrix/provider successor overlay mode drifted")

    if data.get("authority") != EXPECTED_AUTHORITY:
        errors.append("forbidden Solve/Cert/adjudication/output/proof/aggregate authority insertion")

    if check_files:
        if git_blob_sha1(MATRIX_PATH) != EXPECTED_PREDECESSOR["matrix_blob"]:
            errors.append("protected predecessor theorem matrix bytes were rewritten")
        if git_blob_sha1(PROVIDER_PATH) != EXPECTED_PREDECESSOR["provider_blob"]:
            errors.append("protected predecessor provider manifest bytes were rewritten")
        if git_blob_sha1(ADAPTER_PATH) != EXPECTED_REPLAY["tcb"]["landrun_argv_adapter_git_blob_sha1"]:
            errors.append("landrun argv adapter bytes drifted")
        if sha256(ADAPTER_PATH) != EXPECTED_REPLAY["tcb"]["landrun_argv_adapter_sha256"]:
            errors.append("landrun argv adapter SHA-256 drifted")

    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("OTP-FORMAL-SOURCE-SUCCESSOR-002 validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
