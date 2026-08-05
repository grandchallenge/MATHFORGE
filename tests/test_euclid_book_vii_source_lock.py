#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ci" / "validate_euclid_book_vii_source_lock.py"
spec = importlib.util.spec_from_file_location("validate_euclid_book_vii_source_lock", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

PACKAGE = json.loads((ROOT / "sources" / "EUCLID-ELEMENTS-BOOK-VII-MICRO-001" / "source_lock_and_concordance.json").read_text(encoding="utf-8"))
SCHEMA = json.loads((ROOT / "schemas" / "euclid_book_vii_source_lock.schema.json").read_text(encoding="utf-8"))
SOURCE_BYTES = (ROOT / "sources" / "EUCLID-ELEMENTS-BOOK-VII-MICRO-001" / "heath_1908_book_vii_selected_statements.txt").read_bytes()


class EuclidBookVIISourceLockTests(unittest.TestCase):
    def errors(self, candidate, source_bytes=SOURCE_BYTES):
        return module.validate_package(candidate, SCHEMA, source_bytes)

    def assert_rejected(self, candidate, source_bytes=SOURCE_BYTES):
        self.assertTrue(self.errors(candidate, source_bytes))

    def test_baseline_accepts(self):
        self.assertEqual(self.errors(PACKAGE), [])

    def test_rejects_source_byte_substitution(self):
        self.assert_rejected(copy.deepcopy(PACKAGE), SOURCE_BYTES.replace(b"An unit", b"A unit", 1))

    def test_rejects_recorded_source_hash_substitution(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["source_artifact"]["sha256"] = "0" * 64
        self.assert_rejected(candidate)

    def test_rejects_translator_drift(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["edition"]["translator_editor"] = "Unknown translator"
        self.assert_rejected(candidate)

    def test_rejects_publication_year_drift(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["edition"]["publication_year"] = 1956
        self.assert_rejected(candidate)

    def test_rejects_source_url_substitution(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["provenance"]["original_file_url"] = "https://example.invalid/euclid.pdf"
        self.assert_rejected(candidate)

    def test_rejects_invented_whole_scan_hash(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["provenance"]["whole_scan_sha256_recorded"] = True
        self.assert_rejected(candidate)

    def test_rejects_missing_public_domain_basis(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["provenance"]["public_domain"]["basis"] = "unknown"
        self.assert_rejected(candidate)

    def test_rejects_locus_deletion(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["admitted_loci"].pop()
        self.assert_rejected(candidate)

    def test_rejects_locus_insertion(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["admitted_loci"].append("VII.3")
        self.assert_rejected(candidate)

    def test_rejects_number_domain_widening_to_zero(self):
        candidate = copy.deepcopy(PACKAGE)
        entry = next(item for item in candidate["concordance"] if item["locus"] == "VII.def.2")
        entry["modern_normalization"] = "Represent Euclidean numbers by all natural numbers including zero."
        self.assert_rejected(candidate)

    def test_rejects_signed_divisibility_inflation(self):
        candidate = copy.deepcopy(PACKAGE)
        entry = next(item for item in candidate["concordance"] if item["locus"] == "VII.def.3")
        entry["modern_normalization"] = "Interpret measuring as signed divisibility over all integers."
        self.assert_rejected(candidate)

    def test_rejects_vii1_equivalence_inflation(self):
        candidate = copy.deepcopy(PACKAGE)
        entry = next(item for item in candidate["concordance"] if item["locus"] == "VII.1")
        entry["relationship"] = "bounded_domain_translation"
        self.assert_rejected(candidate)

    def test_rejects_extended_euclid_as_present_in_source(self):
        candidate = copy.deepcopy(PACKAGE)
        entry = next(item for item in candidate["modern_extensions"] if item["extension_id"] == "MODERN-EXTENDED-EUCLID")
        entry["source_support"] = "not_verbatim_in_admitted_loci"
        self.assert_rejected(candidate)

    def test_rejects_historical_modern_equivalence(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["authority_boundaries"]["historical_modern_equivalence"] = True
        self.assert_rejected(candidate)

    def test_rejects_bezout_verbatim_attribution(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["authority_boundaries"]["bezout_identity_verbatim_euclid"] = True
        self.assert_rejected(candidate)

    def test_rejects_diophantine_verbatim_attribution(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["authority_boundaries"]["linear_diophantine_theorem_verbatim_euclid"] = True
        self.assert_rejected(candidate)

    def test_rejects_reader_activation(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["authority_boundaries"]["documentary_reader_authorized"] = True
        self.assert_rejected(candidate)

    def test_rejects_plate_authority_inflation(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["authority_boundaries"]["plates_authority"] = "historical_source_authority"
        self.assert_rejected(candidate)

    def test_rejects_novelty_inflation(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["authority_boundaries"]["claims_novelty"] = True
        self.assert_rejected(candidate)

    def test_rejects_priority_inflation(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["authority_boundaries"]["claims_priority"] = True
        self.assert_rejected(candidate)

    def test_rejects_first_formalization_inflation(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["authority_boundaries"]["claims_first_formalization"] = True
        self.assert_rejected(candidate)


if __name__ == "__main__":
    unittest.main()
