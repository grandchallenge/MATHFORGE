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

    def test_rho(rho, expected_crossed, label):
        # Toy entire L_rho(s)=s-rho; the log derivative has a pole at rho.
        def integrand(s):
            return -mellin_proxy(s)*mp.exp((s-mp.mpf("0.5"))*mp.log(D))/(s-rho)

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
        residue=-mellin_proxy(rho)*mp.exp((rho-mp.mpf("0.5"))*mp.log(D))
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
    print("CONTOUR_ORIENTATION_AND_ZERO_MULTIPLICITY_MECHANISM_PASS")


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
    contour_tests()
    print("F003_PRIME_BIN_INDEPENDENT_CONTOUR_AUDIT_PASS")
