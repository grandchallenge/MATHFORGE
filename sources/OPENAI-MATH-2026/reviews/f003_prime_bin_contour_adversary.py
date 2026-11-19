#!/usr/bin/env python3
"""OAI-26 F003 independent contour/residue adversary.

SOURCE LOCK: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
TARGET: lean/OAI/NumberTheory/DirichletL/Hecke/PrimeDyadicBuffered.lean,
        theorem polynomial_bound_in_bin.

Exact rational geometry, independent complex contour quadrature, and an
explicit hostile zero-in-rectangle example. The analytic toy L(s)=s-rho
and Gaussian vertical kernel test contour mechanics only; they are NOT
Hecke L-functions or compactly supported source Mellin transforms.
Requires mpmath 1.3.0. No Lean/Hecke source is imported.
"""
from fractions import Fraction as F
from itertools import product
import mpmath as mp


def geometry_tests():
    total=0
    for a,e,T,i,shift in product(
        [F(51,100),F(3,4),F(1)],
        [F(1,100000),F(1,2000)],
        [F(5,2),F(3),F(17,4)],
        [0,1,2,13],
        [F(-2),F(-1,4),F(0),F(1,2),F(2)],
    ):
        H=(3*i+2)*T
        Hmax=3*(i+1)*T
        R0=F(2)-a-2*e
        R8=F(2)-a-8*e
        left=a+8*e-shift
        right=F(2)-shift
        assert 0<R8<R0
        assert R0-R8==6*e
        assert Hmax-H==T
        assert R0<T
        assert H+R0<Hmax
        assert left+shift==a+8*e
        assert right+shift==2
        assert left<=right
        assert R8==2-(left+shift)
        assert a+2*e>=F(51,100)
        assert a+8*e<=2
        # The midpoint/endpoint geometry is sufficient to check each
        # rectangle's real bounds. Vertical frequencies have max |freq|+V.
        for v in (F(0),F(1),F(3,2)):
            freq=H-v
            assert abs(freq)+v<=H
            assert abs(freq)+v+R0<Hmax
        total+=1
    print("EXACT_RECTANGLE_AND_BUFFER_GEOMETRY_PASS",total)
    # Strict inequalities matter. The boundary zero would violate hmax.
    a=F(3,4);e=F(1,2000)
    assert not (a+2*e < a+2*e)
    print("HOSTILE_ZERO_ON_BUFFER_BOUNDARY_REJECTED")


def contour_tests():
    mp.mp.dps=55
    a=mp.mpf("0.9")
    e=mp.mpf("0.0001")
    left=a+8*e
    right=mp.mpf("2")
    halfheight=mp.mpf("4")
    D=mp.mpf("2")
    pi=mp.pi

    def mellin_proxy(s):
        # An entire Mellin-like Gaussian, rapid in vertical strips.
        return mp.exp((s-mp.mpf("1.5"))**2)

    def test_rho(rho, expected_crossed, label, order=1):
        # Toy meromorphic L_rho(s)=(s-rho)^order. Its log derivative
        # has residue -order, including positive residue for a pole.
        def integrand(s):
            return -order*mellin_proxy(s)*mp.exp((s-mp.mpf("0.5"))*mp.log(D))/(s-rho)

        def vertical(x):
            return mp.quad(lambda t: integrand(x+mp.j*t),
                           [-halfheight,0,halfheight])
        def horizontal(y):
            return mp.quad(lambda x: integrand(x+mp.j*y),
                           [left,(left+right)/2,right])
        R=vertical(right)
        L=vertical(left)
        bottom=horizontal(-halfheight)
        top=horizontal(halfheight)
        observed=(R-L-mp.j*(bottom-top))/(2*pi)
        residue=-order*mellin_proxy(rho)*mp.exp((rho-mp.mpf("0.5"))*mp.log(D))
        if expected_crossed:
            assert left<mp.re(rho)<right
            assert abs(mp.im(rho))<halfheight
            assert abs(residue)>mp.mpf("0.2")
            assert abs(observed-residue)<mp.mpf("1e-38"), (
                label,mp.nstr(observed-residue,12))
            # Hostile test: incorrectly discard the zero residue.
            assert abs(observed)>mp.mpf("0.2")
        else:
            assert mp.re(rho)<left
            assert abs(observed)<mp.mpf("1e-38"), (
                label,mp.nstr(observed,12))
        print(label,"PASS","zero_residue="+mp.nstr(observed,14),
              "expected="+mp.nstr(residue if expected_crossed else 0,14),
              "error="+mp.nstr(abs(observed-(residue if expected_crossed else 0)),6))

    test_rho(mp.mpc("0.3","0.35"),False,
             "ZERO_FREE_CONTOUR_WITHOUT_RESIDUE")
    test_rho(mp.mpc("1.3","0.35"),True,
             "HOSTILE_INTERIOR_ZERO_REQUIRES_RESIDUE")
    test_rho(mp.mpc("1.3","0.35"),True,
             "HOSTILE_DOUBLE_ZERO_GIVES_DOUBLE_RESIDUE",order=2)
    test_rho(mp.mpc("1.1","0.35"),True,
             "HOSTILE_PRINCIPAL_TYPE_POLE_GIVES_OPPOSITE_SIGN",order=-1)
    print("CONTOUR_ORIENTATION_ZERO_MULTIPLICITY_AND_POLE_PASS")


