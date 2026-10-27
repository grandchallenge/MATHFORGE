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
        oid = hashlib.sha1(b"blob " + str(len(payload)).encode() + bytes([0]) + payload).hexdigest()
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


    def test_extended_replay_receipts_and_effective_counts(self):
        x = self.ledger["extended_replays"]
        self.assertEqual([r["global_index_zero_based"] for r in x], [43, 47])
        self.assertEqual([r["run_id"] for r in x], [40500508252, 40500513211])
        self.assertEqual([r["artifact_id"] for r in x], [12736906287, 12734374033])
        self.assertEqual([r["build_exit"] for r in x], [124, 0])
        self.assertEqual([r["axioms_exit"] for r in x], [None, 0])
        self.assertEqual([r["verdict"] for r in x],
                         ["BUILD_TIMEOUT_4200S_NO_AXIOM_AUDIT", "LEAN_REPLAY_AND_AXS_PASS"])
        self.assertEqual(x[1]["observed_axioms"], AXIOMS)
        self.assertEqual(x[1]["extra_axioms"], [])
        self.assertIsNone(x[0]["observed_axioms"])
        self.assertTrue(all(not r["comparator_executed"] for r in x))
        self.assertTrue(all(r["workflow_head"] == "99fd03a672cd7d83dea317d3b4f3ad2441a746a9" for r in x))
        self.assertTrue(all(r["upstream_commit"] == PINNED_UPSTREAM for r in x))
        self.assertTrue(all(r["toolchain"] == "leanprover/lean4:v4.34.1" and r["build_timeout_seconds"] == 4200 for r in x))
        self.assertTrue(all(len(r["artifact_zip_sha256"]) == 64 and len(r["receipt_json_sha256"]) == 64 for r in x))
        self.assertEqual(sum(r["verified_internal_file_hashes"] for r in x), 14)
        self.assertEqual(self.ledger["counts"]["effective_lean_axiom_pass"], 24)
        self.assertEqual(self.ledger["counts"]["effective_build_timeout"], 1)
        self.assertEqual(self.ledger["counts"]["extended_archive_sha256_verified"], 2)
        self.assertEqual(self.ledger["counts"]["extended_internal_file_sha256_verified"], 14)
        self.assertIn("4200s", self.ledger["remaining_obligation"])

    def test_diagnostic_replay_identity_and_timeout_evidence(self):
        rows = self.ledger["diagnostic_replays"]
        self.assertEqual(len(rows), 1)
        row = rows[0]
        self.assertEqual(row["global_index_zero_based"], 43)
        self.assertEqual(row["declaration"], self.preflight["rows"][18]["declaration"])
        self.assertEqual(row["run_id"], 40548732401)
        self.assertEqual(row["workflow_head"], "8ebcb65d3ba8bf10e376c0daba9b8e37f0834aad")
        self.assertEqual(row["upstream_commit"], PINNED_UPSTREAM)
        self.assertEqual(row["toolchain"], "leanprover/lean4:v4.34.1")
        self.assertEqual(row["build_timeout_seconds"], 4200)
        self.assertEqual(row["artifact_id"], 12761280403)
        self.assertEqual(row["artifact_zip_sha256"],
                         "39df37faeb899a02ba36fd5140b850c054ee750b07e5606a2951f08cefef00bf")
        self.assertEqual(row["receipt_json_sha256"],
                         "80fb4fc5657f672a80ed050c0723fac2b9a3fb17b99e5818cf236d3186a87849")
        self.assertEqual(row["build_log_sha256"],
                         "ab9807addcc92f72ddb908e6f27f4a72c45acddccab92bf1967e248b22df7ffa")
        self.assertEqual((row["build_exit"], row["axioms_exit"]), (124, None))
        self.assertIsNone(row["observed_axioms"])
        self.assertFalse(row["comparator_executed"])
        self.assertEqual(row["diagnostic"]["last_observed_lake_step"], "5459/7061")
        self.assertTrue(row["diagnostic"]["partial_stdout_captured"])
        self.assertTrue(row["diagnostic"]["progress_denominator_dynamic"])
        self.assertEqual(row["verified_internal_file_hashes"], 6)
        self.assertEqual(self.ledger["counts"]["diagnostic_archive_sha256_verified"], 1)
        self.assertEqual(self.ledger["counts"]["diagnostic_internal_file_sha256_verified"], 6)
        self.assertEqual(self.ledger["counts"]["effective_lean_axiom_pass"], 24)

if __name__ == "__main__":
    unittest.main()
