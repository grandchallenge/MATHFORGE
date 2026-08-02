from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_provider_manifest",
    ROOT / "ci/validate_openai_ten_proofs_provider_manifest.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OpenAITenProofsProviderManifestTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads(MODULE.MANIFEST_PATH.read_text(encoding="utf-8"))
        self.audit = json.loads(MODULE.AUDIT_PATH.read_text(encoding="utf-8"))
        self.audit_blob = MODULE.git_blob_sha1(MODULE.AUDIT_PATH)
        self.semantic_blobs = {
            artifact_id: MODULE.git_blob_sha1(ROOT / path)
            for artifact_id, (path, _) in MODULE.EXPECTED_SEMANTIC_ARTIFACTS.items()
        }

    def errors(self, *, manifest=None, audit=None, audit_blob=None, semantic_blobs=None):
        return MODULE.validation_errors(
            manifest=copy.deepcopy(self.manifest if manifest is None else manifest),
            audit=copy.deepcopy(self.audit if audit is None else audit),
            audit_blob=self.audit_blob if audit_blob is None else audit_blob,
            semantic_blobs=copy.deepcopy(
                self.semantic_blobs if semantic_blobs is None else semantic_blobs
            ),
        )

    def record(self, manifest, field, record_id):
        return next(item for item in manifest[field] if item.get("record_id") == record_id)

    def test_current_manifest_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_silent_admitted_digest_replacement_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        record = self.record(
            manifest,
            "source_records",
            "OPENAI-TEN-PROOFS-001-ADMITTED-MANUSCRIPT-REVISION",
        )
        record["summary"] = record["summary"].replace(MODULE.ADMITTED_SHA, MODULE.OBSERVED_SHA)
        self.assertTrue(self.errors(manifest=manifest))

    def test_observed_revision_removal_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["source_records"] = [
            item
            for item in manifest["source_records"]
            if item.get("record_id")
            != "OPENAI-TEN-PROOFS-001-OBSERVED-MANUSCRIPT-REVISION"
        ]
        self.assertTrue(self.errors(manifest=manifest))

    def test_family_count_inflation_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        extra = copy.deepcopy(audit["families"][0])
        extra["result_family"] = "OTP-A-SPHERE-PACKING"
        audit["families"].append(extra)
        audit["disposition"]["family_locus_clear_count_after_activation"] = 4
        audit["disposition"]["unexamined_result_family_count"] = 8
        self.assertTrue(self.errors(audit=audit))

    def test_whole_document_equivalence_inflation_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["disposition"]["whole_document_semantic_equivalence"] = "established"
        self.assertTrue(self.errors(audit=audit))

    def test_audit_blob_drift_is_rejected(self) -> None:
        self.assertTrue(self.errors(audit_blob="0" * 40))

    def test_semantic_blob_drift_is_rejected(self) -> None:
        blobs = copy.deepcopy(self.semantic_blobs)
        blobs["OPENAI-TEN-PROOFS-001-SEMANTIC-COMPACTNESS"] = "0" * 40
        self.assertTrue(self.errors(semantic_blobs=blobs))

    def test_route_registration_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["failed_routes"].append(
            {
                "record_id": "MC-ROUTE-OTP-F-EHRHART",
                "summary": "route registered",
                "references": [],
            }
        )
        self.assertTrue(self.errors(manifest=manifest))

    def test_adjudication_promotion_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["may_adjudicate"] = True
        self.assertTrue(self.errors(manifest=manifest))

    def test_permanent_blocker_removal_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        blocked = self.record(
            manifest,
            "status_records",
            "OPENAI-TEN-PROOFS-001-BLOCKED-FAMILIES",
        )
        blocked["summary"] = blocked["summary"].replace(
            "OTP-C-PERMANENT remains blocked", "OTP-C-PERMANENT is clear"
        )
        self.assertTrue(self.errors(manifest=manifest))

    def test_gapcvp_disposition_removal_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["failed_routes"] = [
            item
            for item in manifest["failed_routes"]
            if item.get("record_id")
            != "OPENAI-TEN-PROOFS-001-GAPCVP-ROUTE-BLOCKED"
        ]
        self.assertTrue(self.errors(manifest=manifest))

    def test_all_import_disposition_removal_is_rejected(self) -> None:
        manifest = copy.deepcopy(self.manifest)
        manifest["failed_routes"] = [
            item
            for item in manifest["failed_routes"]
            if item.get("record_id")
            != "OPENAI-TEN-PROOFS-001-ALL-IMPORT-FAILED"
        ]
        self.assertTrue(self.errors(manifest=manifest))


if __name__ == "__main__":
    unittest.main()
