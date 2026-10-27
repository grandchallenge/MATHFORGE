"""Offline hostile source-to-Lean replay harness tests; not a proof replay."""
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]/"sources"/"OPENAI-MATH-2026"
sys.path.insert(0,str(ROOT))
from replay_first25_lean import prepare_tasks,parsed_axioms,extended_budget_authorized
CW=json.loads((ROOT/"FORMALIZATION_CROSSWALK.json").read_text())
REPORT=json.loads((ROOT/"FIRST25_CONFIG_PREFLIGHT.json").read_text())
class ReplayGuards(unittest.TestCase):
 def test_first_five(self):
  x=prepare_tasks(CW,REPORT,0,5)
  self.assertEqual((len(x),x[0]["declaration"],x[-1]["declaration"]),
    (5,"OAI.AbhyankarSathaye.CommutingDerivations.commuting_derivations_with_ordinary_extras","OAI.ArtinCAT0.main"))
 def test_next25_exact_shard(self):
  report=json.loads((ROOT/"NEXT25_CONFIG_PREFLIGHT.json").read_text())
  rows=prepare_tasks(CW,report,0,5)
  self.assertEqual(len(rows),5)
  self.assertEqual(rows[0]["declaration"],"OAI.ComparatorModel.RecursivePotentials.main")
  self.assertNotIn(rows[0]["declaration"],{x["declaration"] for x in REPORT["rows"]})
 def test_invalid_ranges(self):
  for start,count in ((-1,1),(0,0),(24,2),(25,1)):
   with self.assertRaises(ValueError):prepare_tasks(CW,REPORT,start,count)
 def test_extended_budget_exact_targets_only(self):
  for offset,start in ((0,2),(25,18),(25,22)):
   self.assertTrue(extended_budget_authorized(offset,start,1))
   self.assertFalse(extended_budget_authorized(offset,start,2))
  for offset,start in ((0,1),(0,3),(25,17),(25,19),(25,21),(25,23)):
   self.assertFalse(extended_budget_authorized(offset,start,1))
 def test_sorry(self):
  self.assertEqual(parsed_axioms("'T' depends on axioms: [Classical.choice, sorryAx]"),(None,"UNAPPROVED_SORRY_AXIOM"))
 def test_whitelist_observation(self):
  self.assertEqual(parsed_axioms("'T' depends on axioms: [Classical.choice, propext]"),(["Classical.choice","propext"],None))
 def test_no_axioms(self):
  self.assertEqual(parsed_axioms("'T' does not depend on any axioms"),([],None))
 def test_unknown_axioms(self):
  self.assertEqual(parsed_axioms("strange format"),(None,"AXIOM_OUTPUT_NOT_PARSEABLE"))
if __name__=="__main__":unittest.main()
