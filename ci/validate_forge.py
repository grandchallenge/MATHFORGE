#!/usr/bin/env python3
"""Validate MATHFORGE artifacts, provider manifests, and coverage contracts."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
MANIFEST_DIR = ROOT / "provider_manifests"
COVERAGE_PATH = ROOT / "governance" / "provider_coverage.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def schema_path(name: str) -> Path:
    candidates = [
        WORKSPACE / "MATH-PROGRAMME" / "schemas" / name,
        WORKSPACE / "schemas" / name,
        ROOT / "schemas" / name,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(name)


def validate(instance: Any, schema_name: str, label: str) -> list[str]:
    schema = load_json(schema_path(schema_name))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{label}: {error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def programme_refs() -> tuple[set[str], set[str], set[str]]:
    graph_path = WORKSPACE / "MATH-PROGRAMME" / "knowledge_graph" / "union_closed.json"
    mappings_path = WORKSPACE / "MATH-PROGRAMME" / "classification" / "mappings" / "union_closed.json"
    sources_path = WORKSPACE / "MATH-PROGRAMME" / "classification" / "source_registry.json"
    if graph_path.exists() and mappings_path.exists() and sources_path.exists():
        graph = load_json(graph_path)
        mappings = load_json(mappings_path)
        sources = load_json(sources_path)
        return (
            {node["node_id"] for node in graph["nodes"]},
            {mapping["mapping_id"] for mapping in mappings["mappings"]},
            {source["source_id"] for source in sources["sources"]},
        )
    contract = load_json(ROOT / "contracts" / "classification_discovery_refs.json")
    return (
        set(contract["knowledge_graph_refs"]),
        set(contract["classification_mapping_refs"]),
        set(contract["source_ids"]),
    )


def legacy_artifact_errors() -> list[str]:
    errors: list[str] = []
    graph_refs, mapping_refs, source_ids = programme_refs()
    for path in ROOT.rglob("*.json"):
        try:
            load_json(path)
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    for path in (ROOT / "reports" / "problem_cards").glob("*.json"):
        candidate = load_json(path)
        errors.extend(validate(candidate, "candidate_problem.schema.json", str(path.relative_to(ROOT))))
        for graph_ref in candidate.get("knowledge_graph_refs", []):
            if graph_ref not in graph_refs:
                errors.append(f"{path.relative_to(ROOT)}: unresolved knowledge_graph_ref {graph_ref}")
        for mapping_ref in candidate.get("classification_mapping_refs", []):
            if mapping_ref not in mapping_refs:
                errors.append(f"{path.relative_to(ROOT)}: unresolved classification_mapping_ref {mapping_ref}")
        for source_id in candidate.get("discovery_provenance", {}).get("source_ids", []):
            if source_id not in source_ids:
                errors.append(f"{path.relative_to(ROOT)}: unknown discovery source_id {source_id}")
    for path in (ROOT / "reports" / "discovery").glob("*.json"):
        errors.extend(validate(load_json(path), "discovery_record.schema.json", str(path.relative_to(ROOT))))
    return errors


def provider_contract_errors() -> list[str]:
    errors: list[str] = []
    coverage = load_json(COVERAGE_PATH)
    errors.extend(validate(coverage, "provider_coverage.schema.json", str(COVERAGE_PATH.relative_to(ROOT))))

    entries = coverage.get("active_campaigns", [])
    campaign_ids = [entry.get("campaign_id") for entry in entries]
    if len(campaign_ids) != len(set(campaign_ids)):
        errors.append("governance/provider_coverage.json: duplicate campaign_id")

    registered = {
        entry["manifest_path"]
        for entry in entries
        if entry.get("disposition") == "manifest" and isinstance(entry.get("manifest_path"), str)
    }
    discovered = {
        path.relative_to(ROOT).as_posix()
        for path in MANIFEST_DIR.rglob("*.json")
    }
    for missing in sorted(registered - discovered):
        errors.append(f"provider coverage: registered manifest is missing: {missing}")
    for orphan in sorted(discovered - registered):
        errors.append(f"provider coverage: unregistered manifest: {orphan}")

    manifest_ids: list[str] = []
    manifest_campaigns: list[str] = []
    for relative in sorted(registered & discovered):
        path = ROOT / relative
        manifest = load_json(path)
        errors.extend(validate(manifest, "provider_campaign_manifest.schema.json", relative))
        manifest_ids.append(str(manifest.get("manifest_id", "")))
        manifest_campaigns.append(str(manifest.get("campaign_id", "")))

        entry = next((item for item in entries if item.get("manifest_path") == relative), None)
        if entry and manifest.get("campaign_id") != entry.get("campaign_id"):
            errors.append(f"{relative}: campaign_id does not match coverage registry")

        for artifact in manifest.get("artifacts", []):
            ownership = artifact.get("ownership")
            artifact_path = artifact.get("path")
            if ownership == "MATHFORGE":
                local = ROOT / str(artifact_path)
                if not local.is_file():
                    errors.append(f"{relative}: missing local artifact {artifact_path}")
                    continue
                integrity = artifact.get("integrity", {})
                algorithm = integrity.get("algorithm")
                expected = integrity.get("value")
                actual = git_blob_sha1(local) if algorithm == "git_blob_sha1" else sha256(local)
                if actual != expected:
                    errors.append(
                        f"{relative}: {artifact_path} {algorithm} mismatch; expected {expected}, found {actual}"
                    )
            elif ownership == "MATH-PROGRAMME" and manifest.get("coverage_mode") != "retrospective":
                errors.append(f"{relative}: Programme-owned artifact is allowed only in retrospective coverage")

        programme = manifest.get("programme", {})
        if not isinstance(programme.get("commit"), str) or len(programme["commit"]) != 40:
            errors.append(f"{relative}: Programme commit must be a full 40-character identity")

    for label, values in (("manifest_id", manifest_ids), ("campaign_id", manifest_campaigns)):
        duplicates = sorted({value for value in values if values.count(value) > 1})
        for duplicate in duplicates:
            errors.append(f"provider manifests: duplicate {label} {duplicate}")

    manifest_campaign_set = set(manifest_campaigns)
    registry_manifest_set = {
        entry.get("campaign_id")
        for entry in entries
        if entry.get("disposition") == "manifest"
    }
    if manifest_campaign_set != registry_manifest_set:
        errors.append("provider coverage: manifest campaign set does not match registry campaign set")
    return errors


def main() -> int:
    errors = legacy_artifact_errors()
    errors.extend(provider_contract_errors())
    for schema in sorted((ROOT / "schemas").glob("*.json")):
        Draft202012Validator.check_schema(load_json(schema))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"MATHFORGE validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("MATHFORGE JSON, discovery, provider coverage, artifact identity, and handoff contracts are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
