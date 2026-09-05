"""ASP-WP01 exact finite-laboratory tests."""

from __future__ import annotations

import math
import unittest

from domains.adaptive_spectral_peeling.finite_lab import (
    FiniteProductSpace,
    adversarial_regimes,
    all_nontrivial_restrictions,
    basis_orthonormality_error,
    branch_margin,
    exact_treewidth,
    l2_tail_energy,
    level_influence,
    noisy_observations,
    objective_from_coefficients,
    primal_graph,
    random_spectral_coefficients,
    restrict_table,
    restricted_supnorm_residual,
    spectral_coefficients,
    transported_coefficient,
    weighted_l1_tail_envelope,
    expected_tail_after_single_restriction,
)
from domains.adaptive_spectral_peeling.replay_wp01 import run_replay


TOL = 1e-10


class AdaptiveSpectralPeelingWP01Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.space = FiniteProductSpace((2, 3, 2))
        self.coefficients = random_spectral_coefficients(
            self.space, seed=20260830, density=0.7, scale=0.8
        )
        self.values = objective_from_coefficients(
            self.space, self.coefficients
        )

    def test_mixed_categorical_basis_is_orthonormal(self) -> None:
        self.assertLessEqual(basis_orthonormality_error(self.space), TOL)

    def test_full_spectral_reconstruction(self) -> None:
        recovered = spectral_coefficients(self.space, self.values)
        error = max(
            abs(recovered[alpha] - self.coefficients[alpha])
            for alpha in self.coefficients
        )
        self.assertLessEqual(error, TOL)

    def test_t1_every_nontrivial_restriction(self) -> None:
        for restriction in all_nontrivial_restrictions(self.space):
            _, residual_space, residual_values = restrict_table(
                self.space, self.values, restriction
            )
            self.assertIsNotNone(residual_space)
            assert residual_space is not None
            recovered = spectral_coefficients(
                residual_space, residual_values
            )
            for beta, observed in recovered.items():
                with self.subTest(restriction=restriction, beta=beta):
                    predicted = transported_coefficient(
                        self.space,
                        self.coefficients,
                        restriction,
                        beta,
                    )
                    self.assertAlmostEqual(
                        observed, predicted, delta=TOL
                    )

    def test_t2_tail_decrement_equals_boundary_influence(self) -> None:
        degree_cutoff = 1
        original_tail = l2_tail_energy(
            self.coefficients, degree_cutoff
        )
        for coordinate in range(self.space.n):
            with self.subTest(coordinate=coordinate):
                observed = original_tail - expected_tail_after_single_restriction(
                    self.space,
                    self.values,
                    coordinate,
                    degree_cutoff,
                )
                predicted = level_influence(
                    self.coefficients,
                    coordinate,
                    degree_cutoff + 1,
                )
                self.assertAlmostEqual(observed, predicted, delta=TOL)

    def test_t3_tail_envelope_is_never_violated(self) -> None:
        for restriction in all_nontrivial_restrictions(self.space):
            _, residual_space, residual_values = restrict_table(
                self.space, self.values, restriction
            )
            assert residual_space is not None
            residual = restricted_supnorm_residual(
                residual_space, residual_values, max_degree=1
            )
            envelope = weighted_l1_tail_envelope(
                self.space,
                self.coefficients,
                max_degree=1,
                restricted_coordinates=tuple(restriction),
            )
            with self.subTest(restriction=restriction):
                self.assertLessEqual(residual, envelope + TOL)

    def test_known_treewidth_fixtures(self) -> None:
        regimes = adversarial_regimes()
        path_space, path_coefficients, _, _ = regimes["path_width"]
        clique_space, clique_coefficients, _, _ = regimes["clique_width"]
        path_width = exact_treewidth(
            primal_graph(path_space.n, path_coefficients, threshold=0.1)
        )
        clique_width = exact_treewidth(
            primal_graph(clique_space.n, clique_coefficients, threshold=0.1)
        )
        self.assertEqual(path_width, 1)
        self.assertEqual(clique_width, 5)

    def test_influence_and_margin_are_not_conflated(self) -> None:
        regimes = adversarial_regimes()

        high_space, high_coefficients, d, coordinate = regimes[
            "high_influence_zero_margin"
        ]
        high_values = objective_from_coefficients(
            high_space, high_coefficients
        )
        self.assertGreater(
            level_influence(high_coefficients, coordinate, d + 1), 3.9
        )
        self.assertAlmostEqual(
            branch_margin(high_space, high_values, coordinate),
            0.0,
            delta=TOL,
        )

        margin_space, margin_coefficients, d, coordinate = regimes[
            "large_margin_weak_boundary"
        ]
        margin_values = objective_from_coefficients(
            margin_space, margin_coefficients
        )
        self.assertGreater(
            branch_margin(margin_space, margin_values, coordinate),
            2.9,
        )
        self.assertAlmostEqual(
            level_influence(margin_coefficients, coordinate, d + 1),
            0.0,
            delta=TOL,
        )

    def test_l2_and_weighted_l1_tail_can_separate(self) -> None:
        space, coefficients, degree_cutoff, _ = adversarial_regimes()[
            "diffuse_l2_vs_l1_tail"
        ]
        tau2 = math.sqrt(l2_tail_energy(coefficients, degree_cutoff))
        tau_inf = weighted_l1_tail_envelope(
            space, coefficients, degree_cutoff
        )
        self.assertGreaterEqual(tau_inf, 4.0 * tau2)

    def test_noisy_observations_are_seeded_and_non_authoritative(self) -> None:
        first = noisy_observations(
            self.space, self.values, sigma=0.1, seed=17
        )
        second = noisy_observations(
            self.space, self.values, sigma=0.1, seed=17
        )
        third = noisy_observations(
            self.space, self.values, sigma=0.1, seed=18
        )
        self.assertEqual(first, second)
        self.assertNotEqual(first, third)

    def test_deterministic_replay_passes(self) -> None:
        result = run_replay()
        self.assertTrue(result["passed"])


if __name__ == "__main__":
    unittest.main()
