# HC-001 source, formulation, and status audit plan

## Parent campaign

- Programme tracker: `grandchallenge/MATH-PROGRAMME#65`
- Forge tracker: `grandchallenge/MATHFORGE#21`
- Campaign: `HC-001`
- Work Package: `HC-WP00`
- Audit date: 2026-07-24

## Canonical target

Let `X` be a smooth projective algebraic variety over `C`, and let `p` be a nonnegative integer. Define

```math
Hdg^{2p}(X,Q)=H^{2p}(X,Q)\cap H^{p,p}(X)
```

inside `H^{2p}(X,C)`. The classical rational Hodge conjecture asks whether

```math
cl_Q^p: CH^p(X)\otimes_Z Q -> Hdg^{2p}(X,Q)
```

is surjective for every `X` and `p`.

Equivalently, every rational Hodge class should be a rational linear combination of cohomology classes of codimension-`p` irreducible algebraic subvarieties.

## Audit questions

1. What exactly are the domain, coefficient ring, cohomology theory, codimension convention, and cycle equivalence relation in the official statement?
2. Which alternate formulations are equivalent to the canonical target, and which are merely stronger, weaker, parallel, or false?
3. Which boundary cases are established without importing the full conjecture?
4. What is the first unrestricted dimension and codimension not covered by the elementary boundary cases?
5. Which counterexamples delimit the integral and compact-Kahler analogues?
6. Which statements about Hodge loci, deformation, absolute Hodge classes, motivated cycles, standard conjectures, and Tate classes are commonly mistaken for the classical conjecture?
7. What current formalization substrate exists, and where must imported continuum geometry remain explicit?

## Required deliverables

- `source_ledger.yaml`: primary, official, and operational source records with exact audit states.
- `hypothesis_matrix.csv`: formulation-by-formulation comparison of hypotheses and conclusions.
- `current_status_audit.md`: dated open-status determination and conservative known-case boundary.
- `false_proof_seed_ledger.yaml`: executable semantic failure fixtures for WP01.
- Cross-pillar handoff to the MATHSOLVE statement lattice and MATHCERT claim schema.

## Source policy

Primary and official sources control formulation and theorem attribution. Surveys may orient the audit but cannot silently fill missing hypotheses or theorem locators. A source record must state:

- source type and primary/secondary status;
- theorem or passage locator;
- variety class and field;
- dimension and codimension, when restricted;
- coefficient ring;
- cycle group and equivalence relation;
- cohomology theory;
- exact conclusion;
- conditional dependencies;
- unresolved translation or extraction debt.

## Mandatory statement separation

The audit must keep distinct:

1. classical rational Hodge conjecture;
2. integral Hodge conjecture;
3. compact-Kahler analogue;
4. generalized Hodge conjecture;
5. variational Hodge conjecture;
6. algebraicity of Hodge loci;
7. absolute Hodge classes;
8. motivated cycles;
9. Lefschetz standard conjecture and algebraicity of projectors;
10. Tate conjecture and specialization/reduction arguments;
11. effectivity or representation by a single subvariety.

## Claim boundary

This audit does not prove the Hodge conjecture, establish a new known case, determine novelty, or provide an algorithm deciding algebraicity. Numerical period recognition, symbolic manipulation, and formalized abstract interfaces are not continuum proofs of cycle-class surjectivity.

## Completion test

The Forge lane is complete when every promoted status statement has a source locator and complete hypotheses; every neighboring conjecture has an explicit implication or non-implication relation; every source gap is visible; and the false-proof fixtures can be replayed without relying on rhetoric.