#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ci" / "validate_euclid_diophantine_forge.py"
spec = importlib.util.spec_from_file_location("validate_euclid_diophantine_forge", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)
PACKAGE = json.loads((ROOT / "sources" / "EUCLID-DIOPHANTINE-E2E-002" / "forge_package.json").read_text(encoding="utf-8"))
SCHEMA = json.loads((ROOT / "schemas" / "euclid_diophantine_forge_package.schema.json").read_text(encoding="utf-8"))


class EuclidDiophantineForgeTests(unittest.TestCase):
    def errors(self, candidate):
        return module.validate_package(candidate, SCHEMA)

    def assert_rejected(self, candidate):
        self.assertTrue(self.errors(candidate))

    def test_baseline_accepts(self):
        self.assertEqual(self.errors(PACKAGE), [])

    def test_rejects_stage1_identity_substitution(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["protected_stage1_reuse"]["cert"]["merge_commit"] = "0" * 40
        self.assert_rejected(candidate)

    def test_rejects_competing_gcd_policy(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["protected_stage1_reuse"]["reuse_policy"] = "create a replacement gcd definition"
        self.assert_rejected(candidate)

    def test_rejects_not_both_zero_widening(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["problem_card"]["input_contract"]["excluded"] = []
        self.assert_rejected(candidate)

    def test_rejects_zero_target_policy_removal(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["problem_card"]["input_contract"]["zero_target_policy"] = "unspecified"
        self.assert_rejected(candidate)

    def test_rejects_scale_factor_drift(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["reconnaissance_ledger"]["positive_exemplar"]["scale_factor"] = 5
        self.assert_rejected(candidate)

    def test_rejects_constructive_witness_drift(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["reconnaissance_ledger"]["positive_exemplar"]["candidate_solution"]["x"] = -7
        self.assert_rejected(candidate)

    def test_rejects_target_substitution(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["solve_handoff"]["cases"][0]["inputs"]["c"] = 63
        self.assert_rejected(candidate)

    def test_rejects_zero_remainder_as_negative_obstruction(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["reconnaissance_ledger"]["negative_exemplar"]["divisibility_obstruction"]["remainder"] = 0
        candidate["reconnaissance_ledger"]["negative_exemplar"]["divisibility_obstruction"]["quotient"] = 0
        self.assert_rejected(candidate)

    def test_rejects_false_obstruction_equation(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["reconnaissance_ledger"]["negative_exemplar"]["divisibility_obstruction"]["quotient"] = 1
        self.assert_rejected(candidate)

    def test_rejects_timeout_as_unsat_permission(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["solve_handoff"]["forbidden_claims"].remove("unsatisfiable because search failed")
        self.assert_rejected(candidate)

    def test_rejects_premature_certificate_authority(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["solve_handoff"]["required_output"]["authority_state"] = "certified"
        self.assert_rejected(candidate)

    def test_rejects_risk_ledger_gap(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["failure_risks"] = candidate["failure_risks"][:-1]
        self.assert_rejected(candidate)

    def test_rejects_historical_attribution_inflation(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["source_map"][2]["status"] = "verbatim_equivalent"
        self.assert_rejected(candidate)

    def test_rejects_arbitrary_diophantine_completeness(self):
        candidate = copy.deepcopy(PACKAGE)
        candidate["claim_boundary"]["claims_arbitrary_diophantine_completeness"] = True
        self.assert_rejected(candidate)


if __name__ == "__main__":
    unittest.main()
