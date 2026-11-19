# OAI-26 F003 — independent Eisenstein ideal-count proof of the Möbius harmonic mass bound

**Assignment:** `GCL-OAI26-F003-HARMONIC-MASS-RECONSTRUCTION/1`  
**Exact upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Source theorem:** `Moments/MobiusHarmonicMass.full_mass_subpower`, Git blob `c0002eda3a620d5f3c222aa4b27c7510557f221a`, consumed by `Moments/FirstDivisorSupport.supported_harmonic_mass`, blob `fc48eae117d7d2f0e66427127bd82b50ff8dc683`, then `Moments/FirstDivisorCommonBound.actual_supported_annular_harmonic`, blob `36607a6a9a764e918f3c79898f7561a6d836cdc4`.  
**Independent exact-arithmetic test:** [f003_eisenstein_ideal_harmonic_adversary.py](f003_eisenstein_ideal_harmonic_adversary.py).  
**Disposition:** `F003_MOBIUS_HARMONIC_MASS_ALTERNATIVE_PAPER_PROOF_PASS__BLOCK_TO_COMMON_ENERGY_AND_MAIN_ERROR_ANALYTIC_OPEN`.

## 1. Statement actually needed in the source

For any `B≥0` and `δ>0`, the source proves there exists a constant `C>0` such that, for sufficiently large `Z`, every finite selection `Dset` of ideals satisfying

`μ(I)≠0 and I∈Dset  ==>  N(I)≤Z^B`

obeys

`Σ_{I∈Dset} |μ(I)|/N(I) ≤ C Z^δ`.

The source uses a dyadic shell count bound `256` and bounds the number of selected shells by a logarithm. The following proof reconstructs this estimate **independently** directly from the geometry and six-unit quotient of the Eisenstein integers, proving a stronger explicit constant. Its only mathematical prerequisites are: `O=ℤ[ω]` is a principal ideal domain, its nonzero units are `{±1,±ω,±ω²}`, and the principal ideal norm equals `a²-ab+b²` for `a+bω`. These are standard Eisenstein arithmetic facts, not the controversial seven-eighths zero-free estimates.

## 2. Elementary all-scale ideal count

Set `ω=(-1+√(-3))/2`. For `z=a+bω ≠0`,

```text
N(z)=a²−ab+b² ≥ (a²+b²)/2.
```

The inequality follows from `2|ab|≤a²+b²`. If `1≤N(z)≤X` with `X≥1`, then `|a|,|b|≤√(2X)`.

The number of lattice points satisfying these coordinate inequalities is at most

`(2√(2X)+1)² ≤ (4√X)²=16X`,

where `2√2+1<4` and `X≥1`. Exclude the origin. Because `O` is a PID and the six units act **freely** on nonzero elements, exactly six elements generate each nonzero ideal. Therefore

```text
A(X) := # { nonzero ideals I of O : N(I)≤X }
      ≤ (16/6)X = (8/3)X                     (X≥1).
```

The inequality counts *all* ideals, not only squarefree ideals or divisors in a particular packet.

## 3. Dyadic harmonic estimate with explicit smaller constant

For any `Y≥1`, the number of nonzero ideals in the half-open norm interval `[Y,2Y)` is at most `A(2Y)≤(16/3)Y`. Each summand satisfies `1/N(I)≤1/Y`. Hence

```text
Σ_{Y≤N(I)<2Y} 1/N(I) ≤ 16/3.             (†)
```

This improves the source's `256` in the same shell-mass role by elementary planar geometry; it does not indicate a flaw in the original (looser) source theorem.

Since a nonzero ideal has positive integer norm, the intervals `[2^j,2^{j+1})`, `j=0,1,2,...`, partition all nonzero ideal norms. With `X≥1`, at most `1+floor(log₂ X)` shells meet `[1,X]`. By (†),

```text
Σ_{0≠I, N(I)≤X} 1/N(I)
 ≤ (16/3)(1+log₂ X)
 = (16/3)(1+log X/log 2).                (‡)
```

This is uniform over *all* ideals and therefore dominates any finite chosen subfamily.

## 4. From logarithmic growth to the source's arbitrarily small power

Put `X=Z^B` with `Z≥1`, `B≥0`. Then (‡) gives

