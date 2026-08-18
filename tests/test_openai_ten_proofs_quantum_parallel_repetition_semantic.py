from __future__ import annotations
import copy
import json
import unittest
from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "ci/validate_openai_ten_proofs_quantum_parallel_repetition_semantic.py"
spec = importlib.util.spec_from_file_location("otp_g_qpr_semantic_validator", MODULE)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)

RECORD = json.loads(validator.RECORD.read_text(encoding="utf-8"))
SCHEMA = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))

class QuantumParallelRepetitionSemanticAuditTests(unittest.TestCase):
    def test_exact_record_validates(self):
        self.assertEqual([], validator.validation_errors(copy.deepcopy(RECORD), copy.deepcopy(SCHEMA)))

    def test_target_mutation_fails_closed(self):
        r = copy.deepcopy(RECORD)
        r["formal_authority"]["targets"][0] = "QuantumParallelRepetition.not_the_target"
        self.assertTrue(validator.validation_errors(r, copy.deepcopy(SCHEMA)))

    def test_strategy_dimension_semantics_mutation_fails_closed(self):
        r = copy.deepcopy(RECORD)
        r["definition_concordance"]["strategy_model"] = "fixed common dimension"
        self.assertTrue(validator.validation_errors(r, copy.deepcopy(SCHEMA)))

    def test_supremum_attainment_mutation_fails_closed(self):
        r = copy.deepcopy(RECORD)
        r["definition_concordance"]["entangled_value"] = "maximum over attained optimizers"
        self.assertTrue(validator.validation_errors(r, copy.deepcopy(SCHEMA)))

    def test_exponent_denominator_quantifier_mutation_fails_closed(self):
        r = copy.deepcopy(RECORD)
        r["definition_concordance"]["gap_exponent_denominator"] = "epsilon squared"
        self.assertTrue(validator.validation_errors(r, copy.deepcopy(SCHEMA)))

    def test_empty_answer_overclaim_fails_closed(self):
        r = copy.deepcopy(RECORD)
        r["anti_overclaim"]["empty_answer_extension_claimed_as_manuscript_scope"] = True
        self.assertTrue(validator.validation_errors(r, copy.deepcopy(SCHEMA)))

    def test_downstream_authority_inflation_fails_closed(self):
        r = copy.deepcopy(RECORD)
        r["route_controls"]["solve_handoff_authorized"] = True
        self.assertTrue(validator.validation_errors(r, copy.deepcopy(SCHEMA)))

    def test_schema_must_remain_closed(self):
        s = copy.deepcopy(SCHEMA)
        s["additionalProperties"] = True
        self.assertTrue(validator.validation_errors(copy.deepcopy(RECORD), s))

if __name__ == "__main__":
    unittest.main()
