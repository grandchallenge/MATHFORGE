from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "reports" / "discovery" / "ns_ci_001" / "analytic_blocker_audit_01.json"


class NSCIR014AnalyticBlockerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = json.loads(AUDIT_PATH.read_text(encoding="utf-8"))

    def validate_fail_closed(self, audit: dict) -> list[str]:
        errors: list[str] = []
        findings = audit.get("findings", [])
        finding_ids = [item.get("finding_id") for item in findings]
        if len(findings) != 4 or len(finding_ids) != len(set(finding_ids)):
            errors.append("audit must contain four unique initial findings")

        required_obligations = {"R014-O05", "R014-O06", "R014-O10", "R014-O11"}
        covered = {
            obligation
            for finding in findings
            for obligation in finding.get("obligations", [])
        }
        if covered != required_obligations:
            errors.append("initial blocker obligation coverage drift")

        for finding in findings:
            if finding.get("status") != "blocked_exact_gap":
                errors.append(f"{finding.get('finding_id')}: blocker status drift")
            if finding.get("may_mark_clear") is not False:
                errors.append(f"{finding.get('finding_id')}: unsupported clear permission")
            if not finding.get("blocking_gap"):
                errors.append(f"{finding.get('finding_id')}: missing exact gap")
            if len(finding.get("minimal_repair", [])) < 4:
                errors.append(f"{finding.get('finding_id')}: incomplete repair contract")

        obligation_disposition = audit.get("obligation_disposition", {})
        if obligation_disposition.get("proof_obligation_clear_count") != 0:
            errors.append("proof obligation clear count must remain zero")
        for obligation in required_obligations:
            if obligation_disposition.get(obligation) != "blocked_exact_gap":
                errors.append(f"{obligation}: disposition drift")

        lane = audit.get("lane_disposition", {})
        if lane.get("axisymmetric_claim") != "INCOMPLETE_WITH_EXACT_GAPS":
            errors.append("axisymmetric lane disposition drift")
        if lane.get("full_system_claim") != "INCOMPLETE_WITH_EXACT_GAPS":
            errors.append("full-system lane disposition drift")
        for field in (
            "may_change_programme_theorem_status",
            "may_route_to_mathsolve",
            "may_route_to_mathcert",
            "may_promote_global_regularity_claim",
        ):
            if lane.get(field) is not False:
                errors.append(f"downstream gate inflation: {field}")
        return errors

    def test_committed_audit_is_fail_closed(self) -> None:
        self.assertEqual(self.validate_fail_closed(self.audit), [])

    def test_finding_cannot_be_marked_clear_without_repair(self) -> None:
        mutated = copy.deepcopy(self.audit)
        mutated["findings"][0]["status"] = "clear"
        mutated["findings"][0]["may_mark_clear"] = True
        self.assertTrue(self.validate_fail_closed(mutated))

    def test_obligation_clear_count_cannot_inflate(self) -> None:
        mutated = copy.deepcopy(self.audit)
        mutated["obligation_disposition"]["proof_obligation_clear_count"] = 1
        self.assertTrue(self.validate_fail_closed(mutated))

    def test_downstream_route_cannot_open(self) -> None:
        mutated = copy.deepcopy(self.audit)
        mutated["lane_disposition"]["may_route_to_mathsolve"] = True
        mutated["lane_disposition"]["may_route_to_mathcert"] = True
        self.assertTrue(self.validate_fail_closed(mutated))

    def test_falsity_is_not_inferred_from_incompleteness(self) -> None:
        boundary = self.audit["method"]["falsity_boundary"].lower()
        self.assertIn("does not prove", boundary)
        self.assertIn("false", boundary)

    def test_source_lock_is_exactly_pinned(self) -> None:
        lock = self.audit["source_lock"]
        self.assertEqual(
            lock["source_lock_head"],
            "cd064e92d82c7426b42234c075b48553173e0625",
        )
        self.assertEqual(
            set(lock["exact_versions"]),
            {
                "2605.01875v3",
                "2605.01873v2",
                "2605.09797v2",
                "2606.07869v1",
            },
        )


if __name__ == "__main__":
    unittest.main()
