"""Validate pinned WP03 family 012 evidence and reject hostile overclaims."""
import copy,json,unittest
from pathlib import Path
F=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY012_DICKMAN_SEMANTIC_REVIEW.json"
DECL=["OAI.JointDickmanPaper.joint_law","OAI.JointDickmanPaper.increasing_order","OAI.JointDickmanPaper.decreasing_order"]
def valid(d):
 s=d.get("source_lock",{});f=d.get("formalization",{});m=d.get("manuscript",{})
 if d.get("record_type")!="GCL_OAI26_WP03_F012_SEMANTIC_REVIEW/1" or d.get("disposition")!="PROPOSITION_LEVEL_ALIGNMENT":return False
 if s.get("commit")!="1581d4cbdd69a0faf34b2089614fe2a814316a6a":return False
 if s.get("solution_blob")!="ccc0cf7b37c5163324aec1a6b91dd9efd22d7aec" or s.get("intro_blob")!="148765fb95c33fee7ad7c9e31500c16da5eebf59":return False
 if s.get("config_blob")!="7267219acc9f42d882a8704c66c94435235d5b9c":return False
 if f.get("theorems")!=DECL or f.get("challenge_config_theorem_names")!=DECL:return False
 if f.get("comparator_executed_in_review") is not False or f.get("axiom_closure_replayed_in_review") is not False:return False
 if f.get("proof_entrypoints_non_sorry") is not True:return False
 if len(m.get("additional_claims_outside_selected_theorem",[]))<2:return False
 if not all(x in m.get("main_claim","") for x in ["n^a","n^b","real cutoffs"]):return False
 if "strict orderings" not in m.get("order_corollary",""):return False
 if d.get("critic_review",{}).get("independently_authenticated") is not False:return False
 if d.get("coverage",{}).get("other_pilot_open") is not True:return False
 if "no independently proved definition/model equivalence" not in d.get("claim_boundary",""):return False
 return True
class Family012(unittest.TestCase):
 def test_positive(self):self.assertTrue(valid(json.loads(F.read_text())))
 def test_hostile(self):
  d=json.loads(F.read_text())
  mutations=[
   lambda x:x["source_lock"].__setitem__("commit","0"*40),
   lambda x:x["source_lock"].__setitem__("solution_blob","0"*40),
   lambda x:x["formalization"].__setitem__("theorems",DECL[:2]),
   lambda x:x["formalization"].__setitem__("comparator_executed_in_review",True),
   lambda x:x["formalization"].__setitem__("axiom_closure_replayed_in_review",True),
   lambda x:x["coverage"].__setitem__("other_pilot_open",False),
   lambda x:x["manuscript"].__setitem__("main_claim","joint limit of n^a and X^b"),
   lambda x:x.__setitem__("disposition","FULL_SEMANTIC_MATCH_PROVED"),
  ]
  for mutate in mutations:
   a=copy.deepcopy(d);mutate(a);self.assertFalse(valid(a))
if __name__=="__main__":unittest.main()
