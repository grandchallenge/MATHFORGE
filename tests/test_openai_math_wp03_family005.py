"""Family 005: source-bound manuscript-to-Lean proposition, not certification."""
import copy
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
LEDGER = ROOT / "WP03_FAMILY005_CATALAN_SEMANTIC_REVIEW.json"
INDEX = ROOT / "MANUSCRIPT_INDEX.json"
CROSSWALK = ROOT / "FORMALIZATION_CROSSWALK.json"
PIN = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
THEOREM = "OAI.InternalCatalan.catalan_irrational"
STATEMENT = "Irrational (∑' j : ℕ, (-1 : ℝ) ^ j / ((2 * j + 1 : ℕ) : ℝ) ^ 2)"

def valid(d, index, formal):
    if d.get("record_type") != "GCL_OAI26_WP03_F005_SOURCE_SEMANTIC_REVIEW/1":
        return False
    if d.get("disposition") != "PROPOSITION_LEVEL_ALIGNMENT" or d.get("family_id") != "005":
        return False
    lock = d.get("source_lock", {})
    if lock.get("commit") != PIN or lock.get("repository") != "openai/math":
        return False
    if lock.get("pinned_lean_toolchain") != "leanprover/lean4:v4.34.1":
        return False
    files = lock.get("files", {})
    if len(files) != 9 or any(len(x.get("sha1", "")) != 40 for x in files.values()):
        return False
    if files["lean_proof"]["sha1"] != "a21cbc0e56a4e71ec21ce765b16e6ef0adb864f0":
        return False
    if files["lean_challenge"]["sha1"] != "f7941ef960ec9d0ec745f15f2ee7b2ff46bd6058":
        return False
    if files["comparator_config"]["sha1"] != "78b89138b45ecbe09c061b25c2e2f6177ffd4b9b":
        return False
    man = d.get("manuscript", {})
    if man.get("pdf_sha256") != "4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e":
        return False
    if man.get("pdf_pages") != 44 or man.get("main_theorem", {}).get("label") != "Theorem 1.1":
        return False
    if man["main_theorem"]["additional_hypotheses"] != []:
        return False
    if man["main_theorem"]["pdf_page"] != 1 or man["proof_location"]["pdf_page"] != 42:
        return False
    f = d.get("formalization", {})
    if f.get("theorem") != THEOREM or f.get("theorem_statement") != STATEMENT:
        return False
    if f.get("comparator_config_theorem_names") != [THEOREM]:
        return False
    if f.get("challenge_module") != "ComparatorChallenges.Catalan":
        return False
    if f.get("proof_file_contains_sorry") is not False or f.get("challenge_file_contains_placeholder_sorry") is not True:
        return False
    if f.get("exact_declaration_text_matches_challenge") is not True or f.get("additional_hypotheses") != []:
        return False
    if f.get("comparator_executed_in_this_work_package") is not False:
        return False
    if f.get("import_axiom_closure_independently_replayed") is not False:
        return False
    c = d.get("crosswalk", {})
    if c.get("inside_200_main_results") is not False or c.get("in_family_index_372") is not True:
        return False
    if len(formal.get("main_results", [])) != 200:
        return False
    if any("catalan" in json.dumps(x, ensure_ascii=False).lower() for x in formal["main_results"]):
        return False
    fam = [x for x in index["families"] if x["family_id"] == "005"]
    if len(fam) != 1 or len(fam[0]["manuscripts"]) != 1:
        return False
    if fam[0]["manuscripts"][0]["pdf_path"] != files["manuscript_pdf"]["path"]:
        return False
    if d.get("critic_review", {}).get("separate_authenticated_person") is not False:
        return False
    if d["coverage"]["reviewed_this_transaction"] != ["005"] or d["coverage"]["other_families_not_adjudicated"] is not True:
        return False
    if "NOT full semantic-equivalence proof" not in d["claim_boundary"]:
        return False
    return True

class Family005Review(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = json.loads(LEDGER.read_text())
        cls.index = json.loads(INDEX.read_text())
        cls.formal = json.loads(CROSSWALK.read_text())

    def test_source_bound_positive(self):
        self.assertTrue(valid(self.d, self.index, self.formal))

    def test_hostile_claims_fail(self):
        changes = [
            ("wrong proposition", lambda d: d["formalization"].__setitem__("theorem_statement", STATEMENT.replace(" ^ 2)", " ^ 3)"))),
            ("wrong source commit", lambda d: d["source_lock"].__setitem__("commit", "0" * 40)),
            ("incorrect theorem", lambda d: d["formalization"].__setitem__("theorem", "OAI.Forged")),
            ("fake comparator success", lambda d: d["formalization"].__setitem__("comparator_executed_in_this_work_package", True)),
            ("hidden axiom claim", lambda d: d["formalization"].__setitem__("import_axiom_closure_independently_replayed", True)),
            ("swapped proof blob", lambda d: d["source_lock"]["files"]["lean_proof"].__setitem__("sha1", "0" * 40)),
            ("incorrect document page", lambda d: d["manuscript"]["main_theorem"].__setitem__("pdf_page", 2)),
            ("unearned complete pilot", lambda d: d["coverage"].__setitem__("other_families_not_adjudicated", False)),
            ("unearned source classification", lambda d: d["crosswalk"].__setitem__("inside_200_main_results", True)),
            ("unearned fully equivalent", lambda d: d.__setitem__("disposition", "FULL_SEMANTIC_MATCH_PROVED"))
        ]
        for label, change in changes:
            with self.subTest(label=label):
                x = copy.deepcopy(self.d)
                change(x)
                self.assertFalse(valid(x, self.index, self.formal))

if __name__ == "__main__":
    unittest.main()
