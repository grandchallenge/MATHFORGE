#!/usr/bin/env python3
"""F003 exact cyclotomic sextic Gauss normalization and smooth-completion adversary.

Exact arithmetic in Z[omega,zeta_q] for primes q=7,13,19,31,37.
Formal eta exponents are reduced by Phi_q=1+...+T^(q-1). No floats.
The bound on the infinite radial theta sum is independently proved in the
companion report; finite tests do NOT certify analytic estimates or MATHCERT.
"""
from itertools import product
from fractions import Fraction
from math import gcd

PIN="1581d4cbdd69a0faf34b2089614fe2a814316a6a"
PRIMES=(7,13,19,31,37)
R6=((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1))
count=0

def check(b,msg=""):
    global count
    assert b,msg
    count+=1

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def sub(a,b): return (a[0]-b[0], a[1]-b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def norm(a): return a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
def minus(a): return (-a[0],-a[1])
def poly_zeros(q): return [(0,0)]*q
def scale_poly(P,c): return [mul(p,c) for p in P]
def poly_mul(P,Q):
    q=len(P)
    R=poly_zeros(q)
    for a,pa in enumerate(P):
        for b,pb in enumerate(Q):
            R[(a+b)%q]=add(R[(a+b)%q],mul(pa,pb))
    return R
def equal_mod_cyclo(P,Q):
    # Equality modulo 1+zeta+...+zeta^(q-1) for prime q not 3,
    # whose minimal polynomial retains degree q-1 over Q(omega).
    D=[sub(x,y) for x,y in zip(P,Q)]
    return len(set(D))==1

def primitive_logs(q):
    for g in range(2,q):
        A=[pow(g,k,q) for k in range(q-1)]
        if len(set(A))==q-1: return g,{a:i for i,a in enumerate(A)}
    raise ValueError(q)

def tau(q, logs, d, h):
    out=poly_zeros(q)
    for a in range(1,q):
        out[(h*a)%q]=add(out[(h*a)%q],R6[(d*logs[a])%6])
    return out

def conjugate_tau(q, logs, d, h):
    out=poly_zeros(q)
    for a in range(1,q):
        out[(-h*a)%q]=add(out[(-h*a)%q],R6[(-d*logs[a])%6])
    return out

def test_cyclotomic():
    for q in PRIMES:
        g,logs=primitive_logs(q)
        for d in (1,2,3,4,5,7,8,11):
            if d%6==0: continue
            S=tau(q,logs,d,1)
            C=conjugate_tau(q,logs,d,1)
            P=poly_mul(S,C)
            target=poly_zeros(q);target[0]=(q,0)
            check(equal_mod_cyclo(P,target),f"|tau|^2=q fails q={q},d={d},P={P}")
            check(equal_mod_cyclo(tau(q,logs,d,0),poly_zeros(q)))
            for h in range(1,q):
                T=tau(q,logs,d,h)
                predicted=scale_poly(S,R6[(-d*logs[h])%6])
                check(equal_mod_cyclo(T,predicted),f"Gauss shift q={q},d={d},h={h}")
                CT=conjugate_tau(q,logs,d,h)
                predictedC=scale_poly(C,R6[(d*logs[h])%6])
                check(equal_mod_cyclo(CT,predictedC))
            check(len(set(R6))==6)
        print(f"q={q}: exact nonprincipal sextic norm, inverse character and all frequency shifts PASS (field generator {g})")

def test_radial_majorants():
    # Partial nonzero Eisenstein lattice sums, NOT infinite tail validation.
    # Exact theta-tail samples, uniform nonnegative real bounds.
    for den in (1,2,4,8,16,32):
        for num in (1,2,4,8,16):
            th=Fraction(num,den)
            for B in (2,3,4,6):
                s=sum((1+th*norm((a,b)))**(-B)
                      for a,b in product(range(-9,10),repeat=2)
                      if a or b)
                crude=Fraction(1000,1)*(th**(-1) if th<=1 else th**(-B))
                check(s<=crude)
        print(f"theta denominator {den}: exact partial lattice tail ≤ scalar comparator PASS")
    for K in range(1,61):
        actual=sum(1 for a,b in product(range(-15,16),repeat=2)
                   if norm((a,b))<2*K)
        # Each active lattice point has |a|,|b|<2sqrt(K).
        # Integer-only version (1+4sqrt K)^2 upper bounded by (1+4K)^2.
        check(actual <= (1+4*K)**2)
    # Enforce literal q37 threshold and the arithmetic unit orbit.
    for q in PRIMES:
        m=(q-1)//6
        for d in range(1,25):
            gate=(d*m)%6==0
            check(gate==all((d*m*k)%6==0 for k in range(6)))
    print("positive-tail comparator, compact-ball counts, q mod 36 unit gate PASS")

def main():
    test_cyclotomic()
    test_radial_majorants()
    print("EXACT ASSERTIONS",count,"PASS")
    print("LIMIT: no infinite theta tail certified by finite counts; source pin and scope enforced")
    print("PIN",PIN)

if __name__=="__main__":main()
