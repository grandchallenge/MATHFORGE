#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_module("vgse_archive_audit", ROOT / "tools" / "audit_vgse_arxiv_source_archive.py")
SEM = load_module("vgse_weight_semantics", ROOT / "tools" / "classify_vgse_varchenko_weight_semantics.py")


def canonical_sha256(value) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def expected_projection(source_archive: Path) -> dict:
    archive = AUDIT.build_record(source_archive)
    semantics = SEM.build_record(source_archive)
    inventory_by_path = {item["path"]: item for item in archive["member_inventory"]}
    assets = []
    for ref in archive["varchenko_figure_references"]:
        member = inventory_by_path[ref["resolved_member"]]
        meta = ref["asset_pdf_metadata"]
        assets.append(
            {
                "include_line": ref["line"],
                "target": ref["target"],
                "resolved_member": ref["resolved_member"],
                "sha256": member["sha256"],
                "size_bytes": member["size_bytes"],
                "creator": meta["creator"],
                "producer": meta["producer"],
                "generator_markers": meta["generator_markers"],
            }
        )
    relation_hashes = {str(item["line"]): item["line_sha256"] for item in semantics["relations"]}
    summary = semantics["summary"]
    return {
        "source": {
            "arxiv_id": archive["source"]["arxiv_id"],
            "acquisition_url": archive["source"]["acquisition_url"],
            "archive_sha256": archive["source"]["archive_sha256"],
            "archive_size_bytes": archive["source"]["archive_size_bytes"],
            "member_count": archive["member_count"],
            "member_inventory_canonical_sha256": canonical_sha256(archive["member_inventory"]),
        },
        "package_inventory": {
            "code_member_count": len(archive["code_members"]),
            "non_metadata_data_member_count": len(archive["data_members"]),
            "metadata_members": [
                {"path": item["path"], "sha256": item["sha256"], "size_bytes": item["size_bytes"]}
                for item in archive["metadata_members"]
            ],
        },
        "figure16_source_lineage": {
            "source_file": archive["varchenko_figure_references"][0]["source_file"],
            "assets": assets,
        },
        "varchenko_weight_semantics": {
            **summary,
            "relation_line_hashes": relation_hashes,
        },
    }


def validation_errors(source_archive: Path, record_path: Path) -> list[str]:
    errors: list[str] = []
    record = json.loads(record_path.read_text(encoding="utf-8"))
    observed = expected_projection(source_archive)
    for key in ("source", "package_inventory", "figure16_source_lineage", "varchenko_weight_semantics"):
        if record.get(key) != observed[key]:
            errors.append(f"{key} drift")
    finding = record.get("provider_finding", {})
    if finding.get("bundled_graph_or_weight_generation_code_found") is not False:
        errors.append("provider finding inflates bundled code")
    if finding.get("bundled_non_metadata_graph_or_weight_data_found") is not False:
        errors.append("provider finding inflates bundled data")
    if finding.get("explicit_numeric_weight_definition_in_varchenko_window_found") is not False:
        errors.append("provider finding inflates explicit numerical weights")
    if finding.get("exact_source_graph_weight_generation_bridge_found") is not False:
        errors.append("provider finding improperly claims source bridge")
    if finding.get("c06_reopening_effect") != "none_at_provider_stage":
        errors.append("provider finding improperly changes C06 state")
    if observed["varchenko_weight_semantics"]["weight_definition_candidate_lines"]:
        errors.append("source package now contains a weight-definition candidate")
    if observed["package_inventory"]["code_member_count"] or observed["package_inventory"]["non_metadata_data_member_count"]:
        errors.append("source package now contains code/data requiring renewed audit")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-archive", type=Path, required=True)
    parser.add_argument("--record", type=Path, required=True)
    args = parser.parse_args()
    errors = validation_errors(args.source_archive, args.record)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated VGSE arXiv v2 source archive provider record; no source-package C06 bridge found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
