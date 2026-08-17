from __future__ import annotations
import copy, importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("ramsey_validator",ROOT/"ci/validate_openai_ten_proofs_ramsey_semantic.py")
assert SPEC and SPEC.loader
V=importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(V)

class RamseySemanticTests(unittest.TestCase):
    def setUp(self): self.r=V.load(V.RECORD); self.s=V.load(V.SCHEMA)
    def errors(self,r=None,s=None): return V.validation_errors(copy.deepcopy(self.r if r is None else r),copy.deepcopy(self.s if s is None else s))
    def mut(self,path,value):
        r=copy.deepcopy(self.r); n=r
        for k in path[:-1]: n=n[k]
        n[path[-1]]=value; return r
    def test_baseline(self): self.assertEqual([],self.errors())
    def test_open_schema(self):
        s=copy.deepcopy(self.s); s["additionalProperties"]=True; self.assertTrue(self.errors(s=s))
    def test_extra_authority(self):
        r=copy.deepcopy(self.r); r["aggregate_certificate"]=True; self.assertTrue(self.errors(r))
    def test_base_drift(self): self.assertTrue(self.errors(self.mut(["governance","protected_base"],"0"*40)))
    def test_source_digest_drift(self): self.assertTrue(self.errors(self.mut(["source_authority","pdf_sha256"],"0"*64)))
    def test_root_drift(self): self.assertTrue(self.errors(self.mut(["formal_authority","root"],"0"*40)))
    def test_solution_drift(self): self.assertTrue(self.errors(self.mut(["formal_authority","solution","blob"],"0"*40)))
    def test_target_substitution(self):
        r=copy.deepcopy(self.r); r["formal_authority"]["targets"][0]="fake"; self.assertTrue(self.errors(r))
    def test_constant_promoted_to_source(self): self.assertTrue(self.errors(self.mut(["anti_overclaim","explicit_constant_claimed_as_manuscript_constant"],True)))
    def test_explicit_constant_drift(self):
        r=copy.deepcopy(self.r); r["definition_concordance"]["explicit_constant"]=r["definition_concordance"]["explicit_constant"].replace("1/(6*exp 38)","1/(5*exp 38)"); self.assertTrue(self.errors(r))
    def test_small_k_bridge_erasure(self):
        r=copy.deepcopy(self.r); r["definition_concordance"]["explicit_constant"]=r["definition_concordance"]["explicit_constant"].replace("k<342","finite range"); self.assertTrue(self.errors(r))
    def test_triangle_semantics_drift(self):
        r=copy.deepcopy(self.r); r["definition_concordance"]["colouring"]=r["definition_concordance"]["colouring"].replace("CliqueFree 3","CliqueFree 4"); self.assertTrue(self.errors(r))
    def test_least_ramsey_normalization_erasure(self):
        r=copy.deepcopy(self.r); r["definition_concordance"]["ramsey_number"]=r["definition_concordance"]["ramsey_number"].replace("triangleRamseyNumber_forces","unproved"); self.assertTrue(self.errors(r))
    def test_log_base_drift(self):
        r=copy.deepcopy(self.r); r["definition_concordance"]["logarithms"]=r["definition_concordance"]["logarithms"].replace("natural","base 2"); self.assertTrue(self.errors(r))
    def test_explicit_target_classification_inflation(self):
        r=copy.deepcopy(self.r); r["target_audits"][1]["classification"]="source_faithful_exact_projection"; self.assertTrue(self.errors(r))
    def test_epsilon_target_source_verbatim_inflation(self): self.assertTrue(self.errors(self.mut(["anti_overclaim","epsilon_log_target_claimed_source_verbatim"],True)))
    def test_log_exponent_drift(self):
        r=copy.deepcopy(self.r); r["target_audits"][2]["source_relation"]=r["target_audits"][2]["source_relation"].replace("1/3-o(1)","1/2-o(1)"); self.assertTrue(self.errors(r))
    def test_theta_log_omission(self):
        r=copy.deepcopy(self.r); r["target_audits"][3]["formal_relation"]=r["target_audits"][3]["formal_relation"].replace("k*log k","k"); self.assertTrue(self.errors(r))
    def test_nonvacuity_erasure(self):
        r=copy.deepcopy(self.r); r["nonvacuity"]["evidence"]=[x for x in r["nonvacuity"]["evidence"] if "exists_forcesMonochromaticTriangle" not in x]; self.assertTrue(self.errors(r))
    def test_replay_drift(self): self.assertTrue(self.errors(self.mut(["formal_authority","replay","job_id"],0)))
    def test_axiom_inflation(self):
        r=copy.deepcopy(self.r); r["replay_and_axiom_audit"]["permitted_axioms_only"].append("sorryAx"); self.assertTrue(self.errors(r))
    def test_proof_promotion(self): self.assertTrue(self.errors(self.mut(["route_controls","mathematical_target_proved"],True)))
    def test_solve_inflation(self): self.assertTrue(self.errors(self.mut(["route_controls","solve_handoff_authorized"],True)))
    def test_cert_inflation(self): self.assertTrue(self.errors(self.mut(["route_controls","mathcert_route_authorized"],True)))
    def test_aggregate_inflation(self): self.assertTrue(self.errors(self.mut(["route_controls","aggregate_openai_ten_proofs_authority"],True)))
    def test_review_gate_removal(self): self.assertTrue(self.errors(self.mut(["activation","requires_non_author_approved_review"],False)))

if __name__=="__main__": unittest.main()
