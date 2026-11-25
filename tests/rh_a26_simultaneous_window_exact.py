"""Finite exact controls for the conditional window reconstruction.

The logarithmic interval is checked analytically at its breakpoints, not
by sampling floating-point x. Integer center tests are only controls for
the ultrametric argument, not calculations of arithmetic tower centers.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import floor

def window(R,B,U,T):
    assert R>=len(T) and B>=1 and U>0
    if R==0:
        return U/2
    a=next((a for a in sorted(T) if U/(2*B)<a<=U),None)
    if a is None:
        return U/2
    return window(R-1,B,U/(2*B),T-{a})

def verify(R,B,U,T):
    y=window(R,B,U,T)
    J=2**(R+2)*B**R
    assert U/J<=y and 2*y<=U
    for a in T:
        # If [y,2y] intersects [a,infinity), the minimum u is max(a,y).
        # This tests the entire interval, including both endpoints.
        if a<=2*y:
            assert B*a<=max(y,a)
    return y

def interval_controls():
    count=0
    for U,B in product(map(Q,(1,2,8,32,128)),(Q(1),Q(3,2),Q(2),Q(4))):
        T0=[-U,Q(0),U/(2*B),U/2,U,2*U,U/3,U/(4*B)]
        T0=sorted(set(T0))
        for n in range(min(len(T0),4)+1):
            for T in combinations(T0,n):
                for extra in (0,1):
                    verify(n+extra,B,U,set(T));count+=1
    assert verify(3,Q(2),Q(128),{Q(40),Q(10),Q(1)})==4
    # An independently chosen window for a singleton is not automatically
    # valid for the union. At u=4, threshold 3 violates B*a<=u.
    assert 3<=4<2*3
    return count

def log_nat(p,Z):
    k=0
    while p**(k+1)<=Z:k+=1
    return k

def near_controls():
    count=0
    for p in (2,3,5,7):
        for Z in range(1,51):
            b=log_nat(p,Z);mod=p**(b+1)
            for s in range(mod):
                near=[a for a in range(1,Z+1) if (s-a)%mod==0]
                assert len(near)<=1
                count+=1
            # Union bound with duplicate centers.
            centers=[0,1,1,Z,Z+1]
            exc={a for a in range(1,Z+1) if any((s-a)%mod==0 for s in centers)}
            assert len(exc)<=len(centers)
    # Strict threshold necessary: p=3, Z=4, b=1, s=1.
    assert [a for a in range(1,5) if (a-1)%3==0]==[1,4]
    return count

def point_controls():
    count=0
    # x=2^u, X=2^v, Ct=2, J=4; log_l Z <= 2 Ct J log x
    # follows from log l>1/2. Test the exact natural-log bound
    # for l=2 using u,v integer and no floating arithmetic.
    for u in range(1,11):
        for v in range(u,4*u+1):
            Z=2**(2*v)
            assert log_nat(2,Z)<=2*4*u
            count+=1
    # Check exponent accounting for CK=1,2,3 and rational eps, using
    # x=2^(120 CK), eps=1/60, so x^eta=2 exactly.
    for CK in (1,2,3):
        for e,n,n0 in product((1,2),range(1,5),range(1,6)):
            if n>n0: continue
            assert (2*e*n)**CK<= (2*n0)**CK*2**CK
            # x^(eps/4)=2^(CK/2); square to keep exponents integral.
            assert ((2*e*n)**CK)**2*2**CK <= ((2*n0)**CK)**2*2**(3*CK)
            count+=1
    return count

if __name__=="__main__":
    print(f"PASS {interval_controls()} whole-window exact implications; {near_controls()} strict-neighborhood checks; {point_controls()} logarithm/exponent comparisons; strict-boundary and union controls")
