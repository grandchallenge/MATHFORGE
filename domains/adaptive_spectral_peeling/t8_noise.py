"""Finite machinery for ASP-T8-NOISE-002.

Reconnaissance only.  The functions here expose exact finite identities and the
conservative median-of-blocks certificate derived in ASP_T8_NOISE_002.md.
"""

from __future__ import annotations

import itertools
import math
import statistics
from typing import Iterable, Mapping, Sequence, Tuple

from .finite_lab import FiniteProductSpace, Point, basis_value, degree

MultiIndex = Tuple[int, ...]
Observation = Tuple[Point, float]


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
    return sum(value * value for value in values.values()) / len(values)


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
        for j, (x_j, z_j) in enumerate(observations):
            if i == j:
                continue
            total += z_i * z_j * kernel_value(space, indices, x_i, x_j)
    return total / (m * (m - 1))


def exact_null_variance(noise_variance: float, certificate_dimension: int, m: int) -> float:
    """Exact variance at r=0 for homoscedastic independent centered noise."""
    if m < 2:
        raise ValueError("m must be at least two")
    if certificate_dimension < 1:
        raise ValueError("certificate_dimension must be positive")
    return 2.0 * noise_variance**2 * certificate_dimension / (m * (m - 1))


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
    first = 4.0 * (residual_bound**2 + sigma**2) * mu / q
    second = 2.0 * (
        sigma**4 * certificate_dimension
        + (2.0 * sigma**2 + residual_bound**2) * lambda_diag * mu
    ) / (q * (q - 1))
    return first + second


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
    if q < 2:
        raise ValueError("q must be at least two")
    median = statistics.median(block_estimates)
    a_q = 4.0 * (residual_bound**2 + sigma**2) + (
        4.0 * (2.0 * sigma**2 + residual_bound**2) * lambda_diag / q
    )
    d = 4.0 * sigma**4 * certificate_dimension
    return max(0.0, 2.0 * max(median, 0.0) + 4.0 * a_q / q + 4.0 * math.sqrt(d) / q)


def required_odd_block_count(delta: float) -> int:
    """Smallest odd B >= 8 log(1/delta), from the block-median Hoeffding step."""
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie in (0,1)")
    b = max(1, math.ceil(8.0 * math.log(1.0 / delta)))
    return b if b % 2 else b + 1


def t6_energy_threshold(branch_margin: float, lambda_diag: float) -> float:
    """Energy threshold sufficient for epsilon=sqrt(Lambda*mu) < Gamma/4."""
    if branch_margin <= 0.0 or lambda_diag <= 0.0:
        raise ValueError("branch_margin and lambda_diag must be positive")
    return branch_margin**2 / (16.0 * lambda_diag)


def predictor_p0(certificate_dimension: float, branch_margin: float) -> float:
    return certificate_dimension / branch_margin**2


def predictor_p1(
    certificate_dimension: float, branch_margin: float, sigma: float
) -> float:
    return sigma**2 * certificate_dimension**1.5 / branch_margin**2


def predictor_combined(
    certificate_dimension: float,
    branch_margin: float,
    sigma: float,
    residual_bound: float,
) -> float:
    return (
        residual_bound**2 * certificate_dimension
        + sigma**2 * certificate_dimension**1.5
    ) / branch_margin**2


def full_space_null_u_statistic(
    domain_size: int, samples: Sequence[Tuple[int, float]]
) -> float:
    """Fast full-space kernel U-statistic, K(x,y)=M*1{x=y}."""
    m = len(samples)
    if m < 2:
        raise ValueError("at least two samples are required")
    sums = [0.0] * domain_size
    sumsq = [0.0] * domain_size
    for x, noise in samples:
        sums[x] += noise
        sumsq[x] += noise * noise
    ordered_cross = sum(total * total - sq for total, sq in zip(sums, sumsq))
    return domain_size * ordered_cross / (m * (m - 1))
