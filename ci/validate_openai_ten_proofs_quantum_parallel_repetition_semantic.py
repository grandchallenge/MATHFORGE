#!/usr/bin/env python3
from __future__ import annotations
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-G-QUANTUM-PARALLEL-REPETITION/audit_record.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_quantum_parallel_repetition_semantic.schema.json"
TARGETS = [
    "QuantumParallelRepetition.distributionUniformExponential",
    "QuantumParallelRepetition.standardQuantumParallelRepetition",
]
CLASSES = [
    "source_faithful_exact_coordinate_projection_of_theorem_1_1",
    "source_faithful_consequence_on_source_domain_with_formal_empty_answer_extension",
]
AXIOMS = ["propext", "Classical.choice", "Quot.sound"]

def load(p): return json.loads(p.read_text(encoding="utf-8"))

def validation_errors(record=None, schema=None):
    r = load(RECORD) if record is None else record
    s = load(SCHEMA) if schema is None else schema
    e = []
    if s.get("additionalProperties") is not False: e.append("schema must remain top-level closed")
    e += [f"schema: {x.message}" for x in Draft202012Validator(s).iter_errors(r)]
    if (r.get("schema_version"), r.get("record_id"), r.get("candidate_id"), r.get("result_family")) != (
        "1.0.0", "MF-OTP-G-QUANTUM-PARALLEL-REPETITION-SEMANTIC-002", "OPENAI-TEN-PROOFS-001", "OTP-G-QUANTUM-PARALLEL-REPETITION"):
        e.append("record identity drift")
    if r.get("governance") != {"tracker_issue":94,"protected_base":"dbf3b099331a1807c4d3036e7a6a406711ea7cf3","publication_state":"candidate_until_protected_merge","candidate_exit_state":"SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT","head_change_requires_reapproval":True}:
        e.append("governance/base/exit-state drift")
    src = r.get("source_authority", {})
    exact = {"revision":"2026-08-06","pdf_sha256":"ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566","pdf_byte_length":2487031,"pdf_successor_record_blob":"02d1748abed36717afba46451330be165c076737","pdf_successor_protected_merge":"275f435eaf519ada3f0afa4bf8e77cfd0c8fcbb3","chapter":6}
    for k,v in exact.items():
        if src.get(k) != v: e.append(f"source authority drift: {k}")
    loci = "\n".join(src.get("loci", []))
    for t in ("finite two-player one-round", "normalized question distribution", "supremum", "c_qs>0", "epsilon^13", "log(|A||B|)", "n>=1", "arbitrary finite local Hilbert-space dimensions", "does not require the optimum to be attained"):
        if t not in loci: e.append(f"source locus lost: {t}")
    f = r.get("formal_authority", {})
    if f.get("root") != "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6" or f.get("tree") != "174289e4d4958cb0509874e6e53400e098213de7": e.append("formal root/tree drift")
    if f.get("formal_successor_record_blob") != "6993ce9fac2c65ffae7f2a0c7d728aab828ed532": e.append("formal successor drift")
    if f.get("config") != {"path":"ComparatorChallenges/G_QuantumParallelRepetition.json","blob":"c7dd59e9df9ae5d90b35f76a9d958943d8e94770"}: e.append("config identity drift")
    if f.get("challenge") != {"path":"ComparatorChallenges/G_QuantumParallelRepetition.lean","blob":"8257e7726643a8f8c08c7e91584e003ab204c589","byte_length":4660}: e.append("challenge identity drift")
    if f.get("solution") != {"path":"QuantumParallelRepetition.lean","blob":"887c4378f124a5d81a3f2624b6dc34867ec409c4","byte_length":2683872}: e.append("solution identity drift")
    if f.get("targets") != TARGETS: e.append("target inventory/order drift")
    rp = f.get("replay", {})
    if (rp.get("run_id"), rp.get("job_id"), rp.get("result")) != (31945652355, 95161117041, "comparator_lean_kernel_nanoda_accept"): e.append("replay identity/result drift")
    if rp.get("permitted_axioms") != AXIOMS: e.append("formal axiom drift")
    defs = r.get("definition_concordance", {})
    required = {
      "game_model":("questionWeight","normalized","Boolean"),
      "parallel_repetition":("product question weights","every coordinate","G^n"),
      "strategy_model":("independent finite Alice and Bob","density matrix","POVM","not required to have a common dimension","orthonormal bases","no dimension bound"),
      "entangled_value":("sSup","supremum","no optimizer-attainment","definitional identity"),
      "gap_exponent_denominator":("1-entangledValue G","Nonempty A","Nonempty B","exponent 13","Real.log","0<n"),
      "qualitative_consequence":("HasExponentialBound","nonempty answer alphabets","empty-answer edge cases"),
    }
    if set(defs) != set(required): e.append("definition concordance shape drift")
    for k,ts in required.items():
        txt = defs.get(k, "")
        for t in ts:
            if t not in txt: e.append(f"definition concordance lost: {k}/{t}")
    audits = r.get("target_audits", [])
    if len(audits) != 2 or [x.get("target") for x in audits] != TARGETS or [x.get("classification") for x in audits] != CLASSES: e.append("target audit/classification drift")
    if len(audits) == 2:
        needs = [("Theorem 1.1","epsilon^13","Nonempty A/B","pdf_distributionUniformExponential_unconditional"),("game-dependent exponential decay","empty-answer edge cases","exact_standardQuantumParallelRepetition_of_source_rounding")]
        for a,ts in zip(audits, needs):
            txt = a.get("source_relation","") + "\n" + a.get("formal_relation","")
            for t in ts:
                if t not in txt: e.append(f"target evidence lost: {a.get('target')}/{t}")
    nv = r.get("nonvacuity", {})
    if nv.get("state") != "clear_on_declared_source_domain_with_empty_answer_extension_separated": e.append("nonvacuity state drift")
    nvt = "\n".join(nv.get("evidence", []))
    for t in ("Nonempty A","Nonempty B","0 < 1-entangledValue G","0 < n","normalized to total mass 1","pdfAlphabetEntropy_nonneg","exactSourceAnswerTypes_nonempty_of_remaining","formal extension"):
        if t not in nvt: e.append(f"nonvacuity evidence lost: {t}")
    paths = "\n".join(r.get("proof_path_evidence", []))
    for t in ("pdf_distributionUniformExponential_unconditional","unconditionalSourceOneGameRounding_uniform","exactSourceOneGameRounding_unconditional","exact_standardQuantumParallelRepetition_of_source_rounding","winProbabilities_bddAbove"):
        if t not in paths: e.append(f"proof path lost: {t}")
    ra = r.get("replay_and_axiom_audit", {})
    if (ra.get("state"),ra.get("run_id"),ra.get("job_id")) != ("clear_as_source_root_replay_evidence",31945652355,95161117041): e.append("replay audit drift")
    if ra.get("permitted_axioms_only") != AXIOMS: e.append("axiom audit drift")
    ao = r.get("anti_overclaim", {})
    for k in ("abstract_hilbert_space_definitional_identity_claimed","common_local_dimension_restriction_claimed","optimizer_attainment_claimed","empty_answer_extension_claimed_as_manuscript_scope","whole_chapter_semantic_equivalence","proof_bodies_compared_in_full","proof_correctness_certified_here","solve_authority","cert_authority","mathematical_targets_marked_proved","aggregate_ten_proofs_authority"):
        if ao.get(k) is not False: e.append(f"anti-overclaim violated: {k}")
    d = r.get("disposition", {})
    if d.get("semantic_state") != "candidate_clear_pending_independent_review" or d.get("candidate_family_exit_state") != "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT": e.append("candidate disposition drift")
    if d.get("solve_handoff_authorized") is not False or d.get("mathcert_route_authorized") is not False: e.append("downstream authority inflation")
    act = r.get("activation", {})
    for k in ("requires_exact_head_forge_ci","requires_exact_head_gcl_conformance","requires_exact_head_codeql","requires_non_author_approved_review","requires_quantum_information_specialist_review","head_change_requires_reapproval","streamlined_exact_head_binding_allowed_if_control_plan_unchanged","material_control_plan_change_requires_renewed_steward_input","effect_does_not_authorize_solve","effect_does_not_authorize_cert"):
        if act.get(k) is not True: e.append(f"activation weakened: {k}")
    rc = r.get("route_controls", {})
    for k in ("solve_handoff_authorized","mathcert_route_authorized","adjudication_authorized","cert_output_authorized","mathematical_target_proved","aggregate_openai_ten_proofs_authority"):
        if rc.get(k) is not False: e.append(f"route authority inflation: {k}")
    b = r.get("claim_boundary", "")
    for t in ("two registered OTP-G-QUANTUM-PARALLEL-REPETITION targets","independent finite Alice/Bob","sSup","empty-answer edge cases","no MATHSOLVE handoff","aggregate OpenAI Ten Proofs authority"):
        if t not in b: e.append(f"claim boundary lost: {t}")
    return e

def main():
    e = validation_errors()
    if e:
        print("\n".join(e), file=sys.stderr); return 1
    print("validated OTP-G Quantum Parallel Repetition current-root semantic/nonvacuity candidate"); return 0

if __name__ == "__main__": raise SystemExit(main())