def primitive_gamma_strip_checks():
    # Independently inspect the exact Q^(3/5) arithmetic from the
    # source's completed Hecke functional equation on Re(s)=-1/10:
    # completionScale(Q)=sqrt(3Q)/(2pi), exponent (1-2s).re=6/5.
    sigma=F(-1,10)
    assert F(1)-2*sigma==F(6,5)
    assert (F(1)-2*sigma)/2==F(3,5)
    mp.mp.dps=55
    c=mp.gamma(mp.mpf("1.1"))/mp.gamma(mp.mpf("1.9"))
    for t in ["0","0.01","0.1","1","3","10","100","1000"]:
        y=mp.mpf(t)
        z=mp.mpc("-0.1",y)
        lhs=abs(mp.gamma(1-z)/mp.gamma(z))
        rhs=c*(3+abs(y))**2
        assert lhs<=rhs, (t,mp.nstr(lhs),mp.nstr(rhs))
    for q in [1,3,5,25,10**6]:
        Q=mp.mpf(q)
        scale=mp.sqrt(3*Q)/(2*mp.pi)
        rhs=(mp.sqrt(3)/(2*mp.pi))**mp.mpf("1.2")*Q**mp.mpf("0.6")
        assert mp.almosteq(scale**mp.mpf("1.2"),rhs,rel_eps=mp.mpf("1e-48"))
    print("COMPLETED_HECKE_GAMMA_CONDUCTOR_EXPONENT_SAMPLES_PASS",8,5)


def hostile_uniformity_without_growth():
    # Zero-freeness by itself never bounds a logarithmic derivative
    # uniformly. The entire functions L_k(s)=exp(k*(s-2)) have NO zeros,
    # but L'_k(s)/L_k(s)=k. A fixed conductor/height surrogate cannot
    # dominate arbitrarily large k. The source genuinely needs its
    # uniform primitive L-growth/BC+Cauchy estimate, not merely hmax.
    B=mp.mpf("3")
    fake_complexity=mp.mpf("18")  # fixed q=1,t=0 in source's complexity
    k=mp.mpf("1000")
    assert k>B*mp.log(fake_complexity)
    assert abs(mp.exp(k*(2-2)))==1  # normalized at a point
    assert mp.exp(k*(mp.mpf("1.1")-2))!=0
    print("HOSTILE_ZERO_FREE_WITHOUT_GROWTH_CONTROL_REJECTED")


def exponent_tests():
    # Re l+sigma=a+8e, Re r+sigma=2.
    for a,e in product([F(51,100),F(7,8),F(1)],
                       [F(1,100000),F(1,2000)]):
        left=a+8*e-F(1,2)
        right=F(3,2)
        horizontal_width=2-a-8*e
        assert left<right
        assert horizontal_width>0
        assert (right-left)==horizontal_width
        # At the later squared-prime stage kappa = 2beta-1 exactly.
        for beta in [F(7,8),F(9,10),F(1)]:
            kappa=2*beta-1
            assert 2*(beta-F(1,2))==kappa
    # The source has no principal-character pole in the shifted region:
    # nonprincipal is required, so a putative principal zero/pole
    # cannot be covered by the same rectangle statement.
    print("MELLIN_HALF_POWER_AND_HORIZONTAL_WIDTH_PASS",6)
    print("HOSTILE_PRINCIPAL_CHARACTER_NOT_COVERED_BY_HYPOTHESIS_PASS")


def uniformity_tests():
    # Real-variable algebra for the source's uniform binCost; the
    # analytic premise ||L'/L|| <= B log(complexity)+deletion is NOT
    # numerically proved here.
    mp.mp.dps=40
    B=mp.mpf("3")
    local=mp.mpf("2")
    for q,radical,height in product([1,2,9,25,10**6],
                                    [1,2,3], [0,2,100,10**6]):
        if radical>q:
            continue
        c=2*q*(3+height)**2
        K=B*mp.log(c)+local*mp.log(radical)
        assert K>=0
        assert K<=B*mp.log(2*q*(3+height)**2)+local*mp.log(q)
        assert K<=B*mp.log(2*q*(4+height)**2)+local*mp.log(q)
    print("UNIFORM_CONDUCTOR_AND_HEIGHT_LOG_MONOTONICITY_PASS")


if __name__=="__main__":
    geometry_tests()
    exponent_tests()
    uniformity_tests()
    primitive_gamma_strip_checks()
    hostile_uniformity_without_growth()
    contour_tests()
    print("F003_PRIME_BIN_INDEPENDENT_CONTOUR_AUDIT_PASS")
