#!/usr/bin/env python3
"""Fail-closed offline validator for the OAI-26 WP03 twelve-family source triage.

Checks document identity bookkeeping, family/edition coverage, crosswalk exact-path
counts, evidence pointers and prohibition of unsupported certification claims.
Does NOT replay Lean proofs or certify mathematics.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
BASE = ROOT / "sources" / "OPENAI-MATH-2026"
REV = BASE / "reviews"
SOURCE = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"

def require(cond, message):
    if not cond:
        raise AssertionError(message)

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def run():
    manifest = read(REV / "WP03_PILOT12_EVIDENCE_LEDGER.json")
    index = read(BASE / "MANUSCRIPT_INDEX.json")
    cross = read(BASE / "FORMALIZATION_CROSSWALK.json")
    require(manifest["source_commit"] == SOURCE, "pinned source changed")
    require(index["upstream"]["commit"] == SOURCE, "index source revision changed")
    require(cross["origin"]["commit"] == SOURCE, "crosswalk source revision changed")
    require(manifest["family_count"] == 12, "wrong family denominator")
    require(manifest["document_count"] == 24, "wrong edition denominator")
    require(manifest["certified_family_count"] == 0, "unsupported certification")
    require(len(cross["main_results"]) == 200 and len(cross["source_papers"]) == 173, "crosswalk denominator drift")
    expected_ids = [f"{i:03d}" for i in range(1, 13)]
    families = manifest["families"]
    require([f["family_id"] for f in families] == expected_ids, "family omission/duplication/order")
    source_index = {f["family_id"]: f for f in index["families"]}
    require(len(index["families"]) == 372, "family catalogue denominator drift")
    require(sum(len(f["manuscripts"]) for f in index["families"]) == 719, "whole-catalogue edition denominator drift")
    counted = 0
    for family in families:
        fid = family["family_id"]
        require(family["mathematical_certification"] == "NO_MATHCERT_CERTIFICATION", "false certification " + fid)
        require(family["lean_replay_this_review"] == "NOT_RUN", "false replay " + fid)
        require(family["disposition"].startswith(("UNRESOLVED", "PROPOSITION_LEVEL_ALIGNMENT")), "unearned promotion " + fid)
        docs = family["pdfs"]
        source_docs = source_index[fid]["manuscripts"]
        require([d["path"] for d in docs] == [d["pdf_path"] for d in source_docs], "edition mismatch " + fid)
        for doc in docs:
            counted += 1
            require(re.fullmatch(r"[a-f0-9]{40}", doc["git_blob_sha1"]) is not None, "bad git digest " + fid)
            require(re.fullmatch(r"[a-f0-9]{64}", doc["sha256"]) is not None, "bad sha256 " + fid)
            require(doc["byte_length"] > 0 and doc["page_count"] > 0, "invalid PDF length " + fid)
            actual = sum(p["pdf_path"] == doc["path"] for p in cross["source_papers"])
            require(actual == doc["exact_source_paper_crosswalk_matches"], "crosswalk count mismatch " + fid)
        for path in family["review_evidence_paths"]:
            review = ROOT / path
            require(review.is_file(), "missing review document " + str(review))
            txt = review.read_text(encoding="utf-8")
            require(SOURCE in txt, "source identity missing in " + str(review))
            require("NO_MATHCERT" in txt, "certification boundary missing " + str(review))
    require(counted == 24, "total scanned edition count mismatch")
    print("WP03 PILOT12 LEDGER PASS: 12 families, 24 source-locked editions; 0 certifications")
    print("No Lean theorem verification inferred from source or crosswalk coverage.")

if __name__ == "__main__":
    try:
        run()
    except (AssertionError, KeyError, OSError, ValueError) as exc:
        print("WP03 PILOT12 LEDGER FAIL:", exc, file=sys.stderr)
        raise SystemExit(1)
