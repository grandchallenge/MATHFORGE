from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_source_revision_audit",
    ROOT / "ci/validate_openai_ten_proofs_source_revision_audit.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OpenAITenProofsSourceRevisionAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.audit = json.loads(MODULE.AUDIT_PATH.read_text(encoding="utf-8"))
        self.semantic_records = {
            family: json.loads((ROOT / expected["path"]).read_text(encoding="utf-8"))
            for family, expected in MODULE.EXPECTED_FAMILIES.items()
        }
        self.semantic_blobs = {
            family: MODULE.git_blob_sha1(ROOT / expected["path"])
            for family, expected in MODULE.EXPECTED_FAMILIES.items()
        }
        self.provider_manifest_text = MODULE.MANIFEST_PATH.read_text(encoding="utf-8")

    def errors(self, *, audit=None, semantic_records=None, semantic_blobs=None, provider_manifest_text=None):
        return MODULE.validation_errors(
            audit=copy.deepcopy(self.audit if audit is None else audit),
            semantic_records=copy.deepcopy(
                self.semantic_records if semantic_records is None else semantic_records
            ),
            semantic_blobs=copy.deepcopy(
                self.semantic_blobs if semantic_blobs is None else semantic_blobs
            ),
            provider_manifest_text=(
                self.provider_manifest_text
                if provider_manifest_text is None
                else provider_manifest_text
            ),
        )

    def test_current_audit_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_silent_repin_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["admitted_manuscript"]["sha256"] = MODULE.OBSERVED_SHA
        self.assertTrue(self.errors(audit=audit))

    def test_false_whole_document_equivalence_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["disposition"]["whole_document_semantic_equivalence"] = "established"
        self.assertTrue(self.errors(audit=audit))

    def test_false_byte_diff_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["comparison_method"]["exact_whole_document_byte_diff_performed"] = True
        self.assertTrue(self.errors(audit=audit))

    def test_missing_family_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["families"].pop()
        self.assertTrue(self.errors(audit=audit))

    def test_normalized_statement_substitution_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["families"][0]["admitted_normalized_statement"] = "weaker substitute"
        self.assertTrue(self.errors(audit=audit))

    def test_semantic_record_blob_drift_is_rejected(self) -> None:
        blobs = copy.deepcopy(self.semantic_blobs)
        blobs["OTP-J1-COMPACTNESS"] = "0" * 40
        self.assertTrue(self.errors(semantic_blobs=blobs))

    def test_full_proof_body_claim_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["families"][2]["current_revision_findings"]["proof_body_compared_in_full"] = True
        self.assertTrue(self.errors(audit=audit))

    def test_premature_activation_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["families"][1]["current_revision_locus_concordance"] = "clear"
        self.assertTrue(self.errors(audit=audit))

    def test_route_enable_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["route_controls"]["may_route_before_activation"] = True
        self.assertTrue(self.errors(audit=audit))

    def test_clear_count_inflation_is_rejected(self) -> None:
        audit = copy.deepcopy(self.audit)
        audit["disposition"]["family_locus_clear_count_before_activation"] = 3
        self.assertTrue(self.errors(audit=audit))

    def test_premature_provider_manifest_repin_is_rejected(self) -> None:
        text = self.provider_manifest_text + MODULE.OBSERVED_SHA
        self.assertTrue(self.errors(provider_manifest_text=text))


if __name__ == "__main__":
    unittest.main()
