"""Source-locked admission tests for family-342 native Lean semantic bridge.

Never extrapolate these four checked lemmas to intrinsic manifold
smoothness/closedness, global paper acceptance, or MATHCERT promotion.
"""
import json
from pathlib import Path
import unittest

BASE = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
ARTIFACT = BASE / "FAMILY342_SEMANTIC_BRIDGE_ADJUDICATION.json"
HEAD = "f1bea85706b51e759212f4fc6f12f215130ff325"
SOURCE = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
THEOREMS = {
    "OAI.TamingCompatibility.gcl_tames_implies_isNondegenerate",
    "OAI.TamingCompatibility.gcl_symplectic_and_tames_iff_smooth_closed_tames",
    "OAI.TamingCompatibility.gcl_invariant_iff_metric_symmetric_abstract",
    "OAI.TamingCompatibility.gcl_extDeriv_zero_pullback_in_coordinates",
}

class Family342SemanticBridgeEvidence(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(ARTIFACT.read_text(encoding="utf-8"))

    def test_exact_head_source_job_and_proofs(self):
        d = self.d
        self.assertEqual(d["record_type"], "GCL_OPENAI_MATH_F342_SEMANTIC_BRIDGE_ADJUDICATION/1")
        self.assertEqual(d["decision"], "BOUNDED_NATIVE_LEAN_SEMANTIC_BRIDGE_ACCEPTED")
        self.assertEqual(d["protected_head"], HEAD)
        self.assertEqual(d["source_lock"]["commit"], SOURCE)
        self.assertEqual(d["source_lock"]["lean_toolchain"], "leanprover/lean4:v4.34.1")
        self.assertEqual(d["source_lock"]["mathlib_lock"], "d13f23b723b8a846827a245b89c10fc7d3f11612")
        r = d["replay"]
        self.assertEqual(r["run_id"], 40089468868)
        self.assertEqual(r["job_id"], 120859016798)
        self.assertEqual(r["head_sha"], HEAD)
        self.assertEqual(r["job_conclusion"], "success")
        self.assertEqual(r["exit_code"], 0)
        self.assertEqual(set(r["exact_declarations"]), THEOREMS)
        self.assertEqual(set(r["axiom_set_for_each"]),
                         {"propext", "Classical.choice", "Quot.sound"})
        self.assertIs(r["sorryAx_present"], False)
        self.assertIs(r["lean_error_present"], False)
        a = r["evidence_artifact"]
        self.assertEqual(a["artifact_id"], 12558333463)
        self.assertEqual(a["archive_sha256"],
            "3ade86f1289ea222d6bfb02ce13e589492d14f4d19d4f1c6fc7197ba3ffb62d3")
        self.assertTrue(a["all_receipt_file_hashes_verified"])
        self.assertTrue(a["manifest_unchanged"])
        self.assertEqual(a["source_bridge_sha256"],
            "84844916d59bac1aa525aed6606b571e5967ad3e769ae16342fc48042b63eb9f")

    def test_no_semantic_or_certificate_promotion(self):
        d = self.d["proof_disposition"]
        self.assertEqual(d["taming_non_degeneracy"], "CLOSED_LEAN_PASS")
        self.assertEqual(d["taming_symplectic_redundancy"], "CLOSED_LEAN_PASS")
        self.assertEqual(d["euclidean_ext_derivative_pullback_naturality"],
                         "CLOSED_LEAN_PASS_ONE_DIRECTION")
        for name in ("sem342_01_manifold_smoothness_equivalence",
                     "sem342_03_native_metric_correspondence",
                     "sem342_04_manifold_model_equivalence",
                     "literature_priority"):
            self.assertTrue(d[name].startswith("OPEN"))
        self.assertTrue(d["sem342_02_manifold_exterior_closedness_equivalence"].startswith("OPEN"))
        self.assertEqual(d["paper_formalization_semantics"], "NOT_YET_ADMITTED")
        self.assertEqual(d["MATHCERT_certification"], "NOT_GRANTED")
        self.assertEqual(d["source_provider_assurance"], "SOURCE_LOCKED")
        self.assertEqual(d["corrected_October_cone_theorem"],
                         "NOT_COVERED_BY_COMPARATOR")

if __name__ == "__main__":
    unittest.main()
