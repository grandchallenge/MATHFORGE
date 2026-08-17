#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-H-GAPCVP/audit_record.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_gapcvp_semantic.schema.json"

TARGETS = [
    "GapCVP.Comparator.gapCVP400IsNPHard",
    "GapCVP.Comparator.binaryNearestCodewordIsNPHard",
    "GapCVP.Comparator.binarySyndromeDecodingIsNPHard",
    "GapCVP.Comparator.finitePNormGapCVPIsNPHard",
]
PROMISES = [
    "GapCVP.Comparator.gapCVP400Promise",
    "GapCVP.Comparator.binaryNearestCodewordPromise",
    "GapCVP.Comparator.binarySyndromeDecodingPromise",
    "GapCVP.Comparator.finitePGapCVPPromise",
]
CLASSIFICATIONS = [
    "source_faithful_restricted_consequence_integer_target",
    "source_faithful_up_to_generator_orientation",
    "source_faithful_restricted_consequence_consistent_syndrome",
    "source_faithful_fixed_rational_p_consequence",
]
FACTORS = ["n^(1/400)", "n^(1/200)", "n^(1/200)", "n^(1/(200p))"]
FORMAL_FACTORS = [
    "dimension^(1/400)",
    "blockLength^(1/200)",
    "blockLength^(1/200)",
    "dimension^((200*p)^(-1))",
]


def load_record(path: Path = RECORD):
    return json.loads(path.read_text(encoding="utf-8"))


