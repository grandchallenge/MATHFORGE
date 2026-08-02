#!/usr/bin/env python3
"""Validate the bounded OpenAI ten-proofs manuscript revision audit."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
AUDIT_PATH = ROOT / "sources/OPENAI-TEN-PROOFS-001/source_revision_audits/OTP-TRANCHE-001.json"
SCHEMA_PATH = ROOT / "schemas/openai_ten_proofs_source_revision_audit.schema.json"
MANIFEST_PATH = ROOT / "provider_manifests/OPENAI-TEN-PROOFS-001.json"

ADMITTED_SHA = "f318c6508c9d49ef876a5a26cd73928705f96c07bb43e92a0cb35bd3f666ea53"
OBSERVED_SHA = "64b900d5fae6fe22f2ae1b8e3b712d20055194a6c81cf343a2455e5898ac7dd6"
EXPECTED_AUTHORITY = {
    "tracker_issue": "https://github.com/grandchallenge/MATHFORGE/issues/52",
    "admitted_semantic_merge": "cb0a203c36a9ef33270d62ab369df7bc27d3b242",
    "official_lean_root": "e62211d28e3a9131950c89caa6542cfe5eff3bca",
    "official_lean_tree": "2f8e7ac5ae7f157b6b1de636c2c343b1c7a7e365",
}
EXPECTED_FAMILIES = {
    "OTP-F-EHRHART": {
        "path": "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-F-EHRHART.json",
        "blob": "a3dc4de4c38a80b7aec1fae6506b08e14d2e58bb",
        "chapter": 8,
        "theorem": "Theorem 1.1",
        "pdf_page_index": 219,
        "printed_page": 218,
        "finding_keys": {
            "theorem_statement_relation",
            "sharpness_witness_relation",
            "scope_exclusion_preserved",
            "proof_body_compared_in_full",
        },
    },
    "OTP-J1-COMPACTNESS": {
        "path": "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J1-COMPACTNESS.json",
        "blob": "659396358d0d999c00011645f72602f30ccf6b0e",
        "chapter": 10,
        "theorem": "Theorem 1.1",
        "pdf_page_index": 236,
        "printed_page": 235,
        "finding_keys": {
            "theorem_statement_relation",
            "corrected_conjecture_context_relation",
            "connected_bipartite_cyclic_family_scope_preserved",
            "proof_body_compared_in_full",
        },
    },
    "OTP-J2-TWO-DEGENERATE": {
        "path": "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J2-TWO-DEGENERATE.json",
        "blob": "7bd168c46921f64364b20021b6315d68f0fde7d0",
        "chapter": 10,
        "theorem": "Theorem 1.2",
        "pdf_page_index": 236,
        "printed_page": 235,
        "finding_keys": {
            "theorem_statement_relation",
            "degeneracy_definition_context_relation",
            "fixed_connected_bipartite_two_degenerate_scope_preserved",
            "proof_body_compared_in_full",
        },
    },
}
EXPECTED_DISPOSITION = {
    "whole_document_byte_equivalence": "not_established",
    "whole_document_semantic_equivalence": "not_established",
    "family_locus_candidate_clear_count": 3,
    "family_locus_clear_count_before_activation": 0,
    "family_locus_clear_count_after_activation": 3,
    "unexamined_result_family_count": 9,
    "provider_manifest_updated": False,
}
EXPECTED_ROUTE_CONTROLS = {
    "may_route_before_activation": False,
    "route_registered_by_this_record": False,
    "aggregate_route_permitted": False,
    "mathcert_adjudication_authorized": False,
    "cert_output_authorized": False,
    "mathematical_claim_promoted": False,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(
        f"blob {len(data)}\0".encode("ascii") + data,
        usedforsecurity=False,
    ).hexdigest()


def validation_errors(
    audit: dict[str, Any] | None = None,
    semantic_records: dict[str, dict[str, Any]] | None = None,
    semantic_blobs: dict[str, str] | None = None,
    provider_manifest_text: str | None = None,
) -> list[str]:
    errors: list[str] = []
    audit = load_json(AUDIT_PATH) if audit is None else audit
    schema = load_json(SCHEMA_PATH)
    for error in sorted(Draft202012Validator(schema).iter_errors(audit), key=lambda e: list(e.path)):
        errors.append(f"audit schema: {error.json_path}: {error.message}")

    if audit.get("authority") != EXPECTED_AUTHORITY:
        errors.append("audit authority drift")
    admitted = audit.get("admitted_manuscript", {})
    observed = audit.get("observed_manuscript", {})
    if admitted.get("sha256") != ADMITTED_SHA or admitted.get("bytes") != 2266052:
        errors.append("admitted manuscript identity drift")
    if admitted.get("retained_bytes_available") is not False:
        errors.append("unretained admitted bytes represented as available")
    if observed.get("sha256") != OBSERVED_SHA or observed.get("bytes") != 2266371:
        errors.append("observed manuscript identity drift")
    if admitted.get("sha256") == observed.get("sha256"):
        errors.append("distinct manuscript revisions collapsed")

    method = audit.get("comparison_method", {})
    if method.get("exact_whole_document_byte_diff_performed") is not False:
        errors.append("whole-document byte diff falsely asserted")
    if "only for the three recorded theorem loci" not in str(method.get("permitted_inference", "")):
        errors.append("comparison inference boundary drift")

    if semantic_records is None:
        semantic_records = {
            family: load_json(ROOT / expected["path"])
            for family, expected in EXPECTED_FAMILIES.items()
        }
    if semantic_blobs is None:
        semantic_blobs = {
            family: git_blob_sha1(ROOT / expected["path"])
            for family, expected in EXPECTED_FAMILIES.items()
        }

    families = audit.get("families", [])
    family_map = {
        item.get("result_family"): item
        for item in families
        if isinstance(item, dict)
    }
    if len(families) != 3 or set(family_map) != set(EXPECTED_FAMILIES):
        errors.append("family audit membership drift")

    for family, expected in EXPECTED_FAMILIES.items():
        item = family_map.get(family)
        semantic = semantic_records.get(family)
        if not isinstance(item, dict) or not isinstance(semantic, dict):
            continue
        record_ref = item.get("semantic_record", {})
        if record_ref != {"path": expected["path"], "git_blob_sha1": expected["blob"]}:
            errors.append(f"{family}: semantic record reference drift")
        if semantic_blobs.get(family) != expected["blob"]:
            errors.append(f"{family}: semantic record blob drift")
        source = semantic.get("source", {})
        expected_locus = {
            "chapter": expected["chapter"],
            "theorem": expected["theorem"],
            "pdf_page_index": expected["pdf_page_index"],
            "printed_page": expected["printed_page"],
        }
        if item.get("source_locus") != expected_locus:
            errors.append(f"{family}: source locus drift")
        if source.get("sha256") != ADMITTED_SHA:
            errors.append(f"{family}: admitted semantic source identity drift")
        if item.get("admitted_normalized_statement") != source.get("normalized_statement"):
            errors.append(f"{family}: normalized statement substitution")
        findings = item.get("current_revision_findings", {})
        if set(findings) != expected["finding_keys"]:
            errors.append(f"{family}: current-revision finding shape drift")
        if findings.get("theorem_statement_relation") != "equivalent_to_admitted_normalized_statement":
            errors.append(f"{family}: theorem relation drift")
        if findings.get("proof_body_compared_in_full") is not False:
            errors.append(f"{family}: full proof-body comparison falsely asserted")
        if item.get("current_revision_locus_concordance") != "candidate_clear_pending_protected_review":
            errors.append(f"{family}: activation state inflated")

    if audit.get("disposition") != EXPECTED_DISPOSITION:
        errors.append("audit disposition drift or inflation")
    activation = audit.get("activation", {})
    if activation.get("condition") != "exact-head Forge CI, non-author specialist APPROVED review, and protected merge":
        errors.append("activation gate drift")
    if activation.get("head_change_requires_reapproval") is not True:
        errors.append("head-change reapproval disabled")
    if audit.get("route_controls") != EXPECTED_ROUTE_CONTROLS:
        errors.append("route or claim controls inflated")

    if provider_manifest_text is None:
        provider_manifest_text = MANIFEST_PATH.read_text(encoding="utf-8")
    if ADMITTED_SHA not in provider_manifest_text:
        errors.append("provider manifest lost admitted manuscript identity")
    if OBSERVED_SHA in provider_manifest_text:
        errors.append("provider manifest silently repinned before audit activation")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"source revision audit validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(
        "validated bounded current-revision concordance candidates for Ehrhart, Compactness, and Two-degenerate; whole-document equivalence and all route authority remain blocked"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
