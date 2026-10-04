#!/usr/bin/env python3
from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "ci" / "validate_erdos_open_intake.py"
SPEC = importlib.util.spec_from_file_location("validate_erdos_open_intake", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)

LOCK = MODULE.load_json(MODULE.LOCK_PATH)
MANIFEST = MODULE.load_json(MODULE.MANIFEST_PATH)
FC_INDEX = MODULE.load_json(MODULE.FC_INDEX_PATH)
SCHEMA = MODULE.load_json(MODULE.SCHEMA_PATH)


class ErdosOpenIntakeTests(unittest.TestCase):
    def errors(self, manifest=None, lock=None, fc_index=None):
        return MODULE.validation_errors(
            lock if lock is not None else LOCK,
            manifest if manifest is not None else MANIFEST,
            fc_index if fc_index is not None else FC_INDEX,
            SCHEMA,
        )

    def test_baseline_accepts(self):
        self.assertEqual(self.errors(), [])

    def test_expected_counts(self):
        summary = MANIFEST["summary"]
        self.assertEqual(summary["registry_problem_count"], 1221)
        self.assertEqual(summary["strict_open_count"], 593)
        self.assertEqual(summary["strict_open_with_protected_fc_formalization"], 298)
        self.assertEqual(
            summary["strict_open_with_registry_reported_formalization_not_in_protected_fc_snapshot"], 59
        )
        self.assertEqual(summary["strict_open_without_registry_reported_formalization"], 236)
        self.assertEqual(
            summary["strict_open_with_formal_solution_pending_human_status_reconciliation"], 4
        )
        self.assertEqual(summary["excluded_special_unresolved_status_count"], 52)

    def test_rejects_status_inflation(self):
        candidate = copy.deepcopy(MANIFEST)
        candidate["entries"][0]["registry_status"]["state"] = "proved"
        self.assertTrue(self.errors(candidate))

    def test_rejects_duplicate_or_missing_projection(self):
        candidate = copy.deepcopy(MANIFEST)
        candidate["entries"].append(copy.deepcopy(candidate["entries"][0]))
        candidate["summary"]["strict_open_count"] += 1
        self.assertTrue(self.errors(candidate))

    def test_rejects_fake_protected_formalization(self):
        candidate = copy.deepcopy(MANIFEST)
        row = next(item for item in candidate["entries"] if not item["protected_fc"]["present"])
        row["protected_fc"] = {
            "present": True,
            "path": f"FormalConjectures/ErdosProblems/{row['problem_id']}.lean",
            "git_blob_sha1": "0" * 40,
        }
        row["gcl_disposition"] = "OPEN_WITH_PROTECTED_FC_FORMALIZATION"
        self.assertTrue(self.errors(candidate))

    def test_rejects_solve_authorization_inflation(self):
        candidate = copy.deepcopy(MANIFEST)
        candidate["entries"][0]["solve_eligibility"] = "AUTHORIZED"
        self.assertTrue(self.errors(candidate))

    def test_rejects_formal_solution_hold_removal(self):
        candidate = copy.deepcopy(MANIFEST)
        row = next(item for item in candidate["entries"] if item["registry_solution_formalized"]["state"] == "Lean")
        row["programme_triage_state"] = "ELIGIBLE_FOR_PROGRAMME_TRIAGE"
        self.assertTrue(self.errors(candidate))

    def test_rejects_global_authority_inflation(self):
        candidate = copy.deepcopy(MANIFEST)
        candidate["authority_boundary"]["certification_authorized"] = True
        self.assertTrue(self.errors(candidate))


if __name__ == "__main__":
    unittest.main()
