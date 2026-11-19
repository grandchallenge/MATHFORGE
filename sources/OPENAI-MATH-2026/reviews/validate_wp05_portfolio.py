#!/usr/bin/env python3
"""Rebuild and aggressively verify OAI-26 WP05 source-bound portfolio.

A PASS means evidence bookkeeping and noninflation, NOT theorem certification.
"""
import copy
import hashlib
import json
import pathlib
import sys
from collections import Counter

from build_wp05_portfolio import build, OUT, BASE, SOURCE, IMPORT_BASE, INPUT_BLOBS

EXPECTED_CATALOGUE = 372
EXPECTED_PATHS = 719
EXPECTED_FORMAL = 200
EXPECTED_PUBLISHER = 300
EXPECTED_CLASSES = {
    "VERIFIED_WITHIN_EXPLICIT_SCOPE":1,
    "UNRESOLVED":24,
    "INSUFFICIENT_EVIDENCE":347
}
EXPECTED_F008_RECEIPTS = (
    44298907335, 14425447501, 44304148849, 14428700812,
    "4dcf6e4ac49bed6c61b05980ca17036a78d5e894"
)

def require(ok, message):
    if not ok:
        raise AssertionError(message)

def validate(d):
    index=json.loads((BASE/"MANUSCRIPT_INDEX.json").read_text())
    cross=json.loads((BASE/"FORMALIZATION_CROSSWALK.json").read_text())
    wp03=json.loads((BASE/"reviews/WP03_PILOT12_EVIDENCE_LEDGER.json").read_text())
    wp04=json.loads((BASE/"reviews/WP04_ADVERSARIAL_WAVE16_LEDGER.json").read_text())
    risk=json.loads((BASE/"WP02_CANONICAL_3_14_13_RISK_REGISTER.json").read_text())
    require(d["schema"]=="GCL-OAI26-WP05-CANONICAL-372/1", "schema drift")
    require(d["source_lock"]["commit"]==SOURCE, "source revision changed")
    require(d["imported_protected_evidence_head"]==IMPORT_BASE, "evidence import head changed")
    require(d["catalogue"]["families"]==EXPECTED_CATALOGUE, "family denominator")
    require(d["catalogue"]["manuscript_paths"]==EXPECTED_PATHS, "manuscript denominator")
    require(d["catalogue"]["crosswalk_distinct_declarations"]==EXPECTED_FORMAL, "formal denominator")
    require(d["catalogue"]["publisher_top_line_claims"]==EXPECTED_PUBLISHER, "publisher denominator")
    require(d["input_git_blob_sha1_locks"] == INPUT_BLOBS,
            "source input blob-lock ledger changed")
    for relative, expected in INPUT_BLOBS.items():
        raw = (BASE / relative).read_bytes()
        actual = hashlib.sha1(b"blob " + str(len(raw)).encode() + bytes([0]) + raw).hexdigest()
        require(actual == expected, "exact pinned input mutated " + relative)
    require(len(index["families"])==EXPECTED_CATALOGUE, "source family count drift")
    require(len(cross["main_results"])==EXPECTED_FORMAL, "source declaration count drift")
    require(len(cross["source_papers"])==173, "source paper count drift")
    require(len(wp03["families"])==12 and len(wp04["cases"])==19, "source wave changes")
    cases=d["families"]
    require(len(cases)==EXPECTED_CATALOGUE, "missing family row")
    require(len({x["family_id"] for x in cases})==EXPECTED_CATALOGUE, "duplicate family row")
    require([x["family_id"] for x in cases]==sorted(x["family_id"] for x in index["families"]), "family order/mapping drift")
    input_paths=Counter(m["pdf_path"] for f in index["families"] for m in f["manuscripts"])
    output_paths=Counter(m["path"] for f in cases for m in f["source_provenance"]["manuscripts"])
    require(input_paths==output_paths and sum(output_paths.values())==EXPECTED_PATHS,
            "manuscript dropped, added or duplicated")
    require(Counter(x["final_class"] for x in cases)==EXPECTED_CLASSES,
            "classified counts mismatch")
    matched=set()
    for x in cases:
        fid=x["family_id"]
        require(x["certification"]=="NO_CERTIFICATION", "unapproved certification "+fid)
        require(x["source_provenance"]["source_commit"]==SOURCE, "stale source "+fid)
        require(x["final_class"] in (
            "VERIFIED_WITHIN_EXPLICIT_SCOPE","UNRESOLVED","INSUFFICIENT_EVIDENCE"),
            "unsupported final class "+fid)
        for p in x["evidence_paths"]:
            require((BASE.parent.parent / p).is_file(), "evidence missing "+p)
        if x["formal_replay"]=="EXACT_PINNED_PASS":
            require(fid=="008", "proof replay incorrectly attributed "+fid)
            require(x["axiom_audit"]=="EXACT_ALLOWED_THREE_PASS" and
                    x["comparator_replay"]=="HARDENED_ISOLATED_PASS",
                    "F008 missing independent formal gates")
            require(x["semantic_concordance"]=="PROPOSITION_LEVEL_ALIGNMENT__DEFINITIONS_EXPLICIT",
                    "formal-semantic bridge missing")
            require(x["mathematical_criticism"]=="BOUNDED_MODEL_REVIEW__LOW_WEIGHT_PASS",
                    "critic not present")
            receipts=x["replay_receipts"]
            require((receipts["lean"]["run_id"],receipts["lean"]["artifact_id"],
                     receipts["comparator"]["run_id"],receipts["comparator"]["artifact_id"],
                     receipts["source_head"])==EXPECTED_F008_RECEIPTS,"stale F008 run/artifact")
            matched.add(fid)
        else:
            require(x["formal_replay"]=="NOT_IMPORTED_FOR_THIS_FAMILY",
                    "unknown replay result forged "+fid)
            require(x["final_class"]!="VERIFIED_WITHIN_EXPLICIT_SCOPE",
                    "compilation or metadata alone promoted "+fid)
            require(x["replay_receipts"] is None, "unverified receipt invented "+fid)
    require(matched=={"008"}, "verified family set changed without governing evidence")
    f342=next(x for x in cases if x["family_id"]=="342")
    require(f342["final_class"]=="UNRESOLVED", "342 family-wide invalid promotion")
    require(f342["claim_level_exceptions"][0]["status"]=="SEMANTIC_MISMATCH__SUPERSEDED",
            "obsolete cone assertion reaccepted")
    require(d["withdrawn_claim_quarantine"]["promote_without_explicit_governed_source_review"] is False,
            "withdrawn title exclusion bypassed")
    require(set(d["withdrawn_claim_quarantine"]["titles"]) ==
            set(risk["exclusion_policy"]["withdrawn_title_scope"]),
            "withdrawn title drift")
    require(d["verification_throughput"]["new_MATHCERT_certificates"]==0,
            "MATHCERT certificate invented")
    require(d["verification_throughput"]["new_formal_targets_verified_by_wp05_generator"]==0,
            "source ledger mistaken for formal replay")
    require(d==build(), "ledger differs from deterministic protected source rebuild")
    return True

