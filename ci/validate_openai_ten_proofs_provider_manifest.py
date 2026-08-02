#!/usr/bin/env python3
"""Validate the bounded OpenAI ten-proofs provider-manifest revision update."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "provider_manifests/OPENAI-TEN-PROOFS-001.json"
SCHEMA_PATH = ROOT / "schemas/provider_campaign_manifest.schema.json"
AUDIT_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/source_revision_audits/OTP-TRANCHE-001.json"

ADMITTED_SHA = "f318c6508c9d49ef876a5a26cd73928705f96c07bb43e92a0cb35bd3f666ea53"
OBSERVED_SHA = "64b900d5fae6fe22f2ae1b8e3b712d20055194a6c81cf343a2455e5898ac7dd6"
AUDIT_MERGE = "a498ef40b7652b55bf121b5682604e259b8d3073"
AUDIT_BLOB = "80d473b1b545fd9ca05fc5200bcf70ff5f9fcb05"
CERT_REPLAY_MERGE = "563c29c9687aad1bd06330436e3056cce7745c93"
EXPECTED_FAMILIES = {
    "OTP-F-EHRHART",
    "OTP-J1-COMPACTNESS",
    "OTP-J2-TWO-DEGENERATE",
}
EXPECTED_SEMANTIC_ARTIFACTS = {
    "OPENAI-TEN-PROOFS-001-SEMANTIC-EHRHART": (
        "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-F-EHRHART.json",
        "a3dc4de4c38a80b7aec1fae6506b08e14d2e58bb",
    ),
    "OPENAI-TEN-PROOFS-001-SEMANTIC-COMPACTNESS": (
        "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J1-COMPACTNESS.json",
        "659396358d0d999c00011645f72602f30ccf6b0e",
    ),
    "OPENAI-TEN-PROOFS-001-SEMANTIC-TWO-DEGENERATE": (
        "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J2-TWO-DEGENERATE.json",
        "7bd168c46921f64364b20021b6315d68f0fde7d0",
    ),
}
REQUIRED_SOURCE_RECORDS = {
    "OPENAI-TEN-PROOFS-001-ADMITTED-MANUSCRIPT-REVISION",
    "OPENAI-TEN-PROOFS-001-OBSERVED-MANUSCRIPT-REVISION",
    "OPENAI-TEN-PROOFS-001-REASONING-NOTES",
    "OPENAI-TEN-PROOFS-001-BOUNDED-REVISION-AUDIT",
}
REQUIRED_STATUS_RECORDS = {
    "OPENAI-TEN-PROOFS-001-PROTECTED-SEMANTIC-TRANCHE",
    "OPENAI-TEN-PROOFS-001-CURRENT-REVISION-LOCUS-TRANCHE",
    "OPENAI-TEN-PROOFS-001-MATHCERT-REPLAY-EVIDENCE",
    "OPENAI-TEN-PROOFS-001-ROUTE-STATE",
    "OPENAI-TEN-PROOFS-001-BLOCKED-FAMILIES",
    "OPENAI-TEN-PROOFS-001-AGGREGATE-INTEGRATION",
}
REQUIRED_FAILED_ROUTES = {
    "OPENAI-TEN-PROOFS-001-ALL-IMPORT-FAILED",
    "OPENAI-TEN-PROOFS-001-PERMANENT-ROUTE-BLOCKED",
    "OPENAI-TEN-PROOFS-001-GAPCVP-ROUTE-BLOCKED",
    "OPENAI-TEN-PROOFS-001-NINE-FAMILY-REVISION-ROUTE-BLOCKED",
    "OPENAI-TEN-PROOFS-001-THREE-FAMILY-ROUTE-NOT-REGISTERED",
    "OPENAI-TEN-PROOFS-001-AGGREGATE-ROUTE-PROHIBITED",
}
REQUIRED_DEBT = {
    "OPENAI-TEN-PROOFS-001-UPSTREAM-AGGREGATE-DEBT",
    "OPENAI-TEN-PROOFS-001-PERMANENT-COVERAGE-DEBT",
    "OPENAI-TEN-PROOFS-001-GAPCVP-DEFINITION-DEBT",
    "OPENAI-TEN-PROOFS-001-REMAINING-CONCORDANCE-DEBT",
    "OPENAI-TEN-PROOFS-001-WHOLE-DOCUMENT-REVISION-DEBT",
}
FORBIDDEN_ROUTE_IDS = {
    "MC-ROUTE-OTP-F-EHRHART",
    "MC-ROUTE-OTP-J1-COMPACTNESS",
    "MC-ROUTE-OTP-J2-TWO-DEGENERATE",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(
        f"blob {len(data)}\0".encode("ascii") + data,
        usedforsecurity=False,
    ).hexdigest()


def by_id(document: dict[str, Any], field: str, key: str) -> dict[str, dict[str, Any]]:
    records = document.get(field, [])
    if not isinstance(records, list):
        return {}
    return {
        str(item.get(key)): item
        for item in records
        if isinstance(item, dict) and isinstance(item.get(key), str)
    }


def validation_errors(
    manifest: dict[str, Any] | None = None,
    audit: dict[str, Any] | None = None,
    audit_blob: str | None = None,
    semantic_blobs: dict[str, str] | None = None,
) -> list[str]:
    errors: list[str] = []
    manifest = load_json(MANIFEST_PATH) if manifest is None else manifest
    audit = load_json(AUDIT_PATH) if audit is None else audit
    audit_blob = git_blob_sha1(AUDIT_PATH) if audit_blob is None else audit_blob

    schema = load_json(SCHEMA_PATH)
    for error in sorted(
        Draft202012Validator(schema).iter_errors(manifest),
        key=lambda item: list(item.path),
    ):
        errors.append(f"manifest schema: {error.json_path}: {error.message}")

    if manifest.get("manifest_id") != "MF-OPENAI-TEN-PROOFS-001-MANIFEST":
        errors.append("manifest identity drift")
    if manifest.get("campaign_id") != "OPENAI-TEN-PROOFS-001":
        errors.append("campaign identity drift")

    serialized = json.dumps(manifest, sort_keys=True)
    if ADMITTED_SHA not in serialized:
        errors.append("admitted manuscript identity removed")
    if OBSERVED_SHA not in serialized:
        errors.append("observed manuscript revision missing")
    for route_id in FORBIDDEN_ROUTE_IDS:
        if route_id in serialized:
            errors.append(f"forbidden route registered: {route_id}")
    if '"may_adjudicate": true' in serialized.lower():
        errors.append("adjudication authority promoted")
    if '"mathematical_target_proved": true' in serialized.lower():
        errors.append("mathematical target promoted")

    if audit_blob != AUDIT_BLOB:
        errors.append("merged audit blob drift")
    disposition = audit.get("disposition", {})
    if disposition.get("whole_document_byte_equivalence") != "not_established":
        errors.append("whole-document byte equivalence inflated")
    if disposition.get("whole_document_semantic_equivalence") != "not_established":
        errors.append("whole-document semantic equivalence inflated")
    if disposition.get("family_locus_clear_count_after_activation") != 3:
        errors.append("activated family count drift")
    if disposition.get("unexamined_result_family_count") != 9:
        errors.append("unexamined family count drift")
    audit_families = {
        item.get("result_family")
        for item in audit.get("families", [])
        if isinstance(item, dict)
    }
    if audit_families != EXPECTED_FAMILIES:
        errors.append("audit family membership drift")

    artifacts = by_id(manifest, "artifacts", "artifact_id")
    audit_artifact = artifacts.get("OPENAI-TEN-PROOFS-001-SOURCE-REVISION-AUDIT", {})
    if audit_artifact.get("path") != AUDIT_PATH.relative_to(ROOT).as_posix():
        errors.append("audit artifact path drift")
    if audit_artifact.get("integrity") != {
        "algorithm": "git_blob_sha1",
        "value": AUDIT_BLOB,
    }:
        errors.append("audit artifact blob binding drift")

    if semantic_blobs is None:
        semantic_blobs = {
            artifact_id: git_blob_sha1(ROOT / path)
            for artifact_id, (path, _) in EXPECTED_SEMANTIC_ARTIFACTS.items()
        }
    for artifact_id, (path, blob) in EXPECTED_SEMANTIC_ARTIFACTS.items():
        artifact = artifacts.get(artifact_id, {})
        if artifact.get("path") != path:
            errors.append(f"{artifact_id}: path drift")
        if artifact.get("integrity") != {
            "algorithm": "git_blob_sha1",
            "value": blob,
        }:
            errors.append(f"{artifact_id}: manifest blob drift")
        if semantic_blobs.get(artifact_id) != blob:
            errors.append(f"{artifact_id}: repository blob drift")

    source_records = by_id(manifest, "source_records", "record_id")
    if not REQUIRED_SOURCE_RECORDS.issubset(source_records):
        errors.append("required source records missing")
    admitted = str(source_records.get("OPENAI-TEN-PROOFS-001-ADMITTED-MANUSCRIPT-REVISION", {}).get("summary", ""))
    observed = str(source_records.get("OPENAI-TEN-PROOFS-001-OBSERVED-MANUSCRIPT-REVISION", {}).get("summary", ""))
    bounded = str(source_records.get("OPENAI-TEN-PROOFS-001-BOUNDED-REVISION-AUDIT", {}).get("summary", ""))
    if ADMITTED_SHA not in admitted or "not replaced" not in admitted:
        errors.append("admitted revision historical authority drift")
    if OBSERVED_SHA not in observed or "alongside, not in place of" not in observed:
        errors.append("observed revision separation drift")
    for required in (
        AUDIT_MERGE,
        AUDIT_BLOB,
        "Whole-document byte equivalence",
        "whole-document semantic equivalence remain not established",
        "proof bodies were not compared in full",
    ):
        if required not in bounded:
            errors.append(f"bounded audit summary missing: {required}")

    status = by_id(manifest, "status_records", "record_id")
    if not REQUIRED_STATUS_RECORDS.issubset(status):
        errors.append("required status records missing")
    semantic = str(status.get("OPENAI-TEN-PROOFS-001-PROTECTED-SEMANTIC-TRANCHE", {}).get("summary", ""))
    revision = str(status.get("OPENAI-TEN-PROOFS-001-CURRENT-REVISION-LOCUS-TRANCHE", {}).get("summary", ""))
    replay = str(status.get("OPENAI-TEN-PROOFS-001-MATHCERT-REPLAY-EVIDENCE", {}).get("summary", ""))
    route = str(status.get("OPENAI-TEN-PROOFS-001-ROUTE-STATE", {}).get("summary", ""))
    blocked = str(status.get("OPENAI-TEN-PROOFS-001-BLOCKED-FAMILIES", {}).get("summary", ""))
    aggregate = str(status.get("OPENAI-TEN-PROOFS-001-AGGREGATE-INTEGRATION", {}).get("summary", ""))
    for family in EXPECTED_FAMILIES:
        if family not in semantic or family not in revision:
            errors.append(f"{family}: tranche membership missing")
    if "exactly three result families" not in semantic:
        errors.append("semantic tranche count drift")
    if "remaining nine result families" not in revision:
        errors.append("revision tranche count drift")
    if AUDIT_MERGE not in revision or AUDIT_BLOB not in revision:
        errors.append("revision activation authority drift")
    if CERT_REPLAY_MERGE not in replay:
        errors.append("MATHCERT replay merge missing")
    for phrase in (
        "Zero Solve routes",
        "zero Cert routes",
        "zero adjudications",
        "zero Cert outputs",
        "zero mathematical targets",
        "no aggregate ten-proofs route",
    ):
        if phrase not in route:
            errors.append(f"route zero-state missing: {phrase}")
    if "OTP-C-PERMANENT remains blocked" not in blocked:
        errors.append("Permanent blocker removed")
    if "OTP-H-GAPCVP remains blocked" not in blocked:
        errors.append("GapCVP blocker removed")
    if "Nine result families remain outside" not in blocked:
        errors.append("nine-family blocker removed")
    if "All.lean aggregate import remains failed" not in aggregate:
        errors.append("All.lean failure removed")

    failed_routes = by_id(manifest, "failed_routes", "record_id")
    if not REQUIRED_FAILED_ROUTES.issubset(failed_routes):
        errors.append("required failed-route dispositions missing")
    debt = by_id(manifest, "provider_debt", "record_id")
    if not REQUIRED_DEBT.issubset(debt):
        errors.append("required provider debt missing")

    provenance = manifest.get("provenance", {})
    if provenance.get("created_by") != "OTP-SOURCE-REVISION-MANIFEST-001":
        errors.append("manifest provenance drift")
    if AUDIT_MERGE not in set(provenance.get("source_commits", [])):
        errors.append("audit merge absent from provenance")

    boundary = str(manifest.get("non_certification_statement", ""))
    for phrase in (
        "does not establish whole-document byte or semantic equivalence",
        "register a Solve or Cert route",
        "authorize MATHCERT adjudication",
        "issue a Cert output",
        "mark a mathematical target proved",
        "certify an aggregate ten-proofs object",
    ):
        if phrase not in boundary:
            errors.append(f"claim boundary missing: {phrase}")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"provider-manifest validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("validated distinct manuscript revisions, exact three-family locus clearance, preserved blockers, and zero route authority")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
