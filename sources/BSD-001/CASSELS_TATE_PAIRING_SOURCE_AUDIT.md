# BSD-001 source audit — Cassels–Tate pairing interface

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#139`.
- Protected Forge baseline: `33fea960d0bd3efd6c357a27880c4be4e32034b4`.
- Downstream owner: `grandchallenge/MATHSOLVE#162`.
- Disposition: `QUALIFIED_CASSELS_TATE_PAIRING_INTERFACE`.
- Claim class: bounded source theorem interface only.

## Source

Bjorn Poonen and Michael Stoll, *The Cassels-Tate pairing on polarized abelian varieties*, arXiv:`math/9911267`.

The source abstract records the exact interface needed downstream:

1. for an abelian variety `A` over a global field, Cassels and Tate construct a nondegenerate pairing on `Sha(A)_nd`, the quotient of `Sha(A)` by its maximal divisible subgroup;
2. if `A` is an elliptic curve, Cassels' theorem makes this pairing alternating.

## Downstream composition

MATHSOLVE already has a protected low-analytic-rank interface giving finiteness of `Sha(E/Q)` in the selected analytic-rank-one class. For a finite group the maximal divisible subgroup is trivial. Therefore the admitted source interface specializes to a nondegenerate alternating pairing

`Sha(E/Q) x Sha(E/Q) -> Q/Z`.

The further conclusion that a finite abelian group carrying such a pairing has square cardinality is elementary finite-group algebra and may be proved in-package downstream. Forge does not need to promote that derived corollary as a separate arithmetic theorem.

## Boundary

This source interface does not prove finiteness of `Sha`; it does not compute any primary length; it does not prove the BSD leading-term formula; and it does not imply `BSD-R2-A1`, novelty, priority, or MATHCERT certification.

## Provider disposition

`QUALIFIED_CASSELS_TATE_PAIRING_INTERFACE`