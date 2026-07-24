import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = ROOT / "reports" / "discovery" / "ns_ci_001" / "false_proof_fixtures.json"


class NSCIFalseProofFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        with FIXTURE_PATH.open("r", encoding="utf-8") as handle:
            cls.payload = json.load(handle)
        cls.fixtures = {item["id"]: item for item in cls.payload["fixtures"]}

    def test_fixture_ledger_is_complete_and_unique(self) -> None:
        ids = [item["id"] for item in self.payload["fixtures"]]
        self.assertEqual(len(ids), 14)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), {f"FP-{index:03d}" for index in range(1, 15)})
        self.assertIn("do not refute", self.payload["claim_boundary"].lower())

    def test_fp001_exact_l2_not_l4_witness(self) -> None:
        alpha = Fraction(1, 3)
        self.assertLess(2 * alpha, 1, "t^(-alpha) must be square-integrable")
        self.assertGreaterEqual(4 * alpha, 1, "t^(-alpha) must fail fourth-power integrability")
        # Integral_0^1 t^(-2/3) dt = 1 / (1 - 2/3) = 3.
        self.assertEqual(Fraction(1, 1) / (1 - 2 * alpha), 3)
        self.assertEqual(self.fixtures["FP-001"]["expected_outcome"], "reject")

    def test_fp002_energy_interpolation_geometry(self) -> None:
        # Interpolate (q,p)=(infinity,2) with (2,6).
        theta_for_q4 = Fraction(1, 2)
        inverse_q = theta_for_q4 / 2
        inverse_p = (1 - theta_for_q4) / 2 + theta_for_q4 / 6
        self.assertEqual(inverse_q, Fraction(1, 4))
        self.assertEqual(inverse_p, Fraction(1, 3))

        # Requiring p=6 forces theta=1 and hence q=2.
        theta_for_p6 = Fraction(1, 1)
        self.assertEqual((1 - theta_for_p6) / 2 + theta_for_p6 / 6, Fraction(1, 6))
        self.assertEqual(theta_for_p6 / 2, Fraction(1, 2))

    def test_fp007_cutoff_loss_is_fourth_power(self) -> None:
        dimension = 3
        bernstein_exponent = dimension * (Fraction(1, 2) - Fraction(1, 6))
        self.assertEqual(bernstein_exponent, 1)
        self.assertEqual(4 * bernstein_exponent, 4)
        self.assertIn("N^4", self.fixtures["FP-007"]["exact_test"])

    def test_fp008_mollification_loss_is_fourth_power(self) -> None:
        dimension = 3
        smoothing_exponent = dimension * (Fraction(1, 2) - Fraction(1, 6))
        self.assertEqual(smoothing_exponent, 1)
        self.assertEqual(4 * smoothing_exponent, 4)
        self.assertIn("epsilon^(-4)", self.fixtures["FP-008"]["exact_test"])

    def test_fp012_exponent_order_is_not_interchangeable(self) -> None:
        critical_sum = Fraction(2, 4) + Fraction(3, 6)
        reversed_sum = Fraction(2, 6) + Fraction(3, 4)
        self.assertEqual(critical_sum, 1)
        self.assertEqual(reversed_sum, Fraction(13, 12))
        self.assertGreater(reversed_sum, 1)

    def test_all_fixtures_have_scope_and_protection_metadata(self) -> None:
        for fixture_id, fixture in self.fixtures.items():
            with self.subTest(fixture_id=fixture_id):
                self.assertTrue(fixture["false_claim"].strip())
                self.assertTrue(fixture["exact_test"].strip())
                self.assertTrue(fixture["expected_outcome"].strip())
                self.assertTrue(fixture["failure_class"].strip())
                self.assertTrue(fixture["protects"])


if __name__ == "__main__":
    unittest.main()
