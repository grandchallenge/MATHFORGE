from __future__ import annotations

import importlib.util
import io
import tarfile
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "audit_vgse_arxiv_source_archive",
    ROOT / "tools" / "audit_vgse_arxiv_source_archive.py",
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VgseArxivSourceArchiveTests(unittest.TestCase):
    def make_archive(self, files: dict[str, bytes]) -> Path:
        handle = tempfile.NamedTemporaryFile(suffix=".tar.gz", delete=False)
        handle.close()
        path = Path(handle.name)
        with tarfile.open(path, "w:gz") as archive:
            for name, data in files.items():
                info = tarfile.TarInfo(name)
                info.size = len(data)
                archive.addfile(info, io.BytesIO(data))
        self.addCleanup(lambda: path.unlink(missing_ok=True))
        return path

    def test_resolves_example_figure_and_reports_code(self) -> None:
        tex = b"""\\begin{figure}\n\\includegraphics{figures/f16}\n\\caption{Five pictures}\n\\label{fig:five}\n\\end{figure}\nExample B.3 some t-embedding weighted graph statement\n"""
        archive = self.make_archive(
            {
                "main.tex": tex,
                "figures/f16.pdf": b"%PDF-1.4 synthetic",
                "gen.py": b"weights = [1,2,3] # matching",
            }
        )
        record = MODULE.build_record(archive)
        self.assertEqual(record["member_count"], 3)
        self.assertEqual(
            record["example_markers"][0]["resolved_figure_assets"][0]["resolved_member"],
            "figures/f16.pdf",
        )
        self.assertEqual(record["code_members"][0]["path"], "gen.py")
        self.assertTrue(record["generation_term_hits_in_code_or_data"])
        self.assertFalse(record["interpretation"]["mathematical_certification_performed"])

    def test_no_generation_code_is_reported_without_invention(self) -> None:
        archive = self.make_archive(
            {
                "paper.tex": b"Example B.3\n\\includegraphics{f16.pdf}",
                "f16.pdf": b"pdf",
            }
        )
        record = MODULE.build_record(archive)
        self.assertEqual(record["code_members"], [])
        self.assertEqual(record["data_members"], [])
        self.assertEqual(record["generation_term_hits_in_code_or_data"], [])


if __name__ == "__main__":
    unittest.main()
