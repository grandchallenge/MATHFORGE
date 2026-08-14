from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_permanent_repair",
    ROOT / "ci/validate_openai_ten_proofs_permanent_repair.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OpenAITenProofsPermanentRepairTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads(MODULE.MANIFEST_PATH.read_text(encoding="utf-8"))
        self.matrix = json.loads(MODULE.MATRIX_PATH.read_text(encoding="utf-8"))
        self.matrix_blob = MODULE.git_blob_sha1(MODULE.MATRIX_PATH)

    def errors(self, *, manifest=None, matrix=None, matrix_blob=None):
        return MODULE.validation_errors(
            manifest=copy.deepcopy(self.manifest if manifest is None else manifest),
            matrix=copy.deepcopy(self.matrix if matrix is None else matrix),
            matrix_blob=self.matrix_blob if matrix_blob is None else matrix_blob,
        )

    def claim(self, manifest, claim_id):
        return next(item for item in manifest["advertised_claims"] if item["claim_id"] == claim_id)

    def test_current_repair_candidate_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_missing_claim_deletion_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["advertised_claims"].pop(0)
        self.assertTrue(self.errors(manifest=manifest))

    def test_formula_condition_removal_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        claim = self.claim(manifest, "OTP-C-PERMANENT-DIVISION-FREE-FORMULA")
        claim["required_hypotheses"] = [
            h for h in claim["required_hypotheses"] if not h.startswith("hf :")
        ]
        self.assertTrue(self.errors(manifest=manifest))

    def test_representation_conditionality_removal_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        claim = self.claim(manifest, "OTP-C-PERMANENT-RATIONAL-FORMULA")
        claim["representation_premise_required"] = False
        self.assertTrue(self.errors(manifest=manifest))

    def test_circuit_class_substitution_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        claim = self.claim(manifest, "OTP-C-PERMANENT-CIRCUIT")
        claim["claim_class"] = "division_free_formula_lower_bound"
        self.assertTrue(self.errors(manifest=manifest))

    def test_asymptotic_domain_weakening_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        claim = self.claim(manifest, "OTP-C-PERMANENT-CIRCUIT")
        claim["dimension_domain"] = "n >= 32"
        self.assertTrue(self.errors(manifest=manifest))

    def test_formula_to_circuit_lower_bound_promotion_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["coverage_disposition"]["circuit_lower_bound_coverage"] = True
        self.assertTrue(self.errors(manifest=manifest))

    def test_target_count_inflation_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["encoded_target_inventory"]["target_count"] = 3
        self.assertTrue(self.errors(manifest=manifest))

    def test_another_family_insertion_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["result_family"] = "OTP-A-SPHERE-PACKING"
        self.assertTrue(self.errors(manifest=manifest))

    def test_route_insertion_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["route_controls"]["solve_handoff_authorized"] = True
        self.assertTrue(self.errors(manifest=manifest))

    def test_adjudication_insertion_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["route_controls"]["mathcert_adjudication_authorized"] = True
        self.assertTrue(self.errors(manifest=manifest))

    def test_proof_promotion_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["route_controls"]["mathematical_target_proved"] = True
        self.assertTrue(self.errors(manifest=manifest))

    def test_silent_current_upstream_repin_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["authority"]["official_lean_root"] = (
            manifest["non_authoritative_current_upstream_observation"]["observed_head"]
        )
        self.assertTrue(self.errors(manifest=manifest))

    def test_current_upstream_observation_cannot_become_authority(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["non_authoritative_current_upstream_observation"]["repins_protected_authority"] = True
        self.assertTrue(self.errors(manifest=manifest))

    def test_matrix_blob_drift_is_rejected(self) -> None:
        self.assertTrue(self.errors(matrix_blob="0" * 40))

    def test_matrix_circuit_target_invention_is_rejected(self) -> None:
        matrix = copy.deepcopy(self.matrix)
        row = next(item for item in matrix["result_families"] if item["result_id"] == "OTP-C-PERMANENT")
        row["theorem_names"].append("PermanentFormulaLowerBound.invented_circuit_target")
        self.assertTrue(self.errors(matrix=matrix))

    def test_matrix_route_promotion_is_rejected(self) -> None:
        matrix = copy.deepcopy(self.matrix)
        row = next(item for item in matrix["result_families"] if item["result_id"] == "OTP-C-PERMANENT")
        row["may_route_to_solve"] = True
        self.assertTrue(self.errors(matrix=matrix))


if __name__ == "__main__":
    unittest.main()
