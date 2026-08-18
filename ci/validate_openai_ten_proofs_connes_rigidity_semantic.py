#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-E-CONNES-RIGIDITY/audit_record.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_connes_rigidity_semantic.schema.json"

TARGETS = [
    "ConnesRigidity.exists_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors",
    "ConnesRigidity.exists_infinite_pairwise_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors",
]
CLASSES = [
    "source_faithful_two_group_consequence_with_structured_factor_isomorphism",
    "source_faithful_theorem_1_2_projection_with_derived_pairwise_factor_transitivity",
]
AXIOMS = ["propext", "Quot.sound", "Classical.choice"]

def load(p): return json.loads(p.read_text(encoding="utf-8"))

def validation_errors(record=None, schema=None):
    r = load(RECORD) if record is None else record
    s = load(SCHEMA) if schema is None else schema
    e = []
    if s.get("additionalProperties") is not False:
        e.append("schema must remain top-level closed")
    e += [f"schema: {x.message}" for x in Draft202012Validator(s).iter_errors(r)]

    if (r.get("schema_version"), r.get("record_id"), r.get("candidate_id"), r.get("result_family")) != (
        "1.0.0", "MF-OTP-E-CONNES-RIGIDITY-SEMANTIC-002", "OPENAI-TEN-PROOFS-001", "OTP-E-CONNES-RIGIDITY"):
        e.append("record identity drift")

    if r.get("governance") != {
        "tracker_issue":96,
        "protected_base":"081928fceaca9606af4920559f8b79d5e40225a7",
        "publication_state":"candidate_until_protected_merge",
        "candidate_exit_state":"SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT",
        "head_change_requires_reapproval":True,
    }:
        e.append("governance/base/exit-state drift")

    src = r.get("source_authority", {})
    exact_src = {
        "revision":"2026-08-06",
        "pdf_sha256":"ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566",
        "pdf_byte_length":2487031,
        "pdf_successor_record_blob":"02d1748abed36717afba46451330be165c076737",
        "pdf_successor_protected_merge":"275f435eaf519ada3f0afa4bf8e77cfd0c8fcbb3",
        "chapter":4,
    }
    for k,v in exact_src.items():
        if src.get(k) != v: e.append(f"source authority drift: {k}")
    loci = "\n".join(src.get("loci", []))
    for t in ("Theorem 1.2", "finitely generated", "pairwise nonisomorphic",
              "L(Gamma_n)", "Corollary 5.10", "canonical trace",
              "measure-preserving", "do not separately print", "transitivity consequence"):
        if t not in loci: e.append(f"source locus lost: {t}")

    f = r.get("formal_authority", {})
    if f.get("root") != "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6" or f.get("tree") != "174289e4d4958cb0509874e6e53400e098213de7":
        e.append("formal root/tree drift")
    if f.get("formal_successor_record_blob") != "6993ce9fac2c65ffae7f2a0c7d728aab828ed532":
        e.append("formal successor drift")
    if f.get("config") != {"path":"ComparatorChallenges/E_ConnesRigidity.json","blob":"f5d2964be6b1a154bc12b38a0f99f0960960a2d9"}:
        e.append("config identity drift")
    if f.get("challenge") != {"path":"ComparatorChallenges/E_ConnesRigidity.lean","blob":"9425edabd79319cbe2943888c6ece107bdd81dfb"}:
        e.append("challenge identity drift")
    if f.get("solution") != {"path":"ConnesRigidity.lean","blob":"81cf03e3f7ccdc66815cc00c9969bcfd2341c8d6"}:
        e.append("solution identity drift")
    if f.get("mathlib_finite_generation") != {
        "repository":"leanprover-community/mathlib4",
        "commit":"81a5d257c8e410db227a6665ed08f64fea08e997",
        "path":"Mathlib/GroupTheory/Finiteness.lean",
        "blob":"b23c7420082cfcfe583ba2ed39a8c9f0c86d73b1",
    }:
        e.append("finite-generation definition identity drift")
    if f.get("targets") != TARGETS:
        e.append("target inventory/order drift")
    rp = f.get("replay", {})
    if (rp.get("run_id"), rp.get("job_id"), rp.get("result")) != (31945652355, 95161117059, "comparator_lean_kernel_nanoda_accept"):
        e.append("replay identity/result drift")
    if rp.get("permitted_axioms") != AXIOMS:
        e.append("formal axiom drift")

    defs = r.get("definition_concordance", {})
    required = {
      "namespace_identity":("ConnesRigidity.*","ConnesRigidity2.*","no alias"),
      "countable_group_and_icc":("Countable","Infinite G","conjugacy class"),
      "group_isomorphism":("Nonempty","≃*"),
      "property_t":("almost invariant","nonzero invariant","Type u","universe-scoped","does not claim"),
      "group_von_neumann_algebra_and_trace":("bicommutant","left regular","canonicalTrace","delta_1"),
      "factor_isomorphism_structure":("star-algebra","IsProjectionSupremum","trace","PaperFactorUnitaryWitness","maps the group-factor algebras","vacuum","starAlgEquiv_isNormal","not verbatim","not an independently audited equivalence"),
      "finite_generation":("Group.FG","Theorem 1.2","finitely generated"),
      "infinite_family_quantifiers":("Nat","every n","pairwise nonisomorphism","symmetry and transitivity"),
    }
    if set(defs) != set(required):
        e.append("definition concordance shape drift")
    for k,ts in required.items():
        txt = defs.get(k,"")
        for t in ts:
            if t not in txt: e.append(f"definition concordance lost: {k}/{t}")

    audits = r.get("target_audits", [])
    if len(audits) != 2 or [a.get("target") for a in audits] != TARGETS or [a.get("classification") for a in audits] != CLASSES:
        e.append("target audit/classification drift")
    if len(audits) == 2:
        need = [
          ("Corollary 5.10","Theorem 1.2","finite generation","spatial","not claimed as verbatim"),
          ("Theorem 1.2","all-pairs","groupFactorsIsomorphic_trans","groupFactorsIsomorphic_symm","direct formal consequence"),
        ]
        for a,ts in zip(audits,need):
            txt = a.get("source_relation","") + "\n" + a.get("formal_relation","")
            for t in ts:
                if t not in txt: e.append(f"target evidence lost: {a.get('target')}/{t}")

    nv = r.get("nonvacuity", {})
    if nv.get("state") != "clear_for_exact_two_target_surface_with_universe_scope_recorded":
        e.append("nonvacuity state drift")
    nvt = "\n".join(nv.get("evidence", []))
    for t in ("manuscriptInfinitePropertyTFiber","Nat-indexed","paper_factors_isomorphic","paperFactorUnitaryWitness","maps both algebra and vacuum","symmetry/transitivity","universe scope"):
        if t not in nvt: e.append(f"nonvacuity evidence lost: {t}")

    paths = "\n".join(r.get("proof_path_evidence", []))
    for t in ("paperInfinitePropertyTFiber","paperFactorUnitaryWitness","paperHaarTransport","toTracialGroupFactorEquiv","trace_preserving","starAlgEquiv_isNormal","paper_factors_isomorphic","groupFactorsIsomorphic_trans","groupFactorsIsomorphic_symm"):
        if t not in paths: e.append(f"proof path lost: {t}")

    ra = r.get("replay_and_axiom_audit", {})
    if (ra.get("state"),ra.get("run_id"),ra.get("job_id")) != ("clear_as_source_root_replay_evidence",31945652355,95161117059):
        e.append("replay audit drift")
    if ra.get("permitted_axioms_only") != AXIOMS:
        e.append("axiom audit drift")

    ao = r.get("anti_overclaim", {})
    for k in (
        "predecessor_namespace_alias_inferred",
        "theorem_text_claims_trace_preserving_verbatim",
        "theorem_text_claims_normal_star_isomorphism_verbatim",
        "pairwise_gamma_factor_isomorphism_claimed_source_verbatim",
        "universe_polymorphic_property_t_equivalence_claimed",
        "all_analytic_normality_notions_claimed_equivalent",
        "whole_chapter_semantic_equivalence",
        "proof_bodies_compared_in_full",
        "proof_correctness_certified_here",
        "solve_authority","cert_authority",
        "mathematical_targets_marked_proved",
        "aggregate_ten_proofs_authority",
    ):
        if ao.get(k) is not False: e.append(f"anti-overclaim violated: {k}")

    d = r.get("disposition", {})
    if d.get("semantic_state") != "candidate_clear_pending_independent_review" or d.get("candidate_family_exit_state") != "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("candidate disposition drift")
    if d.get("solve_handoff_authorized") is not False or d.get("mathcert_route_authorized") is not False:
        e.append("downstream authority inflation")

    act = r.get("activation", {})
    for k in (
        "requires_exact_head_forge_ci","requires_exact_head_gcl_conformance",
        "requires_exact_head_codeql","requires_non_author_approved_review",
        "requires_operator_algebra_specialist_review","head_change_requires_reapproval",
        "streamlined_exact_head_binding_allowed_if_control_plan_unchanged",
        "material_control_plan_change_requires_renewed_steward_input",
        "effect_does_not_authorize_solve","effect_does_not_authorize_cert",
    ):
        if act.get(k) is not True: e.append(f"activation weakened: {k}")

    rc = r.get("route_controls", {})
    for k in ("solve_handoff_authorized","mathcert_route_authorized","adjudication_authorized","cert_output_authorized","mathematical_targets_proved","aggregate_openai_ten_proofs_authority"):
        if rc.get(k) is not False: e.append(f"route authority inflation: {k}")

    b = r.get("claim_boundary","")
    for t in ("two registered OTP-E-CONNES-RIGIDITY targets","ConnesRigidity.*","ConnesRigidity2.*","spatial/tracial refinement","not claim that trace-preserving","universe-polymorphic","symmetry/transitivity consequence","no MATHSOLVE handoff","aggregate OpenAI Ten Proofs authority"):
        if t not in b: e.append(f"claim boundary lost: {t}")
    return e

def main():
    e = validation_errors()
    if e:
        print("\n".join(e), file=sys.stderr)
        return 1
    print("validated OTP-E Connes rigidity current-root semantic/nonvacuity candidate")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
