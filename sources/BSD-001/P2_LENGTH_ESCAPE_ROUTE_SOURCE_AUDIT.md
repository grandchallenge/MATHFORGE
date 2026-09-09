# BSD-001 source audit — remaining `p=2` arithmetic-length escape routes

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#137`.
- Protected Forge baseline: `57b68d02f27a6b4e82292200c8ac577f161ebf29`.
- Downstream owner: `grandchallenge/MATHSOLVE#162`.
- Screen date: `2026-09-08`.
- Disposition: `QUALIFIED_P2_LENGTH_ROUTE_SCREEN`.
- Claim class: bounded source/applicability evidence only; no theorem promotion or certification.

## Question

After protected MATHSOLVE WP13 and WP14, the selected target still needs an exact unsquared identity at `p=2`:

`ord_2(L'(E,1)/(Omega_E Reg_E))`

`= len_Z2 Sha(E/Q)[2^infinity] + sum_{ell|N} ord_2(c_ell)`.

This audit binds four plausible source interfaces that could appear to narrow or bypass that gap. It records exactly what each source proves and the restriction that prevents direct uniform composition into the selected full class.

This is not an exhaustive literature claim. Failure of the screened sources to close the interface is not proof that no theorem exists.

## Source A — Barrios–Mok: BSD modulo rational squares

Alexander J. Barrios and Chung Pang Mok, *On the Birch and Swinnerton-Dyer formula modulo squares for certain quadratic twists of elliptic curves*, arXiv:`2510.00926v1` (2025).

### Exact interface

The paper defines validity of the full Birch–Swinnerton-Dyer leading-term formula modulo multiplication by a square in `Q^x`.

Theorem 1.1 treats a quadratic-twist pair satisfying a modified Heegner hypothesis and analytic ranks `0/1` (or `1/0`) when `N_-` has an odd number of prime factors. Its conclusion is an equivalence:

`BSD modulo (Q^x)^2 for E^D/Q  <=>  BSD modulo (Q^x)^2 for E/Q`.

Corollary 1.5 gives the semistable low-rank specialization. If `E/Q` is semistable of analytic rank at most one and `D>0` is a fundamental discriminant coprime to `N` such that `E^D/Q` also has analytic rank at most one, then the same modulo-square BSD validity holds for one curve if and only if it holds for the other.

**Locators:** Theorem 1.1 and Corollary 1.5, introduction pp. 3 and 5 of arXiv:`2510.00926v1`.

### Composition boundary

This source transports a square class. It does not prove the modulo-square BSD formula absolutely for either member of an arbitrary pair, and it does not determine an exact `2`-adic valuation inside that square class.

Downstream MATHSOLVE may use the theorem as a parity/square-class transport interface only after separately proving what square-class information implies for the selected normalized quotient. It may not promote the theorem to an exact `BSD(2)` equality.

## Source B — Jetchev: Tamagawa-aware Kolyvagin upper bound

Dimitar P. Jetchev, *Global Divisibility of Heegner Points and Tamagawa Numbers*, arXiv:`math/0703431v1`; Compositio Mathematica 144 (2008), 811–826.

### Exact interface

The introduction explicitly says:

`consider the following hypothesis on an odd prime p`.

Hypothesis `(*)` then assumes `p` does not divide the conductor and `Q(E[p])/Q` has Galois group `GL_2(F_p)`.

Under that prime/hypothesis package, Kolyvagin's formula is written as

`#Sha(E/K)[p^infinity] = p^(2(m_0-m_infinity))`.

Jetchev's Theorem 1.4 proves

`m_infinity >= max_{q|N} ord_p(c_q)`,

and Corollary 1.5 gives the corresponding Tamagawa-aware upper bound on the `p`-primary Sha order.

**Locators:** introduction, Hypothesis `(*)`, Theorem 1.4 and Corollary 1.5, arXiv:`math/0703431v1`, pp. 1–2.

### Composition boundary

The source's theorem is formulated after explicitly restricting to an **odd prime** `p`. The selected campaign has `p=2`. Consequently the theorem is not an admitted `p=2` upper bound and cannot be combined with parity information by silently setting `p=2`.

The facts that the selected conductor is odd and protected WP12 gives residual surjectivity do not remove the source's odd-prime restriction.

## Source C — Kriz–Li: restricted BSD(2) propagation

