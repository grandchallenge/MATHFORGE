"""Exact finite product-space laboratory for ASP-WP01.

This module is deliberately dependency-free.  It provides exhaustive ground truth
for finite *uniform* product measures.  It is reconnaissance machinery, not a
mathematical certification layer.
"""

from __future__ import annotations

from dataclasses import dataclass
import itertools
import math
import random
from typing import Dict, Iterable, Mapping, Sequence, Tuple

Point = Tuple[int, ...]
MultiIndex = Tuple[int, ...]
CoefficientMap = Dict[MultiIndex, float]
ValueTable = Dict[Point, float]


@dataclass(frozen=True)
class FiniteProductSpace:
    """A finite uniform product space with coordinates encoded as 0..m_i-1."""

    cardinalities: Tuple[int, ...]

    def __post_init__(self) -> None:
        if not self.cardinalities:
            raise ValueError("a product space must have at least one coordinate")
        if any(m < 2 for m in self.cardinalities):
            raise ValueError("every coordinate must contain at least two values")

    @property
    def n(self) -> int:
        return len(self.cardinalities)

    @property
    def size(self) -> int:
        result = 1
        for m in self.cardinalities:
            result *= m
        return result

    def points(self) -> Iterable[Point]:
        return itertools.product(*(range(m) for m in self.cardinalities))

    def multiindices(self) -> Iterable[MultiIndex]:
        return itertools.product(*(range(m) for m in self.cardinalities))


def coordinate_basis(cardinality: int) -> Tuple[Tuple[float, ...], ...]:
    """Return a real orthonormal basis for a uniform categorical coordinate.

    Row 0 is the constant function.  Rows 1..m-1 are scaled Helmert contrasts.
    Orthonormality is with respect to the uniform probability measure.
    """

    if cardinality < 2:
        raise ValueError("cardinality must be at least two")

    rows = [tuple(1.0 for _ in range(cardinality))]
    for k in range(1, cardinality):
        scale = math.sqrt(cardinality / (k * (k + 1)))
        row = []
        for value in range(cardinality):
            if value < k:
                row.append(scale)
            elif value == k:
                row.append(-k * scale)
            else:
                row.append(0.0)
        rows.append(tuple(row))
    return tuple(rows)


def basis_tables(space: FiniteProductSpace) -> Tuple[Tuple[Tuple[float, ...], ...], ...]:
    return tuple(coordinate_basis(m) for m in space.cardinalities)


def support(alpha: MultiIndex) -> Tuple[int, ...]:
    return tuple(i for i, value in enumerate(alpha) if value != 0)


def degree(alpha: MultiIndex) -> int:
    return sum(value != 0 for value in alpha)


def basis_value(space: FiniteProductSpace, alpha: MultiIndex, point: Point) -> float:
    if len(alpha) != space.n or len(point) != space.n:
        raise ValueError("basis multi-index and point must match product dimension")
    tables = basis_tables(space)
    result = 1.0
    for i, basis_index in enumerate(alpha):
        result *= tables[i][basis_index][point[i]]
    return result


def basis_supnorm(space: FiniteProductSpace, alpha: MultiIndex) -> float:
    tables = basis_tables(space)
    result = 1.0
    for i, basis_index in enumerate(alpha):
        result *= max(abs(v) for v in tables[i][basis_index])
    return result


def spectral_coefficients(space: FiniteProductSpace, values: Mapping[Point, float]) -> CoefficientMap:
    """Compute every tensor-product coefficient by exact finite enumeration."""

    _validate_complete_table(space, values)
    inv_size = 1.0 / space.size
    return {
        alpha: inv_size
        * sum(values[x] * basis_value(space, alpha, x) for x in space.points())
        for alpha in space.multiindices()
    }


def evaluate_spectrum(
    space: FiniteProductSpace,
    coefficients: Mapping[MultiIndex, float],
    point: Point,
) -> float:
    return sum(
        coefficient * basis_value(space, alpha, point)
        for alpha, coefficient in coefficients.items()
    )


def objective_from_coefficients(
    space: FiniteProductSpace, coefficients: Mapping[MultiIndex, float]
) -> ValueTable:
    _validate_coefficient_keys(space, coefficients)
    return {x: evaluate_spectrum(space, coefficients, x) for x in space.points()}


def truncate_coefficients(
    coefficients: Mapping[MultiIndex, float], max_degree: int
) -> CoefficientMap:
    return {
        alpha: coefficient
        for alpha, coefficient in coefficients.items()
        if degree(alpha) <= max_degree
    }


