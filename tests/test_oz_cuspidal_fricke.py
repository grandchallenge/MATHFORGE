import copy,importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'sources/OZ-CUSPIDAL-FRICKE-001'
s=importlib.util.spec_from_file_location('v',ROOT/'ci/validate_oz_cuspidal_fricke.py');v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
class T(unittest.TestCase):
 def setUp(self):self.m=json.loads((P/'manifest.json').read_text());self.e=json.loads((P/'evidence.json').read_text())
 def test_valid(self):self.assertEqual(v.errors(self.m,self.e),[])
 def test_blob_drift(self):b=copy.deepcopy(self.m);b['authority']['source_blobs']['d1_ledger']['blob']='0'*40;self.assertTrue(v.errors(b,self.e))
 def test_denominator_mutation(self):e=copy.deepcopy(self.e);e['d1']['all_scaled_integer']=False;self.assertTrue(v.errors(self.m,e))
 def test_newform_mutation(self):e=copy.deepcopy(self.e);e['newform']['fstar_q1_q8'][1]=-5;self.assertTrue(v.errors(self.m,e))
 def test_all_n_promotion(self):b=copy.deepcopy(self.m);b['claim_decomposition']['d1_all_n_denominator']='PROVED';self.assertTrue(v.errors(b,self.e))
 def test_half_constant_promotion(self):b=copy.deepcopy(self.m);b['claim_decomposition']['d1_exact_half_constant']='PROVED';self.assertTrue(v.errors(b,self.e))
 def test_irrationality_inflation(self):b=copy.deepcopy(self.m);b['nonclaims']['irrationality_theorem']=True;self.assertTrue(v.errors(b,self.e))
if __name__=='__main__':unittest.main()
