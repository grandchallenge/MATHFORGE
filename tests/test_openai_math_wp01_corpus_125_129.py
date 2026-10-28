"""Bounded source-pinned 125-129 WP01 Lean evidence, not Comparator certification."""
import copy
import csv
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
LEDGER = ROOT / "CORPUS_125_129_LEAN_RECEIPT_LEDGER.json"
CROSSWALK = ROOT / "SOURCE_CROSSWALK_DECLARATIONS.csv"
UPSTREAM = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
RUN = 40601315624
ARTIFACT = 12779820307
AXIOMS = {"Classical.choice", "Quot.sound", "propext"}

def accepted(d, source_rows):
    if d.get("record_type") != "GCL_OAI26_WP01_CORPUS_REPLAY_125_129/1":
        return False
    if d["source"]["commit"] != UPSTREAM or d["source"]["toolchain"] != "leanprover/lean4:v4.34.1":
        return False
    w = d["workflow"]
    if (w["run_id"], w["artifact_id"], w["corpus_range"]) != (RUN, ARTIFACT, [125, 130]):
        return False
    if w["gcl_head"] != "1c1e906d108844b50eac96c51232406f32fdadd5":
        return False
    if w["status"] != "completed" or w["conclusion"] != "success":
        return False
    if d["verification"]["internal_files_sha256_verified"] != 20 or d["verification"]["row_build_axiom_logs_sha256_verified"] != 10:
        return False
    if d["counts"] != {"unique_indices": 5, "lean_axiom_pass": 5, "build_timeout": 0, "comparator_executed": 0}:
        return False
    if len(source_rows) != 200 or len(d["rows"]) != 5:
        return False
    for index, row in enumerate(d["rows"], 125):
        ref = source_rows[index]
        if row.get("index_zero_based") != index or row.get("declaration") != ref["declaration"]:
            return False
        if row.get("comparator_config") != ref["comparator_config"]:
            return False
        if (row.get("run_id"), row.get("artifact_id")) != (RUN, ARTIFACT):
            return False
        if row.get("build_exit") != 0 or row.get("axioms_exit") != 0:
            return False
        if row.get("verdict") != "LEAN_REPLAY_AND_AXS_PASS":
            return False
        if row.get("extra_axioms") != [] or set(row.get("observed_axioms", [])) - AXIOMS:
            return False
        if row.get("comparator_executed") is not False:
            return False
        if len(row.get("source_git_blob", "")) != 40 or len(row.get("comparator_git_blob", "")) != 40:
            return False
        if len(row.get("build_log_sha256", "")) != 64 or len(row.get("axioms_log_sha256", "")) != 64:
            return False
    return True

class TestCorpus125129(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(LEDGER.read_text())
        with CROSSWALK.open(newline="") as f:
            cls.cross = list(csv.DictReader(f))

    def test_source_pinned_positive(self):
        self.assertTrue(accepted(self.data, self.cross))

    def test_hostile_drift_rejected(self):
        cases = [
            ("index_collision", lambda d: d["rows"][1].__setitem__("index_zero_based", 125)),
            ("fabricated_theorem", lambda d: d["rows"][2].__setitem__("declaration", "OAI.Forged.main")),
            ("unapproved_axiom", lambda d: d["rows"][2].__setitem__("extra_axioms", ["sorryAx"])),
            ("comparator_claim", lambda d: d["rows"][3].__setitem__("comparator_executed", True)),
            ("false_build_success", lambda d: d["rows"][1].__setitem__("build_exit", 124)),
            ("source_head_drift", lambda d: d["source"].__setitem__("commit", "0" * 40)),
            ("artifact_drift", lambda d: d["workflow"].__setitem__("artifact_id", 1)),
        ]
        for label, modify in cases:
            with self.subTest(label=label):
                bad = copy.deepcopy(self.data)
                modify(bad)
                self.assertFalse(accepted(bad, self.cross))

if __name__ == "__main__":
    unittest.main()
