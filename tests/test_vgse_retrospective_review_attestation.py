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
    / "VGSE-SOURCE-PROVIDER-001.json"
)
SCHEMA_PATH = ROOT / "schemas" / "vgse_retrospective_review_attestation.schema.json"


class VGSERetrospectiveReviewAttestationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(RECORD_PATH.read_text(encoding="utf-8"))
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.validator = Draft202012Validator(
            schema, format_checker=FormatChecker()
        )

    def errors(self, instance: object) -> list[str]:
        return [error.message for error in self.validator.iter_errors(instance)]

    def test_committed_record_is_valid_and_fail_closed(self) -> None:
        self.assertEqual(self.errors(self.record), [])
        self.assertEqual(self.record["subject"]["pull_request"], 33)
        self.assertEqual(
            self.record["subject"]["head_sha"],
            "c42a663e67a6d8a57f8637e89e3f323226b152d9",
        )
        self.assertEqual(
            self.record["subject"]["merge_commit_sha"],
            "6f79cbca52992bf03ad025347f7416e4e8fa895c",
        )
        self.assertEqual(
            self.record["remedy_contract"]["required_event"], "APPROVED"
        )
        self.assertFalse(self.record["gate_effect"]["may_admit_campaign"])
        self.assertFalse(self.record["gate_effect"]["may_adjudicate_in_mathcert"])
        self.assertFalse(
            self.record["gate_effect"][
                "may_promote_mechanical_or_commercial_claims"
            ]
        )

    def test_comment_cannot_substitute_for_review(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["remedy_contract"]["conversation_comment_is_sufficient"] = True
        self.assertTrue(self.errors(mutated))

    def test_author_self_review_is_rejected(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["remedy_contract"][
            "reviewer_must_differ_from_original_author"
        ] = False
        self.assertTrue(self.errors(mutated))

    def test_historical_review_state_cannot_be_rewritten(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["historical_finding"]["submitted_review_count"] = 1
        mutated["historical_finding"]["review_gate_satisfied_at_merge"] = True
        self.assertTrue(self.errors(mutated))

    def test_subject_identity_cannot_drift(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["subject"]["merge_commit_sha"] = "0" * 40
        self.assertTrue(self.errors(mutated))

    def test_head_change_requires_reapproval(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["remedy_contract"]["reapproval_required_after_head_change"] = False
        self.assertTrue(self.errors(mutated))

    def test_review_remedy_cannot_promote_campaign_or_claims(self) -> None:
        mutated = copy.deepcopy(self.record)
        mutated["gate_effect"]["programme_candidate_state"] = "active"
        mutated["gate_effect"]["may_admit_campaign"] = True
        mutated["gate_effect"]["may_adjudicate_in_mathcert"] = True
        mutated["gate_effect"][
            "may_promote_mechanical_or_commercial_claims"
        ] = True
        self.assertTrue(self.errors(mutated))


if __name__ == "__main__":
    unittest.main()
