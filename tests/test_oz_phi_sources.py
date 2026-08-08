import copy,importlib.util,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'sources/OZ-PHI-SOURCES-001'
s=importlib.util.spec_from_file_location('v',ROOT/'ci/validate_oz_phi_sources.py');v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
class T(unittest.TestCase):
 def setUp(self):self.m=json.loads((P/'manifest.json').read_text());self.e=json.loads((P/'coefficient_laws.json').read_text())
 def test_valid(self):self.assertEqual(v.errors(self.m,self.e),[])
 def test_blob_drift(self):b=copy.deepcopy(self.m);b['authority']['source_blobs']['ledger']['blob']='0'*40;self.assertTrue(v.errors(b,self.e))
 def test_family_insert(self):b=copy.deepcopy(self.m);b['family_partition']['eisenstein_source_claims'].append('s7');self.assertTrue(v.errors(b,self.e))
 def test_law_mutation(self):e=copy.deepcopy(self.e);e['A'][5]+=1;self.assertTrue(v.errors(self.m,e))
 def test_cooper_promotion(self):b=copy.deepcopy(self.m);b['family_partition']['no_fit_in_stated_basis']=[];self.assertTrue(v.errors(b,self.e))
 def test_modularity_inflation(self):b=copy.deepcopy(self.m);b['replay']['modularity_hypotheses_certified']=True;self.assertTrue(v.errors(b,self.e))
 def test_solve_promotion(self):b=copy.deepcopy(self.m);b['nonclaims']['mathsolve_authorized']=True;self.assertTrue(v.errors(b,self.e))
if __name__=='__main__':unittest.main()
