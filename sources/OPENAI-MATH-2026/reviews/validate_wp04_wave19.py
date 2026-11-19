#!/usr/bin/env python3
"""WP04 adversarial wave integrity, explicit negative controls, and source scope.

This validates case coverage and safe semantic verdicts, not mathematical proofs.
"""
import copy
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
BASE = ROOT / "sources" / "OPENAI-MATH-2026"
SOURCE = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
LEDGER = BASE / "reviews" / "WP04_ADVERSARIAL_WAVE16_LEDGER.json"
PREFIX = "GCL-OAI26-WP04-ADVERSARY-v1|" + SOURCE + "|"
MANDATORY = {"revision": 3, "formal": 3, "unfamiliar": 3, "random_baseline": 3}
FORBIDDEN_PROMOTIONS = ("FULL_SEMANTIC_MATCH_PROVED", "CERTIFIED", "MATHCERT_PASS")

def must(value, reason):
    if not value:
        raise AssertionError(reason)

def check(data):
    idx = json.loads((BASE / "MANUSCRIPT_INDEX.json").read_text())
    must(data["source_commit"] == SOURCE, "source revision moved")
    must(data["schema"] == "GCL-OAI26-WP04-ADVERSARIAL-WAVE19/1", "wrong schema")
    must(len(idx["families"]) == 372, "source denominator moved")
    must(sum(len(f["manuscripts"]) for f in idx["families"]) == 719, "edition denominator moved")
    families = {x["family_id"] for x in idx["families"]}
    records = data["cases"]
    ids = [x["family_id"] for x in records]
    must(len(records) == 19 and len(set(ids)) == 19, "missing or duplicate family")
    must(ids == sorted(ids), "case ordering unstable")
    must(set(ids).issubset(families), "unknown family")
    must(data["case_count"] == 19 and data["distinct_family_count"] == 19, "false counts")
    must(data["claim_boundary"] == "NO_MATHCERT_CERTIFICATION", "scope inflation")
    for x in records:
        must(x["certification"] == "NO_CERTIFICATION", "certification promoted " + x["family_id"])
        must(x["independently_authenticated_review"] is False, "fictitious independent reviewer")
        must(x["review_role"] == "NON_AUTHORING_READ_ONLY_LOGICAL_CRITIC", "role attribution changed")
        must(bool(x["source_evidence"]), "missing source evidence " + x["family_id"])
        must(bool(x["hostile_test"]) and bool(x["next_proof_obligation"]), "no adversary/obligation " + x["family_id"])
        must(not any(s in x["disposition"] for s in FORBIDDEN_PROMOTIONS), "unsupported promotion")
        for p in x["source_evidence"]:
            target = ROOT / p
            must(target.is_file(), "unavailable protected source evidence " + str(p))
    sel = data["selection"]
    for key, threshold in MANDATORY.items():
        got = [x for x in records if key in x["categories"]]
        must(len(got) >= threshold, "selection undersampled: "+key)
    excluded = {int(x) for x in ids if x not in sel["random_baseline"]}
    ranks = sorted((hashlib.sha256((PREFIX + f"{n:03d}").encode()).hexdigest(), f"{n:03d}")
                   for n in range(1, 373) if n not in excluded)
    expected = [f for _, f in ranks[:3]]
    must(sel["random_baseline"] == expected, "seeded sample changed after seeing outcome")
    must(sel["random_baseline_ordered_sha256"] == [x[0] for x in ranks[:3]], "seed hash changed")
    byid = {x["family_id"]: x for x in records}
    must(byid["342"]["disposition"] == "SEMANTIC_MISMATCH__SUPERSEDED_CONE_CLAIM",
         "withdrawn unconditional cone equation improperly promoted")
    must("h^-_J=b²_+(X)-1" in byid["342"]["source_observation"], "cone assumption omitted")
    must(byid["006"]["disposition"] == "UNRESOLVED__HIGH_RANK_TAIL_REQUIRED",
         "density promoted to a mean-rank theorem without exceptional tail")
    must(byid["095"]["disposition"] == "UNRESOLVED__DIFFERENT_CONES_AND_LIFT_CLASSES",
         "spectrahedron vs spectrahedral shadow conflation")
    must(byid["008"]["disposition"].startswith("VERIFIED_WITHIN_EXPLICIT_SCOPE"),
         "exact admitted theorem replay improperly discarded or overextended")
    must("MATHCERT" not in byid["008"]["disposition"], "F008 promotion without authorization")
    must(data["withdrawal_protection"]["current_certification_allowed"] is False,
         "publisher withdrawals no longer quarantined")
    return ids

def hostile(data, family, verdict):
    corrupted = copy.deepcopy(data)
    next(x for x in corrupted["cases"] if x["family_id"] == family)["disposition"] = verdict
    try:
        check(corrupted)
    except AssertionError:
        print("HOSTILE_SEMANTIC_ROLLBACK_PASS", family)
    else:
        raise AssertionError("hostile verdict escaped: " + family)

def main():
    ledger = json.loads(LEDGER.read_text())
    ids = check(ledger)
    for fid, verdict in [
        ("342", "VERIFIED_WITHIN_EXPLICIT_SCOPE__UNCONDITIONAL_CONE_EQUALITY"),
        ("006", "VERIFIED_WITHIN_EXPLICIT_SCOPE__MEAN_FROM_DENSITY"),
        ("095", "CONTRADICTED__ALL_CONES_NONLIFTABLE"),
        ("008", "MATHCERT_PASS"),
    ]:
        hostile(ledger, fid, verdict)
    print("WP04_WAVE19_SEMANTIC_VALIDATOR_PASS", len(ids),
          "distinct families; 3 seeded baseline; 4 hostile rollbacks; zero certification")

if __name__ == "__main__":
    try:
        main()
    except (OSError, KeyError, ValueError, AssertionError) as exc:
        print("WP04_WAVE19_VALIDATION_FAIL", exc, file=sys.stderr)
        raise SystemExit(1)