def load_schema(path: Path = SCHEMA):
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record=None, schema=None):
    r = load_record() if record is None else record
    s = load_schema() if schema is None else schema
    e: list[str] = []

    for err in sorted(Draft202012Validator(s).iter_errors(r), key=lambda x: list(x.path)):
        e.append(f"schema: {err.message}")

    g = r.get("governance", {})
    if g.get("tracker_issue") != 90:
        e.append("tracker drift")
    if g.get("protected_base") != "706d0291370bf3f14aa37be0823e33d06f7343b0":
        e.append("protected base drift")
    if g.get("publication_state") != "candidate_until_protected_merge":
        e.append("pre-activation promotion")
    if g.get("candidate_exit_state") != "PROMISE_INTERFACES_CLOSED__SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("candidate exit-state drift")
    if g.get("head_change_requires_reapproval") is not True:
        e.append("head-change reapproval removed")

    src = r.get("source_authority", {})
    exact_source = {
        "revision": "2026-08-06",
        "pdf_sha256": "ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566",
        "pdf_byte_length": 2487031,
        "pdf_successor_record_blob": "02d1748abed36717afba46451330be165c076737",
        "pdf_successor_protected_merge": "275f435eaf519ada3f0afa4bf8e77cfd0c8fcbb3",
        "chapter": 7,
    }
    for key, value in exact_source.items():
        if src.get(key) != value:
            e.append(f"source authority drift: {key}")
    loci = "\n".join(src.get("loci", []))
    for token in ("intermediate region outside the promise", "integer target", "n^(1/400)", "n^(1/200)", "fixed rational p>=1", "n^(1/(200p))"):
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
    if f.get("config") != {"path": "ComparatorChallenges/H_GapCVP.json", "blob": "fdba0e774acc6c2bd6fd450ee155975c0eda1833"}:
        e.append("config identity drift")
    if f.get("challenge") != {"path": "ComparatorChallenges/H_GapCVP.lean", "blob": "770e202350a5c94d3f6516428ff01092cb8f8cb4"}:
        e.append("challenge identity drift")
    sol = f.get("solution", {})
    if sol.get("path") != "GapCVP.lean" or sol.get("blob") != "47f3a395e4d9ec3e2892664860f26ed63421b0c9" or sol.get("byte_length") != 5335203:
        e.append("solution identity drift")
    if f.get("targets") != TARGETS:
        e.append("target inventory drift")
    if f.get("promise_definitions") != PROMISES:
        e.append("promise inventory drift")
    rp = f.get("replay", {})
    if rp.get("run_id") != 31945652355 or rp.get("job_id") != 95161117067:
        e.append("replay identity drift")
    if rp.get("result") != "comparator_lean_kernel_nanoda_accept":
        e.append("replay result drift")
    if rp.get("lean_version") != "4.32.0" or rp.get("lean_commit") != "8c9756b28d64dab099da31a4c09229a9e6a2ef35":
        e.append("Lean toolchain drift")
    if rp.get("exported_target_count") != 4 or rp.get("exported_promise_definition_count") != 4:
        e.append("replay export-count drift")
    if rp.get("permitted_axioms") != ["propext", "Classical.choice", "Quot.sound"]:
        e.append("replay axiom drift")

    mm = r.get("machine_model", {})
    if mm.get("bit_tm_definition") != "GapCVP.BitTM map := Turing.TM2ComputableInPolyTime bitEncoding bitEncoding map":
        e.append("BitTM definition drift")
    if mm.get("mathlib_commit") != "81a5d257c8e410db227a6665ed08f64fea08e997":
        e.append("mathlib commit drift")
    if mm.get("mathlib_path") != "Mathlib/Computability/TuringMachine/Computable.lean" or mm.get("mathlib_blob") != "7779a00f0c3c3909923a5f1bde6b3120b5c2d28a":
        e.append("mathlib machine-model file drift")
    if mm.get("classification") != "deterministic_polynomial_time_machine_witness":
        e.append("machine-model classification drift")
    mm_text = mm.get("analysis", "") + "\n" + mm.get("trust_boundary", "")
    for token in ("finite deterministic TM2", "polynomial time", "every encoded input", "constant factor", "does not independently certify"):
        if token not in mm_text:
            e.append(f"machine-model qualification lost: {token}")

    rs = r.get("reduction_semantics", {})
    if rs.get("classification") != "deterministic_polynomial_time_many_one_promise_hardness":
        e.append("reduction classification drift")
    if rs.get("direction_matches_source") is not True:
        e.append("reduction direction drift")
    if rs.get("search_decision_conflated") is not False:
        e.append("search/decision conflation")
    if rs.get("malformed_input_policy") != "outside_promise":
        e.append("malformed-input promotion")
    if rs.get("intermediate_threshold_policy") != "outside_promise":
        e.append("intermediate-threshold promotion")
    red_text = "\n".join(str(rs.get(k, "")) for k in rs)
    for token in ("total List Bool -> List Bool map", "language-true inputs map to YES", "language-false inputs map to NO", "exact encoded instance", "four PromiseProblem.disjoint", "not independent proof certification"):
        if token not in red_text:
            e.append(f"reduction semantic evidence lost: {token}")

    audits = r.get("target_audits", [])
    if len(audits) != 4:
        e.append("target audit count drift")
    else:
        if [x.get("target") for x in audits] != TARGETS:
            e.append("target audit ordering/inventory drift")
        if [x.get("promise") for x in audits] != PROMISES:
            e.append("promise mapping drift")
        if [x.get("classification") for x in audits] != CLASSIFICATIONS:
            e.append("target classification drift")
        if [x.get("source_factor") for x in audits] != FACTORS or [x.get("formal_factor") for x in audits] != FORMAL_FACTORS:
            e.append("approximation-factor drift")

        eu = audits[0]
        if eu.get("norm") != "Euclidean l2" or "integer-target output surface" not in eu.get("qualification", ""):
            e.append("Euclidean restriction/norm drift")
        if "rational targets" not in eu.get("qualification", "") or "not an assertion of whole-problem interface identity" not in eu.get("qualification", ""):
            e.append("Euclidean generality qualification lost")

        near = audits[1]
        if near.get("norm") != "Hamming distance over ZMod 2" or "transpose/orientation convention" not in near.get("qualification", ""):
            e.append("nearest-codeword representation drift")

        syn = audits[2]
        if syn.get("norm") != "Hamming weight over ZMod 2" or "formal NO side requires at least one solution" not in syn.get("qualification", ""):
            e.append("syndrome consistency qualification lost")
        if "rather than a whole-interface identity claim" not in syn.get("qualification", ""):
            e.append("syndrome scope qualification lost")

        fp = audits[3]
        if fp.get("norm") != "finite l_p" or "external to the input encoding" not in fp.get("qualification", "") or "fixed independently" not in fp.get("qualification", ""):
            e.append("finite-p fixed-parameter qualification lost")

        for idx, a in enumerate(audits):
            if not a.get("nonvacuity_yes") or not a.get("nonvacuity_no"):
                e.append(f"vacuous target audit: {idx}")
        witness_text = "\n".join(a.get("nonvacuity_yes", "") + "\n" + a.get("nonvacuity_no", "") for a in audits)
        for token in ("B=(1)", "B=(2)", "zero code", "C={00}", "H=[0]", "H=I_2", "every fixed finite p>=1"):
            if token not in witness_text:
                e.append(f"nonvacuity witness lost: {token}")

    pt = r.get("parameter_transport", {})
    if pt.get("euclidean_dimension") != "formal dimension equals source lattice dimension n":
        e.append("Euclidean dimension transport drift")
    if pt.get("binary_length") != "formal blockLength equals source binary block length n":
        e.append("binary length transport drift")
    if pt.get("finite_p_scope") != "p is fixed rational >=1 and is not part of the input bits":
        e.append("finite-p scope drift")
    if "squared distances" not in pt.get("squared_distance_note", "") or "without reversing strictness" not in pt.get("squared_distance_note", ""):
        e.append("squared-distance threshold equivalence lost")
    if pt.get("factor_drift_prohibited") is not True or pt.get("constant_400_interpretation_prohibited") is not True:
        e.append("factor guard weakened")

    nv = r.get("nonvacuity", {})
    if nv.get("state") != "clear_all_four_promise_interfaces":
        e.append("nonvacuity state drift")
    if nv.get("yes_witness_count") != 4 or nv.get("no_witness_count") != 4:
        e.append("nonvacuity witness-count drift")
    for key in ("all_yes_sides_inhabited", "all_no_sides_inhabited", "vacuous_hardness_inference_prohibited"):
        if nv.get(key) is not True:
            e.append(f"nonvacuity guard weakened: {key}")
    if "does not by itself prove NP-hardness" not in nv.get("scope_note", ""):
        e.append("nonvacuity authority qualification lost")

    ra = r.get("replay_and_axiom_audit", {})
    if ra.get("state") != "clear_as_source_root_replay_evidence" or ra.get("run_id") != 31945652355 or ra.get("job_id") != 95161117067:
        e.append("replay audit state/identity drift")
    obs = "\n".join(ra.get("observations", []))
    for token in ("exact formal root", "all four target theorem names", "GapCVP solution module built successfully", "Nanoda kernel accepts", "Lean default kernel accepts", "Comparator returned ACCEPT"):
        if token not in obs:
            e.append(f"replay observation lost: {token}")
    if ra.get("permitted_axioms_only") != ["propext", "Classical.choice", "Quot.sound"]:
        e.append("axiom audit drift")
    if "does not independently certify proof correctness" not in ra.get("authority_limit", ""):
        e.append("replay authority limit weakened")

    ao = r.get("anti_overclaim", {})
    required_false = [
        "whole_source_gapcvp_interface_identical",
        "euclidean_rational_target_generality_claimed",
        "syndrome_all_syntactic_instances_claimed",
        "binary_generator_orientation_printed_identically",
        "malformed_inputs_promoted_to_no",
        "intermediate_inputs_promoted_to_no",
        "search_problem_equated_with_decision_promise",
        "constant_factor_400_claimed",
        "proof_correctness_certified_here",
        "solve_authority",
        "cert_authority",
        "mathematical_targets_marked_proved",
        "aggregate_ten_proofs_authority",
    ]
    for key in required_false:
        if ao.get(key) is not False:
            e.append(f"anti-overclaim violated: {key}")

    d = r.get("disposition", {})
    if d.get("semantic_state") != "candidate_clear_pending_independent_review":
        e.append("pre-review semantic activation")
    if d.get("candidate_family_exit_state") != "PROMISE_INTERFACES_CLOSED__SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("family exit-state drift")
    basis = d.get("basis", "")
    for token in ("all four current-root target statements", "actual pinned deterministic TM model", "outside the promise", "integer-target", "syndrome-consistency", "explicit YES and NO witnesses"):
        if token not in basis:
            e.append(f"disposition basis weakened: {token}")
    if d.get("solve_handoff_authorized") is not False or d.get("mathcert_route_authorized") is not False:
        e.append("premature downstream authority in disposition")

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
    if "four registered OTP-H-GAPCVP targets only" not in act.get("effect", ""):
        e.append("activation scope inflation")

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
            e.append(f"route-control inflation: {key}")

    boundary = r.get("claim_boundary", "")
    for token in (
        "integer-target output surface",
        "consistent syndrome systems",
        "malformed and threshold-intermediate bitstrings remain outside the promise",
        "no Solve or MATHCERT route",
        "would not independently certify proof correctness",
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
    print("OTP-H GapCVP current-root semantic audit validates fail-closed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