Daniel Kriz and Chao Li, *Congruences between Heegner points and quadratic twists of elliptic curves*, arXiv:`1606.03172`; Forum of Mathematics, Sigma 7 (2019), e15.

### Exact interface

Theorem 1.12 starts with `E(Q)[2]=0`, a Heegner imaginary quadratic field satisfying the paper's Assumption `(F)`, and odd local Tamagawa number `c_2(E)`; in the additive-at-2 case an additional odd-Manin-constant condition is imposed.

The theorem propagates `BSD(2)` from seed curves to a specified family of quadratic twists. In particular its `Q`-side conclusion assumes `BSD(2)` is already true for the seed pair `E/Q` and `E^(d_K)/Q`.

Section 4.1 makes the arithmetic restriction explicit: under Assumption `(F)` and odd `c_2(E)`, the Heegner point is indivisible by `2`, equivalently all local Tamagawa numbers of `E` are odd, and the relevant `2`-Selmer group has rank one. The paper then propagates this controlled mod-2 situation to its selected twists and computes both sides explicitly.

**Locators:** Theorem 1.12, introduction p. 4; §4.1, p. 18; rank-zero seed propagation in Lemma 5.3.

### Composition boundary

This is a genuine `p=2` result, but it is not a uniform theorem for the selected BSD-R2-A1 class:

- the route is built on the paper's Assumption `(F)` / mod-2 Heegner-indivisibility package;
- its `BSD(2)` mechanism is in the odd-local-Tamagawa regime;
- the `Q`-side propagation requires seed `BSD(2)` input;
- it proves the result for a constructed twist family, not for every curve satisfying the selected campaign hypotheses.

In particular, protected WP13's even-Tamagawa regime is outside the arithmetic mechanism recorded in §4.1.

## Source D — Yan–Zhu: contemporary non-CM ordinary main conjectures

Xiaojun Yan and Xiuwu Zhu, *Main conjectures for non-CM elliptic curves at good ordinary primes*, arXiv:`2412.20078` (2024; subsequent publication history may be recorded separately).

### Exact interface

The source abstract fixes an elliptic curve `E/Q` and a good ordinary prime

`p > 2`,

with irreducible residual representation. It proves further cases of several Iwasawa main conjectures and, as applications, more cases of the `p`-converse and the `p`-part BSD formula in rank at most one.

**Locator:** arXiv:`2412.20078`, abstract.

### Composition boundary

The prime range is explicitly `p>2`. The low-rank `p`-part BSD application therefore does not supply the selected `p=2` theorem.

## Joint bounded disposition

The four screened interfaces support the following exact route diagnosis:

1. Barrios–Mok can transport a modulo-rational-squares BSD statement across suitable low-rank twists; it does not supply unsquared `2`-adic length.
2. Jetchev supplies the tempting Tamagawa-aware Kolyvagin upper bound only after restricting to odd `p`.
3. Kriz–Li genuinely proves and propagates `BSD(2)`, but only on a restricted Heegner-congruence/twist lane with odd local Tamagawa control and seed inputs; it does not cover the full selected class.
4. Yan–Zhu's contemporary non-CM ordinary main-conjecture application explicitly assumes `p>2`.

None of these four interfaces, as stated, is a uniform exact theorem determining

`len_Z2 Sha(E/Q)[2^infinity] + sum_{ell|N} ord_2(c_ell)`

from the selected normalized complex derivative for every `BSD-R2-A1` curve.

This is a statement about the screened interfaces only. It is not a claim that no such theorem exists elsewhere and is not a novelty or priority statement.

## Downstream admissible use

MATHSOLVE may use this audit to:

- prove that modulo-square information is weaker than the exact selected `ord_2` target;
- reject direct specialization of Jetchev or Yan–Zhu to `p=2`;
- classify Kriz–Li as a restricted positive `BSD(2)` lane rather than a uniform theorem;
- sharpen the current mathematical dependency after exhausting these named escape routes.

MATHSOLVE may not use this audit to infer the selected BSD formula, to infer global literature nonexistence, or to manufacture a `p=2` theorem absent from a source.

## Provider disposition

`QUALIFIED_P2_LENGTH_ROUTE_SCREEN`

The unsquared uniform `p=2` arithmetic-length interface remains provider debt unless established in-package or separately admitted from another exact source.