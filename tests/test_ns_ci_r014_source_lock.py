from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RECORD_PATH = ROOT / "reports" / "discovery" / "ns_ci_001" / "claimed_proof_triage_2026.json"
VERIFIER_PATH = ROOT / "tools" / "verify_ns_ci_r014_source_lock.py"


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
        cls.record = json.loads(RECORD_PATH.read_text(encoding="utf-8"))
        cls.verifier = load_verifier()

    def test_exact_versioned_source_family_is_pinned(self) -> None:
        versioned_ids = {
            f"{item['arxiv_id']}v{item['version']}" for item in self.record["sources"]
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

    def test_source_lock_remains_fail_closed_until_digests_are_committed(self) -> None:
        for source in self.record["sources"]:
            self.assertIsNone(source["pdf_sha256"])
            self.assertIsNone(source["tex_sha256"])
        self.assertFalse(self.record["disposition"]["source_bytes_locked"])

    def test_analytic_and_downstream_gates_remain_closed(self) -> None:
        disposition = self.record["disposition"]
        self.assertEqual(disposition["axisymmetric_claim"], "UNRESOLVED")
        self.assertEqual(disposition["full_system_claim"], "UNRESOLVED")
        self.assertEqual(disposition["proof_obligation_clear_count"], 0)
        self.assertFalse(disposition["may_change_programme_theorem_status"])
        self.assertFalse(disposition["may_route_to_mathcert"])
        self.assertFalse(disposition["may_promote_global_regularity_claim"])

    def test_all_proof_obligations_remain_blocking(self) -> None:
        obligations = self.record["proof_obligations"]
        self.assertEqual(len(obligations), 12)
        self.assertTrue(
            all(item["status"] == "unreviewed_blocking" for item in obligations)
        )


if __name__ == "__main__":
    unittest.main()
