from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_permanent_semantic_audit",
    ROOT / "ci/validate_openai_ten_proofs_permanent_semantic_audit.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OpenAITenProofsPermanentSourceLocusNormalizationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(MODULE.RECORD_PATH.read_text(encoding="utf-8"))

    def errors(self, record):
        return MODULE.validation_errors(record=record)

    def test_normalized_source_locus_is_schema_locked(self) -> None:
        self.assertEqual(self.errors(copy.deepcopy(self.record)), [])

    def test_symbolic_division_validity_drift_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        locus = record["manuscript_source"]["permanent_theorem_locus_pin_candidate"]
        locus["normalized_load_bearing_source"]["model"]["validity"] = (
            "every denominator is nonzero after every numerical specialization"
        )
        self.assertTrue(self.errors(record))

    def test_theorem_1_2_variable_leaf_constant_drift_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        locus = record["manuscript_source"]["permanent_theorem_locus_pin_candidate"]
        locus["normalized_load_bearing_source"]["theorem_1_2"]["variable_leaf_bound"] = (
            "Lvar(Phi) >= n^4 / (129 log_2 n)"
        )
        self.assertTrue(self.errors(record))

    def test_theorem_1_3_gate_constant_drift_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        locus = record["manuscript_source"]["permanent_theorem_locus_pin_candidate"]
        locus["normalized_load_bearing_source"]["theorem_1_3"]["gate_bound"] = (
            "G(Phi) >= n^4 / (385 log_2 n)"
        )
        self.assertTrue(self.errors(record))


if __name__ == "__main__":
    unittest.main()
