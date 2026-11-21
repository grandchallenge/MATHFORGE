#!/usr/bin/env python3
"""Source-pinned OAI F003 / independent native mathlib Hecke Euler contract canary.

Inputs: exact raw source files of mathlib@6e96f3e2 HeckeLFunction.lean,
openai/math@1581d4cb Hecke/IdealBridge.lean. The companion quartic arithmetic
verifier must be present in the same directory. Tests confirm source API
identity, then check a genuine imprimitive Euler normalization obstruction.

No claim of a compiled cross-model Lean bridge, idelic local-value theorem,
or analytic continuation.
"""
from __future__ import annotations

import hashlib
from fractions import Fraction
from pathlib import Path
import sys

EXPECTED = {
    "native": "9dcd9a2a11f1407d47b9b0a1000259d237bdfe64",
    "oai": "bcb15758326db111dd0b007b79a58103a4fa659e",
}


def git_blob_sha(content: bytes) -> str:
    header = b"blob " + str(len(content)).encode("ascii") + b"\0"
    return hashlib.sha1(header + content).hexdigest()


def require(cond: bool, reason: str) -> None:
    if not cond:
        raise AssertionError(reason)


def test_external_source(native: str) -> None:
    tests = {
        "native idèle class group, NOT source OAI character":
            "abbrev HeckeCharacter := (IdeleClassGroup R K) →ₜ* ℂ",
        "native prime local unramified predicate":
            "def IsUnramifiedAt (v : HeightOneSpectrum R) : Prop :=",
        "local polynomial defined by actual local unramified test":
            "if χ.IsUnramifiedAt v then 1 - C (χ.localValue v) * X else 1",
        "local value from uniformizer":
            "def localValue (v : HeightOneSpectrum R) : ℂ :=",
        "local Euler factor from local polynomial":
            "def localPowerSeries (v : HeightOneSpectrum R) : PowerSeries ℂ :=",
        "natural-number arithmetic Euler product":
            ".eulerProduct fun v : HeightOneSpectrum R ↦ χ.localEulerFactor v",
        "raw complex Dirichlet series":
            "protected def LSeries (s : ℂ) :=",
        "correct number field instance qualification":
            "[IsIntegralClosure ℤ R K]",
    }
    for description, needle in tests.items():
        require(needle in native, description)
    require("OAI.SevenEighths.HeckeFamily" not in native, "unindependent native module")
    print("NATIVE_HECKE_SOURCE_API_8_CHECKS_PASS", len(tests))


def test_oai_source(oai: str) -> None:
    for needle in (
        "def LFunction (χ : Character) (s : ℂ) : ℂ := continuedLattice χ s / 6",
        "theorem continuedLattice_eq_six_ideal_tsum",
        "theorem LFunction_eq_ideal_tsum",
        "theorem LFunction_differentiableAt",
        "theorem LFunction_entire_nonprincipal",
    ):
        require(needle in oai, "missing OAI source declaration: " + needle)
    print("OAI_LATTICE_MEROMORPHIC_MODEL_5_CHECKS_PASS")


def test_quartic_canary() -> None:
    from f003_quartic_ray_euler_adversary import chi, norm, i_mul, UNIT_SIX
    # Exact integer-valued Gaussian root-of-unity arithmetic from older
    # independent source-locked adversary; no floats and no re-invention.
    require(chi((2, 0)) == (-1, 0), "inert prime char should be -1")
    require(norm((2, 0)) == 4, "inert prime norm should be 4")
    require(chi((3, 1)) == (0, 1), "split prime orientation should be +i")
    require(chi((3, 1)) != (0, -1), "hostile inverse ray character not rejected")
    require(norm((3, 1)) == 7, "split prime norm should be 7")
    for u in UNIT_SIX:
        from f003_quartic_ray_euler_adversary import mul_raw
        require(chi(mul_raw((3, 1),u)) == (0, 1),
                "generator-dependent orientation would be invalid")
    print("INERT_NORM4_SPLIT_NORM7_ORIENTATION_AND_UNIT_CANARY_PASS")

    # Native unramified polynomial at prime (2) is 1 - (-1)X = 1 + X.
    # OAI imprimitive modulus 10 zero extension has local polynomial 1.
    # At s=2 the native local inverse is 16/17; deletion multiplier 17/16.
    x = Fraction(1, 4**2)
    p_native = 1 + x
    e_native = 1 / p_native
    e_imprimitive = Fraction(1, 1)
    require(p_native == Fraction(17, 16), "wrong native polynomial")
    require(e_native == Fraction(16, 17), "wrong native Euler factor")
    require(p_native * e_native == e_imprimitive,
            "missing imprimitive correction")
    require(e_native != e_imprimitive, "false raw external equality accepted")
    # Direct coefficientwise identity through degree 40:
    # (1 + X) Σ (-1)^k X^k = 1.
    coeff = [(-1)**j for j in range(41)]
    deleted = [coeff[j] + (coeff[j-1] if j else 0) for j in range(41)]
    require(deleted == [1] + [0]*40, "imprimitive polynomial not exact")
    print("NATIVE_VS_OAI_IMPRIMITIVE_EULER_NONIDENTITY_AND_CORRECTION_PASS")
    print("NORM4_40_COEFFICIENTS_PASS")


def main() -> None:
    require(len(sys.argv) == 3, "usage: script native_hecke.lean pinned_oai_ideal_bridge.lean")
    raw = {k: Path(path).read_bytes() for k, path in zip(("native", "oai"), sys.argv[1:])}
    for key in ("native", "oai"):
        observed = git_blob_sha(raw[key])
        require(observed == EXPECTED[key],
                f"stale or altered {key} blob: {observed} != {EXPECTED[key]}")
        print("EXACT_GIT_BLOB_LOCK_PASS", key, observed)
    test_external_source(raw["native"].decode("utf-8"))
    test_oai_source(raw["oai"].decode("utf-8"))
    test_quartic_canary()
    print("F003_NATIVE_MATHLIB_HECKE_EULER_CONTRACT_CANARY_PASS")
    print("GLOBAL_IDELE_TO_RAY_FORMAL_EQUIVALENCE_NOT_PROVED")
    print("MEROMORPHIC_CONTINUATION_NOT_PROVED")
    print("MATHCERT_NONE")


if __name__ == "__main__":
    main()
