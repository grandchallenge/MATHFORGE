#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT_COMMIT = "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6"
ROOT_TREE = "174289e4d4958cb0509874e6e53400e098213de7"
PERMITTED_AXIOMS = ["propext", "Quot.sound", "Classical.choice"]

FAMILIES = {
    "OTP-A-SPHERE-PACKING": {
        "config": ("ComparatorChallenges/A_SpherePacking.json", "46b2e7b49da43fb17a7efa88652f8ee1adc01cbe"),
        "challenge": ("ComparatorChallenges/A_SpherePacking.lean", "2477846e1883534837340c636fd928b091509783"),
        "solution": ("SpherePacking.lean", "e6117934a80142a8249356fdafa797eba030e920"),
        "challenge_module": "ComparatorChallenges.A_SpherePacking",
        "solution_module": "SpherePacking",
        "theorems": ["PackingBounds.FullMain.exact_limit", "PackingBounds.FullMain.exact_binary_exponent", "PackingBounds.PackingBridge.sphere_packing_sharp_asymptotic_upper", "PackingBounds.sharpFullCohnElkiesManuscriptConclusions"],
        "definitions": [],
    },
    "OTP-B1-BINARY-CODES": {
        "config": ("ComparatorChallenges/B_BinaryCodes.json", "b530b77972c83396c1f2aed2deccda3a12fb6cab"),
        "challenge": ("ComparatorChallenges/B_BinaryCodes.lean", "c9e93b1944e6806802068cf593fa6557e4267bb1"),
        "solution": ("MetricCodes.lean", "51628c0db81bd6cb9a79777fa601306c9d64cbc5"),
        "challenge_module": "ComparatorChallenges.B_BinaryCodes",
        "solution_module": "MetricCodes",
        "theorems": ["MetricCodes.Hamming.binaryRate_lt_classicalRate", "MetricCodes.Hamming.exists_binaryRate_improvement", "MetricCodes.Johnson.binaryRate_le_combinedVariationalRate", "MetricCodes.MRRW.strict_mrrw2", "MetricCodes.Johnson.binaryRate_lt_mrrw", "MetricCodes.Johnson.exists_binaryRate_mrrw_improvement"],
        "definitions": [],
    },
    "OTP-B2-SPHERICAL-CODES": {
        "config": ("ComparatorChallenges/B_SphericalCodes.json", "b343dca9c0373f80c6304f30f261b81b371661c3"),
        "challenge": ("ComparatorChallenges/B_SphericalCodes.lean", "5f2bcda432b7091097ae8753cac24c08d0c10f6c"),
        "solution": ("MetricCodes.lean", "51628c0db81bd6cb9a79777fa601306c9d64cbc5"),
        "challenge_module": "ComparatorChallenges.B_SphericalCodes",
        "solution_module": "MetricCodes",
        "theorems": ["MetricCodes.Johnson.main_binary_theorem", "MetricCodes.Spherical.HigherHierarchy.main_general", "MetricCodes.Spherical.HigherHierarchy.strict_hierarchy", "MetricCodes.Spherical.HigherHierarchy.NumericalMaximum.eventually_kissingNumber_lt_published"],
        "definitions": [],
    },
    "OTP-D-NON-SOFIC": {
        "config": ("ComparatorChallenges/D_NonSoficGroup.json", "af023106a83552d7fafb4f0d122f121a095f802c"),
        "challenge": ("ComparatorChallenges/D_NonSoficGroup.lean", "158d97224fbd51c203ff07a2f74041ffa2c6013b"),
        "solution": ("NonSoficGroup.lean", "dd1f8e63960300c8674fcd491007d2a628fbc6fe"),
        "challenge_module": "ComparatorChallenges.D_NonSoficGroup",
        "solution_module": "NonSoficGroup",
        "theorems": ["SoficGroups.SourceTopLevelCompressionFinal.exists_finitelyPresented_nonsofic_group"],
        "definitions": [],
    },
    "OTP-E-CONNES-RIGIDITY": {
        "config": ("ComparatorChallenges/E_ConnesRigidity.json", "f5d2964be6b1a154bc12b38a0f99f0960960a2d9"),
        "challenge": ("ComparatorChallenges/E_ConnesRigidity.lean", "9425edabd79319cbe2943888c6ece107bdd81dfb"),
        "solution": ("ConnesRigidity.lean", "81cf03e3f7ccdc66815cc00c9969bcfd2341c8d6"),
        "challenge_module": "ComparatorChallenges.E_ConnesRigidity",
        "solution_module": "ConnesRigidity",
        "theorems": ["ConnesRigidity.exists_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors", "ConnesRigidity.exists_infinite_pairwise_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors"],
        "definitions": [],
    },
    "OTP-G-QUANTUM-PARALLEL-REPETITION": {
        "config": ("ComparatorChallenges/G_QuantumParallelRepetition.json", "c7dd59e9df9ae5d90b35f76a9d958943d8e94770"),
        "challenge": ("ComparatorChallenges/G_QuantumParallelRepetition.lean", "8257e7726643a8f8c08c7e91584e003ab204c589"),
        "solution": ("QuantumParallelRepetition.lean", "887c4378f124a5d81a3f2624b6dc34867ec409c4"),
        "challenge_module": "ComparatorChallenges.G_QuantumParallelRepetition",
        "solution_module": "QuantumParallelRepetition",
        "theorems": ["QuantumParallelRepetition.distributionUniformExponential", "QuantumParallelRepetition.standardQuantumParallelRepetition"],
        "definitions": [],
    },
    "OTP-H-GAPCVP": {
        "config": ("ComparatorChallenges/H_GapCVP.json", "fdba0e774acc6c2bd6fd450ee155975c0eda1833"),
        "challenge": ("ComparatorChallenges/H_GapCVP.lean", "770e202350a5c94d3f6516428ff01092cb8f8cb4"),
        "solution": ("GapCVP.lean", "47f3a395e4d9ec3e2892664860f26ed63421b0c9"),
        "challenge_module": "ComparatorChallenges.H_GapCVP",
        "solution_module": "GapCVP",
        "theorems": ["GapCVP.Comparator.gapCVP400IsNPHard", "GapCVP.Comparator.binaryNearestCodewordIsNPHard", "GapCVP.Comparator.binarySyndromeDecodingIsNPHard", "GapCVP.Comparator.finitePNormGapCVPIsNPHard"],
        "definitions": ["GapCVP.Comparator.gapCVP400Promise", "GapCVP.Comparator.binaryNearestCodewordPromise", "GapCVP.Comparator.binarySyndromeDecodingPromise", "GapCVP.Comparator.finitePGapCVPPromise"],
    },
    "OTP-I-RAMSEY": {
        "config": ("ComparatorChallenges/I_MulticolorTriangleRamsey.json", "ce67db0653e18a2de68f471c00b9f892b789f806"),
        "challenge": ("ComparatorChallenges/I_MulticolorTriangleRamsey.lean", "6a9e42d686720f4b74ddc2001006b0b7a20f11aa"),
        "solution": ("MulticolorTriangleRamsey.lean", "24b55f531a4d36347cd2277b1b9c7d784d91ae35"),
        "challenge_module": "ComparatorChallenges.I_MulticolorTriangleRamsey",
        "solution_module": "MulticolorTriangleRamsey",
        "theorems": ["ErdosProblems.MulticolourTriangleRamsey.erdos_183", "ErdosProblems.MulticolourTriangleRamsey.erdos_problem_183_explicit", "ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_sharp_coefficients", "ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_isTheta"],
        "definitions": [],
    },
}


