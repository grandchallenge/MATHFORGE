#!/usr/bin/env python3
"""Compute a fail-closed machine-readable delta between catalog snapshots."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


def index_entries(entries: Iterable[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for entry in entries:
        key = str(entry.get("source", {}).get("locator", ""))
        if not key or key in result:
            raise ValueError(f"missing or duplicate source locator: {key!r}")
        result[key] = entry
    return result


def compute_delta(
    provider_id: str,
    from_revision: str,
    to_revision: str,
    observed_at: str,
    old_entries: Iterable[dict[str, Any]],
    new_entries: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    old = index_entries(old_entries)
    new = index_entries(new_entries)
    shared = sorted(old.keys() & new.keys())
    statement_changes = [key for key in shared if old[key].get("representations") != new[key].get("representations")]
    classification_or_status_changes = [
        key for key in shared
        if (old[key].get("classification"), old[key].get("status_assertions"))
        != (new[key].get("classification"), new[key].get("status_assertions"))
    ]
    proof_annotation_changes = [key for key in shared if old[key].get("proof_annotations") != new[key].get("proof_annotations")]
    old_toolchains = sorted({entry.get("formal_language", {}).get("toolchain") for entry in old.values() if entry.get("formal_language")})
    new_toolchains = sorted({entry.get("formal_language", {}).get("toolchain") for entry in new.values() if entry.get("formal_language")})
    toolchain_change = None if old_toolchains == new_toolchains else {"from": old_toolchains, "to": new_toolchains}
    deletions = sorted(old.keys() - new.keys())
    invalidations = sorted(set(deletions + statement_changes + classification_or_status_changes + proof_annotation_changes))
    return {
        "schema_version": "2.0.0", "provider_id": provider_id,
        "from_revision": from_revision, "to_revision": to_revision, "observed_at": observed_at,
        "additions": sorted(new.keys() - old.keys()), "deletions": deletions,
        "statement_changes": statement_changes,
        "classification_or_status_changes": classification_or_status_changes,
        "proof_annotation_changes": proof_annotation_changes,
        "toolchain_change": toolchain_change,
        "possible_semantic_invalidations": invalidations,
        "automatic_admission": False,
    }


def read_jsonl(paths: list[Path]) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for path in paths:
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                entries.append(json.loads(line))
    return entries


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider-id", required=True)
    parser.add_argument("--from-revision", required=True)
    parser.add_argument("--to-revision", required=True)
    parser.add_argument("--old", type=Path, nargs="+", required=True)
    parser.add_argument("--new", type=Path, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--observed-at", default=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"))
    args = parser.parse_args()
    delta = compute_delta(args.provider_id, args.from_revision, args.to_revision, args.observed_at, read_jsonl(args.old), read_jsonl(args.new))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(delta, indent=2) + "\n", encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
