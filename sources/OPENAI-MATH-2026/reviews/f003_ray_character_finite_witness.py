#!/usr/bin/env python3
"""Exact elementary checks for finite ray-character counts in Z[omega]/(n).

omega^2 + omega + 1 = 0. This checks selected integer moduli only.
It does NOT verify every Hecke character or any seven-eighths bound.
"""
from math import gcd

EXPECTED = {2:(3,3,1), 3:(6,6,1), 5:(24,6,4), 7:(36,6,6), 11:(120,6,20)}

def norm(z,n):
    a,b=z
    return (a*a-a*b+b*b)%n

def unit_data(n):
    units={(a,b) for a in range(n) for b in range(n)
           if gcd(norm((a,b),n),n)==1}
    image={(a%n,b%n) for a,b in
           [(1,0),(-1,0),(0,1),(0,-1),(-1,-1),(1,1)]}
    assert image <= units and len(units)%len(image)==0
    return len(units),len(image),len(units)//len(image)

for n, expected in EXPECTED.items():
    observed=unit_data(n)
    assert observed==expected,(n,observed,expected)
    print(f"modulus={n} residue_units={observed[0]} "
          f"global_unit_image={observed[1]} ray_character_count={observed[2]}")
    if n==5:
        unsafe=observed[0]
        assert unsafe!=observed[2]
        print("HOSTILE_UNIT_TRIVIALITY_OMISSION_REJECTED",unsafe,observed[2])
print("EISENSTEIN_INTEGER_RAY_QUOTIENT_FINITE_EXAMPLES_PASS")
