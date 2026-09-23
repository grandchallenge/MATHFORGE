import copy, json, unittest
from ci.validate_chaidez_catalog_boundary import POLICY, errors

class BoundaryTests(unittest.TestCase):
    def setUp(self): self.policy = json.loads(POLICY.read_text())
    def test_policy(self): self.assertEqual(errors(self.policy), [])
    def test_no_ingestion_dossier(self):
        changed = copy.deepcopy(self.policy); changed["chaidez_dossier_at_ingestion"] = True
        self.assertTrue(errors(changed))
    def test_no_automatic_promotion(self):
        changed = copy.deepcopy(self.policy); changed["automatic_promotion"] = True
        self.assertTrue(errors(changed))
    def test_reviewed_minimum(self):
        changed = copy.deepcopy(self.policy); changed["minimum_proposal_assurance_tier"] = "SOURCE_LOCKED"
        self.assertTrue(errors(changed))

if __name__ == "__main__": unittest.main()
