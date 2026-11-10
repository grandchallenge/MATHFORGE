"""WP04 source-locked twelve-case critical review controls; not theorem certification."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

P=Path(__file__).resolve().parents[1]/"sources"/"OPENAI-MATH-2026"
F=P/"WP04_FIRST_WAVE_12_ADVERSARIAL_SCOPE_REVIEW.json"
PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
STRATA={"REVISION_DEPENDENCY":3,"FORMAL_MATCH":3,"UNFAMILIAR_DOMAIN":3,"RANDOM_BASELINE":3}

def validate(d):
    if d["record_type"]!="GCL_OAI26_WP04_ADVERSARIAL_FIRST_WAVE_12/1" or d["source_lock"]["commit"]!=PIN:
        raise ValueError("source identity drift")
    rows=d["rows"];ids=[r["family_id"] for r in rows]
    if len(rows)!=12 or len(set(ids))!=12 or set(ids)!={"001","002","003","004","005","006","008","009","010","011","012","342"}:
        raise ValueError("twelve-case identity drift")
    if {s:sum(r["selection_stratum"]==s for r in rows) for s in STRATA}!=STRATA or d["selection_counts"]!=STRATA:
        raise ValueError("stratum coverage")
    if d["new_mathematical_refutations"]!=0 or d["new_certifications"]!=0:
        raise ValueError("unearned mathematical result")
    if d["review_provenance"]["independent_authentication"] is not False:
        raise ValueError("false independent identity")
    if d["review_provenance"]["source_scope"]!="TWELVE_PROTECTED_WP02_WP03_EVIDENCE_RECORDS_NOT_FRESH_PRIMARY_PAPERS":
        raise ValueError("false primary source scope")
    for r in rows:
        if r["source_evidence"]["upstream_commit"]!=PIN or not r["source_evidence"]["git_blob_sha1"]:
            raise ValueError("unbound source")
        if not r["source_evidence"]["path"].startswith("sources/OPENAI-MATH-2026/WP0"):
            raise ValueError("invalid source path")
        if r["certification"]!="NO_CERTIFICATION" or r["counterexample_proved_in_this_pass"] is not False:
            raise ValueError("unsupported certification or counterexample")
        if r["requires_fresh_primary_proof_review"] is not True or r["independently_authenticated"] is not False:
            raise ValueError("critical review boundary")
        if r["evidence_strength"]!="PREDECESSOR_PROTECTED_RECORD_AND_LOGICAL_SCOPE_CRITIC_ONLY":
            raise ValueError("evidence inflation")
    gap=next(r for r in rows if r["family_id"]=="011")
    if gap["review_disposition"]!="PARTIAL_SCOPE_COUNTERWITNESS" or "epsilon" not in gap["mathematical_adversarial_question"]:
        raise ValueError("epsilon hostile semantic mutation")
    cone=next(r for r in rows if r["family_id"]=="342")
    if cone["review_disposition"]!="VERSION_HYPOTHESIS_MISMATCH":
        raise ValueError("withdrawn edition guard")
    if d["hostile_fixture"]["expected_verdict"]!="REJECT_UNSUPPORTED_SCOPE_PROMOTION":
        raise ValueError("hostile fixture guard")
    return True

class TestWP04FirstWave(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.doc=json.loads(F.read_text())
    def test_exact_original(self):self.assertTrue(validate(self.doc))
    def reject(self,fn,why):
        x=deepcopy(self.doc);fn(x)
        with self.assertRaisesRegex(ValueError,why):validate(x)
    def test_duplicate(self):self.reject(lambda x:x["rows"][0].update(family_id="001"),"twelve-case")
    def test_missing_case(self):self.reject(lambda x:x["rows"].pop(),"twelve-case")
    def test_inflated_authentication(self):self.reject(lambda x:x["review_provenance"].update(independent_authentication=True),"false independent")
    def test_false_primary_proof_scope(self):self.reject(lambda x:x["review_provenance"].update(source_scope="FULL_PRIMARY_PAPER_PROOFS"),"false primary")
    def test_fabricated_certification(self):self.reject(lambda x:x["rows"][0].update(certification="MATHCERT_CERTIFIED"),"unsupported certification")
    def test_fabricated_counterexample(self):self.reject(lambda x:x["rows"][0].update(counterexample_proved_in_this_pass=True),"unsupported certification")
    def test_epsilon_hostile(self):self.reject(lambda x:next(r for r in x["rows"] if r["family_id"]=="011").update(review_disposition="FULL_SEMANTIC_MATCH_PROVED"),"epsilon hostile")
    def test_cone_version(self):self.reject(lambda x:next(r for r in x["rows"] if r["family_id"]=="342").update(review_disposition="FULL_SEMANTIC_MATCH_PROVED"),"withdrawn edition")
    def test_stratum_inflation(self):self.reject(lambda x:x["rows"][0].update(selection_stratum="RANDOM_BASELINE"),"stratum coverage")
    def test_source_pin(self):self.reject(lambda x:x["source_lock"].update(commit="0"*40),"source identity")
    def test_fake_refutations(self):self.reject(lambda x:x.update(new_mathematical_refutations=1),"unearned mathematical")

if __name__=="__main__":unittest.main()
