#!/usr/bin/env python3
"""Independent finite cyclic H^1 fixture for RH-A26 prime-to-index transfer.

For C_m acting on one-dimensional F_p by scalar a with a^m=1,
crossed homomorphisms are indexed by z with S_m(a)*z=0;
principal cocycles have z=(a-1)*b. Tests the finite-index-unit
mechanism in original SelUnit/eigV, NOT Galois/Sha cohomology.
"""


def h1_cyclic(p, m, a):
    assert m > 0 and pow(a, m, p) == 1
    s = sum(pow(a, i, p) for i in range(m)) % p
    z = {v for v in range(p) if s * v % p == 0}
    b = {(a - 1) * v % p for v in range(p)}
    assert b <= z
    return z, b


def main():
    tested = 0
    for p in (2, 3, 5, 7, 11, 13):
        for m in range(1, 26):
            for a in range(1, p):
                if pow(a, m, p) != 1:
                    continue
                z, b = h1_cyclic(p, m, a)
                if m % p:
                    assert z == b, (p, m, a, z, b)
                tested += 1
    z, b = h1_cyclic(3, 3, 1)
    assert z == {0, 1, 2} and b == {0}
    print(f"PASS {tested} valid cyclic actions; p∤m yields H^1=0; excluded p=m=3 has nonzero H^1")


if __name__ == "__main__":
    main()
