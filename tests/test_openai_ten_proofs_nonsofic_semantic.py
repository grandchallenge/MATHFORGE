from __future__ import annotations
import copy, importlib.util, json, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MODULE=ROOT / "ci/validate_openai_ten_proofs_nonsofic_semantic.py"
spec=importlib.util.spec_from_file_location("otp_d_nonsofic_validator",MODULE)
validator=importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)
RECORD=json.loads(validator.RECORD.read_text(encoding="utf-8"))
SCHEMA=json.loads(validator.SCHEMA.read_text(encoding="utf-8"))

class NonSoficSemanticAuditTests(unittest.TestCase):
    def test_exact_record_validates(self):
        self.assertEqual([],validator.validation_errors(copy.deepcopy(RECORD),copy.deepcopy(SCHEMA)))
    def test_target_mutation_fails_closed(self):
        r=copy.deepcopy(RECORD); r["formal_authority"]["targets"][0]="wrong.target"
        self.assertTrue(validator.validation_errors(r,copy.deepcopy(SCHEMA)))
    def test_sofic_convention_mutation_fails_closed(self):
        r=copy.deepcopy(RECORD); r["definition_concordance"]["sofic_convention"]="different metric"
        self.assertTrue(validator.validation_errors(r,copy.deepcopy(SCHEMA)))
    def test_finite_presentation_mutation_fails_closed(self):
        r=copy.deepcopy(RECORD); r["definition_concordance"]["finite_presentation"]="finitely generated only"
        self.assertTrue(validator.validation_errors(r,copy.deepcopy(SCHEMA)))
    def test_source_consequence_inflation_fails_closed(self):
        r=copy.deepcopy(RECORD); r["anti_overclaim"]["finitely_presented_conclusion_claimed_source_verbatim"]=True
        self.assertTrue(validator.validation_errors(r,copy.deepcopy(SCHEMA)))
    def test_proof_dependency_mutation_fails_closed(self):
        r=copy.deepcopy(RECORD); r["proof_path_evidence"]=["unrelated theorem"]*8
        self.assertTrue(validator.validation_errors(r,copy.deepcopy(SCHEMA)))
    def test_replay_mutation_fails_closed(self):
        r=copy.deepcopy(RECORD); r["formal_authority"]["replay"]["job_id"]=0
        self.assertTrue(validator.validation_errors(r,copy.deepcopy(SCHEMA)))
    def test_downstream_authority_inflation_fails_closed(self):
        r=copy.deepcopy(RECORD); r["route_controls"]["mathcert_route_authorized"]=True
        self.assertTrue(validator.validation_errors(r,copy.deepcopy(SCHEMA)))
    def test_schema_must_remain_closed(self):
        s=copy.deepcopy(SCHEMA); s["additionalProperties"]=True
        self.assertTrue(validator.validation_errors(copy.deepcopy(RECORD),s))

if __name__=="__main__": unittest.main()
