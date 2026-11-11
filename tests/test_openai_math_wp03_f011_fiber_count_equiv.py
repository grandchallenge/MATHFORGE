"""Pinned mathematical custody guard for external and GCL totient-fiber semantics.

An earlier exact source-pinned Lean 4.34.1 kernel replay is separately recorded.
This Python guard does not itself prove the mathematics.
"""
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
import json
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]/"sources"/"OPENAI-MATH-2026"
SOURCE=ROOT/"WP03_FAMILY011_EXTERNAL_FIBER_COUNT_EQUIV.lean"
RECEIPT=ROOT/"WP03_FAMILY011_EXTERNAL_FIBER_COUNT_EQUIV_REPLAY.json"
EXPECTED_SHA="30886e87944de53e0f681ccfe8d6d4a71bd5fe6607abe16e44b524bf3153c31c"
EXPECTED_HEAD="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
EXTERNAL_HEAD="f75d4f2c2d6685a0547f17fa07240377aa2c2ed4"
THEOREMS=[
"GCL.OAI26.Family011.external_fiber_count_eq_g_of_pos",
"GCL.OAI26.Family011.infinite_gcl_of_external",
"GCL.OAI26.Family011.gcl_claim_of_external_claim"]
AXIOMS={"propext","Classical.choice","Quot.sound"}

def validate(source,record):
    if record["record_type"]!="GCL_OAI26_F011_EXTERNAL_G_EQUIV_LEAN_REPLAY/1":
        raise ValueError("wrong record type")
    if sha256(source.encode()).hexdigest()!=EXPECTED_SHA or record["proof"]["sha256"]!=EXPECTED_SHA:
        raise ValueError("source hash drift")
    if record["external_source"]["commit"]!=EXTERNAL_HEAD or record["gcl_source"]["commit"]!=EXPECTED_HEAD:
        raise ValueError("source revision drift")
    if record["external_source"]["git_blob_sha1"]!="ac85c9a6a0878d18de3d923ca1a14e8213089c03":
        raise ValueError("external g source changed")
    if record["gcl_source"]["git_blob_sha1"]!="217cfe4d7f9c39981eabe9bbeeb8458febb0fc76":
        raise ValueError("GCL g source changed")
    if set(record["proof"]["theorems"])!=set(THEOREMS):
        raise ValueError("missing formal theorem")
    for name in THEOREMS:
        d=record["proof"]["theorems"][name]
        if d["lean_exit"]!=0 or set(d["axioms"])!=AXIOMS:
            raise ValueError("failed or untrusted theorem")
    if record["proof"]["execution"]["compiler_exit"]!=0 or record["proof"]["execution"]["compiler_errors"]!=0:
        raise ValueError("Lean replay incomplete")
    b=record["acceptance_limits"]
    if b["external_unconditional_theorem_proof_replayed_by_gcl"] or b["mathcert_certified"] or b["programme_closed"]:
        raise ValueError("unearned external proof acceptance")
    anchors=["Nat.totient m = n",
             "OAI.TotientFibers.g n",
             "theorem external_fiber_count_eq_g_of_pos",
             "0 < n",
             "theorem infinite_gcl_of_external",
             "h.sdiff (Set.finite_singleton 0)",
             "theorem gcl_claim_of_external_claim",
             "#print axioms GCL.OAI26.Family011.gcl_claim_of_external_claim"]
    if any(s not in source for s in anchors):
        raise ValueError("altered theorem text")
    if re.search(r"(?m)^\\s*(sorry|admit|axiom)\\b",source):
        raise ValueError("proof placeholder")
    return True

class TestF011TotientFiberIdentity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s=SOURCE.read_text()
        cls.j=json.loads(RECEIPT.read_text())
    def test_valid_receipt(self):self.assertTrue(validate(self.s,self.j))
    def reject(self,change,message):
        x=deepcopy(self.j);change(x)
        with self.assertRaisesRegex(ValueError,message):validate(self.s,x)
    def test_wrong_external_head(self):
        self.reject(lambda x:x["external_source"].update(commit="0"*40),"revision")
    def test_wrong_g_definition(self):
        self.reject(lambda x:x["gcl_source"].update(git_blob_sha1="0"*40),"GCL g")
    def test_unearned_external_proof_pass(self):
        self.reject(lambda x:x["acceptance_limits"].update(external_unconditional_theorem_proof_replayed_by_gcl=True),"unearned")
    def test_unearned_certification(self):
        self.reject(lambda x:x["acceptance_limits"].update(mathcert_certified=True),"unearned")
    def test_lost_theorem(self):
        self.reject(lambda x:x["proof"]["theorems"].pop(THEOREMS[1]),"missing formal")
    def test_sorry_axiom(self):
        self.reject(lambda x:x["proof"]["theorems"][THEOREMS[2]]["axioms"].append("sorryAx"),"untrusted")
    def test_false_lean_result(self):
        self.reject(lambda x:x["proof"]["execution"].update(compiler_exit=1),"replay incomplete")
    def test_erased_zero_exclusion(self):
        with self.assertRaisesRegex(ValueError,"source hash drift"):
            validate(self.s.replace("h.sdiff (Set.finite_singleton 0)","h"),self.j)

if __name__=="__main__":
    unittest.main()
