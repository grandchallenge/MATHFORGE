#!/usr/bin/env python3
"""Deterministic metadata-only OpenAI Math 2026 provider snapshot builder.

This adapter indexes manuscript TITLE metadata only, not a theorem proposition or proof.
Reproducing its bytes cannot create semantic review, campaign authority or certification.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from build_semantic_catalog import (
    ROOT, sha256_bytes, sha256_file, canonical_line, normalized_text,
    write_json, CatalogError, EXCLUDED_INFERENCES,
)

PROVIDER = "OAI-MATH-2026"
SNAPSHOT = "OAI-MATH-1581D4CB"
UPSTREAM = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
INPUT = ROOT / "sources" / "OPENAI-MATH-2026" / "MANUSCRIPT_INDEX.json"
PREFIX = "openai-math"
SHARD_ROWS = 180
CLAIM = ("This provider indexes pinned manuscript titles and provenance, not theorem texts. "
         "No Lean proof replay, statement equivalence, novelty, Programme authority, "
         "MATHSOLVE result, Claim Ledger mutation or MATHCERT certification is established.")

def entries(index: dict):
    assert index["upstream"]["commit"] == UPSTREAM
    seen = set()
    row = 0
    for family in index["families"]:
        fid = family["family_id"]
        for manuscript in family["manuscripts"]:
            path = manuscript["pdf_path"]
            title = manuscript["title"]
            if path in seen or not path.startswith("preprints/") or not path.endswith(".pdf"):
                raise CatalogError(f"invalid or repeated indexed source: {path}")
            seen.add(path)
            source_record = {"family_id": fid, "pdf_path": path, "title": title}
            source_sha = sha256_bytes(canonical_line(source_record).rstrip(b"\n"))
            yield {
                "schema_version": "2.0.0",
                "catalog_id": f"GCL-CAT-OAI-{row:05d}",
                "provider_id": PROVIDER, "snapshot_id": SNAPSHOT,
                "source": {
                    "locator": f"sources/OPENAI-MATH-2026/MANUSCRIPT_INDEX.json#family={fid}&paper={row}",
                    "url": f"https://github.com/openai/math/blob/{UPSTREAM}/{path}",
                    "raw_sha256": source_sha,
                },
                "statement_kind": "other",
                "representations": {"original": title, "normalized": normalized_text(title),
                                    "normalization_method": "verbatim manuscript-title whitespace normalization v1"},
                "classification": {"msc2020_primary": None,
                                   "mapping_method": "unclassified manuscript title; no inferred MSC or theorem topic",
                                   "facets": [f"family:{fid}", f"family_headline:{family['headline']}"]},
                "status_assertions": [], "proof_annotations": [],
                "licensing": {"license": "Apache-2.0 root repository; metadata only",
                              "redistribution_class": "metadata_only"},
                "assurance": {"tier": "SOURCE_LOCKED",
                              "evidence": ["source:openai/math@" + UPSTREAM,
                                           "sources/OPENAI-MATH-2026/MANUSCRIPT_INDEX.json"]},
                "relation_ids": [],
                "unresolved_ambiguities": [
                    "Manuscript title is not its theorem statement.",
                    "Literature, exact corrected versions, Lean replay and statement concordance remain unaudited."
                ],
                "excluded_inferences": EXCLUDED_INFERENCES,
                "claim_boundary": CLAIM,
            }
            row += 1

def build() -> dict:
    data = json.loads(INPUT.read_text(encoding="utf-8"))
    listed = list(entries(data))
    if len(data["families"]) != 372 or len(listed) != 719:
        raise CatalogError("pinned OpenAI Math catalogue cardinality drift")
    if not any("CAT(0)-spaces" in p["source"]["url"] for p in listed):
        raise CatalogError("CAT(0) parser regression")
    shards = []
    for i in range(0, len(listed), SHARD_ROWS):
        bucket = listed[i:i + SHARD_ROWS]
        path = ROOT / "catalog" / "entries" / f"{PREFIX}-{i//SHARD_ROWS:05d}.jsonl"
        raw = b"".join(canonical_line(record) for record in bucket)
        path.write_bytes(raw)
        shards.append({
            "path": path.relative_to(ROOT).as_posix(), "entry_count": len(bucket),
            "byte_length": len(raw), "sha256": sha256_bytes(raw),
            "first_catalog_id": bucket[0]["catalog_id"],
            "last_catalog_id": bucket[-1]["catalog_id"],
        })
    existing = list((ROOT / "catalog" / "entries").glob(PREFIX + "-*.jsonl"))
    if len(existing) != len(shards):
        raise CatalogError("stale OpenAI Math shards detected")
    manifest = {
        "schema_version": "2.0.0", "snapshot_id": SNAPSHOT, "provider_id": PROVIDER,
        "revision": UPSTREAM, "admitted_at": "2026-10-23T21:45:49Z",
        "admission_basis": {"revision_kind": "exact_commit", "benchmark_tag": None,
                            "tag_exception_reason": "Upstream is an immutable public Git commit, not a benchmark release."},
        "source_objects": [{"locator": INPUT.relative_to(ROOT).as_posix(), "sha256": sha256_file(INPUT)}],
        "inventory_count": len(listed), "catalog_shards": shards,
        "replay": {
            "adapter": "catalog/build_openai_math_provider.py", "adapter_version": "1.0.0",
            "command": "python catalog/build_openai_math_provider.py build",
            "environment": ["Python >=3.11; standard library", "pinned OpenAI Math index within MATHFORGE"],
            "deterministic": True,
        },
        "claim_boundary": CLAIM,
    }
    write_json(ROOT / "catalog" / "providers" / f"{SNAPSHOT}.json", manifest)
    return manifest

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("command", choices=["build"])
    p.parse_args()
    print(json.dumps({"snapshot_id": build()["snapshot_id"], "entries": 719}))
