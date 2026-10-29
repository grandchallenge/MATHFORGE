"""WP03 F007 exact-source statement scope: positive and hostile fixtures."""
import copy,json,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY007_ORDINARY_CORRELATIONS_REVIEW.json"
PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
THEOREMS=["OAI.OrdinaryTwoPointCorrelations.liouville_log_saving","OAI.OrdinaryTwoPointCorrelations.binary_corrected_elliott","OAI.OrdinaryTwoPointCorrelations.affine_corrected_elliott"]
def check(d):
 if d.get("record_type")!="GCL_OAI26_WP03_F007_PROPOSITION_TRIAGE/1" or d.get("disposition")!="BOUNDED_THREE_RESULT_STATEMENT_ALIGNMENT":return False
 s=d.get("source",{})
 if s.get("commit")!=PIN or s.get("pdf_sha256")!="ccb6f339a7505db7ab158dae4b739164ed8dda32be4012b0310198dd32f5c70a":return False
 if s.get("pdf_git_blob")!="a1fa025a59ecbfc5176d16cfdc6e0afd418cc82e" or s.get("pdf_pages")!=87:return False
 if s.get("lean_source_blob")!="2bd48811e73bbdc80c1f738fa889a14189186408":return False
 r=d.get("results",[])
 if [x.get("lean") for x in r]!=THEOREMS:return False
 if any("limitation" not in x or not x["limitation"] for x in r):return False
 if any("nonproportional" not in x["finding"] for x in (r[0],r[2])):return False
 if "uniform nonpretentiousness" not in r[1]["finding"]:return False
 if d.get("comparator",{}).get("executed_this_review") is not False:return False
 if d["comparator"]["config_selected_theorems"]!=THEOREMS:return False
 if d.get("review",{}).get("mathematical_certification") is not False:return False
 if d["review"]["all_imported_definitions_checked"] is not False:return False
 if "not complete definition bridge" not in d.get("claim_boundary",""):return False
 return True
class Family007(unittest.TestCase):
 def test_positive(self):self.assertTrue(check(json.loads(P.read_text())))
 def test_hostile(self):
  x=json.loads(P.read_text())
  changes=[
   lambda d:d["source"].__setitem__("commit","0"*40),
   lambda d:d["source"].__setitem__("pdf_sha256","0"*64),
   lambda d:d["results"][0].__setitem__("lean","OAI.Fake"),
   lambda d:d["results"][0].__setitem__("finding","all affine pairs"),
   lambda d:d["results"][1].__setitem__("finding","cancellation without uniformity"),
   lambda d:d["comparator"].__setitem__("executed_this_review",True),
   lambda d:d["review"].__setitem__("mathematical_certification",True),
   lambda d:d.__setitem__("disposition","FULL_CERTIFIED"),
  ]
  for fn in changes:
   y=copy.deepcopy(x);fn(y);self.assertFalse(check(y))
if __name__=="__main__": unittest.main()
