import copy,json,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY011_ACTUAL_UNINDEXED_FIBER_DECLARATION.json"
def valid(d):
 x=d.get("exact_comparison",{});u=d.get("upstream",{});c=d.get("coverage",{})
 return (d.get("record_type")=="OAI26_WP03_F011_UNINDEXED_ACTUAL_DECLARATION/1" and d.get("disposition")=="PARTIAL_FORMAL_SUPPORT_FIBER_LEMMAS_MAIN_EXPONENT_GAP" and d.get("source_commit")=="1581d4cbdd69a0faf34b2089614fe2a814316a6a" and u.get("blob")=="217cfe4d7f9c39981eabe9bbeeb8458febb0fc76" and "totient_large_fibers_of_one_le" in " ".join(u.get("lean_declarations",[])) and "1<=epsilon" in x.get("lean_exponent_theorem","") and "0<epsilon<1" in x.get("gap","") and c.get("unindexed_main_concept_found") is True and c.get("source_main_theorem_matched") is False and c.get("full_family011_proved") is False and c.get("all_WP03_certified") is False)
class Review(unittest.TestCase):
 def test_positive(self):self.assertTrue(valid(json.loads(P.read_text())))
 def test_hostile(self):
  d=json.loads(P.read_text())
  for f in [lambda z:z.__setitem__("disposition","FULL_THEOREM_PROVED"),lambda z:z["upstream"].__setitem__("blob","0"*40),lambda z:z["exact_comparison"].__setitem__("lean_exponent_theorem","all epsilon"),lambda z:z["exact_comparison"].__setitem__("gap","none"),lambda z:z["coverage"].__setitem__("source_main_theorem_matched",True),lambda z:z["coverage"].__setitem__("all_WP03_certified",True)]:
   z=copy.deepcopy(d);f(z);self.assertFalse(valid(z))
if __name__=="__main__":unittest.main()
