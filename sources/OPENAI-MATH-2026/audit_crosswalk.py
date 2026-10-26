#!/usr/bin/env python3
"""Source-only inventory accounting; never interprets an indexed declaration as a proof."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PINNED_UPSTREAM = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
UPSTREAM_FORMALIZATION_BLOB = "275eee8cfab7ce49d3a5e88f02cbb8f28fe6fee6"


def unique(values, label):
    counts = Counter(values)
    duplicates = sorted(x for x, n in counts.items() if n > 1)
    if duplicates:
        raise ValueError(f"duplicate {label}: {duplicates[:10]}")
    return counts


def audit(index, crosswalk, source_lock):
    families = index["families"]
    unique((f["family_id"] for f in families), "family IDs")
    papers = [(f["family_id"], p) for f in families for p in f["manuscripts"]]
    paths = unique((p["pdf_path"] for _, p in papers), "catalogue PDF paths")
    if any(not p.startswith("preprints/") or not p.endswith(".pdf")
           or ".." in Path(p).parts for p in paths):
        raise ValueError("malformed/unsafe catalogue PDF path")
    source_papers = crosswalk["source_papers"]
    unique((s["pdf_path"] for s in source_papers), "formalization source paths")
    indexed = {p["pdf_path"]: family_id for family_id, p in papers}
    sources_by_family = {f["family_id"]: [] for f in families}
    source_exceptions = []
    for s in source_papers:
        path = s["pdf_path"]
        found = path in indexed
        if s["indexed_manuscript"] is not found:
            raise ValueError(f"incorrect formalization indexed_manuscript flag: {path}")
        if found:
            sources_by_family[indexed[path]].append({"title": s["title"], "pdf_path": path})
        else:
            source_exceptions.append({"title": s["title"], "pdf_path": path,
                                      "status": "SOURCE_EDITION_NOT_IN_CURRENT_INDEX"})
    results = crosswalk["main_results"]
    unique((r["declaration"] for r in results), "qualified theorem declarations")
    for r in results:
        if (not r["lean_source"].startswith("lean/") or
            not r["comparator_config"].startswith("lean/ComparatorChallenges/") or
            not r["comparator_config"].endswith(".json") or
            r["replay"] != "NOT_RUN" or r["semantic_review"] != "NOT_REVIEWED"):
            raise ValueError(f"unrecognized source-only crosswalk row: {r['declaration']}")
    comparator_counts = Counter(r["comparator_config"] for r in results)
    revisions = crosswalk.get("revision_exceptions", [])
    if sorted(x["pdf_path"] for x in source_exceptions) != sorted(
        x["formalization_reference"] for x in revisions
    ):
        raise ValueError("unmatched historical formalization edition lacks revision exception")
    if source_lock["upstream"]["observed_commit"] != PINNED_UPSTREAM:
        raise ValueError("source lock drift")
    if (source_lock["repository_reported"]["manuscript_count"] != len(papers) or
        source_lock["repository_reported"]["result_family_count"] != len(families)):
        raise ValueError("upstream denominator conflict")
    if (len(families), len(papers), len(source_papers), len(results)) != (372, 719, 173, 200):
        raise ValueError("pinned corpus inventory count drift")
    mapped_count = sum(bool(v) for v in sources_by_family.values())
    return {
        "record_type": "GCL_OAI26_SOURCE_CROSSWALK_LEDGER/1",
        "upstream_commit": PINNED_UPSTREAM,
        "claim_boundary": "SOURCE_ONLY_NO_PROOF_REPLAY_NO_SEMANTIC_BRIDGE_NO_MATHCERT",
        "summary": {
            "family_count": len(families), "unique_catalogue_paths": len(paths),
            "source_record_count": len(source_papers),
            "indexed_source_record_count": len(source_papers)-len(source_exceptions),
            "unindexed_source_record_count": len(source_exceptions),
            "source_linked_family_count": mapped_count,
            "families_without_source_paper_match": len(families)-mapped_count,
            "distinct_declarations": len(results),
            "distinct_solution_file_paths": len({r["lean_source"] for r in results}),
            "distinct_comparator_config_paths": len(comparator_counts),
            "comparator_configs_shared_across_declarations": sum(v>1 for v in comparator_counts.values()),
            "publisher_reported_formalized_top_line_results": source_lock["repository_reported"]["top_line_results_formalized"],
            "publisher_count_reconciled_to_declarations": False,
            "declarations_explicitly_bound_to_family": 0,
        },
        "families": [
            {"family_id": f["family_id"], "headline": f["headline"],
             "manuscripts": f["manuscripts"],
             "manifest_source_papers": sorted(sources_by_family[f["family_id"]],
                                             key=lambda x: x["pdf_path"]),
             "manifest_source_match_only": bool(sources_by_family[f["family_id"]]),
             "formal_theorems_assigned": None,
             "assignment_state": "DECLARATION_TO_FAMILY_EDGE_NOT_IN_SOURCE_MANIFEST"}
            for f in sorted(families, key=lambda x: x["family_id"])
        ],
        "declarations": [
            {"declaration": r["declaration"], "lean_source": r["lean_source"],
             "comparator_config": r["comparator_config"], "family_id": None,
             "family_binding": "NOT_PROVIDED_BY_UPSTREAM_FORMALIZATION_MANIFEST",
             "lean_replay": r["replay"], "semantic_review": r["semantic_review"]}
            for r in sorted(results, key=lambda x: x["declaration"])
        ],
        "unindexed_source_editions": sorted(source_exceptions, key=lambda x: x["pdf_path"]),
        "source_revision_exceptions": revisions,
        "shared_comparator_configs": [
            {"path": path, "declaration_count": count} for path, count
            in sorted(comparator_counts.items()) if count > 1
        ],
    }

def verify_upstream_yaml(blob, crosswalk):
    """Optional exact pinned upstream replay; PyYAML is needed only for this input."""
    blob_sha = hashlib.sha1(b"blob " + str(len(blob)).encode() + b"\0" + blob).hexdigest()
    if blob_sha != UPSTREAM_FORMALIZATION_BLOB:
        raise ValueError("upstream formalization.yaml blob differs from pinned SOURCE_LOCK")
    try:
        import yaml
    except ImportError as exc:
        raise ValueError("optional upstream replay requires PyYAML") from exc
    upstream = yaml.safe_load(blob)
    source_paths = sorted(s["id"].removeprefix("../") for s in upstream["sources"])
    indexed_paths = sorted(s["pdf_path"] for s in crosswalk["source_papers"])
    if source_paths != indexed_paths:
        raise ValueError("upstream YAML sources do not match GCL source records")
    rows = sorted((r["declaration"], "lean/"+r["file"],
                   "lean/"+r["comparator_config"])
                  for r in upstream["status"]["main_results"])
    gcl = sorted((r["declaration"], r["lean_source"], r["comparator_config"])
                 for r in crosswalk["main_results"])
    if rows != gcl:
        raise ValueError("upstream main-result triples do not match GCL crosswalk")
    return {"upstream_yaml_blob_sha1": blob_sha, "source_paths_matched": len(source_paths),
            "declaration_config_triples_matched": len(rows)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=Path, default=ROOT/"MANUSCRIPT_INDEX.json")
    parser.add_argument("--crosswalk", type=Path, default=ROOT/"FORMALIZATION_CROSSWALK.json")
    parser.add_argument("--source-lock", type=Path, default=ROOT/"SOURCE_LOCK.json")
    parser.add_argument("--upstream-yaml", type=Path)
    parser.add_argument("--output", type=Path, default=ROOT/"SOURCE_CROSSWALK_LEDGER.json")
    parser.add_argument("--check", action="store_true", help="compare committed ledger; do not write")
    args = parser.parse_args()
    read = lambda path: json.loads(path.read_text(encoding="utf-8"))
    index, crosswalk, source_lock = map(read, (args.index, args.crosswalk, args.source_lock))
    result = audit(index, crosswalk, source_lock)
    if args.upstream_yaml:
        evidence = verify_upstream_yaml(args.upstream_yaml.read_bytes(), crosswalk)
        print("UPSTREAM_SOURCE_REPLAY_PASS", json.dumps(evidence, sort_keys=True))
    content = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)+"\n"
    if args.check:
        if not args.output.is_file() or args.output.read_text(encoding="utf-8") != content:
            raise SystemExit("FAIL: source crosswalk ledger output drift")
    else:
        args.output.write_text(content, encoding="utf-8")
    print("SOURCE_LEDGER_PASS", json.dumps(result["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
