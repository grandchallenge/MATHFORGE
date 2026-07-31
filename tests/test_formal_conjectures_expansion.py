from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


class FormalConjecturesExpansionTests(unittest.TestCase):
    ARCHIVE_SHA256 = "1c74747519c17f873f323198a92104538667092f3274a667a09e1a6b219a7bcb"
    SNAPSHOT_SHA256 = "e7534f913160cc9cef4eb80a735c44b7b1a8ea4273f0f5236d82cc7b9dab042b"
    INVENTORY_SHA256 = "2693de3b83c0990b0e7c62ab5032698c6dde6de0942441ba7d6cdb035625e687"

    def setUp(self) -> None:
        self.root = ROOT / "formal_sources" / "formal_conjectures"
        self.replay_dir = self.root / "replays" / "FC-GDM-002"
        self.lock = json.loads(
            (self.root / "source_locks" / "FC-GDM-002.json").read_text(encoding="utf-8")
        )
        self.snapshot_ref = json.loads(
            (
                self.root
                / "snapshots"
                / "FC-GDM-002-ACTIVE-CAMPAIGN-EXPANSION.replay.json"
            ).read_text(encoding="utf-8")
        )
        self.manifest = json.loads(
            (self.replay_dir / "REPLAY_MANIFEST.json").read_text(encoding="utf-8")
        )

    def validate(self, instance: dict, schema_name: str) -> list[str]:
        schema = json.loads((ROOT / "schemas" / schema_name).read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        return [error.message for error in validator.iter_errors(instance)]

    def manifest_record(self, member_name: str) -> dict:
        matches = [
            record
            for record in self.manifest["records"]
            if Path(record["path"]).name == member_name
        ]
        self.assertEqual(len(matches), 1, member_name)
        return matches[0]

    def reference_matches_manifest(self, reference: dict) -> bool:
        member = reference["snapshot_member"]
        record = self.manifest_record(member["name"])
        return (
            member["byte_length"] == record["byte_length"]
            and member["sha256"] == record["sha256"]
            and reference["statement_count"] == record["statement_count"]
        )

    @staticmethod
    def unresolved_pnp_is_fail_closed(record: dict) -> bool:
        return (
            record.get("relation") == "unresolved"
            and any(item.get("severity") == "blocking" for item in record.get("findings", []))
            and len(record.get("obligations", [])) >= 1
        )

    def test_lock_reference_and_manifest_are_valid(self) -> None:
        self.assertEqual(self.validate(self.lock, "external_formal_source.schema.json"), [])
        self.assertEqual(
            self.validate(self.snapshot_ref, "formal_statement_replay_reference.schema.json"),
            [],
        )
        self.assertEqual(
            self.validate(self.manifest, "formal_source_replay_manifest.schema.json"),
            [],
        )
        self.assertEqual(
            self.snapshot_ref["source_commit"], self.lock["revision"]["commit"]
        )
        self.assertTrue(self.reference_matches_manifest(self.snapshot_ref))
        self.assertEqual(self.snapshot_ref["statement_count"], 43)
        self.assertEqual(
            self.snapshot_ref["canonical_snapshot_sha256"],
            "2b6bda841d15b022ec8c66bc332177d1283ca791f5d5f6e82323c304d1e6fdf6",
        )

    def test_exact_actions_artifact_identity_is_pinned(self) -> None:
        bundle = self.snapshot_ref["replay_bundle"]
        self.assertEqual(bundle["repository"], "grandchallenge/MATHFORGE")
        self.assertEqual(bundle["workflow_run_id"], 30544600547)
        self.assertEqual(bundle["artifact_id"], 8761186970)
        self.assertEqual(bundle["artifact_name"], "formal-conjectures-expanded-replay")
        self.assertEqual(bundle["archive_sha256"], self.ARCHIVE_SHA256)

        snapshot_record = self.manifest_record(
            self.snapshot_ref["snapshot_member"]["name"]
        )
        inventory_record = self.manifest_record("FC-GDM-002-FULL-INVENTORY.json")
        self.assertEqual(snapshot_record["sha256"], self.SNAPSHOT_SHA256)
        self.assertEqual(snapshot_record["byte_length"], 52589)
        self.assertEqual(snapshot_record["statement_count"], 43)
        self.assertEqual(inventory_record["sha256"], self.INVENTORY_SHA256)
        self.assertEqual(inventory_record["byte_length"], 1255363)
        self.assertEqual(inventory_record["problem_count"], 3232)

    def test_committed_replay_derivatives_match_manifest(self) -> None:
        for member in (
            "FC-GDM-002-INVENTORY-SCREEN.json",
            "FC-GDM-002-TAG-RESOLUTION.json",
        ):
            data = (self.replay_dir / member).read_bytes()
            record = self.manifest_record(member)
            self.assertEqual(len(data), record["byte_length"], member)
            self.assertEqual(hashlib.sha256(data).hexdigest(), record["sha256"], member)

    def test_tag_resolution_requires_commit_only_lock(self) -> None:
        record = json.loads(
            (self.replay_dir / "FC-GDM-002-TAG-RESOLUTION.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(record["resolution"], "commit_only_required")
        self.assertIsNone(record["selected_tag"])
        self.assertEqual(record["pinned_commit"], self.lock["revision"]["commit"])
        self.assertEqual(record["containing_benchmark_tags"], [])

    def test_inventory_screen_rejects_lexical_false_positive(self) -> None:
        screen = json.loads(
            (self.replay_dir / "FC-GDM-002-INVENTORY-SCREEN.json").read_text(
                encoding="utf-8"
            )
        )
        searches = {entry["campaign_id"]: entry for entry in screen["searches"]}
        self.assertEqual(searches["HC-001"]["hits"], [])
        self.assertTrue(searches["YM-001"]["hits"])
        self.assertTrue(
            all("mills" in hit["matched_terms"] for hit in searches["YM-001"]["hits"])
        )
        ym = json.loads(
            (self.root / "coverage" / "YM-001.json").read_text(encoding="utf-8")
        )
        self.assertEqual(ym["disposition"], "lexical-false-positive")

    def test_concordance_and_coverage_artifacts_validate(self) -> None:
        for path in sorted((self.root / "concordance").glob("*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(
                self.validate(record, "statement_concordance.schema.json"), [], path.name
            )
        for path in sorted((self.root / "coverage").glob("*.json")):
            record = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(
                self.validate(record, "formal_source_coverage_record.schema.json"),
                [],
                path.name,
            )
            evidence = record["inventory_evidence"]
            self.assertEqual(evidence["replay_bundle_sha256"], self.ARCHIVE_SHA256)
            self.assertEqual(
                evidence["inventory_member"], "FC-GDM-002-FULL-INVENTORY.json"
            )
        ledger = json.loads(
            (
                self.root
                / "update_ledgers"
                / "FC-GDM-001-TO-FC-GDM-002.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(
            self.validate(ledger, "formal_source_update_ledger.schema.json"), []
        )
        self.assertEqual(ledger["theorem_delta"]["removed"], [])
        self.assertEqual(ledger["theorem_delta"]["renamed"], [])
        self.assertEqual(ledger["theorem_delta"]["category_changes"], [])

    def test_adversarial_drift_contracts(self) -> None:
        tampered_reference = json.loads(json.dumps(self.snapshot_ref))
        tampered_reference["snapshot_member"]["sha256"] = "0" * 64
        self.assertFalse(self.reference_matches_manifest(tampered_reference))

        pnp = json.loads(
            (self.root / "concordance" / "PNP-001.json").read_text(encoding="utf-8")
        )
        self.assertTrue(self.unresolved_pnp_is_fail_closed(pnp))
        incomplete_pnp = json.loads(json.dumps(pnp))
        incomplete_pnp["findings"] = [
            item for item in incomplete_pnp["findings"] if item["severity"] != "blocking"
        ]
        self.assertFalse(self.unresolved_pnp_is_fail_closed(incomplete_pnp))

        locked_blobs = {
            item["path"]: item["git_blob_sha1"]
            for item in self.lock["revision"]["artifact_blobs"]
        }
        self.assertEqual(
            locked_blobs[pnp["upstream_statement"]["path"]],
            pnp["upstream_statement"]["git_blob_sha1"],
        )
        drifted_pnp = json.loads(json.dumps(pnp))
        drifted_pnp["upstream_statement"]["git_blob_sha1"] = "0" * 40
        self.assertNotEqual(
            locked_blobs[drifted_pnp["upstream_statement"]["path"]],
            drifted_pnp["upstream_statement"]["git_blob_sha1"],
        )

        theorem_names = {
            json.loads(path.read_text(encoding="utf-8"))["upstream_statement"]["theorem"]
            for path in (self.root / "concordance").glob("*.json")
        }
        required = {
            "UnionClosed.union_closed",
            "ComplexityTheory.P_ne_NP",
            "RiemannZetaValues.irrational_five",
            "RiemannZetaValues.exists_irrational_of_five_seven_nine_eleven",
        }
        self.assertTrue(required.issubset(theorem_names))

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
            record = json.loads(
                (self.root / "concordance" / name).read_text(encoding="utf-8")
            )
            observed[name] = record["upstream_statement"]["theorem"]
        self.assertEqual(observed, expected)


if __name__ == "__main__":
    unittest.main()
