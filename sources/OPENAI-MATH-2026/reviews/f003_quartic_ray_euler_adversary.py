#!/usr/bin/env python3
"""Exact independent F003 quartic Eisenstein ray-character/Euler adversary.

The ring Z[omega]/(5), omega^2+omega+1=0, is F_25.
A generator of F_25^× has order 24. Quotienting by the image
of global units μ_6 leaves a cyclic group C_4 with four ray
characters; this program builds a faithful quartic one and checks
its exact values, principal ideal choices and deleted Euler factors.

NO analytic nonvanishing or standard idèle-character formalization.
"""
from __future__ import annotations

from typing import Optional

P = 5
G = (1, 3)
ONE = (1, 0)
ZERO = (0, 0)
UNIT_SIX = ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1))
IPOW = ((1, 0), (0, 1), (-1, 0), (0, -1))

def mod(z: tuple[int,int]) -> tuple[int,int]:
    return (z[0] % P, z[1] % P)

def mul_raw(a: tuple[int,int], b: tuple[int,int]) -> tuple[int,int]:
    x, y = a; u, v = b
    return (x*u-y*v, x*v+y*u-y*v)

def mul(a: tuple[int,int], b: tuple[int,int]) -> tuple[int,int]:
    return mod(mul_raw(a,b))

def pow_ring(a: tuple[int,int], n:int) -> tuple[int,int]:
    assert n>=0
    out=ONE
    while n:
        if n&1: out=mul(out,a)
        a=mul(a,a)
        n//=2
    return out

def norm(z:tuple[int,int])->int:
    a,b=z
    return a*a-a*b+b*b

LOG={pow_ring(G,k):k for k in range(24)}
assert len(LOG)==24, "wrong primitive generator of F25 units"
assert set(LOG)=={(a,b) for a in range(P) for b in range(P) if (a,b)!=ZERO}
assert pow_ring(G,24)==ONE
assert all(pow_ring(G,k)!=ONE for k in (1,2,3,4,6,8,12))
assert {LOG[mod(z)] for z in UNIT_SIX}=={0,4,8,12,16,20}

def i_mul(a:tuple[int,int],b:tuple[int,int])->tuple[int,int]:
    x,y=a;u,v=b
    return (x*u-y*v,x*v+y*u)

def chi(z:tuple[int,int])->tuple[int,int]:
    """χ : (O/(5)) → ℤ[i]; nonunits map to zero."""
    k=LOG.get(mod(z))
    return (0,0) if k is None else IPOW[k%4]

def bad_non_unit_trivial(z:tuple[int,int])->int|None:
    """Hostile: exponent mod 24 does NOT descend through global units."""
    return LOG.get(mod(z))

def test():
    values=[(a,b) for a in range(P) for b in range(P)]
    for a in values:
        for b in values:
            assert chi(mul(a,b))==i_mul(chi(a),chi(b)),(a,b)
    print("FINITE_CHARACTER_MULTIPLICATIVITY_PASS", len(values)**2)
    for z in values:
        for u in UNIT_SIX:
            assert chi(mul(z,mod(u)))==chi(z), (z,u)
    assert all(chi(u)==(1,0) for u in UNIT_SIX)
    print("GLOBAL_UNIT_TRIVIALITY_PASS",len(values)*len(UNIT_SIX))
    assert len({LOG[x]%4 for x in LOG})==4
    assert chi((5,0))==(0,0) and norm((5,0))==25
    print("INERT_MODULUS_5_ZERO_COEFFICIENT_PASS")

    # The ideal (2) is prime because 2 is inert in Q(√−3).
    # The ideal (3) ramifies: (1−ω)^2 = −3ω.
    # The ideal (7) splits: 7=(3+ω)(2−ω).
    pi3=(1,-1)
    pi7=(3,1)
    pi7bar=(2,-1)
    assert norm((2,0))==4 and norm(pi3)==3
    assert norm(pi7)==norm(pi7bar)==7
    assert mul_raw(pi7,pi7bar)==(7,0)
    assert mul_raw(pi3,pi3)==(0,-3)
    assert chi((2,0))==(-1,0)
    assert chi(pi3)==(0,-1)
    assert chi(pi7)==chi(pi7bar)==(0,1)
    assert chi((3,0))==i_mul(chi(pi3),chi(pi3))==(-1,0)
    assert chi((7,0))==i_mul(chi(pi7),chi(pi7bar))==(-1,0)
    print("PRIME_IDEAL_NORMS_RAMIFIED_SPLIT_INERT_PASS")

    # An O-unit changes principal-ideal generator, but not χ((α)).
    for prime in ((2,0), pi3, pi7, pi7bar):
        for u in UNIT_SIX:
            assert chi(mul_raw(prime,u))==chi(prime)
    print("PRINCIPAL_GENERATOR_CHOICE_INVARIANCE_PASS")

    # Increasing modulus from 5 to 10 deletes the inert prime (2).
    # Primitive local series at (2): Σ (-1)^k X^k=1/(1+X).
    # Multiply by deletion factor (1+X) to get 1 exactly.
    N=30
    local=[(-1)**k for k in range(N+1)]
    deleted=[local[k]+(local[k-1] if k else 0) for k in range(N+1)]
    assert deleted==[1]+[0]*N
    assert local[1]==-1 and deleted[1]==0
    print("IMPRIMITIVE_5_TO_10_EULER_DELETION_IDENTITY_PASS",N)

    # Nontrivial character mod 5 has 4th roots of unity; allowing every
    # 24th root instead would violate invariance under ω.
    omega=(0,1)
    assert chi(omega)==(1,0)
    assert bad_non_unit_trivial(omega)==16
    assert bad_non_unit_trivial(omega)!=0
    print("HOSTILE_UNRESTRICTED_UNIT_CHARACTER_REJECTED")

    # A hypothetical erroneous split prime of norm 5 is incompatible
    # with the inert quotient field and N((5))=25.
    assert all((a*a-a*b+b*b)%5!=0 for a,b in values if (a,b)!=ZERO)
    print("HOSTILE_INERT_5_SPLIT_FACTOR_REJECTED")
    print("F003_QUARTIC_CHARACTER_AND_EULER_ADVERSARY_PASS")

if __name__=="__main__":
    test()
