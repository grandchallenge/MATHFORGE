from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class NsofSourceConcordanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(
            (ROOT / "sources" / "NSOF-001" / "source_revision_concordance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_official_source_and_screenshot_identities_remain_distinct(self) -> None:
        screenshot = self.record["intake_evidence"]
        manuscript = self.record["official_release"]["complete_manuscript"]
        self.assertEqual(
            screenshot["sha256"],
            "531d8b044623569e43949f094985c083e07cf3c0c6a7b6db6e0b5c3339b57420",
        )
        self.assertEqual(
            manuscript["sha256"],
            "f318c6508c9d49ef876a5a26cd73928705f96c07bb43e92a0cb35bd3f666ea53",
        )
        self.assertNotEqual(screenshot["sha256"], manuscript["sha256"])

    def test_screenshot_concordance_fails_closed_on_revision_identity(self) -> None:
        concordance = self.record["screenshot_to_source_concordance"]
        disposition = self.record["disposition"]
        self.assertEqual(concordance["attribution"], "concordant_openai")
        self.assertEqual(concordance["revision_identity"], "not_established")
        self.assertFalse(disposition["source_revision_concordance_complete"])
        self.assertFalse(disposition["may_route_to_solve"])
        self.assertFalse(disposition["may_adjudicate_in_mathcert"])

    def test_main_paper_and_stronger_target_are_not_conflated(self) -> None:
        manuscript = self.record["manuscript_scope"]
        route = self.record["stronger_finite_presentation_route"]
        self.assertFalse(manuscript["finitely_presented_claim_in_main_chapter"])
        self.assertIn("Section 3.11", route["official_reasoning_notes_locator"])
        self.assertEqual(
            route["solution_module"]["target"],
            "SoficGroups.SourceTopLevelCompressionFinal.exists_finitelyPresented_nonsofic_group",
        )

    def test_disconnected_roots_are_preserved(self) -> None:
        history = self.record["upstream_revision_history"]
        self.assertFalse(history["common_ancestor"])
        self.assertNotEqual(
            history["previously_locked_disconnected_root"],
            history["current_official_root"],
        )


if __name__ == "__main__":
    unittest.main()
