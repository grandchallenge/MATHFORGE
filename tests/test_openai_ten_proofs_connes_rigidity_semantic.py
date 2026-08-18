from __future__ import annotations
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VP = ROOT / "ci/validate_openai_ten_proofs_connes_rigidity_semantic.py"
spec = importlib.util.spec_from_file_location("validator", VP)
validator = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(validator)

def base_record():
    return json.loads(validator.RECORD.read_text(encoding="utf-8"))

def base_schema():
    return json.loads(validator.SCHEMA.read_text(encoding="utf-8"))

class ConnesRigiditySemanticAuditTests(unittest.TestCase):
    def reject(self, mutate):
        r = base_record()
        mutate(r)
        self.assertTrue(validator.validation_errors(record=r))

    def test_exact_record_validates(self):
        self.assertEqual([], validator.validation_errors())

    def test_namespace_alias_mutation_fails_closed(self):
        self.reject(lambda r: r["definition_concordance"].__setitem__(
            "namespace_identity",
            r["definition_concordance"]["namespace_identity"].replace("no alias", "alias inferred")))

    def test_icc_mutation_fails_closed(self):
        self.reject(lambda r: r["definition_concordance"].__setitem__(
            "countable_group_and_icc",
            r["definition_concordance"]["countable_group_and_icc"].replace("Infinite G", "Finite G")))

    def test_property_t_universe_mutation_fails_closed(self):
        self.reject(lambda r: r["anti_overclaim"].__setitem__(
            "universe_polymorphic_property_t_equivalence_claimed", True))

    def test_factor_structure_mutation_fails_closed(self):
        self.reject(lambda r: r["anti_overclaim"].__setitem__(
            "theorem_text_claims_trace_preserving_verbatim", True))

    def test_finite_generation_mutation_fails_closed(self):
        self.reject(lambda r: r["formal_authority"]["mathlib_finite_generation"].__setitem__(
            "blob", "0" * 40))

    def test_infinite_quantifier_mutation_fails_closed(self):
        self.reject(lambda r: r["definition_concordance"].__setitem__(
            "infinite_family_quantifiers",
            r["definition_concordance"]["infinite_family_quantifiers"].replace("every n", "some n")))

    def test_source_classification_inflation_fails_closed(self):
        self.reject(lambda r: r["target_audits"][1].__setitem__(
            "classification", "verbatim_source_theorem"))

    def test_replay_mutation_fails_closed(self):
        self.reject(lambda r: r["formal_authority"]["replay"].__setitem__(
            "job_id", 0))

    def test_downstream_authority_inflation_fails_closed(self):
        self.reject(lambda r: r["route_controls"].__setitem__(
            "mathcert_route_authorized", True))

    def test_schema_must_remain_closed(self):
        s = base_schema()
        s["additionalProperties"] = True
        self.assertTrue(validator.validation_errors(schema=s))

if __name__ == "__main__":
    unittest.main()
