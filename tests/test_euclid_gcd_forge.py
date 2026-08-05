from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ci" / "validate_euclid_gcd_forge.py"
SPEC = importlib.util.spec_from_file_location("validate_euclid_gcd_forge", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

PACKAGE = json.loads(
    (ROOT / "sources" / "EUCLID-GCD-E2E-001" / "forge_package.json").read_text(encoding="utf-8")
)
SCHEMA = json.loads(
    (ROOT / "schemas" / "euclid_gcd_forge_package.schema.json").read_text(encoding="utf-8")
)


class EuclidGcdForgeTests(unittest.TestCase):
    def assert_rejected(self, mutation) -> None:
        candidate = copy.deepcopy(PACKAGE)
        mutation(candidate)
        self.assertTrue(MODULE.validate_package(candidate, SCHEMA))

    def test_canonical_package_is_valid(self) -> None:
        self.assertEqual(MODULE.validate_package(PACKAGE, SCHEMA), [])

    def test_changed_remainder_is_rejected(self) -> None:
        self.assert_rejected(lambda x: x["reconnaissance_ledger"]["euclidean_trace"][0].__setitem__("remainder", 41))

    def test_changed_quotient_is_rejected(self) -> None:
        self.assert_rejected(lambda x: x["reconnaissance_ledger"]["euclidean_trace"][1].__setitem__("quotient", 3))

    def test_non_decreasing_remainder_is_rejected(self) -> None:
        self.assert_rejected(lambda x: x["reconnaissance_ledger"]["euclidean_trace"][0].__setitem__("remainder", 105))

    def test_truncated_trace_is_rejected(self) -> None:
        self.assert_rejected(lambda x: x["reconnaissance_ledger"].__setitem__("euclidean_trace", x["reconnaissance_ledger"]["euclidean_trace"][:2]))

    def test_changed_bezout_coefficient_is_rejected(self) -> None:
        self.assert_rejected(lambda x: x["reconnaissance_ledger"]["bezout_witness"].__setitem__("x", -1))

    def test_zero_zero_widening_is_rejected(self) -> None:
        self.assert_rejected(lambda x: x["problem_card"]["input_contract"].__setitem__("excluded", []))

    def test_false_historical_attribution_is_rejected(self) -> None:
        def mutate(x):
            x["source_map"][1]["status"] = "verbatim_euclidean_bezout_theorem"
            x["source_map"][1]["support_scope"] = "Euclid proves the modern integer Bézout identity verbatim"
        self.assert_rejected(mutate)

    def test_candidate_cannot_claim_certification(self) -> None:
        self.assert_rejected(lambda x: x["claim_boundary"].__setitem__("certifies_candidate_witness", True))

    def test_missing_risk_is_rejected(self) -> None:
        self.assert_rejected(lambda x: x.__setitem__("failure_risks", x["failure_risks"][:-1]))

    def test_handoff_authority_inflation_is_rejected(self) -> None:
        self.assert_rejected(lambda x: x["solve_handoff"]["required_output"].__setitem__("authority_state", "certified"))


if __name__ == "__main__":
    unittest.main()
