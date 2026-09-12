# BSD-001 source audit — fixed-`2` height nondegeneracy and derived-height bypass screen

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP38-P2-K-HEIGHT-NONDEGENERACY-AND-NORMALIZATION`.
- Protected MATHFORGE predecessor: `eceaf6f0f2e10e5bd48afd1ca57f9245669202de`.
- Protected MATHSOLVE predecessor: `a9b823e526059ffefb62b3d331d85f04c456a97d`.
- Screen date: `2026-09-12`.
- Disposition: `BOUNDED_NO_APPLICABLE_LITERAL_P2_NONDEGENERACY_OR_DERIVED_BYPASS_FOUND`.
- Claim class: source/applicability screen only; not a theorem-nonexistence statement.

## Protected query

WP37 establishes that Nekovář's cyclotomic Selmer-complex Bockstein and first height exist integrally at `p=2` over the protected WP09 imaginary quadratic field `K` because `K` is totally imaginary. It leaves the exact boundary

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

The bounded query is:

> For the selected non-CM elliptic curve branch with good ordinary reduction at `2`, irreducible/surjective `E[2]`, and a protected imaginary quadratic field `K` in which every prime dividing `2N` splits, does a screened source prove nondegeneracy/primitivity of the first cyclotomic Nekovář height at the fixed prime `2`, or provide a literal-`p=2` derived-height theorem that bypasses first-height nondegeneracy while retaining an integral `Z_2` lattice?

This audit does not ask whether such a theorem can exist. It records only the applicability of the exact screened sources below.

## Source A — Macias Castillo–Sano 2026

Daniel Macias Castillo and Takamichi Sano, *On Selmer complexes, Stark systems and derived p-adic heights*, arXiv:2603.23978v1 (25 March 2026).

Primary public source inspected: `https://arxiv.org/html/2603.23978`.

This is the closest contemporary source structurally. It proves comparison theorems for Nekovář Selmer complexes and Poitou–Tate complexes, relates determinant lines to Stark systems, constructs Heegner-point Stark systems, and compares Bertolini–Darmon derived heights with Nekovář's higher-height formalism.

However, §1.2 states explicitly:

`For simplicity, we assume that p is odd throughout this article.`

This is a global hypothesis of the article, preceding the Selmer-complex, Stark-system, Heegner-point, and derived-height results. Therefore none of the paper's arithmetic applications can be specialized mechanically to the fixed prime `p=2` in BSD-001.

**Disposition:** `INAPPLICABLE_AT_FIXED_P2_GLOBAL_ODD_PRIME_HYPOTHESIS`.

The paper remains a structural comparator only. It is not admitted as a literal-`p=2` determinant, Stark-system, or derived-height theorem.

## Source B — Howard derived heights

Benjamin Howard, *Derived p-adic heights and p-adic L-functions*, arXiv:1202.6343.

Primary public source inspected: `https://arxiv.org/html/1202.6343`.

The paper develops derived `p`-adic heights, relates higher derivatives of cohomological `p`-adic `L`-functions to derived heights, and studies degeneracy via Iwasawa-module structure. It is therefore a natural candidate for bypassing a zero first height.

The introduction fixes the prime globally by the literal hypothesis

`Fix forever a rational prime p>2.`

Hence the derived-height and Iwasawa-module results in this source are not literal-`p=2` results.

**Disposition:** `INAPPLICABLE_AT_FIXED_P2_GLOBAL_P_GT_2_HYPOTHESIS`.

No Howard derived-height statement from this source is imported into BSD-001 at `p=2`.

## Source C — Heegner points at Eisenstein primes

The screened public source `https://web.math.princeton.edu/~dkriz/Eisenstein.pdf` proves nonvanishing/indivisibility results for Heegner points at Eisenstein primes and includes a `p=2` branch.

The exact `p=2` elliptic specialization is nevertheless incompatible with the protected selected class for two independent reasons.

1. The source is an Eisenstein/residually reducible route. BSD-001 has protected irreducible, in fact surjective, residual representation `E[2]` with image `GL_2(F_2) ~= S3`.
2. In Remark 2.3 the source states that, when `p=2` and the GL2-type abelian variety is an elliptic curve, one must have the trivial residual character and, from Theorem 2.1, the conductor `N` must be a power of `2`. The protected BSD-001 selected class has good reduction at `2`, so `2` does not divide `N`; this does not lie in that `p=2` Eisenstein conductor branch.

The PDF's theorem text and Remark 2.3 were inspected through the public source surface. The environment's screenshot fetch for the relevant PDF page returned a cache-miss error, so this audit does not claim an independent page-image lock or byte digest. The exact text locator remains Remark 2.3 following Theorem 2.1.

**Disposition:** `INAPPLICABLE_RESIDUALLY_REDUCIBLE_AND_CONDUCTOR_BRANCH`.

This source may not be used to infer nondegeneracy for the selected surjective `E[2]`, good-at-`2` branch.

## Existing protected D1c comparator

No new D1c premise is admitted here. The already-protected WP17B/WP17C source records remain controlling:

- Kato's literal-`p=2` ordinary control misses the height-one prime containing `2`; its all-height-one integral upgrade assumes `p != 2`.
- The protected contemporary non-CM ordinary screen records that the closest irreducible-residual main-conjecture results retain odd-prime hypotheses.

A current 2026 comparator, Yan–Zhu, *Main conjectures for non-CM elliptic curves at good ordinary primes* (Journal of Algebra 693 (2026), 372–402), likewise begins by fixing an odd prime and states the cyclotomic application for `p>2`. This corroborates the protected D1c barrier but is not needed to alter it.

## What this screen establishes

The three targeted routes that most directly match WP37's successor query do not discharge D2a:

- the 2026 Selmer-complex/Stark-system/derived-height route is odd-prime throughout;
- Howard's derived-height bypass fixes `p>2` globally;
- the apparent Heegner `p=2` nonvanishing route lies on an Eisenstein/residually reducible conductor branch incompatible with the selected good-at-`2`, surjective-`E[2]` class.

Accordingly the protected successor boundary remains

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

This is a **bounded source/applicability conclusion**, not a claim that no theorem can prove fixed-`2` nondegeneracy.

## Consequence for the research route

The failure of the screened D2a sources is not a reason to stop the campaign. D2b–D2e remain separately executable comparison obligations:

- exact comparison of the Nekovář `K`-Selmer lattice with the protected primitive Kummer/WP20 lattice;
- exact valuation of Disegni interpolation/test-vector factors;
- exact classical Gross–Zagier/WP00 normalization comparison on the same Heegner line;
- exact WP06 descent retaining every `2`-power discrepancy.

A future source that proves literal-`p=2` nondegeneracy or an integral derived-height bypass can be inserted at D2a without invalidating those comparison calculations.

## Claim firewall

This audit does not:

- assert theorem nonexistence;
- prove or assume nondegeneracy of the first `2`-adic height;
- specialize an odd-prime theorem to `p=2`;
- transfer an Eisenstein/reducible result to the selected irreducible branch;
- close D1c;
- close D2;
- prove `BSD-R2-A1`;
- imply MATHCERT certification, novelty, or priority.
