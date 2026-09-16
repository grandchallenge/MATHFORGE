# BSD-001 R5-RES source amendment — Kim refined explicit reciprocity and the exact local normalization

## Record

- Campaign: `BSD-001`.
- Parent provider operation: `grandchallenge/MATHFORGE#225`.
- Downstream theorem operation: `grandchallenge/MATHSOLVE#273`.
- Parent source audit protected at `grandchallenge/MATHFORGE@c84fbed7d6bdae2b36514fea736e0ed52752c6a6`.
- Protected MATHSOLVE R5-PRIM completion: `36202d97e2cd96956c8a4aafa43941f6219776c5`.
- Source: Chan-Ho Kim, *The structure of Selmer groups and the Iwasawa main conjecture for elliptic curves*, final manuscript dated 2025-05-12, especially §3 and Theorem 3.11.
- Source locator: `https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-kim.pdf` and arXiv:2203.12159.
- Claim class: source/dependency refinement only.

## Why this amendment is required

The protected parent R5-RES audit correctly identifies the old Kim–Kim–Sun `(NA)` condition as unavailable on the good-ordinary `p=2` lane. The final Chan-Ho Kim manuscript materially refines that older source interface: it explicitly treats local `p`-power torsion in the integral dual-exponential lattice and derives a refined Kato/Kurihara reciprocity identity without simply assuming that local torsion vanishes.

Therefore downstream MATHSOLVE should not model the missing literal-2 bridge as an unspecified anomalous factor. The exact odd-prime architecture is sharper and must be preserved.

## 1. The refined source handles local p-power torsion explicitly

Section 3 states that its purpose is to connect Kato's Kolyvagin system with Kurihara numbers by:

1. studying the local torsion `E(Q_p)[p]`;
2. computing the integral image of the Bloch–Kato dual exponential map;
3. extending the dual exponential map to torsion coefficients;
4. deriving a refined explicit reciprocity law.

The manuscript explicitly says this **significantly refines** the earlier Kim–Kim–Sun computation.

It defines

`t = length_{Z_p}(E(Q_p)[p^infinity])`

outside the split multiplicative convention, and tracks the local integral lattice through the torsion-coefficient map rather than reducing a rational dual exponential naively modulo the Kolyvagin ideal.

**Source disposition:** `LOCAL_TORSION_FACTOR_EXPLICITLY_TRACKED`.

## 2. Exact odd-prime reciprocity formula

Theorem 3.11 assumes:

- `p >= 5`;
- the residual representation is surjective;
- the Manin constant is prime to `p`.

For a Kolyvagin index `n`, with the source's torsion dual-exponential normalization `xi`, it proves

`xi o exp^*_{omega_E} o loc^s_p(kappa_n^Kato) = u * p^t * delta_tilde_n`

in `Z_p / I_n Z_p`, where `u` is a unit and

`p^t = #E(Q_p)[p^infinity]`.

Thus the explicit analytic witness is not the raw Kurihara number alone. The local torsion contribution is an exact multiplicative factor in the integral reciprocity identity.

The theorem is a derivative of Kato's explicit reciprocity law combined with the integral lattice computation and the modular-symbol derivative calculation.

**Source disposition:** `REFINED_RECIPROCITY_EQUALS_UNIT_TIMES_LOCAL_TORSION_TIMES_KURIHARA_NUMBER`.

## 3. Consequence for the p=2 replay target

The protected parent audit's qualitative conclusion remains correct: no literal-2 theorem is supplied. But the replay obligation can now be stated exactly.

A literal-2 theorem must reproduce, in the selected protected normalization, the source's torsion-coefficient construction and prove an identity of the shape

`normalized_local_map(kappa_n^Kato) = unit * 2^t * delta_tilde_n`

or an equivalent corrected identity, with

`t = length_{Z_2}(E(Q_2)[2^infinity])`,

while accounting for any additional `2`-adic contribution of the chosen modular-symbol period / Manin constant normalization.

The replay must not divide by `2^t` unless integrality of the normalized target after that division is separately proved. At finite mod-2 level, multiplication by `2^t` kills the right-hand side whenever `t>0`; hence a naive mod-2 Kurihara witness is then insufficient. The exact local torsion exponent must be incorporated into the finite-detection theorem.

When `t=0`, the local-torsion factor itself is a unit, but literal-2 applicability of Theorem 3.11 still does not follow: its proof and statement begin at `p>=5`, and the period/Manin-constant and torsion-coefficient constructions still require a literal-2 replay.

## 4. The correct first downstream theorem boundary

The parent audit named

`MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY`.

This amendment retains that identifier but gives it exact required content:

1. construct the torsion-coefficient Bloch–Kato dual-exponential / equivalent local regulator at `p=2` on the selected good-ordinary lane;
2. determine its exact integral image lattice;
3. track `t = length(E(Q_2)[2^infinity])` explicitly;
4. prove a derivative Kato reciprocity identity comparing a selected finite Kato/Kolyvagin component to a Kurihara/modular-symbol quantity, up to a **2-adic unit after all explicit local/period factors are extracted**;
5. prove compatibility with the protected finite-layer detector from R5-PRIM;
6. identify and retain any even Manin-constant / integral-period contribution rather than assuming it is a unit.

This is strictly stronger and more precise than merely removing the old `(NA)` hypothesis.

## 5. What is already protected downstream and need not be reproved

This source amendment does not reopen:

- WP60M selected defect exclusion;
- WP60R characteristic-two localization/core graphs and Kolyvagin-system freeness;
- WP60S inverse-limit compatibility;
- WP60T literal-2 Kato derivative construction;
- WP23/WP46A local-control/support calculations;
- R5-LIFT determinant membership;
- R5-PRIM's equivalence between height-one primitivity and residual inverse-limit nonvanishing, including finite detection.

Those results constrain the normalization that the new reciprocity bridge must match.

## 6. Source-level disposition after amendment

The parent source disposition remains

`QUALIFIED_REPLAY_ARCHITECTURE_WITH_P2_ANOMALOUS_ORDINARY_RECIPROCITY_GAP`,

but the gap is now sharpened to a specific odd-prime theorem interface:

`Kim Theorem 3.11 at literal p=2, with exact local 2-power torsion and period normalization retained`.

No direct source-current theorem located in this operation supplies that literal-2 extension.

## Claim firewall

This amendment does not establish:

- Kim Theorem 3.11 at `p=2`;
- integrality after dividing by `2^t`;
- oddness of any selected Manin constant;
- nonvanishing of a Kurihara number or normalized Kurihara quantity on the selected lane;
- `MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY`;
- `MISSING_P2_RESIDUAL_CYCLOTOMIC_KATO_KOLYVAGIN_NONVANISHING`;
- R5-RES, R5-PRIM, D2d, BSD-R2-A1, novelty/priority, public certification or MATHCERT certification.
