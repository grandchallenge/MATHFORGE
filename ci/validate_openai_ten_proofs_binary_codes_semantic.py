#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-B1-BINARY-CODES/audit_record.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_binary_codes_semantic.schema.json"

TARGETS = [
    "MetricCodes.Hamming.binaryRate_lt_classicalRate",
    "MetricCodes.Hamming.exists_binaryRate_improvement",
    "MetricCodes.Johnson.binaryRate_le_combinedVariationalRate",
    "MetricCodes.MRRW.strict_mrrw2",
    "MetricCodes.Johnson.binaryRate_lt_mrrw",
    "MetricCodes.Johnson.exists_binaryRate_mrrw_improvement",
]
CLASSIFICATIONS = [
    "source_faithful_derived_consequence",
    "derived_positive_margin_certificate",
    "source_faithful_exact_projection",
    "source_faithful_exact_projection",
    "source_faithful_derived_consequence",
    "derived_positive_margin_certificate",
]
PERMITTED_AXIOMS = ["propext", "Quot.sound", "Classical.choice"]


def load_record(path: Path = RECORD):
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema(path: Path = SCHEMA):
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record=None, schema=None):
    r = load_record() if record is None else record
    s = load_schema() if schema is None else schema
    e: list[str] = []

    if s.get("additionalProperties") is not False:
        e.append("top-level schema must remain closed")
    for err in sorted(Draft202012Validator(s).iter_errors(r), key=lambda x: list(x.path)):
        e.append(f"schema: {err.message}")

    if r.get("schema_version") != "1.0.0" or r.get("record_id") != "MF-OTP-B1-BINARY-CODES-SEMANTIC-002":
        e.append("record identity drift")
    if r.get("candidate_id") != "OPENAI-TEN-PROOFS-001" or r.get("result_family") != "OTP-B1-BINARY-CODES":
        e.append("candidate/family drift")

    g = r.get("governance", {})
    expected_g = {
        "tracker_issue": 91,
        "protected_base": "b9dda1a5b958fd1be37a26324a025013a39584c1",
        "publication_state": "candidate_until_protected_merge",
        "candidate_exit_state": "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT",
        "head_change_requires_reapproval": True,
    }
    if g != expected_g:
        e.append("governance/base/exit-state drift")

    src = r.get("source_authority", {})
    exact_source = {
        "document": "Ten Advances in Mathematics and Theoretical Computer Science",
        "revision": "2026-08-06",
        "pdf_sha256": "ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566",
        "pdf_byte_length": 2487031,
        "pdf_successor_record_path": "sources/OPENAI-TEN-PROOFS-001/pdf_source_successors/OTP-SOURCE-PDF-SUCCESSOR-002.json",
        "pdf_successor_record_blob": "02d1748abed36717afba46451330be165c076737",
        "pdf_successor_protected_merge": "275f435eaf519ada3f0afa4bf8e77cfd0c8fcbb3",
        "chapter": 2,
    }
    for key, value in exact_source.items():
        if src.get(key) != value:
            e.append(f"source authority drift: {key}")
    loci = "\n".join(src.get("loci", []))
    for token in ("A2(n,d)", "R2(delta)", "kappa_H", "M2=min", "kappa_CW", "kappa_bin", "Theorem 1.1", "Theorem 3.8"):
        if token not in loci:
            e.append(f"source locus lost: {token}")

    f = r.get("formal_authority", {})
    if f.get("repository") != "openai/ten-proofs":
        e.append("formal repository drift")
    if f.get("root") != "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6" or f.get("tree") != "174289e4d4958cb0509874e6e53400e098213de7":
        e.append("formal root/tree drift")
    if f.get("formal_successor_record_blob") != "6993ce9fac2c65ffae7f2a0c7d728aab828ed532":
        e.append("formal successor drift")
    if f.get("config") != {"path": "ComparatorChallenges/B_BinaryCodes.json", "blob": "b530b77972c83396c1f2aed2deccda3a12fb6cab"}:
        e.append("config identity drift")
    if f.get("challenge") != {"path": "ComparatorChallenges/B_BinaryCodes.lean", "blob": "c9e93b1944e6806802068cf593fa6557e4267bb1"}:
        e.append("challenge identity drift")
    if f.get("solution") != {"path": "MetricCodes.lean", "blob": "51628c0db81bd6cb9a79777fa601306c9d64cbc5", "byte_length": 4531268}:
        e.append("solution identity drift")
    if f.get("targets") != TARGETS:
        e.append("target inventory/order drift")
    rp = f.get("replay", {})
    if rp.get("run_id") != 31945652355 or rp.get("job_id") != 95161117069 or rp.get("result") != "comparator_lean_kernel_nanoda_accept":
        e.append("replay identity/result drift")
    if rp.get("lean_version") != "4.32.0" or rp.get("lean_commit") != "8c9756b28d64dab099da31a4c09229a9e6a2ef35":
        e.append("Lean toolchain drift")
    if rp.get("permitted_axioms") != PERMITTED_AXIOMS:
        e.append("formal replay axiom drift")

    defs = r.get("definition_concordance", {})
    expected_def_keys = {"binary_code", "maximum_size", "rate", "entropy_and_m1", "whole_cube", "constant_weight", "second_mrrw"}
    if set(defs) != expected_def_keys:
        e.append("definition concordance shape drift")
    field_tokens = {
        "maximum_size": ("A2(n,d)", "codeNumber_pos"),
        "rate": ("ceil(delta*n)", "base 2", "limsup"),
        "entropy_and_m1": ("H2", "M1"),
        "whole_cube": ("kappa_H", "0<=b<a<=1/2", "Gamma_H"),
        "constant_weight": ("kappa_CW", "kappa_bin", "spectralLimit"),
        "second_mrrw": ("sInf", "source minimum M2", "exists_mrrw_minimizer", "mrrwRate_eq_objective_of_minimizer"),
    }
    for field, tokens in field_tokens.items():
        text = str(defs.get(field, ""))
        for token in tokens:
            if token not in text:
                e.append(f"definition concordance qualification lost: {field}:{token}")

    audits = r.get("target_audits", [])
    if len(audits) != 6:
        e.append("target audit count drift")
    else:
        if [x.get("target") for x in audits] != TARGETS:
            e.append("target audit inventory/order drift")
        if [x.get("classification") for x in audits] != CLASSIFICATIONS:
            e.append("target classification drift")
        text = "\n".join(x.get("source_relation", "") + "\n" + x.get("solution_path", "") for x in audits)
        for token in ("R2<=kappa_H<M1", "epsilon", "R2<=kappa_bin", "kappa_bin<M2", "R2<M2", "mrrwRate(delta)-combinedVariationalRate(delta)"):
            if token not in text:
                e.append(f"target relation evidence lost: {token}")

    nv = r.get("nonvacuity", {})
    if nv.get("state") != "clear_for_all_six_targets":
        e.append("nonvacuity state drift")
    nvtext = "\n".join(nv.get("evidence", []))
    for token in ("delta=1/4", "codeNumber_pos", "Hamming.rateSet_nonempty_of_interior", "Johnson.rateSet_nonempty_of_interior", "exists_mrrw_minimizer", "positive differences"):
        if token not in nvtext:
            e.append(f"nonvacuity evidence lost: {token}")

    ra = r.get("replay_and_axiom_audit", {})
    if ra.get("state") != "clear_as_source_root_replay_evidence" or ra.get("run_id") != 31945652355 or ra.get("job_id") != 95161117069:
        e.append("replay audit drift")
    if ra.get("permitted_axioms_only") != PERMITTED_AXIOMS:
        e.append("axiom audit drift")
    obs = "\n".join(ra.get("observations", []))
    for token in ("all six target names", "MetricCodes solution module built successfully", "Nanoda kernel accepts", "Lean default kernel accepts", "Comparator returned ACCEPT"):
        if token not in obs:
            e.append(f"replay observation lost: {token}")
    if "does not independently certify proof correctness" not in ra.get("authority_limit", ""):
        e.append("replay authority limit weakened")

    ao = r.get("anti_overclaim", {})
    for key in (
        "positive_margin_targets_source_printed_verbatim", "whole_chapter_semantic_equivalence",
        "proof_bodies_compared_in_full", "proof_correctness_certified_here", "solve_authority",
        "cert_authority", "mathematical_targets_marked_proved", "aggregate_ten_proofs_authority",
    ):
        if ao.get(key) is not False:
            e.append(f"anti-overclaim violated: {key}")

    d = r.get("disposition", {})
    if d.get("semantic_state") != "candidate_clear_pending_independent_review" or d.get("candidate_family_exit_state") != "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("candidate disposition drift")
    if d.get("solve_handoff_authorized") is not False or d.get("mathcert_route_authorized") is not False:
        e.append("downstream authority inflation in disposition")
    basis = d.get("basis", "")
    for token in ("ceiling convention", "M2", "minimizer theorem", "inhabited", "exact source projection"):
        if token not in basis:
            e.append(f"disposition basis weakened: {token}")

    act = r.get("activation", {})
    for key in ("requires_exact_head_forge_ci", "requires_exact_head_gcl_conformance", "requires_exact_head_codeql", "requires_non_author_approved_review", "head_change_requires_reapproval", "streamlined_exact_head_binding_allowed_if_control_plan_unchanged", "material_control_plan_change_requires_renewed_steward_input", "effect_does_not_authorize_solve", "effect_does_not_authorize_cert"):
        if act.get(key) is not True:
            e.append(f"activation gate weakened: {key}")

    rc = r.get("route_controls", {})
    for key in ("solve_handoff_authorized", "mathcert_route_authorized", "adjudication_authorized", "cert_output_authorized", "mathematical_target_proved", "aggregate_openai_ten_proofs_authority"):
        if rc.get(key) is not False:
            e.append(f"route/authority inflation: {key}")

    boundary = r.get("claim_boundary", "")
    for token in ("six registered OTP-B1-BINARY-CODES targets", "epsilon statements", "sInf formulation of M2", "no MATHSOLVE handoff", "no aggregate OpenAI Ten Proofs authority"):
        if token not in boundary:
            e.append(f"claim boundary missing token: {token}")

    return e


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated OTP-B1 Binary Codes current-root semantic/nonvacuity candidate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
