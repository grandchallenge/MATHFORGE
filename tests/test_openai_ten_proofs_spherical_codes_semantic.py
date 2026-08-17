from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "spherical_codes_semantic_validator",
    ROOT / "ci" / "validate_openai_ten_proofs_spherical_codes_semantic.py",
)
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class SphericalCodesSemanticAuditTests(unittest.TestCase):
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

    def test_config_blob_drift(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "config", "blob"], "0" * 40)))

    def test_challenge_blob_drift(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "challenge", "blob"], "0" * 40)))

    def test_solution_blob_drift(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "solution", "blob"], "0" * 40)))

    def test_target_substitution(self):
        r = copy.deepcopy(self.r)
        r["formal_authority"]["targets"][0] = "MetricCodes.unregistered"
        self.assertTrue(self.errors(r))

    def test_predecessor_seven_target_authority_inflation(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "predecessor_target_surface_authority_transferred"], True)))

    def test_target_surface_drift_erasure(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "target_surface_drift"], "no_drift")))

    def test_binary_domain_drift(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"]["binary_surface"] = r["definition_concordance"]["binary_surface"].replace("0<delta<1/2", "0<=delta<1/2")
        self.assertTrue(self.errors(r))

    def test_spherical_domain_drift(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"]["spherical_code"] = r["definition_concordance"]["spherical_code"].replace("0<s<1", "-1<s<1")
        self.assertTrue(self.errors(r))

    def test_r_zero_erasure(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"]["hierarchy"] = r["definition_concordance"]["hierarchy"].replace("r=0", "r=1")
        self.assertTrue(self.errors(r))

    def test_closed_hierarchy_orientation_drift(self):
        r = copy.deepcopy(self.r)
        r["definition_concordance"]["hierarchy"] = r["definition_concordance"]["hierarchy"].replace("2*Gamma>=s", "2*Gamma>s")
        self.assertTrue(self.errors(r))

    def test_strict_hierarchy_classification_drift(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][2]["classification"] = "derived_internal_certificate"
        self.assertTrue(self.errors(r))

    def test_numerical_target_promoted_to_exact_source_projection(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][3]["classification"] = "source_faithful_exact_projection"
        self.assertTrue(self.errors(r))

    def test_source_o1_erasure(self):
        r = copy.deepcopy(self.r)
        r["target_audits"][3]["source_relation"] = "The source prints an eventual exact 0.39661 exponent."
        self.assertTrue(self.errors(r))

    def test_numerical_source_verbatim_inflation(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "numerical_target_source_printed_verbatim"], True)))

    def test_exact_eventual_manuscript_inflation(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "exact_039661_eventual_bound_claimed_as_manuscript_statement"], True)))

    def test_nonvacuity_binary_erasure(self):
        r = copy.deepcopy(self.r)
        r["nonvacuity"]["evidence"] = [x for x in r["nonvacuity"]["evidence"] if "delta=1/4" not in x]
        self.assertTrue(self.errors(r))

    def test_nonvacuity_singleton_erasure(self):
        r = copy.deepcopy(self.r)
        r["nonvacuity"]["evidence"] = [x for x in r["nonvacuity"]["evidence"] if "singleton unit-vector code" not in x]
        self.assertTrue(self.errors(r))

    def test_nonvacuity_hierarchy_erasure(self):
        r = copy.deepcopy(self.r)
        r["nonvacuity"]["evidence"] = [x for x in r["nonvacuity"]["evidence"] if "Gamma=sqrt(2)/3" not in x]
        self.assertTrue(self.errors(r))

    def test_nonvacuity_localization_erasure(self):
        r = copy.deepcopy(self.r)
        r["nonvacuity"]["evidence"] = [x for x in r["nonvacuity"]["evidence"] if "Icc 0 s" not in x]
        self.assertTrue(self.errors(r))

    def test_replay_job_drift(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "replay", "job_id"], 0)))

    def test_axiom_inflation(self):
        r = copy.deepcopy(self.r)
        r["replay_and_axiom_audit"]["permitted_axioms_only"].append("Classical.propComplete")
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
