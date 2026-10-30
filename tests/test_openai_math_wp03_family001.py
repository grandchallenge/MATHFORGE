"""WP03 F001: indexed-coverage absence is bounded and not an absolute non-formalization proof."""
import unittest,json,copy
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY001_MILNE_INDEXED_COVERAGE.json"
def valid(x):
 s=x.get("source_lock",{});e=x.get("indexed_evidence",{});c=x.get("coverage",{})
 return (x.get("record_type")=="GCL_OAI26_WP03_F001_INDEXED_COVERAGE_REVIEW/1" and x.get("family_id")=="001" and x.get("disposition")=="UNFORMALIZED_IN_PINNED_INDEXED_COMPARATOR_SCOPE" and s.get("commit")=="1581d4cbdd69a0faf34b2089614fe2a814316a6a" and s.get("files",{}).get("manuscript_pdf",{}).get("blob")=="3780abc1f47a23e546f28190bd3db7b24419f1f9" and x.get("manuscript",{}).get("pdf_sha256")=="640701a0ea8d8026d2f019e571e052f2d106cad3f5216cf6f7fca0d643873234" and e.get("crosswalk_rows")==200 and e.get("crosswalk_milne_hodge_rationality_hits")==0 and e.get("source_docs_001_present") is False and e.get("comparator_name_milne_hodge_rationality_specialization_hits")==0 and c.get("semantic_proposition_alignment_established") is False and c.get("remaining_pilot_families_open") is True and "NOT evidence of no Lean formalization anywhere" in x.get("claim_boundary",""))
class Review(unittest.TestCase):
 def test_pinned(self):self.assertTrue(valid(json.loads(P.read_text())))
 def test_hostile(self):
  x=json.loads(P.read_text())
  changes=[
   lambda d:d.__setitem__("disposition","FULL_SEMANTIC_MATCH_PROVED"),
   lambda d:d["source_lock"].__setitem__("commit","0"*40),
   lambda d:d["source_lock"]["files"]["manuscript_pdf"].__setitem__("blob","0"*40),
   lambda d:d["manuscript"].__setitem__("pdf_sha256","0"*64),
   lambda d:d["indexed_evidence"].__setitem__("crosswalk_rows",0),
   lambda d:d["indexed_evidence"].__setitem__("source_docs_001_present",True),
   lambda d:d["indexed_evidence"].__setitem__("comparator_name_milne_hodge_rationality_specialization_hits",1),
   lambda d:d["coverage"].__setitem__("semantic_proposition_alignment_established",True),
   lambda d:d.__setitem__("claim_boundary","There is no Lean proof anywhere"),
  ]
  for f in changes:
   y=copy.deepcopy(x);f(y);self.assertFalse(valid(y))
if __name__=="__main__":unittest.main()
