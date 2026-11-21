#!/usr/bin/env python3
"""Exact-integer regression for RH-A26 original log_bnd_le_mul_log source.

All checks are integer arithmetic; no source Lean replay or arithmetic cohomology
claim is made.  The universal proof appears in the companion D05 PsiBound audit.
"""


def run():
    from math import factorial

    checked = 0
    # Bound originally: bnd(F, k) = 16 * F^(k+1) * k!
    # Claim for 1<= e+1<=t, t>=2, F>=1:
    # bnd(F,e+1) <= (t*F)^(2*t+5).
    for f in range(1, 33):
        for t in range(2, 51):
            upper = pow(t * f, 2 * t + 5)
            for e in range(t):
                k = e + 1
                lower = 16 * pow(f, k + 1) * factorial(k)
                assert lower <= upper, (f, t, e)
                checked += 1

    # Controls that violate the required t>=2 / k<=t hypotheses:
    assert 16 * 1**2 * factorial(1) > (1 * 1) ** (2 * 1 + 5)
    assert 16 * 1**(8 + 1) * factorial(8) > (2 * 1) ** (2 * 2 + 5)
    print(f"PASS: {checked} exact integer bound instances; two invalid-premise controls rejected")


if __name__ == "__main__":
    run()
