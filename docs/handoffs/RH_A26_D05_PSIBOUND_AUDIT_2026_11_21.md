# RH-A26 D05 — PsiBound reconstruction, independent prime-budget lemma, and nonvacuity

**Date:** 2026-11-21  
**Original-source identity:** Alpöge–Claude assembled 14-part archive SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`; all paths below relative to `lean/src/`.  
**Classification:** source-level proof dependency audit; independent finite-character/size-budget derivation; no exact-original Lean replay, no RH/GRH or MATHCERT certification.

## 1. Exact claimed PsiBound theorem

`Development/AutomorphicArithmetic/AutomorphicVarieties/OddResidueBounds/ZeroMemUnrHom.lean`, SHA-256 `c6cac1eefc91d4bf1972ae1b8ccc54ab3ce3238e19e397dafb49bb739bcecf48`, declares `UpperTheory.V.Odd.PsiBound`:

For every CM abelian extension `E/ℚ`, algebraic closure `Ω`, modulus `N`, cyclotomic action `ρ : (ZMod N)ˣ →* Gal(E/ℚ)`, odd prime `l` with `l ∤ [E:ℚ]`, finite DVR `ℤ_l`-algebra `O`, `e≥1`, and character `ψ : Gal(E/ℚ) →* Oˣ` satisfying the parity condition `chiOf ρ ψ (-1)=(-1)^(e+1)`, whenever `a ∈ O` represents `alN (e+1) (chiOf ρ ψ)`, the genuine cohomology eigenspace length obeys

```text
psiLen(Ω,e,ψ) ≤ addVal_O(a).
```

Here `psiLen` is `Module.length O (shaEig(...))`; `alN k χ := (den N k : R) * Bprim k χ` is a denominator-scaled generalized Bernoulli value. This is **not** a definition making the bound tautological. In particular, if `a` is a valuation unit, the bound forces this cohomology eigenspace length to be zero.

The exclusions `l≠2`, `l ∤ [E:ℚ]`, the parity condition, and the precise `IsCycAct` action are **essential**, and must never be discarded in translating to character or prime-sum bounds.

## 2. Genuine origin: Poitou–Tate + unramified orthogonality

`.../PrimitiveFrobeniusFixed/Iv.lean`, SHA-256 `5f08d36359f3812eb54ad017057aaf484eaf0073462746a27746861c19e6bdcc`, proves exactly
```lean
theorem UpperTheory.V.ML.iv :
    GlobalTheory.Published.PoitouTateDuality →
    ReciprocityTheory.Gal.UnramifiedOrthogonality →
    UpperTheory.V.Odd.PsiBound :=
  fun h₁ h₂ => UpperTheory.V.ML.psiOf (UpperTheory.V.ML.recip h₁ h₂)
```

- `.../PrimitiveFrobeniusFixed/OverIff.lean`, SHA-256 `189230817c6416180d71e7e0fbc7fba7568ad1f8d46709f06003f5cfe97df28`: `ML.recip : PoitouTateDuality → UnramifiedOrthogonality → Rec`. `Rec` is an explicit local reciprocity statement controlling a product `n(τ)c(g)` at a prime `q` under cocycle, unramifiedness and level hypotheses, not an unqualified assertion of RH.
- `.../PrimitiveFrobeniusFixed/PsiOf.lean`, SHA-256 `be81f7279d28d67f9be81ade8a028375c11be57c11a5559f82240c14009ebd63`: `ML.psiOf : Rec → PsiBound`. It builds the associated Dirichlet character `ψ'`, proves `orderOf ψ'` divides `[E:ℚ]`, transports the parity and the character value, and invokes `ML.vChar` then an eigenspace/character comparison. This is the exact `l∤[E:ℚ]` → `l∤orderOf ψ'` transfer.
- `.../PrimitiveFrobeniusFixed/PrimCase.lean`, `ML.vChar : Rec → ...` works first with primitive characters, then pulls through the conductor using `lev_case` and the primitive-character comparison. The actual local/global reciprocity, Bernoulli divisibility and eigenspace comparison remain the mathematical load-bearing inputs.
- `Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/Brauer.lean`, `LitCoh` has an explicit `uo : UnramifiedOrthogonality` field; `.../DenseThresholdCases/HVCore.lean` applies `ML.iv (pt_s hN) hN.coh.uo`. Thus the submitted proof provides those two named source hypotheses and does not merely invoke an unbound `PsiBound` axiom in the last step. Independent truth of the named mathematical predicates, and kernel replay of their providers, are **not established by this source trace**.

## 3. From PsiBound to all-prime negative Sha estimate

`.../OddResidueBounds/ThmBcOfPsiBound.lean`, SHA-256 `90808ac87265e481e18121781c242726f0a8ae0bfd9832cf3b4d31c079c49d24`:
```lean
theorem primeBound_of (h : PsiBound) : PrimeBound :=
  prime_of actEx actFacts prodVal atPrime h
theorem thmBcFree_of (h : PsiBound) : ThmBcFree :=
  thmBc_of deg stickBound (primeBound_of h)
```

The logical separation is necessary:

(A) If `l∤n=[E:ℚ]`, `PrimeBound` controls the aggregate eigenspace length across any finite prime subset via Stickelberger/Bernoulli character valuations. These are *not* obtained from a pointwise bound by summing over infinitely many primes without further proof: the original `prodVal` input supplies a finite-prime **global product budget**.

