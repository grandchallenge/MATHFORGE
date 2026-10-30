import copy,json,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"sources/OPENAI-MATH-2026/WP03_FAMILY011_NEIGHBOR_DECLARATION_DISAMBIGUATION.json"
def valid(d):
 t=d.get("targets",[]);b=d.get("boundaries",{})
 return (d.get("record_type")=="OAI26_WP03_F011_NEIGHBOR_DECLARATION_DISAMBIGUATION/1" and d.get("source_commit")=="1581d4cbdd69a0faf34b2089614fe2a814316a6a" and d.get("disposition")=="FOUR_NEARBY_COMPARATOR_NAMES_NOT_PROPOSITION_MATCHES" and [x.get("config") for x in t]==["TotientAsymptotic","TotientCompanionZero","SmoothObstruction","SmoothInitialForm"] and [x.get("implementation_blob") for x in t]==["60225f2c27398c81d0f330b12ff88393cdf63cc5","2f3f673b65f9bb058cccb8a4a24e50bb619d2696","14ebe0aebe09a2b10090df619308c58e7848e095","a17d2687a4fc11ea1a470e2c2a390e2977642f48"] and b.get("not_proof_of_no_unindexed_declaration") is True and b.get("full_semantic_match") is False and b.get("certification") is False and b.get("WP03_complete") is False)
class Review(unittest.TestCase):
 def test_positive(self):self.assertTrue(valid(json.loads(P.read_text())))
 def test_hostile(self):
  d=json.loads(P.read_text())
  for f in [lambda x:x.__setitem__("disposition","MATCHED"),lambda x:x.__setitem__("source_commit","0"*40),lambda x:x["targets"].pop(),lambda x:x["targets"][0].__setitem__("implementation_blob","0"*40),lambda x:x["boundaries"].__setitem__("not_proof_of_no_unindexed_declaration",False),lambda x:x["boundaries"].__setitem__("full_semantic_match",True),lambda x:x["boundaries"].__setitem__("certification",True),lambda x:x["boundaries"].__setitem__("WP03_complete",True)]:
   z=copy.deepcopy(d);f(z);self.assertFalse(valid(z))
if __name__=="__main__":unittest.main()
