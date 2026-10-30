import copy,json,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY003_QUASI_RIEMANN_EDITION_REVIEW.json"
def valid(d):
 s=d.get("source_lock",{});a=d.get("source_results",[]);l=d.get("lean_targets",[]);c=d.get("coverage",{})
 return (d.get("record_type")=="GCL_OAI26_WP03_F003_THREE_EDITION_SEMANTIC_TRIAGE/1" and d.get("family_id")=="003" and d.get("disposition")=="PROPOSITION_LEVEL_ALIGNMENT_WITH_VERSION_DISTINCTION" and s.get("commit")=="1581d4cbdd69a0faf34b2089614fe2a814316a6a" and len(s.get("manuscript_source_files",[]))==3 and [x.get("git_blob") for x in s["manuscript_source_files"]]==["268c4e3206d460c617d3d2129742a72b831b3def","2000faddbbebac5de0ecfe0b962534ea61a852d5","7e41c77c252348369ca0fb99cbe389271ba6ce86"] and [x.get("main_bound") for x in a]==["Re(s)>7/8","Re(s)>11/12","one uniform c/log q gap"] and len(l)==4 and c.get("manuscript_count")==3 and c.get("deep_semantic_bridge_complete") is False and c.get("other_pilot_families_open") is True and "no exhaustive model bridge" in d.get("claim_boundary",""))
class F003(unittest.TestCase):
 def test_positive(self):self.assertTrue(valid(json.loads(P.read_text())))
 def test_hostile(self):
  d=json.loads(P.read_text())
  edits=[
   lambda x:x.__setitem__("disposition","FULL_SEMANTIC_MATCH_PROVED"),
   lambda x:x["source_lock"].__setitem__("commit","0"*40),
   lambda x:x["source_lock"]["manuscript_source_files"].pop(),
   lambda x:x["source_results"][1].__setitem__("main_bound","Re(s)>7/8"),
   lambda x:x["source_results"][0].__setitem__("main_bound","Re(s)>1/2"),
   lambda x:x["source_results"][2].__setitem__("main_bound","no real zeros at all"),
   lambda x:x["lean_targets"].pop(),
   lambda x:x["coverage"].__setitem__("deep_semantic_bridge_complete",True),
   lambda x:x["coverage"].__setitem__("other_pilot_families_open",False),
   lambda x:x.__setitem__("claim_boundary","The manuscripts are certified")
  ]
  for f in edits:
   z=copy.deepcopy(d);f(z);self.assertFalse(valid(z))
if __name__=="__main__":unittest.main()
