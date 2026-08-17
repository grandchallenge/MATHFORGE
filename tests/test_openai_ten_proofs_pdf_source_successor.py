import copy
import json
import unittest
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/pdf_source_successors/OTP-SOURCE-PDF-SUCCESSOR-002.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_pdf_source_successor.schema.json"


class TestPdfSourceSuccessor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = json.loads(RECORD.read_text(encoding="utf-8"))
        cls.schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    def rejects(self, mutate):
        candidate = copy.deepcopy(self.record)
        mutate(candidate)
        with self.assertRaises((jsonschema.ValidationError, AssertionError)):
            jsonschema.Draft202012Validator(self.schema).validate(candidate)

    def test_canonical_record_valid(self):
        jsonschema.Draft202012Validator(self.schema).validate(self.record)

    def test_reject_predecessor_rewrite(self):
        self.rejects(lambda r: r["predecessor"].__setitem__("sha256", r["current_source"]["sha256"]))

    def test_reject_current_digest_drift(self):
        self.rejects(lambda r: r["current_source"].__setitem__("sha256", "0" * 64))

    def test_reject_length_drift(self):
        self.rejects(lambda r: r["current_source"].__setitem__("byte_length", 1))

    def test_reject_url_substitution(self):
        self.rejects(lambda r: r["current_source"].__setitem__("url", "https://example.com/paper.pdf"))

    def test_reject_page_count_drift(self):
        self.rejects(lambda r: r["current_source"].__setitem__("page_count", 252))

    def test_reject_hidden_family_addition(self):
        self.rejects(lambda r: r["family_loci"].append({"family":"OTP-F-EHRHART","chapter":8,"primary_loci":["Theorem 1.1"]}))

    def test_reject_family_removal(self):
        self.rejects(lambda r: r["family_loci"].pop())

    def test_reject_semantic_promotion(self):
        self.rejects(lambda r: r["authority_effect"].__setitem__("family_semantic_clearance", True))

    def test_reject_solve_promotion(self):
        self.rejects(lambda r: r["authority_effect"].__setitem__("solve_authority", True))

    def test_reject_cert_promotion(self):
        self.rejects(lambda r: r["authority_effect"].__setitem__("cert_authority", True))

    def test_reject_whole_document_equivalence(self):
        self.rejects(lambda r: r["authority_effect"].__setitem__("whole_document_equivalence", True))

    def test_reject_aggregate_authority(self):
        self.rejects(lambda r: r["authority_effect"].__setitem__("aggregate_authority", True))


if __name__ == "__main__":
    unittest.main()
