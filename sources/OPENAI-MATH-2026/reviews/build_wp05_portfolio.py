#!/usr/bin/env python3
"""Build a fail-closed OAI-26 source-scoped WP05 372-family portfolio ledger.

No network, no Lean execution. Source/semantic claims are evidence-bound to
the repository files and to the two exact runs already independently audited.
"""
from collections import Counter, defaultdict
from pathlib import Path
import json
import sys

BASE = Path(__file__).resolve().parents[1]
REV = BASE / "reviews"
SOURCE = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
UPSTREAM_TREE = "45074722c918576d65b4c8be9686c76f508ba696"
IMPORT_BASE = "fef6acbcc757a153509d6728e878c63404e8ad36"
OUT = REV / "WP05_CANONICAL_372_FAMILY_VERDICTS.json"
INPUT_BLOBS = {
    "MANUSCRIPT_INDEX.json": "7a0b00eb9bfdeb59b157a98ee6522fc685580152",
    "FORMALIZATION_CROSSWALK.json": "5fc50adc9430a91f22f1c3913bdfec62fe75acda",
    "WP02_CANONICAL_3_14_13_RISK_REGISTER.json": "2d43ab80ca9d6a4395566d38f0afd5a464e4395e",
    "reviews/WP03_PILOT12_EVIDENCE_LEDGER.json": "1aabf4800ae73da166258f3cdfdde8ec00da370a",
    "reviews/WP04_ADVERSARIAL_WAVE16_LEDGER.json": "747f65889cd1adfde7e4ff7170e07f6a49781bb8",
    "reviews/WP01_F008_DUAL_REPLAY_RECEIPT.md": "13f791bd5b9ae8df9900ad46a1a5ef689985ef14",
    "reviews/WP04_F008_ADVERSARIAL_MATHEMATICAL_REVIEW.md": "ed29fa92fe9b4910954311c482c496c02174f084",
    "WP01_COMPARATOR_200_PROTECTED_RECEIPT_INDEX.json": "2766fa809aeb297c4f11dda8f90c4e5ebdc6050f",
    "CORPUS_199_6500S_LEAN_RECEIPT_LEDGER.json": "da4f6e7eafbbdf570fdc488023ca16ccdb5bf7fe",
    "CORPUS_199_COMPARATOR_RECEIPT_LEDGER.json": "addd218e196f77c8d08bb76274e634f2ed2e3cc1",
}

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def require(value, message):
    if not value:
        raise ValueError(message)

