"""Deterministic finite confrontation for ASP-T8-NOISE-002.

The confrontation uses the exact r=0 variance identity of the kernel U-statistic
to compare the original C/Gamma^2 predictor with the noise-dominated
sigma^2*C^(3/2)/Gamma^2 predictor.  No random fitting is involved.
"""

from __future__ import annotations

import math

from .t8_noise import exact_null_variance, t6_energy_threshold


def minimum_m_for_sd_threshold(c: int, gamma: float, sigma: float, z: float = 2.0) -> int:
    """Smallest m with z*SD(U_m) <= Gamma^2/(16 C) at the exact-surrogate null."""
    threshold = t6_energy_threshold(gamma, c)
    noise_variance = sigma * sigma
    m = 2
    while z * math.sqrt(exact_null_variance(noise_variance, c, m)) > threshold:
        m += 1
    return m


def loglog_slope(xs: list[float], ys: list[float]) -> float:
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    numerator = sum((x - mx) * (y - my) for x, y in zip(lx, ly))
    denominator = sum((x - mx) ** 2 for x in lx)
    return numerator / denominator


def main() -> None:
    gamma = 1.0
    sigma = 0.25
    dimensions = [2, 4, 8, 16, 32, 64, 128]
    costs = [minimum_m_for_sd_threshold(c, gamma, sigma) for c in dimensions]
    slope = loglog_slope([float(c) for c in dimensions[2:]], [float(m) for m in costs[2:]])

    print("ASP-T8-NOISE-002 exact-null confrontation")
    print(f"gamma={gamma} sigma={sigma}")
    print("C,m,P0=C/Gamma^2,P1=sigma^2*C^(3/2)/Gamma^2")
    for c, m in zip(dimensions, costs):
        p0 = c / gamma**2
        p1 = sigma**2 * c**1.5 / gamma**2
        print(f"{c},{m},{p0:.8g},{p1:.8g}")
    print(f"loglog_slope_m_vs_C={slope:.6f}")
    print("expected_noise_dominated_exponent=1.5")


if __name__ == "__main__":
    main()
