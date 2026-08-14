from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_openai_ten_proofs_permanent_semantic_audit",
    ROOT / "ci/validate_openai_ten_proofs_permanent_semantic_audit.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class OpenAITenProofsPermanentSemanticAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.record = json.loads(MODULE.RECORD_PATH.read_text(encoding="utf-8"))
        self.repair = json.loads(MODULE.REPAIR_PATH.read_text(encoding="utf-8"))
        self.replay = json.loads(MODULE.REPLAY_PATH.read_text(encoding="utf-8"))
        self.revision = json.loads(MODULE.REVISION_AUDIT_PATH.read_text(encoding="utf-8"))
        self.witness = MODULE.WITNESS_PATH.read_text(encoding="utf-8")

    def errors(self, *, record=None, repair=None, replay=None, revision=None, witness=None):
        return MODULE.validation_errors(
            record=copy.deepcopy(self.record if record is None else record),
            repair=copy.deepcopy(self.repair if repair is None else repair),
            replay=copy.deepcopy(self.replay if replay is None else replay),
            revision_audit=copy.deepcopy(self.revision if revision is None else revision),
            witness_text=self.witness if witness is None else witness,
        )

    def test_current_candidate_record_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_family_boundary_inflation_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["family_boundary"] = "PERMANENT_FORMULA_AND_CIRCUIT_LOWER_BOUNDS"
        self.assertTrue(self.errors(record=record))

    def test_protected_root_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_lean_source"]["historical_commit"] = "0" * 40
        self.assertTrue(self.errors(record=record))

    def test_protected_archive_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_lean_source"]["deterministic_archive_sha256"] = "0" * 64
        self.assertTrue(self.errors(record=record))

    def test_challenge_blob_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_lean_source"]["challenge_git_blob_sha1"] = "0" * 40
        self.assertTrue(self.errors(record=record))

    def test_later_upstream_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["protected_lean_source"]["later_upstream_revision_substituted"] = True
        self.assertTrue(self.errors(record=record))

    def test_historical_pdf_retention_inflation_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["manuscript_source"]["historical_admitted_revision"]["retained_bytes_available"] = True
        self.assertTrue(self.errors(record=record))

    def test_historical_pdf_byte_identity_inflation_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["manuscript_source"]["permanent_theorem_locus_pin_candidate"]["byte_identity_to_historical_admitted_revision_verified"] = True
        self.assertTrue(self.errors(record=record))

    def test_whole_document_semantic_equivalence_inflation_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["manuscript_source"]["historical_whole_document_semantic_equivalence_established"] = True
        self.assertTrue(self.errors(record=record))

    def test_original_locus_url_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["manuscript_source"]["permanent_theorem_locus_pin_candidate"]["url"] = "https://example.com/other.pdf"
        self.assertTrue(self.errors(record=record))

    def test_nonvacuity_replay_failure_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["nonvacuity_witness"]["exact_replay_clear"] = False
        self.assertTrue(self.errors(record=record))

    def test_nonvacuity_run_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["nonvacuity_witness"]["lean_run"] = 1
        self.assertTrue(self.errors(record=record))

    def test_witness_sorry_rejected(self) -> None:
        self.assertTrue(self.errors(witness=self.witness + "\nexample : True := by sorry\n"))

    def test_witness_admit_rejected(self) -> None:
        self.assertTrue(self.errors(witness=self.witness + "\nexample : True := by admit\n"))

    def test_rational_division_constructor_insertion_rejected(self) -> None:
        self.assertTrue(self.errors(witness=self.witness + "\n-- | .div f g => .div f g\n"))

    def test_target_substitution_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][0]["target"] = "PermanentFormulaLowerBound.some_other_target"
        self.assertTrue(self.errors(record=record))

    def test_variable_leaf_constant_drift_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][0]["source_variable_leaf_constant"] = 129
        self.assertTrue(self.errors(record=record))

    def test_gate_constant_drift_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][1]["source_gate_constant"] = 385
        self.assertTrue(self.errors(record=record))

    def test_gate_bound_coverage_inflation_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][0]["encoded_gate_bound"] = True
        self.assertTrue(self.errors(record=record))

    def test_total_leaf_vertex_coverage_inflation_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][1]["encoded_total_leaves_or_vertices_consequence"] = True
        self.assertTrue(self.errors(record=record))

    def test_coordinate_deletion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][0]["coordinates"].pop()
        self.assertTrue(self.errors(record=record))

    def test_unresolved_coordinate_cannot_clear(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][0]["coordinates"][0]["classification"] = "UNRESOLVED_SEMANTIC_GAP"
        self.assertTrue(self.errors(record=record))

    def test_disqualifying_coordinate_cannot_clear(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][1]["coordinates"][0]["classification"] = "DISQUALIFYING_MISMATCH"
        self.assertTrue(self.errors(record=record))

    def test_projection_weakening_cannot_be_erased(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][0]["source_conclusion_projection"]["classification"] = "EXACT_MATCH"
        self.assertTrue(self.errors(record=record))

    def test_preactivation_clearance_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][0]["state_before_activation"] = "SEMANTIC_AND_NONVACUITY_CLEAR"
        self.assertTrue(self.errors(record=record))

    def test_postactivation_candidate_downgrade_detected(self) -> None:
        record = copy.deepcopy(self.record)
        record["targets"][1]["candidate_exit_state_after_activation"] = "SEMANTIC_PARTIAL__CHARACTERIZED_GAPS"
        self.assertTrue(self.errors(record=record))

    def test_review_gate_removal_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["activation"]["requires_non_author_approved_review"] = False
        self.assertTrue(self.errors(record=record))

    def test_head_change_reapproval_removal_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["activation"]["head_change_requires_reapproval"] = False
        self.assertTrue(self.errors(record=record))

    def test_circuit_coverage_inflation_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["arithmetic_circuit_coverage"] = True
        self.assertTrue(self.errors(record=record))

    def test_solve_authority_insertion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["solve_handoff_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_mathcert_authority_insertion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["mathcert_route_authorized"] = True
        self.assertTrue(self.errors(record=record))

    def test_proof_promotion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["mathematical_target_proved"] = True
        self.assertTrue(self.errors(record=record))

    def test_aggregate_authority_insertion_rejected(self) -> None:
        record = copy.deepcopy(self.record)
        record["route_controls"]["aggregate_openai_ten_proofs_authority"] = True
        self.assertTrue(self.errors(record=record))

    def test_repair_circuit_inflation_rejected(self) -> None:
        repair = copy.deepcopy(self.repair)
        repair["coverage_disposition"]["circuit_lower_bound_coverage"] = True
        self.assertTrue(self.errors(repair=repair))

    def test_replay_target_inventory_drift_rejected(self) -> None:
        replay = copy.deepcopy(self.replay)
        replay["successful_replay"]["target_inventory"]["targets"][0] = "PermanentFormulaLowerBound.other"
        self.assertTrue(self.errors(replay=replay))

    def test_historical_revision_audit_drift_rejected(self) -> None:
        revision = copy.deepcopy(self.revision)
        revision["admitted_manuscript"]["sha256"] = "0" * 64
        self.assertTrue(self.errors(revision=revision))


if __name__ == "__main__":
    unittest.main()
