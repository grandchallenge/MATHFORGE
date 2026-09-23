import copy
import json
import unittest

from catalog.build_semantic_catalog import ROOT, canonical_inventory_sha256, catalog_validation_errors, derive_source_path, msc_from_subjects, relation_policy_errors
from ci.validate_forge import validate


class SemanticCatalogTests(unittest.TestCase):
    def test_lean_quoted_module_component_preserves_embedded_dot(self):
        self.assertEqual(
            derive_source_path("FormalConjectures.Arxiv.«0911.2077».Conjecture6_3"),
            "FormalConjectures/Arxiv/0911.2077/Conjecture6_3.lean",
        )

    def test_single_digit_source_subject_maps_to_two_digit_msc_class(self):
        self.assertEqual(msc_from_subjects(["5"]), "05-XX")

    def test_inventory_digest_is_independent_of_json_formatting(self):
        first = {"problems": [
            {"module": "M.B", "theorem": "B", "subjects": ["11", "05"], "answerKinds": ["Prop", "non-Prop"]},
            {"module": "M.A", "theorem": "A", "subjects": ["03"]},
        ]}
        reordered = {"problems": [
            {"theorem": "A", "subjects": ["03"], "module": "M.A"},
            {"answerKinds": ["non-Prop", "Prop"], "subjects": ["05", "11"], "theorem": "B", "module": "M.B"},
        ]}
        self.assertEqual(canonical_inventory_sha256(first), canonical_inventory_sha256(reordered))

    def test_complete_catalog_validates(self):
        self.assertEqual(catalog_validation_errors(), [])

    def test_unknown_assurance_tier_is_rejected(self):
        entry = json.loads((ROOT / "catalog" / "entries" / "researchmath-00000.jsonl").read_text(encoding="utf-8").splitlines()[0])
        mutated = copy.deepcopy(entry)
        mutated["assurance"]["tier"] = "CERTIFIED"
        self.assertTrue(validate(mutated, "semantic_catalog_entry.schema.json", "mutated"))

    def test_status_without_issuer_is_rejected(self):
        entry = json.loads((ROOT / "catalog" / "entries" / "researchmath-00000.jsonl").read_text(encoding="utf-8").splitlines()[0])
        mutated = copy.deepcopy(entry)
        mutated["status_assertions"][0].pop("issuer")
        self.assertTrue(validate(mutated, "semantic_catalog_entry.schema.json", "mutated"))

    def test_automated_equivalence_is_forbidden(self):
        relation = {
            "schema_version": "2.0.0", "relation_id": "GCL-REL-TEST-001",
            "subject_id": "GCL-CAT-RM-00000", "predicate": "same_statement",
            "object_id": "GCL-CAMPAIGN:TEST", "review_state": "AUTOMATED_PROPOSAL",
            "proposer": "lexical matcher", "evidence": ["similarity:1.0"],
        }
        self.assertEqual(validate(relation, "semantic_relation.schema.json", "relation"), [])
        self.assertTrue(relation_policy_errors(relation))

    def test_certification_is_explicitly_excluded(self):
        entry = json.loads((ROOT / "catalog" / "entries" / "researchmath-00000.jsonl").read_text(encoding="utf-8").splitlines()[0])
        self.assertIn("certification", entry["excluded_inferences"])
        self.assertNotIn("certificate", entry)


if __name__ == "__main__":
    unittest.main()
