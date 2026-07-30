from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
ADAPTER_PATH = ROOT / "formal_sources" / "formal_conjectures" / "intake.py"
SPEC = importlib.util.spec_from_file_location("formal_conjectures_intake", ADAPTER_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FormalConjecturesProviderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.lock = json.loads(
            (ROOT / "formal_sources" / "formal_conjectures" / "source_lock.json").read_text(encoding="utf-8")
        )
        self.extracted = json.loads(
            (ROOT / "tests" / "fixtures" / "formal_conjectures_extract.json").read_text(encoding="utf-8")
        )
        self.blobs = MODULE.artifact_blob_map(self.lock)

    def validate(self, instance: dict, schema_name: str) -> list[str]:
        schema = json.loads((ROOT / "schemas" / schema_name).read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [error.message for error in validator.iter_errors(instance)]

    def test_source_lock_matches_schema(self) -> None:
        self.assertEqual(self.validate(self.lock, "external_formal_source.schema.json"), [])

    def test_snapshot_is_deterministic_and_valid(self) -> None:
        snapshot = MODULE.build_snapshot(
            self.lock, self.extracted, self.blobs, "2026-07-30T11:08:00Z"
        )
        reversed_input = {"problems": list(reversed(self.extracted["problems"]))}
        reversed_snapshot = MODULE.build_snapshot(
            self.lock, reversed_input, self.blobs, "2026-07-30T11:08:00Z"
        )
        self.assertEqual(snapshot["snapshot_sha256"], reversed_snapshot["snapshot_sha256"])
        self.assertEqual(self.validate(snapshot, "formal_statement_snapshot.schema.json"), [])
        MODULE.verify_snapshot(self.lock, snapshot)

    def test_missing_locked_blob_fails_closed(self) -> None:
        broken = json.loads(json.dumps(self.extracted))
        broken["problems"][0]["module"] = "FormalConjectures.Millenium.Unlocked"
        with self.assertRaises(MODULE.IntakeError):
            MODULE.build_snapshot(self.lock, broken, self.blobs, "2026-07-30T11:08:00Z")

    def test_digest_tampering_is_rejected(self) -> None:
        snapshot = MODULE.build_snapshot(
            self.lock, self.extracted, self.blobs, "2026-07-30T11:08:00Z"
        )
        snapshot["statements"][0]["category"] = "research solved"
        with self.assertRaises(MODULE.IntakeError):
            MODULE.verify_snapshot(self.lock, snapshot)

    def test_committed_snapshot_and_concordances_validate(self) -> None:
        snapshot_path = (
            ROOT / "formal_sources" / "formal_conjectures" / "snapshots" / "FC-GDM-001-RH-NS-PILOT.json"
        )
        snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
        self.assertEqual(self.validate(snapshot, "formal_statement_snapshot.schema.json"), [])
        MODULE.verify_snapshot(self.lock, snapshot)
        for name in ("RH-001.json", "NS-CI-001.json"):
            concordance = json.loads(
                (ROOT / "formal_sources" / "formal_conjectures" / "concordance" / name).read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual(self.validate(concordance, "statement_concordance.schema.json"), [])

    def test_external_formal_source_registry_is_closed(self) -> None:
        registry = json.loads(
            (ROOT / "governance" / "external_formal_sources.json").read_text(encoding="utf-8")
        )
        self.assertEqual(
            self.validate(registry, "external_formal_source_registry.schema.json"), []
        )
        source_ids = [entry["source_id"] for entry in registry["sources"]]
        self.assertEqual(len(source_ids), len(set(source_ids)))

        registered_locks = {entry["source_lock_path"] for entry in registry["sources"]}
        discovered_locks = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "formal_sources").glob("*/source_lock.json")
        }
        self.assertEqual(registered_locks, discovered_locks)

        registered_snapshots = {
            path for entry in registry["sources"] for path in entry["snapshot_paths"]
        }
        discovered_snapshots = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "formal_sources").glob("*/snapshots/*.json")
        }
        self.assertEqual(registered_snapshots, discovered_snapshots)

        registered_concordances = {
            path for entry in registry["sources"] for path in entry["concordance_paths"]
        }
        discovered_concordances = {
            path.relative_to(ROOT).as_posix()
            for path in (ROOT / "formal_sources").glob("*/concordance/*.json")
        }
        self.assertEqual(registered_concordances, discovered_concordances)

        for entry in registry["sources"]:
            self.assertTrue((ROOT / entry["source_lock_path"]).is_file())
            self.assertTrue((ROOT / entry["adapter_path"]).is_file())
            lock = json.loads((ROOT / entry["source_lock_path"]).read_text(encoding="utf-8"))
            self.assertEqual(lock["source_id"], entry["source_id"])
            for relative in entry["snapshot_paths"] + entry["concordance_paths"]:
                self.assertTrue((ROOT / relative).is_file())


if __name__ == "__main__":
    unittest.main()
