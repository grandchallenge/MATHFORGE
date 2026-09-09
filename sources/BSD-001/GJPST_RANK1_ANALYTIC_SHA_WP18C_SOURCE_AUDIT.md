# BSD-001 — GJPST rank-one analytic-Sha normalization audit for WP18C

## Disposition

`QUALIFIED_EXACT_RANK1_ANALYTIC_NORMALIZATION_SOURCE`

This audit qualifies one narrow external theorem interface for downstream use in `BSD-R2-A1-WP18C`:

> For every elliptic curve `E/Q` of rank one and conductor at most `1000`, the GJPST analytic BSD order `#Sha(E)_an` is exactly `1` in the normalization stated in their Definition 1.2 / Conjecture 1.1.

The qualified statement is the exact rank-one analytic-order conclusion proved in the proof of Theorem 1.8 of Grigorov–Jorza–Patrikis–Stein–Tarniţă (2009). It is not an admission of every later theorem in that paper.

## Primary source

Grigor Grigorov, Andrei Jorza, Stefan Patrikis, William A. Stein, Corina E. Tarniţă,

**Computational verification of the Birch and Swinnerton-Dyer conjecture for individual elliptic curves**, Mathematics of Computation 78 (2009), no. 268, 2397–2425.

DOI: `10.1090/S0025-5718-09-02253-4`.

Public author copy used for audit:

`https://ctarnita.scholar.princeton.edu/document/95`

Companion author project page:

`https://wstein.org/papers/bsdalg/`

## Exact source statement used

GJPST Definition 1.2 defines

`#Sha(E)_an = L^(r)(E,1) * (#E(Q)_tor)^2 / (r! * Omega_E * Reg_E * product_p c_p)`.

In the proof of Theorem 1.8 the authors state:

1. Cremona computed a numerical approximation to `#Sha(E)_an` to at least ten digits for every rank-one curve of conductor at most `1000`;
2. Gross–Zagier gives an explicit formula proving that `#Sha(E)_an` is rational with bounded denominator;
3. their computed denominator bound for all such rank-one curves is at most `5,248,800`, far smaller than the retained decimal separation scale;
4. therefore `#Sha(E)_an = 1` **exactly** for each rank-one elliptic curve of conductor at most `1000`.

This is the admitted conclusion. A floating-point recognition by itself is not admitted; the source's rationality and denominator bound are material to exactness.

## Normalization comparison with protected WP00

The source normalization matches the protected WP00 target on every factor material to WP18C.

### `L(E,s)`

GJPST uses the Hasse–Weil `L(E,s)` and its ordinary derivative `L^(r)(E,1)/r!`, not the derivative of the completed `Lambda`-function.

WP00 likewise fixes the complete finite Euler-product `L(E,s)` and uses `L^(r)(E,1)/r!` in the strong leading-term formula.

**Disposition:** exact match.

### Real period

GJPST defines

`Omega_E = integral_{E(R)} |omega|`,

where

`omega = dx/(2y + a1*x + a3)`

is the invariant differential attached to a minimal Weierstrass model.

WP00 fixes the same whole-real-locus period for the minimal Néron differential.

**Disposition:** exact match. No `Omega^+` half/double substitution is permitted.

### Regulator

GJPST defines `Reg_E` as the absolute determinant of the canonical height pairing on `E(Q)/tors`.

WP00 fixes the determinant of the Néron–Tate pairing on a basis of the free Mordell–Weil quotient.

**Disposition:** exact match.

### Tamagawa factors

GJPST uses

`c_p = [E(Q_p):E_0(Q_p)]`.

WP00 uses the same Néron local Tamagawa number.

**Disposition:** exact match.

### Rational torsion

Both formulas divide by `(#E(Q)_tors)^2`.

**Disposition:** exact match.

## Exact downstream consequence

For rank one, the qualified source identity is

`1 = L'(E,1) * (#E(Q)_tors)^2 / (Omega_E * Reg_E * product_l c_l)`.

Therefore

`L'(E,1)/(Omega_E Reg_E) = (product_l c_l)/(#E(Q)_tors)^2`

**exactly**.

For a downstream curve with odd rational torsion this implies

`ord_2(L'(E,1)/(Omega_E Reg_E)) = sum_{l|N} ord_2(c_l)`.

For a downstream curve with trivial rational torsion the equality holds already as a positive rational identity

`L'(E,1)/(Omega_E Reg_E) = product_l c_l`.

Thus for the WP00/WP16 definition

`delta_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E)) - sum_{l|N} ord_2(c_l)`,

the admitted source conclusion gives

`delta_2(E)=0`

for any rank-one conductor-`<=1000` curve with odd rational torsion, provided the protected downstream records establish the rank, conductor, torsion and local Tamagawa inputs.

## Applicability to the protected WP18A controls

The source theorem range is broad enough for both protected controls:

- `53a1`: rank one, conductor `53`, trivial rational torsion;
- `203b1`: rank one, conductor `203`, trivial rational torsion.

No non-CM, residual-representation, ordinary-at-2, Tamagawa-parity, or optimal-curve hypothesis is needed for the specific admitted analytic-order conclusion from the proof of Theorem 1.8.

The protected WP18A/WP18B records, not this source audit, own those curve-specific facts.

## Correction / erratum audit

The author project page warns that Lawson–Wuthrich (2015/2016) identified a serious mistake in a later Galois-cohomology lemma of GJPST.

Lawson–Wuthrich, **Vanishing of some Galois cohomology groups for elliptic curves**, arXiv:1505.02940 / Springer Proc. Math. Stat. 188 (2016), explicitly state that the mistake affects the GJPST attempt to extend Cha's odd-prime Kolyvagin bound: their discussion concerns an odd prime `p`, Galois cohomology of `E[p]`, and the corrected Heegner-index bound.

The WP18C interface admitted here does **not** use that argument. It uses only:

- Definition 1.2 / Conjecture 1.1 normalization;
- the proof of Theorem 1.8 establishing exact analytic order `1` for rank-one conductor-`<=1000` curves from Gross–Zagier rationality, a denominator bound, and controlled numerical approximation.

The source's separate `p=2` descent theorem is also not needed for WP18C because protected MATHSOLVE WP18B already establishes the arithmetic `2`-primary Sha side independently.

**Correction disposition:** the known later odd-prime cohomology error does not invalidate the admitted WP18C analytic-normalization statement.

## What is not admitted

This audit does **not** admit or assert:

- a uniform proof of `BSD-R2-A1`;
- a new `p=2` Iwasawa/Fitting-control theorem;
- the flawed uncorrected odd-prime cohomology theorem from the original paper;
- any claim that a decimal approximation alone identifies an exact rational value;
- analytic Sha as a substitute for the independently computed finite Selmer group;
- MATHCERT certification;
- novelty, priority, patentability, or commercial claims.

## Downstream use contract

MATHSOLVE may use this source only to identify the **analytic** WP00-normalized quotient on a curve already proved downstream to have:

- rank one;
- conductor at most `1000`;
- the stated rational torsion;
- the exact WP00 Tamagawa factors.

The arithmetic Sha/Selmer side must remain independently sourced or proved. In particular, for WP18C the intended composition is:

`GJPST exact #Sha_an=1`

`+ protected WP18A exact Tamagawa data`

`+ protected WP18B independent Sha[2^infinity]=0`

`=> exact individual-control delta_2(E)=0 and equality with the unit Fitting valuation`.

That composition is an individual-control theorem, not uniform selected-class closure and not certification.
