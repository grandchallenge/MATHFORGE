from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "binary_codes_semantic_validator",
    ROOT / "ci" / "validate_openai_ten_proofs_binary_codes_semantic.py",
)
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class BinaryCodesSemanticAuditTests(unittest.TestCase):
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

    def test_baseline(self):
        self.assertEqual(self.errors(), [])

    def test_top_level_schema_injection(self):
        r = copy.deepcopy(self.r)
        r["unregistered_authority"] = True
        self.assertTrue(self.errors(r))

    def test_open_schema(self):
        s = copy.deepcopy(self.s)
        s["additionalProperties"] = True
        self.assertTrue(self.errors(schema=s))

    def test_protected_base_drift(self):
        self.assertTrue(self.errors(self.mutate(["governance", "protected_base"], "0" * 40)))

    def test_source_digest_drift(self):
        self.assertTrue(self.errors(self.mutate(["source_authority", "pdf_sha256"], "0" * 64)))

    def test_formal_root_drift(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "root"], "0" * 40)))

    def test_solution_blob_drift(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "solution", "blob"], "0" * 40)))

    def test_target_substitution(self):
        r = copy.deepcopy(self.r)
        r["formal_authority"]["targets"][0] = "MetricCodes.unregistered"
        self.assertTrue(self.errors(r))

    def test_axiom_inflation(self):
        r = copy.deepcopy(self.r)
        r["replay_and_axiom_audit"]["permitted_axioms_only"].append("Classical.propComplete")
        self.assertTrue(self.errors(r))

    def test_log_base_drift(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"]["rate"] = r["definition_concordance"]["rate"].replace("base 2", "natural logarithm")
        self.assertTrue(self.errors(r))

    def test_ceiling_drift(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"]["rate"] = r["definition_concordance"]["rate"].replace("ceil(delta*n)", "floor(delta*n)")
        self.assertTrue(self.errors(r))

    def test_kappa_h_erasure(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"]["whole_cube"] = "uninterpreted variational bound"
        self.assertTrue(self.errors(r))

    def test_constant_weight_erasure(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"]["constant_weight"] = "uninterpreted shell bound"
        self.assertTrue(self.errors(r))

    def test_m2_minimum_bridge_erasure(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"]["second_mrrw"] = "mrrwRate is an sInf"
        self.assertTrue(self.errors(r))

    def test_positive_margin_promoted_to_verbatim_source(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "positive_margin_targets_source_printed_verbatim"], True)))

    def test_target_classification_inflation(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][1]["classification"] = "source_faithful_exact_projection"
        self.assertTrue(self.errors(r))

    def test_target_relation_erasure(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][3]["source_relation"] = "some strict bound"
        self.assertTrue(self.errors(r))

    def test_nonvacuity_code_number_erasure(self):
        r = copy.deepcopy(self.r)
        r["nonvacuity"]["evidence"] = [x for x in r["nonvacuity"]["evidence"] if "codeNumber_pos" not in x]
        self.assertTrue(self.errors(r))

    def test_nonvacuity_hamming_rate_set_erasure(self):
        r = copy.deepcopy(self.r)
        r["nonvacuity"]["evidence"] = [x for x in r["nonvacuity"]["evidence"] if "Hamming.rateSet_nonempty" not in x]
        self.assertTrue(self.errors(r))

    def test_nonvacuity_johnson_rate_set_erasure(self):
        r = copy.deepcopy(self.r)
        r["nonvacuity"]["evidence"] = [x for x in r["nonvacuity"]["evidence"] if "Johnson.rateSet_nonempty" not in x]
        self.assertTrue(self.errors(r))

    def test_minimizer_nonvacuity_erasure(self):
        r = copy.deepcopy(self.r)
        r["nonvacuity"]["evidence"] = [x for x in r["nonvacuity"]["evidence"] if "exists_mrrw_minimizer" not in x]
        self.assertTrue(self.errors(r))

    def test_proof_certification_inflation(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "proof_correctness_certified_here"], True)))

    def test_whole_chapter_inflation(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "whole_chapter_semantic_equivalence"], True)))

    def test_solve_authority_inflation(self):
        self.assertTrue(self.errors(self.mutate(["route_controls", "solve_handoff_authorized"], True)))

    def test_cert_authority_inflation(self):
        self.assertTrue(self.errors(self.mutate(["route_controls", "mathcert_route_authorized"], True)))

    def test_proved_target_inflation(self):
        self.assertTrue(self.errors(self.mutate(["route_controls", "mathematical_target_proved"], True)))

    def test_aggregate_authority_inflation(self):
        self.assertTrue(self.errors(self.mutate(["route_controls", "aggregate_openai_ten_proofs_authority"], True)))

    def test_review_gate_removal(self):
        self.assertTrue(self.errors(self.mutate(["activation", "requires_non_author_approved_review"], False)))

    def test_head_change_reapproval_removal(self):
        self.assertTrue(self.errors(self.mutate(["activation", "head_change_requires_reapproval"], False)))

    def test_material_change_steward_gate_removal(self):
        self.assertTrue(self.errors(self.mutate(["activation", "material_control_plan_change_requires_renewed_steward_input"], False)))


if __name__ == "__main__":
    unittest.main()
