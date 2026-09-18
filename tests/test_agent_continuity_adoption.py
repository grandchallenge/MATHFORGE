from __future__ import annotations

import copy
import unittest

from ci.validate_agent_continuity_adoption import ROOT, adoption_errors, load_json

class AgentContinuityAdoptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.record = load_json(ROOT / ".gcl/agent-continuity.json")
        cls.agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")

    def test_repository_candidate_is_valid(self) -> None:
        self.assertEqual([], adoption_errors(self.record, self.agents))

    def test_provenance_requirements_cannot_be_disabled(self) -> None:
        record = copy.deepcopy(self.record)
        record["checkpoint_requirements"]["source_or_provider_identity"] = False
        errors = adoption_errors(record, self.agents)
        self.assertTrue(any("source_or_provider_identity" in error for error in errors))

    def test_discovery_evidence_cannot_be_elevated_to_proof(self) -> None:
        record = copy.deepcopy(self.record)
        record["authority_preservation"]["discovery_evidence_is_proof"] = True
        errors = adoption_errors(record, self.agents)
        self.assertTrue(any("discovery_evidence_is_proof" in error for error in errors))

    def test_agent_substitution_cannot_inherit_independent_verification(self) -> None:
        record = copy.deepcopy(self.record)
        record["authority_preservation"]["independent_verification_inherited_across_agent_substitution"] = True
        errors = adoption_errors(record, self.agents)
        self.assertTrue(any("independent_verification_inherited" in error for error in errors))

    def test_routine_short_operations_are_not_forced_into_checkpointing(self) -> None:
        record = copy.deepcopy(self.record)
        record["applicability"]["routine_short_operations_checkpoint_required"] = True
        errors = adoption_errors(record, self.agents)
        self.assertTrue(any("routine short operations" in error for error in errors))

if __name__ == "__main__":
    unittest.main()
