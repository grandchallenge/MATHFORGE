from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_permanent_source_reassertion",
    ROOT / "ci/validate_openai_ten_proofs_permanent_source_reassertion.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OpenAITenProofsPermanentSourceReassertionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(MODULE.RECORD_PATH.read_text(encoding="utf-8"))
        self.repair = json.loads(MODULE.REPAIR_PATH.read_text(encoding="utf-8"))

    def errors(self, *, record=None, repair=None):
        return MODULE.validation_errors(
            record=copy.deepcopy(self.record if record is None else record),
            repair=copy.deepcopy(self.repair if repair is None else repair),
        )

    def test_current_reassertion_candidate_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_historical_commit_drift_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["historical_provenance"]["commit"] = "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6"
        self.assertTrue(self.errors(record=record))

    def test_tree_drift_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["historical_provenance"]["tree"] = "0" * 40
        self.assertTrue(self.errors(record=record))

    def test_archive_drift_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["historical_provenance"]["deterministic_archive_sha256"] = "0" * 64
        self.assertTrue(self.errors(record=record))

    def test_mirror_name_cannot_create_authority(self) -> None:
        record = copy.deepcopy(self.record)
        record["recovery_source"]["mirror_name_creates_authority"] = True
        self.assertTrue(self.errors(record=record))

    def test_recovery_commit_substitution_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["recovery_source"]["retrieved_commit"] = "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6"
        self.assertTrue(self.errors(record=record))

    def test_false_archive_match_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["verification"]["archive_match"] = False
        self.assertTrue(self.errors(record=record))

    def test_source_asset_digest_substitution_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["gcl_archival_carrier"]["source_asset"]["digest"] = "sha256:" + "0" * 64
        self.assertTrue(self.errors(record=record))

    def test_non_gcl_carrier_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["gcl_archival_carrier"]["repository"] = "utensil/ten-proofs"
        self.assertTrue(self.errors(record=record))

    def test_mutable_carrier_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["gcl_archival_carrier"]["immutable"] = False
        self.assertTrue(self.errors(record=record))

    def test_permanent_file_blob_substitution_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["permanent_family_files"][0]["git_blob_sha1"] = "0" * 40
        self.assertTrue(self.errors(record=record))

    def test_permanent_file_sha_substitution_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["permanent_family_files"][0]["sha256"] = "0" * 64
        self.assertTrue(self.errors(record=record))

    def test_file_deletion_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["permanent_family_files"].pop()
        self.assertTrue(self.errors(record=record))

    def test_replay_may_begin_cannot_be_removed(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["fresh_family_replay_may_begin"] = False
        self.assertTrue(self.errors(record=record))

    def test_replay_clearance_cannot_be_invented(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["fresh_family_replay_clear"] = True
        self.assertTrue(self.errors(record=record))

    def test_semantic_authority_cannot_be_invented(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["semantic_nonvacuity_audit_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_solve_route_cannot_be_invented(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["solve_handoff_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_cert_route_cannot_be_invented(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["cert_route_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_proof_status_cannot_be_promoted(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["mathematical_target_proved"] = True
        self.assertTrue(self.errors(record=record))

    def test_repair_boundary_inflation_is_rejected(self) -> None:
        repair = copy.deepcopy(self.repair)
        repair["proposed_family_boundary"] = "PERMANENT_FORMULA_AND_CIRCUIT_LOWER_BOUNDS"
        self.assertTrue(self.errors(repair=repair))

    def test_circuit_coverage_inflation_is_rejected(self) -> None:
        repair = copy.deepcopy(self.repair)
        repair["coverage_disposition"]["circuit_lower_bound_coverage"] = True
        self.assertTrue(self.errors(repair=repair))


if __name__ == "__main__":
    unittest.main()