`Σ 1/N(I) ≤ (16/3)[1+(B/log 2)log Z]`.

For every `δ>0` and `Z≥1`,

`log Z ≤ Z^δ/(eδ)`.

Proof: writing `u=log Z≥0`, the function `u exp(−δu)` has maximum `1/(eδ)` at `u=1/δ`. Since also `1≤Z^δ`,

```text
Σ_{0≠I,N(I)≤Z^B} 1/N(I)
 ≤ C(B,δ) Z^δ

C(B,δ) = (16/3) (1 + B/(e δ log 2)).
```

Now `|μ(I)|∈{0,1}` for nonzero ideals of a Dedekind domain. Terms with `μ(I)=0` contribute zero; every term with `μ(I)≠0` in a source-admissible finite ideal set has `N(I)≤Z^B`. Thus

```text
Σ_{I∈Dset} |μ(I)|/N(I) ≤ C(B,δ) Z^δ.
```

This is exactly the **subpower Möbius harmonic mass obligation** of the pinned source, with a concrete valid constant and without invoking its `selected_card_subpower` or `divisor_dyad_card` proof. The zero ideal contributes no nonzero Möbius mass in the source's decomposition; the proof is stated for nonzero ideals to avoid the zero-norm denominator.

The source's more specialized theorem `FirstDivisorSupport.supported_harmonic_mass` filters a finite ideal set by `N(I)≤H/N(D)≤Z^B`. It follows immediately from the same estimate because `N(D)≥1` for nonzero `D`, and any selected nonzero `I` is in the cap.

## 5. Executable independent adversary

The test program enumerates every integer pair `(a,b)` with `a²−ab+b²≤16,384`, excluding `(0,0)`. It computes exact counts for every norm, validates that each element count is divisible by six, and counts the corresponding principal ideals by dividing by six. Among its checks:

- Exact norm multiplicities: norm 1→1 ideal, 2→0, 3→1, 4→1, 5→0, 7→2, 9→1, 25→1, 49→3.
- For every integer `1≤X≤16,384`, check `3 A(X)≤8X` using integer arithmetic.
- For every dyadic shell within the same norm range, sum all ideal weights `1/N(I)` using exact `fractions.Fraction` and check `≤16/3`.
- At eight representative scales, check the all-ideal harmonic sum against the appropriate number of dyadic shells.
- A deliberately incorrect calculation that fails to divide by the six global units is rejected already at norm one (`6>16/3`).
- Independently check `2N(z)≥a²+b²` over the full integer box `[-100,100]²`; the general inequality has the separate paper proof in §2.

Exact recorded finite replay: `MAX_NORM=16,384`; 15 dyadic shells, all PASS. The largest *observed* dyadic shell weighted sum in this range was `1`, well below the rigorous bound `16/3`. This finite result corroborates, but does **not substitute for**, the all-scale proof above. The executable only uses Python's standard library and has no upstream Mathlib, Hecke or OAI imports.

## 6. Remaining analytic obstacle and scientific scope

This closes the *independent mathematical reconstruction of one downstream harmonic-mass input*. It does **not** independently prove `Moments/FirstDivisorCommonBound.actual_supported_annular_harmonic` in its entirety: that theorem also invokes `actual_supported_annular_block`, a nontrivial estimate transferring left/right common energies to a block norm, with coarse/dead divisor cases. Nor does it prove the child main/error normalized Gauss-source bounds in `Energy/CanonicalMainHomogeneous` and `Energy/CanonicalErrorHomogeneous`.

Next independent analytic target: `Moments/FirstDivisorCommonBound.actual_supported_annular_block`, its active-Möbius/coarse-support cases, actual Cauchy–Schwarz and annular Fourier normalization; in parallel, `Energy/CanonicalMainSubsets.actual_original_subsets_main_power` and `Energy/CanonicalErrorSubsets.actual_original_subsets_error_power` at the homogeneous child-estimate interface.

**No universal new number-theory theorem is claimed as novel:** the logarithmic ideal harmonic mass bound is standard lattice-counting arithmetic. This is an independent proof and sharper explicit elementary constant in the pinned GCL review context, not proof of seven-eighths nonvanishing and not MATHCERT.
