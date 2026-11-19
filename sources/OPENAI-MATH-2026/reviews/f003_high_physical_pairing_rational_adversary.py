#!/usr/bin/env python3
"""Source-independent exact-rational adversary for OAI-26 F003 high physical pairing.

Pinned source: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
Targets: FirstReferenceEnergy.pairedBudget/sourceFactor,
 FirstPhysicalNormalization.pairedBudget_le_cap/physical_power_identity,
 CanonicalHighPhysical.actual_high_physical,
 CappedAnalyticSuccessor.actual_successor / WidthSchedule.
Validates the source's *algebraic interfaces*, not its analytic
main/error source-column estimates or the seven-eighths theorem.
Standard library only. All mathematical quantities are Fraction.
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt

def paired_terms():
    # Four left by four right nonnegative contributions. The actual
    # windowBudget also contains nonnegative common height/profile factors.
    choices=(0,1,4,9)
    H=Q(9)
    cases=0
    for e in product(choices, repeat=8):
        el=e[:4]; er=e[4:]
        S=sum(isqrt(v) for v in el)*sum(isqrt(v) for v in er)
        assert S<=16*H
        cases+=1
    assert cases==65_536
    assert sum(isqrt(9) for _ in range(4))**2==16*H
    assert 16*H>15*H
    print("FOUR_BY_FOUR_SQRT_PAIRING_SHARP_16_PASS",cases)
    print("HOSTILE_REPLACING_16_BY_15_REJECTED")

def conductor_and_loss():
    cases=0
    Z=Q(2)
    for m,ell,k,q,p,low,amplitude in product(
       (0,1,6,15),(-3,0,2),(0,1,3),(0,1,3),
       (Q(1,5),Q(2),Q(7)),(Q(1,5),Q(1,10)),(Q(1),Q(3))
    ):
        if p<low: continue
        K=Z**k
        n=Z**q
        # Source's normalization before slot-height factors:
        # sourceFactor = 4*fixedPresentationCost*K*n/p.
        source=Q(4)*amplitude*K*n/p
        source_exponent=m-k-q+ell
        # This is exactly K n Z^(m-log_Z(K)-log_Z(n)+ell).
        assert K*n*(Z**source_exponent)==Z**(m+ell)
        # Paired budget <= 16 * F * Z^source_exponent.
        F=Q(3,2)
        bound_left=source*Q(16)*F*(Z**source_exponent)
        bound_right=(Q(16)*Q(4)*amplitude/low)*F*Z**(m+ell)
        assert bound_left<=bound_right
        if p==low:
            assert bound_left==bound_right
        cases+=1
    assert cases>100
    print("CONDUCTOR_K_NORM_EXACT_CANCELLATION_PASS",cases)
    print("SOURCE_SUPPORT_LOWER_BOUND_AND_LOSS_MONOTONICITY_PASS")

def two_sided_height_and_constant():
    cases=0
    for JL,JR,h,t,CL,CR,PL,PR in product(
        (0,1,3), (0,2,4), (Q(0),Q(2,3),Q(4)),
        (Q(0),Q(3,4),Q(2)), (Q(1,3),Q(10)),
        (Q(1),Q(17)), (Q(1),Q(4)), (Q(1,2),Q(9))
    ):
        ctrl=max(PL,PR)
        C0=Q(2);C1=Q(5)
        FL=CL*(C0+C1+1)*PL**2*(1+h)**JL
        FR=CR*(C0+C1+1)*PR**2*(1+h)**JR
        Fcap=(CL+CR)*(C0+C1+1)*ctrl**2*(1+h)**(JL+JR)
        assert FL<=Fcap and FR<=Fcap
        assert (1+h)**(JL+JR)*(1+t)**(JL+JR) <= (1+t+h)**(2*(JL+JR))
        # Uniform physical constant is permitted to depend on
        # characteristic constants CL,CR selected after η,Q.
        Cp=Q(13,4)
        PLmom=Q(2);PRmom=Q(3)
        Cmass=Q(5)
        Cm=Cmass*(CL+CR)*(1+PLmom)*(1+PRmom)
        assert Cp*(CL+CR)*PLmom*PRmom<=Cm
        cases+=1
    print("TWO_COLUMN_COMMON_ENVELOPE_AND_HEIGHT_EXPONENT_PASS",cases)
    # source loss gate has powers[j]+base <= ell, so Z>1 permits
    # bounding all four column terms by a common Z^ell.
    for Z in (Q(2),Q(5)):
        for powers in [(-4,-2,0,1),(1,2,3,4)]:
            base=Q(3)
            ell=base+max(powers)
            assert all(Z**(base+p)<=Z**ell for p in powers)
            assert not (Z**(ell-1)>Z**ell)
    print("FOUR_POWER_EXPONENT_BUDGET_PASS")

def last_stage_plateau():
    def ceilq(x):
        return -((-x.numerator)//x.denominator)
    def band(m,a,reserve,k):
        return min(m,reserve/Q(16)+Q(k)*a/2)
    t=Q(1,100_000_000)
    epsilon=t/4
    a=epsilon/16000
    assert a==t/64000
    m=Q(2)
    n=ceilq(2*m/a)+1
    assert n==25_600_000_000_001
    # Any actual reserve obeys 0<r<=a/100.
    for reserve in (a/1_000_000,a/200,a/100):
        assert band(m,a,reserve,n-2)<m
        assert band(m,a,reserve,n-1)==m
        assert band(m,a,reserve,n)==m
        assert band(m,a,reserve,n)-a/2<=band(m,a,reserve,n-1)
    # Generic parameter/remainder adversaries.
    cases=0
    for m,a in product((Q(1,7),Q(2),Q(7,5),Q(10)),
                       (Q(1,100),Q(1,3),Q(2,5),Q(3,4))):
        n=ceilq(2*m/a)+1
        r=a/200
        for k in range(n):
            parent=band(m,a,r,k+1)
            child=band(m,a,r,k)
            assert parent-a/2<=child
            assert parent>=child
            cases+=1
    print("INDUCTION_PREDECESSOR_STAGE_NOT_STRICT_WIDTH_GAIN_PASS",cases)
    print("LAST_TWO_WIDTHS_EQUAL_MCAP_AT_25600000000000_AND_25600000000001_PASS")
    print("HOSTILE_STRICT_WIDTH_GROWTH_AT_LAST_STEP_REJECTED")

if __name__=="__main__":
    paired_terms()
    conductor_and_loss()
    two_sided_height_and_constant()
    last_stage_plateau()
    print("F003_HIGH_PHYSICAL_PAIRING_AND_INDUCTION_AUDIT_PASS")
