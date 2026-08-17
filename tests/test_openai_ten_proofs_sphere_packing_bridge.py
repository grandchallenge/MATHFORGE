from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "sphere_bridge_validator",
    ROOT / "ci" / "validate_openai_ten_proofs_sphere_packing_bridge.py",
)
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class SpherePackingBridgeSemanticTests(unittest.TestCase):
    def setUp(self):
        self.r = V.load()

    def errors(self, record=None):
        return V.validation_errors(copy.deepcopy(self.r if record is None else record))

    def mutate(self, path, value):
        r = copy.deepcopy(self.r)
        node = r
        for key in path[:-1]:
            node = node[key]
        node[path[-1]] = value
        return r

    def test_current_record_passes(self):
        self.assertEqual(self.errors(), [])

    def test_source_digest_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["source_authority", "pdf_sha256"], "0" * 64)))

    def test_formal_root_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "root"], "0" * 40)))

    def test_solution_blob_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "solution", "blob"], "0" * 40)))

    def test_target_substitution_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "target"], "PackingBounds.FullMain.exact_limit")))

    def test_replay_substitution_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "isolated_replay", "job_id"], 1)))

    def test_unit_separation_normalization_deletion_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"][2]["analysis"] = "The names look similar."
        self.assertTrue(self.errors(r))

    def test_delta_alias_inflation_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "sphere_packing_constant_is_declared_alias_for_delta_d"], True)))

    def test_upper_density_verbatim_inflation_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "source_prints_formal_upper_density_implementation"], True)))

    def test_explicit_error_source_inflation_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "source_prints_explicit_error_function"], True)))

    def test_normalization_status_weakening_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"][2]["status"] = "assumed"
        self.assertTrue(self.errors(r))

    def test_nonvacuity_loss_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["nonvacuity", "state"], "blocked")))

    def test_axiom_inflation_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["replay_and_axiom_audit"]["permitted_axioms_only"].append("Classical.propComplete")
        self.assertTrue(self.errors(r))

    def test_proof_certification_inflation_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "proof_correctness_certified_here"], True)))

    def test_solve_authority_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["route_controls", "solve_handoff_authorized"], True)))

    def test_cert_authority_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["route_controls", "mathcert_route_authorized"], True)))

    def test_mathematical_proof_promotion_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["route_controls", "mathematical_target_proved"], True)))

    def test_aggregate_authority_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["route_controls", "aggregate_openai_ten_proofs_authority"], True)))

    def test_review_gate_removal_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["activation", "requires_non_author_approved_review"], False)))

    def test_human_steward_gate_removal_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["activation", "requires_human_steward_disposition"], False)))

    def test_head_change_must_require_reapproval(self):
        self.assertTrue(self.errors(self.mutate(["activation", "head_change_requires_reapproval"], False)))

    def test_solve_not_implicitly_authorized_by_activation(self):
        self.assertTrue(self.errors(self.mutate(["activation", "effect_does_not_authorize_solve"], False)))


if __name__ == "__main__":
    unittest.main()
