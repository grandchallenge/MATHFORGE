#!/usr/bin/env python3
"""OAI26 F003: independent Eisenstein quartic Gaussian FE and high-stage capacity audit.

Source locks: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
  TraceCharacter.traceCharacter_eq_paperE, GaussianTheta.parameter and
  theta_functional_equation, StripActual.completionScale_eq_inv,
  Energy/PositiveHighSourceBound.PositiveHighAt.
No upstream code imported. mpmath 1.3; exact Gaussian-integer residue operations
and fractional high-stage constraints. Finite sums have explicit analytic
Gaussian-tail majorants. Test of ONE primitive character, not all characters.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
import mpmath as mp

P=5
GEN=(1,3)
ROOTS=((1,0),(0,1),(-1,0),(0,-1))
ONE=(1,0)
ZERO=(0,0)

def mul_mod(x,y):
    a,b=x; c,d=y
    return ((a*c-b*d)%P,(a*d+b*c-b*d)%P)

def char_log():
    x=ONE; log={}
    for k in range(24):
        assert x not in log
        log[x]=k
        x=mul_mod(x,GEN)
    assert x==ONE and len(log)==P*P-1
    return log

LOG=char_log()

def chi(z):
    k=LOG.get((z[0]%P,z[1]%P))
    return ZERO if k is None else ROOTS[k%4]

def zadd(x,y):
    return (x[0]+y[0],x[1]+y[1])

def norm(z):
    a,b=z
    return a*a-a*b+b*b

def unit_invariance_and_primitive():
    six=((1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1))
    assert {LOG[(a%P,b%P)] for a,b in six}==set(range(0,24,4))
    for a in range(P):
        for b in range(P):
            x=(a,b)
            for u in six:
                assert chi(mul_mod(x,u))==chi(x)
    # (5) is inert; a nontrivial F25-character thus has conductor (5),
    # not the unit ideal. The group of global units has order six.
    assert chi((1,0))==(1,0)
    assert chi((0,0))==ZERO
    assert chi(GEN)==(0,1)
    print("FINITE_QUARTIC_CHARACTER_GLOBAL_UNIT_AND_PRIMITIVITY_PASS")

def gauss_exact():
    # For c=5, the paper additive character is
    # exp(2 pi i*(2/sqrt(3))*Im((a+b omega)/5)) = exp(2 pi i*b/5).
    rows=[]
    for b in range(P):
        rows.append(sum_gaussian([chi((a,b)) for a in range(P)]))
    assert rows==[(0,0),(2,-1),(-2,1),(-2,1),(2,-1)],rows
    # tau=(2-i)*(zeta+zeta^-1-zeta^2-zeta^-2)
    #     =sqrt(5)*(2-i). The last cyclotomic identity is exact.
    eps=mp.mpc(2,-1)/mp.sqrt(5)
    zeta=mp.exp(2j*mp.pi/5)
    gauss=sum(mp.mpc(*rows[b])*zeta**b for b in range(P))
    assert abs(gauss-5*eps)<mp.mpf("1e-92")
    assert abs(abs(eps)-1)<mp.mpf("1e-92")
    assert abs(eps*(1/eps)-1)<mp.mpf("1e-92")
    print("EXACT_GAUSS_ROWS_AND_CYCLOTOMIC_ROOT_NUMBER_PASS",
          "epsilon="+mp.nstr(eps,23))
    return eps

def sum_gaussian(vals):
    return sum((v[0] for v in vals),0),sum((v[1] for v in vals),0)

def lattice_coefficients(R):
    by_norm=defaultdict(lambda:ZERO)
    for a in range(-R,R+1):
        for b in range(-R,R+1):
            n=norm((a,b))
            by_norm[n]=zadd(by_norm[n],chi((a,b)))
    assert by_norm[0]==ZERO
    return {n:v for n,v in by_norm.items() if v!=ZERO}

def theta(t,coeff):
    alpha=2*t/(mp.sqrt(3)*P)
    return mp.fsum(mp.mpc(*v)*mp.exp(-mp.pi*alpha*n)
                   for n,v in coeff.items())

def gaussian_outside_box_bound(t,R):
    # norm(a+b omega)>= (a*a+b*b)/2 for all integers a,b.
    # Union bound over |a|>R or |b|>R, then separate variables.
    c=mp.pi*t/(P*mp.sqrt(3))
    tail_one=mp.exp(-c*(R+1)**2)/(1-mp.exp(-c*(2*R+3)))
    all_one=1+2*mp.exp(-c)/(1-mp.exp(-3*c))
    return 4*tail_one*all_one

def theta_checks(eps):
    R=48
    coeff=lattice_coefficients(R)
    times=tuple(mp.mpf(x) for x in ("0.25","0.5","1","2","4"))
    vals={t:theta(t,coeff) for t in times}
    max_resid=mp.mpf(0)
    max_tail=mp.mpf(0)
    for t in times:
        lhs=vals[t]
        rhs=eps/t * mp.conj(vals[1/t])
        residue=abs(lhs-rhs)
        trunc=gaussian_outside_box_bound(t,R)+abs(eps)/t*gaussian_outside_box_bound(1/t,R)
        assert residue<10*trunc+mp.mpf("1e-88"),(str(t),mp.nstr(residue,8))
        assert trunc<mp.mpf("1e-87"),(str(t),mp.nstr(trunc,8))
        max_resid=max(max_resid,residue)
        max_tail=max(max_tail,trunc)
        print("THETA_FE_PASS",mp.nstr(t,6),
              "theta="+mp.nstr(lhs,15),
              "residual="+mp.nstr(residue,4),
              "trunc_bound="+mp.nstr(trunc,4))
    lhs=vals[mp.mpf(1)]
    # Reject missing sqrt(N(c))=5 normalization.
    assert abs(lhs-5*eps*mp.conj(lhs))>mp.mpf("0.2")
    # Reject conjugating the Gauss root on the wrong side.
    assert abs(lhs-mp.conj(eps)*mp.conj(lhs))>mp.mpf("0.2")
    print("HOSTILE_WRONG_ROOT_AND_CONDUCTOR_NORMALIZATION_REJECTED")
    print("GAUSSIAN_THETA_FE_BOUNDED_TRUNCATION_PASS",
          "max_residual="+mp.nstr(max_resid,8),
          "max_tail="+mp.nstr(max_tail,8))

def capacity_checks():
    # Source Energy/PositiveHighSourceBound.PositiveHighAt:
    # x+y+6*kappa*w <= m,  5*m/6 <= x+y+w,
    # with x=length(Z,X1), y=length(Z,X2), w=sum slot weights.
    # Their DIFFERENCE forces (6*kappa-1)*w <= m/6.
    m=F(1)
    x=y=F(43,100)
    w=F(1,50)
    for beta in (F(7,8),F(9,10),F(1)):
        kappa=2*beta-1
        assert kappa>=F(3,4)
        assert x+y+6*kappa*w<=m
        assert 5*m/6<=x+y+w
        assert (6*kappa-1)*w <=m/6
        # necessary max slot mass w/m <= 1/(6*(6*kappa-1))
        assert w/m<=1/(6*(6*kappa-1))
    # This is an ARITHMETIC witness, not a witness for the full
    # NaturalState/Profiles/PositiveAt logical hypotheses.
    hostile_w=F(1,10)
    assert x+y+hostile_w>=5*m/6
    assert x+y+6*F(3,4)*hostile_w>m
    print("HIGH_STAGE_CAPACITY_NONVACUOUS_ARITHMETIC_WITNESS_PASS",
          "lengths=43/100,43/100","prime_weight=1/50")
    print("HIGH_STAGE_WEIGHT_CEILING_AND_HOSTILE_HEAVY_WEIGHT_PASS")

if __name__=="__main__":
    mp.mp.dps=100
    unit_invariance_and_primitive()
    eps=gauss_exact()
    theta_checks(eps)
    capacity_checks()
    print("F003_INDEPENDENT_QUARTIC_THETA_AND_HIGH_STAGE_CAPACITY_PASS")
