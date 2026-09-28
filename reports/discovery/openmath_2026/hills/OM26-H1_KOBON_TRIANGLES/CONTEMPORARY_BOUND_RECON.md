# OM26-H1 contemporary bound-research reconnaissance

**Captured:** 2026-09-27

## Source identity

Public repository: `alejandrozu/kobon-proof`
Protected external commit observed: `22d1165f6c455fe45e461baef4410f6d5c78a014`
Repository description: `lean proof of the even line kobon augmentation proposition`.

Relevant exact source objects:

- `research/six-hour-2026-09-21/general-bounds/upper-bound-scope-audit.md` — blob `5ba2f73df5ca677d5f0d81e82389d90ef9a56aaf`;
- `research/six-hour-2026-09-21/general-bounds/clean-line-parity.md` — blob `9cdfd43d3c9d9f47485d4c2a45926bcf22574ab0`;
- `research/six-hour-2026-09-21/general-bounds/multiplicity-budget.md` — blob `a2dc06f950e860c0a0a45734e0a77b15ad3b826a`;
- `research/six-hour-2026-09-21/general-bounds/README.md` — blob `3f7342eaa31e96122909f22eba0a608787e1685e`;
- `FORMALIZATION.md` — blob `f7b58671a6a0f3fa47b7f369308480fb6e3537a1`.

## What this source says that matters for H1-12

The repository independently reaches the same scope warning as our Forge audit: BBL/Blanc even-order bounds are simple-arrangement results and cannot automatically certify the unrestricted classical problem. It also records Blanc's later simple even-order polynomial `floor(n(n-5/2)/3)`, which equals **93 at n=18**. Thus any hill construction scoring 94 or 95 must be nonsimple (parallelism and/or a finite multiple intersection).

It also contains a paper-level restricted nonsimple theorem:

> For every even n>=4, a pairwise nonparallel arrangement with at most two finite multiple points, of arbitrary multiplicity, has T <= floor(n(n-5/2)/3)+1.

At n=18 this gives T <= 94.

The same note derives a weighted theorem for pairwise nonparallel arrangements with arbitrarily many multiple points. In particular, if every multiple point has multiplicity at least five, it gives the simple polynomial T <= floor(n(n-5/2)/3), which is 93 at n=18.

The repository explicitly labels the complete global extraction/clean-line charging argument as paper-level geometry rather than a finished unrestricted Lean theorem. Its local fan obstruction and arithmetic components have stronger formal support, but the unrestricted classical upper problem remains open in that source.

## Structural consequences for our search

Subject to independent downstream proof review of the stated restricted theorem, a hypothetical n=18 score-95 arrangement cannot lie in the pairwise-nonparallel class with at most two finite multiple points. More basically, Blanc's simple 93 bound means any score above 93 must occupy a nonsimple stratum. Therefore the next search should concentrate on singular strata:

- at least one parallel pair; or
- if pairwise nonparallel, at least three finite multiple points, with triple/quadruple points the difficult multiplicities.

Our verified 93 Bader-order reconstruction already lies on a parallel stratum (three intended parallel pairs), which makes coordinated parallel-preserving moves a higher-value next search than smoothing toward a simple arrangement.

## Claim boundary

This is source reconnaissance. GCL has not independently certified the external paper-level restricted theorem, and this record does not promote 94 to a hill-global upper bound. It narrows route design and identifies exact external proof obligations for later Solve/Cert review.
