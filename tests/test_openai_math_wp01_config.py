"""Source-only WP01 pinned config fixtures, no Lean execution or theorem certification."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]/"sources"/"OPENAI-MATH-2026"
spec=importlib.util.spec_from_file_location("wp01_source",ROOT/"replay_first25_sources.py")
audit=importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)

class PinnedFirstShardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cw=json.loads((ROOT/"FORMALIZATION_CROSSWALK.json").read_text())
        cls.report=json.loads((ROOT/"FIRST25_CONFIG_PREFLIGHT.json").read_text())

    def test_source_evidence_and_exact_order(self):
        self.assertTrue(audit.check_report(self.cw,self.report))
        self.assertEqual(len(self.report["rows"]),25)
        self.assertEqual(sum(x["config_includes_decl"] for x in self.report["rows"]),25)
        self.assertEqual(sum(x["source_contains_unqualified_name"] for x in self.report["rows"]),25)
        self.assertEqual(self.report["scope"],"SOURCE_FILES_AND_CONFIG_ONLY_NOT_LEAN_REPLAY")

    def test_utf8_order_not_locale_order(self):
        declarations={x["declaration"] for x in self.report["rows"]}
        self.assertIn("OAI.CPTSeparation.main",declarations)
        self.assertIn("OAI.ComparatorModel.CurrentMain.main",declarations)
        self.assertNotIn("OAI.binary_sweep_contraction_and_mixing",declarations)
        self.assertNotIn("OAI.common_bases_fpras",declarations)

    def test_injected_false_positive_config_rejected(self):
        x=deepcopy(self.report)
        x["rows"][0]["config_includes_decl"]=False
        with self.assertRaisesRegex(ValueError,"not witnessed"):
            audit.check_report(self.cw,x)

    def test_declaration_config_substitution_rejected(self):
        x=deepcopy(self.report)
        x["rows"][0]["config_theorems"]=["OAI.Invented.fake"]
        with self.assertRaisesRegex(ValueError,"does not list"):
            audit.check_report(self.cw,x)

    def test_source_identity_tampering_rejected(self):
        x=deepcopy(self.report)
        x["rows"][0]["source_blob"]="bad"
        with self.assertRaisesRegex(ValueError,"invalid pinned"):
            audit.check_report(self.cw,x)

    def test_formal_claim_promotion_rejected(self):
        x=deepcopy(self.report)
        x["scope"]="LEAN_REPLAY_PASS"
        with self.assertRaisesRegex(ValueError,"falsely promoted"):
            audit.check_report(self.cw,x)

    def test_wrong_shard_rejected(self):
        x=deepcopy(self.report)
        x["rows"][0],x["rows"][1]=x["rows"][1],x["rows"][0]
        with self.assertRaisesRegex(ValueError,"UTF-8 shard"):
            audit.check_report(self.cw,x)

if __name__=="__main__":unittest.main()
