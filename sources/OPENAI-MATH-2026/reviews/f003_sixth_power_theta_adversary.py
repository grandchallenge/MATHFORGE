#!/usr/bin/env python3
"""F003 exact bounded sextic theta/unit-symmetry and critical-radius adversary.

Finite prime-field sextic characters and integer Eisenstein representatives;
NO replacement for the pinned genuine characters, smooth source profile, Lean
proof of Poisson, composite CRT, or universal seeded-energy estimate.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import gcd

PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
PRIMES={7:(3,1),13:(4,1),19:(5,2),31:(6,1),37:(7,3)}
ROOTS6=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
UNITS=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))
checks=0

def require(v,msg=""):
    global checks
    assert v,msg
    checks+=1

def norm(z):
    a,b=z
    return a*a-a*b+b*b

def mul(x,y):
    a,b=x
    c,d=y
    return a*c-b*d,a*d+b*c-b*d

def lattice(B):
    return ((a,b) for a,b in product(range(-B,B+1),repeat=2))

def primitive_logs(q):
    for g in range(2,q):
        vals=[pow(g,e,q) for e in range(q-1)]
        if len(set(vals))==q-1:
            return g,{v:i for i,v in enumerate(vals)}
    raise ValueError(q)

def residue_map(p,q):
    a,b=p
    return (-a*pow(b,-1,q))%q

def residue(z,r,q):
    return (z[0]+r*z[1])%q

def plus(x,y):
    return x[0]+y[0],x[1]+y[1]

def char_exponent(z,q,r,logs,d):
    v=residue(z,r,q)
    return None if v==0 else (d*logs[v])%6

def char_sum(q,p,logs,r,d,X):
    # Formal integer ring Z[omega] evaluates sixth roots exactly.
    total=(0,0)
    B=int((4*X)**.5)+2
    for z in lattice(B):
        nz=norm(z)
        if nz==0 or nz>X: continue
        e=char_exponent(z,q,r,logs,d)
        if e is not None:total=plus(total,ROOTS6[e])
    return total

def test_prime(q,p):
    require(norm(p)==q)
    r=residue_map(p,q)
    require((r*r+r+1)%q==0)
    require(q%6==1)
    g,logs=primitive_logs(q)
    require(len(logs)==q-1)
    for u in UNITS:
        require(norm(u)==1)
        require(residue(u,r,q)!=0)
    for d in (1,2,3,4,5,6,7,8,11,12):
        trivial_all=all(char_exponent(u,q,r,logs,d)==0 for u in UNITS)
        criterion=(d*((q-1)//6))%6==0
        require(trivial_all==criterion,f"unit norm gate q={q}, d={d}")
        if not trivial_all:
            for X in (1,3,4,7,13,19,31):
                require(char_sum(q,p,logs,r,d,X)==(0,0),
                        f"radial orbit not canceled q={q},d={d},X={X}")
        # Gauss frequency change-of-variable, equality of exact formal
        # root-of-unity monomial multisets, not floating point.
        for u in range(1,q):
            left=Counter(((d*logs[x])%6,(u*x)%q) for x in range(1,q))
            right=Counter((((d*(logs[y]-logs[u]))%6),y)
                          for y in range(1,q))
            require(left==right,f"prime field Gauss shift q={q},d={d},u={u}")
    if q==37:
        require(char_sum(q,p,logs,r,7,1)==(6,0))
        # Only six units (norm one), no Eisenstein norm two elements.
        require(all(norm(z)!=2 for z in lattice(3)))
    if q in (7,13,19,31):
        require(char_sum(q,p,logs,r,7,1)==(0,0))
    print(f"q={q}, Eisenstein p={p}, omega mod p={r}, primitive field generator={g}; unit gate and exact phase shifts PASS")

def cutoff_principal(q,c,d,t):
    # Phi_surrogate(x) = 1 if 0<=x<2, else zero.
    # K=q^(d-1)*t, all lattice sums are finite.
    B=int((8*q)**.5)+3
    a=sum(1 for u in lattice(B) if norm(u)>0 and norm(u)<2*t
          and True)  # below, sieve by residue divisibility for each q prime
    return a

def cutoff_tests(q,p):
    r=residue_map(p,q)
    # nonprincipal d=7: z=p^6*u with p not dividing u.
    for t in (F(1,4),F(1,2),F(3,4),F(1),F(2),F(q,2),F(q)):
        B=int((8*q)**.5)+3
        eligible=[z for z in lattice(B) if norm(z)<2*t and
                  residue(z,r,q)!=0]
        if 2*t<=1:
            require(not eligible)
        if q==37 and t==1:
            require(len(eligible)==6)
            require(set(eligible)==set(UNITS))
        # principal c=6,d=12: all nonzero z=p^11*u (unit mod p),
        # or z=p^12*v (any v); the origin always survives.
        numerator=(q-1)*sum(1 for v in lattice(B) if norm(v)*q<2*t)
        numerator-=len(eligible)
        baseline=(q-1) if 2*t<=1 else None
        if baseline is not None:
            require(numerator==baseline)
        # The exact prefactor (1-1/q) q^((6+12)/2-1)
        # multiplies numerator; at low radius it is the origin
        # (1-1/q)^2 q^9.
        if baseline is not None:
            pref=F(q-1,q)*q**8
            require(pref*numerator==F((q-1)**2,q**2)*q**9)
    print(f"q={q}: radial hard cutoff, p^6/p^7 nonprincipal and p^6/p^12 origin checks PASS")

def theta_coefficient_tests():
    for q in (7,13,19,31,37):
        for c in (6,12,18):
            for d in range(c+1,c+9):
                # q^c - q^(c-1) / q^((c+d)/2) is the
                # coefficient of K in the exact mixed Poisson formula.
                numerator=F(q**c-q**(c-1),1)
                # Compare *squares* to avoid floating-point sqrt.
                amplitude_squared=F(numerator*numerator,q**(c+d))
                claimed=F((q-1)**2,q**2)
                exp=c-d
                claimed*=F(q**exp) if exp>=0 else F(1,q**(-exp))
                require(amplitude_squared==claimed)
    print("all exact Poisson coefficient squares PASS")

def main():
    for a,b in product(range(-25,26),repeat=2):
        require(2*norm((a,b))==a*a+b*b+(a-b)**2)
    for q,p in PRIMES.items():
        test_prime(q,p)
        cutoff_tests(q,p)
    theta_coefficient_tests()
    print("EXACT ASSERTIONS",checks,"PASS")
    print("CAUTION: no unverified smooth-source, CRT-global, infinite-Poisson or MATHCERT claim")
    print("PIN",PIN)

if __name__=="__main__":
    main()
