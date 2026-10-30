import json, copy, unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY004_H10Q_INDEXED_COVERAGE.json"
def valid(d):
 s=d.get("source",{});i=d.get("index",{});c=d.get("coverage",{})
 return (d.get("record_type")=="GCL_OAI26_WP03_F004_INDEXED_REVIEW/1" and d.get("disposition")=="UNFORMALIZED_IN_PINNED_INDEXED_COMPARATOR_SCOPE" and s.get("commit")=="1581d4cbdd69a0faf34b2089614fe2a814316a6a" and len(s.get("manuscripts",[]))==2 and s["manuscripts"][0].get("intro_git_blob")=="693a8ab0c2c42e664b50992e6cf605177125a7ad" and s["manuscripts"][1].get("main_tex_git_blob")=="8b71e1d9df391376eba07b86698bf8814b54af2c" and i.get("main_result_count")==200 and i.get("matching_named_h10q_rows")==0 and i.get("lean_docs_004_present") is False and i.get("named_h10q_comparator_hits")==0 and c.get("semantic_equivalence_proved") is False and c.get("pilot_complete") is False and "does not establish no theorem" in d.get("scope",""))
class F004(unittest.TestCase):
 def test_positive(self):self.assertTrue(valid(json.loads(P.read_text())))
 def test_hostile(self):
  d=json.loads(P.read_text());f=[
   lambda x:x.__setitem__("disposition","FULL_SEMANTIC_MATCH_PROVED"),
   lambda x:x["source"].__setitem__("commit","0"*40),
   lambda x:x["source"]["manuscripts"].pop(),
   lambda x:x["source"]["manuscripts"][0].__setitem__("intro_git_blob","0"*40),
   lambda x:x["index"].__setitem__("lean_docs_004_present",True),
   lambda x:x["index"].__setitem__("matching_named_h10q_rows",1),
   lambda x:x["coverage"].__setitem__("semantic_equivalence_proved",True),
   lambda x:x["coverage"].__setitem__("pilot_complete",True)]
  for fn in f:
   a=copy.deepcopy(d);fn(a);self.assertFalse(valid(a))
if __name__=="__main__":unittest.main()
