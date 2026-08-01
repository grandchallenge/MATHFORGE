from __future__ import annotations

import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_ten_proofs_semantic",
    ROOT / "ci" / "validate_ten_proofs_semantic.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TenProofsSemanticAuditTests(unittest.TestCase):
    def setUp(self) -> None:
        self.records = MODULE.load_records()
        self.document = MODULE.DOCUMENT_PATH.read_text(encoding="utf-8")

    def errors(self, records=None, document=None):
        return MODULE.validation_errors(
            records=copy.deepcopy(self.records if records is None else records),
            document=self.document if document is None else document,
        )

    def record_for(self, family: str):
        for filename, record in self.records.items():
            if record["result_family"] == family:
                return filename, record
        self.fail(f"missing record for {family}")

    def test_current_tranche_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_source_gate_cannot_clear_before_activation(self) -> None:
        filename, _ = self.record_for("OTP-F-EHRHART")
        records = copy.deepcopy(self.records)
        records[filename]["disposition"]["source_gate_before_activation"] = "clear"
        self.assertTrue(self.errors(records))

    def test_route_cannot_open_before_activation(self) -> None:
        filename, _ = self.record_for("OTP-J1-COMPACTNESS")
        records = copy.deepcopy(self.records)
        records[filename]["route_effect"]["may_route_before_activation"] = True
        self.assertTrue(self.errors(records))

    def test_aggregate_route_and_cert_self_authorization_are_rejected(self) -> None:
        filename, _ = self.record_for("OTP-J2-TWO-DEGENERATE")
        for field in ("aggregate_route_permitted", "mathcert_adjudication_authorized"):
            with self.subTest(field=field):
                records = copy.deepcopy(self.records)
                records[filename]["route_effect"][field] = True
                self.assertTrue(self.errors(records))

    def test_exact_lean_identity_cannot_drift(self) -> None:
        filename, _ = self.record_for("OTP-F-EHRHART")
        records = copy.deepcopy(self.records)
        records[filename]["lean"]["challenge_blob"] = "0" * 40
        self.assertTrue(self.errors(records))

    def test_theorem_target_set_cannot_drift(self) -> None:
        filename, _ = self.record_for("OTP-J1-COMPACTNESS")
        records = copy.deepcopy(self.records)
        records[filename]["lean"]["theorem_names"].pop()
        self.assertTrue(self.errors(records))

    def test_nonvacuity_requires_checked_witness(self) -> None:
        filename, _ = self.record_for("OTP-J2-TWO-DEGENERATE")
        records = copy.deepcopy(self.records)
        records[filename]["nonvacuity"]["witness_theorems"] = []
        self.assertTrue(self.errors(records))

    def test_head_change_must_require_reapproval(self) -> None:
        filename, _ = self.record_for("OTP-F-EHRHART")
        records = copy.deepcopy(self.records)
        records[filename]["activation"]["head_change_requires_reapproval"] = False
        self.assertTrue(self.errors(records))

    def test_blocked_repair_lane_cannot_enter_clear_tranche(self) -> None:
        filename, _ = self.record_for("OTP-F-EHRHART")
        records = copy.deepcopy(self.records)
        records[filename]["result_family"] = "OTP-C-PERMANENT"
        self.assertTrue(self.errors(records))

    def test_unexpected_record_is_rejected(self) -> None:
        records = copy.deepcopy(self.records)
        records["EXTRA.json"] = copy.deepcopy(next(iter(records.values())))
        self.assertTrue(self.errors(records))

    def test_document_preserves_route_and_blocker_tokens(self) -> None:
        for token in (
            "No handoff opens on this branch",
            "Permanent",
            "GapCVP",
            "All.lean",
        ):
            with self.subTest(token=token):
                document = self.document.replace(token, "REMOVED", 1)
                self.assertTrue(self.errors(document=document))


if __name__ == "__main__":
    unittest.main()
