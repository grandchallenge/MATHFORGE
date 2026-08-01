from __future__ import annotations

import copy
import json
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "reports" / "discovery" / "ns_ci_001" / "analytic_blocker_audit_02.json"


class NSCIR014AnalyticBlockerPassTwoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))

    def validate_fail_closed(self, audit: dict) -> list[str]:
        errors: list[str] = []
        findings = audit.get("findings", [])
        expected = {
            "R014-AF-005": ("R014-O09", "blocked_exact_gap"),
            "R014-AF-006": ("R014-O08", "not_clear"),
            "R014-AF-007": ("R014-O12", "blocked_statement_concordance"),
        }
        indexed = {item.get("finding_id"): item for item in findings}
        if set(indexed) != set(expected):
            errors.append("pass-two finding set drift")
        for finding_id, (obligation, status) in expected.items():
            finding = indexed.get(finding_id, {})
            if obligation not in finding.get("obligations", []):
                errors.append(f"{finding_id}: obligation drift")
            if finding.get("status") != status:
                errors.append(f"{finding_id}: status drift")
            if finding.get("may_mark_clear") is not False:
                errors.append(f"{finding_id}: unsupported clear permission")
            if not finding.get("blocking_gap"):
                errors.append(f"{finding_id}: missing exact gap")
            if len(finding.get("minimal_repair", [])) < 4:
                errors.append(f"{finding_id}: incomplete repair contract")

        verified = audit.get("verified_sublemmas", [])
        if len(verified) != 1:
            errors.append("expected one conditional verified sublemma")
        else:
            sublemma = verified[0]
            if sublemma.get("verification_id") != "R014-VS-001":
                errors.append("verified-sublemma identity drift")
            if sublemma.get("obligation") != "R014-O07":
                errors.append("verified-sublemma obligation drift")
            if sublemma.get("may_clear_obligation") is not False:
                errors.append("partial exponent replay cleared end-to-end obligation")
            if not sublemma.get("remaining_dependencies"):
                errors.append("verified sublemma lost dependency ledger")

        disposition = audit.get("obligation_disposition", {})
        if disposition.get("proof_obligation_clear_count") != 0:
            errors.append("proof-obligation clear count inflated")
        expected_dispositions = {
            "R014-O07": "not_clear_conditional_sublemma_verified",
            "R014-O08": "not_clear_imported_theorem_match",
            "R014-O09": "blocked_exact_gap",
            "R014-O12": "blocked_statement_concordance",
        }
        for obligation, status in expected_dispositions.items():
            if disposition.get(obligation) != status:
                errors.append(f"{obligation}: disposition drift")

        lane = audit.get("lane_disposition", {})
        for claim in ("axisymmetric_claim", "full_system_claim"):
            if lane.get(claim) != "INCOMPLETE_WITH_EXACT_GAPS":
                errors.append(f"{claim}: lane disposition drift")
        for field in (
            "may_change_programme_theorem_status",
            "may_route_to_mathsolve",
            "may_route_to_mathcert",
            "may_promote_global_regularity_claim",
        ):
            if lane.get(field) is not False:
                errors.append(f"downstream gate inflation: {field}")
        return errors

    def test_committed_pass_two_audit_is_fail_closed(self) -> None:
        self.assertEqual(self.validate_fail_closed(self.audit), [])

    def test_five_dimensional_parabolic_exponent(self) -> None:
        d = Fraction(5, 1)
        exponent = 2 * (d + 2) / d
        self.assertEqual(exponent, Fraction(14, 5))

    def test_three_dimensional_sobolev_and_serrin_arithmetic(self) -> None:
        p = Fraction(14, 5)
        p_star = 3 * p / (3 - p)
        serrin = 2 / p + Fraction(3, 1) / p_star
        self.assertEqual(p_star, 42)
        self.assertEqual(serrin, Fraction(11, 14))
        self.assertLess(serrin, 1)

    def test_partial_exponent_replay_cannot_clear_o07(self) -> None:
        mutated = copy.deepcopy(self.audit)
        mutated["verified_sublemmas"][0]["may_clear_obligation"] = True
        mutated["obligation_disposition"]["R014-O07"] = "clear"
        mutated["obligation_disposition"]["proof_obligation_clear_count"] = 1
        self.assertTrue(self.validate_fail_closed(mutated))

    def test_packet_order_gap_cannot_be_downgraded_without_repair(self) -> None:
        mutated = copy.deepcopy(self.audit)
        mutated["findings"][0]["status"] = "clear"
        mutated["findings"][0]["may_mark_clear"] = True
        self.assertTrue(self.validate_fail_closed(mutated))

    def test_version_concordance_cannot_be_inferred_from_shared_title(self) -> None:
        mutated = copy.deepcopy(self.audit)
        mutated["findings"][2]["status"] = "clear"
        self.assertTrue(self.validate_fail_closed(mutated))

    def test_imported_criterion_cannot_open_cert_route(self) -> None:
        mutated = copy.deepcopy(self.audit)
        mutated["lane_disposition"]["may_route_to_mathcert"] = True
        self.assertTrue(self.validate_fail_closed(mutated))


if __name__ == "__main__":
    unittest.main()
