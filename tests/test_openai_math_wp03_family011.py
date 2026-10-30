import json,copy,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY011_PRIME_PREDECESSORS_INDEXED_COVERAGE.json"
def valid(d):
 s=d.get("source_lock",{});m=s.get("manuscripts",[]);i=d.get("indexed_search",{});c=d.get("coverage",{})
 return (d.get("family_id")=="011" and d.get("disposition")=="UNFORMALIZED_IN_PINNED_INDEXED_COMPARATOR_SCOPE" and s.get("commit")=="1581d4cbdd69a0faf34b2089614fe2a814316a6a" and [x.get("blob") for x in m]==["3d9d4c55c1f30d7736e7c7427b97cb0461f06040","79950676c100e2d2d9252cc5465707a0d8f6c891","837740bf086f56d9c20fba6b3c7ff20ff53b581d"] and i.get("upstream_lean_docs_011_present") is False and i.get("direct_named_prime_predecessor_Poisson_Dirichlet_match") is False and c.get("initial_review_of_family011_complete") is True and c.get("all_twelve_pilot_initial_reviews_present") is True and c.get("full_semantic_bridge_complete") is False and c.get("WP03_parent_complete") is False and "NOT all twelve proof-semantic matches" in d.get("claim_boundary",""))
class F011(unittest.TestCase):
 def test_positive(self):self.assertTrue(valid(json.loads(P.read_text())))
 def test_hostile(self):
  d=json.loads(P.read_text());changes=[lambda z:z.__setitem__("disposition","FULL_MATCH"),lambda z:z["source_lock"].__setitem__("commit","0"*40),lambda z:z["source_lock"]["manuscripts"].pop(),lambda z:z["source_lock"]["manuscripts"][0].__setitem__("blob","0"*40),lambda z:z["indexed_search"].__setitem__("upstream_lean_docs_011_present",True),lambda z:z["indexed_search"].__setitem__("direct_named_prime_predecessor_Poisson_Dirichlet_match",True),lambda z:z["coverage"].__setitem__("full_semantic_bridge_complete",True),lambda z:z["coverage"].__setitem__("WP03_parent_complete",True),lambda z:z.__setitem__("claim_boundary","All certified")]
  for change in changes:
   x=copy.deepcopy(d);change(x);self.assertFalse(valid(x))
if __name__=="__main__":unittest.main()
