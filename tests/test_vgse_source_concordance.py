from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_vgse_source_concordance",
    ROOT / "tools" / "verify_vgse_source_concordance.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VgseSourceConcordanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(
            (ROOT / "sources" / "VGSE-001" / "source_revision_concordance.json").read_text(
                encoding="utf-8"
            )
        )

    def test_normalization_allows_only_recorded_packaging_differences(self) -> None:
        author = "Date: June 3, 2026\nExample B.1 Proposition B.2"
        arxiv = (
            "arXiv:2410.09574v2 [hep-th] 3 Jun 2026\n"
            "Date: June 4, 2026\nExample B.1 Proposition B.2"
        )
        self.assertEqual(MODULE.normalize(author), MODULE.normalize(arxiv))

    def test_source_and_reconstruction_are_disjoint(self) -> None:
        transcription = self.record["source_transcription"]
        direct = set(transcription["directly_stated"])
        reconstructed = set(transcription["not_source_transcribed"])
        self.assertFalse(direct & reconstructed)
        self.assertIn("the Example B.1 matrix C", direct)
        self.assertIn("the positive numerical graph weights and Kasteleyn representative", reconstructed)

    def test_provider_verification_does_not_inflate_lifecycle_or_claims(self) -> None:
        disposition = self.record["disposition"]
        self.assertEqual(disposition["author_pdf_identity"], "provider_verified")
        self.assertEqual(disposition["mathematical_certification"], "not_performed")
        self.assertEqual(disposition["campaign_admission"], "not_authorized")
        self.assertEqual(disposition["commercial_claims"], "prohibited")


if __name__ == "__main__":
    unittest.main()
