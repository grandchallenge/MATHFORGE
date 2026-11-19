#!/usr/bin/env python3
"""OAI-26 F003 independent Eisenstein ideal-count / harmonic-mass adversary.

Exact integer lattice enumeration, quotient by six global units, Fraction
harmonic weights, dyadic shells. No OAI source, Lean, or Hecke package imports.

The paper proof covers ALL X>=1 and ALL finite ideal subsets; this program
is finite adversarial corroboration through MAX_NORM=16384 only.
Source: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
Target: Moments/MobiusHarmonicMass.full_mass_subpower, via
Moments/FirstDivisorSupport.supported_harmonic_mass.
"""
from fractions import Fraction
from math import isqrt

MAX_NORM=16384

def count_ideal_norms(mx):
    # For nonzero a+b*omega, N(a+b*omega)=a*a-a*b+b*b.
    # Six units act freely and preserve norm. Each nonzero principal
    # ideal has exactly six nonzero generators.
    bound=isqrt(2*mx)+1
    elements=[0]*(mx+1)
    for a in range(-bound,bound+1):
        for b in range(-bound,bound+1):
            if not (a or b):
                continue
            n=a*a-a*b+b*b
            if n<=mx:
                assert n>0
                elements[n]+=1
    assert all(v%6==0 for v in elements), "Global unit quotient invalid"
    return elements,[v//6 for v in elements]

def norm_count_checks(elements,ideals):
    expected={1:1,2:0,3:1,4:1,5:0,7:2,9:1,25:1,49:3}
    for n,wanted in expected.items():
        assert ideals[n]==wanted,(n,ideals[n],wanted)
    count=0
    max_over_x=(Fraction(0),0)
    for x in range(1,MAX_NORM+1):
        count+=ideals[x]
        assert 3*count<=8*x,(x,count)
        ratio=Fraction(count,x)
        if ratio>max_over_x[0]:
            max_over_x=(ratio,x)
    print("EXACT_IDEAL_COUNT_BY_NORM_PASS",MAX_NORM,
          "max_ratio="+str(max_over_x[0]),"at="+str(max_over_x[1]))
    assert elements[1]==6 and ideals[1]==1
    assert Fraction(elements[1],1)>Fraction(16,3)
    print("HOSTILE_OMIT_SIX_GLOBAL_UNIT_QUOTIENT_REJECTED")

def shell_checks(ideals):
    lower=1; shells=0; max_weight=Fraction(0)
    while lower<=MAX_NORM:
        upper=min(2*lower,MAX_NORM+1)
        terms=sum((Fraction(ideals[n],n) for n in range(lower,upper)), Fraction(0))
        assert terms<=Fraction(16,3),(lower,terms)
        if terms>max_weight:
            max_weight=terms
        shells+=1
        lower*=2
    print("EISENSTEIN_ALL_IDEAL_DYADIC_MASS_PASS",shells,
          "max_weight="+str(max_weight))
    for X in (1,3,7,25,100,1000,4096,MAX_NORM):
        # This dominates arbitrary finite subsets of ideals, even BEFORE
        # throwing out nonsquarefree terms with mu=0.
        lhs=sum((Fraction(ideals[n],n) for n in range(1,X+1)),Fraction(0))
        number_shells=X.bit_length()
        assert lhs<=Fraction(16*number_shells,3)
    print("MOBIUS_SELECTED_SUBSET_DOMINATED_BY_ALL_IDEALS_PASS",8)

def proof_constants():
    # Independent arithmetic behind universal proof:
    # Q(a,b)>= (a*a+b*b)/2.
    for a in range(-100,101):
        for b in range(-100,101):
            q=a*a-a*b+b*b
            assert 2*q>=a*a+b*b
    # For every real X>=1, 2 sqrt(2X)+1 <=4 sqrt(X)
    # follows from 2sqrt(2)+1<4; check 2sqrt2<3 by 8<9.
    assert 8<9
    # #nonzero ideals of norm <= X <=16X/6 = 8X/3.
    # A half-open dyadic shell [Y,2Y) contributes <=
    # (8/3)(2Y)/Y =16/3 to sum 1/N(I).
    assert Fraction(8,3)*2==Fraction(16,3)
    # The factor 16/3 is not asserted best possible.
    print("GENERAL_LATTICE_INEQUALITY_AND_EXPLICIT_SHELL_CONSTANT_PASS")

if __name__=="__main__":
    proof_constants()
    elements,ideals=count_ideal_norms(MAX_NORM)
    norm_count_checks(elements,ideals)
    shell_checks(ideals)
    print("F003_EISENSTEIN_IDEAL_HARMONIC_MASS_INDEPENDENT_AUDIT_PASS")
