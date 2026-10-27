"""Fail-closed exact-head admission of family-342 native tangent metric semantics.

The nine admitted Lean declarations are not a proof of the chartwise atlas
equivalence, the cone theorem, scientific priority, or MATHCERT authority.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sources" / "OPENAI-MATH-2026"
TARGET = BASE / "FAMILY342_NATIVE_METRIC_ADJUDICATION.json"
HEAD = "4a40e6a6231700f6201ca86c505e571094860d52"
SOURCE = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
NATIVE = {
    "OAI.TamingCompatibility.gcl_eval_skew",
    "OAI.TamingCompatibility.gcl_eval_neg_left",
    "OAI.TamingCompatibility.gcl_eval_neg_right",
    "OAI.TamingCompatibility.gcl_native_invariant_iff_metric_symmetric",
    "OAI.TamingCompatibility.gcl_native_compatible_iff_symmetric_positive",
}

class NativeMetricBridgeEvidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(TARGET.read_text(encoding="utf-8"))

    def test_pinned_exact_main_evidence(self):
        d = self.d
        self.assertEqual(d["record_type"], "GCL_OPENAI_MATH_F342_NATIVE_METRIC_ADJUDICATION/1")
        self.assertEqual(d["decision"], "EXACT_MAIN_NATIVE_METRIC_KERNEL_PASS")
        self.assertEqual(d["protected_head"], HEAD)
        self.assertEqual(d["source_lock"]["commit"], SOURCE)
        self.assertEqual(d["source_lock"]["toolchain"], "leanprover/lean4:v4.34.1")
        self.assertEqual(d["source_lock"]["mathlib_commit"], "d13f23b723b8a846827a245b89c10fc7d3f11612")
        r = d["replay"]
        self.assertEqual(r["run_id"], 40094136070)
        self.assertEqual(r["head_sha"], HEAD)
        self.assertEqual(r["event"], "workflow_dispatch")
        self.assertEqual(r["job_id"], 120872796223)
        self.assertEqual(r["job_name"], "semantic-342")
        self.assertEqual(r["job_conclusion"], "success")
        self.assertEqual(r["result_exit"], 0)
        self.assertEqual(set(r["axioms_each"]), {"propext","Classical.choice","Quot.sound"})
        self.assertIs(r["sorryAx_present"], False)
        self.assertIs(r["Lean_error_present"], False)
        self.assertEqual(len(r["declarations"]), 9)
        self.assertTrue(NATIVE.issubset(set(r["declarations"])))
        a = d["evidence"]
        self.assertEqual(a["artifact_id"], 12560057130)
        self.assertEqual(a["artifact_sha256"], "096695aeb4f736bfdd5b53cbbe4574aac7dc97f1139d5a725e7f8db18b643b38")
        self.assertTrue(a["hashes_for_all_receipt_files_verified"])
        self.assertTrue(a["lake_manifest_pre_post_digests_match"])
        self.assertEqual(r["native_bridge_sha256"],
            "a70976d4f4789a183d24213602698ba76c06f65e3f744c93fcfe22a89b1b172b")

    def test_paper_semantics_not_promoted(self):
        d = self.d["adjudication"]
        for f in ("SEM342_03_alternating_metric_pointwise",
                  "SEM342_03_symmetry_iff_invariance",
                  "SEM342_03_compatible_iff_symmetric_positive"):
            self.assertEqual(d[f], "CLOSED_NATIVE_LEAN_PASS")
        for f in ("SEM342_03_metric_smoothness",
                  "SEM342_01_intrinsic_smoothness",
                  "SEM342_02_intrinsic_exterior_closedness",
                  "SEM342_04_manifold_hypotheses_equivalence"):
            self.assertTrue(d[f].startswith("OPEN"))
        self.assertEqual(d["atlas_level_S_C_paper_argument"],
                         "MATHEMATICAL_ARGUMENT_RECORDED_NOT_KERNEL_PROVED")
        self.assertEqual(d["corrected_cone_theorem"], "NOT_COVERED_BY_COMPARATOR")
        self.assertEqual(d["paper_manuscript_semantics"], "NOT_YET_ADMITTED")
        self.assertEqual(d["source_catalogue"], "SOURCE_LOCKED")
        self.assertEqual(d["MATHCERT"], "NOT_GRANTED")
        self.assertTrue((BASE/"FAMILY342_ATLAS_EQUIVALENCE_MATH_PROOF.md").exists())

if __name__ == "__main__":
    unittest.main()
