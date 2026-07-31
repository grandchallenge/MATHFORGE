from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import unittest
import zipfile
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
ADAPTER_PATH = ROOT / "formal_sources" / "formal_conjectures" / "intake.py"
SPEC = importlib.util.spec_from_file_location("formal_conjectures_intake_expansion", ADAPTER_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FormalConjecturesExpansionTests(unittest.TestCase):
    ARCHIVE_SHA256 = "1c74747519c17f873f323198a92104538667092f3274a667a09e1a6b219a7bcb"

    def setUp(self) -> None:
        self.root = ROOT / "formal_sources" / "formal_conjectures"
        self.replay_dir = self.root / "replays" / "FC-GDM-002"
        self.bundle = self.replay_dir / "formal-conjectures-expanded-replay.zip"
        self.lock = json.loads((self.root / "source_locks" / "FC-GDM-002.json").read_text(encoding="utf-8"))
        self.snapshot_path = self.root / "snapshots" / "FC-GDM-002-ACTIVE-CAMPAIGN-EXPANSION.json"
        self.snapshot = json.loads(self.snapshot_path.read_text(encoding="utf-8"))

    def validate(self, instance: dict, schema_name: str) -> list[str]:
        schema = json.loads((ROOT / "schemas" / schema_name).read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [error.message for error in validator.iter_errors(instance)]

    def test_lock_and_snapshot_are_replay_derived_and_valid(self) -> None:
        self.assertEqual(self.validate(self.lock, "external_formal_source.schema.json"), [])
        self.assertEqual(self.validate(self.snapshot, "formal_statement_snapshot.schema.json"), [])
        MODULE.verify_snapshot(self.lock, self.snapshot)
        self.assertEqual(len(self.snapshot["statements"]), 43)
        self.assertEqual(
            self.snapshot["snapshot_sha256"],
            "2b6bda841d15b022ec8c66bc332177d1283ca791f5d5f6e82323c304d1e6fdf6",
        )

    def test_exact_replay_bundle_closes_over_manifest_and_committed_bytes(self) -> None:
        archive_bytes = self.bundle.read_bytes()
        self.assertEqual(hashlib.sha256(archive_bytes).hexdigest(), self.ARCHIVE_SHA256)
        committed_manifest = (self.replay_dir / "REPLAY_MANIFEST.json").read_bytes()
        with zipfile.ZipFile(self.bundle) as archive:
            self.assertEqual(archive.read("REPLAY_MANIFEST.json"), committed_manifest)
            manifest = json.loads(committed_manifest)
            self.assertEqual(self.validate(manifest, "formal_source_replay_manifest.schema.json"), [])
            for record in manifest["records"]:
                member = Path(record["path"]).name
                data = archive.read(member)
                self.assertEqual(len(data), record["byte_length"], member)
                self.assertEqual(hashlib.sha256(data).hexdigest(), record["sha256"], member)

                if member == self.snapshot_path.name:
                    committed = self.snapshot_path.read_bytes()
                elif member in {
                    "FC-GDM-002-INVENTORY-SCREEN.json",
                    "FC-GDM-002-TAG-RESOLUTION.json",
                }:
                    committed = (self.replay_dir / member).read_bytes()
                else:
                    continue
                self.assertEqual(committed, data, member)

    def test_tag_resolution_requires_commit_only_lock(self) -> None:
        record = json.loads((self.replay_dir / "FC-GDM-002-TAG-RESOLUTION.json").read_text(encoding="utf-8"))
        self.assertEqual(record["resolution"], "commit_only_required")
        self.assertIsNone(record["selected_tag"])
        self.assertEqual(record["pinned_commit"], self.lock["revision"]["commit"])
        self.assertEqual(record["containing_benchmark_tags"], [])

    def test_inventory_screen_rejects_lexical_false_positive(self) -> None:
        screen = json.loads((self.replay_dir / "FC-GDM-002-INVENTORY-SCREEN.json").read_text(encoding="utf-8"))
        searches = {entry["campaign_id"]: entry for entry in screen["searches"]}
        self.assertEqual(searches["HC-001"]["hits"], [])
        self.assertTrue(searches["YM-001"]["hits"])
        self.assertTrue(all("mills" in hit["matched_terms"] for hit in searches["YM-001"]["hits"]))
        ym = json.loads((self.root / "coverage" / "YM-001.json").read_text(encoding="utf-8"))
        self.assertEqual(ym["disposition"], "lexical-false-positive")

    def test_concordance_and_coverage_artifacts_validate(self) -> None:
        for path in sorted((self.root / "concordance").glob("*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(self.validate(record, "statement_concordance.schema.json"), [], path.name)
        for path in sorted((self.root / "coverage").glob("*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(self.validate(record, "formal_source_coverage_record.schema.json"), [], path.name)
            evidence = record["inventory_evidence"]
            self.assertEqual(evidence["replay_bundle_sha256"], self.ARCHIVE_SHA256)
            self.assertEqual(evidence["inventory_member"], "FC-GDM-002-FULL-INVENTORY.json")
        ledger = json.loads((self.root / "update_ledgers" / "FC-GDM-001-TO-FC-GDM-002.json").read_text(encoding="utf-8"))
        self.assertEqual(self.validate(ledger, "formal_source_update_ledger.schema.json"), [])
        self.assertEqual(ledger["theorem_delta"]["removed"], [])
        self.assertEqual(ledger["theorem_delta"]["renamed"], [])

    def test_adversarial_drift_contracts(self) -> None:
        tampered = json.loads(json.dumps(self.snapshot))
        tampered["statements"][0]["category"] = "research solved"
        with self.assertRaises(MODULE.IntakeError):
            MODULE.verify_snapshot(self.lock, tampered)

        theorem_ids = {item["statement_id"] for item in self.snapshot["statements"]}
        required = {
            "FC:UnionClosed.union_closed",
            "FC:ComplexityTheory.P_ne_NP",
            "FC:RiemannZetaValues.irrational_five",
            "FC:RiemannZetaValues.exists_irrational_of_five_seven_nine_eleven",
        }
        self.assertTrue(required.issubset(theorem_ids))

    def test_oz_quantifier_scopes_remain_separate(self) -> None:
        expected = {
            "OZ-001-ZETA5.json": "RiemannZetaValues.irrational_five",
            "OZ-001-ZETA7.json": "RiemannZetaValues.irrational_seven",
            "OZ-001-ZETA9.json": "RiemannZetaValues.irrational_nine",
            "OZ-001-ZETA11.json": "RiemannZetaValues.irrational_eleven",
            "OZ-001-ODD-UNIVERSAL.json": "RiemannZetaValues.irrational_odd",
            "OZ-001-ODD-INFINITUDE.json": "RiemannZetaValues.infinite_irrational_at_odd",
            "OZ-001-ZUDILIN-5-11.json": "RiemannZetaValues.exists_irrational_of_five_seven_nine_eleven",
        }
        observed = {}
        for name, theorem in expected.items():
            record = json.loads((self.root / "concordance" / name).read_text(encoding="utf-8"))
            observed[name] = record["upstream_statement"]["theorem"]
        self.assertEqual(observed, expected)


if __name__ == "__main__":
    unittest.main()
