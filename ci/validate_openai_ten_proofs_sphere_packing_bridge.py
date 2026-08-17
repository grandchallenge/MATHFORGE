#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-A-SPHERE-PACKING-BRIDGE/audit_record.json"

EXPECTED_TOP = {
    "schema_version",
    "record_id",
    "candidate_id",
    "result_family",
    "audit_scope",
    "governance",
    "source_authority",
    "formal_authority",
    "definition_concordance",
    "target_dependency",
    "nonvacuity",
    "replay_and_axiom_audit",
    "anti_overclaim",
    "disposition",
    "activation",
    "route_controls",
    "claim_boundary",
}

EXPECTED_DEF_STATUSES = [
    "exact_after_unit_separation_restriction",
    "definitionally_concordant_upper_density_realization",
    "proved_normalization_equivalence",
    "proved_exact_normalization",
]


def load(path: Path = RECORD):
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record=None):
    r = load() if record is None else record
    e: list[str] = []

    if set(r) != EXPECTED_TOP:
        e.append("top-level record shape drift")
    if r.get("schema_version") != "1.0.0":
        e.append("schema version drift")
    if r.get("record_id") != "MF-OTP-A-SPHERE-PACKING-BRIDGE-SEMANTIC-003":
        e.append("record id drift")
    if r.get("candidate_id") != "OPENAI-TEN-PROOFS-001" or r.get("result_family") != "OTP-A-SPHERE-PACKING":
        e.append("candidate/family drift")
    if r.get("audit_scope") != "PackingBounds.PackingBridge.sphere_packing_sharp_asymptotic_upper only":
        e.append("audit scope inflation")

    g = r.get("governance", {})
    if g.get("tracker_issue") != 89:
        e.append("tracker drift")
    if g.get("protected_base") != "706d0291370bf3f14aa37be0823e33d06f7343b0":
        e.append("protected base drift")
    if g.get("publication_state") != "candidate_until_protected_merge":
        e.append("pre-activation publication inflation")
    if "residual packing-density normalization surface" not in g.get("history_policy", ""):
        e.append("successor scope/history boundary lost")

    s = r.get("source_authority", {})
    if s.get("revision") != "2026-08-06":
        e.append("source revision drift")
    if s.get("pdf_sha256") != "ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566":
        e.append("source digest drift")
    if s.get("pdf_byte_length") != 2487031:
        e.append("source length drift")
    if s.get("pdf_successor_record_blob") != "02d1748abed36717afba46451330be165c076737":
        e.append("source successor record drift")
    if s.get("pdf_successor_protected_merge") != "275f435eaf519ada3f0afa4bf8e77cfd0c8fcbb3":
        e.append("source successor merge drift")
    if s.get("chapter") != 1:
        e.append("source chapter drift")
    loci = s.get("loci", [])
    for token in ("Delta_d", "Equation (4)", "Theorem 1.1", "displayed consequence"):
        if not any(token in x for x in loci):
            e.append(f"missing source locus: {token}")

    f = r.get("formal_authority", {})
    if f.get("repository") != "openai/ten-proofs":
        e.append("formal repository drift")
    if f.get("root") != "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6":
        e.append("formal root drift")
    if f.get("tree") != "174289e4d4958cb0509874e6e53400e098213de7":
        e.append("formal tree drift")
    if f.get("formal_successor_record_blob") != "6993ce9fac2c65ffae7f2a0c7d728aab828ed532":
        e.append("formal successor drift")
    if f.get("config", {}).get("blob") != "46b2e7b49da43fb17a7efa88652f8ee1adc01cbe":
        e.append("config blob drift")
    if f.get("challenge", {}).get("blob") != "2477846e1883534837340c636fd928b091509783":
        e.append("challenge blob drift")
    if f.get("solution", {}).get("blob") != "e6117934a80142a8249356fdafa797eba030e920" or f.get("solution", {}).get("byte_length") != 2096663:
        e.append("solution carrier drift")
    if f.get("target") != "PackingBounds.PackingBridge.sphere_packing_sharp_asymptotic_upper":
        e.append("target drift")
    replay = f.get("isolated_replay", {})
    if replay.get("run_id") != 31945652355 or replay.get("job_id") != 95161117046:
        e.append("replay identity drift")
    if replay.get("result") != "comparator_lean_kernel_nanoda_accept" or replay.get("exported_target_present") is not True:
        e.append("replay result drift")
    if replay.get("lean_version") != "4.32.0" or replay.get("lean_commit") != "8c9756b28d64dab099da31a4c09229a9e6a2ef35":
        e.append("Lean toolchain drift")
    if f.get("permitted_axioms") != ["propext", "Classical.choice", "Quot.sound"]:
        e.append("permitted axiom drift")

    defs = r.get("definition_concordance", [])
    if len(defs) != 4 or [x.get("status") for x in defs] != EXPECTED_DEF_STATUSES:
        e.append("definition concordance drift")
    joined = "\n".join(x.get("analysis", "") for x in defs)
    for token in ("separation 1", "radius-1/2", "limsup", "rescale_upper_packing_density", "packing_supremum_eq_unit_separation", "volume_half_ball"):
        if token not in joined:
            e.append(f"normalization evidence lost: {token}")
    if "No claim is made that the manuscript prints this implementation formula verbatim" not in joined:
        e.append("upper-density implementation qualification lost")

    dep = r.get("target_dependency", {})
    if dep.get("classification") != "source_faithful_displayed_consequence_with_proved_scale_normalization":
        e.append("target dependency classification drift")
    source_chain = dep.get("source_chain", [])
    for token in ("Equation (4)", "Theorem 1.1", "displayed"):
        if not any(token in x for x in source_chain):
            e.append(f"source dependency lost: {token}")
    lean_chain = dep.get("lean_chain", [])
    for token in ("packing_supremum_eq_unit_separation", "sphere_packing_le_admissible", "sphere_packing_le_radial_linear_program_ennreal", "exists_manuscriptPackingIsLittleO", "sphere_packing_sharp_asymptotic_upper"):
        if not any(token in x for x in lean_chain):
            e.append(f"Lean dependency lost: {token}")
    note = dep.get("normal_form_note", "")
    if "explicit function e" not in note or "not a stronger asymptotic rate claim" not in note:
        e.append("little-o normal-form qualification lost")

    nv = r.get("nonvacuity", {})
    if nv.get("state") != "clear_for_packing_bridge_surface":
        e.append("bridge nonvacuity lost")
    evidence = nv.get("evidence", [])
    for token in ("singleton center set", "upper_packing_density_le_one", "admissible_nonempty", "0 < d"):
        if not any(token in x for x in evidence):
            e.append(f"nonvacuity evidence lost: {token}")
    if "does not certify the mathematical proof" not in nv.get("scope_note", ""):
        e.append("nonvacuity authority boundary lost")

    ra = r.get("replay_and_axiom_audit", {})
    if ra.get("state") != "clear_as_source_root_replay_evidence":
        e.append("replay evidence classification drift")
    if ra.get("run_id") != 31945652355 or ra.get("job_id") != 95161117046:
        e.append("replay audit identity drift")
    obs = ra.get("observations", [])
    for token in ("exact source root", "exact target", "Nanoda kernel accepted", "Lean default kernel accepted", "Comparator returned ACCEPT"):
        if not any(token in x for x in obs):
            e.append(f"replay observation lost: {token}")
    if ra.get("permitted_axioms_only") != ["propext", "Classical.choice", "Quot.sound"]:
        e.append("replay axiom boundary drift")
    if "does not convert it into independent proof certification" not in ra.get("authority_limit", ""):
        e.append("replay authority limit weakened")

    a = r.get("anti_overclaim", {})
    if a.get("sphere_packing_constant_is_declared_alias_for_delta_d") is not False:
        e.append("Delta alias inflation")
    if "proved scale-normalization theorem" not in a.get("reason", ""):
        e.append("normalization proof rationale lost")
    for key in (
        "source_prints_formal_upper_density_implementation",
        "source_prints_explicit_error_function",
        "proof_correctness_certified_here",
        "whole_chapter_equivalence",
        "solve_authority",
        "cert_authority",
        "mathematical_target_marked_proved",
        "aggregate_ten_proofs_authority",
    ):
        if a.get(key) is not False:
            e.append(f"prohibited authority: {key}")

    d = r.get("disposition", {})
    if d.get("target_semantic_state") != "candidate_clear_pending_independent_review":
        e.append("target activation inflation")
    if d.get("target_classification") != "source_faithful_displayed_consequence_with_proved_scale_normalization":
        e.append("target classification drift")
    if d.get("normalization_blocker_resolved") is not True or d.get("nonvacuity_clear") is not True:
        e.append("candidate finding drift")
    if d.get("candidate_family_disposition") != "SPHERE_PACKING_CURRENT_ROOT__SEMANTIC_AND_NONVACUITY_CLEAR__SOLVE_HANDOFF_NOT_AUTHORIZED":
        e.append("candidate family disposition drift")

    act = r.get("activation", {})
    for key in (
        "requires_exact_head_forge_ci",
        "requires_exact_head_gcl_conformance",
        "requires_exact_head_codeql",
        "requires_non_author_approved_review",
        "requires_human_steward_disposition",
        "head_change_requires_reapproval",
        "effect_does_not_authorize_solve",
        "effect_does_not_authorize_cert",
    ):
        if act.get(key) is not True:
            e.append(f"activation gate weakened: {key}")
    effect = act.get("effect", "")
    if "already protected ten-field composite" not in effect or "closes the current-root MATHFORGE semantic audit" not in effect:
        e.append("activation effect drift")

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
            e.append(f"route authority inflation: {key}")

    boundary = r.get("claim_boundary", "")
    for token in (
        "proved scale invariance",
        "does not certify proof correctness independently of MATHCERT",
        "does not assert verbatim source/formal implementation identity",
        "does not create a Solve or Cert route",
        "does not mark the mathematical target proved",
        "no aggregate OpenAI Ten Proofs authority",
    ):
        if token not in boundary:
            e.append(f"claim boundary weakened: {token}")

    return e


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("OTP-A Sphere packing-density bridge semantic audit validates fail-closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
