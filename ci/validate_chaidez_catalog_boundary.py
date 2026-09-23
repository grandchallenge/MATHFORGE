#!/usr/bin/env python3
import json, sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "governance" / "chaidez_catalog_boundary.json"
SCHEMA = ROOT / "schemas" / "chaidez_catalog_boundary.schema.json"
EXPECTED_COMMIT = "861479cb599df01f6e9cafc8647fdefe56249d29"
EXPECTED_BLOB = "29e12c793d116c6c3af121c04486c5daa6c09e1e"

def errors(document=None):
    data = document or json.loads(POLICY.read_text())
    result = [e.message for e in Draft202012Validator(json.loads(SCHEMA.read_text())).iter_errors(data)]
    authority = data.get("programme_authority", {})
    if (authority.get("commit"), authority.get("git_blob_sha1")) != (EXPECTED_COMMIT, EXPECTED_BLOB):
        result.append("Programme Chaidez authority identity drift")
    if data.get("chaidez_dossier_at_ingestion") is not False or data.get("automatic_promotion") is not False:
        result.append("catalog authority inflation")
    return result

if __name__ == "__main__":
    failures = errors()
    if failures: print("\n".join(failures), file=sys.stderr)
    else: print("validated MATHFORGE source-record and reviewed-promotion boundary")
    raise SystemExit(bool(failures))
