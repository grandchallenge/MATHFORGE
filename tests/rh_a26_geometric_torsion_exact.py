"""Finite exact mechanism controls; not original Lean replay."""
from itertools import product, permutations
from math import prod, gcd
from functools import reduce

def det2(a,b,c,d): return a*d-b*c
# Full-rank lattice index and rank-one saturation, including zero columns.
det_cases=rankone=0
for a,b,c,d in product(range(-3,4),repeat=4):
    det=abs(det2(a,b,c,d))
    assert det <= (abs(a)+abs(c))*(abs(b)+abs(d))
    if det==0:
        g=reduce(gcd,map(abs,(a,b,c,d)))
        assert g <= max(1,abs(a)+abs(c),abs(b)+abs(d))
        rankone+=1
    det_cases+=1
# Exact exponent recurrence, avoid constructing enormous torsion integers.
rec=0
for m,A,s in product(range(9),range(9),range(1,9)):
    e=A*sum(s**j for j in range(1,m+1))
    assert e<=m*A*s**m
    if m: assert e==A*s**m+A*sum(s**j for j in range(1,m))
    rec+=1
# Orbit exponent compression and final constant compression.
orb=0
for b,N,p in product(range(1,25),range(1,13),range(9)):
    if N>b: continue
    assert 2*b*(1+b*N)+((5*b+2)*b+1)*b*N*(p+1)<=12*(p+1)*b**3*N
    orb+=1
assert 7681212<2**24
# HNF residue collision implies integral left equivalence in Q case.
# B=|det A| A^-1; verify exact over bounded nonsingular matrices.
keys={}; collisions=0
for a,b,c,d in product(range(-2,3),repeat=4):
    t=det2(a,b,c,d)
    if not t: continue
    I=abs(t); sign=1 if t>0 else -1
    B=tuple(sign*x for x in (d,-b,-c,a))
    key=(I,tuple(x%I for x in B))
    if key in keys:
        u,v,w,z=keys[key]
        C=(a*z-b*w,-a*v+b*u,c*z-d*w,-c*v+d*u)
        assert all(x%I==0 for x in C)
        assert abs(det2(*[x//I for x in C]))==1
        collisions+=1
    else: keys[key]=(a,b,c,d)
# Congruence separation on finite-order signed permutations in dimension 3.
signed=set()
for p in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        M=tuple(signs[i] if p[i]==j else 0 for i in range(3) for j in range(3))
        signed.add(tuple(x%3 for x in M))
assert len(signed)==48
print(f"PASS {det_cases} determinant cases ({rankone} singular); {rec} recurrence cases; {orb} orbit exponents; {collisions} residue collisions; {len(signed)} signed permutation residues")
