#!/usr/bin/env python3
"""Resolve immutable Formal Conjectures benchmark tags containing a pinned commit."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

TAG_RE = re.compile(r"^bench-v(?P<benchmark>[0-9]+)-lean4\.(?P<major>[0-9]+)\.(?P<minor>[0-9]+)$")


def git(repo: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        check=check,
        capture_output=True,
        text=True,
    )


def tag_key(tag: str) -> tuple[int, int, int]:
    match = TAG_RE.fullmatch(tag)
    if match is None:
        raise ValueError(tag)
    return (
        int(match.group("benchmark")),
        int(match.group("major")),
        int(match.group("minor")),
    )


def resolve(repo: Path, commit: str) -> dict[str, object]:
    git(repo, "fetch", "--tags", "--force")
    tags = [
        tag.strip()
        for tag in git(repo, "tag", "--contains", commit, "--list", "bench-v*-lean4.*").stdout.splitlines()
        if TAG_RE.fullmatch(tag.strip())
    ]
    tags.sort(key=tag_key)
    selected = tags[-1] if tags else None
    selected_commit = None
    if selected is not None:
        selected_commit = git(repo, "rev-parse", f"{selected}^{{commit}}").stdout.strip()
    return {
        "schema_version": "1.0.0",
        "repository": "google-deepmind/formal-conjectures",
        "pinned_commit": commit,
        "containing_benchmark_tags": tags,
        "selected_tag": selected,
        "selected_tag_commit": selected_commit,
        "resolution": "immutable_tag_available" if selected else "commit_only_required",
        "reason": (
            "Selected the greatest benchmark and Lean-version tuple among immutable benchmark tags whose tagged commit contains the pinned revision."
            if selected
            else "No immutable benchmark tag fetched from the upstream repository contains the pinned revision; retain the exact commit lock."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = resolve(args.repository, args.commit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
