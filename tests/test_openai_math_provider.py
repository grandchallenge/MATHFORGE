"""Gate exact OpenAI Math provider admission at SOURCE_LOCKED assurance only."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = "OAI-MATH-1581D4CB"

class SourceOnlyProviderTests(unittest.TestCase):
    def test_admitted_metadata_only(self):
        registry = json.loads((ROOT / "governance/external_sources.json").read_text())
        row = next(x for x in registry["providers"] if x["provider_id"] == "OAI-MATH-2026")
        self.assertEqual(row["source_class"], "mathematical_corpus")
        self.assertEqual(row["visibility"], "public_metadata_only")
        self.assertEqual(row["licensing"]["disposition"], "metadata_only")
        self.assertFalse(row["refresh_policy"]["automatic_admission"])
        manifest = json.loads((ROOT / "catalog/manifest.json").read_text())
        self.assertEqual(manifest["total_entries"], 18007)
        self.assertIn(SNAPSHOT, manifest["provider_snapshots"])
        snapshot = json.loads((ROOT / "catalog/providers" / (SNAPSHOT + ".json")).read_text())
        self.assertEqual(snapshot["inventory_count"], 719)
        self.assertEqual(sum(s["entry_count"] for s in snapshot["catalog_shards"]), 719)
        for shard in snapshot["catalog_shards"]:
            for line in (ROOT / shard["path"]).read_text(encoding="utf-8").splitlines():
                entry = json.loads(line)
                self.assertEqual(entry["assurance"]["tier"], "SOURCE_LOCKED")
                self.assertEqual(entry["statement_kind"], "other")
                self.assertEqual(entry["licensing"]["redistribution_class"], "metadata_only")
                self.assertEqual(entry["proof_annotations"], [])
                self.assertEqual(entry["relation_ids"], [])
                self.assertIn("certification", entry["excluded_inferences"])

    def test_pinned_builder_reproduces_committed_bytes(self):
        manifest_path = ROOT / "catalog/providers" / (SNAPSHOT + ".json")
        before = manifest_path.read_bytes()
        manifest = json.loads(before)
        shard_bytes = {s["path"]: (ROOT / s["path"]).read_bytes() for s in manifest["catalog_shards"]}
        completed = subprocess.run(
            [sys.executable, "catalog/build_openai_math_provider.py", "build"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertEqual(completed.returncode, 0, msg=completed.stdout + completed.stderr)
        self.assertEqual(before, manifest_path.read_bytes())
        for p, b in shard_bytes.items():
            self.assertEqual(b, (ROOT / p).read_bytes(), msg=p)

if __name__ == "__main__":
    unittest.main()