def l2_tail_energy(coefficients: Mapping[MultiIndex, float], max_degree: int) -> float:
    """Return squared L2 tail norm, sum_{deg(alpha)>d} |a_alpha|^2."""

    return sum(
        coefficient * coefficient
        for alpha, coefficient in coefficients.items()
        if degree(alpha) > max_degree
    )


def level_influence(
    coefficients: Mapping[MultiIndex, float], coordinate: int, level: int
) -> float:
    """Return level-resolved influence energy for one coordinate."""

    return sum(
        coefficient * coefficient
        for alpha, coefficient in coefficients.items()
        if degree(alpha) == level and alpha[coordinate] != 0
    )


def total_influence(
    coefficients: Mapping[MultiIndex, float], coordinate: int
) -> float:
    return sum(
        coefficient * coefficient
        for alpha, coefficient in coefficients.items()
        if alpha[coordinate] != 0
    )


def weighted_l1_tail_envelope(
    space: FiniteProductSpace,
    coefficients: Mapping[MultiIndex, float],
    max_degree: int,
    restricted_coordinates: Sequence[int] = (),
) -> float:
    """Assignment-independent T3 envelope after restricting selected coordinates."""

    restricted = frozenset(restricted_coordinates)
    return sum(
        abs(coefficient) * basis_supnorm(space, alpha)
        for alpha, coefficient in coefficients.items()
        if sum(
            alpha[i] != 0
            for i in range(space.n)
            if i not in restricted
        )
        > max_degree
    )


def restrict_table(
    space: FiniteProductSpace,
    values: Mapping[Point, float],
    restriction: Mapping[int, int],
) -> Tuple[Tuple[int, ...], FiniteProductSpace | None, Dict[Point, float]]:
    """Restrict coordinates and return active indices, residual space and table."""

    _validate_complete_table(space, values)
    _validate_restriction(space, restriction)
    active = tuple(i for i in range(space.n) if i not in restriction)

    if not active:
        point = tuple(restriction[i] for i in range(space.n))
        return active, None, {(): values[point]}

    residual_space = FiniteProductSpace(tuple(space.cardinalities[i] for i in active))
    restricted_values: Dict[Point, float] = {}
    for residual_point in residual_space.points():
        full_point = [0] * space.n
        for i, value in restriction.items():
            full_point[i] = value
        for residual_i, full_i in enumerate(active):
            full_point[full_i] = residual_point[residual_i]
        restricted_values[tuple(residual_point)] = values[tuple(full_point)]
    return active, residual_space, restricted_values


def transported_coefficient(
    space: FiniteProductSpace,
    coefficients: Mapping[MultiIndex, float],
    restriction: Mapping[int, int],
    residual_alpha: MultiIndex,
) -> float:
    """T1 right-hand side for a coefficient after an arbitrary restriction."""

    _validate_restriction(space, restriction)
    active = tuple(i for i in range(space.n) if i not in restriction)
    if len(residual_alpha) != len(active):
        raise ValueError("residual multi-index has incorrect dimension")

    tables = basis_tables(space)
    result = 0.0
    for alpha, coefficient in coefficients.items():
        if tuple(alpha[i] for i in active) != tuple(residual_alpha):
            continue
        factor = 1.0
        for coordinate, fixed_value in restriction.items():
            factor *= tables[coordinate][alpha[coordinate]][fixed_value]
        result += coefficient * factor
    return result


def restricted_supnorm_residual(
    residual_space: FiniteProductSpace,
    residual_values: Mapping[Point, float],
    max_degree: int,
) -> float:
    coefficients = spectral_coefficients(residual_space, residual_values)
    truncated = truncate_coefficients(coefficients, max_degree)
    return max(
        abs(residual_values[x] - evaluate_spectrum(residual_space, truncated, x))
        for x in residual_space.points()
    )


def expected_tail_after_single_restriction(
    space: FiniteProductSpace,
    values: Mapping[Point, float],
    coordinate: int,
    max_degree: int,
) -> float:
    """Uniformly average the residual L2 tail over all values of one coordinate."""

    if coordinate < 0 or coordinate >= space.n:
        raise IndexError("coordinate out of range")
    total = 0.0
    cardinality = space.cardinalities[coordinate]
    for fixed_value in range(cardinality):
        _, residual_space, residual_values = restrict_table(
            space, values, {coordinate: fixed_value}
        )
        if residual_space is None:
            tail = 0.0
        else:
            tail = l2_tail_energy(
                spectral_coefficients(residual_space, residual_values), max_degree
            )
        total += tail / cardinality
    return total


