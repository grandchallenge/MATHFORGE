from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADOPTION_PATH = (
    ROOT
    / "reports"
    / "discovery"
    / "ns_ci_001"
    / "source_lock_adoption_for_analytic_audit_01.json"
)


class NSCIR014SourceLockAdoptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.record = json.loads(ADOPTION_PATH.read_text(encoding="utf-8"))

    def validate(self, record: dict) -> list[str]:
        errors: list[str] = []
        lock = record.get("source_lock", {})
        review = lock.get("submitted_review", {})
        gate = record.get("gate_effect", {})
        adoption = record.get("adoption", {})

        if lock.get("pull_request") != 45:
            errors.append("source-lock PR drift")
        if lock.get("exact_head_sha") != "cd064e92d82c7426b42234c075b48553173e0625":
            errors.append("source-lock head drift")
        if lock.get("merge_commit_sha") != "53336812a5b8f806d907d3e7fcbc79f11bca45b8":
            errors.append("source-lock merge drift")
        if review.get("state") != "APPROVED":
            errors.append("source-lock review is not approved")
        if review.get("reviewer") != "jimsteeg":
            errors.append("source-lock reviewer drift")
        if review.get("reviewer_differs_from_author") is not True:
            errors.append("source-lock review independence lost")
        if adoption.get("analytic_audit_base") != "main":
            errors.append("analytic audit must target main")
        if adoption.get("source_revision_substitution_permitted") is not False:
            errors.append("unlocked source substitution permitted")
        if adoption.get("newer_source_requires_new_lock") is not True:
            errors.append("newer source may bypass source lock")
        if gate.get("source_bytes_locked") is not True:
            errors.append("source-byte lock lost")
        if gate.get("proof_obligation_clear_count") != 0:
            errors.append("source lock improperly clears analytic obligations")
        for field in (
            "may_change_programme_theorem_status",
            "may_route_to_mathsolve",
            "may_route_to_mathcert",
            "may_promote_global_regularity_claim",
        ):
            if gate.get(field) is not False:
                errors.append(f"downstream gate inflation: {field}")
        return errors

    def test_committed_adoption_is_valid_and_fail_closed(self) -> None:
        self.assertEqual(self.validate(self.record), [])

    def test_review_cannot_be_removed(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["source_lock"]["submitted_review"]["state"] = "COMMENTED"
        self.assertTrue(self.validate(mutated))

    def test_source_revision_cannot_be_substituted(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["adoption"]["source_revision_substitution_permitted"] = True
        self.assertTrue(self.validate(mutated))

    def test_source_lock_cannot_clear_proof_obligation(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["gate_effect"]["proof_obligation_clear_count"] = 1
        self.assertTrue(self.validate(mutated))

    def test_source_lock_cannot_open_downstream_route(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["gate_effect"]["may_route_to_mathcert"] = True
        self.assertTrue(self.validate(mutated))


if __name__ == "__main__":
    unittest.main()
