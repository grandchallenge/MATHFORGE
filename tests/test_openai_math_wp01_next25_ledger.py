"""Validate WP01 next25 evidence ledger without claiming mathematical certification."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
LEDGER = ROOT / "NEXT25_LEAN_RECEIPT_LEDGER.json"
PREFLIGHT = ROOT / "NEXT25_CONFIG_PREFLIGHT.json"
PINNED_HEAD = "9c3a18aec029998f4303b399d5dc09e6b7ce7059"
PINNED_UPSTREAM = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
AXIOMS = ["Classical.choice", "Quot.sound", "propext"]


class Next25LedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
        cls.preflight = json.loads(PREFLIGHT.read_text(encoding="utf-8"))

    def test_source_and_preflight_identity(self):
        source = self.ledger["source_identity"]
        self.assertEqual(source["gcl_workflow_head"], PINNED_HEAD)
        self.assertEqual(source["upstream_commit"], PINNED_UPSTREAM)
        payload = PREFLIGHT.read_bytes()
        oid = hashlib.sha1(b"blob " + str(len(payload)).encode() + b"\\0" + payload).hexdigest()
        self.assertEqual(source["preflight_blob_sha"], oid)
        self.assertEqual(len(self.preflight["rows"]), 25)

    def test_shards_and_archives(self):
        shards = self.ledger["shards"]
        self.assertEqual(len(shards), 5)
        self.assertEqual(sum(s["verified_internal_file_hashes"] for s in shards), 96)
        self.assertEqual([s["zero_based_global_range"] for s in shards],
                         [[i, i + 5] for i in range(25, 50, 5)])
        for s in shards:
            self.assertEqual(len(s["artifact_zip_sha256"]), 64)
            self.assertEqual(len(s["receipt_json_sha256"]), 64)
            self.assertEqual(s["original_attempt"], 1)
            self.assertTrue(s["workflow_run_url"].endswith(str(s["workflow_run_id"])))

    def test_exact_rows_and_claim_boundary(self):
        rows = self.ledger["rows"]
        self.assertEqual(len(rows), 25)
        self.assertEqual([r["global_index_zero_based"] for r in rows], list(range(25, 50)))
        for i, (r, p) in enumerate(zip(rows, self.preflight["rows"])):
            self.assertEqual(r["declaration"], p["declaration"])
            self.assertEqual(r["source_git_blob"], p["source_blob"])
            self.assertEqual(r["comparator_config_git_blob"], p["comparator_blob"])
            self.assertEqual(r["solution_module"], p["solution_module"])
            self.assertFalse(r["comparator_executed"])
            shard = self.ledger["shards"][i // 5]
            self.assertEqual((r["run_id"], r["artifact_id"]),
                             (shard["workflow_run_id"], shard["artifact_id"]))
            if r["global_index_zero_based"] in (43, 47):
                self.assertEqual(r["build_exit"], 124)
                self.assertIsNone(r["axioms_exit"])
                self.assertIsNone(r["observed_axioms"])
                self.assertNotEqual(r["verdict"], "LEAN_REPLAY_AND_AXS_PASS")
            else:
                self.assertEqual((r["build_exit"], r["axioms_exit"]), (0, 0))
                self.assertEqual(r["observed_axioms"], AXIOMS)
                self.assertEqual(r["extra_axioms"], [])
                self.assertEqual(r["verdict"], "LEAN_REPLAY_AND_AXS_PASS")
        self.assertEqual(self.ledger["counts"]["lean_axiom_pass"], 23)
        self.assertEqual(self.ledger["counts"]["build_timeout"], 2)
        self.assertIn("Comparator not executed", self.ledger["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
