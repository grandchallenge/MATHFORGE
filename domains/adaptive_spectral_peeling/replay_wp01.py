"""Deterministic ASP-WP01 invariant replay.

Run from the MATHFORGE repository root:

    python domains/adaptive_spectral_peeling/replay_wp01.py
"""

from __future__ import annotations

import json
import math
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from domains.adaptive_spectral_peeling.finite_lab import (
    FiniteProductSpace,
    adversarial_regimes,
    all_nontrivial_restrictions,
    basis_orthonormality_error,
    instance_metrics,
    l2_tail_energy,
    level_influence,
    objective_from_coefficients,
    random_spectral_coefficients,
    restrict_table,
    restricted_supnorm_residual,
    spectral_coefficients,
    transported_coefficient,
    weighted_l1_tail_envelope,
    expected_tail_after_single_restriction,
)


TOLERANCE = 1e-10
SEED = 170600764


def run_replay() -> dict:
    space = FiniteProductSpace((2, 3, 2))
    source_coefficients = random_spectral_coefficients(
        space, seed=SEED, density=0.72, scale=0.9
    )
    values = objective_from_coefficients(space, source_coefficients)
    recovered = spectral_coefficients(space, values)

    basis_error = basis_orthonormality_error(space)
    reconstruction_error = max(
        abs(recovered[alpha] - source_coefficients[alpha])
        for alpha in source_coefficients
    )

    # T1: every nonempty, non-full restriction and every residual coefficient.
    t1_error = 0.0
    restriction_count = 0
    coefficient_comparisons = 0
    for restriction in all_nontrivial_restrictions(space):
        restriction_count += 1
        _, residual_space, residual_values = restrict_table(space, values, restriction)
        assert residual_space is not None
        restricted_coefficients = spectral_coefficients(
            residual_space, residual_values
        )
        for beta, observed in restricted_coefficients.items():
            predicted = transported_coefficient(
                space, source_coefficients, restriction, beta
            )
            t1_error = max(t1_error, abs(observed - predicted))
            coefficient_comparisons += 1

    # T2: exact average over every value of every coordinate.
    original_tail = l2_tail_energy(source_coefficients, max_degree=1)
    t2_error = 0.0
    for coordinate in range(space.n):
        observed_decrement = original_tail - expected_tail_after_single_restriction(
            space, values, coordinate, max_degree=1
        )
        predicted_decrement = level_influence(
            source_coefficients, coordinate, level=2
        )
        t2_error = max(
            t2_error, abs(observed_decrement - predicted_decrement)
        )

    # T3: enumerate every nontrivial restriction and compare actual residual to
    # the assignment-independent weighted spectral envelope.
    t3_max_violation = -math.inf
    t3_largest_residual = 0.0
    t3_smallest_slack = math.inf
    for restriction in all_nontrivial_restrictions(space):
        _, residual_space, residual_values = restrict_table(space, values, restriction)
        assert residual_space is not None
        residual = restricted_supnorm_residual(
            residual_space, residual_values, max_degree=1
        )
        envelope = weighted_l1_tail_envelope(
            space,
            source_coefficients,
            max_degree=1,
            restricted_coordinates=tuple(restriction),
        )
        t3_max_violation = max(t3_max_violation, residual - envelope)
        t3_largest_residual = max(t3_largest_residual, residual)
        t3_smallest_slack = min(t3_smallest_slack, envelope - residual)

    regimes = {}
    for name, (regime_space, coefficients, degree_cutoff, branch_coordinate) in adversarial_regimes().items():
        regimes[name] = instance_metrics(
            regime_space,
            coefficients,
            max_degree=degree_cutoff,
            heavy_threshold=0.1,
            branch_coordinate=branch_coordinate,
            sigma=0.05,
        )

    structural_checks = {
        "large_influence_zero_margin": (
            regimes["high_influence_zero_margin"]["max_boundary_influence"] >= 3.9
            and regimes["high_influence_zero_margin"]["branch_margin"] <= TOLERANCE
        ),
        "large_margin_weak_boundary": (
            regimes["large_margin_weak_boundary"]["branch_margin"] >= 2.9
            and regimes["large_margin_weak_boundary"]["max_boundary_influence"] <= TOLERANCE
        ),
        "l2_vs_l1_tail_separated": (
            regimes["diffuse_l2_vs_l1_tail"]["tau_inf_envelope"]
            >= 4.0 * regimes["diffuse_l2_vs_l1_tail"]["tau2"]
        ),
        "path_treewidth_one": regimes["path_width"]["treewidth"] == 1,
        "clique_treewidth_five": regimes["clique_width"]["treewidth"] == 5,
    }

    passed = (
        basis_error <= TOLERANCE
        and reconstruction_error <= TOLERANCE
        and t1_error <= TOLERANCE
        and t2_error <= TOLERANCE
        and t3_max_violation <= TOLERANCE
        and all(structural_checks.values())
    )

    return {
        "work_package": "ASP-WP01",
        "campaign_candidate": "ASP-001",
        "scope": "finite_uniform_product_spaces",
        "seed": SEED,
        "tolerance": TOLERANCE,
        "basis_orthonormality_max_error": basis_error,
        "spectral_reconstruction_max_error": reconstruction_error,
        "t1": {
            "max_error": t1_error,
            "restriction_count": restriction_count,
            "coefficient_comparisons": coefficient_comparisons,
        },
        "t2": {"max_error": t2_error},
        "t3": {
            "max_residual_minus_envelope": t3_max_violation,
            "largest_actual_residual": t3_largest_residual,
            "smallest_envelope_slack": t3_smallest_slack,
        },
        "adversarial_regimes": regimes,
        "structural_checks": structural_checks,
        "passed": passed,
        "claim_boundary": (
            "Finite computational confrontation only; passing does not certify "
            "T1-T7, novelty, or a mathematical theorem."
        ),
    }


def main() -> int:
    result = run_replay()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