def exact_optima(values: Mapping[Point, float], tolerance: float = 1e-12) -> Tuple[float, Tuple[Point, ...]]:
    minimum = min(values.values())
    minimizers = tuple(sorted(x for x, value in values.items() if abs(value - minimum) <= tolerance))
    return minimum, minimizers


def optimum_gap(values: Mapping[Point, float], tolerance: float = 1e-12) -> float:
    minimum, minimizers = exact_optima(values, tolerance=tolerance)
    if len(minimizers) != 1:
        return 0.0
    higher = [value for value in values.values() if value > minimum + tolerance]
    return min(higher) - minimum if higher else math.inf


def branch_minima(
    space: FiniteProductSpace,
    values: Mapping[Point, float],
    coordinate: int,
) -> Tuple[float, ...]:
    if coordinate < 0 or coordinate >= space.n:
        raise IndexError("coordinate out of range")
    result = []
    for fixed_value in range(space.cardinalities[coordinate]):
        branch = [
            value
            for point, value in values.items()
            if point[coordinate] == fixed_value
        ]
        result.append(min(branch))
    return tuple(result)


def branch_margin(
    space: FiniteProductSpace,
    values: Mapping[Point, float],
    coordinate: int,
    tolerance: float = 1e-12,
) -> float:
    minima = sorted(branch_minima(space, values, coordinate))
    if len(minima) < 2:
        return math.inf
    if abs(minima[1] - minima[0]) <= tolerance:
        return 0.0
    return minima[1] - minima[0]


def primal_graph(
    coordinate_count: int,
    coefficients: Mapping[MultiIndex, float],
    threshold: float = 0.0,
) -> Dict[int, set[int]]:
    graph = {i: set() for i in range(coordinate_count)}
    for alpha, coefficient in coefficients.items():
        if abs(coefficient) <= threshold:
            continue
        variables = support(alpha)
        for left, right in itertools.combinations(variables, 2):
            graph[left].add(right)
            graph[right].add(left)
    return graph


def elimination_width(graph: Mapping[int, set[int]], order: Sequence[int]) -> int:
    working = {vertex: set(neighbors) for vertex, neighbors in graph.items()}
    width = 0
    for vertex in order:
        neighbors = set(working[vertex])
        width = max(width, len(neighbors))
        for left, right in itertools.combinations(neighbors, 2):
            working[left].add(right)
            working[right].add(left)
        for neighbor in neighbors:
            working[neighbor].discard(vertex)
        working[vertex].clear()
    return width


def exact_treewidth(graph: Mapping[int, set[int]], max_vertices: int = 8) -> int:
    """Compute treewidth by exhaustive elimination-order search for tiny graphs."""

    vertices = tuple(graph)
    if len(vertices) > max_vertices:
        raise ValueError(
            f"exact treewidth is restricted to <= {max_vertices} vertices in WP01"
        )
    return min(
        elimination_width(graph, order)
        for order in itertools.permutations(vertices)
    )


def random_spectral_coefficients(
    space: FiniteProductSpace,
    seed: int,
    density: float = 0.6,
    scale: float = 0.8,
    max_degree: int | None = None,
) -> CoefficientMap:
    """Generate a deterministic random spectral objective for finite confrontation."""

    if not (0.0 <= density <= 1.0):
        raise ValueError("density must lie in [0,1]")
    rng = random.Random(seed)
    result: CoefficientMap = {}
    for alpha in space.multiindices():
        if max_degree is not None and degree(alpha) > max_degree:
            result[alpha] = 0.0
            continue
        if rng.random() <= density:
            result[alpha] = rng.uniform(-scale, scale) / (1.0 + degree(alpha))
        else:
            result[alpha] = 0.0
    return result


def noisy_observations(
    space: FiniteProductSpace,
    values: Mapping[Point, float],
    sigma: float,
    seed: int,
) -> ValueTable:
    """Return one deterministic seeded Gaussian-noise observation per point."""

    if sigma < 0:
        raise ValueError("sigma must be nonnegative")
    _validate_complete_table(space, values)
    rng = random.Random(seed)
    return {
        x: values[x] + (rng.gauss(0.0, sigma) if sigma else 0.0)
        for x in space.points()
    }


