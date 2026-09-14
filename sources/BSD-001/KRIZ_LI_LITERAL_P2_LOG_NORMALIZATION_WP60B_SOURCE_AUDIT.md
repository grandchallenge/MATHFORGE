# BSD-001 source audit — Kriz–Li literal-`p=2` logarithm normalization

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#188`.
- Downstream execution tracker: `grandchallenge/MATHSOLVE#215`.
- Protected MATHFORGE baseline: `e44baeeed5d508fd4e5332c883c837951e51c000`.
- Protected MATHSOLVE baseline: `20a980fd8fb3e3a4cceabf0e37af838a16c1608e`.
- Constitutional issuance anchor: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Primary source: Daniel Kriz and Chao Li, *Goldfeld's conjecture and congruences between Heegner points*, Forum of Mathematics, Sigma 7 (2019), e15, DOI `10.1017/fms.2019.9`.
- Source locations checked: Theorem 1.12 and its Assumption `(F)`; Theorem 1.16; §5.1; Lemma 5.4.
- Disposition: `QUALIFIED_LITERAL_P2_LOG_NORMALIZATION_AND_INDIVISIBILITY_INTERFACE`.
- Claim class: bounded source/applicability evidence only; no theorem promotion or certification.

## Exact downstream query

WP60B asks for the exact literal-`p=2` Kriz–Li logarithmic condition, including every normalization factor, so that MATHSOLVE can compare it with the protected decomposition

`P_K(f)=m_K(f)P+T`.

This audit records only the source interface. It does not perform the downstream comparison with `m_K(f)`.

## Heegner point and differential normalization

Kriz–Li fix an elliptic curve `E/Q` of conductor `N`, an imaginary quadratic field `K` satisfying the Heegner hypothesis for `N`, and a modular parametrization

`pi_E:X_0(N)->E`.

They denote by `P in E(K)` the corresponding Heegner point, defined up to sign and torsion with respect to that fixed parametrization.

They then choose the invariant differential `omega_E` by the exact normalization

`pi_E^*(omega_E)=f(q) dq/q`,

where `f` is the normalized newform attached to `E`.

The paper explicitly notes that this `omega_E` need not be the Néron differential when `E` is not the optimal curve in its isogeny class.

**Disposition:** `EXACT_PARAMETRIZATION_NORMALIZED_DIFFERENTIAL`.

## Assumption `(F)` at literal `p=2`

Theorem 1.12 assumes `E(Q)[2]=0` and the existence of an imaginary quadratic field `K` satisfying the Heegner hypothesis for `N` such that:

1. `2` splits in `K`; and
2. the normalized logarithmic quantity

   `(# E_tilde^ns(F_2) / 2) * log_{omega_E}(P)`

   is nonzero modulo `2`.

Equivalently, using the paper's displayed typography,

`#E_tilde^ns(F_2) * log_{omega_E}(P) / 2 != 0 (mod 2)`.

For good reduction at `2`, `E_tilde^ns(F_2)=E(F_2)`, so the cardinality is

`#E(F_2)=3-a_2`.

The factor `1/2` is part of the source condition and must not be dropped.

**Disposition:** `EXACT_LITERAL_P2_ASSUMPTION_F`.

## Congruence propagation

Theorem 1.16 gives a congruence between suitably Euler-factor-normalized `p`-adic logarithms of Heegner points on congruent elliptic curves. In the `p=2` quadratic-twist application, the paper uses this to propagate the nonvanishing modulo `2` of the normalized logarithmic expression to selected twists.

This theorem does not prove that every elliptic curve in an arbitrary external selected class admits a field `K` satisfying `(F)`.

**Disposition:** `CONGRUENCE_PROPAGATION_NOT_UNIFORM_FIELD_EXISTENCE`.

## Lemma 5.4 and the exact consequence used in the BSD(2) argument

In §5 the paper assumes `(F)` and, in Theorem 5.1, additionally assumes the local Tamagawa number `c_2(E)` is odd (with an additional odd-Manin-constant condition in the additive-at-2 case).

Lemma 5.4 proves that the right-hand side of the Gross–Zagier/BSD index identity is a `2`-adic unit. The proof argues that if the Heegner point were divisible by `2`, then the normalized logarithmic expression in `(F)` would vanish modulo `2`, a contradiction.

Thus the source supports the implication, under its stated hypotheses,

`Assumption (F) => the Heegner point P is indivisible by 2`.

The paper's subsequent BSD(2) propagation over `Q` uses further seed-BSD hypotheses. Those seed hypotheses are not part of the present admitted interface.

**Disposition:** `ASSUMPTION_F_IMPLIES_HEEGNER_2_INDIVISIBILITY_UNDER_STATED_LOCAL_HYPOTHESES`.

## What the source does not supply

The source does not prove:

- that every curve in protected `BSD-R2-A1` admits a WP09-compatible field satisfying `(F)`;
- that `(F)` is independent of, equivalent to, or stronger than the parity of the protected Heegner index `m_K(f)`;
- an exact value of `ord_2(m_K(f))` in the WP00/WP58A normalization;
- an exact value of the protected twist quotient `ord_2(lambda_D)`;
- a direct exact theorem for `R_2(E,K,f)`;
- the selected theorem `BSD-R2-A1`.

Those are downstream mathematical questions for MATHSOLVE.

## Provider conclusion

The exact literal-`p=2` source interface is now pinned:

`(F) <=> [2 splits in K] and [(#E_tilde^ns(F_2)/2) log_{omega_E}(P) != 0 mod 2]`,

with `omega_E` normalized by

`pi_E^*omega_E=f(q)dq/q`.

Under the paper's §5 local hypotheses, `(F)` forces the Heegner point to be indivisible by `2`.

No uniform existence theorem for a WP09-compatible `(F)` field is admitted.

**Disposition:** `QUALIFIED_LITERAL_P2_LOG_NORMALIZATION_AND_INDIVISIBILITY_INTERFACE`.

## Claim firewall

This audit does not establish:

- a uniform Kriz–Li `(F)` field for the selected class;
- parity or a valuation of `m_K(f)`;
- a WP00 normalization comparison;
- BSD(2) for the protected selected curve;
- `BSD-R2-A1`;
- novelty, priority, or MATHCERT certification.
