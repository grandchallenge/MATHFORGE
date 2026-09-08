"""Finite machinery for ASP-T8-NOISE-002.

Reconnaissance only.  The functions here expose exact finite identities and the
conservative median-of-blocks certificate derived in ASP_T8_NOISE_002.md.
"""

from __future__ import annotations

import math
import statistics
from typing import Mapping, Sequence, Tuple

from .finite_lab import FiniteProductSpace, Point, basis_value, degree

MultiIndex = Tuple[int, ...]
Observation = Tuple[Point, float]


def _require_finite(value: float, label: str) -> float:
    try:
        finite = math.isfinite(value)
    except TypeError as error:
        raise ValueError(f"{label} must be a finite real number") from error
    if not finite:
        raise ValueError(f"{label} must be finite")
    return value


def degree_indices(space: FiniteProductSpace, max_degree: int) -> Tuple[MultiIndex, ...]:
    return tuple(alpha for alpha in space.multiindices() if degree(alpha) <= max_degree)


def kernel_value(
    space: FiniteProductSpace,
    indices: Sequence[MultiIndex],
    x: Point,
    y: Point,
) -> float:
    return sum(basis_value(space, alpha, x) * basis_value(space, alpha, y) for alpha in indices)


def kernel_diagonal_sup(
    space: FiniteProductSpace, indices: Sequence[MultiIndex]
) -> float:
    return max(kernel_value(space, indices, x, x) for x in space.points())


def kernel_hilbert_schmidt_sq(
    space: FiniteProductSpace, indices: Sequence[MultiIndex]
) -> float:
    """E[K(X,X')^2] under the uniform product measure."""
    points = tuple(space.points())
    total = sum(kernel_value(space, indices, x, y) ** 2 for x in points for y in points)
    return total / (space.size * space.size)


def exact_l2_energy(values: Mapping[Point, float]) -> float:
    if not values:
        raise ValueError("at least one residual value is required")
    result = sum(
        _require_finite(value, f"residual value at {point}") ** 2
        for point, value in values.items()
    ) / len(values)
    return _require_finite(result, "exact L2 energy")


def u_statistic_energy(
    space: FiniteProductSpace,
    indices: Sequence[MultiIndex],
    observations: Sequence[Observation],
) -> float:
    m = len(observations)
    if m < 2:
        raise ValueError("at least two holdout observations are required")
    total = 0.0
    for i, (x_i, z_i) in enumerate(observations):
        _require_finite(z_i, f"observation {i}")
        for j, (x_j, z_j) in enumerate(observations):
            if i == j:
                continue
            _require_finite(z_j, f"observation {j}")
            total += z_i * z_j * kernel_value(space, indices, x_i, x_j)
    return _require_finite(total / (m * (m - 1)), "U-statistic energy")


def exact_null_variance(noise_variance: float, certificate_dimension: int, m: int) -> float:
    """Exact variance at r=0 for homoscedastic independent centered noise."""
    if m < 2:
        raise ValueError("m must be at least two")
    if certificate_dimension < 1:
        raise ValueError("certificate_dimension must be positive")
    _require_finite(noise_variance, "noise_variance")
    if noise_variance < 0.0:
        raise ValueError("noise_variance must be nonnegative")
    return _require_finite(
        2.0 * noise_variance**2 * certificate_dimension / (m * (m - 1)),
        "exact null variance",
    )


def block_variance_upper_bound(
    mu: float,
    q: int,
    residual_bound: float,
    sigma: float,
    certificate_dimension: int,
    lambda_diag: float,
) -> float:
    """Variance upper bound for one q-sample kernel U-statistic block."""
    if q < 2:
        raise ValueError("q must be at least two")
    for value, label in (
        (mu, "mu"),
        (residual_bound, "residual_bound"),
        (sigma, "sigma"),
        (lambda_diag, "lambda_diag"),
    ):
        _require_finite(value, label)
    if mu < 0.0 or residual_bound < 0.0 or sigma < 0.0:
        raise ValueError("mu, residual_bound, and sigma must be nonnegative")
    if certificate_dimension < 1 or lambda_diag <= 0.0:
        raise ValueError("certificate_dimension and lambda_diag must be positive")
    first = 4.0 * (residual_bound**2 + sigma**2) * mu / q
    second = 2.0 * (
        sigma**4 * certificate_dimension
        + (2.0 * sigma**2 + residual_bound**2) * lambda_diag * mu
    ) / (q * (q - 1))
    return _require_finite(first + second, "block variance upper bound")


