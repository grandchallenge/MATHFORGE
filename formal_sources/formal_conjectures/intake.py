#!/usr/bin/env python3
"""Fail-closed intake for pinned Formal Conjectures statement snapshots."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


class IntakeError(RuntimeError):
    """Raised when a governed intake identity or invariant fails."""


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise IntakeError(f"cannot load JSON from {path}: {exc}") from exc


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def digest_payload(snapshot: dict[str, Any]) -> dict[str, Any]:
    return {
        "source_lock_id": snapshot["source_lock_id"],
        "source_commit": snapshot["source_commit"],
        "scope": snapshot["scope"],
        "statements": snapshot["statements"],
    }


def snapshot_digest(snapshot: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_bytes(digest_payload(snapshot))).hexdigest()


def derive_source_path(module: str) -> str:
    if not module.startswith("FormalConjectures."):
        raise IntakeError(f"unexpected module outside FormalConjectures: {module}")
    return module.replace(".", "/") + ".lean"


def git_output(repo: Path, *args: str) -> str:
    try:
        completed = subprocess.run(
            ["git", "-C", str(repo), *args],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        stderr = getattr(exc, "stderr", "") or ""
        raise IntakeError(f"git {' '.join(args)} failed: {stderr.strip()}") from exc
    return completed.stdout.strip()


def artifact_blob_map(lock: dict[str, Any]) -> dict[str, str]:
    blobs: dict[str, str] = {}
    for item in lock["revision"]["artifact_blobs"]:
        path = item["path"]
        if path in blobs:
            raise IntakeError(f"duplicate locked artifact path: {path}")
        blobs[path] = item["git_blob_sha1"]
    return blobs


def verify_checkout(lock: dict[str, Any], checkout: Path) -> dict[str, str]:
    expected_commit = lock["revision"]["commit"]
    actual_commit = git_output(checkout, "rev-parse", "HEAD")
    if actual_commit != expected_commit:
        raise IntakeError(f"source commit mismatch: expected {expected_commit}, found {actual_commit}")

    locked = artifact_blob_map(lock)
    for path, expected_blob in locked.items():
        actual_blob = git_output(checkout, "rev-parse", f"HEAD:{path}")
        if actual_blob != expected_blob:
            raise IntakeError(
                f"source blob mismatch for {path}: expected {expected_blob}, found {actual_blob}"
            )

    toolchain = (checkout / "lean-toolchain").read_text(encoding="utf-8").strip()
    if toolchain != lock["toolchain"]["lean_toolchain"]:
        raise IntakeError(
            f"Lean toolchain mismatch: expected {lock['toolchain']['lean_toolchain']}, found {toolchain}"
        )
    return locked


def normalize_problem(problem: dict[str, Any], blobs: dict[str, str]) -> dict[str, Any]:
    module = str(problem.get("module", ""))
    theorem = str(problem.get("theorem", ""))
    if not theorem:
        raise IntakeError("extracted problem is missing theorem name")
    source_path = derive_source_path(module)
    if source_path not in blobs:
        raise IntakeError(f"no locked source blob for extracted module {module} ({source_path})")

    proof_kind = problem.get("formalProofKind")
    proof_link = problem.get("formalProofLink")
    if (proof_kind is None) != (proof_link is None):
        raise IntakeError(f"partial formal proof metadata for {theorem}")
    formal_proof = None if proof_kind is None else {"kind": proof_kind, "link": proof_link}

    return {
        "statement_id": f"FC:{theorem}",
        "theorem": theorem,
        "module": module,
        "source_path": source_path,
        "source_git_blob_sha1": blobs[source_path],
        "category": problem.get("category"),
        "subjects": sorted(str(item) for item in problem.get("subjects", [])),
        "statement": str(problem.get("statement", "")),
        "docstring": problem.get("docstring"),
        "formal_proof": formal_proof,
        "has_sorry_free_proof": bool(problem.get("hasSorryFreeProof", False)),
        "answer_kinds": list(problem.get("answerKinds", [])),
        "file_first_added": problem.get("fileFirstAdded"),
        "file_last_modified": problem.get("fileLastModified"),
        "review_state": "source-verified",
        "claim_boundary": (
            "This record proves only that the statement was extracted from the pinned Lean source. "
            "It does not establish semantic equivalence, current status, or certification."
        ),
    }


def build_snapshot(
    lock: dict[str, Any],
    extracted: dict[str, Any],
    blobs: dict[str, str],
    generated_at: str,
) -> dict[str, Any]:
    problems = extracted.get("problems")
    if not isinstance(problems, list) or not problems:
        raise IntakeError("extractor output must contain a non-empty problems array")
    statements = sorted(
        (normalize_problem(problem, blobs) for problem in problems),
        key=lambda item: (item["module"], item["theorem"]),
    )
    ids = [item["statement_id"] for item in statements]
    if len(ids) != len(set(ids)):
        raise IntakeError("duplicate theorem identity in extractor output")

    scope = lock["selection"]
    selected = set(scope["paths"])
    observed = {item["source_path"] for item in statements}
    if not observed.issubset(selected):
        raise IntakeError(f"extractor emitted paths outside locked selection: {sorted(observed - selected)}")

    snapshot = {
        "schema_version": "1.0.0",
        "snapshot_id": f"MF-FORMAL-SNAPSHOT-{lock['source_id']}-{scope['scope_id']}",
        "source_lock_id": lock["source_lock_id"],
        "source_id": lock["source_id"],
        "source_repository": lock["repository"]["full_name"],
        "source_commit": lock["revision"]["commit"],
        "scope": {"scope_id": scope["scope_id"], "paths": list(scope["paths"])},
        "generated_at": generated_at,
        "digest_contract": "sha256-canonical-json-v1",
        "snapshot_sha256": "",
        "statements": statements,
        "non_certification_statement": (
            "This snapshot is a source-identity and formulation artifact. Lean elaboration, upstream "
            "category labels, and sorry-free metadata do not by themselves establish truth or MATHCERT certification."
        ),
    }
    snapshot["snapshot_sha256"] = snapshot_digest(snapshot)
    return snapshot


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=False, ensure_ascii=True) + "\n", encoding="utf-8")


def run_extractor(checkout: Path, selected_paths: list[str], build: bool) -> dict[str, Any]:
    if build:
        commands = [
            ["lake", "exe", "cache", "get"],
            ["lake", "build", "FormalConjecturesAnswerPostpone"],
        ]
        for command in commands:
            try:
                subprocess.run(command, cwd=checkout, check=True)
            except (OSError, subprocess.CalledProcessError) as exc:
                raise IntakeError(f"command failed: {' '.join(command)}") from exc

    combined: list[dict[str, Any]] = []
    for path in selected_paths:
        command = ["lake", "exe", "extract_names", path]
        try:
            completed = subprocess.run(command, cwd=checkout, check=True, capture_output=True, text=True)
            output = json.loads(completed.stdout)
        except (OSError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
            raise IntakeError(f"extractor failed for {path}") from exc
        problems = output.get("problems")
        if not isinstance(problems, list):
            raise IntakeError(f"extractor output for {path} has no problems array")
        combined.extend(problems)
    return {"problems": combined}


def verify_snapshot(lock: dict[str, Any], snapshot: dict[str, Any]) -> None:
    if snapshot.get("source_lock_id") != lock.get("source_lock_id"):
        raise IntakeError("snapshot source_lock_id does not match lock")
    if snapshot.get("source_commit") != lock["revision"]["commit"]:
        raise IntakeError("snapshot source commit does not match lock")
    expected = snapshot_digest(snapshot)
    if snapshot.get("snapshot_sha256") != expected:
        raise IntakeError(
            f"snapshot digest mismatch: expected {expected}, found {snapshot.get('snapshot_sha256')}"
        )
    locked = artifact_blob_map(lock)
    for statement in snapshot.get("statements", []):
        path = statement.get("source_path")
        if locked.get(path) != statement.get("source_git_blob_sha1"):
            raise IntakeError(f"statement source identity mismatch: {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    normalize = sub.add_parser("normalize", help="normalize saved extractor JSON")
    normalize.add_argument("--source-lock", type=Path, required=True)
    normalize.add_argument("--extract-json", type=Path, required=True)
    normalize.add_argument("--output", type=Path, required=True)
    normalize.add_argument("--generated-at", required=True)

    intake = sub.add_parser("intake", help="verify a checkout, run extraction, and write a snapshot")
    intake.add_argument("--source-lock", type=Path, required=True)
    intake.add_argument("--checkout", type=Path, required=True)
    intake.add_argument("--output", type=Path, required=True)
    intake.add_argument("--generated-at", required=True)
    intake.add_argument("--skip-build", action="store_true")

    verify = sub.add_parser("verify", help="verify a committed snapshot")
    verify.add_argument("--source-lock", type=Path, required=True)
    verify.add_argument("--snapshot", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    lock = load_json(args.source_lock)
    blobs = artifact_blob_map(lock)

    if args.command == "normalize":
        snapshot = build_snapshot(lock, load_json(args.extract_json), blobs, args.generated_at)
        write_json(args.output, snapshot)
    elif args.command == "intake":
        verify_checkout(lock, args.checkout)
        extracted = run_extractor(args.checkout, lock["selection"]["paths"], not args.skip_build)
        snapshot = build_snapshot(lock, extracted, blobs, args.generated_at)
        write_json(args.output, snapshot)
    else:
        verify_snapshot(lock, load_json(args.snapshot))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except IntakeError as exc:
        print(f"formal-conjectures intake error: {exc}", file=sys.stderr)
        raise SystemExit(2)
