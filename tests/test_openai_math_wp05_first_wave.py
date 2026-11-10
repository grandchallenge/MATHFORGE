"""WP05 conservative first-wave ledger tests; source accounting is not certification."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026"
PIN = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
LEDGER = ROOT / "WP05_FIRST_WAVE_372_FAMILY_VERDICT_LEDGER.json"

def validate(j, index, crosswalk, risks):
    if j["record_type"] != "GCL_OAI26_WP05_FIRST_WAVE_PORTFOLIO_VERDICT_LEDGER/1":
        raise ValueError("invalid schema")
    if j["source"]["upstream_commit"] != PIN or index["upstream"]["commit"] != PIN or crosswalk["origin"]["commit"] != PIN:
        raise ValueError("stale source head")
    rows = j["rows"]
    ids = [r["family_id"] for r in rows]
    if len(rows) != 372 or len(set(ids)) != 372 or ids != [f["family_id"] for f in index["families"]]:
        raise ValueError("family coverage mismatch")
    if any([r["headline"] != f["headline"] or r["manuscripts"] != f["manuscripts"]
            for r, f in zip(rows, index["families"])]):
        raise ValueError("source manuscript drift")
    pdfs = [m["pdf_path"] for row in rows for m in row["manuscripts"]]
    if len(pdfs) != 719 or len(set(pdfs)) != 719:
        raise ValueError("PDF path coverage mismatch")
    d = j["denominators"]
    if any((d["families"] != 372, d["pdf_paths"] != 719,
            d["formalization_declarations"] != len(crosswalk["main_results"]) or d["formalization_declarations"] != 200,
            d["source_paper_records"] != len(crosswalk["source_papers"]) or d["source_paper_records"] != 173)):
        raise ValueError("denominator mismatch")
    if d["publisher_300_to_indexed_200_mapping"] != "UNRECONCILED":
        raise ValueError("publisher count promotion")
    if j["new_final_mathematical_family_verdicts"] != 0:
        raise ValueError("unsupported final verdict count")
    for row in rows:
        if row["certification"] != "NO_CERTIFICATION":
            raise ValueError("false certification")
        if row["source_provenance"]["exact_declaration_to_family_binding"] != "NOT_ESTABLISHED":
            raise ValueError("invented declaration binding")
        if row["verdict"] not in ("UNRESOLVED","INSUFFICIENT_EVIDENCE"):
            raise ValueError("unsupported semantic promotion")
        if row["comparator_replay"] != "CORPUS_200_OF_200_TECHNICAL_ONLY_NOT_ATTRIBUTED_TO_FAMILY":
            raise ValueError("technical-to-family promotion")
    if len(risks["rows"]) != 30 or len(j["withdrawn_source_exceptions"]) != 3:
        raise ValueError("withdrawn coverage mismatch")
    if any(w.get("exclusion") != "EXCLUDE_FROM_ACCEPTED_CURRENT_RESULT_COUNTS_AND_CERTIFICATION_INTAKE"
           for w in j["withdrawn_source_exceptions"]):
        raise ValueError("withdrawal promotion")
    return True

class FirstWaveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger=json.loads(LEDGER.read_text())
        cls.index=json.loads((ROOT/"MANUSCRIPT_INDEX.json").read_text())
        cls.crosswalk=json.loads((ROOT/"FORMALIZATION_CROSSWALK.json").read_text())
        cls.risks=json.loads((ROOT/"WP02_CANONICAL_3_14_13_RISK_REGISTER.json").read_text())

    def test_positive_complete_and_source_pinned(self):
        self.assertTrue(validate(self.ledger,self.index,self.crosswalk,self.risks))
        self.assertEqual(len({r["family_id"] for r in self.ledger["rows"]}),372)

    def test_no_false_certification(self):
        x=deepcopy(self.ledger);x["rows"][0]["certification"]="MATHCERT_CERTIFIED"
        with self.assertRaisesRegex(ValueError,"false certification"):validate(x,self.index,self.crosswalk,self.risks)

    def test_no_comparator_to_semantic_promotion(self):
        x=deepcopy(self.ledger);x["rows"][0]["verdict"]="VERIFIED_WITHIN_EXPLICIT_SCOPE"
        with self.assertRaisesRegex(ValueError,"unsupported semantic promotion"):validate(x,self.index,self.crosswalk,self.risks)

    def test_no_invented_family_declaration_link(self):
        x=deepcopy(self.ledger);x["rows"][0]["source_provenance"]["exact_declaration_to_family_binding"]="PROVED"
        with self.assertRaisesRegex(ValueError,"invented declaration binding"):validate(x,self.index,self.crosswalk,self.risks)

    def test_duplicate_family_rejected(self):
        x=deepcopy(self.ledger);x["rows"][1]["family_id"]=x["rows"][0]["family_id"]
        with self.assertRaisesRegex(ValueError,"family coverage mismatch"):validate(x,self.index,self.crosswalk,self.risks)

    def test_missing_pdf_rejected(self):
        x=deepcopy(self.ledger);x["rows"][0]["manuscripts"]=[]
        with self.assertRaisesRegex(ValueError,"source manuscript drift"):validate(x,self.index,self.crosswalk,self.risks)

    def test_source_revision_drift_rejected(self):
        x=deepcopy(self.ledger);x["source"]["upstream_commit"]="0"*40
        with self.assertRaisesRegex(ValueError,"stale source head"):validate(x,self.index,self.crosswalk,self.risks)

    def test_withdrawn_cannot_promote(self):
        x=deepcopy(self.ledger);x["withdrawn_source_exceptions"][0]["exclusion"]="INCLUDE_CERTIFIED"
        with self.assertRaisesRegex(ValueError,"withdrawal promotion"):validate(x,self.index,self.crosswalk,self.risks)

    def test_300_is_not_200(self):
        x=deepcopy(self.ledger);x["denominators"]["publisher_300_to_indexed_200_mapping"]="EQUIVALENT"
        with self.assertRaisesRegex(ValueError,"publisher count promotion"):validate(x,self.index,self.crosswalk,self.risks)

if __name__ == "__main__":
    unittest.main()
