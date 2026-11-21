#!/usr/bin/env python3
"""Exact F003 principal sixth-power theta-discrepancy verifier.

Compares direct normalized Eisenstein prime-power Gauss valuation pair sum
with independent two-scale lattice counts for rational *step* radial profiles.
Tests algebraic identities and origin obstruction only, not smooth Poisson,
Lean elaboration or full Gaussian child energies.
"""
from fractions import Fraction as F
from itertools import product

PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
PRIMES={7:(3,1),13:(4,1),19:(5,2),31:(6,1),37:(7,3)}
checks=0

def check(b,msg=""):
    global checks
    assert b,msg
    checks+=1

def norm(z):
    a,b=z
    return a*a-a*b+b*b

def residue(z,p,q):
    a,b=p
    return (z[0]-a*pow(b,-1,q)*z[1])%q

def theta_step(t,B=23):
    return sum(1 for z in product(range(-B,B+1),repeat=2)
               if F(norm(z),1)<2*t)

def directly(q,p,T,c,d,B=23):
    # Nonzero g_d requires z=p^(d-1)u. The exact principal table:
    # product = (q-1)*q^((c+d)/2-2) [(q-1) if p|u else -1].
    pref=(q-1)*q**((c+d)//2-2)
    coeff=0
    for z in product(range(-B,B+1),repeat=2):
        if norm(z)>=2*T:continue
        coeff+=(q-1 if residue(z,p,q)==0 else -1)
    return pref*coeff

def via_two_scale(q,T,c,d,B=23):
    pref=(q-1)*q**((c+d)//2-2)
    return pref*(q*theta_step(T/q,B)-theta_step(T,B))

def main():
    for q,p in PRIMES.items():
        check(norm(p)==q)
        r=(-p[0]*pow(p[1],-1,q))%q
        check((r*r+r+1)%q==0)
        Ts=[F(1,8),F(1,4),F(1,2),F(5,8),F(3,4),F(1),F(3,2),F(2),
            F(3),F(5),F(q,5),F(q,2),F(q)]
        for c,d in ((6,12),(6,18),(12,18),(12,24)):
            check(c<d and c%6==d%6==0)
            # Both principal sector labels must coincide even after q-powers.
            check(q**c%36==q**d%36==1)
            for T in Ts:
                lhs=directly(q,p,T,c,d)
                rhs=via_two_scale(q,T,c,d)
                check(lhs==rhs,f"principal discrepancy q={q}, c={c}, d={d}, T={T}")
                check(q*(T/q)-T==0)
                if 2*T<=1:
                    expect=F((q-1)**2,q**2)*q**((c+d)//2)
                    check(lhs==expect,f"origin barrier q={q},c={c},d={d},T={T}")
                # Exact cutoff no norm 2 among Eisenstein units.
                check(theta_step(T)>=1)
        print(f"q={q}, principal c,d multiples of 6: exact Gauss pair = q*theta(T/q)-theta(T); low-origin PASS")
    for a,b in product(range(-25,26),repeat=2):
        check(2*norm((a,b))==a*a+b*b+(a-b)**2)
    check(all(norm((a,b))!=2 for a,b in product(range(-4,5),repeat=2)))
    print("EXACT ASSERTIONS",checks,"PASS")
    print("TEST SCOPE: discontinuous step-profile model, not smooth source Schwartz replay")
    print("PIN",PIN)

if __name__=="__main__":main()
