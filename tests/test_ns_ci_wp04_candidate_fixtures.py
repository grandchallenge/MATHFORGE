import unittest
from fractions import Fraction


class NSCIWP04CandidateFixtureTests(unittest.TestCase):
    def test_a2_dissipation_wavenumber_exponent_is_critical(self) -> None:
        # Lambda_lambda(t) = lambda * Lambda(lambda^2 t), so the L^p_t
        # integral scales by lambda^(p-2).
        p = Fraction(2, 1)
        self.assertEqual(p - 2, 0)
        self.assertGreater(Fraction(5, 2) - 2, 0)
        self.assertLess(Fraction(1, 1) - 2, 0)

    def test_a2_naive_product_of_l1_coefficients_can_diverge(self) -> None:
        # f(t)=g(t)=t^(-2/3) are each integrable on (0,1), while
        # f(t)g(t)=t^(-4/3) is not. This rejects a closure that combines
        # Lambda^2 in L^1_t and the energy dissipation density in L^1_t
        # by multiplication alone.
        alpha = Fraction(2, 3)
        beta = Fraction(2, 3)
        self.assertLess(alpha, 1)
        self.assertLess(beta, 1)
        self.assertGreaterEqual(alpha + beta, 1)

    def test_a2_low_frequency_bound_has_unclosed_product_structure(self) -> None:
        # In three dimensions, Bernstein L^2 -> L^6 costs one power of
        # the cutoff. Combining the cutoff and energy estimates yields the
        # schematic factor Lambda^2 * ||u||_2^2 * ||grad u||_2^2.
        dimension = 3
        bernstein_power = dimension * (Fraction(1, 2) - Fraction(1, 6))
        self.assertEqual(bernstein_power, 1)
        self.assertEqual(2 * bernstein_power, 2)

    def test_d1_compensated_interface_is_scale_covariant(self) -> None:
        # Pi_K and nu||Delta u^K||_2^2 scale like lambda^3.
        # ||grad u^K||_2^2 scales like lambda, hence a must scale like
        # lambda^2. Its time integral is then invariant.
        flux_power = 3
        laplacian_energy_power = 3
        gradient_energy_power = 1
        coefficient_power = flux_power - gradient_energy_power
        self.assertEqual(flux_power, laplacian_energy_power)
        self.assertEqual(coefficient_power, 2)
        self.assertEqual(coefficient_power - 2, 0)

    def test_d1_cutoff_must_transform_under_scaling(self) -> None:
        # For dyadic lambda=2^m, the cutoff index transforms N -> N+m.
        n = 7
        m = 3
        self.assertEqual(n + m, 10)
        self.assertNotEqual(n, n + m)

    def test_e1_pointwise_bounds_do_not_imply_uniform_bound(self) -> None:
        # Each approximant may have a finite bound K_n while sup_n K_n is
        # infinite. The bridge requires exists K_T, forall n, not the
        # reversed quantifier order.
        pointwise_bounds = list(range(1, 101))
        self.assertTrue(all(bound < float("inf") for bound in pointwise_bounds))
        self.assertEqual(max(pointwise_bounds), 100)
        self.assertGreater(max(pointwise_bounds), pointwise_bounds[0])

    def test_shortlist_has_three_distinct_roles(self) -> None:
        shortlist = {
            "NS-CI-R014-A2": "critical criterion",
            "NS-CI-R014-D1": "mechanism interface",
            "NS-CI-R014-E1": "data-class bridge",
        }
        self.assertEqual(len(shortlist), 3)
        self.assertEqual(len(set(shortlist.values())), 3)


if __name__ == "__main__":
    unittest.main()
