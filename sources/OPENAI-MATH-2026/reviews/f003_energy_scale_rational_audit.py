#!/usr/bin/env python3
"""GCL OAI-26 F003 exact-rational audit of source-locked energy scales.

This independently recalculates the algebra of:
  ParametersHighData.lean: t <= 1/10^8; ell_j <= t/200; sum ell = 1/6
  DetectorPlainMomentParameters.lean: stageError = t/4, kappaPlain = 3/4+2Δ
  Moments/FirstSecondLossParameters.lean: depth(M,a) = ceil(2M/a)+1
  Energy/WidthSchedule.lean: amplification, count, reserve, width, loss
  ParametersHighData.lean: height choice τ <= t/(4(J+7))
  Detector/FinalAssemblyMomentInput.lean: 2τ(1+J) <= t
No external dependencies and no claim to replay full higher-order moment bounds.
All calculations use Fraction and integers; no floating point.
"""
from fractions import Fraction as F

TMAX=F(1,100_000_000)
M=F(2)
B=F(0)

def ceil_f(a):
    return -((-a.numerator)//a.denominator)

def cap_min(a,b):
    return a if a<=b else b

def amplification(eps):
    return cap_min(F(1),eps/16000)

def depth(m,a):
    return ceil_f(2*m/a)+1

def schedule(m,b,eps):
    a=amplification(eps)
    k=depth(m,a)
    scale=F(k)+m+10*b+30
    r=cap_min(a/100,eps/(1_000_000*scale))
    mesh=r/(F(3,4)+1)
    width=r/16+F(k)*a/2
    loss=r+64*F(k)*r
    return dict(a=a,k=k,scale=scale,r=r,mesh=mesh,width=width,loss=loss)

def basic_bounds():
    # The slot lower bound is true for every actual HighData, not a witness
    # construction. At the optimistic maximum allowed t it is minimized.
    n_min=ceil_f(F(1,6)/(TMAX/200))
    assert n_min==3_333_333_334
    assert F(n_min)*TMAX/200>=F(1,6)
    assert F(n_min-1)*TMAX/200<F(1,6)
    # Source: at final detector parameters Mcap=2, epsilon=t/4.
    eps=TMAX/4
    out=schedule(M,B,eps)
    assert out["a"] == TMAX/64000
    assert out["k"] == 25_600_000_000_001
    assert out["width"] > M
    assert out["loss"] <= eps/1000
    assert out["r"] <= out["a"]/100
    assert out["r"] <= eps/(1_000_000*out["scale"])
    assert 20*out["r"] <= out["a"]/2
    # Number of subsets of the Fin N slots is 2^N.
    # Since 2^10 > 10^3, this requires at least 0.3N decimal digits;
    # do not materialize this fantastically large integer.
    digits_lower=(3*n_min)//10+1
    assert digits_lower >= 1_000_000_001
    print("SLOT_COUNT_LOWER_BOUND_PASS",n_min)
    print("SYMBOLIC_INDUCTION_DEPTH_LOWER_BOUND_PASS",out["k"])
    print("SUBSET_ENUMERATION_DECIMAL_DIGITS_LOWER_BOUND_PASS",digits_lower)
    print("FINAL_WIDTH_COVERS_CAP_PASS")
    print("FINAL_STAGE_LOSS_WITHIN_EPS_OVER_1000_PASS")
    print("STAGE_WIDTH_MIN_BOUND_AND_LOSS_BUDGET_PASS")
    # Important: the calculations are lower bounds for every valid HighData
    # at t<=tmax, not construction of an actual HighData witness.
    return n_min,out

def all_positive_height_budgets():
    # Source HighData.height_choice selects tau <= t/(4*(J+7)).
    # These finite rational witnesses test algebraic absorption. The
    # general proof is 2tau(1+J)<= t*(1+J)/(2(J+7)) < t.
    for j in (0,1,5,100,1_000_000,10**20):
        J=F(j)
        t=TMAX
        cost=F(1,10**12)
        eps=F(1,10**15)
        tau=cap_min(F(1,200)*cost/16,
                    cap_min(F(1,800),t/(4*(J+7))))
        assert tau>0
        assert 2*tau*(1+J)<=t
        assert tau*(2+4*eps)<t
        assert 4*tau<F(1,200)*cost
        assert tau<t
    print("HEIGHT_POLYNOMIAL_ABSORPTION_EXACT_FRACTION_PASS",6)
    # Hostile choice tau=t would NOT absorb arbitrary height polynomial
    # degrees; this shows why the source quantifier choice is necessary.
    assert 2*TMAX*(1+F(1))>TMAX
    print("HOSTILE_UNSCALED_HEIGHT_CHOICE_REJECTED")

def beta_kappa_saturation():
    # source: Δ=β-7/8, κ_plain=3/4+2Δ.
    # 2β-1 is identical, so the high-stage κ bound is saturated exactly.
    for beta in (F(7,8)+F(1,1000), F(9,10),F(99,100),F(1)):
        delta=beta-F(7,8)
        kappa=F(3,4)+2*delta
        assert kappa==2*beta-1
        assert kappa>=F(3,4)
        assert kappa<=1
        assert not (kappa-F(1,10**9)>=2*beta-1)
    print("KAPPA_EQUALS_TWO_BETA_MINUS_ONE_SATURATED_PASS",4)
    print("HOSTILE_KAPPA_BELOW_BETA_THRESHOLD_REJECTED")

if __name__=="__main__":
    basic_bounds()
    all_positive_height_budgets()
    beta_kappa_saturation()
    print("F003_EXACT_ENERGY_SCALE_AUDIT_PASS")
