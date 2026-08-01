from __future__ import annotations

import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORD_PATH = (
    ROOT
    / "reports"
    / "discovery"
    / "ns_ci_001"
    / "claimed_proof_triage_2026.json"
)


class NSCIClaimedProofTriage2026Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.record = json.loads(RECORD_PATH.read_text(encoding="utf-8"))
        cls.sources = {item["arxiv_id"]: item for item in cls.record["sources"]}
        cls.obligations = {
            item["id"]: item for item in cls.record["proof_obligations"]
        }
        cls.fixtures = {
            item["id"]: item
            for item in cls.record["manuscript_specific_fixtures"]
        }

    def test_exact_manuscript_family_is_locked(self) -> None:
        self.assertEqual(
            set(self.sources),
            {"2605.01875", "2605.01873", "2605.09797", "2606.07869"},
        )
        self.assertEqual(self.sources["2605.01875"]["version"], 3)
        self.assertEqual(self.sources["2605.01873"]["version"], 2)
        self.assertEqual(self.sources["2605.09797"]["version"], 2)
        self.assertEqual(self.sources["2606.07869"]["version"], 1)

    def test_full_system_companion_is_not_omitted(self) -> None:
        correction = self.record["scope_correction"]
        self.assertEqual(correction["required_companion_added"], "arXiv:2605.01873")
        self.assertIn("axisymmetric Part I", correction["reason"])
        self.assertIn("full-system Part II", correction["reason"])

    def test_axisymmetric_and_full_system_lanes_remain_separate(self) -> None:
        lanes = {item["lane_id"]: item for item in self.record["theorem_lanes"]}
        self.assertTrue(lanes["AXISYMMETRIC-SWIRL"]["must_be_audited_independently"])
        self.assertTrue(
            lanes["FULL-THREE-DIMENSIONAL"]["must_be_audited_independently"]
        )
        self.assertNotEqual(
            set(lanes["AXISYMMETRIC-SWIRL"]["sources"]),
            set(lanes["FULL-THREE-DIMENSIONAL"]["sources"]),
        )

    def test_every_proof_obligation_is_blocking(self) -> None:
        self.assertEqual(len(self.obligations), 12)
        self.assertEqual(
            {item["status"] for item in self.obligations.values()},
            {"unreviewed_blocking"},
        )
        self.assertEqual(self.record["disposition"]["proof_obligation_clear_count"], 0)

    def test_five_dimensional_parabolic_exponent_is_exact(self) -> None:
        dimension = 5
        exponent = Fraction(2 * (dimension + 2), dimension)
        self.assertEqual(exponent, Fraction(14, 5))
        self.assertIn("14/5", self.fixtures["R014-FP-005"]["exact_test"])

    def test_source_pairing_weight_cancellation_is_explicit(self) -> None:
        exact_test = self.fixtures["R014-FP-004"]["exact_test"]
        self.assertIn("2 integral G Gamma W dr dz", exact_test)
        obligation = self.obligations["R014-O05"]["requirement"]
        self.assertIn("2 Gamma W/r^3", obligation)
        self.assertIn("dmu5", obligation)

    def test_pdf_and_tex_digests_remain_fail_closed(self) -> None:
        for source in self.sources.values():
            self.assertIsNone(source["pdf_sha256"])
            self.assertIsNone(source["tex_sha256"])
        self.assertFalse(self.record["disposition"]["source_bytes_locked"])

    def test_no_theorem_status_or_certification_promotion(self) -> None:
        disposition = self.record["disposition"]
        self.assertEqual(disposition["axisymmetric_claim"], "UNRESOLVED")
        self.assertEqual(disposition["full_system_claim"], "UNRESOLVED")
        self.assertFalse(disposition["may_change_programme_theorem_status"])
        self.assertFalse(disposition["may_route_to_mathcert"])
        self.assertFalse(disposition["may_promote_global_regularity_claim"])

    def test_manuscript_specific_fixture_coverage(self) -> None:
        self.assertEqual(len(self.fixtures), 10)
        failure_classes = {item["failure_class"] for item in self.fixtures.values()}
        self.assertIn("CYLINDRICAL_MEASURE_DRIFT", failure_classes)
        self.assertIn("AXIS_BOUNDARY_DISPOSAL", failure_classes)
        self.assertIn("NEAR_AXIS_SINGULARITY", failure_classes)
        self.assertIn("CIRCULAR_ENERGY_SEEDING", failure_classes)
        self.assertIn("DESCENDANT_NONTERMINATION", failure_classes)
        self.assertIn("COMPACTNESS_GAP", failure_classes)
        self.assertIn("SYMMETRY_PROMOTION", failure_classes)
        self.assertIn("RESTRICTED_TO_GLOBAL_DRIFT", failure_classes)


if __name__ == "__main__":
    unittest.main()
