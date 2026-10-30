import copy,json,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY010_PROMODULARITY_INDEXED_COVERAGE.json"
def valid(d):
 s=d.get("source_lock",{});i=d.get("indexed_search",{});c=d.get("coverage",{})
 return (d.get("record_type")=="GCL_OAI26_WP03_F010_BOUNDED_INDEX_REVIEW/1" and d.get("disposition")=="UNFORMALIZED_IN_PINNED_INDEXED_COMPARATOR_SCOPE" and s.get("commit")=="1581d4cbdd69a0faf34b2089614fe2a814316a6a" and [x.get("blob") for x in s.get("introductions",[])]==["8ed0f2c8c7188b5518cca2c1852178d3a5cb0286","2062b92ebaaf703861ff18deca6341c3243d0a16","7ec908e661050a5dfa8ca2cb9a1501b6b41c62cc"] and [x.get("name") for x in d.get("results",[])]==["unrestricted_pro_modularity","hecke_dimension","fontaine_mazur"] and i.get("upstream_docs_010_present") is False and i.get("named_matches_for_modularity_hecke_fontaine_mazur")==0 and c.get("complete_formal_semantic_bridge") is False and c.get("pilot_complete") is False and "no claim that all Lean formalizations are absent" in d.get("claim_boundary",""))
class Review(unittest.TestCase):
 def test_positive(self):self.assertTrue(valid(json.loads(P.read_text())))
 def test_hostile(self):
  d=json.loads(P.read_text());changes=[
   lambda z:z.__setitem__("disposition","FULL_SEMANTIC_MATCH"),
   lambda z:z["source_lock"].__setitem__("commit","0"*40),
   lambda z:z["source_lock"]["introductions"].pop(),
   lambda z:z["results"].pop(),
   lambda z:z["indexed_search"].__setitem__("upstream_docs_010_present",True),
   lambda z:z["indexed_search"].__setitem__("named_matches_for_modularity_hecke_fontaine_mazur",1),
   lambda z:z["coverage"].__setitem__("complete_formal_semantic_bridge",True),
   lambda z:z["coverage"].__setitem__("pilot_complete",True),
   lambda z:z.__setitem__("claim_boundary","All theorems certified")
  ]
  for f in changes:
   a=copy.deepcopy(d);f(a);self.assertFalse(valid(a))
if __name__=="__main__":unittest.main()