def build():
    index = load(BASE / "MANUSCRIPT_INDEX.json")
    cross = load(BASE / "FORMALIZATION_CROSSWALK.json")
    risk = load(BASE / "WP02_CANONICAL_3_14_13_RISK_REGISTER.json")
    technical = load(BASE / "WP01_COMPARATOR_200_PROTECTED_RECEIPT_INDEX.json")
    require(technical["source_commit"] == SOURCE and
            technical["distinct_declarations"] == 200 and
            technical["unique_indices_covered"] == 200 and
            len(technical["rows"]) == 200, "WP01 technical coverage index changed")
    pilot = load(REV / "WP03_PILOT12_EVIDENCE_LEDGER.json")
    adversary = load(REV / "WP04_ADVERSARIAL_WAVE16_LEDGER.json")
    require(index["upstream"]["commit"] == SOURCE, "manifest source changed")
    require(cross["origin"]["commit"] == SOURCE, "crosswalk source changed")
    require(risk["source_lock"]["commit"] == SOURCE, "risk source changed")
    require(pilot["source_commit"] == SOURCE and adversary["source_commit"] == SOURCE, "wave source changed")
    require(len(index["families"]) == 372, "family denominator")
    require(sum(len(f["manuscripts"]) for f in index["families"]) == 719, "manuscript denominator")
    require(len(cross["main_results"]) == 200 and len(cross["source_papers"]) == 173, "crosswalk denominator")
    require(len(adversary["cases"]) == 19 and len(pilot["families"]) == 12, "wave denominator")
    idx = {x["family_id"]: x for x in index["families"]}
    require(len(idx) == 372, "duplicate family IDs")
    prior = {x["family_id"]: x for x in pilot["families"]}
    reviewed = {x["family_id"]: x for x in adversary["cases"]}
    riskrows = defaultdict(list)
    for x in risk["rows"]:
        if x.get("family_id") is not None:
            riskrows[x["family_id"]].append(x)
    paperpaths = Counter(x["pdf_path"] for x in cross["source_papers"])
    named = {
      "003": ["OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re",
              "OAI.SiegelZeros.WeightedTorusJets.exists_absolute_real_zero_gap"],
      "008": ["OAI.DeligneDrinfeld.main"],
      "342": ["OAI.TamingCompatibility.taming_implies_compatibility"],
    }
    declarations = {x["declaration"]: x for x in cross["main_results"]}
    for v in named.values():
        for name in v:
            require(name in declarations, "manual declaration hint missing " + name)
    records = []
    for fid in sorted(idx):
        meta = idx[fid]
        p = prior.get(fid)
        a = reviewed.get(fid)
        source_paths = [m["pdf_path"] for m in meta["manuscripts"]]
        source_paper_hits = sum(paperpaths[path] for path in source_paths)
        riskset = riskrows.get(fid, [])
        formal = fid == "008"
        if formal:
            verdict = "VERIFIED_WITHIN_EXPLICIT_SCOPE"
            why = ("Exact pinned Lean theorem and permissible axiom closure, independent "
                   "isolated hardened Comparator, explicit bounded statement bridge "
                   "and low-weight mathematical adversary; NOT complete manuscript certification.")
        elif p is not None or a is not None or riskset:
            verdict = "UNRESOLVED"
            why = ("Scoped source/semantic or revision-risk review records unresolved "
                   "mathematical obligations. No exact positive whole-proof replay admitted here.")
        else:
            verdict = "INSUFFICIENT_EVIDENCE"
            why = ("Catalogue source metadata is locked but no governed family-level "
                   "mathematical proof adjudication imported into this portfolio.")
        risks = sorted(set(
            [str(r.get("severity", "unassessed")).upper() for r in riskset] +
            (["SOURCE_SEMANTIC"] if a else []) +
            (["VERSION_MISMATCH"] if fid == "342" else [])
        ))
        pointers = []
        if p:
            pointers += p["review_evidence_paths"]
        if a:
            pointers += a["source_evidence"]
            pointers.append("sources/OPENAI-MATH-2026/reviews/WP04_ADVERSARIAL_WAVE19_REPORT.md")
        if riskset:
            pointers.append("sources/OPENAI-MATH-2026/WP02_CANONICAL_3_14_13_RISK_REGISTER.json")
        if formal:
            pointers += ["sources/OPENAI-MATH-2026/reviews/WP03_FAMILY008_EXPANDED_DEFINITION_BRIDGE.md",
                         "sources/OPENAI-MATH-2026/reviews/WP01_F008_DUAL_REPLAY_RECEIPT.md",
                         "sources/OPENAI-MATH-2026/reviews/WP04_F008_ADVERSARIAL_MATHEMATICAL_REVIEW.md"]
        pointers = sorted(set(pointers))
        row = {
            "family_id": fid,
            "headline": meta["headline"],
            "source_provenance": {
                "source_commit": SOURCE,
                "metadata": "PINNED_CATALOGUE",
                "pdf_bytes_checked_in_imported_wave": bool(p) or fid in ("095", "191", "223"),
                "manuscripts": [{"title":m["title"], "path":m["pdf_path"]}
                                for m in meta["manuscripts"]],
                "source_paper_crosswalk_path_matches": source_paper_hits,
                "disclaimer": "Path matches do not automatically map any of the 200 Lean declarations."
            },
            "formal_declaration_candidates": [
                {"declaration": name, "comparator_config": declarations[name]["comparator_config"],
                 "identity_status": "EXPLICIT_SCOPED_CORRESPONDENCE_NOT_CATALOGUE_WIDE"}
                for name in named.get(fid, [])],
            "formal_replay": "EXACT_PINNED_PASS" if formal else "NOT_IMPORTED_FOR_THIS_FAMILY",
            "axiom_audit": "EXACT_ALLOWED_THREE_PASS" if formal else "NOT_IMPORTED_FOR_THIS_FAMILY",
            "comparator_replay": "HARDENED_ISOLATED_PASS" if formal else "NOT_IMPORTED_FOR_THIS_FAMILY",
            "semantic_concordance": (
                "PROPOSITION_LEVEL_ALIGNMENT__DEFINITIONS_EXPLICIT" if formal
                else a["disposition"] if a else p["disposition"] if p
                else "NOT_REVIEWED_FOR_THIS_FAMILY"),
            "mathematical_criticism": (
                "BOUNDED_MODEL_REVIEW__LOW_WEIGHT_PASS" if formal
                else "BOUNDED_SOURCE_LOGICAL_CRITIC__NOT_FULL_PROOF" if a
                else "NOT_IMPORTED_FOR_THIS_FAMILY"),
            "risk": {"flags": risks,
                     "wp02_rows": [{"key":r["key"], "category":r["category"],
                                    "severity":r.get("severity", "unassessed")}
                                   for r in riskset]},
            "evidence_paths": pointers,
            "final_class": verdict,
            "verdict_reason": why,
            "certification": "NO_CERTIFICATION",
            "claim_level_exceptions": (
                [{"claim":"September 23 unconditional cone identity",
                  "status":"SEMANTIC_MISMATCH__SUPERSEDED",
                  "current_edition":"October 6 conditional h_J^- = b2+(X)-1",
                  "distinction":"Main existence theorem is not refuted by this statement revision."}]
                if fid == "342" else []),
            "claim_level_technical_results": (
                [{
                    "claim": "Riemann zeta nonvanishing Re(s)>7/8 only",
                    "declaration": "OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re",
                    "crosswalk_index": 199,
                    "lean_axioms": "EXACT_PINNED_PASS__ALLOWED_THREE",
                    "comparator": "HARDENED_ACCEPTED",
                    "lean_run": 40743532665,
                    "lean_artifact": 12845633244,
                    "comparator_run": 40777019339,
                    "comparator_artifact": 12859904511,
                    "evidence_paths": [
                        "sources/OPENAI-MATH-2026/CORPUS_199_6500S_LEAN_RECEIPT_LEDGER.json",
                        "sources/OPENAI-MATH-2026/CORPUS_199_COMPARATOR_RECEIPT_LEDGER.json"],
                    "qualification": "TECHNICAL_ZETA_SUBCLAIM_ONLY_NOT_ALL_FINITE_ORDER_HECKE_FAMILY"
                }]
                if fid == "003" else []),
            "replay_receipts": (
                {"lean":{"run_id":44298907335, "job_id":134783123190,
                         "artifact_id":14425447501,
                         "zip_sha256":"c33410fb5331c7c3178cf4714e64ddfd91972e7dc6bfb52c02ac1a782c14cbac"},
                 "comparator":{"run_id":44304148849, "job_id":134801236450,
                               "artifact_id":14428700812,
                               "zip_sha256":"ee010b0d1f8de9eb079a6c3a4af00b1926a41aafc3ddb6587bc63c99752997ad"},
                 "source_head":"4dcf6e4ac49bed6c61b05980ca17036a78d5e894"}
                if formal else None),
        }
        records.append(row)
    require(sum(len(r["source_provenance"]["manuscripts"]) for r in records) == 719,
            "dropped PDF paths")
    byclass = dict(sorted(Counter(x["final_class"] for x in records).items()))
    verdict = {
        "schema":"GCL-OAI26-WP05-CANONICAL-372/1",
        "source_lock":{"repository":"openai/math","commit":SOURCE,"tree":UPSTREAM_TREE},
        "imported_protected_evidence_head": IMPORT_BASE,
        "input_git_blob_sha1_locks": INPUT_BLOBS,
        "catalogue":{"families":372,"manuscript_paths":719,
                     "crosswalk_source_papers":173,
                     "crosswalk_distinct_declarations":200,
                     "publisher_top_line_claims":300,
                     "counting_warning":"300 publisher claims != 200 indexed declarations != 372 families != 719 manuscripts"},
        "classification_precedence":["Only exact formal replay plus axioms plus comparator plus bounded semantic/math criticism can justify VERIFIED_WITHIN_EXPLICIT_SCOPE",
                                     "Historic claim-level mismatches remain distinct from family-wide verdicts",
                                     "Reviewed nonfinal and revision-risk cases remain UNRESOLVED",
                                     "Metadata-only cases remain INSUFFICIENT_EVIDENCE",
                                     "No MATHCERT source yields NO_CERTIFICATION for all rows"],
        "withdrawn_claim_quarantine":{
            "source":"sources/OPENAI-MATH-2026/WP02_CANONICAL_3_14_13_RISK_REGISTER.json",
            "titles":risk["exclusion_policy"]["withdrawn_title_scope"],
            "promote_without_explicit_governed_source_review":False,
            "current_family_mapping":"NOT_ESTABLISHED__DO_NOT_INFER_FROM_TITLE"},
        "waves":[{"name":"WP03 source-semantic","distinct_families":12,"newly_verified_theorems_within_wave":0},
                 {"name":"WP04 bounded adversarial","distinct_families":19,
                  "overlap_with_wp03":12,"newly_verified_theorems_within_wave":0}],
        "wp01_technical_corpus_evidence": {
            "source": "sources/OPENAI-MATH-2026/WP01_COMPARATOR_200_PROTECTED_RECEIPT_INDEX.json",
            "covered_distinct_comparator_indices": 200,
            "indexed_declarations": 200,
            "protected_receipt_files": 87,
            "duplicate_index_199_counted_once": True,
            "index_only_bindings": technical["index_only_bindings"],
            "scope": "HARDENED_TECHNICAL_COMPARATOR_ONLY_NOT_FAMILY_SEMANTIC_MATCH"
        },
        "verification_throughput":{
            "families_with_formal_exact_replay_and_comparator_imported":1,
            "corpus_wide_comparator_technical_accepted_indices": 200,
            "family003_exact_zeta_subclaim_lean_and_comparator_evidence": True,
            "full_paper_hecke_claim_verified_by_index199": False,
            "distinct_formal_targets_verifiably_imported":1,
            "new_formal_targets_verified_by_wp05_generator":0,
            "distinct_bounded_mathematical_critic_cases_in_wp04":19,
            "historical_claim_mismatches_flagged":1,
            "new_MATHCERT_certificates":0,
            "family_final_class_counts":byclass},
        "families":records,
        "claim_boundary":"SOURCE_SCOPED_PORTFOLIO__NO_MATHCERT_CERTIFICATION"}
    return verdict

if __name__=="__main__":
    try:
        data=build()
        OUT.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        print("WP05_GENERATOR_PASS families",len(data["families"]),"manuscripts",
              sum(len(x["source_provenance"]["manuscripts"]) for x in data["families"]),
              "classes",data["verification_throughput"]["family_final_class_counts"])
    except (OSError,KeyError,ValueError,TypeError) as e:
        print("WP05_GENERATOR_FAIL",e,file=sys.stderr)
        raise SystemExit(1)
