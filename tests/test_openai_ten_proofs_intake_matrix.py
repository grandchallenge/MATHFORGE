from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

from ci.validate_forge import theorem_intake_matrix_instance_errors


ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = (
    ROOT / "sources" / "OPENAI-TEN-PROOFS-001" / "theorem_intake_matrix.json"
)
SCHEMA_PATH = ROOT / "schemas" / "theorem_intake_matrix.schema.json"


class OpenAITenProofsIntakeMatrixTests(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = json.loads(MATRIX_PATH.read_text(encoding="utf-8"))
        self.schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.validator = Draft202012Validator(
            self.schema, format_checker=FormatChecker()
        )

    def schema_errors(self, instance: object) -> list[str]:
        return [error.message for error in self.validator.iter_errors(instance)]

    def test_current_record_is_schema_valid_and_fail_closed(self) -> None:
        self.assertEqual(self.schema_errors(self.matrix), [])
        self.assertEqual(theorem_intake_matrix_instance_errors(self.matrix), [])
        self.assertEqual(len(self.matrix["result_families"]), 12)
        self.assertEqual(
            sum(len(family["theorem_names"]) for family in self.matrix["result_families"]),
            41,
        )
        self.assertEqual(
            sum(family["replay_gate"] == "clear" for family in self.matrix["result_families"]),
            12,
        )
        self.assertEqual(
            sum(family["source_gate"] == "clear" for family in self.matrix["result_families"]),
            0,
        )
        self.assertFalse(self.matrix["disposition"]["may_route_any_result"])
        self.assertEqual(self.matrix["disposition"]["solve_handoffs_opened"], 0)

    def test_route_inflation_mutation_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.matrix)
        mutated["result_families"][0]["may_route_to_solve"] = True
        mutated["disposition"]["may_route_any_result"] = True
        self.assertTrue(self.schema_errors(mutated))
        self.assertTrue(theorem_intake_matrix_instance_errors(mutated))

    def test_admitted_count_mutation_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.matrix)
        mutated["disposition"]["admitted_result_count"] = 1
        self.assertTrue(self.schema_errors(mutated))

    def test_source_gate_drift_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.matrix)
        mutated["result_families"][0]["source_gate"] = "clear"
        errors = theorem_intake_matrix_instance_errors(mutated)
        self.assertTrue(any("source-clear count" in error for error in errors))
        self.assertTrue(any("source_gate_clear_count" in error for error in errors))

    def test_disconnected_identity_collapse_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.matrix)
        mutated["source_identity"]["current_official_root"] = mutated["source_identity"][
            "previous_disconnected_intake_root"
        ]
        errors = theorem_intake_matrix_instance_errors(mutated)
        self.assertTrue(any("roots must remain distinct" in error for error in errors))

    def test_stale_connes_target_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.matrix)
        connes = next(
            family
            for family in mutated["result_families"]
            if family["result_id"] == "OTP-E-CONNES-RIGIDITY"
        )
        connes["theorem_names"] = ["ConnesRigidity.connesRigidityAssertion_false"]
        errors = theorem_intake_matrix_instance_errors(mutated)
        self.assertTrue(any("Connes Comparator targets" in error for error in errors))

    def test_aggregate_import_failure_cannot_be_erased(self) -> None:
        mutated = copy.deepcopy(self.matrix)
        mutated["trusted_replay"]["aggregate_all_import"]["state"] = "passed"
        self.assertTrue(self.schema_errors(mutated))
        errors = theorem_intake_matrix_instance_errors(mutated)
        self.assertTrue(any("All.lean failure" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
