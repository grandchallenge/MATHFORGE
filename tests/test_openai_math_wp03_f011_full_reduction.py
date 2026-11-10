"""Guard exact fixed-delta F011 reduction before separate Lean kernel replay.

These tests detect false formalization and source promotion; passing them alone
does not establish the Lean theorem.
"""
from pathlib import Path
import re
import unittest

PATH = Path(__file__).resolve().parents[1] / "sources" / "OPENAI-MATH-2026" / "WP03_FAMILY011_FULL_ASYMPTOTIC_REDUCTION.lean"

def validate(source: str):
    anchors = (
        "import OAI.NumberTheory.TotientFibers.FiniteFiber",
        "noncomputable def smoothPrimeSet",
        "Finset.Ioc (2 * x) (5 * x)",
        "q.Prime → q ∣ p - 1",
        "def SmoothPrimeCount : Prop",
        "∀ δ : ℝ, 0 < δ → δ < 1 / 4",
        "∀ η : ℝ, 0 < η",
        "∀ᶠ x : ℕ in atTop",
        "(x : ℝ) ^ (1 - η) ≤",
        "def PrimeSupplyForExponent (ε : ℝ) : Prop",
        "theorem prime_supply_of_smooth_count",
        "(hcount : SmoothPrimeCount)",
        "theorem infinite_fibers_of_smooth_count",
        "finite_large_fiber_rpow",
        "infinite_of_unbounded_g",
        "totient_large_fibers_of_one_le",
    )
    for item in anchors:
        if item not in source:
            raise ValueError("missing protected statement anchor " + item)
    for bad in (r"\bsorry\b", r"\badmit\b", r"(?m)^\s*axiom\b"):
        if re.search(bad, source):
            raise ValueError("unproved placeholder or fresh axiom")
    if "delta(x)" in source or "δ(x)" in source:
        raise ValueError("unlicensed variable delta")
    return True

class TestF011FullReductionSource(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = PATH.read_text()

    def test_source_has_no_placeholder_and_explicit_count(self):
        self.assertTrue(validate(self.source))

    def reject(self, changed, phrase):
        with self.assertRaisesRegex(ValueError, phrase):
            validate(changed)

    def test_reject_sorry(self):
        self.reject(self.source + "\nsorry\n", "unproved placeholder")

    def test_reject_new_axiom(self):
        self.reject(self.source + "\naxiom smooth_prime_count : True\n", "unproved placeholder")

    def test_reject_erased_count(self):
        self.reject(self.source.replace("(hcount : SmoothPrimeCount)", "(hcount : True)"), "missing protected")

    def test_reject_smoothness_loss(self):
        self.reject(self.source.replace("q.Prime → q ∣ p - 1", "q.Prime → q ∣ p"), "missing protected")

    def test_reject_corpus_range_mutation(self):
        self.reject(self.source.replace("Finset.Ioc (2 * x) (5 * x)", "Finset.Ioc x (5 * x)"), "missing protected")

    def test_reject_variable_delta(self):
        self.reject(self.source + "\n-- δ(x) allowed\n", "unlicensed variable delta")

if __name__ == "__main__":
    unittest.main()
