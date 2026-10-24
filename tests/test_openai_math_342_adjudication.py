"""Fail-closed source-only family-342 Comparator result admission.

The evidence here is a replay attestation to an exact Lean target. It does not
establish paper equivalence, external mathematical truth or MATHCERT authority.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sources" / "OPENAI-MATH-2026"
EXPECTED_HEAD = "470398de928083cf7f890edc99d459aa43b1c38d"
EXPECTED_SOURCE = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
TARGET = "OAI.TamingCompatibility.taming_implies_compatibility"

class Family342ComparatorAdjudicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads((BASE/"FAMILY342_COMPARATOR_ADJUDICATION.json").read_text(encoding="utf-8"))

    def test_exact_replay_identity_and_hardened_exit(self):
        d = self.record
        self.assertEqual(d["record_type"], "GCL_OPENAI_MATH_FAMILY342_COMPARATOR_ADJUDICATION/1")
        self.assertEqual(d["decision"], "HARDENED_COMPARATOR_REPLAY_ACCEPTED")
        self.assertEqual(d["protected_head"], EXPECTED_HEAD)
        self.assertEqual(d["source_lock"]["commit"], EXPECTED_SOURCE)
        self.assertEqual(d["source_lock"]["lean_toolchain"], "leanprover/lean4:v4.34.1")
        self.assertEqual(d["replay"]["run_id"], 40041645086)
        self.assertEqual(d["replay"]["event_head"], EXPECTED_HEAD)
        self.assertEqual(d["replay"]["comparator"]["challenged_declaration"], TARGET)
        self.assertEqual(d["replay"]["comparator"]["hardened_exit_code"], 0)
        self.assertIsNone(d["replay"]["comparator"]["diagnostic_exit_code"])
        self.assertTrue(d["replay"]["comparator"]["hardened_accepted"])
        self.assertIn("Lean default kernel accepts the solution",
                      d["replay"]["comparator"]["observed_success_lines"])
        self.assertIn("Finished with result: success",
                      d["replay"]["comparator"]["observed_success_lines"])
        self.assertEqual(set(d["replay"]["lean"]["printed_axioms"]),
                         set(d["replay"]["lean"]["config_permitted_axioms"]))
        self.assertEqual(set(d["replay"]["lean"]["printed_axioms"]),
                         {"propext", "Quot.sound", "Classical.choice"})

    def test_source_metadata_consistency_and_nonpromotion(self):
        d=self.record
        crosswalk=json.loads((BASE/"FORMALIZATION_CROSSWALK.json").read_text(encoding="utf-8"))
        self.assertEqual(crosswalk["origin"]["commit"], EXPECTED_SOURCE)
        self.assertEqual(crosswalk["lean_replay_status"], "NOT_RUN",
                         "global 200-target crosswalk must not be bulk-promoted by one replay")
        self.assertEqual(d["conclusions"]["comparator_execution_gate"], "CLOSED_PASS")
        self.assertEqual(d["conclusions"]["lean_kernel_gate"], "CLOSED_PASS")
        for gate in ("paper_formalization_gate","correction_semantics_gate","literature_priority_gate"):
            self.assertEqual(d["conclusions"][gate], "OPEN")
        self.assertEqual(d["conclusions"]["MATHCERT_certification"], "NOT_GRANTED")
        self.assertEqual(d["conclusions"]["provider_assurance"], "SOURCE_LOCKED")
        self.assertEqual(d["semantics"]["corrected_cone_theorem"], "NOT_FORMALIZED_BY_THIS_COMPARATOR")
        for field in ("comparator_artifact","lean_artifact"):
            art = d["evidence"][field]
            self.assertEqual(len(art["archive_sha256"]),64)
            self.assertTrue(art["artifact_id"] > 0)
            self.assertTrue(art["expires_at"].startswith("2026-11-23T"))
        self.assertEqual(d["evidence"]["comparator_artifact"]["hardened_log_sha256"],
                         "fb13c3b7bff01a5549ba587295d0dfbfd1fd5dc363724a0fcdbe6c9f9c256ed2")

if __name__ == "__main__":
    unittest.main()
