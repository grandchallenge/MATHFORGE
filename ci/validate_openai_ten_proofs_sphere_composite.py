#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-A-SPHERE-PACKING-COMPOSITE/audit_record.json"

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
    "field_audit",
    "nonvacuity",
    "anti_overclaim",
    "disposition",
    "activation",
    "claim_boundary",
}

EXPECTED_FIELDS = {
    "root_before_infimum": ("source_proof_reformulation", "clear"),
    "root_before_infimum_vanishing_error": ("derived_error_normal_form", "clear"),
    "linear_program_root": ("direct_source_theorem_projection", "clear"),
    "natural_logarithmic_rate": ("derived_logarithmic_equivalent", "clear"),
    "natural_vanishing_exponential_error": ("derived_error_normal_form", "clear"),
    "universal_nonnegative_delta": ("source_lower_bound_projection_with_safe_normalization", "clear"),
    "base_two_exponent_positive": ("derived_elementary_consequence", "clear"),
    "base_two_decimal_certificate": ("derived_formal_numerical_certificate_not_source_precision", "clear_with_mandatory_label"),
    "base_two_logarithmic_rate": ("displayed_source_consequence", "clear"),
    "base_two_vanishing_exponential_error": ("derived_error_normal_form_of_displayed_source_consequence", "clear"),
}


def load(path: Path = RECORD):
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record=None):
    r = load() if record is None else record
    e: list[str] = []

    if set(r) != EXPECTED_TOP:
        e.append("top-level record shape drift")
    if r.get("schema_version") != "1.0.0":
        e.append("schema version drift")
    if r.get("record_id") != "MF-OTP-A-SPHERE-PACKING-COMPOSITE-SEMANTIC-002":
        e.append("record id drift")
    if r.get("candidate_id") != "OPENAI-TEN-PROOFS-001" or r.get("result_family") != "OTP-A-SPHERE-PACKING":
        e.append("candidate/family drift")
    if r.get("audit_scope") != "PackingBounds.sharpFullCohnElkiesManuscriptConclusions only":
        e.append("audit scope inflation")

    g = r.get("governance", {})
    if g.get("tracker_issue") != 89:
        e.append("tracker drift")
    if g.get("protected_base") != "275f435eaf519ada3f0afa4bf8e77cfd0c8fcbb3":
        e.append("protected base drift")
    if g.get("publication_state") != "candidate_until_protected_merge":
        e.append("pre-activation publication inflation")

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
    for token in ("Theorem 1.1", "Theorem 3.8", "Equation (31)", "Equations (85)-(86)"):
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
    if f.get("target") != "PackingBounds.sharpFullCohnElkiesManuscriptConclusions":
        e.append("target drift")
    if f.get("isolated_replay") != "comparator_lean_kernel_nanoda_accept":
        e.append("replay state drift")
    if f.get("permitted_axioms") != ["propext", "Classical.choice", "Quot.sound"]:
        e.append("permitted axiom drift")

    defs = r.get("definition_concordance", [])
    if len(defs) != 4 or [x.get("status") for x in defs] != ["equivalent", "exact", "exact", "proved_equivalence"]:
        e.append("definition concordance drift")

    fields = r.get("field_audit", [])
    by_name = {x.get("field"): x for x in fields}
    if len(fields) != 10 or set(by_name) != set(EXPECTED_FIELDS):
        e.append("ten-field inventory drift")
    for name, (classification, status) in EXPECTED_FIELDS.items():
        item = by_name.get(name, {})
        if item.get("classification") != classification:
            e.append(f"classification drift: {name}")
        if item.get("status") != status:
            e.append(f"status drift: {name}")
        if not item.get("source_locus") or not item.get("lean_dependency") or not item.get("analysis"):
            e.append(f"missing field evidence: {name}")

    root_analysis = by_name.get("root_before_infimum", {}).get("analysis", "")
    if "not the Fourier sign-uncertainty Theorem 1.2" not in root_analysis:
        e.append("Theorem 1.2 anti-conflation lost")
    delta_analysis = by_name.get("universal_nonnegative_delta", {}).get("analysis", "")
    if "No claim that the source itself states epsilon_d>=0" not in delta_analysis:
        e.append("source epsilon sign overclaim protection lost")
    decimal_analysis = by_name.get("base_two_decimal_certificate", {}).get("analysis", "")
    if "not printed in the manuscript" not in decimal_analysis or "checked mathematical consequence" not in decimal_analysis:
        e.append("decimal provenance qualification lost")

    nv = r.get("nonvacuity", {})
    if nv.get("state") != "clear_for_composite_surface":
        e.append("composite nonvacuity lost")
    evidence = nv.get("evidence", [])
    for token in ("admissible_nonempty", "radialToFull", "fullQuotientSet_eq_radial", "eventually_linearProgram_pos"):
        if not any(token in x for x in evidence):
            e.append(f"nonvacuity evidence lost: {token}")
    if "does not by itself close" not in nv.get("scope_note", ""):
        e.append("packing-bridge nonvacuity boundary lost")

    a = r.get("anti_overclaim", {})
    if a.get("theorem_1_2_used_for_any_field") is not False:
        e.append("Theorem 1.2 false attribution")
    if a.get("decimal_precision_source_authored") is not False:
        e.append("decimal source-authorship inflation")
    if a.get("composite_is_verbatim_single_source_theorem") is not False:
        e.append("single-theorem inflation")
    if a.get("composite_kind") != "mixed_source_projection_and_checked_derived_consequence":
        e.append("composite kind drift")
    for key in (
        "proof_correctness_certified_here",
        "whole_chapter_equivalence",
        "whole_family_semantic_clearance",
        "solve_authority",
        "cert_authority",
        "aggregate_ten_proofs_authority",
    ):
        if a.get(key) is not False:
            e.append(f"prohibited authority: {key}")

    d = r.get("disposition", {})
    if d.get("target_semantic_state") != "candidate_clear_pending_independent_review":
        e.append("target activation inflation")
    if d.get("target_classification") != "source_faithful_derived_composite_certificate":
        e.append("target classification drift")
    if d.get("all_ten_fields_accounted_for") is not True:
        e.append("ten-field completeness lost")
    if d.get("rejected_fields") != []:
        e.append("rejected-field disposition drift")
    if d.get("qualified_fields") != ["base_two_decimal_certificate"]:
        e.append("qualified-field boundary drift")
    if "not as manuscript-authored decimal precision" not in d.get("qualification", ""):
        e.append("decimal disposition qualification lost")
    if d.get("family_state_after_activation") != "SEMANTIC_PARTIAL__COMPOSITE_CLEAR_PACKING_BRIDGE_NORMALIZATION_REMAINS":
        e.append("family residual-blocker drift")

    act = r.get("activation", {})
    condition = act.get("condition", "")
    if "protected merge" not in condition or "exact-head CI" not in condition or "non-author specialist APPROVED review" not in condition:
        e.append("activation gate weakened")
    if act.get("effect") != "semantic and nonvacuity clearance for PackingBounds.sharpFullCohnElkiesManuscriptConclusions only":
        e.append("activation effect inflation")
    if act.get("effect_is_retroactive") is not False or act.get("head_change_requires_reapproval") is not True:
        e.append("activation/reapproval semantics drift")

    boundary = r.get("claim_boundary", "")
    for token in (
        "does not certify proof correctness",
        "does not assert that the ten fields form one manuscript theorem",
        "does not attribute the 30-decimal certificate to the source text",
        "does not close the separate packing-density bridge target",
        "does not create a Solve or Cert route",
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
    print("OTP-A Sphere composite semantic audit validates fail-closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
