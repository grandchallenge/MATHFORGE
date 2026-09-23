import copy
import unittest

from catalog.compute_delta import compute_delta
from ci.validate_forge import validate


def entry(locator="source#one"):
    return {
        "source": {"locator": locator},
        "representations": {"normalized": "statement one"},
        "classification": {"msc2020_primary": "11-XX"},
        "status_assertions": [{"issuer": "provider", "value": "open"}],
        "proof_annotations": [],
        "formal_language": {"toolchain": "Lean 4.27.0"},
    }


class CatalogDeltaTests(unittest.TestCase):
    def delta(self, old, new, to_revision="b" * 40):
        return compute_delta("FC-GDM", "a" * 40, to_revision, "2026-09-22T00:00:00Z", old, new)

    def test_addition_and_deletion(self):
        delta = self.delta([entry()], [entry("source#two")])
        self.assertEqual(delta["additions"], ["source#two"])
        self.assertEqual(delta["deletions"], ["source#one"])

    def test_statement_status_proof_and_toolchain_changes(self):
        old = entry()
        new = copy.deepcopy(old)
        new["representations"]["normalized"] = "statement two"
        new["status_assertions"][0]["value"] = "solved"
        new["proof_annotations"] = [{"issuer": "provider", "value": "proof"}]
        new["formal_language"]["toolchain"] = "Lean 4.33.1"
        delta = self.delta([old], [new])
        self.assertEqual(delta["statement_changes"], ["source#one"])
        self.assertEqual(delta["classification_or_status_changes"], ["source#one"])
        self.assertEqual(delta["proof_annotation_changes"], ["source#one"])
        self.assertIsNotNone(delta["toolchain_change"])
        self.assertEqual(delta["possible_semantic_invalidations"], ["source#one"])
        self.assertEqual(validate(delta, "external_source_delta.schema.json", "delta"), [])

    def test_provider_rollback_remains_non_admitting(self):
        delta = self.delta([entry()], [entry()], to_revision="0" * 40)
        self.assertFalse(delta["automatic_admission"])


if __name__ == "__main__":
    unittest.main()
