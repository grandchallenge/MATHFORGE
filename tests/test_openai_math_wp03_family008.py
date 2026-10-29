"""WP03 family 008 pinned principal-theorem statement review. No certification."""
import copy
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
LEDGER = ROOT / "WP03_FAMILY008_DELIGNE_DRINFELD_SEMANTIC_REVIEW.json"
INDEX = ROOT / "MANUSCRIPT_INDEX.json"
FORMAL = ROOT / "FORMALIZATION_CROSSWALK.json"
LEAN_EVIDENCE = ROOT / "CORPUS_25_89_LEAN_RECEIPT_LEDGER.json"
PIN = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
THEOREM = "OAI.DeligneDrinfeld.main"

def accepted(d, manuscripts, crosswalk, replay):
    if d.get("record_type") != "GCL_OAI26_WP03_F008_SOURCE_SEMANTIC_REVIEW/1":
        return False
    if d.get("disposition") != "PROPOSITION_LEVEL_ALIGNMENT" or d.get("family_id") != "008":
        return False
    src = d.get("source_lock", {})
    if src.get("commit") != PIN or src.get("repository") != "openai/math":
        return False
    if src.get("toolchain") != "leanprover/lean4:v4.34.1":
        return False
    blobs = src.get("files", {})
    if len(blobs) != 9 or any(len(v.get("blob", "")) != 40 for v in blobs.values()):
        return False
    required = {
        "lean_foundations": "04320b5982c12c9d638b6f7119f6e83c69ca6c13",
        "lean_solution": "98a996a90f4f57a205a3e3e8673a8528e8e3dbbf",
        "lean_challenge": "35b7ac31d724c1b5383d30513443ecabda05e53c",
        "comparator_config": "479c2ef4d2352da81193e5ff8248f2cf86f484d7",
        "manuscript_pdf": "0aa3328661d35567ec7e2dfb802b0351003e7a31",
    }
    if any(blobs.get(k, {}).get("blob") != v for k,v in required.items()):
        return False
    man=d.get("manuscript",{})
    if man.get("pdf_sha256")!="5ae63f326803a634e7c6dc5684ce7062ea0ac6940a88a75c7052875382dbc762":
        return False
    if man.get("pdf_pages")!=41 or man.get("pdf_bytes")!=539601:
        return False
    if man.get("main_result",{}).get("number")!="Theorem 1.1" or man["main_result"].get("pdf_page")!=2:
        return False
    if man["main_result"].get("extra_hypotheses") != [] or man["proof"]["pdf_page"]!=40:
        return False
    if len(man.get("formalization_scope_exclusions",[])) < 2:
        return False
    lean=d.get("lean",{})
    if lean.get("index_zero_based")!=38 or lean.get("declaration")!=THEOREM:
        return False
    if lean.get("challenge_module")!="ComparatorChallenges.DeligneDrinfeld" or lean.get("comparator_config_theorem_names")!=[THEOREM]:
        return False
    if lean.get("source_challenge_normalized_identity")!={"IsSolution":True,"MainStatement":True,"oddWeight":True,"Graded":True}:
        return False
    if lean.get("odd_weights")!="oddWeight k = 2*k+3 (k : ℕ), corresponding to manuscript 3,5,7,...":
        return False
    if lean.get("comparator_executed_in_review") is not False or lean.get("manuscript_definition_bridge_independently_proved") is not False:
        return False
    if lean.get("challenge_placeholder_sorry") is not True:
        return False
    features=lean.get("main_statement_features",[])
    if len(features)!=6 or not any("Continuity" in x for x in features) or not any("Ihara" in x for x in features):
        return False
    family=[x for x in manuscripts.get("families",[]) if x.get("family_id")=="008"]
    if len(family)!=1 or len(family[0]["manuscripts"])!=1:
        return False
    if family[0]["manuscripts"][0]["pdf_path"]!=blobs["manuscript_pdf"]["path"]:
        return False
    formal_rows=[x for x in crosswalk["main_results"] if x["declaration"]==THEOREM]
    if len(formal_rows)!=1 or formal_rows[0]["comparator_config"]!=blobs["comparator_config"]["path"]:
        return False
    corpus=[x for x in replay["rows"] if x.get("index_zero_based")==38]
    if len(corpus)!=1 or corpus[0]["declaration"]!=THEOREM:
        return False
    old=d.get("prior_separate_wp01_lean_evidence",{})
    if old.get("ledger_blob")!="530e9a65b37345957f29049b5b24353f0fe8887d" or old.get("index")!=38:
        return False
    if old.get("run_id")!=corpus[0]["run_id"] or old.get("run_id")!=40490625900:
        return False
    if corpus[0].get("solution_git_blob")!=blobs["lean_solution"]["blob"]:
        return False
    if corpus[0].get("comparator_git_blob")!=blobs["comparator_config"]["blob"]:
        return False
    if (old.get("build_exit"),old.get("axioms_exit"))!=(0,0) or old.get("extra_axioms")!=[]:
        return False
    if old.get("comparator_executed") is not False or corpus[0].get("comparator_executed") is not False:
        return False
    if d.get("critic_review",{}).get("separate_authenticated_identity") is not False:
        return False
    if d.get("coverage",{}).get("reviewed_this_transaction") != ["008"] or d["coverage"].get("remaining_pilot_not_adjudicated") is not True:
        return False
    if "neither full definition/model-bridge equivalence" not in d.get("claim_boundary",""):
        return False
    return True

class Family008Review(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc=json.loads(LEDGER.read_text())
        cls.man=json.loads(INDEX.read_text())
        cls.formal=json.loads(FORMAL.read_text())
        cls.replay=json.loads(LEAN_EVIDENCE.read_text())
    def test_source_bound(self):
        self.assertTrue(accepted(self.doc,self.man,self.formal,self.replay))
    def test_hostile_controls(self):
        mutations=[
            ("wrong source",lambda d:d["source_lock"].__setitem__("commit","0"*40)),
            ("wrong paper",lambda d:d["manuscript"].__setitem__("pdf_sha256","0"*64)),
            ("wrong theorem",lambda d:d["lean"].__setitem__("declaration","OAI.Forged.main")),
            ("pentagon removed",lambda d:d["lean"]["source_challenge_normalized_identity"].__setitem__("IsSolution",False)),
            ("odd weights changed",lambda d:d["lean"].__setitem__("odd_weights","oddWeight k = 2*k+1")),
            ("completion omitted",lambda d:d["lean"].__setitem__("main_statement_features",["graded","Ihara"])),
            ("comparator fabricated",lambda d:d["lean"].__setitem__("comparator_executed_in_review",True)),
            ("full bridge fabricated",lambda d:d["lean"].__setitem__("manuscript_definition_bridge_independently_proved",True)),
            ("crosswalk index drift",lambda d:d["prior_separate_wp01_lean_evidence"].__setitem__("index",39)),
            ("false certification",lambda d:d.__setitem__("disposition","FULL_SEMANTIC_MATCH_PROVED")),
            ("false pilot",lambda d:d["coverage"].__setitem__("remaining_pilot_not_adjudicated",False)),
        ]
        for name,change in mutations:
            with self.subTest(name=name):
                bad=copy.deepcopy(self.doc)
                change(bad)
                self.assertFalse(accepted(bad,self.man,self.formal,self.replay))

if __name__=="__main__":
    unittest.main()
