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

    def test_current_fresh_replay_record_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_historical_root_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["historical_commit"] = "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6"
        self.assertTrue(self.errors(record=record))

    def test_tree_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["tree"] = "0" * 40
        self.assertTrue(self.errors(record=record))

    def test_archive_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["deterministic_archive_sha256"] = "0" * 64
        self.assertTrue(self.errors(record=record))

    def test_later_upstream_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_source"]["later_upstream_revision_substituted"] = True
        self.assertTrue(self.errors(record=record))

    def test_non_gcl_carrier_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["source_carrier"]["repository"] = "utensil/ten-proofs"
        self.assertTrue(self.errors(record=record))

    def test_mutable_carrier_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["source_carrier"]["immutable"] = False
        self.assertTrue(self.errors(record=record))

    def test_carrier_digest_drift_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["source_carrier"]["asset_digest"] = "sha256:" + "0" * 64
        self.assertTrue(self.errors(record=record))

    def test_archive_verification_loss_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["successful_replay"]["archive_download_verified"] = False
        self.assertTrue(self.errors(record=record))

    def test_file_identity_verification_loss_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["successful_replay"]["permanent_family_file_identities_verified"] = False
        self.assertTrue(self.errors(record=record))

    def test_build_failure_cannot_be_represented_as_clear(self) -> None:
        record = copy.deepcopy(self.record)
        record["successful_replay"]["permanent_solution_module_built"] = False
        self.assertTrue(self.errors(record=record))

    def test_elaboration_failure_cannot_be_represented_as_clear(self) -> None:
        record = copy.deepcopy(self.record)
        record["successful_replay"]["permanent_challenge_elaborated"] = False
        self.assertTrue(self.errors(record=record))

    def test_current_head_target_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["successful_replay"]["target_inventory"]["targets"][0] = "PermanentFormulaLowerBound.some_other_target"
        self.assertTrue(self.errors(record=record))

    def test_circuit_target_insertion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["successful_replay"]["target_inventory"]["circuit_target_count"] = 1
        self.assertTrue(self.errors(record=record))

    def test_formula_conditionality_removal_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["successful_replay"]["target_inventory"]["formula_targets_conditional"] = False
        self.assertTrue(self.errors(record=record))

    def test_replay_clearance_removal_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["disposition"]["fresh_family_replay_clear"] = False
        self.assertTrue(self.errors(record=record))

    def test_semantic_audit_cannot_be_claimed_performed(self) -> None:
        record = copy.deepcopy(self.record)
        record["disposition"]["semantic_nonvacuity_audit_performed"] = True
        self.assertTrue(self.errors(record=record))

    def test_semantic_authority_insertion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["semantic_nonvacuity_audit_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_solve_route_insertion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["solve_handoff_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_cert_route_insertion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["cert_route_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_proof_promotion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["mathematical_target_proved"] = True
        self.assertTrue(self.errors(record=record))

    def test_repair_boundary_inflation_rejected(self) -> None:
        repair = copy.deepcopy(self.repair)
        repair["proposed_family_boundary"] = "PERMANENT_FORMULA_AND_CIRCUIT_LOWER_BOUNDS"
        self.assertTrue(self.errors(repair=repair))

    def test_repair_circuit_coverage_inflation_rejected(self) -> None:
        repair = copy.deepcopy(self.repair)
        repair["coverage_disposition"]["circuit_lower_bound_coverage"] = True
        self.assertTrue(self.errors(repair=repair))


if __name__ == "__main__":
    unittest.main()
