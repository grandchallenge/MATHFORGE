"""Non-certifying source and replay-custody gates for OAI26 F011.

The external Lean compilation is a separate replay; tests must not represent
static source validation as a kernel proof.
"""
from copy import deepcopy
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
PIN = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
MANIFEST = "cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794"
SOURCE = ROOT / "WP03_FAMILY011_CONDITIONAL_SUPPLY_BRIDGE.lean"
LEDGER = ROOT / "WP03_FAMILY011_CONDITIONAL_SUPPLY_REPLAY.json"

def validate(doc, source):
    if doc["record_type"] != "GCL_OAI26_WP03_F011_CONDITIONAL_BRIDGE_REPLAY/1":
        raise ValueError("receipt type")
    if doc["source"]["commit"] != PIN or doc["source"]["lake_manifest_sha256"] != MANIFEST:
        raise ValueError("source identity")
    if doc["formalization"]["blob_sha1"] != "449f329248bde7ac27830deb1f1f3f5dcb35b276":
        raise ValueError("source blob")
    if doc["formalization"]["predicate"] != "GCL.OAI26.Family011.PrimeSupplyForExponent":
        raise ValueError("predicate custody")
    if doc["formalization"]["unconditional_prime_supply_proved"] is not False:
        raise ValueError("unsupported prime supply")
    if doc["disposition"] != "CONDITIONAL_TRANSFER_LEAN_COMPILED_SUPPLY_OPEN":
        raise ValueError("unsupported mathematical promotion")
    if doc["execution"]["bridge_lean_exit"] != 0 or doc["execution"]["source_module_build_exit"] != 0:
        raise ValueError("failed local Lean evidence")
    if doc["execution"]["independently_authenticated"] is not False:
        raise ValueError("false independent identity")
    if doc["execution"]["axioms_current_revised_file_replayed"] is not False:
        raise ValueError("false current axiom replay")
    if "def PrimeSupplyForExponent" not in source or "hsupply : PrimeSupplyForExponent ε" not in source:
        raise ValueError("missing explicit supply hypothesis")
    if "finite_large_fiber_rpow" not in source or "infinite_of_unbounded_g" not in source:
        raise ValueError("missing pinned transfer lemmas")
    if "sorry" in source or "admit" in source or "axiom " in source:
        raise ValueError("unsupported proof shortcut")
    return True

class TestF011Bridge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = json.loads(LEDGER.read_text())
        cls.source = SOURCE.read_text()

    def test_receipt_and_source(self):
        self.assertTrue(validate(self.doc, self.source))

    def reject(self, fn, error):
        doc = deepcopy(self.doc)
        source = self.source
        doc, source = fn(doc, source)
        with self.assertRaisesRegex(ValueError, error):
            validate(doc, source)

    def test_unconditional_promote(self):
        self.reject(lambda d,s:(dict(d, formalization=dict(d["formalization"], unconditional_prime_supply_proved=True)),s),"unsupported prime supply")

    def test_missing_supply(self):
        self.reject(lambda d,s:(d,s.replace("hsupply : PrimeSupplyForExponent ε","hsupply : True")),"missing explicit supply")

    def test_unsafe_axiom(self):
        self.reject(lambda d,s:(d,s+"\naxiom fabricated : True\n"),"unsupported proof shortcut")

    def test_unjustified_independent_authentication(self):
        self.reject(lambda d,s:(dict(d,execution=dict(d["execution"],independently_authenticated=True)),s),"false independent")

    def test_source_pin_drift(self):
        self.reject(lambda d,s:(dict(d,source=dict(d["source"],commit="0"*40)),s),"source identity")

    def test_false_revised_axiom_audit(self):
        self.reject(lambda d,s:(dict(d,execution=dict(d["execution"],axioms_current_revised_file_replayed=True)),s),"false current axiom")

    def test_fabricated_disposition(self):
        self.reject(lambda d,s:(dict(d,disposition="UNCONDITIONAL_THEOREM_PROVED"),s),"unsupported mathematical promotion")

if __name__ == "__main__":
    unittest.main()
