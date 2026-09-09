# BSD-001 source audit — Heegner primitivity at `p=2`

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#134`.
- Screen date: `2026-09-08`.
- Exact-interface refresh: `2026-09-08`.
- Disposition: `QUALIFIED_P2_HEEGNER_PRIMITIVITY_ROUTE_BARRIER`.
- Claim class: route/source diagnosis only; no theorem promotion or certification.

## Question

The protected Solve frontier needs an exact integral theorem controlling the 2-primary Heegner/Selmer length and the corresponding Tate–Shafarevich contribution. This audit asks whether the standard odd-prime primitivity route can simply be specialized to `p=2`.

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

Exact public source identity used for reconstruction: author-hosted PDF `https://www.math.columbia.edu/~chaoli/raising.pdf`; journal identity as above.

The paper contrasts the odd-prime rank-lowering step used in Wei Zhang's strategy with `p=2`.

For odd `p>=5`, the cited Gross–Parson/Zhang theorem uses a level-raising prime satisfying

`q != +/-1 (mod p)`

and, from Selmer rank one, obtains a positive-density set of level raises with Selmer rank zero.

The source states that this key congruence condition is impossible for `p=2`. It then proves genuinely different behavior in its mod-2 setting.

### Exact Assumption 4.1 interface

For an elliptic curve `E/Q` of conductor `N`, a level-raising prime `q`, and an imaginary quadratic field `K`, Assumption 4.1 requires:

1. `rho_bar_{E,2}` is surjective;
2. `E` has good or multiplicative reduction at `2`;
3. the Serre conductor `N(rho_bar_{E,2})` equals the odd part of `N`; if `2|N`, the residual representation is ramified at `2`;
4. if `2` does not divide `N`, then `rho_bar_{E,2}|G_Q2` is nontrivial;
5. `q` is a mod-2 level-raising prime: `q` does not divide `2N` and `a_q` is even;
6. `K` is imaginary quadratic and satisfies the Heegner hypothesis for `E`: every prime factor of `N` splits in `K`;
7. `q` is inert in `K`.

**Locator:** Assumption 4.1, paper p.8 in the author-hosted PDF.

Remark 4.2 states that Assumption 4.1(3) is equivalent to the component group of the Néron model at each bad prime having odd order; in particular all local Tamagawa numbers are odd.

**Locator:** Remark 4.2, paper p.8.

### Exact Selmer-rank notation and order-two Frobenius condition

Definition 1.5 defines

`s_2(E/K) := dim_F2 Sel_2(E/K)`

and the corresponding `lambda`-Selmer rank of the level-raised abelian variety.

The mod-2 level-raising discussion records that for `q` not dividing `2N`, `a_q` even is equivalent to residual Frobenius being either the identity or the order-two unipotent class in `GL_2(F_2) ~= S3`.

**Locator:** Definition 1.5 and section 1.9, paper pp.2-3.

### Exact obstruction theorem

Theorem 7.1 assumes Assumption 4.1 and additionally that `Frob_q` has order `2` on the common residual module. It proves

`s_2(E/K)=1  =>  s_lambda(A/K)=2`.

Thus in this exact hypothesis class the level-raised 2-Selmer rank cannot be lowered from one to zero.

**Locator:** Theorem 7.1, paper p.13.

This is a rank-lowering obstruction. It is not a `p=2` primitivity theorem and not a BSD(2) formula.

### Local-at-2 condition may not be deleted

Remark 6.2 states that the conclusion of Theorem 6.1 may fail if the nontriviality of `rho_bar_{E,2}|G_Q2` is dropped, due to uncertainty in the local condition at `2`. The source gives the explicit curve

`2351a1: y^2 + xy + y = x^3 - 5x - 5`

with trivial residual restriction to `G_Q2` as its example.

**Locator:** Remark 6.2, paper p.13.

Downstream use may cite this example only as evidence that the local source hypothesis is substantive. The source example is not by itself an admitted `BSD-R2-A1` instance.

## Qualified composition statement

Sources A and B jointly support the following bounded conclusion.

The standard odd-prime proof technology for the exact Heegner-index formula cannot be transferred mechanically to `p=2`:

1. the exact known primitivity/index theorem being screened assumes `p>3`;
2. a key rank-lowering step behind Wei Zhang's odd-prime primitivity method uses a congruence condition unavailable at `p=2`;
3. in Chao Li's exact Assumption 4.1 class, when the residual Frobenius at the level-raising prime has order two, a rank-one 2-Selmer group is sent to rank two rather than rank zero.

This establishes a **route obstruction**, not an impossibility theorem.

## Relation to the selected BSD class

Protected Solve work may determine whether each source hypothesis follows from the selected class; this provider record does not make those downstream deductions for Solve.

In particular, source-level facts that remain distinct are:

- global residual surjectivity;
- residual-conductor equality / odd bad component groups;
- local nontriviality at `2` when the conductor is odd;
- existence of the required `q` and `K`;
- the minimal condition `s_2(E/K)=1`.

No one of these may be silently replaced by another.

## Interaction with protected Solve results

WP06 already proves exact quadratic 2-power descent and exposes all finite plus/minus defect groups rather than dividing by two.

WP09 supplies a suitable auxiliary `K` and corrected Disegni applicability at `p=2`.

Later protected Solve work may discharge or reinterpret some Chao Li hypotheses, but it does not change the source theorem itself.

Neither existing Solve result proves primitivity of a 2-adic Heegner Kolyvagin system. Source A identifies primitivity as the missing ingredient that upgrades Kolyvagin's upper bound to the exact Heegner-index/Sha formula in the standard odd-prime lane.

## What remains admissible

The following remain valid future routes:

- a new integral `p=2` primitivity theorem proved by a method not requiring the obstructed rank-lowering step;
- a direct exact 2-primary Heegner-index theorem that bypasses Kolyvagin-system primitivity as formulated above;
- a different arithmetic-length theorem yielding the WP00 target directly;
- the separate integral Iwasawa lane already recorded by Solve.

## Claim boundary

This audit does **not** establish:

- impossibility of a general `p=2` Heegner/Kolyvagin theorem;
- the Chao Li obstruction outside its exact stated hypotheses;
- an exact 2-primary Sha/index equality;
- the rank-zero twist 2-part of BSD;
- `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.

## Provider disposition

`QUALIFIED_P2_HEEGNER_PRIMITIVITY_ROUTE_BARRIER`

Downstream use is limited to the exact source interfaces above, exclusion of a mechanical specialization of the standard odd-prime primitivity/rank-lowering proof technology, and identification of the missing integral `p=2` primitivity/index theorem.