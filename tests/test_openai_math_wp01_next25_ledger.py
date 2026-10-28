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
        self.assertEqual(self.ledger["counts"]["effective_lean_axiom_pass"], 25)
        self.assertEqual(self.ledger["counts"]["effective_build_timeout"], 0)
        self.assertEqual(self.ledger["counts"]["extended_archive_sha256_verified"], 2)
        self.assertEqual(self.ledger["counts"]["extended_internal_file_sha256_verified"], 14)
        self.assertIn("No remaining Lean/axiom replay obligation", self.ledger["remaining_obligation"])


    def test_staged_index43_receipt_and_effective_coverage(self):
        import copy

        ledger = self.ledger
        staged = ledger["staged_replays"]
        self.assertEqual(len(staged), 1)
        row = staged[0]
        original = ledger["rows"][43 - 25]

        def admissible(candidate):
            return (
                candidate["global_index_zero_based"] == 43
                and candidate["declaration"] == original["declaration"]
                and candidate["solution_git_blob"] == original["source_git_blob"]
                and candidate["comparator_config_git_blob"] == original["comparator_config_git_blob"]
                and candidate["workflow_run_id"] == 40610405028
                and candidate["workflow_conclusion"] == "success"
                and candidate["workflow_head"] == "d98ca6719e08956068a5f1ff9c48c1dc889fd94b"
                and candidate["upstream_commit"] == PINNED_UPSTREAM
                and candidate["upstream_tree"] == ledger["source_identity"]["upstream_tree"]
                and candidate["upstream_manifest_sha256"] == ledger["source_identity"]["upstream_manifest_sha256"]
                and candidate["toolchain"] == "leanprover/lean4:v4.34.1"
                and candidate["prewarm_exit"] == 124
                and candidate["prewarm_budget_seconds"] == 4200
                and candidate["prewarm_elapsed_seconds"] == 4200
                and candidate["target_build_budget_seconds"] == 4200
                and candidate["build_exit"] == candidate["axioms_exit"] == 0
                and candidate["observed_axioms"] == AXIOMS
                and candidate["extra_axioms"] == []
                and candidate["verdict"] == "LEAN_REPLAY_AND_AXS_PASS"
                and candidate["comparator_executed"] is False
                and candidate["artifact_id"] == 12787250318
                and candidate["artifact_zip_sha256"] == "6d21737e67e09cf873f29b6e1af156c68c6fd9be53fe22f90a40b5b757b660dc"
                and candidate["receipt_json_sha256"] == "685a6bb69fcef19fb037b44242a414c674a6d4710a7cc1744e1555ceeca67db4"
                and candidate["verified_internal_file_hashes"] == 13
                and all(len(candidate[k]) == 64 for k in (
                    "prewarm_log_sha256", "build_log_sha256", "axioms_log_sha256"
                ))
            )

        self.assertTrue(admissible(row))
        # Hostile fixtures: source drift, unapproved axiom, and failed target must fail closed.
        for key, bad_value in [
            ("workflow_head", "0" * 40),
            ("upstream_commit", "0" * 40),
            ("extra_axioms", ["sorryAx"]),
            ("axioms_exit", 124),
            ("build_exit", 124),
            ("comparator_executed", True),
            ("artifact_zip_sha256", "0" * 64),
            ("solution_git_blob", "0" * 40),
        ]:
            bad = copy.deepcopy(row)
            bad[key] = bad_value
            self.assertFalse(admissible(bad), key)

        self.assertEqual(ledger["counts"]["effective_lean_axiom_pass"], 25)
        self.assertEqual(ledger["counts"]["effective_build_timeout"], 0)
        self.assertEqual(ledger["counts"]["staged_archive_sha256_verified"], 1)
        self.assertEqual(ledger["counts"]["staged_internal_file_sha256_verified"], 13)
        self.assertEqual(ledger["current_unresolved"], [])
        self.assertEqual(ledger["counts"]["lean_axiom_pass"], 23)
        self.assertEqual(ledger["counts"]["build_timeout"], 2)
        self.assertEqual(len(ledger["unresolved"]), 2)  # historical evidence retained
        self.assertFalse(any(r["comparator_executed"] for r in ledger["rows"]))
        self.assertIn("Comparator not executed", ledger["claim_boundary"])

if __name__ == "__main__":
    unittest.main()
