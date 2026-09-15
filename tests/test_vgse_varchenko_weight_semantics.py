from __future__ import annotations

import importlib.util
import io
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "classify_vgse_varchenko_weight_semantics",
    ROOT / "tools" / "classify_vgse_varchenko_weight_semantics.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VgseVarchenkoWeightSemanticsTests(unittest.TestCase):
    def make_archive(self, tex: bytes) -> Path:
        handle = tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False)
        handle.close()
        path = Path(handle.name)
        with tarfile.open(path, "w:gz") as archive:
            for name, data in {
                "main.tex": tex,
                "figures_t_emb/Varc-a.pdf": b"%PDF synthetic",
                "figures_t_emb/Varc-b.pdf": b"%PDF synthetic",
            }.items():
                info = tarfile.TarInfo(name)
                info.size = len(data)
                archive.addfile(info, io.BytesIO(data))
        self.addCleanup(lambda: path.unlink(missing_ok=True))
        return path

    def test_classifies_weight_definition_by_lhs_position(self) -> None:
        record = MODULE.classify_line(r"\\mathrm{wt}(e)=\\frac{2}{7}", 10)
        self.assertIsNotNone(record)
        self.assertEqual(record["classification"], "weight_definition_candidate")
        self.assertTrue(record["weight_token_on_lhs"])
        self.assertTrue(record["numeric_rhs"])

    def test_classifies_c_equals_measurement_as_measurement_relation(self) -> None:
        record = MODULE.classify_line(r"C=\\operatorname{Meas}(\\Gamma,\\mathrm{wt})", 11)
        self.assertIsNotNone(record)
        self.assertEqual(record["classification"], "measurement_relation")
        self.assertTrue(record["measurement_token_on_rhs"])
        self.assertTrue(record["weight_token_on_rhs"])

    def test_classifies_measurement_equals_c_as_measurement_relation(self) -> None:
        record = MODULE.classify_line(r"\\operatorname{Meas}(\\Gamma,\\mathrm{wt})=C", 12)
        self.assertIsNotNone(record)
        self.assertEqual(record["classification"], "measurement_relation")
        self.assertTrue(record["measurement_token_on_lhs"])
        self.assertTrue(record["weight_token_on_lhs"])

    def test_archive_record_emits_no_source_prose(self) -> None:
        tex = b"""\\mathrm{wt}(e)=3\n\\operatorname{Meas}(\\Gamma,\\mathrm{wt})=C\n\\includegraphics{figures_t_emb/Varc-a}\n\\includegraphics{figures_t_emb/Varc-b}\n"""
        record = MODULE.build_record(self.make_archive(tex))
        self.assertEqual(record["summary"]["numeric_weight_definition_candidate_lines"], [1])
        self.assertEqual(record["summary"]["measurement_relation_lines"], [2])
        self.assertFalse(record["interpretation"]["source_prose_emitted"])
        self.assertNotIn("text", record["relations"][0])


if __name__ == "__main__":
    unittest.main()
