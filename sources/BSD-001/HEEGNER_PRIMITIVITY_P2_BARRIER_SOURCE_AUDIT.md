# BSD-001 source audit — Heegner primitivity at `p=2`

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#134`.
- Screen date: `2026-09-08`.
- Disposition: `QUALIFIED_P2_HEEGNER_PRIMITIVITY_ROUTE_BARRIER`.
- Claim class: route/source diagnosis only; no theorem promotion or certification.

## Question

The protected Solve frontier `BSD-R2-A1-2PRIMARY-HEEGNER-INDEX` needs an exact integral theorem controlling the 2-primary index of a Heegner point and the corresponding Tate–Shafarevich group. This audit asks whether the standard odd-prime primitivity route can simply be specialized to `p=2`.

## Source A — Burungale–Castella–Kim

Ashay A. Burungale, Francesc Castella, and Chan-Ho Kim, *Indivisibility of Heegner points and arithmetic applications*, arXiv:1806.01691v2 (2018).

Primary arXiv identity: `arXiv:1806.01691v2`.

The paper works with a good ordinary prime satisfying `p>3`. Under its generalized Heegner, residual, and splitting hypotheses it imports Wei Zhang's proof of Kolyvagin's conjecture as primitivity of the Heegner Kolyvagin system.

The source explains the logical mechanism explicitly:

`primitive Kolyvagin system -> sharp Kolyvagin structure theorem -> exact Sha / Heegner-index equality`.

In analytic rank one, its Corollary 3.4 gives, under the hypotheses of its primitivity theorem,

`ord_p(#Sha(E/K)[p^infinity]) = 2 * ord_p([E(K): Z y_K])`,

where `y_K` is the Heegner point.

This is exactly the algebraic shape sought by the direct arithmetic BSD lane. It is not a `p=2` theorem: the source's setup and primitivity input require `p>3`.

The same paper also records an equality involving the square of a Mordell–Weil index, the `p`-primary Sha order, and Tamagawa factors, but only up to a `p`-adic unit inside its `p>3` framework. That formulation may not be promoted to an exact `ord_2` identity.

## Source B — Chao Li

Chao Li, *Level Raising mod 2 and Obstruction to Rank Lowering*, International Mathematics Research Notices 2019, no. 8, 2332–2355. DOI: `10.1093/imrn/rnx188`.

The author-hosted paper and journal record identify the exact source.

The paper contrasts the odd-prime rank-lowering step used in Wei Zhang's strategy with `p=2`.

For odd `p>=5`, the cited Gross–Parson/Zhang theorem uses a level-raising prime satisfying

`q != +/-1 (mod p)`

and, from Selmer rank one, obtains a positive-density set of level raises with Selmer rank zero.

The source states that this key congruence condition is impossible for `p=2`. It then proves a genuinely different behavior in its mod-2 setting. Under Assumption 4.1, which includes a **surjective** residual representation together with its other local hypotheses, Theorem 7.1 shows that for the relevant order-two Frobenius level-raising primes,

`s_2(E/K)=1  =>  s_lambda(A/K)=2`.

Thus the level-raised 2-Selmer rank cannot be lowered to zero in that source's hypothesis class.

## Qualified composition statement

These sources jointly support the following bounded conclusion.

The standard odd-prime proof technology for the exact Heegner-index formula cannot be transferred mechanically to `p=2`:

1. the exact known primitivity/index theorem being screened assumes `p>3`;
2. a key rank-lowering step behind Wei Zhang's odd-prime primitivity method uses a congruence condition unavailable at `p=2`;
3. in Chao Li's surjective mod-2 Heegner subcase, the analogous level-raising operation is proved to raise the rank-one Selmer situation to rank two rather than lower it to zero.

This establishes a **route obstruction**, not an impossibility theorem.

## Relation to the selected BSD class

`BSD-R2-A1` assumes that `E[2]` is irreducible. Chao Li's Assumption 4.1 uses the stronger condition that the residual representation is surjective.

Over `F_2`, irreducibility does not by itself imply surjectivity: the order-three subgroup of `GL_2(F_2)` can act irreducibly. Therefore Chao Li's no-rank-lowering theorem is not a theorem for every curve in the selected BSD class.

It is valid evidence that the standard odd-prime rank-lowering/primitivity machine has a structural mod-2 failure on a substantial subcase and hence cannot be used as a uniform proof of `BSD-R2-A1` without new input.

## Interaction with protected Solve results

WP06 already proves exact quadratic 2-power descent and exposes all finite plus/minus defect groups rather than dividing by two.

WP09 supplies a suitable auxiliary `K` and corrected Disegni applicability at `p=2`.

Neither result proves primitivity of a 2-adic Heegner Kolyvagin system. Source A identifies primitivity as the missing ingredient that upgrades Kolyvagin's upper bound to the exact Heegner-index/Sha formula in the standard odd-prime lane.

## What remains admissible

The following would still be valid future routes:

- a new integral `p=2` primitivity theorem proved by a method not requiring the obstructed rank-lowering step;
- a direct exact 2-primary Heegner-index theorem that bypasses Kolyvagin-system primitivity as formulated above;
- a different arithmetic-length theorem yielding the WP00 target directly;
- the separate integral Iwasawa lane already recorded by Solve.

## Claim boundary

This audit does **not** establish:

- impossibility of a general `p=2` Heegner/Kolyvagin theorem;
- the Chao Li obstruction for all irreducible `E[2]`;
- an exact 2-primary Sha/index equality;
- the rank-zero twist 2-part of BSD;
- `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.

## Provider disposition

`QUALIFIED_P2_HEEGNER_PRIMITIVITY_ROUTE_BARRIER`

Downstream use is limited to excluding a mechanical specialization of the standard odd-prime primitivity/rank-lowering proof technology and to naming the missing integral `p=2` primitivity/index theorem.