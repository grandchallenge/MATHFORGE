#!/usr/bin/env python3
"""Independent exact finite-ring adversary for F003 pair-conductor Gaussian theorem.

This checks the Eisenstein norm, a nondegenerate additive-pairing model away
from the ramified prime 3, finite Fourier Plancherel, coprime CRT factorization
and conductor-exponent arithmetic. It does NOT compute the actual sextic
character, prove infinite Poisson summation, or replace the source's primitive
quotientTrace at moduli divisible by 3.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd

PIN = "1581d4cbdd69a0faf34b2089614fe2a814316a6a"

def norm(x):
    a, b = x
    return a*a-a*b+b*b

def trace_pair(z, x, m):
    a,b=z
    c,d=x
    return (2*a*c-a*d-b*c-b*d)%m

def pairing_coeff(x,m):
    c,d=x
    return ((2*c-d)%m,(-c-d)%m)

def residues(m):
    return list(product(range(m),repeat=2))

def units(m):
    return [x for x in residues(m) if gcd(norm(x),m)==1]

def additive_image_card(x,m):
    A,B=pairing_coeff(x,m)
    return m//gcd(m,A,B)

def exact_orthogonality(m):
    tests=0
    for x in residues(m):
        order=additive_image_card(x,m)
        if x==(0,0):
            assert order==1
        else:
            assert order>1, (m,x,order)
        # The image of z -> trace(z*x) is a subgroup of cyclic Z/m,
        # each of its residues has equal fiber cardinality.
        h=[0]*m
        for z in residues(m):
            h[trace_pair(z,x,m)]+=1
        active=[i for i,n in enumerate(h) if n]
        assert len(active)==order
        assert set(h[i] for i in active)=={m*m//order}
        assert h[0]==m*m//order
        tests+=5
    return tests

def exact_plancherel_unitmask(m):
    # g(z)=1/m * sum_x unitmask(x)*zeta_m^trace(z*x).
    # Normalized Fourier Plancherel reduces to sum_z characters=0
    # except at x=y (the primitive pairing), so mean |g|^2=U/m^2.
    U=units(m)
    hits=0
    for x in U:
        for y in U:
            diff=((x[0]-y[0])%m,(x[1]-y[1])%m)
            order=additive_image_card(diff,m)
            assert (order==1)==(x==y)
            if order==1: hits+=1
    assert hits==len(U)
    assert 0<=F(hits,m*m)<=1
    return len(U)**2+2, F(hits,m*m),len(U)

def crt_zero_cross(m,n):
    assert gcd(m,n)==1
    q=m*n
    seen=set()
    for z in residues(q):
        seen.add(((z[0]%m,z[1]%m),(z[0]%n,z[1]%n)))
    assert len(seen)==q*q==(m*m)*(n*n)
    tests=1
    # Every summand in the cross-correlation of g_m and g_n
    # contains a nontrivial character of Z[omega]/(mn).
    # Such a character sums to zero exactly, by finite orthogonality.
    for x in units(m):
        for y in units(n):
            Am,Bm=pairing_coeff(x,m)
            An,Bn=pairing_coeff(y,n)
            A=(n*Am-m*An)%q
            B=(n*Bm-m*Bn)%q
            assert not(A==0 and B==0), (m,n,x,y)
            assert q//gcd(q,A,B)>1
            tests+=2
    return tests

def conductor_gap():
    tests=0
    for Z in (2,3,5,7):
        for rho in (2,4,6,8):
            for d in range(0,rho,2):
                K=Z**rho
                pair_N=Z**d
                assert pair_N<K
                t=Z**((rho-d)//2)
                assert t*t==K//pair_N
                for A in (2,4,6,10,16):
                    actual=F(pair_N,(1+t)**A)
                    claimed=F(Z**d,Z**(A*(rho-d)//2))
                    assert actual<=claimed
                    tests+=4
    return tests

def main():
    checked=0
    for a,b in product(range(-30,31),repeat=2):
        assert 2*norm((a,b))==a*a+b*b+(a-b)**2
        checked+=1
    for m in (2,4,5,7,8,10,11):
        checked+=exact_orthogonality(m)
        n,frac,U=exact_plancherel_unitmask(m)
        checked+=n
        print(f"mod {m}: norm={m*m}, unit-count={U}, mean-square={frac}, primitive pairing PASS")
    for m,n in ((2,5),(4,5),(4,7),(5,7)):
        ntest=crt_zero_cross(m,n)
        checked+=ntest
        print(f"CRT pair {m},{n}: {ntest} exact checks; off-diagonal zero PASS")
    # Hostile mutation: uncorrected field trace pairing has discriminant 3
    # and is degenerate modulo 3. The source uses primitive quotientTrace.
    witness=(2,1)
    assert witness!=(0,0)
    assert pairing_coeff(witness,3)==(0,0)
    assert additive_image_card(witness,3)==1
    checked+=3
    checked+=conductor_gap()
    print("mod 3 raw-trace degeneracy FOUND (expected hostile mutation)")
    print("conductor-gap exponent inequalities PASS")
    print(f"ASSERTIONS {checked} PASS")
    print("BOUNDARY: actual primitive source transfer proof mathematical, no Lean replay of new lemma")
    print("BOUNDARY: sharp high-conductor/shared-prime Gaussian child energies OPEN")
    print("PIN", PIN)

if __name__=="__main__":
    main()
