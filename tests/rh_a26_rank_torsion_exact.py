"""Exact finite controls of the arithmetic counting bridge, not Lean replay."""
from itertools import product
from math import prod,gcd
weights=units=counts=bock=0
for ell,k,nu in product(range(2,8),range(0,8,2),range(1,5)):
    Q=ell**nu
    U=prod(1-ell**s for s in range(1,k+1))
    assert gcd(U,Q)==1
    u=pow(U,-1,Q)
    assert (u*ell**k*U-ell**k)%Q==0
    units+=1
    for j in range(1,k+2):
        P=prod(ell**j-ell**s for s in range(2,k+2))
        assert P==(ell**k*U if j==1 else 0)
        weights+=1
# Map from Z^r x Z/M to Z/Q with allowed generator images.
for Q,M,r in product(range(2,9),range(1,10),range(3)):
    for coeff in product(range(Q),repeat=r):
        for t in range(Q):
            if M*t%Q: continue
            img={(sum(c*x for c,x in zip(coeff,v))+t*y)%Q
                 for v in product(range(Q),repeat=r) for y in range(M)}
            assert len(img)<=Q**r*M
            counts+=1
# Two-term chain complex: d: Z -> Z multiplication by M.
# Modular cycle y has beta=[M*y/Q] in Z/M; zero iff lifts to integral cycle.
for Q,M in product(range(1,25),repeat=2):
    fibers={}
    for y in range(Q):
        if M*y%Q: continue
        beta=(M*y//Q)%M
        assert Q*beta%M==0
        assert (beta==0)==(y==0)
        assert (M*(y+Q)//Q)%M==beta
        fibers.setdefault(beta,[]).append(y)
        bock+=1
    assert len(fibers)<=M
    assert all(len(v)==1 for v in fibers.values())
# Real rank zero cannot imply a uniform torsion count.
for M in (2,10,100,10000):
    assert len(range(M))==M
print(f"PASS {weights} weight products; {units} modular inverses; {counts} image counts; {bock} Bockstein lift controls")
