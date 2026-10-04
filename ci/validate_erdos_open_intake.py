#!/usr/bin/env python3
"""Fail-closed validator for ERDOS-OPEN-001."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sources" / "ERDOS-OPEN-001"
LOCK_PATH = BASE / "source_lock.json"
MANIFEST_PATH = BASE / "open_problem_manifest.json"
FC_INDEX_PATH = BASE / "protected_fc_index.json"
REGISTRY_PATH = BASE / "upstream" / "problems.yaml"
REGISTRY_SCHEMA_PATH = BASE / "upstream" / "problems.schema.json"
SCHEMA_PATH = ROOT / "schemas" / "erdos_open_intake.schema.json"
SPECIAL_STATES = ("decidable", "falsifiable", "verifiable", "not provable", "not disprovable", "independent")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    payload = b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    return hashlib.sha1(payload).hexdigest()


def scalar(value: str) -> Any:
    value = value.strip()
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def parse_registry(text: str) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    section: str | None = None
    nested = {"informal_status", "formal_status", "status", "formalized"}
    for line in text.splitlines():
        match = re.match(r"^- number:\s*(.+)$", line)
        if match:
            if current is not None:
                records.append(current)
            current = {"number": scalar(match.group(1))}
            section = None
            continue
        if current is None:
            continue
        match = re.match(r"^  ([a-z_]+):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            if key in nested and value == "":
                section = key
                current[key] = {}
            else:
                section = None
                current[key] = scalar(value)
            continue
        match = re.match(r"^    ([a-z_]+):\s*(.*)$", line)
        if match and section:
            key, value = match.groups()
            current[section][key] = scalar(value)
    if current is not None:
        records.append(current)
    return records


def build_expected(lock: dict[str, Any], records: list[dict[str, Any]], fc_index: dict[str, Any]) -> dict[str, Any]:
    fc_by_id = {item["problem_id"]: item for item in fc_index["entries"]}
    special_counts = {
        state: sum(1 for item in records if item.get("informal_status", {}).get("state") == state)
        for state in SPECIAL_STATES
    }
    entries: list[dict[str, Any]] = []
    for record in records:
        if record.get("informal_status", {}).get("state") != "open":
            continue
        problem_id = str(record["number"])
        protected = fc_by_id.get(problem_id)
        statement_state = record.get("formalized", {}).get("state", "no")
        solution_state = record.get("formal_status", {}).get("state", "unformalized")
        if protected:
            disposition = "OPEN_WITH_PROTECTED_FC_FORMALIZATION"
            protected_record = {
                "present": True,
                "path": protected["path"],
                "git_blob_sha1": protected["git_blob_sha1"],
            }
        elif statement_state == "yes":
            disposition = "OPEN_WITH_REGISTRY_REPORTED_FORMALIZATION_NOT_IN_PROTECTED_FC_SNAPSHOT"
            protected_record = {"present": False, "path": None, "git_blob_sha1": None}
        else:
            disposition = "OPEN_WITHOUT_REGISTRY_REPORTED_FORMALIZATION"
            protected_record = {"present": False, "path": None, "git_blob_sha1": None}
        entries.append({
            "problem_id": problem_id,
            "site_url": f"https://www.erdosproblems.com/{problem_id}",
            "prize": record.get("prize"),
            "tags": record.get("tags", []) if isinstance(record.get("tags", []), list) else [],
            "registry_status": {
                "state": "open",
                "last_update": record.get("informal_status", {}).get("last_update"),
            },
            "registry_solution_formalized": {
                "state": solution_state,
                "last_update": record.get("formal_status", {}).get("last_update"),
            },
            "registry_statement_formalized": {
                "state": statement_state,
                "last_update": record.get("formalized", {}).get("last_update"),
            },
            "protected_fc": protected_record,
            "gcl_disposition": disposition,
            "programme_triage_state": (
                "HOLD_PENDING_REGISTRY_STATUS_RECONCILIATION"
                if solution_state == "Lean"
                else "ELIGIBLE_FOR_PROGRAMME_TRIAGE"
            ),
            "solve_eligibility": "REQUIRES_PROGRAMME_SELECTION",
        })

    summary = {
        "registry_problem_count": len(records),
        "strict_open_count": len(entries),
        "strict_open_with_protected_fc_formalization": sum(1 for item in entries if item["protected_fc"]["present"]),
        "strict_open_with_registry_reported_formalization_not_in_protected_fc_snapshot": sum(
            1 for item in entries
            if item["gcl_disposition"] == "OPEN_WITH_REGISTRY_REPORTED_FORMALIZATION_NOT_IN_PROTECTED_FC_SNAPSHOT"
        ),
        "strict_open_without_registry_reported_formalization": sum(
            1 for item in entries if item["gcl_disposition"] == "OPEN_WITHOUT_REGISTRY_REPORTED_FORMALIZATION"
        ),
        "strict_open_with_formal_solution_pending_human_status_reconciliation": sum(
            1 for item in entries if item["registry_solution_formalized"]["state"] == "Lean"
        ),
        "excluded_special_unresolved_status_count": sum(special_counts.values()),
        "excluded_special_unresolved_statuses": special_counts,
    }
    return {
        "schema_version": "1.0.0",
        "intake_id": "ERDOS-OPEN-001",
        "source_lock_id": lock["source_lock_id"],
        "generated_on": lock["generated_on"],
        "selection": {
            "registry_field": "informal_status.state",
            "included_state": "open",
            "interpretation": "Strict open intake only. Special unresolved computational or independence statuses are recorded in the summary but are not included as strict-open rows.",
        },
        "summary": summary,
        "entries": entries,
        "authority_boundary": {
            "registry_status_is_evidence_not_gcl_mathematical_adjudication": True,
            "protected_fc_presence_is_statement_source_identity_not_proof": True,
            "solve_authorized": False,
            "certification_authorized": False,
            "promotion_authorized": False,
        },
    }


def validation_errors(lock: Any, manifest: Any, fc_index: Any, schema: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(lock, dict) or not isinstance(manifest, dict) or not isinstance(fc_index, dict):
        return ["lock, manifest, and FC index must all be objects"]

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors.extend(
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(manifest), key=lambda item: list(item.path))
    )

    artifacts = lock.get("artifacts", {})
    for key, path in (
        ("registry_snapshot_git_blob_sha1", REGISTRY_PATH),
        ("registry_schema_snapshot_git_blob_sha1", REGISTRY_SCHEMA_PATH),
        ("protected_fc_index_git_blob_sha1", FC_INDEX_PATH),
        ("open_manifest_git_blob_sha1", MANIFEST_PATH),
    ):
        expected = artifacts.get(key)
        actual = git_blob_sha1(path)
        if expected != actual:
            errors.append(f"{key} mismatch: expected {expected}, found {actual}")

    registry = lock.get("registry_source", {})
    if registry.get("data_git_blob_sha1") != git_blob_sha1(REGISTRY_PATH):
        errors.append("registry snapshot does not preserve the locked upstream data blob")
    if registry.get("schema_git_blob_sha1") != git_blob_sha1(REGISTRY_SCHEMA_PATH):
        errors.append("registry schema snapshot does not preserve the locked upstream schema blob")
    if registry.get("repository") != "teorth/erdosproblems":
        errors.append("registry repository identity drifted")
    if registry.get("website") != "https://www.erdosproblems.com/":
        errors.append("registry website locator drifted")

    provider = lock.get("protected_formal_provider", {})
    if provider.get("provider_snapshot_id") != "FC-GDM-85F86371":
        errors.append("protected FC provider snapshot identity drifted")
    if fc_index.get("provider_snapshot_id") != provider.get("provider_snapshot_id"):
        errors.append("FC index provider snapshot mismatch")
    if fc_index.get("source_commit") != provider.get("source_commit"):
        errors.append("FC index source commit mismatch")
    if fc_index.get("erdos_directory_tree_sha1") != provider.get("erdos_directory_tree_sha1"):
        errors.append("FC index directory tree identity mismatch")
    if fc_index.get("lean_file_count") != provider.get("lean_file_count"):
        errors.append("FC index file count mismatch")
    if len(fc_index.get("entries", [])) != provider.get("lean_file_count"):
        errors.append("FC index entries do not match locked file count")

    fc_ids = [item.get("problem_id") for item in fc_index.get("entries", [])]
    if len(fc_ids) != len(set(fc_ids)):
        errors.append("FC index contains duplicate problem identities")
    for item in fc_index.get("entries", []):
        problem_id = str(item.get("problem_id", ""))
        if item.get("path") != f"FormalConjectures/ErdosProblems/{problem_id}.lean":
            errors.append(f"FC index path mismatch for problem {problem_id}")
        if not re.fullmatch(r"[0-9a-f]{40}", str(item.get("git_blob_sha1", ""))):
            errors.append(f"FC index blob identity malformed for problem {problem_id}")

    records = parse_registry(REGISTRY_PATH.read_text(encoding="utf-8"))
    expected_manifest = build_expected(lock, records, fc_index)
    if manifest != expected_manifest:
        errors.append("committed manifest is not the deterministic strict-open projection of the locked registry and protected FC index")

    if lock.get("counts") != expected_manifest["summary"]:
        errors.append("source-lock counts do not match the deterministic manifest summary")

    boundary = lock.get("authority_boundary", {})
    for key in ("solve_authorized", "certification_authorized", "automatic_upstream_refresh"):
        if boundary.get(key) is not False:
            errors.append(f"source-lock authority boundary {key} must remain false")
    if boundary.get("current_status_authority_retained_by_math_programme") is not True:
        errors.append("MATH-PROGRAMME current-status authority must remain explicit")
    return errors


def main() -> int:
    errors = validation_errors(
        load_json(LOCK_PATH),
        load_json(MANIFEST_PATH),
        load_json(FC_INDEX_PATH),
        load_json(SCHEMA_PATH),
    )
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"ERDOS-OPEN-001 validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    manifest = load_json(MANIFEST_PATH)
    summary = manifest["summary"]
    print(
        "ERDOS-OPEN-001 valid: "
        f"{summary['strict_open_count']} strict-open records; "
        f"{summary['strict_open_with_protected_fc_formalization']} protected FC; "
        f"{summary['strict_open_with_registry_reported_formalization_not_in_protected_fc_snapshot']} registry-formalized outside protected FC; "
        f"{summary['strict_open_without_registry_reported_formalization']} without registry-reported statement formalization"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