def git_output(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def verify(root: Path, family_id: str) -> int:
    expected = FAMILIES[family_id]
    errors: list[str] = []
    if git_output(root, "rev-parse", "HEAD") != ROOT_COMMIT:
        errors.append("upstream root drift")
    if git_output(root, "rev-parse", "HEAD^{tree}") != ROOT_TREE:
        errors.append("upstream tree drift")

    for field in ("config", "challenge", "solution"):
        rel, blob = expected[field]
        path = root / rel
        if not path.is_file():
            errors.append(f"missing {field}: {rel}")
        elif git_blob_sha1(path) != blob:
            errors.append(f"{family_id}: {field} blob drift")

    config_path = root / expected["config"][0]
    if config_path.is_file():
        cfg = json.loads(config_path.read_text(encoding="utf-8"))
        if cfg.get("challenge_module") != expected["challenge_module"]:
            errors.append("challenge module drift")
        if cfg.get("solution_module") != expected["solution_module"]:
            errors.append("solution module drift")
        if cfg.get("theorem_names") != expected["theorems"]:
            errors.append("theorem target drift")
        if cfg.get("definition_names", []) != expected["definitions"]:
            errors.append("definition target drift")
        if cfg.get("permitted_axioms") != PERMITTED_AXIOMS:
            errors.append("permitted axiom drift")
        if cfg.get("enable_nanoda") is not True:
            errors.append("Nanoda must remain enabled")

    solution_text = (root / expected["solution"][0]).read_text(encoding="utf-8")
    challenge_text = (root / expected["challenge"][0]).read_text(encoding="utf-8")
    solution_placeholders = list(re.finditer(r"\b(?:sorry|admit)\b", solution_text))
    solution_axioms = list(re.finditer(r"(?m)^\s*axiom\s+", solution_text))
    solution_unsafe = list(re.finditer(r"(?m)^\s*unsafe\s+(?:def|theorem)\s+", solution_text))
    challenge_placeholders = list(re.finditer(r"\b(?:sorry|admit)\b", challenge_text))
    challenge_axioms = list(re.finditer(r"(?m)^\s*axiom\s+", challenge_text))
    challenge_unsafe = list(re.finditer(r"(?m)^\s*unsafe\s+(?:def|theorem)\s+", challenge_text))
    print(f"OTP_SUCCESSOR_SCAN_FAMILY={family_id}")
    print(f"OTP_SUCCESSOR_SOLUTION_PLACEHOLDER_COUNT={len(solution_placeholders)}")
    print(f"OTP_SUCCESSOR_SOLUTION_CUSTOM_AXIOM_DECL_COUNT={len(solution_axioms)}")
    print(f"OTP_SUCCESSOR_SOLUTION_UNSAFE_DECL_COUNT={len(solution_unsafe)}")
    print(f"OTP_SUCCESSOR_CHALLENGE_PLACEHOLDER_COUNT={len(challenge_placeholders)}")
    print(f"OTP_SUCCESSOR_CHALLENGE_CUSTOM_AXIOM_DECL_COUNT={len(challenge_axioms)}")
    print(f"OTP_SUCCESSOR_CHALLENGE_UNSAFE_DECL_COUNT={len(challenge_unsafe)}")
    if solution_placeholders:
        errors.append("solution source contains sorry/admit placeholder")
    if solution_axioms:
        errors.append("solution source contains a direct custom axiom declaration")

    if family_id == "OTP-H-GAPCVP":
        required_def_fragments = [
            "def gapCVP400Promise : PromiseProblem where",
            "def binaryNearestCodewordPromise : PromiseProblem where",
            "def binarySyndromeDecodingPromise : PromiseProblem where",
            "def finitePGapCVPPromise (p : ℚ) (hp : 1 ≤ p) : PromiseProblem where",
        ]
        for fragment in required_def_fragments:
            if fragment not in challenge_text:
                errors.append(f"GapCVP current-root structural definition missing: {fragment}")
        if challenge_text.count("disjoint := by sorry") < 4:
            errors.append("GapCVP challenge no longer exposes the expected unresolved disjointness placeholders")
        print("OTP_SUCCESSOR_GAPCVP_STRUCTURAL_INTERFACES=EXPLICIT_BODIES_WITH_OPEN_CHALLENGE_PLACEHOLDERS")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("OTP_SUCCESSOR_UPSTREAM_AUDIT=PASS")
    return 0


def write_axiom_audit(root: Path, family_id: str, output: Path) -> int:
    expected = FAMILIES[family_id]
    lines = [f"import {expected['solution_module']}", ""]
    for theorem in expected["theorems"]:
        lines.append(f"#print axioms {theorem}")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OTP_SUCCESSOR_AXIOM_AUDIT_FILE={output}")
    return 0


def check_axiom_log(family_id: str, log_path: Path) -> int:
    text = log_path.read_text(encoding="utf-8", errors="replace")
    expected_count = len(FAMILIES[family_id]["theorems"])
    if "sorryAx" in text:
        print("ERROR: target axiom report contains sorryAx", file=sys.stderr)
        return 1
    matches = re.findall(r"depends on axioms:\s*\[([^\]]*)\]", text, flags=re.MULTILINE)
    if len(matches) != expected_count:
        print(f"ERROR: expected {expected_count} theorem axiom reports, found {len(matches)}", file=sys.stderr)
        return 1
    allowed = set(PERMITTED_AXIOMS)
    for raw in matches:
        found = {item.strip() for item in raw.split(",") if item.strip()}
        unexpected = found - allowed
        if unexpected:
            print(f"ERROR: unexpected target axioms: {sorted(unexpected)}", file=sys.stderr)
            return 1
    print(f"OTP_SUCCESSOR_AXIOM_REPORTS=PASS_{expected_count}_OF_{expected_count}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    verify_parser = sub.add_parser("verify")
    verify_parser.add_argument("--root", type=Path, required=True)
    verify_parser.add_argument("--family", choices=sorted(FAMILIES), required=True)

    write_parser = sub.add_parser("write-axiom-audit")
    write_parser.add_argument("--root", type=Path, required=True)
    write_parser.add_argument("--family", choices=sorted(FAMILIES), required=True)
    write_parser.add_argument("--output", type=Path, required=True)

    check_parser = sub.add_parser("check-axiom-log")
    check_parser.add_argument("--family", choices=sorted(FAMILIES), required=True)
    check_parser.add_argument("--log", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "verify":
        return verify(args.root, args.family)
    if args.command == "write-axiom-audit":
        return write_axiom_audit(args.root, args.family, args.output)
    return check_axiom_log(args.family, args.log)


if __name__ == "__main__":
    raise SystemExit(main())
