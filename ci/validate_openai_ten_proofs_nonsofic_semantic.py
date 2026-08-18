#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-D-NON-SOFIC/audit_record.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_nonsofic_semantic.schema.json"
TARGET = "SoficGroups.SourceTopLevelCompressionFinal.exists_finitelyPresented_nonsofic_group"
CLASSIFICATION = "derived_finitely_presented_nonsofic_consequence_of_source_nonsofic_construction"
AXIOMS = ["propext", "Classical.choice", "Quot.sound"]

def load(path): return json.loads(path.read_text(encoding="utf-8"))

def validation_errors(record=None, schema=None):
    r = load(RECORD) if record is None else record
    s = load(SCHEMA) if schema is None else schema
    e=[]
    if s.get("additionalProperties") is not False: e.append("schema must remain top-level closed")
    e += [f"schema: {x.message}" for x in Draft202012Validator(s).iter_errors(r)]
    if (r.get("schema_version"),r.get("record_id"),r.get("candidate_id"),r.get("result_family")) != ("1.0.0","MF-OTP-D-NON-SOFIC-SEMANTIC-002","OPENAI-TEN-PROOFS-001","OTP-D-NON-SOFIC"):
        e.append("record identity drift")
    if r.get("governance") != {"tracker_issue":95,"protected_base":"f0a40146cca7fd39c5724ed5be033ee9092625ac","publication_state":"candidate_until_protected_merge","candidate_exit_state":"SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT","head_change_requires_reapproval":True}:
        e.append("governance/base/exit-state drift")
    src=r.get("source_authority",{})
    exact={"revision":"2026-08-06","pdf_sha256":"ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566","pdf_byte_length":2487031,"pdf_successor_record_blob":"02d1748abed36717afba46451330be165c076737","pdf_successor_protected_merge":"275f435eaf519ada3f0afa4bf8e77cfd0c8fcbb3","chapter":3}
    for k,v in exact.items():
        if src.get(k)!=v: e.append(f"source authority drift: {k}")
    loci="\n".join(src.get("loci",[]))
    for t in ("Theorem 1.1","does not state that a finitely presented","finitely generated nonsofic subgroup","EL_D(R)","EL_9(R)","normalized Hamming","countable-group sofic approximation"):
        if t not in loci: e.append(f"source locus lost: {t}")
    f=r.get("formal_authority",{})
    if f.get("root")!="94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6" or f.get("tree")!="174289e4d4958cb0509874e6e53400e098213de7": e.append("formal root/tree drift")
    if f.get("formal_successor_record_blob")!="6993ce9fac2c65ffae7f2a0c7d728aab828ed532": e.append("formal successor drift")
    if f.get("config")!={"path":"ComparatorChallenges/D_NonSoficGroup.json","blob":"af023106a83552d7fafb4f0d122f121a095f802c"}: e.append("config identity drift")
    if f.get("challenge")!={"path":"ComparatorChallenges/D_NonSoficGroup.lean","blob":"158d97224fbd51c203ff07a2f74041ffa2c6013b","byte_length":1117}: e.append("challenge identity drift")
    if f.get("solution")!={"path":"NonSoficGroup.lean","blob":"dd1f8e63960300c8674fcd491007d2a628fbc6fe","byte_length":1343031}: e.append("solution identity drift")
    if f.get("mathlib_finite_presentation")!={"repository":"leanprover-community/mathlib4","commit":"81a5d257c8e410db227a6665ed08f64fea08e997","path":"Mathlib/GroupTheory/FinitelyPresentedGroup.lean","blob":"449ec578624bd05410992e89048a7c1a7bae238d"}: e.append("finite-presentation authority drift")
    if f.get("targets") != [TARGET]: e.append("target inventory drift")
    rp=f.get("replay",{})
    if (rp.get("run_id"),rp.get("job_id"),rp.get("result")) != (31945652355,95161117044,"comparator_lean_kernel_nanoda_accept"): e.append("replay identity/result drift")
    if rp.get("permitted_axioms") != AXIOMS: e.append("formal axiom drift")
    defs=r.get("definition_concordance",{})
    required={
      "sofic_convention":("normalizedHamming","GoodOn","every finite F","finite exhaustion","1/(n+2)"),
      "source_nonsofic_carrier":("EL_D(R)","EL_9(R)","binaryLeavittElementaryGroup 9","ninePrefixElementaryGroupEquiv","not_sofic"),
      "finite_obstruction":("exists_finite_obstruction","0<epsilon<1","finite F","not a claim printed"),
      "table_group":("multiplicationTable","tableRelators","PresentedGroup","tableGroup_not_sofic_of_obstruction"),
      "finite_presentation":("FreeGroup (Fin n)","surjective","normal closure","finitely many relations","tableGroup_finitelyPresented"),
      "universe_and_existence":("preserves","Type","Group instance","no universe lift"),
    }
    if set(defs)!=set(required): e.append("definition concordance shape drift")
    for k,ts in required.items():
        txt=defs.get(k,"")
        for t in ts:
            if t not in txt: e.append(f"definition concordance lost: {k}/{t}")
    audits=r.get("target_audits",[])
    if len(audits)!=1 or audits[0].get("target")!=TARGET or audits[0].get("classification")!=CLASSIFICATION: e.append("target audit/classification drift")
    if len(audits)==1:
        txt=audits[0].get("source_relation","")+"\n"+audits[0].get("formal_relation","")
        for t in ("does not state","finitely generated nonsofic subgroup","exists_finitelyPresented_not_sofic_of_not_sofic","finite failed sofic test","not a verbatim projection"):
            if t not in txt: e.append(f"target evidence lost: {t}")
    nv=r.get("nonvacuity",{})
    if nv.get("state")!="clear_for_exact_target": e.append("nonvacuity state drift")
    nvt="\n".join(nv.get("evidence",[]))
    for t in ("concrete countable group","actual negation","0<epsilon<1","PresentedGroup","pulling","concrete group structure"):
        if t not in nvt: e.append(f"nonvacuity evidence lost: {t}")
    paths="\n".join(r.get("proof_path_evidence",[]))
    for t in ("binaryLeavittElementaryGroup_not_sofic","exists_finite_obstruction","tableRelators","tableGroup_finitelyPresented","goodOn_pullbackTableModel","tableGroup_not_sofic_of_obstruction","exists_finitelyPresented_not_sofic_of_not_sofic"):
        if t not in paths: e.append(f"proof path lost: {t}")
    ra=r.get("replay_and_axiom_audit",{})
    if (ra.get("state"),ra.get("run_id"),ra.get("job_id")) != ("clear_as_source_root_replay_evidence",31945652355,95161117044): e.append("replay audit drift")
    if ra.get("permitted_axioms_only") != AXIOMS: e.append("axiom audit drift")
    ao=r.get("anti_overclaim",{})
    for k in ("finitely_presented_conclusion_claimed_source_verbatim","source_theorem_1_1_rewritten_as_finitely_presented","unit_group_definitionally_identified_with_el9","finite_obstruction_claimed_as_manuscript_result","whole_chapter_semantic_equivalence","proof_bodies_compared_in_full","proof_correctness_certified_here","solve_authority","cert_authority","mathematical_target_marked_proved","aggregate_ten_proofs_authority"):
        if ao.get(k) is not False: e.append(f"anti-overclaim violated: {k}")
    d=r.get("disposition",{})
    if d.get("semantic_state")!="candidate_clear_pending_independent_review" or d.get("candidate_family_exit_state")!="SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT": e.append("candidate disposition drift")
    if d.get("solve_handoff_authorized") is not False or d.get("mathcert_route_authorized") is not False: e.append("downstream authority inflation")
    act=r.get("activation",{})
    for k in ("requires_exact_head_forge_ci","requires_exact_head_gcl_conformance","requires_exact_head_codeql","requires_non_author_approved_review","requires_geometric_group_theory_specialist_review","head_change_requires_reapproval","streamlined_exact_head_binding_allowed_if_control_plan_unchanged","material_control_plan_change_requires_renewed_steward_input","effect_does_not_authorize_solve","effect_does_not_authorize_cert"):
        if act.get(k) is not True: e.append(f"activation weakened: {k}")
    rc=r.get("route_controls",{})
    for k in ("solve_handoff_authorized","mathcert_route_authorized","adjudication_authorized","cert_output_authorized","mathematical_target_proved","aggregate_openai_ten_proofs_authority"):
        if rc.get(k) is not False: e.append(f"route authority inflation: {k}")
    b=r.get("claim_boundary","")
    for t in ("single registered OTP-D-NON-SOFIC target","finite-obstruction","does not attribute finite presentation","standard finite-generators","no MATHSOLVE handoff","aggregate OpenAI Ten Proofs authority"):
        if t not in b: e.append(f"claim boundary lost: {t}")
    return e

def main():
    e=validation_errors()
    if e:
        print("\n".join(e),file=sys.stderr); return 1
    print("validated OTP-D Non-Sofic current-root semantic/nonvacuity candidate"); return 0

if __name__=="__main__": raise SystemExit(main())
