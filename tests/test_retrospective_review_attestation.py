from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
RECORD_PATH = (
    ROOT
    / "governance"
    / "review_attestations"
    / "OTP-EVIDENCE-CORR-001.json"
)
SCHEMA_PATH = ROOT / "schemas" / "retrospective_review_attestation.schema.json"


class RetrospectiveReviewAttestationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(RECORD_PATH.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.validator = Draft202012Validator(
            schema, format_checker=FormatChecker()
        )

    def errors(self, instance: object) -> list[str]:
        return [error.message for error in self.validator.iter_errors(instance)]

    def test_committed_remedy_contract_is_valid_and_fail_closed(self) -> None:
        self.assertEqual(self.errors(self.record), [])
        self.assertEqual(self.record["subject"]["pull_request"], 39)
        self.assertEqual(
            self.record["subject"]["head_sha"],
            "6dcf5d64f221f67a3f498578775a3ffb034801ff",
        )
        self.assertEqual(
            self.record["subject"]["merge_commit_sha"],
            "72452f4579749448169cacf9f2ab22a4df2bb182",
        )
        self.assertEqual(
            self.record["remedy_contract"]["required_event"], "APPROVED"
        )
        self.assertTrue(
            self.record["remedy_contract"][
                "reviewer_must_differ_from_original_author"
            ]
        )
        self.assertEqual(self.record["gate_effect"]["source_gate_clear_count"], 0)
        self.assertEqual(self.record["gate_effect"]["solve_handoffs_opened"], 0)
        self.assertFalse(self.record["gate_effect"]["may_promote_claims"])

    def test_conversation_comment_cannot_be_promoted_to_review(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["remedy_contract"]["conversation_comment_is_sufficient"] = True
        self.assertTrue(self.errors(mutated))

    def test_author_self_review_cannot_satisfy_remedy(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["remedy_contract"][
            "reviewer_must_differ_from_original_author"
        ] = False
        self.assertTrue(self.errors(mutated))

    def test_historical_review_count_cannot_be_rewritten(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["historical_finding"]["submitted_review_count"] = 1
        mutated["historical_finding"]["review_gate_satisfied_at_merge"] = True
        self.assertTrue(self.errors(mutated))

    def test_exact_subject_identity_cannot_drift(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["subject"]["head_sha"] = "0" * 40
        self.assertTrue(self.errors(mutated))

    def test_review_remedy_cannot_promote_downstream_gates(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["gate_effect"]["source_gate_clear_count"] = 1
        mutated["gate_effect"]["solve_handoffs_opened"] = 1
        mutated["gate_effect"]["may_adjudicate_in_mathcert"] = True
        mutated["gate_effect"]["may_promote_claims"] = True
        self.assertTrue(self.errors(mutated))

    def test_head_change_requires_reapproval(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["remedy_contract"]["reapproval_required_after_head_change"] = False
        self.assertTrue(self.errors(mutated))


if __name__ == "__main__":
    unittest.main()
