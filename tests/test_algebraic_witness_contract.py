from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from ci import validate_forge


class AlgebraicWitnessContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_root = Path(__file__).resolve().parents[1]
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "schemas").mkdir(parents=True)
        (self.root / "governance").mkdir(parents=True)
        (self.root / "examples" / "algebraic_witnesses").mkdir(parents=True)
        for name in (
            "algebraic_witness.schema.json",
            "algebraic_witness_registry.schema.json",
        ):
            shutil.copy2(self.source_root / "schemas" / name, self.root / "schemas" / name)
        shutil.copy2(
            self.source_root / "governance" / "algebraic_witness_registry.json",
            self.root / "governance" / "algebraic_witness_registry.json",
        )
        shutil.copy2(
            self.source_root / "examples" / "algebraic_witnesses" / "GB-WITNESS-DEMO-001.json",
            self.root / "examples" / "algebraic_witnesses" / "GB-WITNESS-DEMO-001.json",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def errors(self) -> list[str]:
        with (
            patch.object(validate_forge, "ROOT", self.root),
            patch.object(validate_forge, "WORKSPACE", self.root.parent),
            patch.object(
                validate_forge,
                "ALGEBRAIC_WITNESS_DIR",
                self.root / "examples" / "algebraic_witnesses",
            ),
            patch.object(
                validate_forge,
                "ALGEBRAIC_WITNESS_REGISTRY",
                self.root / "governance" / "algebraic_witness_registry.json",
            ),
        ):
            return validate_forge.algebraic_witness_errors()

    def load_witness(self) -> tuple[Path, dict]:
        path = self.root / "examples" / "algebraic_witnesses" / "GB-WITNESS-DEMO-001.json"
        return path, json.loads(path.read_text(encoding="utf-8"))

    def rewrite_registry_digest(self, witness_path: Path) -> None:
        registry_path = self.root / "governance" / "algebraic_witness_registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["witnesses"][0]["git_blob_sha1"] = validate_forge.git_blob_sha1(witness_path)
        registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")

    def test_committed_fixture_is_valid(self) -> None:
        self.assertEqual([], self.errors())

    def test_rejects_variable_count_drift(self) -> None:
        path, witness = self.load_witness()
        witness["variables"]["variable_count"] = 3
        path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
        self.rewrite_registry_digest(path)
        self.assertTrue(any("variable_count" in error for error in self.errors()))

    def test_rejects_budget_overrun(self) -> None:
        path, witness = self.load_witness()
        witness["execution"]["peak_intermediate_terms"] = 1000
        path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
        self.rewrite_registry_digest(path)
        self.assertTrue(any("intermediate-term count exceeds" in error for error in self.errors()))

    def test_rejects_failed_execution_without_failure_entry(self) -> None:
        path, witness = self.load_witness()
        witness["execution"]["status"] = "timed_out"
        witness["handoff"]["trust_status"] = "blocked"
        path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
        self.rewrite_registry_digest(path)
        registry_path = self.root / "governance" / "algebraic_witness_registry.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        registry["witnesses"][0]["execution_status"] = "timed_out"
        registry["witnesses"][0]["trust_status"] = "blocked"
        registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(any("failure-ledger entry" in error for error in self.errors()))

    def test_rejects_unregistered_witness(self) -> None:
        extra = self.root / "examples" / "algebraic_witnesses" / "ORPHAN.json"
        extra.write_text("{}\n", encoding="utf-8")
        self.assertTrue(any("unregistered witness" in error for error in self.errors()))

    def test_rejects_blob_drift(self) -> None:
        path, witness = self.load_witness()
        witness["handoff"]["notes"] += " drift"
        path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(any("git_blob_sha1 mismatch" in error for error in self.errors()))


if __name__ == "__main__":
    unittest.main()
