#!/usr/bin/env python3
"""Validate MATHFORGE JSON and programme-owned artifact contracts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent


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


def validate(path: Path, schema_name: str) -> list[str]:
    instance = json.loads(path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path(schema_name).read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [f"{path}: {error.json_path}: {error.message}" for error in validator.iter_errors(instance)]


def programme_refs() -> tuple[set[str], set[str], set[str]]:
    graph_path = WORKSPACE / "MATH-PROGRAMME" / "knowledge_graph" / "union_closed.json"
    mappings_path = (
        WORKSPACE / "MATH-PROGRAMME" / "classification" / "mappings" / "union_closed.json"
    )
    sources_path = (
        WORKSPACE / "MATH-PROGRAMME" / "classification" / "source_registry.json"
    )
    if graph_path.exists() and mappings_path.exists() and sources_path.exists():
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        mappings = json.loads(mappings_path.read_text(encoding="utf-8"))
        sources = json.loads(sources_path.read_text(encoding="utf-8"))
        return (
            {node["node_id"] for node in graph["nodes"]},
            {mapping["mapping_id"] for mapping in mappings["mappings"]},
            {source["source_id"] for source in sources["sources"]},
        )
    contract = json.loads(
        (ROOT / "contracts" / "classification_discovery_refs.json").read_text(encoding="utf-8")
    )
    return (
        set(contract["knowledge_graph_refs"]),
        set(contract["classification_mapping_refs"]),
        set(contract["source_ids"]),
    )


def main() -> int:
    errors = []
    graph_refs, mapping_refs, source_ids = programme_refs()
    for path in ROOT.rglob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    for path in (ROOT / "reports" / "problem_cards").glob("*.json"):
        errors.extend(validate(path, "candidate_problem.schema.json"))
        candidate = json.loads(path.read_text(encoding="utf-8"))
        for graph_ref in candidate.get("knowledge_graph_refs", []):
            if graph_ref not in graph_refs:
                errors.append(f"{path}: unresolved knowledge_graph_ref {graph_ref}")
        for mapping_ref in candidate.get("classification_mapping_refs", []):
            if mapping_ref not in mapping_refs:
                errors.append(f"{path}: unresolved classification_mapping_ref {mapping_ref}")
        for source_id in candidate.get("discovery_provenance", {}).get("source_ids", []):
            if source_id not in source_ids:
                errors.append(f"{path}: unknown discovery source_id {source_id}")
    for path in (ROOT / "reports" / "discovery").glob("*.json"):
        errors.extend(validate(path, "discovery_record.schema.json"))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("MATHFORGE JSON and governed artifacts are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
