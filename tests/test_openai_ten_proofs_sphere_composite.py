from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "sphere_composite_validator",
    ROOT / "ci" / "validate_openai_ten_proofs_sphere_composite.py",
)
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class SphereCompositeSemanticTests(unittest.TestCase):
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

    def field(self, record, name):
        return next(x for x in record["field_audit"] if x["field"] == name)

    def test_current_record_passes(self):
        self.assertEqual(self.errors(), [])

    def test_field_deletion_is_rejected(self):
        r = copy.deepcopy(self.r)
        r["field_audit"].pop()
        self.assertTrue(self.errors(r))

    def test_field_insertion_is_rejected(self):
        r = copy.deepcopy(self.r)
        extra = copy.deepcopy(r["field_audit"][0])
        extra["field"] = "invented_field"
        r["field_audit"].append(extra)
        self.assertTrue(self.errors(r))

    def test_direct_source_inflation_is_rejected(self):
        r = copy.deepcopy(self.r)
        self.field(r, "root_before_infimum")["classification"] = "direct_source_theorem_projection"
        self.assertTrue(self.errors(r))

    def test_theorem_1_2_conflation_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "theorem_1_2_used_for_any_field"], True)))

    def test_decimal_source_authorship_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "decimal_precision_source_authored"], True)))

    def test_decimal_qualification_removal_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["disposition", "qualified_fields"], [])))

    def test_single_manuscript_theorem_inflation_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "composite_is_verbatim_single_source_theorem"], True)))

    def test_proof_certification_inflation_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "proof_correctness_certified_here"], True)))

    def test_whole_family_clearance_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "whole_family_semantic_clearance"], True)))

    def test_solve_authority_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "solve_authority"], True)))

    def test_cert_authority_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "cert_authority"], True)))

    def test_aggregate_authority_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["anti_overclaim", "aggregate_ten_proofs_authority"], True)))

    def test_packing_bridge_blocker_cannot_be_erased(self):
        self.assertTrue(self.errors(self.mutate(["disposition", "family_state_after_activation"], "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT")))

    def test_source_digest_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["source_authority", "pdf_sha256"], "0" * 64)))

    def test_formal_root_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "root"], "0" * 40)))

    def test_solution_blob_drift_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "solution", "blob"], "0" * 40)))

    def test_target_substitution_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["formal_authority", "target"], "PackingBounds.FullMain.exact_limit")))

    def test_nonvacuity_loss_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["nonvacuity", "state"], "blocked")))

    def test_review_gate_removal_is_rejected(self):
        self.assertTrue(self.errors(self.mutate(["activation", "condition"], "protected merge after CI")))

    def test_head_change_must_require_reapproval(self):
        self.assertTrue(self.errors(self.mutate(["activation", "head_change_requires_reapproval"], False)))


if __name__ == "__main__":
    unittest.main()
