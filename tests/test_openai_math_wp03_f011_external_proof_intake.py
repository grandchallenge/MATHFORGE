"""Source-pinned external F011 proof-candidate intake; no GCL proof promotion."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

P = Path(__file__).resolve().parents[1]/"sources"/"OPENAI-MATH-2026"/"WP03_F011_EXTERNAL_ANALYTIC_LEAN_PROOF_INTAKE.json"
PIN = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"
AUX = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
HEAD = "f75d4f2c2d6685a0547f17fa07240377aa2c2ed4"

def validate(d):
    if d["record_type"] != "GCL_OAI26_F011_INDEPENDENT_LEAN_ANALYTIC_PROOF_SOURCE_INTAKE/1":
        raise ValueError("unknown receipt")
    if d["exact_source"]["gcl_revision"] != PIN or d["exact_source"]["external_revision"] != AUX:
        raise ValueError("source revision drift")
    if d["exact_source"]["matched_files_count"] != 10:
        raise ValueError("source coverage drift")
    files = d["exact_source"]["matched_manuscript_blobs"]
    if len(files) != 8 or any(not k.endswith(".tex") or len(v) != 40 for k,v in files.items()):
        raise ValueError("source section mismatch")
    if not all(len(d["exact_source"][k]) == 40 for k in ("master_paper_tex_blob","bibliography_blob")):
        raise ValueError("non-pinned manuscript source")
    ext = d["external_repository"]
    if ext["name"] != "cadamcat/totient-fibers-lean4" or ext["head"] != HEAD or ext["total_lean_modules"] != 939:
        raise ValueError("external identity drift")
    if ext["supply_contract"]["quantifiers"] != "∀ real δ, 0<δ<1/4; ∀ σ>0; ∀ᶠ real x atTop":
        raise ValueError("fixed-delta real-x quantifier loss")
    if "p−1" not in ext["supply_contract"]["prime_predicate"] or "floor(2x)" not in ext["supply_contract"]["prime_predicate"]:
        raise ValueError("shifted prime predicate drift")
    packages = ext["closed_package_graph"]["interfaces"]
    if len(packages) != 10 or [p["name"] for p in packages] != [f"P{i}" for i in range(1,11)]:
        raise ValueError("package map incomplete")
    if any(p["paper_section"] not in files for p in packages):
        raise ValueError("bad manuscript reference")
    if ext["static_gate"]["gcl_exit_code"] != 0 or ext["static_gate"]["last_verified_source_head"] != HEAD:
        raise ValueError("unverified static gate")
    report=d["external_author_report"]
    if report["trusted_as"] != "AUTHOR_REPORTED_NOT_YET_GCL_REPLAYED":
        raise ValueError("author report promoted")
    if set(report["axioms_reported"]) != {"propext","Classical.choice","Quot.sound"}:
        raise ValueError("author axiom report changed")
    local=d["gcl_reproduction"]
    if local["kernel_replay"] != "PENDING" or local["source_to_gcl_nat_adapter_replay"] != "PENDING":
        raise ValueError("unverified local proof promoted")
    if d["claim_boundaries"]["gcl_acceptance"] or d["claim_boundaries"]["mathcert_certification"]:
        raise ValueError("premature certification")
    return True

class TestExternalProofIntake(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.data=json.loads(P.read_text())
    def test_contract(self):self.assertTrue(validate(self.data))
    def reject(self, mutate, pattern):
        d=deepcopy(self.data);mutate(d)
        with self.assertRaisesRegex(ValueError,pattern):validate(d)
    def test_false_kernel_pass(self):
        self.reject(lambda d:d["gcl_reproduction"].update(kernel_replay="PASS"),"unverified local")
    def test_malicious_source_swap(self):
        self.reject(lambda d:d["exact_source"].update(gcl_revision="0"*40),"source revision")
    def test_quantifier_loss(self):
        self.reject(lambda d:d["external_repository"]["supply_contract"].update(quantifiers="∀ δ(x), ..."),"fixed-delta")
    def test_wrong_shift(self):
        self.reject(lambda d:d["external_repository"]["supply_contract"].update(prime_predicate="p smooth"),"shifted prime")
    def test_removed_package(self):
        self.reject(lambda d:d["external_repository"]["closed_package_graph"]["interfaces"].pop(),"package map")
    def test_fabricated_certification(self):
        self.reject(lambda d:d["claim_boundaries"].update(mathcert_certification=True),"premature certification")
    def test_author_report_promoted(self):
        self.reject(lambda d:d["external_author_report"].update(trusted_as="GCL_VERIFIED"),"author report")
    def test_wrong_axioms(self):
        self.reject(lambda d:d["external_author_report"]["axioms_reported"].append("sorryAx"),"author axiom")

if __name__ == "__main__":unittest.main()
