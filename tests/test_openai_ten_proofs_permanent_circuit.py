from __future__ import annotations
import copy, importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('v',ROOT/'ci/validate_openai_ten_proofs_permanent_circuit.py')
assert SPEC and SPEC.loader
V=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(V)
class CircuitAuditTests(unittest.TestCase):
    def setUp(self): self.r=V.load(V.RECORD)
    def errors(self,r=None): return V.validation_errors(copy.deepcopy(self.r if r is None else r))
    def mutate_source(self,k,v):
        r=copy.deepcopy(self.r); r['source_theorem_1_1'][k]=v; return r
    def test_current(self): self.assertEqual(self.errors(),[])
    def test_threshold(self): self.assertTrue(self.errors(self.mutate_source('dimension_threshold',65535)))
    def test_constant(self): self.assertTrue(self.errors(self.mutate_source('finite_bound_denominator',143)))
    def test_division(self): self.assertTrue(self.errors(self.mutate_source('division_allowed',True)))
    def test_fanout(self): self.assertTrue(self.errors(self.mutate_source('fanout_reuse_allowed',False)))
    def test_input_count(self): self.assertTrue(self.errors(self.mutate_source('input_gates_counted',True)))
    def test_target_count(self):
        r=copy.deepcopy(self.r); r['exact_overlay_replay']['target_count']=2; self.assertTrue(self.errors(r))
    def test_nanoda(self):
        r=copy.deepcopy(self.r); r['exact_overlay_replay']['nanoda_kernel']='failed'; self.assertTrue(self.errors(r))
    def test_nonvacuity(self):
        r=copy.deepcopy(self.r); r['nonvacuity']['state']='BLOCKED'; self.assertTrue(self.errors(r))
    def test_bigomega_loss(self):
        r=copy.deepcopy(self.r); r['coverage']['source_theorem_1_1_bigomega_consequence']=False; self.assertTrue(self.errors(r))
    def test_formula_mutation(self):
        r=copy.deepcopy(self.r); r['coverage']['formula_theorems_1_2_1_3_mutated']=True; self.assertTrue(self.errors(r))
    def test_pdf_inflation(self):
        r=copy.deepcopy(self.r); r['coverage']['historical_pdf_byte_equivalence']=True; self.assertTrue(self.errors(r))
    def test_solve_inflation(self):
        r=copy.deepcopy(self.r); r['coverage']['solve_handoff']=True; self.assertTrue(self.errors(r))
    def test_cert_inflation(self):
        r=copy.deepcopy(self.r); r['coverage']['mathcert_intake_or_route']=True; self.assertTrue(self.errors(r))
    def test_adjudication(self):
        r=copy.deepcopy(self.r); r['coverage']['adjudication']=True; self.assertTrue(self.errors(r))
    def test_aggregate(self):
        r=copy.deepcopy(self.r); r['coverage']['aggregate_ten_proofs_authority']=True; self.assertTrue(self.errors(r))
if __name__=='__main__': unittest.main()
