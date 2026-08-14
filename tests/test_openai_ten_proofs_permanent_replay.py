from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_permanent_replay",
    ROOT / "ci/validate_openai_ten_proofs_permanent_replay.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OpenAITenProofsPermanentReplayTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(MODULE.RECORD_PATH.read_text(encoding="utf-8"))
        self.repair = json.loads(MODULE.REPAIR_PATH.read_text(encoding="utf-8"))

    def errors(self, *, record=None, repair=None):
        return MODULE.validation_errors(
            record=copy.deepcopy(self.record if record is None else record),
            repair=copy.deepcopy(self.repair if repair is None else repair),
        )

    def test_current_characterized_blocker_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_silent_repin_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["commit"] = "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6"
        self.assertTrue(self.errors(record=record))

    def test_tree_substitution_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["tree"] = "0" * 40
        self.assertTrue(self.errors(record=record))

    def test_archive_substitution_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["deterministic_archive_sha256"] = "0" * 64
        self.assertTrue(self.errors(record=record))

    def test_archival_reassertion_cannot_be_disabled(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["archival_reassertion_policy"]["permitted"] = False
        self.assertTrue(self.errors(record=record))

    def test_new_carrier_identity_is_explicitly_permitted(self) -> None:
        policy = self.record["protected_source"]["archival_reassertion_policy"]
        self.assertIs(policy["new_carrier_commit_identity_permitted"], True)
        self.assertEqual(self.errors(), [])

    def test_historical_provenance_cannot_be_dropped(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["archival_reassertion_policy"]["historical_provenance_must_be_preserved"] = False
        self.assertTrue(self.errors(record=record))

    def test_reasserted_tree_match_cannot_be_relaxed(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["archival_reassertion_policy"]["protected_tree_must_match"] = False
        self.assertTrue(self.errors(record=record))

    def test_reasserted_archive_match_cannot_be_relaxed(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["archival_reassertion_policy"]["deterministic_archive_sha256_must_match"] = False
        self.assertTrue(self.errors(record=record))

    def test_later_upstream_revision_cannot_be_substituted_as_carrier(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["archival_reassertion_policy"]["later_upstream_revision_substitution_permitted"] = True
        self.assertTrue(self.errors(record=record))

    def test_fetch_failure_cannot_be_promoted_to_success(self) -> None:
        record = copy.deepcopy(self.record)
        record["attempt"]["fetch_result"] = "success"
        self.assertTrue(self.errors(record=record))

    def test_checkout_cannot_be_falsely_completed(self) -> None:
        record = copy.deepcopy(self.record)
        record["attempt"]["source_checkout_completed"] = True
        self.assertTrue(self.errors(record=record))

    def test_solution_build_cannot_be_falsely_reached(self) -> None:
        record = copy.deepcopy(self.record)
        record["attempt"]["solution_build_reached"] = True
        self.assertTrue(self.errors(record=record))

    def test_challenge_elaboration_cannot_be_falsely_reached(self) -> None:
        record = copy.deepcopy(self.record)
        record["attempt"]["challenge_elaboration_reached"] = True
        self.assertTrue(self.errors(record=record))

    def test_unretained_archive_cannot_be_claimed_recovered(self) -> None:
        record = copy.deepcopy(self.record)
        record["reacquisition_audit"]["retained_deterministic_archive_bytes_found"] = True
        self.assertTrue(self.errors(record=record))

    def test_later_upstream_substitution_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["reacquisition_audit"]["later_upstream_head_substituted"] = True
        self.assertTrue(self.errors(record=record))

    def test_replay_clearance_inflation_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["disposition"]["fresh_family_replay_clear"] = True
        self.assertTrue(self.errors(record=record))

    def test_source_reassertion_lane_cannot_be_silently_closed(self) -> None:
        record = copy.deepcopy(self.record)
        record["disposition"]["source_reassertion_operation_may_begin"] = False
        self.assertTrue(self.errors(record=record))

    def test_semantic_audit_premature_opening_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["disposition"]["semantic_audit_may_begin"] = True
        self.assertTrue(self.errors(record=record))

    def test_source_reassertion_authority_cannot_be_removed(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["source_reassertion_authorized"] = False
        self.assertTrue(self.errors(record=record))

    def test_semantic_authority_insertion_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["semantic_nonvacuity_audit_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_solve_route_insertion_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["solve_handoff_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_cert_route_insertion_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["cert_route_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_proof_promotion_is_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["mathematical_target_proved"] = True
        self.assertTrue(self.errors(record=record))

    def test_repair_boundary_drift_is_rejected(self) -> None:
        repair = copy.deepcopy(self.repair)
        repair["proposed_family_boundary"] = "PERMANENT_FORMULA_AND_CIRCUIT_LOWER_BOUNDS"
        self.assertTrue(self.errors(repair=repair))

    def test_repair_circuit_coverage_inflation_is_rejected(self) -> None:
        repair = copy.deepcopy(self.repair)
        repair["coverage_disposition"]["circuit_lower_bound_coverage"] = True
        self.assertTrue(self.errors(repair=repair))


if __name__ == "__main__":
    unittest.main()
