#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "governance/downstream_observations/OPENAI-TEN-PROOFS-001.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_downstream_observation.schema.json"
FILES = {
    "provider_manifest": (
        ROOT / "provider_manifests/OPENAI-TEN-PROOFS-001.json",
        "fe1dab478e4ef9d6ddfe1b94a289fe7b51f58472",
    ),
    "ehrhart_semantic": (
        ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-F-EHRHART.json",
        "a3dc4de4c38a80b7aec1fae6506b08e14d2e58bb",
    ),
    "compactness_semantic": (
        ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J1-COMPACTNESS.json",
        "659396358d0d999c00011645f72602f30ccf6b0e",
    ),
    "two_degenerate_semantic": (
        ROOT / "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J2-TWO-DEGENERATE.json",
        "7bd168c46921f64364b20021b6315d68f0fde7d0",
    ),
    "revision_audit": (
        ROOT / "sources/OPENAI-TEN-PROOFS-001/source_revision_audits/OTP-TRANCHE-001.json",
        "80d473b1b545fd9ca05fc5200bcf70ff5f9fcb05",
    ),
}
EXPECTED_FAMILIES = [
    {
        "result_family": "OTP-F-EHRHART",
        "route_state": "qualified",
        "adjudication_count": 1,
        "restricted_cert_output_count": 1,
        "disposition": "qualified_encoded_targets_only",
        "mathematical_target_proved": False,
    },
    {
        "result_family": "OTP-J1-COMPACTNESS",
        "route_state": "submitted",
        "adjudication_count": 0,
        "restricted_cert_output_count": 0,
        "disposition": None,
        "mathematical_target_proved": False,
    },
    {
        "result_family": "OTP-J2-TWO-DEGENERATE",
        "route_state": "submitted",
        "adjudication_count": 0,
        "restricted_cert_output_count": 0,
        "disposition": None,
        "mathematical_target_proved": False,
    },
]


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload,
        usedforsecurity=False,
    ).hexdigest()


def validation_errors(
    *,
    record: dict[str, Any] | None = None,
    schema: dict[str, Any] | None = None,
    blobs: dict[str, str] | None = None,
) -> list[str]:
    record = load(RECORD) if record is None else record
    schema = load(SCHEMA) if schema is None else schema
    blobs = (
        {name: git_blob_sha1(path) for name, (path, _) in FILES.items()}
        if blobs is None
        else blobs
    )
    errors: list[str] = []

    if schema.get("additionalProperties") is not False:
        errors.append("downstream observation schema must remain closed")
    errors.extend(
        f"schema violation: {error.message}"
        for error in Draft202012Validator(schema).iter_errors(record)
    )

    for name, (_, expected) in FILES.items():
        if blobs.get(name) != expected:
            errors.append(f"protected Forge blob drift: {name}")

    authority = record.get("forge_authority", {})
    if authority.get("owns_cert_route") is not False:
        errors.append("Forge route authority inflation")
    if authority.get("owns_adjudication") is not False:
        errors.append("Forge adjudication authority inflation")
    if authority.get("owns_cert_output") is not False:
        errors.append("Forge Cert-output authority inflation")

    cert = record.get("mathcert_authority", {})
    expected_cert = {
        "repository": "grandchallenge/MATHCERT",
        "execution_merge": "1d5b1e6514787005ed75e363df7ea953dcd9391a",
        "documentary_closure_merge": "150344d25b50895203c59f4193a8e97bb1cbbf81",
        "closure_exact_reviewed_head": "207df8462f427e0c41604614ebe1a291ad89273f",
        "closure_review_id": 4840018727,
        "closure_human_steward_disposition_comment": 5160923732,
    }
    for key, value in expected_cert.items():
        if cert.get(key) != value:
            errors.append(f"MATHCERT authority drift: {key}")

    if cert.get("route_registry", {}).get("git_blob_sha1") != "0487c3ebf702229741f16a544d68af25cf994e41":
        errors.append("MATHCERT route-registry blob drift")
    if cert.get("certificate", {}).get("git_blob_sha1") != "27a855c949b67e71372c7f0d6601d80125d33968":
        errors.append("MATHCERT certificate blob drift")
    if cert.get("post_merge_attestation", {}).get("git_blob_sha1") != "d8b36ffdb3b5e732b385c9bac5576aa96dd1fcbe":
        errors.append("MATHCERT attestation blob drift")
    if cert.get("successor_closure", {}).get("git_blob_sha1") != "c50a397a84873b358a54db2e602058da103b75e8":
        errors.append("MATHCERT successor-closure blob drift")

    if record.get("observed_family_state") != EXPECTED_FAMILIES:
        errors.append("observed family state drift")
    if record.get("aggregate_output_count") != 0:
        errors.append("aggregate output inflation")
    if record.get("mathematical_targets_marked_proved") != 0:
        errors.append("proof-status promotion")

    limitations = record.get("preserved_limitations", {})
    expected_limitations = {
        "whole_document_byte_equivalence": "not_established_between_all_revisions",
        "whole_document_semantic_equivalence": "not_established",
        "proof_body_compared_in_full": False,
        "blocked_repair_lanes": ["OTP-C-PERMANENT", "OTP-H-GAPCVP"],
        "all_lean_state": "failed_namespace_collision",
        "unexamined_result_family_count": 9,
        "aggregate_ten_proofs_authority": False,
    }
    for key, value in expected_limitations.items():
        if limitations.get(key) != value:
            errors.append(f"preserved limitation drift: {key}")

    boundary = str(record.get("claim_boundary", ""))
    for token in (
        "does not create or own a Cert route",
        "mathematical target proved",
        "all equality cases",
        "whole-document equivalence",
        "Compactness or Two-degenerate",
        "aggregate authority",
        "commercial claims",
    ):
        if token not in boundary:
            errors.append(f"claim boundary missing token: {token}")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated Forge downstream observation with no Cert authority inflation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
