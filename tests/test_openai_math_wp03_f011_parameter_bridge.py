"""WP03/F011 fixed-delta parameter bridge: deterministic rational and hostile checks.

Tests mathematical parameter identities and documentary claim boundaries.
They do not verify the manuscript's prime-distribution assertion.
"""
from fractions import Fraction
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]/"sources"/"OPENAI-MATH-2026"
NOTE=ROOT/"WP03_FAMILY011_PRIME_SUPPLY_PARAMETER_BRIDGE.md"

def parameters(a):
    if not isinstance(a,int) or a<6:
        raise ValueError("a must be integer >= 6")
    delta=Fraction(2*a-1,2*a*(a-1))
    eta=Fraction(1,4*a)
    assert 0<delta<Fraction(1,4)
    assert a*delta==1+Fraction(1,2*(a-1))
    assert (a-1)*delta==1-2*eta
    assert (a-1)*delta<1-eta
    return delta,eta

def supply_choice(a,eps):
    if not (0<eps<=1 and a*eps>=4):
        raise ValueError("epsilon or a*epsilon out of range")
    return parameters(a)

def validate_note(s):
    for expression in ("(2a-1) / (2a(a-1))", "1/(4a)",
                       "aδ = 1 + 1/(2(a-1))",
                       "(a-1)δ = 1 - 1/(2a)",
                       "PrimeSupplyForExponent ε",
                       "fixed-\`δ\` prime-count",
                       "not independent proof"):
        if expression not in s:
            raise ValueError("missing exact proof or scope anchor: "+expression)
    if "**Claim boundary:** conditional deduction" not in s:
        raise ValueError("false unconditional promotion")
    return True

class TestF011Parameters(unittest.TestCase):
    def test_rational_identities(self):
        for a in (6,7,8,10,11,16,20,32,64,100,256,1000):
            parameters(a)

    def test_epsilon_cases(self):
        for eps in (Fraction(1),Fraction(1,2),Fraction(1,3),Fraction(1,10),Fraction(1,100)):
            a=max(6,(4*eps.denominator+eps.numerator-1)//eps.numerator)
            supply_choice(a,eps)

    def test_invalid_a(self):
        for a in (0,1,4,5):
            with self.assertRaises(ValueError):parameters(a)

    def test_false_parameter_threshold(self):
        with self.assertRaises(ValueError):supply_choice(6,Fraction(1,10))

    def test_count_exponent_gap(self):
        for a in (6,8,32,100):
            delta,eta=parameters(a)
            self.assertGreater(Fraction(1)-eta,(a-1)*delta)

    def test_documentary_boundary(self):
        self.assertTrue(validate_note(NOTE.read_text()))

    def test_hostile_missing_premise(self):
        with self.assertRaisesRegex(ValueError,"missing exact proof"):
            validate_note(NOTE.read_text().replace("PrimeSupplyForExponent ε","TRIVIAL"))

if __name__=="__main__":
    unittest.main()
