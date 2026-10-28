"""Hostile offline checks for the bounded index-145 timeout exception."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "sources" / "OPENAI-MATH-2026"))
from replay_corpus_lean import validate_build_timeout

class CorpusBudgetGuards(unittest.TestCase):
    def test_legacy_budgets_unchanged(self):
        for timeout in (1500, 4200):
            for start, count in ((25, 5), (145, 1), (199, 1)):
                self.assertIsNone(validate_build_timeout(start, count, timeout))

    def test_exact_exception_only(self):
        self.assertIsNone(validate_build_timeout(145, 1, 6500))
        for start, count in ((144, 1), (146, 1), (145, 2), (145, 5), (199, 1), (25, 1)):
            with self.subTest(start=start, count=count):
                with self.assertRaises(ValueError):
                    validate_build_timeout(start, count, 6500)

    def test_unknown_budget_rejected(self):
        for timeout in (0, 1800, 4201, 7200):
            with self.assertRaises(ValueError):
                validate_build_timeout(145, 1, timeout)

    def test_workflow_advertises_and_guards_exception(self):
        text = (ROOT / ".github/workflows/openai-math-corpus-lean.yml").read_text()
        self.assertIn('          - "6500"', text)
        self.assertIn('GCL_START: ${{ inputs.shard_start }}', text)
        self.assertIn('GCL_COUNT: ${{ inputs.shard_count }}', text)
        self.assertIn('"$GCL_START" != "145" || "$GCL_COUNT" != "1"', text)
        self.assertIn('timeout-minutes: 145', text)

if __name__ == "__main__":
    unittest.main()
