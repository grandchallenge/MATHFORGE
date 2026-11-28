"""Finite exact controls of SFinal, not original Lean replay or duality proof."""
from itertools import product
from fractions import Fraction as F
from math import gcd

def val(a,p):
    assert a>0
    v=0
    while a%p==0:a//=p;v+=1
    return v

def ilog(a,p):
    assert a>=1
    k=0
    while a>=p:a//=p;k+=1
    return k

# LTE at the safe initial depth 2 (including the prime two).
local=0
for p,i,E in product((2,3,5,7,11),range(1,41),range(1,41)):
    k=2+val(i,p)+val(E,p)
    q=p**(k+1)
    assert pow(1+p*p,i*E,q)!=1
    assert pow(1+p*p,i*E,p**k)==1
    for r in (1,k,k+1,k+2):
        Q=p**r
        a=pow(1+p*p,-i*E,Q)
        assert gcd(a-1,Q)==p**min(k,r)
        local+=1
# Abstract finite local-global length identity; kernels and cokernels
# measured independently for maps between possibly different modules.
lengths=0
for p,r,s,a in product((2,3,5,7),range(1,5),range(1,5),range(5)):
    m=p**r;n=p**s
    # map x->coefficient*x mod n, respecting source modulus
    coefficient=p**max(0,s-r)*p**a
    kernel=gcd(m, m*gcd(n,coefficient)//n)
    image=n//gcd(n,coefficient)
    coker=n//image
    assert kernel*image==m
    assert val(m,p)+val(coker,p)==val(kernel,p)+val(n,p)
    assert val(m,p)<=val(kernel,p)+val(n,p)
    lengths+=1
# Finite primary composition length and cardinality.
cards=0
for p,exponents in product((2,3,5,7),product(range(5),repeat=3)):
    N=1
    for a in exponents:N*=p**a
    assert val(N,p)==sum(exponents)
    cards+=1
# Local valuation contribution and rational upper bound in NumFin.
num=0
for E,n in product(range(1,65),range(1,65)):
    x=2*E*n
    assert E+3<=2*(2*E)*(2*E+3)
    assert 4*n*n*(2*E)*(2*E+3)<=10*x*x<=x**9-1
    for Y in (F(1,2),F(2,3),F(1),F(10)):
        P=4*n*n*Y*(2*E)*(2*E+3)
        for C in (-1,0,1,24,141):
            p=x**max(C,0)
            assert P<=(x**9-1)*p*Y
            assert p*Y+(x**9-1)*p*Y==x**(max(C,0)+9)*Y
            num+=1
assert max(141,0)+9==150
print(f"PASS {local} local invariant controls; {lengths} exact length identities; {cards} finite module cardinalities; {num} numerical absorption controls")
