#!/usr/bin/env python3
"""Validate MATHFORGE adoption of GCL-AGENT-CONTINUITY-001."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
ADOPTION_REL = ".gcl/agent-continuity.json"
AGENTS_REL = "AGENTS.md"
SCHEMA_REL = "schemas/agent_continuity_adoption.schema.json"

SCHEMA_AUTHORITY_COMMIT = "7e6b61ddf77e2d73309657d089a98cae84cc735f"
SCHEMA_BLOB_SHA = "b019881a54763a949613c8116260b729742867bd"
LOCAL_VALIDATOR = "ci/validate_agent_continuity_adoption.py"

EXPECTED = {
    "repository": "grandchallenge/MATHFORGE",
    "specialization": "MATHFORGE-PROVENANCE-CONTINUITY-001",
    "local_validator": LOCAL_VALIDATOR,
}
EXPECTED_SCHEMA_BINDING = {
    "authority_commit": SCHEMA_AUTHORITY_COMMIT,
    "schema_blob_sha": SCHEMA_BLOB_SHA,
    "local_snapshot": SCHEMA_REL,
    "local_snapshot_authoritative": False,
    "mutable_remote_fetch_allowed": False,
}

REQUIRED_CHECKPOINT_FIELDS = (
    "source_or_provider_identity",
    "acquired_byte_digests_or_immutable_source_refs",
    "provider_manifest_state",
    "transcribed_normalized_reconstructed_distinction",
    "search_or_reconstruction_parameters",
    "generated_witness_identities",
    "failed_searches_or_ruled_out_routes",
    "deterministic_next_evidence_action",
)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha(path: Path) -> str:
    payload = path.read_bytes()
    header = f"blob {len(payload)}\0".encode("utf-8")
    return hashlib.sha1(header + payload).hexdigest()


def common_schema_errors(record: dict[str, Any], root: Path = ROOT) -> list[str]:
    schema_path = root / SCHEMA_REL
    if not schema_path.is_file():
        return [f"missing pinned common adoption schema: {SCHEMA_REL}"]

    observed_blob = git_blob_sha(schema_path)
    if observed_blob != SCHEMA_BLOB_SHA:
        return [
            f"pinned schema blob mismatch: expected {SCHEMA_BLOB_SHA}, found {observed_blob}"
        ]

    try:
        schema = load_json(schema_path)
        Draft202012Validator.check_schema(schema)
    except Exception as exc:
        return [f"invalid pinned common adoption schema: {exc}"]

    validator = Draft202012Validator(schema)
    return [
        f"common schema {error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(record), key=lambda item: list(item.path))
    ]


def adoption_errors(record: dict[str, Any], agents_text: str, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    errors.extend(common_schema_errors(record, root))

    for key, value in EXPECTED.items():
        if record.get(key) != value:
            errors.append(f"{key}: expected {value!r}, found {record.get(key)!r}")

    specialization_data = record.get("specialization_data", {})
    if not isinstance(specialization_data, dict):
        errors.append("specialization_data must be an object")
        specialization_data = {}

    binding = specialization_data.get("schema_binding", {})
    if not isinstance(binding, dict):
        errors.append("specialization_data.schema_binding must be an object")
        binding = {}
    for key, value in EXPECTED_SCHEMA_BINDING.items():
        if binding.get(key) != value:
            errors.append(
                f"specialization_data.schema_binding.{key}: expected {value!r}, "
                f"found {binding.get(key)!r}"
            )

    applicability = specialization_data.get("applicability", {})
    if not isinstance(applicability, dict):
        errors.append("specialization_data.applicability must be an object")
        applicability = {}
    if applicability.get("interruption_prone_discovery_or_reconstruction") is not True:
        errors.append("interruption-prone discovery/reconstruction must be in scope")
    if applicability.get("routine_short_operations_checkpoint_required") is not False:
        errors.append("routine short operations must not be universally checkpoint-required")

    checkpoint = specialization_data.get("checkpoint_requirements", {})
    if not isinstance(checkpoint, dict):
        errors.append("specialization_data.checkpoint_requirements must be an object")
        checkpoint = {}
    for key in REQUIRED_CHECKPOINT_FIELDS:
        if checkpoint.get(key) is not True:
            errors.append(f"checkpoint_requirements.{key} must be true")

    unexpected_specialization = set(specialization_data) - {
        "schema_binding",
        "applicability",
        "checkpoint_requirements",
    }
    if unexpected_specialization:
        errors.append(
            "unexpected Forge specialization_data fields: "
            + ", ".join(sorted(unexpected_specialization))
        )

    authority = record.get("authority_preservation", {})
    if not isinstance(authority, dict):
        errors.append("authority_preservation must be an object")
        authority = {}
    expected_authority = {
        "authority_changed": False,
        "discovery_evidence_is_proof": False,
        "certification_authority_changed": False,
        "promotion_authority_changed": False,
        "independent_verification_inherited_across_agent_substitution": False,
    }
    for key, value in expected_authority.items():
        if authority.get(key) is not value:
            errors.append(f"authority_preservation.{key} must be {value!r}")

    required_agent_tokens = (
        "GCL-AGENT-CONTINUITY-001@1.0.0",
        "source/provider identity",
        "discovery evidence and generated witnesses are not proof, certification, or promotion",
        "agent substitution",
    )
    agents_lower = agents_text.lower()
    for token in required_agent_tokens:
        if token.lower() not in agents_lower:
            errors.append(f"AGENTS.md missing Forge continuity binding token: {token}")

    return errors


def repository_errors(root: Path = ROOT) -> list[str]:
    adoption_path = root / ADOPTION_REL
    agents_path = root / AGENTS_REL
    if not adoption_path.is_file():
        return [f"missing required adoption record: {ADOPTION_REL}"]
    if not agents_path.is_file():
        return [f"missing required agent instructions: {AGENTS_REL}"]
    try:
        record = load_json(adoption_path)
    except Exception as exc:
        return [f"invalid adoption JSON: {exc}"]
    if not isinstance(record, dict):
        return ["adoption record must be an object"]
    return adoption_errors(record, agents_path.read_text(encoding="utf-8"), root)


def main() -> int:
    errors = repository_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(
        "MATHFORGE GCL-AGENT-CONTINUITY-001 adoption: PASS "
        f"(INTELLECT schema {SCHEMA_AUTHORITY_COMMIT}:{SCHEMA_BLOB_SHA})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
