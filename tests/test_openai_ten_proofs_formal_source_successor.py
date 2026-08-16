from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ci" / "validate_openai_ten_proofs_formal_source_successor.py"
SPEC = importlib.util.spec_from_file_location("otp_successor_validator", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class FormalSourceSuccessorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(MODULE.RECORD_PATH.read_text(encoding="utf-8"))

    def errors(self, record=None):
        return MODULE.validation_errors(copy.deepcopy(self.record if record is None else record), check_files=False)

    def test_current_record_passes(self):
        self.assertEqual(self.errors(), [])

    def test_predecessor_history_rewrite_rejected(self):
        record = copy.deepcopy(self.record)
        record["predecessor"]["root"] = "0" * 40
        self.assertTrue(self.errors(record))

    def test_successor_root_substitution_rejected(self):
        record = copy.deepcopy(self.record)
        record["successor"]["root"] = "1" * 40
        self.assertTrue(self.errors(record))

    def test_successor_archive_substitution_rejected(self):
        record = copy.deepcopy(self.record)
        record["successor"]["deterministic_archive_sha256"] = "2" * 64
        self.assertTrue(self.errors(record))

    def test_hidden_target_change_rejected(self):
        record = copy.deepcopy(self.record)
        record["families"][1]["theorem_names"].append("Hidden.Target")
        self.assertTrue(self.errors(record))

    def test_b2_drift_cannot_be_treated_as_noop(self):
        record = copy.deepcopy(self.record)
        record["families"][2]["drift"] = "target_membership_stable"
        self.assertTrue(self.errors(record))

    def test_connes_namespace_cannot_be_silently_aliased(self):
        record = copy.deepcopy(self.record)
        record["families"][4]["theorem_names"][0] = "ConnesRigidity2.exists_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors"
        self.assertTrue(self.errors(record))

    def test_gapcvp_definitions_do_not_create_semantic_clearance(self):
        record = copy.deepcopy(self.record)
        record["families"][6]["semantic_state"] = "not_clear"
        self.assertTrue(self.errors(record))

    def test_sphere_cannot_be_promoted_from_replay(self):
        record = copy.deepcopy(self.record)
        record["families"][0]["semantic_state"] = "not_clear"
        self.assertTrue(self.errors(record))

    def test_all_lean_substitution_rejected(self):
        record = copy.deepcopy(self.record)
        record["replay"]["mode"] = "aggregate_All.lean"
        self.assertTrue(self.errors(record))

    def test_solve_handoff_insertion_rejected(self):
        record = copy.deepcopy(self.record)
        record["authority"]["solve_handoff_created"] = True
        self.assertTrue(self.errors(record))

    def test_mathcert_route_insertion_rejected(self):
        record = copy.deepcopy(self.record)
        record["authority"]["mathcert_route_created"] = True
        self.assertTrue(self.errors(record))

    def test_adjudication_or_output_insertion_rejected(self):
        record = copy.deepcopy(self.record)
        record["authority"]["adjudication_created"] = True
        record["authority"]["cert_output_created"] = True
        self.assertTrue(self.errors(record))

    def test_proof_promotion_rejected(self):
        record = copy.deepcopy(self.record)
        record["authority"]["mathematical_target_proved"] = True
        self.assertTrue(self.errors(record))

    def test_other_family_mutation_rejected(self):
        record = copy.deepcopy(self.record)
        record["families"][7]["family_id"] = "OTP-J1-COMPACTNESS"
        self.assertTrue(self.errors(record))

    def test_aggregate_authority_rejected(self):
        record = copy.deepcopy(self.record)
        record["authority"]["aggregate_ten_proofs_authority_created"] = True
        self.assertTrue(self.errors(record))

    def test_predecessor_matrix_binding_rewrite_rejected(self):
        record = copy.deepcopy(self.record)
        record["predecessor"]["theorem_matrix"]["git_blob_sha1"] = "3" * 40
        self.assertTrue(self.errors(record))

    def test_predecessor_provider_binding_rewrite_rejected(self):
        record = copy.deepcopy(self.record)
        record["predecessor"]["provider_manifest"]["git_blob_sha1"] = "4" * 40
        self.assertTrue(self.errors(record))


if __name__ == "__main__":
    unittest.main()
