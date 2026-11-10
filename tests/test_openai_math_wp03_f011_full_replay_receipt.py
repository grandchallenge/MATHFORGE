"""Evidence-custody and hostile replay-receipt tests for the source-locked F011 proof.

These tests check documentary consistency; Lean replay must be inspected separately.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
LEAN = ROOT / "WP03_FAMILY011_FULL_ASYMPTOTIC_REDUCTION.lean"
EVIDENCE = ROOT / "WP03_FAMILY011_FULL_ASYMPTOTIC_REDUCTION_REPLAY.json"
UPSTREAM = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
MANIFEST = "cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794"
THEOREMS = (
    "GCL.OAI26.Family011.prime_supply_of_smooth_count",
    "GCL.OAI26.Family011.infinite_fibers_of_smooth_count",
)
AXIOMS = {"propext", "Classical.choice", "Quot.sound"}

def validate(receipt, source):
    if receipt["record_type"] != "GCL_OAI26_WP03_F011_FULL_ASYMPTOTIC_REDUCTION_LEAN_REPLAY/1":
        raise ValueError("receipt type mismatch")
    pin = receipt["source"]
    if pin["upstream_commit"] != UPSTREAM or pin["manifest_sha256"] != MANIFEST:
        raise ValueError("pinned source or manifest mismatch")
    if pin["lean_toolchain"] != "leanprover/lean4:v4.34.1":
        raise ValueError("Lean toolchain mismatch")
    if hashlib.sha256(source.encode("utf-8")).hexdigest() != pin["lean_file_sha256"]:
        raise ValueError("proof source digest mismatch")
    if set(receipt["declaration_replay"]) != set(THEOREMS):
        raise ValueError("theorem identity drift")
    for theorem in THEOREMS:
        result = receipt["declaration_replay"][theorem]
        if result["status"] != "LEAN_KERNEL_ACCEPTED" or set(result["axioms"]) != AXIOMS:
            raise ValueError("Lean replay or axioms mismatch")
    run = receipt["execution"]
    if run["exit_code"] != 0 or run["errors_reported"] != 0:
        raise ValueError("compiler evidence does not pass")
    if run["origin"] != "OS_ACCOUNT_ONLY_NOT_INDEPENDENTLY_AUTHENTICATED":
        raise ValueError("false independent execution")
    if receipt["scope"]["analytic_premise_independently_proved"] is not False:
        raise ValueError("false analytic theorem promotion")
    if receipt["scope"]["source_full_paper_semantic_equivalence_certified"] is not False:
        raise ValueError("false manuscript certification")
    if receipt["scope"]["mathcert_certification"] is not False:
        raise ValueError("false MATHCERT certification")
    if receipt["authority"]["mathematical_claim"] != "PROVED_CONDITIONAL_IMPLICATION_ONLY":
        raise ValueError("false unconditional claim")
    return True

class TestF011FullReplayCustody(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.receipt = json.loads(EVIDENCE.read_text())
        cls.source = LEAN.read_text()

    def test_exact_receipt(self):
        self.assertTrue(validate(self.receipt, self.source))

    def reject(self, mutate, error):
        d = deepcopy(self.receipt)
        mutate(d)
        with self.assertRaisesRegex(ValueError, error):
            validate(d, self.source)

    def test_false_unconditional_promotion(self):
        self.reject(lambda x: x["authority"].update(mathematical_claim="UNCONDITIONAL_PROVED"), "false unconditional")

    def test_false_analytic_premise_proved(self):
        self.reject(lambda x: x["scope"].update(analytic_premise_independently_proved=True), "false analytic")

    def test_false_certification(self):
        self.reject(lambda x: x["scope"].update(mathcert_certification=True), "false MATHCERT")

    def test_unexpected_axiom(self):
        self.reject(lambda x: x["declaration_replay"][THEOREMS[0]]["axioms"].append("admit"), "axioms mismatch")

    def test_falsified_compiler_exit(self):
        self.reject(lambda x: x["execution"].update(exit_code=1), "compiler evidence")

    def test_wrong_upstream(self):
        self.reject(lambda x: x["source"].update(upstream_commit="0"*40), "pinned source")

    def test_falsified_independent_execution(self):
        self.reject(lambda x: x["execution"].update(origin="EXTERNALLY_INDEPENDENT"), "false independent")

if __name__ == "__main__":
    unittest.main()
