"""Source-only regression tests for the pinned OpenAI Math 2026 intake."""
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"

def load_extractor():
    spec = importlib.util.spec_from_file_location("openai_math_replay", ROOT / "replay_index.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.extract

class OpenAIMathSourceTests(unittest.TestCase):
    def test_pdf_link_with_parentheses(self):
        text = (
            "<tbody><tr><td>**337. Integral fillings.**</td></tr></tbody>\n"
            "<tbody><tr><td>&emsp;[Sharp integral fillings in CAT(0) spaces]"
            "(preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf)"
            "</td></tr></tbody>"
        )
        families = load_extractor()(text)
        self.assertEqual(len(families), 1)
        self.assertEqual(
            families[0]["manuscripts"][0]["pdf_path"],
            "preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf"
        )

    def test_committed_index_cardinality_and_paths(self):
        obj = json.loads((ROOT / "MANUSCRIPT_INDEX.json").read_text(encoding="utf-8"))
        papers = [p for f in obj["families"] for p in f["manuscripts"]]
        paths = [p["pdf_path"] for p in papers]
        self.assertEqual((len(obj["families"]), len(paths), len(set(paths))), (372, 719, 719))
        self.assertTrue(all(x.startswith("preprints/") and x.endswith(".pdf") for x in paths))
        self.assertIn(
            "preprints/Sharp-integral-fillings-in-CAT(0)-spaces-September-23-2026/paper.pdf",
            paths
        )

    def test_upstream_formalization_crosswalk_is_noncertifying(self):
        obj = json.loads((ROOT / "FORMALIZATION_CROSSWALK.json").read_text(encoding="utf-8"))
        self.assertEqual(len(obj["source_papers"]), 173)
        self.assertEqual(len(obj["main_results"]), 200)
        self.assertEqual(sum(x["indexed_manuscript"] for x in obj["source_papers"]), 172)
        self.assertEqual(obj["review_status_upstream"], "unchecked")
        self.assertEqual(obj["lean_replay_status"], "NOT_RUN")
        self.assertEqual(obj["mathematical_certification"], "NOT_CLAIMED")
        self.assertEqual(len(obj["revision_exceptions"]), 1)
        self.assertEqual(obj["revision_exceptions"][0]["family_id"], "342")

if __name__ == "__main__":
    unittest.main()
