#!/usr/bin/env python3
"""Fail-closed validator for the Book VII exact-byte source lock and concordance."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_PATH = ROOT / "sources" / "EUCLID-ELEMENTS-BOOK-VII-MICRO-001" / "source_lock_and_concordance.json"
SOURCE_PATH = ROOT / "sources" / "EUCLID-ELEMENTS-BOOK-VII-MICRO-001" / "heath_1908_book_vii_selected_statements.txt"
SCHEMA_PATH = ROOT / "schemas" / "euclid_book_vii_source_lock.schema.json"

EXPECTED_LOCI = ["VII.def.1", "VII.def.2", "VII.def.3", "VII.def.5", "VII.def.12", "VII.def.14", "VII.1", "VII.2"]
EXPECTED_STATEMENTS = {
    "VII.def.1": "An unit is that by virtue of which each of the things that exist is called one.",
    "VII.def.2": "A number is a multitude composed of units.",
    "VII.def.3": "A number is a part of a number, the less of the greater, when it measures the greater;",
    "VII.def.5": "The greater number is a multiple of the less when it is measured by the less.",
    "VII.def.12": "Numbers prime to one another are those which are measured by an unit alone as a common measure.",
    "VII.def.14": "Numbers composite to one another are those which are measured by some number as a common measure.",
    "VII.1": "Two unequal numbers being set out, and the less being continually subtracted in turn from the greater, if the number which is left never measures the one before it until an unit is left, the original numbers will be prime to one another.",
    "VII.2": "Given two numbers not prime to one another, to find their greatest common measure.",
}
EXPECTED_PORISM = "From this it is manifest that, if a number measure two numbers, it will also measure their greatest common measure."
EXPECTED_SOURCE_SHA256 = "66d3d62cb75cccc0d705fa06c8845f3d9c2c61952f9994862d54c7679517e6d0"
EXPECTED_SOURCE_BYTES = 1492
EXPECTED_EXTENSIONS = {
    "MODERN-REMAINDER-EUCLID": ("later_algorithmic_normalization", "not_verbatim_in_admitted_loci"),
    "MODERN-EXTENDED-EUCLID": ("later_derived_extension", "not_present_in_admitted_loci"),
    "MODERN-BEZOUT": ("later_derived_extension", "not_present_in_admitted_loci"),
    "MODERN-LINEAR-DIOPHANTINE": ("later_derived_extension", "not_present_in_admitted_loci"),
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current: str | None = None
    lines: list[str] = []
    for line in text.splitlines():
        match = re.fullmatch(r"\[([A-Za-z0-9.]+)\]", line)
        if match:
            if current is not None:
                sections[current] = "\n".join(lines).strip()
            current = match.group(1)
            lines = []
        elif current is not None:
            lines.append(line)
    if current is not None:
        sections[current] = "\n".join(lines).strip()
    return sections


def semantic_errors(package: Any, source_bytes: bytes) -> list[str]:
    errors: list[str] = []
    if not isinstance(package, dict):
        return ["package must be an object"]

    source = package.get("source_artifact", {})
    digest = hashlib.sha256(source_bytes).hexdigest()
    if len(source_bytes) != EXPECTED_SOURCE_BYTES or source.get("byte_length") != EXPECTED_SOURCE_BYTES:
        errors.append("source transcription byte length drifted")
    if digest != EXPECTED_SOURCE_SHA256 or source.get("sha256") != EXPECTED_SOURCE_SHA256:
        errors.append("source transcription SHA-256 drifted")
    if b"\r" in source_bytes:
        errors.append("source transcription must use LF line endings only")
    if not source_bytes.endswith(b"\n"):
        errors.append("source transcription must have one final newline")
    try:
        source_text = source_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return errors + ["source transcription is not valid UTF-8"]

    sections = parse_sections(source_text)
    expected_sections = dict(EXPECTED_STATEMENTS)
    expected_sections["VII.2.porism"] = EXPECTED_PORISM
    if sections != expected_sections:
        errors.append("source transcription sections or exact text drifted")

    if package.get("admitted_loci") != EXPECTED_LOCI:
        errors.append("admitted locus order or membership drifted")
    statements = package.get("statements", [])
    actual = {item.get("locus"): item for item in statements if isinstance(item, dict)}
    if list(actual) != EXPECTED_LOCI or len(actual) != len(EXPECTED_LOCI):
        errors.append("statement locus order, uniqueness, or membership drifted")
    for locus, expected in EXPECTED_STATEMENTS.items():
        item = actual.get(locus, {})
        if item.get("exact_text") != expected:
            errors.append(f"{locus} exact historical statement drifted")
        if locus == "VII.2":
            if item.get("attached_porism") != EXPECTED_PORISM:
                errors.append("VII.2 porism drifted")
        elif "attached_porism" in item:
            errors.append(f"{locus} must not acquire an attached porism")

    provenance = package.get("provenance", {})
    if provenance.get("whole_scan_sha256_recorded") is not False:
        errors.append("whole-scan SHA-256 must remain unrecorded unless independently acquired")
    if provenance.get("whole_scan_role") != "provenance_only_not_governed_byte_surface":
        errors.append("whole scan must remain provenance-only")
    public_domain = provenance.get("public_domain", {})
    if public_domain.get("status") != "public_domain" or "Mechanical scan" not in str(public_domain.get("basis", "")):
        errors.append("public-domain mechanical-scan basis drifted")
    if public_domain.get("commons_statement_required") is not True:
        errors.append("Commons public-domain statement must remain required")

    concordance = package.get("concordance", [])
    actual_concordance = {item.get("locus"): item for item in concordance if isinstance(item, dict)}
    if list(actual_concordance) != EXPECTED_LOCI or len(actual_concordance) != len(EXPECTED_LOCI):
        errors.append("concordance locus order, uniqueness, or membership drifted")
    def2 = actual_concordance.get("VII.def.2", {})
    if "greater than one" not in str(def2.get("modern_normalization", "")):
        errors.append("VII.def.2 must preserve the historical unit/number distinction")
    if not {"zero", "negative integers", "signed coefficients"}.issubset(set(def2.get("unsupported_extensions", []))):
        errors.append("VII.def.2 must exclude zero and signed-domain widening")
    def3 = actual_concordance.get("VII.def.3", {})
    if "m < n" not in str(def3.get("modern_normalization", "")) or "positive natural k" not in str(def3.get("modern_normalization", "")):
        errors.append("VII.def.3 must retain positive oriented measuring semantics")
    def12 = actual_concordance.get("VII.def.12", {})
    if "gcd(a,b) = 1" not in str(def12.get("modern_normalization", "")):
        errors.append("VII.def.12 bounded gcd normalization drifted")
    prop1 = actual_concordance.get("VII.1", {})
    if prop1.get("relationship") != "constructive_coprimality_analogue":
        errors.append("VII.1 must remain a constructive analogue, not verbatim modern equivalence")
    prop2 = actual_concordance.get("VII.2", {})
    if prop2.get("relationship") != "constructive_greatest_common_measure_analogue":
        errors.append("VII.2 must remain a constructive analogue")
    if "porism" not in str(prop2.get("historical_object_domain", "")).lower():
        errors.append("VII.2 concordance must retain the porism")

    extensions = package.get("modern_extensions", [])
    actual_extensions = {item.get("extension_id"): (item.get("classification"), item.get("source_support")) for item in extensions if isinstance(item, dict)}
    if actual_extensions != EXPECTED_EXTENSIONS:
        errors.append("modern extension classification or source support drifted")

    historical_text = "\n".join(EXPECTED_STATEMENTS.values()) + "\n" + EXPECTED_PORISM
    for forbidden in ("Bézout", "Diophantine", "signed integer", "remainder algorithm"):
        if forbidden.lower() in historical_text.lower():
            errors.append(f"historical statement surface must not contain modern extension term {forbidden}")

    boundary = package.get("authority_boundaries", {})
    if boundary.get("candidate_exact_byte_lock_prepared") is not True:
        errors.append("candidate exact-byte lock must remain prepared")
    for key in ("protected_source_lock_effective", "historical_modern_equivalence", "modern_extended_euclid_verbatim_euclid", "bezout_identity_verbatim_euclid", "linear_diophantine_theorem_verbatim_euclid", "documentary_reader_authorized", "edition_record_authorized", "documentary_manifest_admission_authorized", "programme_stage3_activated", "claims_novelty", "claims_priority", "claims_first_formalization", "certifies_modern_mathematics"):
        if boundary.get(key) is not False:
            errors.append(f"authority boundary {key} must be false")
    if boundary.get("plates_authority") != "pedagogical_orientation_only":
        errors.append("plate authority must remain pedagogical_orientation_only")

    next_gate = package.get("next_gate", {})
    if next_gate.get("programme_reader_may_begin_after_this_candidate") is not False:
        errors.append("candidate Forge package must not activate the Programme reader")
    return errors


def validate_package(package: Any, schema: Any, source_bytes: bytes) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [f"{error.json_path}: {error.message}" for error in sorted(validator.iter_errors(package), key=lambda item: list(item.path))]
    errors.extend(semantic_errors(package, source_bytes))
    return errors


def main() -> int:
    errors = validate_package(load_json(PACKAGE_PATH), load_json(SCHEMA_PATH), SOURCE_PATH.read_bytes())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"EUCLID Book VII source-lock validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("EUCLID Book VII exact transcription bytes, Heath 1908 provenance, eight-locus concordance, modern-extension exclusions, and documentary authority boundaries are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
