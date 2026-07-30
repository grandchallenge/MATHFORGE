#!/usr/bin/env python3
"""Resolve immutable Formal Conjectures benchmark tags around a pinned commit."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

TAG_RE = re.compile(r"^bench-v(?P<benchmark>[0-9]+)-lean4\.(?P<major>[0-9]+)\.(?P<minor>[0-9]+)$")


def git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def tag_key(tag: str) -> tuple[int, int, int]:
    match = TAG_RE.fullmatch(tag)
    if match is None:
        raise ValueError(tag)
    return tuple(int(match.group(name)) for name in ("benchmark", "major", "minor"))


def matching_tags(output: str) -> list[str]:
    tags = [tag.strip() for tag in output.splitlines() if TAG_RE.fullmatch(tag.strip())]
    return sorted(set(tags), key=tag_key)


def classify(
    *,
    commit: str,
    exact_tags: list[str],
    containing_tags: list[str],
    selected_tag_commit: str | None,
) -> dict[str, object]:
    exact = sorted(set(exact_tags), key=tag_key)
    containing = sorted(set(containing_tags), key=tag_key)
    exact_tag = exact[-1] if exact else None
    containing_tag = containing[-1] if containing else None
    selected = exact_tag or containing_tag
    if exact_tag:
        resolution = "exact_immutable_tag"
        recommendation = "immutable_tag"
        reason = "An immutable benchmark tag points exactly at the pinned revision."
    elif containing_tag:
        resolution = "containing_immutable_tag"
        recommendation = "exact_commit"
        reason = (
            "An immutable benchmark tag contains the pinned revision but points at a later commit. "
            "The source lock must remain the exact commit to avoid importing unreviewed changes."
        )
    else:
        resolution = "commit_only_required"
        recommendation = "exact_commit"
        reason = "No fetched immutable benchmark tag contains the pinned revision."
    return {
        "schema_version": "1.0.0",
        "repository": "google-deepmind/formal-conjectures",
        "pinned_commit": commit,
        "exact_benchmark_tags": exact,
        "containing_benchmark_tags": containing,
        "selected_tag": selected,
        "selected_tag_commit": selected_tag_commit if selected else None,
        "resolution": resolution,
        "lock_recommendation": recommendation,
        "reason": reason,
    }


def resolve(repo: Path, commit: str) -> dict[str, object]:
    git(repo, "fetch", "--tags", "--force")
    exact = matching_tags(git(repo, "tag", "--points-at", commit, "--list", "bench-v*-lean4.*"))
    containing = matching_tags(git(repo, "tag", "--contains", commit, "--list", "bench-v*-lean4.*"))
    selected = (exact[-1] if exact else None) or (containing[-1] if containing else None)
    selected_commit = git(repo, "rev-parse", f"{selected}^{{commit}}") if selected else None
    return classify(
        commit=commit,
        exact_tags=exact,
        containing_tags=containing,
        selected_tag_commit=selected_commit,
    )


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
