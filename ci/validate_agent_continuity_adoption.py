#!/usr/bin/env python3
"""Validate MATHFORGE adoption of GCL-AGENT-CONTINUITY-001."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ADOPTION_REL = ".gcl/agent-continuity.json"
AGENTS_REL = "AGENTS.md"

EXPECTED = {
    "policy_id": "GCL-AGENT-CONTINUITY-001",
    "version": "1.0.0",
    "repository": "grandchallenge/MATHFORGE",
    "specialization": "MATHFORGE-PROVENANCE-CONTINUITY-001",
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

def adoption_errors(record: dict[str, Any], agents_text: str) -> list[str]:
    errors: list[str] = []
    for key, value in EXPECTED.items():
        if record.get(key) != value:
            errors.append(f"{key}: expected {value!r}, found {record.get(key)!r}")
    if record.get("required") is not True:
        errors.append("required must be true")

    applicability = record.get("applicability", {})
    if applicability.get("interruption_prone_discovery_or_reconstruction") is not True:
        errors.append("interruption-prone discovery/reconstruction must be in scope")
    if applicability.get("routine_short_operations_checkpoint_required") is not False:
        errors.append("routine short operations must not be universally checkpoint-required")

    checkpoint = record.get("checkpoint_requirements", {})
    for key in REQUIRED_CHECKPOINT_FIELDS:
        if checkpoint.get(key) is not True:
            errors.append(f"checkpoint_requirements.{key} must be true")

    authority = record.get("authority_preservation", {})
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
    for token in required_agent_tokens:
        if token not in agents_text:
            errors.append(f"AGENTS.md missing Forge continuity binding token: {token}")

    return errors

def repository_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
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
    return adoption_errors(record, agents_path.read_text(encoding="utf-8"))

def main() -> int:
    errors = repository_errors()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("MATHFORGE GCL-AGENT-CONTINUITY-001 adoption: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
