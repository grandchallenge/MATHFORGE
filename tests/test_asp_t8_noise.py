from __future__ import annotations

import itertools
import math
import unittest

from domains.adaptive_spectral_peeling.finite_lab import FiniteProductSpace, objective_from_coefficients
from domains.adaptive_spectral_peeling.replay_t8_noise import (
    loglog_slope,
    minimum_m_for_sd_threshold,
)
from domains.adaptive_spectral_peeling.t8_noise import (
    degree_indices,
    exact_l2_energy,
    exact_null_variance,
    kernel_diagonal_sup,
    kernel_hilbert_schmidt_sq,
    predictor_p0,
    predictor_p1,
    t6_energy_threshold,
    u_statistic_energy,
)


class AspT8NoiseTests(unittest.TestCase):
    def test_projection_kernel_hilbert_schmidt_identity(self) -> None:
        space = FiniteProductSpace((2, 2, 2))
        indices = degree_indices(space, 1)
        self.assertEqual(len(indices), 4)
        self.assertAlmostEqual(kernel_diagonal_sup(space, indices), 4.0, places=12)
        self.assertAlmostEqual(kernel_hilbert_schmidt_sq(space, indices), 4.0, places=12)

    def test_u_statistic_unbiasedness_by_exact_enumeration(self) -> None:
        space = FiniteProductSpace((2, 2))
        indices = degree_indices(space, 1)
        # Residual lies in V_{<=1}.
        residual = objective_from_coefficients(
            space,
            {
                (0, 0): 0.10,
                (1, 0): 0.20,
                (0, 1): -0.15,
                (1, 1): 0.0,
            },
        )
        mu = exact_l2_energy(residual)
        points = tuple(space.points())
        noises = (-0.3, 0.3)  # centered bounded sub-Gaussian fixture
        total = 0.0
        count = 0
        for x1, x2, e1, e2 in itertools.product(points, points, noises, noises):
            total += u_statistic_energy(
                space,
                indices,
                ((x1, residual[x1] + e1), (x2, residual[x2] + e2)),
            )
            count += 1
        self.assertAlmostEqual(total / count, mu, places=12)

    def test_exact_null_variance_by_exhaustive_finite_confrontation(self) -> None:
        space = FiniteProductSpace((2, 2))
        indices = degree_indices(space, 1)
        c = len(indices)
        points = tuple(space.points())
        sigma = 0.25
        noises = (-sigma, sigma)
        m = 3
        values = []
        for xs in itertools.product(points, repeat=m):
            for es in itertools.product(noises, repeat=m):
                observations = tuple((x, e) for x, e in zip(xs, es))
                values.append(u_statistic_energy(space, indices, observations))
        empirical_mean = sum(values) / len(values)
        empirical_variance = sum((value - empirical_mean) ** 2 for value in values) / len(values)
        predicted = exact_null_variance(sigma**2, c, m)
        self.assertAlmostEqual(empirical_mean, 0.0, places=12)
        self.assertAlmostEqual(empirical_variance, predicted, places=12)

    def test_noise_predictor_has_three_halves_c_exponent(self) -> None:
        gamma = 0.5
        sigma = 0.2
        c1, c2 = 4.0, 16.0
        self.assertAlmostEqual(predictor_p0(c2, gamma) / predictor_p0(c1, gamma), 4.0)
        self.assertAlmostEqual(predictor_p1(c2, gamma, sigma) / predictor_p1(c1, gamma, sigma), 8.0)

    def test_exact_null_cost_sweep_confronts_three_halves_exponent(self) -> None:
        gamma = 1.0
        sigma = 0.25
        dimensions = [2, 4, 8, 16, 32, 64, 128]
        costs = [minimum_m_for_sd_threshold(c, gamma, sigma) for c in dimensions]
        self.assertEqual(costs, [9, 24, 65, 182, 513, 1449, 4097])
        slope = loglog_slope(
            [float(c) for c in dimensions[2:]],
            [float(m) for m in costs[2:]],
        )
        self.assertGreater(slope, 1.48)
        self.assertLess(slope, 1.51)

    def test_t6_energy_threshold(self) -> None:
        gamma = 0.8
        c = 10.0
        threshold = t6_energy_threshold(gamma, c)
        self.assertAlmostEqual(math.sqrt(c * threshold), gamma / 4.0)


if __name__ == "__main__":
    unittest.main()
