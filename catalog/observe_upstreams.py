#!/usr/bin/env python3
"""Read-only weekly observer for external provider heads.

The observer writes an artifact outside the governed registry and never changes an
admitted snapshot. A changed head is a review signal, not an admission event.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


class ObservationError(RuntimeError):
    pass


def git_head(url: str) -> str:
    completed = subprocess.run(
        ["git", "ls-remote", url, "refs/heads/main"],
        check=True, capture_output=True, text=True,
    )
    fields = completed.stdout.strip().split()
    if len(fields) != 2 or len(fields[0]) != 40:
        raise ObservationError(f"cannot resolve immutable main head for {url}")
    return fields[0]


def observe(output: Path, observed_at: str) -> bool:
    registry = json.loads((ROOT / "governance" / "external_sources.json").read_text(encoding="utf-8"))
    movements: list[dict[str, Any]] = []
    for provider in registry["providers"]:
        admitted = provider["admitted_snapshot"]["revision"]
        observed = git_head(provider["upstream"]["url"])
        if observed != admitted:
            movements.append({
                "schema_version": "2.0.0",
                "provider_id": provider["provider_id"],
                "from_revision": admitted,
                "to_revision": observed,
                "observed_at": observed_at,
                "additions": [],
                "deletions": [],
                "statement_changes": [],
                "classification_or_status_changes": [],
                "proof_annotation_changes": [],
                "toolchain_change": None,
                "possible_semantic_invalidations": ["FULL_PROVIDER_DELTA_REQUIRED_BEFORE_ADMISSION"],
                "automatic_admission": False,
            })
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({
        "schema_version": "2.0.0",
        "observed_at": observed_at,
        "changed": bool(movements),
        "movements": movements,
        "authority_boundary": "This is a read-only observation. It neither updates admitted identity nor promotes catalog, campaign, claim, proof, or certification state."
    }, indent=2) + "\n", encoding="utf-8", newline="\n")
    return bool(movements)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--observed-at", default=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"))
    args = parser.parse_args()
    try:
        changed = observe(args.output, args.observed_at)
    except (OSError, KeyError, json.JSONDecodeError, subprocess.CalledProcessError, ObservationError) as exc:
        print(f"observer error: {exc}", file=sys.stderr)
        return 1
    print(f"changed={'true' if changed else 'false'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
