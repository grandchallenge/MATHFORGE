"""Guard exact Lean-replayed F011 external real-x to GCL natural-x statement adapter.

Static tests do not substitute for the source-pinned Lean compiler receipt.
"""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]/"sources"/"OPENAI-MATH-2026"
SRC=ROOT/"WP03_FAMILY011_EXTERNAL_REAL_TO_NAT_ADAPTER.lean"
LEDGER=ROOT/"WP03_FAMILY011_EXTERNAL_REAL_TO_NAT_ADAPTER_REPLAY.json"
SHA256="566efa9ff4d4f91f0dbba5f002ce5a2eb604ad63a9b9a03e086894a85c06b066"
UPSTREAM="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
AXIOMS={"propext","Classical.choice","Quot.sound"}
NAMES=(
"GCL.OAI26.Family011.smooth_count_of_external",
"GCL.OAI26.Family011.infinite_fibers_of_external")

def verify(s, j):
    if j["record_type"]!="GCL_OAI26_F011_EXTERNAL_REAL_TO_NAT_LEAN_REPLAY/1":
        raise ValueError("wrong receipt type")
    if sha256(s.encode()).hexdigest()!=SHA256 or j["proof"]["sha256"]!=SHA256:
        raise ValueError("proof source hash mismatch")
    if j["gcl_source"]["commit"]!=UPSTREAM or j["gcl_source"]["toolchain"]!="leanprover/lean4:v4.34.1":
        raise ValueError("upstream source drift")
    if j["external_source"]["commit"]!="f75d4f2c2d6685a0547f17fa07240377aa2c2ed4":
        raise ValueError("external revision drift")
    if not j["proof"]["previous_protected_source_byte_prefix_identical"]:
        raise ValueError("GCL proof prefix drift")
    if set(j["proof"]["theorems"])!=set(NAMES):
        raise ValueError("theorem custody drift")
    for x in NAMES:
        r=j["proof"]["theorems"][x]
        if r["lean_exit"]!=0 or set(r["axioms"])!=AXIOMS:
            raise ValueError("kernel receipt or axioms drift")
    if j["execution"]["compiler_exit"]!=0 or j["execution"]["compiler_errors"]!=0:
        raise ValueError("local Lean compiler failure")
    if j["execution"]["roles_separate_external_identity"] is not False:
        raise ValueError("false independent identity")
    if j["boundaries"]["external_unconditional_supply_kernel_replayed_by_gcl"] is not False:
        raise ValueError("unearned external theorem acceptance")
    if j["boundaries"]["mathcert_certified"] is not False or j["boundaries"]["programme_closed"] is not False:
        raise ValueError("premature certification")
    if j["external_source"]["note"].find("NOT imported")<0:
        raise ValueError("missing non-import scope boundary")
    anchors=("def ExternalSmoothPrimeCount : Prop",
             "noncomputable def externalSmoothShiftedPrimes",
             "Finset.Ioc ⌊2 * x⌋₊ ⌊5 * x⌋₊",
             "q.Prime → q ∣ p - 1",
             "theorem smooth_count_of_external",
             "theorem infinite_fibers_of_external",
             "theorem prime_supply_of_smooth_count",
             "#print axioms GCL.OAI26.Family011.smooth_count_of_external",
             "#print axioms GCL.OAI26.Family011.infinite_fibers_of_external")
    if any(v not in s for v in anchors):
        raise ValueError("source semantic anchor lost")
    if re.search(r"(?m)^\s*(sorry|admit|axiom)\b",s):
        raise ValueError("unproved placeholder")
    return True

class TestF011ExternalAdapter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s=SRC.read_text()
        cls.j=json.loads(LEDGER.read_text())
    def test_exact(self):
        self.assertTrue(verify(self.s,self.j))
    def reject(self,mutate,error):
        x=deepcopy(self.j)
        mutate(x)
        with self.assertRaisesRegex(ValueError,error):
            verify(self.s,x)
    def test_external_false_acceptance(self):
        self.reject(lambda x:x["boundaries"].update(external_unconditional_supply_kernel_replayed_by_gcl=True),"unearned external")
    def test_mathcert_promotion(self):
        self.reject(lambda x:x["boundaries"].update(mathcert_certified=True),"premature certification")
    def test_kernel_error(self):
        self.reject(lambda x:x["execution"].update(compiler_exit=1),"local Lean")
    def test_axios(self):
        self.reject(lambda x:x["proof"]["theorems"][NAMES[0]]["axioms"].append("sorryAx"),"axioms")
    def test_source_swap(self):
        self.reject(lambda x:x["external_source"].update(commit="0"*40),"external revision")
    def test_false_identity(self):
        self.reject(lambda x:x["execution"].update(roles_separate_external_identity=True),"false independent")
    def test_erased_prime_shift(self):
        with self.assertRaisesRegex(ValueError,"source"):
            verify(self.s.replace("q.Prime → q ∣ p - 1","q.Prime → q ∣ p"),self.j)
    def test_proof_placeholder(self):
        with self.assertRaisesRegex(ValueError,"proof source hash"):
            verify(self.s+"\nsorry\n",self.j)

if __name__=="__main__":
    unittest.main()
