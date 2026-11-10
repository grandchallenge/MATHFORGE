"""OAI26 WP04 first-wave adversarial record controls: not proof certification."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
SRC = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
WAVE = ROOT / "WP04_FIRST_WAVE_12_CASE_CRITICAL_GUARDS.json"
BASELINE = ROOT / "WP04_DETERMINISTIC_RANDOM_BASELINE_3.json"


def blob_sha1(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def verify(wave, baseline, index):
    if wave["record_type"] != "GCL_OAI26_WP04_ADVERSARIAL_FIRST_WAVE_LOGIC_GUARDS/1":
        raise ValueError("wave schema")
    if wave["source"]["upstream_commit"] != SRC or baseline["source"]["upstream_commit"] != SRC:
        raise ValueError("source drift")
    rows = wave["rows"]
    ids = [x["family_id"] for x in rows]
    if ids != [str(n).zfill(3) for n in range(1,13)]:
        raise ValueError("twelve case coverage")
    if wave["selection"]["count"] != 12:
        raise ValueError("case count")
    if wave["selection"]["strata_overlap"]["unfamiliar_domain"] != ["001","004","011"]:
        raise ValueError("domain critic stratum")
    if wave["selection"]["random_baseline_path"] != "sources/OPENAI-MATH-2026/WP04_DETERMINISTIC_RANDOM_BASELINE_3.json":
        raise ValueError("random sample binding")
    if not wave["boundaries"]["mathematical_review_not_completed"] or not wave["boundaries"]["primary_paper_proof_body_not_independently_checked"]:
        raise ValueError("misrepresented mathematical review")
    if wave["boundaries"]["mATHCERT_certification"] is not False:
        raise ValueError("false certification")
    for row in rows:
        if not row["critical_inference_test"] or not row["hostile_mutation_rejection"] or not row["remaining_mathematical_obligation"]:
            raise ValueError("empty critical test")
        if row["independent_authenticated_person"] is not False or row["certification"] != "NO_CERTIFICATION":
            raise ValueError("false independent or certification authority")
        if row["independent_primary_proof_body_review"] != "NOT_COMPLETED":
            raise ValueError("fabricated primary proof review")
        p = Path(__file__).resolve().parents[1] / row["source_file"]
        if not p.is_file() or blob_sha1(p.read_bytes()) != row["source_file_git_blob"]:
            raise ValueError("protected source drift")
        case=json.loads(p.read_text())
        if case["disposition"] != row["source_review_disposition"]:
            raise ValueError("source disposition drift")
    if len(baseline["rows"]) != 3 or len({r["family_id"] for r in baseline["rows"]}) != 3:
        raise ValueError("baseline sample coverage")
    candidates=[]
    for family in index["families"]:
        if int(family["family_id"])<=12:
            continue
        x=(0x1581d4cb ^ int(family["family_id"])) & 0xffffffff
        x^=(x<<13)&0xffffffff
        x^=x>>17
        x^=(x<<5)&0xffffffff
        candidates.append((x&0xffffffff,family["family_id"],family))
    expected=sorted(candidates,key=lambda x:(x[0],x[1]))[:3]
    if [r["family_id"] for r in baseline["rows"]] != [f["family_id"] for _,_,f in expected]:
        raise ValueError("random sample identity")
    for row,(score,_,family) in zip(baseline["rows"],expected):
        if row["score_uint32"]!=score or row["manuscript_paths"] != [m["pdf_path"] for m in family["manuscripts"]]:
            raise ValueError("random source identity")
        if row["status"] != "SOURCE_SAMPLED_PRIMARY_PROOF_NOT_REVIEWED" or row["critic_verdict"]!="NOT_ADJUDICATED":
            raise ValueError("random case false adjudication")
        if row["certification"]!="NO_CERTIFICATION":
            raise ValueError("false random certification")
    if any(x["family_id"] in ids for x in baseline["rows"]):
        raise ValueError("random pilot overlap")
    return True


class WP04FirstWave(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wave=json.loads(WAVE.read_text())
        cls.baseline=json.loads(BASELINE.read_text())
        cls.index=json.loads((ROOT/"MANUSCRIPT_INDEX.json").read_text())

    def test_complete_source_bound_first_wave(self):
        self.assertTrue(verify(self.wave,self.baseline,self.index))

    def reject_wave(self,change,reason):
        x=deepcopy(self.wave);change(x)
        with self.assertRaisesRegex(ValueError,reason):verify(x,self.baseline,self.index)

    def reject_baseline(self,change,reason):
        x=deepcopy(self.baseline);change(x)
        with self.assertRaisesRegex(ValueError,reason):verify(self.wave,x,self.index)

    def test_missing_case(self):
        self.reject_wave(lambda x:x["rows"].pop(),"twelve case coverage")

    def test_duplicate_case(self):
        self.reject_wave(lambda x:x["rows"][1].update(family_id="001"),"twelve case coverage")

    def test_source_blob_drift(self):
        self.reject_wave(lambda x:x["rows"][0].update(source_file_git_blob="0"*40),"protected source drift")

    def test_false_independence(self):
        self.reject_wave(lambda x:x["rows"][0].update(independent_authenticated_person=True),"false independent")

    def test_false_certification(self):
        self.reject_wave(lambda x:x["rows"][0].update(certification="MATHCERT_CERTIFIED"),"false independent")

    def test_false_mathematical_review(self):
        self.reject_wave(lambda x:x["boundaries"].update(primary_paper_proof_body_not_independently_checked=False),"misrepresented mathematical review")

    def test_critical_question_missing(self):
        self.reject_wave(lambda x:x["rows"][10].update(critical_inference_test=""),"empty critical test")

    def test_random_selection_changed(self):
        self.reject_baseline(lambda x:x["rows"][0].update(family_id="111"),"random sample identity")

    def test_random_cannot_be_preapproved(self):
        self.reject_baseline(lambda x:x["rows"][0].update(critic_verdict="ACCEPTED"),"random case false adjudication")

    def test_random_edition_drift(self):
        self.reject_baseline(lambda x:x["rows"][0]["manuscript_paths"].clear(),"random source identity")

if __name__=="__main__":
    unittest.main()
