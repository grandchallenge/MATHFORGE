#!/usr/bin/env python3
"""Build a compact, deterministic coverage screen from a replayed extractor inventory."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

QUERY_SETS = {
    "HC-001": ["hodge", "cycleclass", "cycle_class", "algebraiccycle", "algebraic_cycle"],
    "YM-001": ["yangmills", "yang_mills", "massgap", "mass_gap", "mills"],
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def derive_source_path(module: str) -> str:
    if not module.startswith("FormalConjectures."):
        raise ValueError(f"unexpected module: {module}")
    return module.replace(".", "/") + ".lean"


def haystack(problem: dict[str, Any]) -> str:
    return " ".join(
        str(problem.get(key, ""))
        for key in ("theorem", "module", "category")
    ).lower().replace("-", "_").replace(".", "_")


def screen(inventory: dict[str, Any], raw_bytes: bytes, upstream_commit: str) -> dict[str, Any]:
    problems = inventory.get("problems")
    if not isinstance(problems, list) or not problems:
        raise ValueError("inventory must contain a non-empty problems array")
    searches = []
    for campaign_id, terms in QUERY_SETS.items():
        hits = []
        for problem in problems:
            text = haystack(problem)
            matched = sorted(term for term in terms if term in text)
            if matched:
                hits.append({
                    "theorem": str(problem.get("theorem", "")),
                    "module": str(problem.get("module", "")),
                    "source_path": derive_source_path(str(problem.get("module", ""))),
                    "category": problem.get("category"),
                    "matched_terms": matched,
                })
        hits.sort(key=lambda item: (item["module"], item["theorem"]))
        searches.append({
            "campaign_id": campaign_id,
            "query_terms": terms,
            "hits": hits,
        })
    result = {
        "schema_version": "1.0.0",
        "screen_id": "MF-FC-GDM-002-FULL-INVENTORY-SCREEN",
        "upstream_repository": "google-deepmind/formal-conjectures",
        "upstream_commit": upstream_commit,
        "inventory": {
            "byte_length": len(raw_bytes),
            "sha256": hashlib.sha256(raw_bytes).hexdigest(),
            "problem_count": len(problems),
        },
        "searches": searches,
        "claim_boundary": (
            "This screen reports exact keyword hits in the replayed extractor inventory. "
            "A zero-hit result is not proof of mathematical absence, and a lexical hit is not semantic coverage."
        ),
    }
    result["screen_sha256"] = hashlib.sha256(canonical_bytes({
        key: value for key, value in result.items() if key != "screen_sha256"
    })).hexdigest()
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--upstream-commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raw = args.inventory.read_bytes()
    inventory = json.loads(raw)
    result = screen(inventory, raw, args.upstream_commit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
