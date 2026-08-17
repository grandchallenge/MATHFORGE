#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-B2-SPHERICAL-CODES/audit_record.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_spherical_codes_semantic.schema.json"

TARGETS = [
    "MetricCodes.Johnson.main_binary_theorem",
    "MetricCodes.Spherical.HigherHierarchy.main_general",
    "MetricCodes.Spherical.HigherHierarchy.strict_hierarchy",
    "MetricCodes.Spherical.HigherHierarchy.NumericalMaximum.eventually_kissingNumber_lt_published",
]
CLASSIFICATIONS = [
    "source_faithful_exact_projection",
    "source_faithful_structured_projection_theorem_1_2_and_consequence",
    "source_faithful_structured_projection_corollary_1_3",
    "formal_strengthening_entailing_source_asymptotic_numerical_statement",
]
PERMITTED_AXIOMS = ["propext", "Classical.choice", "Quot.sound"]


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

    if r.get("schema_version") != "1.0.0":
        e.append("schema version drift")
    if r.get("record_id") != "MF-OTP-B2-SPHERICAL-CODES-SEMANTIC-002":
        e.append("record identity drift")
    if r.get("candidate_id") != "OPENAI-TEN-PROOFS-001" or r.get("result_family") != "OTP-B2-SPHERICAL-CODES":
        e.append("candidate/family drift")

    g = r.get("governance", {})
    expected_g = {
        "tracker_issue": 92,
        "protected_base": "24a1fa0f020ee9cc7fbe2e7aea4cd840268ca748",
        "publication_state": "candidate_until_protected_merge",
        "candidate_exit_state": "SUCCESSOR_FOUR_TARGET_SURFACE__SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT",
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
    for token in (
        "0<delta<1/2", "R2(delta)<=kappa_bin(delta)<M2(delta)",
        "r>=0", "0<s<1", "2*Gamma_r>s", "closed hierarchy infimum",
        "strictly level by level", "0.39661+o(1)",
        "does not print an eventual exact exponent 0.39661",
    ):
        if token not in loci:
            e.append(f"source locus lost: {token}")

    f = r.get("formal_authority", {})
    if f.get("repository") != "openai/ten-proofs":
        e.append("formal repository drift")
    if f.get("root") != "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6":
        e.append("formal root drift")
    if f.get("tree") != "174289e4d4958cb0509874e6e53400e098213de7":
        e.append("formal tree drift")
    if f.get("formal_successor_record_blob") != "6993ce9fac2c65ffae7f2a0c7d728aab828ed532":
        e.append("formal successor drift")
    if f.get("config") != {"path": "ComparatorChallenges/B_SphericalCodes.json", "blob": "b343dca9c0373f80c6304f30f261b81b371661c3"}:
        e.append("config identity drift")
    if f.get("challenge") != {"path": "ComparatorChallenges/B_SphericalCodes.lean", "blob": "5f2bcda432b7091097ae8753cac24c08d0c10f6c"}:
        e.append("challenge identity drift")
    if f.get("solution") != {"path": "MetricCodes.lean", "blob": "51628c0db81bd6cb9a79777fa601306c9d64cbc5"}:
        e.append("solution identity drift")
    if f.get("predecessor_target_surface_authority_transferred") is not False:
        e.append("predecessor seven-target authority inflation")
    if f.get("target_surface_drift") != "explicit_replacement_of_predecessor_seven_target_surface_with_four_current_targets":
        e.append("target-surface drift erased or rewritten")
    if f.get("targets") != TARGETS:
        e.append("target inventory/order drift")
    rp = f.get("replay", {})
    if rp.get("run_id") != 31945652355 or rp.get("job_id") != 95161117118:
        e.append("replay identity drift")
    if rp.get("mode") != "isolated_family_comparator_not_All.lean" or rp.get("result") != "comparator_lean_kernel_nanoda_accept":
        e.append("replay mode/result drift")
    if rp.get("lean_version") != "4.32.0" or rp.get("lean_commit") != "8c9756b28d64dab099da31a4c09229a9e6a2ef35":
        e.append("Lean toolchain drift")
    if rp.get("permitted_axioms") != PERMITTED_AXIOMS:
        e.append("formal replay axiom drift")

    defs = r.get("definition_concordance", {})
    expected_keys = {"binary_surface", "spherical_code", "rate", "hierarchy", "localization", "numerical"}
    if set(defs) != expected_keys:
        e.append("definition concordance shape drift")
    required_by_field = {
        "binary_surface": ("0<delta<1/2", "R2<=kappa_bin<M2"),
        "spherical_code": ("inner product <=s", "s=cos(theta)", "0<s<1"),
        "rate": ("limsup", "log_2", "s=1/2"),
        "hierarchy": ("r=0", "Interlacing", "u(1+u)", "Gamma", "Phi", "2*Gamma>=s"),
        "localization": ("Icc 0 s", "strict_hierarchy"),
        "numerical": ("stronger", "0.39661+o(1)", "not"),
    }
    for field, tokens in required_by_field.items():
        text = defs.get(field, "")
        for token in tokens:
            if token not in text:
                e.append(f"definition concordance weakened: {field}/{token}")

    audits = r.get("target_audits", [])
    if len(audits) != 4:
        e.append("target audit count drift")
    else:
        if [x.get("target") for x in audits] != TARGETS:
            e.append("target audit inventory/order drift")
        if [x.get("classification") for x in audits] != CLASSIFICATIONS:
            e.append("target classification drift")
        required_target_tokens = [
            ("0<delta<1/2", "R2<=kappa_bin<M2"),
            ("Theorem 1.2", "eventual", "closed-hierarchy"),
            ("Corollary 1.3", "r>=0", "localized"),
            ("0.39661+o(1)", "does not print", "strictly stronger"),
        ]
        for item, tokens in zip(audits, required_target_tokens):
            text = item.get("source_relation", "") + "\n" + item.get("formal_relation", "")
            for token in tokens:
                if token not in text:
                    e.append(f"target relation evidence lost: {item.get('target')}/{token}")

    nv = r.get("nonvacuity", {})
    if nv.get("state") != "clear_for_successor_four_target_surface":
        e.append("nonvacuity state drift")
    nvtext = "\n".join(nv.get("evidence", []))
    for token in (
        "delta=1/4", "s=1/2", "singleton unit-vector code", "r=0",
        "a0=1", "Gamma=sqrt(2)/3", "2*sqrt(2)/3>1/2", "Icc 0 s",
        "atTop eventual quantifier",
    ):
        if token not in nvtext:
            e.append(f"nonvacuity evidence lost: {token}")

    ra = r.get("replay_and_axiom_audit", {})
    if ra.get("state") != "clear_as_source_root_replay_evidence":
        e.append("replay audit state drift")
    if ra.get("run_id") != 31945652355 or ra.get("job_id") != 95161117118:
        e.append("replay audit identity drift")
    if ra.get("permitted_axioms_only") != PERMITTED_AXIOMS:
        e.append("axiom audit drift")
    obs = "\n".join(ra.get("observations", []))
    for token in ("exactly the four successor target names", "MetricCodes solution module built successfully", "Nanoda kernel accepts", "Lean default kernel accepts", "Comparator returned ACCEPT"):
        if token not in obs:
            e.append(f"replay observation lost: {token}")
    if "does not independently certify proof correctness" not in ra.get("authority_limit", ""):
        e.append("replay authority limit weakened")

    ao = r.get("anti_overclaim", {})
    for key in (
        "predecessor_seven_target_authority_transferred",
        "numerical_target_source_printed_verbatim",
        "exact_039661_eventual_bound_claimed_as_manuscript_statement",
        "proof_bodies_compared_in_full",
        "proof_correctness_certified_here",
        "whole_chapter_semantic_equivalence",
        "solve_authority",
        "cert_authority",
        "mathematical_targets_marked_proved",
        "aggregate_ten_proofs_authority",
    ):
        if ao.get(key) is not False:
            e.append(f"anti-overclaim violated: {key}")

    d = r.get("disposition", {})
    if d.get("semantic_state") != "candidate_clear_pending_independent_review":
        e.append("candidate semantic disposition drift")
    if d.get("candidate_family_exit_state") != "SUCCESSOR_FOUR_TARGET_SURFACE__SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("candidate exit disposition drift")
    if d.get("solve_handoff_authorized") is not False or d.get("mathcert_route_authorized") is not False:
        e.append("downstream authority inflation in disposition")
    basis = d.get("basis", "")
    for token in ("four current targets", "Three are source-faithful", "stronger formal certificate", "0.39661+o(1)", "inhabited"):
        if token not in basis:
            e.append(f"disposition basis weakened: {token}")

    act = r.get("activation", {})
    for key in (
        "requires_exact_head_forge_ci",
        "requires_exact_head_gcl_conformance",
        "requires_exact_head_codeql",
        "requires_non_author_approved_review",
        "head_change_requires_reapproval",
        "streamlined_exact_head_binding_allowed_if_control_plan_unchanged",
        "material_control_plan_change_requires_renewed_steward_input",
        "effect_does_not_authorize_solve",
        "effect_does_not_authorize_cert",
    ):
        if act.get(key) is not True:
            e.append(f"activation gate weakened: {key}")

    rc = r.get("route_controls", {})
    for key in (
        "solve_handoff_authorized",
        "mathcert_route_authorized",
        "adjudication_authorized",
        "cert_output_authorized",
        "mathematical_target_proved",
        "aggregate_openai_ten_proofs_authority",
    ):
        if rc.get(key) is not False:
            e.append(f"route/authority inflation: {key}")

    boundary = r.get("claim_boundary", "")
    for token in (
        "four registered current-root OTP-B2-SPHERICAL-CODES targets",
        "predecessor seven-target drift",
        "formal strengthening",
        "0.39661+o(1)",
        "no MATHSOLVE handoff",
        "no aggregate OpenAI Ten Proofs authority",
    ):
        if token not in boundary:
            e.append(f"claim boundary missing token: {token}")

    return e


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated OTP-B2 Spherical Codes successor four-target semantic/nonvacuity candidate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
