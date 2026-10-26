"""Pinned source-accounting positive and hostile fixtures; not a theorem audit."""
from copy import deepcopy
import csv
import io
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
spec = importlib.util.spec_from_file_location("oai26_source_audit", ROOT/"audit_crosswalk.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class SourceCrosswalkAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = json.loads((ROOT/"MANUSCRIPT_INDEX.json").read_text())
        cls.crosswalk = json.loads((ROOT/"FORMALIZATION_CROSSWALK.json").read_text())
        cls.lock = json.loads((ROOT/"SOURCE_LOCK.json").read_text())

    def test_exact_pinned_ledger_and_byte_repeatability(self):
        got = mod.audit(self.index, self.crosswalk, self.lock)
        committed = json.loads((ROOT/"SOURCE_CROSSWALK_LEDGER.json").read_text())
        self.assertEqual(got, committed)
        s = got["summary"]
        self.assertEqual((s["family_count"], s["unique_catalogue_paths"]), (372, 719))
        self.assertEqual((s["source_record_count"], s["indexed_source_record_count"]), (173, 172))
        self.assertEqual((s["source_linked_family_count"], s["families_without_source_paper_match"]), (135, 237))
        self.assertEqual((s["distinct_declarations"], s["distinct_solution_file_paths"],
                          s["distinct_comparator_config_paths"]), (200, 192, 189))
        self.assertEqual(s["declarations_explicitly_bound_to_family"], 0)
        self.assertFalse(s["publisher_count_reconciled_to_declarations"])
        self.assertEqual(len(got["unindexed_source_editions"]), 1)
        self.assertIn("September-23", got["unindexed_source_editions"][0]["pdf_path"])
        self.assertTrue(all(row["family_id"] is None for row in got["declarations"]))
        self.assertEqual(got, mod.audit(self.index, self.crosswalk, self.lock))

    def test_csv_manuscript_and_declaration_projections(self):
        result = mod.audit(self.index, self.crosswalk, self.lock)
        first = mod.csv_ledgers(result)
        self.assertEqual(first, mod.csv_ledgers(result))
        for name, content in first.items():
            self.assertEqual((ROOT/name).read_text(encoding="utf-8"), content)
        manuscripts = list(csv.DictReader(io.StringIO(first["SOURCE_CROSSWALK_MANUSCRIPTS.csv"])))
        declarations = list(csv.DictReader(io.StringIO(first["SOURCE_CROSSWALK_DECLARATIONS.csv"])))
        self.assertEqual(len(manuscripts), 719)
        self.assertEqual({row["family_id"] for row in manuscripts},
                         {family["family_id"] for family in result["families"]})
        self.assertEqual({row["manuscript_path"] for row in manuscripts},
                         {m["pdf_path"] for family in result["families"]
                          for m in family["manuscripts"]})
        self.assertEqual(len(declarations), 200)
        self.assertEqual({row["declaration"] for row in declarations},
                         {entry["declaration"] for entry in result["declarations"]})
        self.assertTrue(all(row["family_id"] == "" and
                            row["family_binding"] == "UNRECONCILED" for row in declarations))
        self.assertTrue(all(row["declaration_family_edge"] == "UNRECONCILED"
                            for row in manuscripts))
        family337 = [row for row in manuscripts if row["family_id"] == "337"]
        self.assertEqual(len(family337), 2)
        self.assertEqual({row["source_paper_path_match"] for row in family337}, {"NO"})

    def test_duplicate_pdf_rejected(self):
        idx = deepcopy(self.index)
        idx["families"][1]["manuscripts"][0]["pdf_path"] = idx["families"][0]["manuscripts"][0]["pdf_path"]
        with self.assertRaisesRegex(ValueError, "duplicate catalogue PDF"):
            mod.audit(idx, self.crosswalk, self.lock)

    def test_duplicate_declaration_rejected(self):
        cw = deepcopy(self.crosswalk)
        cw["main_results"][1]["declaration"] = cw["main_results"][0]["declaration"]
        with self.assertRaisesRegex(ValueError, "duplicate qualified theorem"):
            mod.audit(self.index, cw, self.lock)

    def test_orphan_without_revision_exception_rejected(self):
        cw = deepcopy(self.crosswalk)
        cw["revision_exceptions"] = []
        with self.assertRaisesRegex(ValueError, "revision exception"):
            mod.audit(self.index, cw, self.lock)

    def test_false_indexed_flag_rejected(self):
        cw = deepcopy(self.crosswalk)
        cw["source_papers"][0]["indexed_manuscript"] = False
        with self.assertRaisesRegex(ValueError, "indexed_manuscript flag"):
            mod.audit(self.index, cw, self.lock)

    def test_source_lock_drift_rejected(self):
        lock = deepcopy(self.lock)
        lock["upstream"]["observed_commit"] = "0" * 40
        with self.assertRaisesRegex(ValueError, "source lock drift"):
            mod.audit(self.index, self.crosswalk, lock)

    def test_no_silent_replay_promotion(self):
        cw = deepcopy(self.crosswalk)
        cw["main_results"][0]["replay"] = "PASS"
        with self.assertRaisesRegex(ValueError, "source-only crosswalk row"):
            mod.audit(self.index, cw, self.lock)

    def test_wrong_upstream_git_blob_rejected(self):
        with self.assertRaisesRegex(ValueError, "differs from pinned"):
            mod.verify_upstream_yaml(b"changed source", self.crosswalk)


if __name__ == "__main__":
    unittest.main()
