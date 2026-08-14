from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_permanent_full_formula_consequences",
    ROOT / "ci" / "validate_openai_ten_proofs_permanent_full_formula_consequences.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class PermanentFullFormulaConsequencesTests(unittest.TestCase):
    def setUp(self):
        self.record = MODULE.load(MODULE.RECORD)

    def errors(self, record=None):
        return MODULE.validation_errors(copy.deepcopy(self.record if record is None else record))

    def mutate_projection(self, path, value):
        r = copy.deepcopy(self.record)
        target = r["source_projection"]
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
        return r

    def test_current_record_passes(self):
        self.assertEqual(self.errors(), [])

    def test_threshold_drift_rejected(self):
        self.assertTrue(self.errors(self.mutate_projection(["dimension_threshold"], 31)))

    def test_log_base_drift_rejected(self):
        self.assertTrue(self.errors(self.mutate_projection(["log_base"], 10)))

    def test_128_drift_rejected(self):
        self.assertTrue(self.errors(self.mutate_projection(["division_free", "variable_leaf_constant"], 129)))

    def test_256_drift_rejected(self):
        self.assertTrue(self.errors(self.mutate_projection(["division_free", "internal_gate_constant"], 255)))

    def test_192_drift_rejected(self):
        self.assertTrue(self.errors(self.mutate_projection(["rational", "vertex_count_constant"], 193)))

    def test_384_drift_rejected(self):
        self.assertTrue(self.errors(self.mutate_projection(["rational", "internal_gate_constant"], 383)))

    def test_circuit_inflation_rejected(self):
        r = copy.deepcopy(self.record)
        r["coverage"]["source_theorem_1_1_circuit_complexity"] = True
        self.assertTrue(self.errors(r))

    def test_pdf_equivalence_inflation_rejected(self):
        r = copy.deepcopy(self.record)
        r["coverage"]["historical_pdf_byte_equivalence"] = True
        self.assertTrue(self.errors(r))

    def test_premature_solve_route_rejected(self):
        r = copy.deepcopy(self.record)
        r["coverage"]["solve_handoff_for_new_targets"] = True
        self.assertTrue(self.errors(r))

    def test_premature_mathcert_route_rejected(self):
        r = copy.deepcopy(self.record)
        r["coverage"]["mathcert_route_for_new_targets"] = True
        self.assertTrue(self.errors(r))

    def test_adjudication_rejected(self):
        r = copy.deepcopy(self.record)
        r["coverage"]["adjudication"] = True
        self.assertTrue(self.errors(r))

    def test_cert_output_rejected(self):
        r = copy.deepcopy(self.record)
        r["coverage"]["cert_output"] = True
        self.assertTrue(self.errors(r))

    def test_proof_promotion_rejected(self):
        r = copy.deepcopy(self.record)
        r["coverage"]["mathematical_target_proved_promoted"] = True
        self.assertTrue(self.errors(r))

    def test_aggregate_promotion_rejected(self):
        r = copy.deepcopy(self.record)
        r["coverage"]["aggregate_ten_proofs_authority"] = True
        self.assertTrue(self.errors(r))

    def test_kernel_failure_rejected(self):
        r = copy.deepcopy(self.record)
        r["exact_overlay_replay"]["nanoda_kernel"] = "failed"
        self.assertTrue(self.errors(r))

    def test_archive_mutation_rejected(self):
        r = copy.deepcopy(self.record)
        r["exact_overlay_replay"]["immutable_archive_modified"] = True
        self.assertTrue(self.errors(r))


if __name__ == "__main__":
    unittest.main()