def instance_metrics(
    space: FiniteProductSpace,
    coefficients: Mapping[MultiIndex, float],
    max_degree: int,
    heavy_threshold: float,
    branch_coordinate: int,
    sigma: float = 0.0,
) -> Dict[str, float | int]:
    values = objective_from_coefficients(space, coefficients)
    graph = primal_graph(
        space.n,
        {
            alpha: coefficient
            for alpha, coefficient in coefficients.items()
            if abs(coefficient) >= heavy_threshold
        },
    )
    return {
        "n": space.n,
        "domain_size": space.size,
        "max_degree": max_degree,
        "heavy_count": sum(
            abs(coefficient) >= heavy_threshold
            for coefficient in coefficients.values()
        ),
        "tau2": math.sqrt(l2_tail_energy(coefficients, max_degree)),
        "tau_inf_envelope": weighted_l1_tail_envelope(
            space, coefficients, max_degree
        ),
        "treewidth": exact_treewidth(graph),
        "max_boundary_influence": max(
            level_influence(coefficients, i, max_degree + 1)
            for i in range(space.n)
        ),
        "branch_margin": branch_margin(space, values, branch_coordinate),
        "optimum_gap": optimum_gap(values),
        "sigma": sigma,
    }


def adversarial_regimes() -> Dict[str, Tuple[FiniteProductSpace, CoefficientMap, int, int]]:
    """Crossed fixtures that separate ASP structural quantities."""

    # High level-2 influence with no branch preference: x0*x1 is symmetric.
    space4 = FiniteProductSpace((2, 2, 2, 2))
    high_influence_zero_margin: CoefficientMap = {
        (1, 1, 0, 0): 2.0,
    }

    # Large branch gap induced by a first-order term, but zero level-2 influence.
    large_margin_weak_boundary: CoefficientMap = {
        (1, 0, 0, 0): 1.5,
    }

    # Many tiny cubic terms: squared tail stays small while l1 envelope accumulates.
    space6 = FiniteProductSpace((2, 2, 2, 2, 2, 2))
    diffuse_tail: CoefficientMap = {
        tuple(1 if i in triple else 0 for i in range(6)): 0.02
        for triple in itertools.combinations(range(6), 3)
    }

    # Pairwise path and clique provide known width-1 and width-5 fixtures.
    path: CoefficientMap = {
        tuple(1 if i in (edge, edge + 1) else 0 for i in range(6)): 0.3
        for edge in range(5)
    }
    clique: CoefficientMap = {
        tuple(1 if i in pair else 0 for i in range(6)): 0.3
        for pair in itertools.combinations(range(6), 2)
    }

    return {
        "high_influence_zero_margin": (space4, high_influence_zero_margin, 1, 0),
        "large_margin_weak_boundary": (space4, large_margin_weak_boundary, 1, 0),
        "diffuse_l2_vs_l1_tail": (space6, diffuse_tail, 2, 0),
        "path_width": (space6, path, 1, 0),
        "clique_width": (space6, clique, 1, 0),
    }


def all_nontrivial_restrictions(space: FiniteProductSpace) -> Iterable[Dict[int, int]]:
    """Enumerate every nonempty, non-full coordinate restriction."""

    coordinates = range(space.n)
    for restricted_count in range(1, space.n):
        for restricted_coordinates in itertools.combinations(coordinates, restricted_count):
            for values in itertools.product(
                *(range(space.cardinalities[i]) for i in restricted_coordinates)
            ):
                yield dict(zip(restricted_coordinates, values))


def basis_orthonormality_error(space: FiniteProductSpace) -> float:
    error = 0.0
    for cardinality in space.cardinalities:
        basis = coordinate_basis(cardinality)
        for left in range(cardinality):
            for right in range(cardinality):
                inner = (
                    sum(
                        basis[left][value] * basis[right][value]
                        for value in range(cardinality)
                    )
                    / cardinality
                )
                target = 1.0 if left == right else 0.0
                error = max(error, abs(inner - target))
    return error


def _validate_complete_table(
    space: FiniteProductSpace, values: Mapping[Point, float]
) -> None:
    expected = set(space.points())
    actual = set(values)
    if actual != expected:
        missing = len(expected - actual)
        extra = len(actual - expected)
        raise ValueError(
            f"objective table must cover the complete domain (missing={missing}, extra={extra})"
        )


def _validate_coefficient_keys(
    space: FiniteProductSpace, coefficients: Mapping[MultiIndex, float]
) -> None:
    for alpha in coefficients:
        if len(alpha) != space.n:
            raise ValueError("coefficient multi-index has incorrect dimension")
        if any(
            alpha[i] < 0 or alpha[i] >= space.cardinalities[i]
            for i in range(space.n)
        ):
            raise ValueError("coefficient multi-index is outside the basis range")


def _validate_restriction(
    space: FiniteProductSpace, restriction: Mapping[int, int]
) -> None:
    for coordinate, value in restriction.items():
        if coordinate < 0 or coordinate >= space.n:
            raise IndexError("restricted coordinate out of range")
        if value < 0 or value >= space.cardinalities[coordinate]:
            raise ValueError("restricted value outside coordinate domain")
