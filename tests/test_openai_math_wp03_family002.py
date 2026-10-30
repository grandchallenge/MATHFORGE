import copy, json, unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY002_BSD_INDEXED_COVERAGE.json"
def valid(d):
 a=d.get("source_lock",{});b=d.get("index_assessment",{});c=d.get("coverage",{});m=d.get("manuscript_claims",[])
 return (d.get("record_type")=="GCL_OAI26_WP03_F002_BOUNDED_INDEX_REVIEW/1" and d.get("disposition")=="UNFORMALIZED_IN_PINNED_INDEXED_COMPARATOR_SCOPE" and a.get("commit")=="1581d4cbdd69a0faf34b2089614fe2a814316a6a" and [x.get("blob") for x in a.get("source_introductions",[])]==["8afa7de5ae4ade572e70565d81d624bd34476c4e","553f4809afa0d22a18a5e1943281717a27fac579","3f6fb17bc250067d9fa2f9933f099310dac56a39"] and [x.get("name") for x in m]==["full_BSD","all_prime_converse","two_primary_BSD"] and b.get("source_manuscript_count")==3 and b.get("crosswalk_main_result_count")==200 and b.get("named_BSD_Selmer_crosswalk_hits")==0 and b.get("upstream_lean_docs_002_present") is False and b.get("named_BSD_Selmer_comparator_hits")==0 and c.get("full_semantic_bridge_complete") is False and c.get("all_12_pilot_families_complete") is False and "does NOT establish no Lean theorem anywhere" in d.get("claim_boundary",""))
class F002(unittest.TestCase):
 def test_positive(self):self.assertTrue(valid(json.loads(P.read_text())))
 def test_hostile(self):
  d=json.loads(P.read_text());f=[
   lambda z:z.__setitem__("disposition","FULL_SEMANTIC_MATCH"),
   lambda z:z["source_lock"].__setitem__("commit","0"*40),
   lambda z:z["source_lock"]["source_introductions"].pop(),
   lambda z:z["source_lock"]["source_introductions"][0].__setitem__("blob","0"*40),
   lambda z:z["manuscript_claims"].pop(),
   lambda z:z["index_assessment"].__setitem__("upstream_lean_docs_002_present",True),
   lambda z:z["index_assessment"].__setitem__("named_BSD_Selmer_comparator_hits",1),
   lambda z:z["coverage"].__setitem__("full_semantic_bridge_complete",True),
   lambda z:z["coverage"].__setitem__("all_12_pilot_families_complete",True),
   lambda z:z.__setitem__("claim_boundary","All claims are proven in Lean")
  ]
  for edit in f:
   x=copy.deepcopy(d);edit(x);self.assertFalse(valid(x))
if __name__=="__main__":unittest.main()
