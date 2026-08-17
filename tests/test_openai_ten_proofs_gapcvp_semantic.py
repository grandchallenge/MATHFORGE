from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "gapcvp_semantic_validator",
    ROOT / "ci" / "validate_openai_ten_proofs_gapcvp_semantic.py",
)
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class GapCVPSemanticAuditTests(unittest.TestCase):
    def setUp(self):
        self.r = V.load_record()
        self.s = V.load_schema()

    def errors(self, record=None, schema=None):
        return V.validation_errors(
            copy.deepcopy(self.r if record is None else record),
            copy.deepcopy(self.s if schema is None else schema),
        )

    def mutate(self, path, value):
        r = copy.deepcopy(self.r)
        node = r
        for key in path[:-1]:
            node = node[key]
        node[path[-1]] = value
        return r

    def test_current_record_passes(self):
        self.assertEqual(self.errors(), [])

    def test_top_level_schema_injection_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["unregistered_authority"] = True
        self.assertTrue(self.errors(r))

    def test_source_digest_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["source_authority", "pdf_sha256"], "0" * 64)))

    def test_formal_root_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "root"], "0" * 40)))

    def test_solution_blob_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "solution", "blob"], "0" * 40)))

    def test_target_substitution_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["formal_authority"]["targets"][0] = "GapCVP.Comparator.unregisteredTarget"
        self.assertTrue(self.errors(r))

    def test_promise_substitution_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["formal_authority"]["promise_definitions"][2] = "GapCVP.Comparator.unregisteredPromise"
        self.assertTrue(self.errors(r))

    def test_replay_job_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "replay", "job_id"], 1)))

    def test_mathlib_machine_model_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["machine_model", "mathlib_commit"], "0" * 40)))

    def test_bittm_uninterpreted_label_inflation_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["machine_model", "classification"], "uninterpreted_polynomial_time_label")))

    def test_reduction_direction_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["reduction_semantics", "direction_matches_source"], False)))

    def test_search_decision_conflation_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["reduction_semantics", "search_decision_conflated"], True)))

    def test_malformed_input_promotion_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["reduction_semantics", "malformed_input_policy"], "no")))

    def test_intermediate_threshold_promotion_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["reduction_semantics", "intermediate_threshold_policy"], "no")))

    def test_euclidean_factor_drift_to_constant_400_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][0]["source_factor"] = "400"
        r["target_audits"][0]["formal_factor"] = "400"
        self.assertTrue(self.errors(r))

    def test_binary_factor_drift_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][1]["source_factor"] = "n^(1/400)"
        self.assertTrue(self.errors(r))

    def test_finite_p_factor_drift_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][3]["source_factor"] = "n^(1/200)"
        self.assertTrue(self.errors(r))

    def test_euclidean_whole_interface_inflation_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][0]["qualification"] = "The formal target is identical to the whole source GapCVP interface."
        self.assertTrue(self.errors(r))

    def test_nearest_generator_orientation_erasure_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][1]["qualification"] = "The matrices are printed identically."
        self.assertTrue(self.errors(r))

    def test_syndrome_consistency_erasure_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][2]["qualification"] = "Every syntactic syndrome instance has identical source semantics."
        self.assertTrue(self.errors(r))

    def test_finite_p_input_dependent_parameter_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][3]["qualification"] = "p is supplied as part of each encoded instance."
        self.assertTrue(self.errors(r))

    def test_norm_substitution_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][0]["norm"] = "l1"
        self.assertTrue(self.errors(r))

    def test_threshold_weakening_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][0]["no_threshold"] = "distance >= n^(1/400) r"
        # The exact threshold is also protected by the factor/source semantics and
        # the claim boundary; make the mutation unambiguously authority-changing.
        r["parameter_transport"]["squared_distance_note"] = "strictness changed"
        self.assertTrue(self.errors(r))

    def test_fixed_p_scope_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["parameter_transport", "finite_p_scope"], "p is encoded in the input")))

    def test_constant_400_guard_removal_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["parameter_transport", "constant_400_interpretation_prohibited"], False)))

    def test_nonvacuity_witness_count_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["nonvacuity", "no_witness_count"], 0)))

    def test_nonvacuity_witness_deletion_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][2]["nonvacuity_no"] = ""
        self.assertTrue(self.errors(r))

    def test_axiom_inflation_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["replay_and_axiom_audit"]["permitted_axioms_only"].append("Classical.propComplete")
        self.assertTrue(self.errors(r))

    def test_whole_source_interface_inflation_flag_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "whole_source_gapcvp_interface_identical"], True)))

    def test_malformed_no_inflation_flag_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "malformed_inputs_promoted_to_no"], True)))

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

    def test_head_change_reapproval_removal_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["activation", "head_change_requires_reapproval"], False)))

    def test_activation_must_not_authorize_solve(self):
        self.assertTrue(self.errors(self.mutate(["activation", "effect_does_not_authorize_solve"], False)))


if __name__ == "__main__":
    unittest.main()
