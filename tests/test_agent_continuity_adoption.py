from __future__ import annotations

import copy
import unittest

from ci.validate_agent_continuity_adoption import ROOT, adoption_errors, load_json


class AgentContinuityAdoptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.record = load_json(ROOT / ".gcl/agent-continuity.json")
        cls.agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    def errors(self, mutate) -> list[str]:
        record = copy.deepcopy(self.record)
        mutate(record)
        return adoption_errors(record, self.agents)

    def test_repository_candidate_is_valid(self) -> None:
        self.assertEqual([], adoption_errors(self.record, self.agents))

    def test_common_policy_drift_is_rejected(self) -> None:
        errors = self.errors(lambda r: r.update({"policy_id": "OTHER"}))
        self.assertTrue(any("common schema" in error for error in errors))

    def test_local_validator_identity_is_required(self) -> None:
        errors = self.errors(lambda r: r.pop("local_validator"))
        self.assertTrue(any("local_validator" in error for error in errors))

    def test_schema_binding_cannot_drift(self) -> None:
        errors = self.errors(
            lambda r: r["specialization_data"]["schema_binding"].update(
                {"schema_blob_sha": "0" * 40}
            )
        )
        self.assertTrue(any("schema_blob_sha" in error for error in errors))

    def test_mutable_remote_schema_fetch_is_forbidden(self) -> None:
        errors = self.errors(
            lambda r: r["specialization_data"]["schema_binding"].update(
                {"mutable_remote_fetch_allowed": True}
            )
        )
        self.assertTrue(any("mutable_remote_fetch_allowed" in error for error in errors))

    def test_provenance_requirements_cannot_be_disabled(self) -> None:
        errors = self.errors(
            lambda r: r["specialization_data"]["checkpoint_requirements"].update(
                {"source_or_provider_identity": False}
            )
        )
        self.assertTrue(any("source_or_provider_identity" in error for error in errors))

    def test_discovery_evidence_cannot_be_elevated_to_proof(self) -> None:
        errors = self.errors(
            lambda r: r["authority_preservation"].update(
                {"discovery_evidence_is_proof": True}
            )
        )
        self.assertTrue(any("discovery_evidence_is_proof" in error for error in errors))

    def test_certification_authority_cannot_expand(self) -> None:
        errors = self.errors(
            lambda r: r["authority_preservation"].update(
                {"certification_authority_changed": True}
            )
        )
        self.assertTrue(any("certification_authority_changed" in error for error in errors))

    def test_promotion_authority_cannot_expand(self) -> None:
        errors = self.errors(
            lambda r: r["authority_preservation"].update(
                {"promotion_authority_changed": True}
            )
        )
        self.assertTrue(any("promotion_authority_changed" in error for error in errors))

    def test_agent_substitution_cannot_inherit_independent_verification(self) -> None:
        errors = self.errors(
            lambda r: r["authority_preservation"].update(
                {"independent_verification_inherited_across_agent_substitution": True}
            )
        )
        self.assertTrue(any("independent_verification_inherited" in error for error in errors))

    def test_routine_short_operations_are_not_forced_into_checkpointing(self) -> None:
        errors = self.errors(
            lambda r: r["specialization_data"]["applicability"].update(
                {"routine_short_operations_checkpoint_required": True}
            )
        )
        self.assertTrue(any("routine short operations" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
