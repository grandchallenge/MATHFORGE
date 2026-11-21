#!/usr/bin/env python3
"""RH-A26 isolated finite smoke check of the author's error-dominance inequality.

Reference: original pinned
Development/AutomorphicArithmetic/AutomorphicVarieties/
CMFieldExponentialBounds/ErrorTermsLeSqrtExpRpow.lean.

This verifies selected numerical instances in log space, not a theorem,
original Lean replay, or any estimate for cohomological Selmer/Sha lengths.
"""
import math


def logsumexp(values):
    top = max(values)
    return top + math.log(sum(math.exp(v - top) for v in values))


def test_positive_example():
    # eps > 0; K,C > 0; write r = x^(eps/5), so
    # x^(eps/4) = r^(5/4), x^(4eps/5) = r^4,
    # x^eps/2 = r^5/2. Set log u = 2*x^(eps/4).
    eps, k, c = 0.01, 2.0, 5.0
    n = math.log(2) + abs(c) + abs(k) + 1
    d = 9 + 2 * abs(c)
    threshold_r = 2 * (d + math.log(n) + 1)
    assert eps > 0 and threshold_r > 0

    def margin(r):
        a = r ** (5 / 4)
        b = r ** 4
        left_log = logsumexp([
            b + math.log(math.log(2)),
            8 * a + math.log(k),
            2 * c * a,
            b + math.log(c),
        ])
        right_log = r ** 5 / 2
        return right_log - left_log

    # Failure before the "sufficiently large x" gate is informative.
    assert margin(2.0) < 0
    for r in (math.ceil(threshold_r), math.ceil(threshold_r) + 3):
        assert r >= threshold_r
        assert margin(r) > 0
    print("PASS: log-domain checks satisfy the explicit asymptotic gate")
    print("eps=", eps, "K=", k, "C=", c, "threshold r=", threshold_r)
    print("margins at r=2,45,48:", *[round(margin(r), 3) for r in (2, 45, 48)])


if __name__ == "__main__":
    test_positive_example()
