#!/usr/bin/env python3
from __future__ import annotations

import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-I-RAMSEY/audit_record.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_ramsey_semantic.schema.json"
TARGETS = [
    "ErdosProblems.MulticolourTriangleRamsey.erdos_183",
    "ErdosProblems.MulticolourTriangleRamsey.erdos_problem_183_explicit",
    "ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_sharp_coefficients",
    "ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_isTheta",
]
CLASSES = [
    "source_faithful_exact_projection_of_displayed_consequence_4",
    "formal_explicit_constant_strengthening_plus_source_faithful_divergence",
    "source_faithful_epsilonized_logarithmic_reformulation",
    "source_faithful_logarithmic_reformulation_of_printed_theta",
]
AXIOMS = ["propext", "Quot.sound", "Classical.choice"]

def load(p): return json.loads(p.read_text(encoding="utf-8"))

def validation_errors(record=None, schema=None):
    r = load(RECORD) if record is None else record
    s = load(SCHEMA) if schema is None else schema
    e=[]
    if s.get("additionalProperties") is not False: e.append("schema must remain top-level closed")
    e += [f"schema: {x.message}" for x in Draft202012Validator(s).iter_errors(r)]
    if (r.get("schema_version"),r.get("record_id"),r.get("candidate_id"),r.get("result_family")) != ("1.0.0","MF-OTP-I-RAMSEY-SEMANTIC-002","OPENAI-TEN-PROOFS-001","OTP-I-RAMSEY"):
        e.append("record identity drift")
    g=r.get("governance",{})
    if g != {"tracker_issue":93,"protected_base":"0520d8bae3853798f2edca67c526133e46847a54","publication_state":"candidate_until_protected_merge","candidate_exit_state":"SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT","head_change_requires_reapproval":True}:
        e.append("governance/base/exit-state drift")
    src=r.get("source_authority",{})
    exact={"revision":"2026-08-06","pdf_sha256":"ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566","pdf_byte_length":2487031,"pdf_successor_record_blob":"02d1748abed36717afba46451330be165c076737","pdf_successor_protected_merge":"275f435eaf519ada3f0afa4bf8e77cfd0c8fcbb3","chapter":9}
    for k,v in exact.items():
        if src.get(k)!=v: e.append(f"source authority drift: {k}")
    loci="\n".join(src.get("loci",[]))
    for t in ("least N","absolute c>0","does not specify c=1/(6e^38)","lim_{k->infinity}","1/3-o(1)","Theta(k)","natural"):
        if t not in loci: e.append(f"source locus lost: {t}")
    f=r.get("formal_authority",{})
    if f.get("root")!="94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6" or f.get("tree")!="174289e4d4958cb0509874e6e53400e098213de7": e.append("formal root/tree drift")
    if f.get("formal_successor_record_blob")!="6993ce9fac2c65ffae7f2a0c7d728aab828ed532": e.append("formal successor drift")
    if f.get("config")!={"path":"ComparatorChallenges/I_MulticolorTriangleRamsey.json","blob":"ce67db0653e18a2de68f471c00b9f892b789f806"}: e.append("config identity drift")
    if f.get("challenge")!={"path":"ComparatorChallenges/I_MulticolorTriangleRamsey.lean","blob":"6a9e42d686720f4b74ddc2001006b0b7a20f11aa"}: e.append("challenge identity drift")
    if f.get("solution")!={"path":"MulticolorTriangleRamsey.lean","blob":"24b55f531a4d36347cd2277b1b9c7d784d91ae35","byte_length":125769}: e.append("solution identity drift")
    if f.get("targets")!=TARGETS: e.append("target inventory/order drift")
    rp=f.get("replay",{})
    if (rp.get("run_id"),rp.get("job_id"),rp.get("result"))!=(31945652355,95161117103,"comparator_lean_kernel_nanoda_accept"): e.append("replay identity/result drift")
    if rp.get("permitted_axioms")!=AXIOMS: e.append("formal axiom drift")
    defs=r.get("definition_concordance",{})
    required={
      "colouring":("every colour","CliqueFree 3","monochromatic triangle"),
      "ramsey_number":("Nat.sInf","nonempty","triangleRamseyNumber_forces","triangleFree_lt_triangleRamseyNumber","least-N"),
      "logarithms":("natural","Real.log","log-base"),
      "explicit_constant":("unspecified","1/(6*exp 38)","quantitativeLowerBound_explicit_all","quantitativeLowerBound_explicit_small","k<342"),
      "asymptotics":("epsilonized","1/3-o(1)","1+o(1)","Theta"),
    }
    if set(defs)!=set(required): e.append("definition concordance shape drift")
    for k,ts in required.items():
        txt=defs.get(k,"")
        for t in ts:
            if t not in txt: e.append(f"definition concordance lost: {k}/{t}")
    audits=r.get("target_audits",[])
    if len(audits)!=4 or [x.get("target") for x in audits]!=TARGETS or [x.get("classification") for x in audits]!=CLASSES: e.append("target audit/classification drift")
    if len(audits)==4:
        need=[("consequence (4)","divergentRamseyRoot"),("unspecified","1/(6e^38)","quantitativeLowerBound_explicit_all"),("1/3-o(1)","factorial"),("k^{Theta(k)}","k*log k")]
        for a,ts in zip(audits,need):
            txt=a.get("source_relation","")+"\n"+a.get("formal_relation","")
            for t in ts:
                if t not in txt: e.append(f"target evidence lost: {a.get('target')}/{t}")
    nv=r.get("nonvacuity",{})
    if nv.get("state")!="clear_for_all_four_targets": e.append("nonvacuity state drift")
    nvt="\n".join(nv.get("evidence",[]))
    for t in ("k=2","exists_forcesMonochromaticTriangle","nonempty","triangleRamseyNumber_forces","triangleFree_lt_triangleRamseyNumber","0<triangleRamseyNumber","atTop"):
        if t not in nvt: e.append(f"nonvacuity evidence lost: {t}")
    paths="\n".join(r.get("proof_path_evidence",[]))
    for t in ("erdos_183","divergentRamseyRoot","quantitativeLowerBound_explicit_all","exp 38","k<342","triangleRamseyNumber_factorial_upper","log_isTheta"):
        if t not in paths: e.append(f"proof path lost: {t}")
    ra=r.get("replay_and_axiom_audit",{})
    if (ra.get("state"),ra.get("run_id"),ra.get("job_id")) != ("clear_as_source_root_replay_evidence",31945652355,95161117103): e.append("replay audit drift")
    if ra.get("permitted_axioms_only")!=AXIOMS: e.append("axiom audit drift")
    ao=r.get("anti_overclaim",{})
    for k in ("explicit_constant_claimed_as_manuscript_constant","epsilon_log_target_claimed_source_verbatim","whole_chapter_semantic_equivalence","proof_bodies_compared_in_full","proof_correctness_certified_here","solve_authority","cert_authority","mathematical_targets_marked_proved","aggregate_ten_proofs_authority"):
        if ao.get(k) is not False: e.append(f"anti-overclaim violated: {k}")
    d=r.get("disposition",{})
    if d.get("semantic_state")!="candidate_clear_pending_independent_review" or d.get("candidate_family_exit_state")!="SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT": e.append("candidate disposition drift")
    if d.get("solve_handoff_authorized") is not False or d.get("mathcert_route_authorized") is not False: e.append("downstream authority inflation")
    act=r.get("activation",{})
    for k in ("requires_exact_head_forge_ci","requires_exact_head_gcl_conformance","requires_exact_head_codeql","requires_non_author_approved_review","head_change_requires_reapproval","streamlined_exact_head_binding_allowed_if_control_plan_unchanged","material_control_plan_change_requires_renewed_steward_input","effect_does_not_authorize_solve","effect_does_not_authorize_cert"):
        if act.get(k) is not True: e.append(f"activation weakened: {k}")
    rc=r.get("route_controls",{})
    for k in ("solve_handoff_authorized","mathcert_route_authorized","adjudication_authorized","cert_output_authorized","mathematical_target_proved","aggregate_openai_ten_proofs_authority"):
        if rc.get(k) is not False: e.append(f"route authority inflation: {k}")
    b=r.get("claim_boundary","")
    for t in ("four registered OTP-I-RAMSEY targets","unspecified absolute constant c","1/(6e^38)","no MATHSOLVE handoff","aggregate OpenAI Ten Proofs authority"):
        if t not in b: e.append(f"claim boundary lost: {t}")
    return e

def main():
    e=validation_errors()
    if e:
        print("\n".join(e),file=sys.stderr); return 1
    print("validated OTP-I Ramsey current-root semantic/nonvacuity candidate"); return 0
if __name__=="__main__": raise SystemExit(main())
