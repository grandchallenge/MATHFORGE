"""Adversarial tests for exact-pinned OAI26 F011 cloud replay worker.

The production Lake error guard is extracted from the committed worker's AST
and executed with a fake git readback. No network, Colab session or build.
"""
import ast
import hashlib
from pathlib import Path
from types import SimpleNamespace
import unittest
import tempfile

WORKER = Path(__file__).resolve().parents[1] / "scripts" / "oai26_f011_external_proof_replay.py"
SHA256 = "a410b203c934da98aa6c03a6dde8f1bbb8eca7ba272962e77216f3a39ab160b3"
ROOT = Path("/content/gcl_colab_job/src")
REVISIONS = {
    "OAI": "adc7f1241b42e322a6451854ab7e4b4c146bf78a",
    "iut": "d9465c111ec4073709f67e9fccec7e3eb374a816",
    "mathlib": "d13f23b723b8a846827a245b89c10fc7d3f11612",
}
EXPECTED = f"error: iut: Lake resolved an unexpected checkout at {ROOT/'.lake/packages/iut'}."

def guard_code():
    tree = ast.parse(WORKER.read_text())
    matches = [
        n for n in ast.walk(tree) if isinstance(n, ast.If)
        and isinstance(n.test, ast.Compare)
        and isinstance(n.test.left, ast.Name) and n.test.left.id == "lake_rc"
        and len(n.test.ops) == 1 and isinstance(n.test.ops[0], ast.NotEq)
        and len(n.test.comparators) == 1
        and isinstance(n.test.comparators[0], ast.Constant)
        and n.test.comparators[0].value == 0
    ]
    if len(matches) != 1:
        raise ValueError("ambiguous or missing real Lake guard")
    return compile(ast.fix_missing_locations(ast.Module(body=matches, type_ignores=[])), str(WORKER), "exec")

def replay_guard(log, lake_rc=1, revisions=None):
    mapping = revisions or REVISIONS
    def check_output(args, *, env, text):
        assert args[:3] == ["git", "-C", str(ROOT/".lake/packages"/args[2].split("/")[-1])] or args[:1]==["git"]
        package = Path(args[2]).name
        return mapping[package] + "\n"
    with tempfile.TemporaryDirectory() as d:
        out = Path(d)
        (out/"lake_update.log").write_text(log)
        environment = dict(
            lake_rc=lake_rc, OUT=out, ROOT=ROOT,
            MATHLIB=REVISIONS["mathlib"], ENV={},
            subprocess=SimpleNamespace(check_output=check_output),
        )
        exec(guard_code(), environment)

class TestF011CloudWorker(unittest.TestCase):
    def test_source_pin(self):
        self.assertEqual(hashlib.sha256(WORKER.read_bytes()).hexdigest(), SHA256)

    def test_no_bypass_of_source_pin(self):
        s=WORKER.read_text()
        self.assertIn("        check_pins(ROOT,ENV)\n        if lake_rc!=0:",s)
        self.assertIn("execute(\"apply_patches\",",s)
        self.assertIn("execute(\"leanchecker\",",s)
        self.assertIn("execute(\"verify\",",s)

    def test_documented_condition_with_correct_git_revisions(self):
        replay_guard("info: dependency checkout finished\n"+EXPECTED+"\nEXIT 1\n")

    def test_unexpected_guard_is_refused(self):
        with self.assertRaisesRegex(RuntimeError,"UNEXPECTED_LAKE_UPDATE_FAILURE"):
            replay_guard("error: unrelated transitive dependency failed\n")

    def test_multiple_errors_not_accepted(self):
        with self.assertRaisesRegex(RuntimeError,"UNEXPECTED_LAKE_UPDATE_FAILURE"):
            replay_guard(EXPECTED+"\nerror: missing source package\n")

    def test_transport_timeout_not_accepted(self):
        with self.assertRaisesRegex(RuntimeError,"UNEXPECTED_LAKE_UPDATE_FAILURE"):
            replay_guard(EXPECTED+"\n",lake_rc=124)

    def test_fake_git_revision_not_accepted(self):
        for package in REVISIONS:
            modified=dict(REVISIONS);modified[package]="0"*40
            with self.subTest(package=package), self.assertRaisesRegex(RuntimeError,"PINNED_POSTUPDATE_REVISION_DRIFT"):
                replay_guard(EXPECTED+"\n",revisions=modified)

    def test_unrelated_stdout_not_promoted_to_error(self):
        # A successful command needs no exception; other stages remain pinned.
        replay_guard("info: packages fetched\n",lake_rc=0)

if __name__ == "__main__":
    unittest.main()