(B) If odd `l∣n`, the universal finite-subset prime argument is no longer supported by `PsiBound`'s prime-to-degree hypothesis. Instead `StickBound` supplies individual prime estimates and `deg` establishes `l∣M.deg` so all exceptional odd primes belong to a *fixed finite set* of factors of `M.deg`.

(C) The resulting sum is exactly the original `minusBound(C, o, n, F, t)`:
```math
3nt^2\log(tF)+C\sum_{l\mid o,\, l\ne2}l n^2t^2\log(tlF)^2,
```
where `F=condF E`, `n=[E:ℚ]`, `o=M.deg`, `t≥2`, and `C≥0`.

### Independent finite-character and global-budget argument

Let `A=(ℤ/Nℤ)^×` and `K=ker ρ`. Since `A` is finite abelian, characters on `A` trivial on `K` inject into `Hom(A/K, ℂ^×)`. Finite abelian duality gives exactly `|A/K|` complex characters. Thus any subset satisfying the kernel and parity restrictions has cardinality at most `[A:K]`. If the cyclotomic action is surjective, `[A:K]=[E:ℚ]=n`.

For any finite set `S` of primes not dividing `n`, suppose the actual `PsiBound`/eigenspace transport and the global product estimate supply `w(l)≥0` with
```math
\log(l)\operatorname{len}_{l,e}\le w(l)\log(l),\quad
\sum_{l\in S}w(l)\log(l)\le |\mathrm{CharSet}|\log\operatorname{bnd}(F,e+1).
```
Summing and using `|CharSet|≤n` gives the **finite-subset** result
```math
\sum_{l\in S}\log(l)\operatorname{len}_{l,e}
\le n\log\operatorname{bnd}(F,e+1).
```
This deduction is independently proved here from the explicitly named input inequalities and finite abelian duality. It is **conditional**: the actual `PsiBound` and product estimate are not reproved in this tranche.

### Independently proved conductor/height compression

At the original source `.../GaloisLibrary/BernoulliNumbers/MapGenBChar.lean`,
```math
\operatorname{bnd}(F,k)=16F^{k+1} k!
```
for positive integer `F`. For `t≥2` and `1≤e+1≤t`, independently:
```math
16\le(tF)^4,\quad
F^{e+2}\le(tF)^{t+1},\quad
(e+1)!\le(tF)^t.
```
Multiplying yields
```math
\operatorname{bnd}(F,e+1)\le(tF)^{2t+5}.
```
Since `tF≥2`, apply monotonicity of `\log`:
```math
\log\operatorname{bnd}(F,e+1)\le(2t+5)\log(tF).
```
Summing across `e=1,...,t-1`, using `(t-1)(2t+5)≤3t^2` for `t≥2`, gives the first term `3nt²log(tF)`. The exceptional-prime terms are similarly bounded by `C\sum_{l\mid o,l≠2}l n² t²\log(tlF)^2` using `e+1≤t`, nonnegativity, and the fixed exceptional-prime set. This independently checks the finite arithmetic compression, *conditional on* `PrimeBound` and `StickBound`.

**Executable test:** `tests/rh_a26_psi_prime_bound_exact.py`, GitHub branch SHA-256 `1917a5a4a1d90b1071b49e38e23be42af3d6e0731f9a71a3a26c12960acd7bb4`, checked **40,768 exact integer tuples** `1≤F≤32,2≤t≤50,0≤e<t`, plus two deliberate invalid-premise controls, PASS. GitHub-fetched execution receipt `1408b345082e429db33a08d116a57e18`. Regression does not prove any Galois cohomology bound.

## 4. Important nonvacuity result

The original archive **does** contain an actual construction for `LData`: `Formalism/GaloisCohomology/GaloisCohomologyProofs/LdataNonempty.lean`, SHA-256 `29ba1c683ee864f8d9b1f234dcbb7a6b75d8a68866cac08fbe7e5879e5ce172b`. Its `ldata_nonempty` builds the finite set of prime ideals above `l`, uses canonical valuation over each prime, and descends the cyclotomic character to the quotient unramified outside that set. `ldataExists` quantifies over every number field, algebraic closure and prime.

This **removes the narrow concern** that the universal `LData` quantifiers are vacuous because no `LData` exists: the author provides a constructive source-level proof. It does **not** independently verify the imported ramification/prime-factor or formal Lean kernel theorems, nor establish the existence of all `IsChiField` families for the asymptotic windows.

## 5. Still open, exactly

1. Independently validate the genuine *local* reciprocity assertion `ML.recip` from the actual Poitou–Tate and unramified-orthogonality pairing; verify all class groups, local norm maps and finite-coefficient topologies.
2. Independently reconstruct `ML.vChar` / `ML.psiOf`: integral generalized Bernoulli values, parity, character order, correct `shaEig` comparison, and equality of the relevant lattice length to `psiLen`.
3. Independently validate `prodVal` and `atPrime` global valuation-to-character-sum budget, not merely finite-character counting.
4. Confirm existence of genuine `IsChiField` examples and that `VWinAt` asymptotic windows do not only quantify over empty fields.
5. Pinned Lean v4.33.1 exact-original proof and `#print axioms` replay on suitable hardware still open.

**Disposition:** `RH-A26_D05_PSIBOUND_SOURCE_HYPOTHESES_TRACED__PRIME_BUDGET_COMPRESSION_INDEPENDENTLY_VERIFIED__LOCAL_RECIPROCITY_AND_SHA_EIGENLENGTH_OPEN`.
