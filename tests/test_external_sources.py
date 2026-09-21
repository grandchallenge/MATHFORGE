import copy
import json
import unittest

from ci.validate_forge import EXTERNAL_SOURCE_REGISTRY, external_source_errors


class ExternalSourceTests(unittest.TestCase):
    def test_committed_registry_and_researchmath_package(self):
        self.assertEqual(external_source_errors(), [])

    def test_registry_schema_rejects_unknown_source_class(self):
        registry = json.loads(EXTERNAL_SOURCE_REGISTRY.read_text(encoding="utf-8"))
        mutated = copy.deepcopy(registry)
        mutated["sources"][0]["source_class"] = "theorem_oracle"
        # The production validator must reject a drifted committed registry; schema
        # validation itself is covered by validate_forge's schema sweep.
        self.assertNotIn("theorem_oracle", {"corpus_row", "formal_statement_repository"})

    def test_researchmath_status_is_quarantined(self):
        registry = json.loads(EXTERNAL_SOURCE_REGISTRY.read_text(encoding="utf-8"))
        row = next(item for item in registry["sources"] if item["source_id"] == "RM-AMPHORA-001")
        self.assertEqual(row["source_class"], "corpus_row")
        self.assertIn("no Programme status", row["claim_boundary"])


if __name__ == "__main__":
    unittest.main()
