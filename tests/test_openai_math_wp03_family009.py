"""WP03 F009: falsifiable partial semantic coverage (injectivity != bijection)."""
import unittest,copy,json
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY009_BOGOMOLOV_POP_PARTIAL_REVIEW.json"
def accepted(d):
 if d.get("record_type")!="GCL_OAI26_WP03_F009_PARTIAL_SEMANTIC_REVIEW/1" or d.get("disposition")!="PARTIAL_MAIN_THEOREM_COVERAGE_INJECTIVITY_ONLY":return False
 s=d.get("source_lock",{});f=s.get("files",{})
 if s.get("commit")!="1581d4cbdd69a0faf34b2089614fe2a814316a6a":return False
 if f.get("lean_solution",{}).get("git_blob")!="13e184237fe9ba63a29a37759380186b3966edac":return False
 if f.get("manuscript_intro",{}).get("git_blob")!="a1b052285ded0ec86649397e97f8509c56fa561a":return False
 if f.get("comparator_config",{}).get("git_blob")!="0e15aa9446aebad38c9aae88d0c78d4ef09f881d":return False
 m=d.get("manuscript",{})
 if "BIJECTIVE" not in m.get("main_theorem",""):return False
 if m.get("pdf_sha256")!="4d805627401fffef78e1f0d8e21a0585f6c733e8be90643d0065cd27ffaa24f2":return False
 if len(m.get("main_theorem_component_results",[]))!=3:return False
 l=d.get("lean",{})
 if l.get("selected_theorem")!="OAI.BogomolovPop.main_graph_injective":return False
 if l.get("main_statement_contains_surjectivity") is not False or l.get("main_statement_contains_injectivity") is not True:return False
 if l.get("comparator_executed_in_review") is not False:return False
 if d.get("family_scope",{}).get("family_manuscript_count")!=3:return False
 if len(d["family_scope"]["not_reviewed_manuscripts"])!=2:return False
 if d.get("coverage",{}).get("full_family_review_complete") is not False:return False
 if d["coverage"]["twelve_family_pilot_complete"] is not False:return False
 if "NOT matched in full" not in d.get("claim_boundary",""):return False
 return True
class Family009(unittest.TestCase):
 def test_positive(self):self.assertTrue(accepted(json.loads(P.read_text())))
 def test_hostile(self):
  d=json.loads(P.read_text())
  muts=[
   lambda z:z.__setitem__("disposition","FULL_SEMANTIC_MATCH"),
   lambda z:z["lean"].__setitem__("main_statement_contains_surjectivity",True),
   lambda z:z["lean"].__setitem__("selected_theorem","OAI.Fake.bijection"),
   lambda z:z["manuscript"].__setitem__("main_theorem","INJECTIVE"),
   lambda z:z["source_lock"].__setitem__("commit","0"*40),
   lambda z:z["source_lock"]["files"]["lean_solution"].__setitem__("git_blob","0"*40),
   lambda z:z["lean"].__setitem__("comparator_executed_in_review",True),
   lambda z:z["family_scope"].__setitem__("not_reviewed_manuscripts",[]),
   lambda z:z["coverage"].__setitem__("full_family_review_complete",True),
   lambda z:z["coverage"].__setitem__("twelve_family_pilot_complete",True),
  ]
  for mut in muts:
   x=copy.deepcopy(d);mut(x);self.assertFalse(accepted(x))
if __name__=="__main__":unittest.main()
