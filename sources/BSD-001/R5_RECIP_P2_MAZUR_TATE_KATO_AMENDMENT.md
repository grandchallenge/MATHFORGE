# BSD-001 R5-RECIP source amendment — literal-p=2 Kato reciprocity and modular-element integrality

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#230`.
- Downstream theorem operation: `grandchallenge/MATHSOLVE#278`.
- Protected entering provider: `grandchallenge/MATHFORGE@8b16da7ec245cfef30c318518401b0f474fc1fb8`.
- Parent source decomposition: `sources/BSD-001/R5_RECIP_P2_KIM_KKS_DEPENDENCY_DECOMPOSITION.md`.
- Claim class: source/dependency amendment only.

Primary sources:

1. Masato Kurihara and Rei Otsuki, *On the Growth of Selmer Groups of an Elliptic Curve with Supersingular Reduction in the Z_2-extension of Q*, Pure Appl. Math. Q. 2 (2006), 557–568, especially §1.2 and §2.2.
2. Christian Wuthrich, *On the integrality of modular symbols and Kato's Euler system for elliptic curves*, Documenta Math. 19 (2014), 381–402, especially §§1–3 and the class 17a example.
3. Kazuya Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), Theorems 12.4 and 12.5, used only through the exact literal-2 interface explicitly invoked by Kurihara–Otsuki.
4. Glenn Stevens, *Stickelberger elements and modular parametrizations of elliptic curves*, Invent. Math. 98 (1989), 75–106, used only as the modular-element integrality source cited by Kurihara–Otsuki; no stronger Stevens conjectural statement is imported.

## 1. Kato explicit reciprocity is genuinely available at literal p=2 in the cyclotomic tower

Kurihara–Otsuki explicitly state that the proofs of the relevant parts of Kato Theorems 12.4 and 12.5 apply in their cyclotomic `Z_2` setting even at `p=2`. They construct compatible Kato classes

`z_{Q_infinity}=(z_{Q_n}) in lim H^1(Q_n,T)`

and record, for even characters, the dual-exponential interpolation formula

`sum_sigma psi(sigma) exp^*(sigma z_{Q_n}) = omega_E * L(E,psi,1)/Omega_E`.

For the trivial character they write explicitly

`exp^*(z_Q)
 = omega_E * (1-a_2/2+1/2) * L(E,1)/Omega_E`.

This is direct peer-reviewed evidence that the Kato explicit-reciprocity mechanism itself is not invalid merely because the prime is `2` in a cyclotomic `Z_2` tower.

The local lattice computed in that paper is supersingular-specific and is **not** imported to the selected good-ordinary lane.

**Source disposition:** `KATO_CYCLOTOMIC_EXPLICIT_RECIPROCITY_LITERAL_P2_ADMITTED`.

## 2. Literal-p=2 modular elements can be integral even though individual modular-symbol denominators are subtle

Kurihara–Otsuki normalize their real modular symbols by a Néron period and form Mazur–Tate modular elements `theta_{Q_n}`. In their literal-2 setting they state:

- `E[2]` is irreducible;
- the Manin constant is therefore prime to `2` in their setting;
- consequently `theta_{Q_n}` lies in the integral group ring `Z_2[Gal(Q_n/Q)]`, citing Stevens Corollary 3.15 and related modular-parametrization results.

The downstream selected ordinary lane has its own independently protected irreducible/surjective `E[2]` and semistable Manin/differential `2`-unit results. This source record does **not** infer the selected-lane modular-element integrality automatically from Kurihara–Otsuki's supersingular theorem; it admits the existence of a genuine literal-2 integral modular-element formalism and identifies the exact kind of integral object that should be replayed.

**Source disposition:** `LITERAL_P2_MAZUR_TATE_GROUP_RING_INTEGRALITY_ARCHITECTURE_ADMITTED`.

## 3. Individual p=2 modular-symbol integrality must not be assumed

Wuthrich defines the modular-symbol lattice from the primitive real/imaginary periods of the Néron period lattice and proves strong denominator control for odd semistable primes. He explicitly warns that the corresponding result does not hold in general at `p=2`.

His class `17a` example exhibits the failure: the optimal curve `17a1` has rational Mordell–Weil group `Z/4Z`, and the modular-symbol lattice has a genuine power-of-two discrepancy; Wuthrich states that this shows the odd-prime lattice lemma is not valid for `p=2`.

Therefore downstream R5-RECIP must not replace the literal-2 modular-element problem by the stronger unsupported assertion

`[a/n]^+ in Z_2 for every a,n`.

The selected lane may rule out Wuthrich's failure mechanism using its protected residual irreducibility and odd-isogeny structure, but that is a new mathematical replay to be proved in MATHSOLVE.

**Source disposition:** `RAW_P2_MODULAR_SYMBOL_INTEGRALITY_NOT_SOURCE_AVAILABLE`.

## 4. Period conventions must remain explicit

The source conventions are not interchangeable without a factor-of-two check.

- Wuthrich's `Omega_E^+` is the least positive real period in the Néron period lattice.
- Kim's R5-RES source uses the real Néron period defined from the integral of a minimal invariant differential over `E(R)`.
- Kurihara–Otsuki explicitly normalize their real symbol by a Néron period written as twice a least positive real period in their convention.

At literal `2`, these conventions can differ by a nonunit real-component factor. A downstream proof must either work directly with an integral Mazur–Tate/relative-homology element or carry the real-component factor explicitly. It may not silently identify the three period normalizations.

**Source disposition:** `REAL_PERIOD_FACTOR_OF_TWO_MUST_BE_TRACKED_AT_P2`.

## 5. Consequence for the downstream proof architecture

The protected parent decomposition remains correct, but its analytic obligation is sharpened.

The downstream theorem should aim at an **integral group-ring derivative object**, not at raw coefficientwise `2`-integrality of every plus modular symbol.

A valid literal-2 replay may proceed by:

1. proving selected-lane `2`-saturation of the relevant relative-homology / Mazur–Tate lattice using residual irreducibility and the protected semistable optimal parametrization;
2. carrying any real-component factor explicitly;
3. applying the algebraic Kolyvagin derivative operator to that integral group-ring object;
4. combining the result with the protected literal-2 local dual-exponential lattice and Kato's literal-2 cyclotomic explicit reciprocity interface.

This architecture is compatible with Kim Theorem 3.11's integral-lattice bookkeeping without asserting the printed `p>=5` theorem itself at `p=2`.

## 6. Source-level disposition

`P2_KATO_RECIPROCITY_ADMITTED_AND_MAZUR_TATE_INTEGRAL_OBJECT_ROUTE_IDENTIFIED`.

This materially narrows the remaining R5-RECIP debt. The Kato explicit-reciprocity law itself is no longer a source-level small-prime blocker. The remaining analytic work is to prove the selected-lane integral modular-element / derivative normalization with exact real-period factors.

## Claim firewall

This source amendment does not establish:

- selected-lane coefficientwise raw modular-symbol integrality at `2`;
- selected-lane Mazur–Tate integrality without a downstream proof;
- the literal-2 KKS derivative theorem in the selected normalization;
- the full normalized Kato/Kurihara reciprocity theorem;
- a nonzero normalized finite witness;
- residual Kato/Kolyvagin nonvanishing;
- R5-RES or R5-PRIM;
- D2d or BSD-R2-A1;
- novelty, priority, public certification or MATHCERT certification.
