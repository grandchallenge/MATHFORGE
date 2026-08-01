from __future__ import annotations

import importlib.util
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TRIAGE_PATH = ROOT / "reports" / "discovery" / "ns_ci_001" / "claimed_proof_triage_2026.json"
LOCK_PATH = ROOT / "reports" / "discovery" / "ns_ci_001" / "source_byte_lock_2026.json"
VERIFIER_PATH = ROOT / "tools" / "verify_ns_ci_r014_source_lock.py"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def load_verifier():
    spec = importlib.util.spec_from_file_location("ns_ci_r014_source_lock", VERIFIER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load source-lock verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class NSCIR014SourceLockTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.triage = json.loads(TRIAGE_PATH.read_text(encoding="utf-8"))
        cls.lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
        cls.verifier = load_verifier()

    def test_exact_versioned_source_family_is_pinned(self) -> None:
        versioned_ids = {
            f"{item['arxiv_id']}v{item['version']}" for item in self.lock["sources"]
        }
        self.assertEqual(
            versioned_ids,
            {
                "2605.01875v3",
                "2605.01873v2",
                "2605.09797v2",
                "2606.07869v1",
            },
        )
        verifier_ids = {item["versioned_id"] for item in self.verifier.SOURCE_SPECS}
        self.assertEqual(verifier_ids, versioned_ids)

    def test_initial_triage_state_is_preserved_as_history(self) -> None:
        for source in self.triage["sources"]:
            self.assertIsNone(source["pdf_sha256"])
            self.assertIsNone(source["tex_sha256"])
        self.assertFalse(self.triage["disposition"]["source_bytes_locked"])
        self.assertEqual(
            self.lock["supersedes_source_identity_state_in"],
            "reports/discovery/ns_ci_001/claimed_proof_triage_2026.json",
        )

    def test_committed_source_lock_has_exact_integrity_fields(self) -> None:
        self.assertTrue(self.lock["disposition"]["source_bytes_locked"])
        self.assertEqual(len(self.lock["sources"]), 4)
        for source in self.lock["sources"]:
            with self.subTest(source_id=source["source_id"]):
                self.assertRegex(source["pdf_sha256"], SHA256_RE)
                self.assertRegex(source["tex_sha256"], SHA256_RE)
                self.assertGreater(source["pdf_bytes"], 0)
                self.assertGreater(source["tex_bytes"], 0)
                self.assertTrue(source["pdf_header_valid"])
                self.assertTrue(source["pdf_eof_marker_present"])
                self.assertEqual(source["tex_container"], "gzip")
                self.assertEqual(
                    source["page_count_basis"], "arxiv_metadata_not_pdfinfo_replay"
                )

    def test_acquisition_artifact_is_content_addressed(self) -> None:
        acquisition = self.lock["acquisition"]
        self.assertEqual(acquisition["workflow_run_id"], 30706549352)
        self.assertEqual(acquisition["artifact_id"], 8820499597)
        self.assertRegex(
            acquisition["artifact_digest"], re.compile(r"^sha256:[0-9a-f]{64}$")
        )
        self.assertFalse(acquisition["copyrighted_source_bytes_retained_in_repository"])

    def test_analytic_and_downstream_gates_remain_closed(self) -> None:
        disposition = self.lock["disposition"]
        self.assertEqual(disposition["axisymmetric_claim"], "UNRESOLVED")
        self.assertEqual(disposition["full_system_claim"], "UNRESOLVED")
        self.assertEqual(disposition["proof_obligation_clear_count"], 0)
        self.assertFalse(disposition["may_change_programme_theorem_status"])
        self.assertFalse(disposition["may_route_to_mathsolve"])
        self.assertFalse(disposition["may_route_to_mathcert"])
        self.assertFalse(disposition["may_promote_global_regularity_claim"])

    def test_all_proof_obligations_remain_blocking(self) -> None:
        obligations = self.triage["proof_obligations"]
        self.assertEqual(len(obligations), 12)
        self.assertTrue(
            all(item["status"] == "unreviewed_blocking" for item in obligations)
        )


if __name__ == "__main__":
    unittest.main()
