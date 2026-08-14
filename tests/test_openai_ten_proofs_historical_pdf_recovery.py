from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_historical_pdf_recovery",
    ROOT / "ci" / "validate_openai_ten_proofs_historical_pdf_recovery.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class HistoricalPdfRecoveryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = MODULE.load(MODULE.RECORD)

    def errors(self, record=None):
        return MODULE.validation_errors(copy.deepcopy(self.record if record is None else record))

    def test_current_record_passes(self):
        self.assertEqual(self.errors(), [])

    def test_digest_drift_rejected(self):
        r = copy.deepcopy(self.record)
        r["historical_identity"]["sha256"] = "0" * 64
        self.assertTrue(self.errors(r))

    def test_byte_length_drift_rejected(self):
        r = copy.deepcopy(self.record)
        r["historical_identity"]["byte_length"] = 2266371
        self.assertTrue(self.errors(r))

    def test_false_recovery_promotion_rejected(self):
        r = copy.deepcopy(self.record)
        r["exit_state"] = "HISTORICAL_ADMITTED_PDF_BYTES_RECOVERED__EXACT_SHA256_MATCH"
        self.assertTrue(self.errors(r))

    def test_current_pdf_substitution_rejected(self):
        r = copy.deepcopy(self.record)
        r["known_source_drift"]["may_substitute_for_historical_payload"] = True
        self.assertTrue(self.errors(r))

    def test_semantic_match_cannot_replace_bytes(self):
        r = copy.deepcopy(self.record)
        r["acceptance_gate"]["semantic_or_theorem_locus_match_sufficient"] = True
        self.assertTrue(self.errors(r))

    def test_filename_match_cannot_replace_bytes(self):
        r = copy.deepcopy(self.record)
        r["acceptance_gate"]["filename_or_current_official_status_sufficient"] = True
        self.assertTrue(self.errors(r))

    def test_blocker_cannot_invalidate_semantic_clearance(self):
        r = copy.deepcopy(self.record)
        r["downstream_independence"]["invalidates_permanent_semantic_nonvacuity_clearance"] = True
        self.assertTrue(self.errors(r))

    def test_blocker_cannot_stop_existing_routing(self):
        r = copy.deepcopy(self.record)
        r["downstream_independence"]["blocks_routing_of_already_cleared_variable_leaf_targets"] = True
        self.assertTrue(self.errors(r))

    def test_whole_document_equivalence_inflation_rejected(self):
        r = copy.deepcopy(self.record)
        r["downstream_independence"]["creates_whole_document_semantic_equivalence"] = True
        self.assertTrue(self.errors(r))

    def test_search_surface_deletion_rejected(self):
        r = copy.deepcopy(self.record)
        r["search_surface"] = r["search_surface"][:2]
        self.assertTrue(self.errors(r))


if __name__ == "__main__":
    unittest.main()
