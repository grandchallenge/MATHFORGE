"""Guard OAI26 Family 011 conditional prime-supply bridge against false promotion."""
import json
from pathlib import Path
from copy import deepcopy
import unittest

ROOT=Path(__file__).resolve().parents[1]/"sources"/"OPENAI-MATH-2026"
DOC=ROOT/"WP03_FAMILY011_CONDITIONAL_SUPPLY_BRIDGE_REPLAY.json"
LEAN=ROOT/"WP03_FAMILY011_CONDITIONAL_SUPPLY_BRIDGE.lean"
PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"

def validate(d,s):
    if d["source_lock"]["commit"]!=PIN or d["source_lock"]["upstream_module_blob"]!="217cfe4d7f9c39981eabe9bbeeb8458febb0fc76":
        raise ValueError("source pin")
    if d["local_lean_replay"]["source_file"]!="sources/OPENAI-MATH-2026/WP03_FAMILY011_CONDITIONAL_SUPPLY_BRIDGE.lean":
        raise ValueError("source binding")
    if "theorem infinite_fibers_of_supply" not in s or "def PrimeSupplyForExponent" not in s or "sorry" in s or "admit" in s:
        raise ValueError("Lean proof text")
    if "hsupply : PrimeSupplyForExponent ε" not in s or "finite_large_fiber_rpow" not in s or "infinite_of_unbounded_g" not in s:
        raise ValueError("unproved supply hypothesis erased")
    if d["conditional_result"]["hypotheses"]!=["0 < ε","ε ≤ 1","PrimeSupplyForExponent ε"]:
        raise ValueError("hypothesis drift")
    if d["missing_analytic_bridge"]["status"]!="UNPROVED" or d["mathematical_certification"] is not False or d["programme_close"] is not False:
        raise ValueError("unearned certification or prime supply")
    if d["local_lean_replay"]["exact_revised_bridge_compile_exit"]!=0:
        raise ValueError("replay failure")
    if d["local_lean_replay"]["chad_execution_origin"]!="LOCAL_OS_ONLY_NOT_INDEPENDENTLY_AUTHENTICATED":
        raise ValueError("false independent replay")
    if d["disposition"]!="CONDITIONAL_LEAN_BRIDGE_COMPILED_NONCERTIFYING":
        raise ValueError("inflated disposition")
    return True

class TestFamily011ConditionalBridge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(DOC.read_text())
        cls.source=LEAN.read_text()
    def test_positive(self):
        self.assertTrue(validate(self.data,self.source))
    def hostile(self, change, failure, source=None):
        x=deepcopy(self.data)
        change(x)
        with self.assertRaisesRegex(ValueError,failure):
            validate(x,self.source if source is None else source)
    def test_no_prime_supply_promotion(self):
        self.hostile(lambda x:x["missing_analytic_bridge"].update(status="PROVED"),"unearned")
    def test_no_certification(self):
        self.hostile(lambda x:x.update(mathematical_certification=True),"unearned")
    def test_no_programme_closure(self):
        self.hostile(lambda x:x.update(programme_close=True),"unearned")
    def test_no_false_independence(self):
        self.hostile(lambda x:x["local_lean_replay"].update(chad_execution_origin="INDEPENDENTLY_AUTHENTICATED"),"false independent")
    def test_pin_not_rewritable(self):
        self.hostile(lambda x:x["source_lock"].update(commit="0"*40),"source pin")
    def test_no_premise_erasure(self):
        self.hostile(lambda x:None,"unproved supply hypothesis erased",self.source.replace("hsupply : PrimeSupplyForExponent ε","hsupply : True"))
    def test_no_sorry(self):
        self.hostile(lambda x:None,"Lean proof text",self.source+"\nsorry\n")
    def test_no_false_disposition(self):
        self.hostile(lambda x:x.update(disposition="FULL_MANUSCRIPT_PROVED"),"inflated")

if __name__=="__main__":unittest.main()