def hostile(base, label, mutate):
    d=copy.deepcopy(base)
    mutate(d)
    try:
        validate(d)
    except (AssertionError, ValueError, KeyError, TypeError, IndexError):
        print("WP05_HOSTILE_ROLLBACK_PASS",label)
    else:
        raise AssertionError("unsafe promotion not detected "+label)

def target(d,fid):
    return next(x for x in d["families"] if x["family_id"]==fid)

def main():
    d=json.loads(OUT.read_text())
    validate(d)
    hostile(d,"SOURCE_ONLY_PROMOTION",lambda a: target(a,"001").update(final_class="VERIFIED_WITHIN_EXPLICIT_SCOPE"))
    hostile(d,"PDF_PATH_LOSS",lambda a: target(a,"223")["source_provenance"]["manuscripts"].pop())
    hostile(d,"WRONG_LEAN_ARTIFACT",lambda a: target(a,"008")["replay_receipts"]["lean"].update(artifact_id=1))
    hostile(d,"WITHDRAWN_REINSTATEMENT",lambda a: a["withdrawn_claim_quarantine"].update(promote_without_explicit_governed_source_review=True))
    hostile(d,"OBSOLETE_CONE_REVIVAL",lambda a: target(a,"342")["claim_level_exceptions"][0].update(status="VERIFIED_WITHIN_EXPLICIT_SCOPE"))
    hostile(d,"STALE_EVIDENCE_HEAD",lambda a: a.update(imported_protected_evidence_head="0"*40))
    hostile(d,"ALTERED_SOURCE_BLOB_LOCK",lambda a: a["input_git_blob_sha1_locks"].update({"MANUSCRIPT_INDEX.json":"0"*40}))
    print("WP05_CANONICAL_LEDGER_PASS 372 families, 719 documents, 200 indexed declarations; 7 hostile rollbacks, 0 certifications")

if __name__=="__main__":
    try:
        main()
    except (OSError, KeyError, ValueError, TypeError, AssertionError) as exc:
        print("WP05_LEDGER_FAIL",exc,file=sys.stderr)
        raise SystemExit(1)