def noisy_energy_ucb_from_block_median(
    block_estimates: Sequence[float],
    q: int,
    residual_bound: float,
    sigma: float,
    certificate_dimension: int,
    lambda_diag: float,
) -> float:
    """Explicit T8 noisy UCB from the median of independent q-sample blocks."""
    if not block_estimates:
        raise ValueError("at least one block estimate is required")
    if len(block_estimates) % 2 == 0:
        raise ValueError("an odd number of independent block estimates is required")
    if q < 2:
        raise ValueError("q must be at least two")
    for index, estimate in enumerate(block_estimates):
        _require_finite(estimate, f"block estimate {index}")
    for value, label in (
        (residual_bound, "residual_bound"),
        (sigma, "sigma"),
        (lambda_diag, "lambda_diag"),
    ):
        _require_finite(value, label)
    if residual_bound < 0.0 or sigma < 0.0:
        raise ValueError("residual_bound and sigma must be nonnegative")
    if certificate_dimension < 1 or lambda_diag <= 0.0:
        raise ValueError("certificate_dimension and lambda_diag must be positive")
    median = statistics.median(block_estimates)
    a_q = 4.0 * (residual_bound**2 + sigma**2) + (
        4.0 * (2.0 * sigma**2 + residual_bound**2) * lambda_diag / q
    )
    d = 4.0 * sigma**4 * certificate_dimension
    result = 2.0 * max(median, 0.0) + 4.0 * a_q / q + 4.0 * math.sqrt(d) / q
    return _require_finite(max(0.0, result), "noisy energy UCB")


def required_odd_block_count(delta: float) -> int:
    """Smallest odd B >= 8 log(1/delta), from the block-median Hoeffding step."""
    _require_finite(delta, "delta")
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie in (0,1)")
    b = max(1, math.ceil(8.0 * math.log(1.0 / delta)))
    return b if b % 2 else b + 1


def t6_energy_threshold(branch_margin: float, lambda_diag: float) -> float:
    """Energy threshold sufficient for epsilon=sqrt(Lambda*mu) < Gamma/4."""
    _require_finite(branch_margin, "branch_margin")
    _require_finite(lambda_diag, "lambda_diag")
    if branch_margin <= 0.0 or lambda_diag <= 0.0:
        raise ValueError("branch_margin and lambda_diag must be positive")
    return branch_margin**2 / (16.0 * lambda_diag)


def predictor_p0(certificate_dimension: float, branch_margin: float) -> float:
    _require_finite(certificate_dimension, "certificate_dimension")
    _require_finite(branch_margin, "branch_margin")
    if certificate_dimension <= 0.0 or branch_margin <= 0.0:
        raise ValueError("certificate_dimension and branch_margin must be positive")
    return certificate_dimension / branch_margin**2


def predictor_p1(
    certificate_dimension: float, branch_margin: float, sigma: float
) -> float:
    _require_finite(sigma, "sigma")
    if sigma < 0.0:
        raise ValueError("sigma must be nonnegative")
    predictor_p0(certificate_dimension, branch_margin)
    return sigma**2 * certificate_dimension**1.5 / branch_margin**2


def predictor_combined(
    certificate_dimension: float,
    branch_margin: float,
    sigma: float,
    residual_bound: float,
) -> float:
    _require_finite(residual_bound, "residual_bound")
    if residual_bound < 0.0:
        raise ValueError("residual_bound must be nonnegative")
    return residual_bound**2 * predictor_p0(
        certificate_dimension, branch_margin
    ) + predictor_p1(certificate_dimension, branch_margin, sigma)


def full_space_null_u_statistic(
    domain_size: int, samples: Sequence[Tuple[int, float]]
) -> float:
    """Fast full-space kernel U-statistic, K(x,y)=M*1{x=y}."""
    m = len(samples)
    if m < 2:
        raise ValueError("at least two samples are required")
    if domain_size < 1:
        raise ValueError("domain_size must be positive")
    sums = [0.0] * domain_size
    sumsq = [0.0] * domain_size
    for x, noise in samples:
        if x < 0 or x >= domain_size:
            raise ValueError("sample point is outside the domain")
        _require_finite(noise, f"noise at point {x}")
        sums[x] += noise
        sumsq[x] += noise * noise
    ordered_cross = sum(total * total - sq for total, sq in zip(sums, sumsq))
    return _require_finite(
        domain_size * ordered_cross / (m * (m - 1)),
        "full-space null U-statistic",
    )
