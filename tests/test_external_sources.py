import copy
import json
import unittest

from ci.validate_forge import EXTERNAL_SOURCE_REGISTRY, external_source_errors, validate


class ExternalSourceTests(unittest.TestCase):
    def test_committed_registry_and_researchmath_package(self):
        self.assertEqual(external_source_errors(), [])

    def test_registry_schema_rejects_unknown_source_class(self):
        registry = json.loads(EXTERNAL_SOURCE_REGISTRY.read_text(encoding="utf-8"))
        mutated = copy.deepcopy(registry)
        mutated["providers"][0]["source_class"] = "theorem_oracle"
        self.assertTrue(validate(mutated, "external_source_registry.schema.json", "mutated"))

    def test_registry_schema_rejects_automatic_admission(self):
        registry = json.loads(EXTERNAL_SOURCE_REGISTRY.read_text(encoding="utf-8"))
        mutated = copy.deepcopy(registry)
        mutated["providers"][0]["refresh_policy"]["automatic_admission"] = True
        self.assertTrue(validate(mutated, "external_source_registry.schema.json", "mutated"))

    def test_researchmath_status_is_quarantined(self):
        registry = json.loads(EXTERNAL_SOURCE_REGISTRY.read_text(encoding="utf-8"))
        row = next(item for item in registry["providers"] if item["provider_id"] == "RM-AMPHORA-001")
        self.assertEqual(row["source_class"], "mathematical_corpus")
        self.assertIn("no Programme status", row["claim_boundary"])

    def test_deepmind_scopes_are_aliases_of_one_provider(self):
        registry = json.loads(EXTERNAL_SOURCE_REGISTRY.read_text(encoding="utf-8"))
        deepmind = next(item for item in registry["providers"] if item["provider_id"] == "FC-GDM")
        self.assertEqual(deepmind["legacy_source_ids"], ["FC-GDM-001", "FC-GDM-002"])
        self.assertEqual(deepmind["observatory"]["admission_state"], "UPSTREAM_AHEAD")


if __name__ == "__main__":
    unittest.main()
