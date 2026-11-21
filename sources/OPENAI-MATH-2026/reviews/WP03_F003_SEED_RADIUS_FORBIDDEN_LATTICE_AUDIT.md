# OAI-26 Family 003 — source-radius/seed-power forbidden sublattices for actual Gaussian child inputs

**Assignment:** GCL-OAI26-F003-SEED-RADIUS-FORBIDDEN-LATTICE/1  
**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Protected predecessor:** MATHFORGE PR #584, merged at `dbba38628d586667cb7f2957022df13ee4a1a4f0`  
**Disposition:** `ACTUAL_SEEDED_GAUSSIAN_FORBIDDEN_SUBLATTICE_K1_TO_K5_MATH_PROVED__ZERO_SMALL_K_NONTRIVIAL__SHARP_COMPOSITE_ENERGIES_OPEN`  
**MATHCERT:** NONE. Independent mathematical reconstruction from pinned Lean premises; no new Lean elaboration of the resulting theorem.

## A. Exact actual child source inputs

Fix **an actual source input** \(s:\texttt{Input}\ \iota\), a nonzero squarefree seed ideal \(S\), its actual source conductor \(T\), and the original finite coefficient function
\(\beta(I)=\texttt{(original s T S).beta}(I)=\texttt{coefficient s T S}(I)\). Assume \(s.W_1(0)=s.W_2(0)=0\). These hypotheses hold for the main and nested-error children in the pinned Gaussian theorems whenever their supplied positive annular profile gates are instantiated (the profile supports start at \(a>0\)); the theorem below explicitly retains this condition rather than silently replacing it with `Ready`.

Put \(H=\texttt{CenteredMomentOriginalCommonHarmonic.sourceRadius}(s)\), \(V=\texttt{volume}(s)>0\) and \(n=N(S)=S.\texttt{absNorm}\in\mathbb N_{\ge1}\). The genuine normalized source is

\[
E_s(K)=\frac1V\sum_{z\in O}
  \bigg|\sum_{I\in Q_s}\beta(I)\,
  \texttt{heightCoeff}(s.\eta,s.t,I)\,g_I(z)\bigg|^2
  \Phi(N(z)/K),
  \quad K>0,
\]

where \(O=\mathbb Z[\omega]\), \(\Phi=\texttt{FirstAmplificationChoice.ballProfile}\), and \(g_I\) is the **actual** normalized sextic Gaussian row for \(I\) via `sourceGenerator=primaryGenerator`. Nothing about \(s\) is replaced by a synthetic source.

The directly inspected pinned Lean facts are:

* `Moments/SourceCommonMask.lean:column_nonzero_masks` (blob `8186f884a29ef58f3160bef5907cf369a3ca848a`) and `Moments/OriginalCommonHarmonic.lean:original_column_mask` (blob `420e446b72c8a1a5084d120b4bbeaa7b82eed634`): \(\beta(I)\ne0\Rightarrow S\mid I\) and \(I\) coprime to conductor \(T\);
* `Moments/OriginalCommonHarmonic.lean:original_column_norm` (same blob): if the two plain source profiles vanish at zero, \(\beta(I)\ne0\Rightarrow I\ne0\) and \(N(I)\le H\);
* `Detector/Sextic.lean:actualSextic_primePowerGauss_at_pow` (blob `7637e778920da530c04b8ca5dea16dfcede93bf1`) together with `Detector/LocalPhysical.lean:sexticGauss_prime_power` (blob `e936163fe9fc53cc0f3538331701fb4203a3fb62`): at a good supported prime p, for exponent \(e\in\{1,2,3,4,5\}\) the normalized \(g_{p^e}(z)\) vanishes whenever \(p^e\mid z\), indeed it is supported at exact \(p\)-adic valuation \(e-1\);
* `Moments/Canonical.lean:canonicalCRTCharacter_mk` (blob `91df584105ed95bc611b0c17ac584668b19b8a79`) and `Poisson/EisensteinLattice.lean:quotientProdEquivPi` (blob `226813526b901f11057d4e4ae0f4be1a52957d4d`) transport this **local zero factor** to any supported composite \(g_I\), with the cofactor units changing phases but never the local valuation zero.

The source proves these constituent facts in Lean. Their following combined *seed-power restriction* is derived independently as a mathematical argument and is **not yet a separate pinned Lean theorem**.

## B. Five exact forbidden Eisenstein sublattices

**Theorem (source-bound forbidden-sublattice hierarchy).** Let \(j\in\{1,2,3,4,5\}\). Under the actual source hypotheses of §A,

\[
\boxed{H<n^{j+1}
\quad\Longrightarrow\quad
P_s(z)=0\quad
\text{for every }z\in O\text{ with }S^j\mid (z),}
\tag{F003-S1}
\]

where \(P_s(z)=\sum_{I\in Q_s}\beta(I)\,\texttt{heightCoeff}(s.\eta,s.t,I)g_I(z)\).

**Proof.** If \(S=O\) is the unit ideal, then \(n=1\) and the hypothesis \(H<n^{j+1}=1\) excludes all nonzero columns by their integral norm \(N(I)\ge1\); the assertion is immediate. Otherwise, every column with nonzero \(\beta(I)\) is divisible by nonunit squarefree \(S\) and has \(N(I)\le H\). If every prime ideal \(\mathfrak p\mid S\) occurred in \(I\) with exponent at least \(j+1\), then squarefreeness would imply \(S^{j+1}\mid I\). By exact multiplicativity of ideal norms, \(N(I)\ge n^{j+1}>H\), a contradiction. Hence for each nonzero \(\beta(I)\) there is at least one seed prime \(\mathfrak p\mid S\) with \(1\le e=v_{\mathfrak p}(I)\le j\le5\). For any physical \(z\) satisfying \(S^j\mid(z)\), \(v_{\mathfrak p}(z)\ge j\ge e\). The genuine nonprincipal sextic prime-power Gauss row at \(\mathfrak p^e\) vanishes at this frequency; the composite row \(g_I(z)\) has this zero factor by exact CRT. Thus **each individual active summand is zero** and so is their polynomial, with no triangle inequality or coefficient cancellation assumption. \(\square\)

The squarefree seed is essential to the simple threshold \(n^{j+1}\); it is a hypothesis of the actual `CanonicalMainGaussian` and `CanonicalErrorGaussian` statements, not an invented restriction.

**The first cutoff:** If \(H<n\), there are **no** nonzero coefficients at all, because \(S\mid I\) and \(N(I)\le H\) would imply \(n\le H\). Hence \(\texttt{normalizedGaussSource}=0\) for every positive K and any nonnegative source window. This improves the pinned `FirstPhysicalZeroRadius.sourceGaussEnergy_zero` base case \(H\le0\) when a large seed forces emptiness at positive \(H\).

**The principal-origin cutoff:** At \(j=5\),

\[
\boxed{H<n^6\quad\Longrightarrow\quad
P_s(0)=0,\quad
P_s(z)=0\ \ \forall z\in S^5.}
\tag{F003-S2}
\]

This strengthens the general origin floor of admitted PR #584: a **nonzero principal sixth-power column** with seed \(S\) requires \(N(I)\ge n^6\). Therefore the exact origin obstruction is automatically absent when \(n>H^{1/6}\). The inequality \(H<n^6\) is a *case gate*, not a conclusion of `Ready` for every source.

**Exact small-physical-radius zero theorem:** The actual source cutoff \(\Phi(u)\) is zero for \(u\ge2\). If \(0<K\le1/2\), every \(z\ne0\) has Eisenstein norm \(N(z)\ge1\), so only \(z=0\) can enter the Gaussian energy. By (F003-S2),

\[
\boxed{0<K\le\frac12,\quad H<n^6
\quad\Longrightarrow\quad
E_s(K)=0.}
\tag{F003-S3}
\]

The same statement holds for the **actual** nested error child \(\texttt{errorInput}\) with its own \(H=sourceRadius(errorInput)\), actual seed S, volume and physical error radius; there is no substitution of main K for error K.

**Exact conductor consistency:** If the full actual source conductor \(T\) shares any ideal prime with the seed \(S\), pinned `SourceCommonMask.column_nonzero_masks` already forces \(\beta\equiv0\). Thus the seed hierarchy only needs work in the live conductor-coprime branch; it introduces no new conductor loss or fictitious epsilon.

## C. Optimality as a pure Gaussian row theorem, but not a source counterexample

The strict threshold \(n^{j+1}\) cannot be replaced by \(n^{j+1}+\delta\) in an *unrestricted* row theorem. For any supported squarefree seed \(S\) with a principal generator \(s\) and any \(j=1,\ldots,5\), take the single supported ideal \(I=S^{j+1}\) and physical \(z=s^j\) so \(S^j\mid(z)\) and \(N(I)=n^{j+1}\). At each seed prime the local frequency has exact valuation \(j=(j+1)-1\), where the genuine local nonprincipal Gauss sum is nonzero when \(j+1\le5\); for \(j+1=6\) the genuine principal row is also nonzero on valuation five. CRT gives \(g_{S^{j+1}}(s^j)\ne0\). This establishes **geometric sharpness** of the threshold for row support, but does **not** assert that a chosen single-column Gaussian coefficient arises from any permissible F003 input with all `Matches`, `Ready`, `ZeroAt` or `PositiveAt` gates.

## D. A new source-specific proof-obligation reduction

For any actual main child \(d_m=\texttt{child}(s,C,R_0,B,\tau,t)\), set \(H_m=\texttt{sourceRadius}(d_m)\), \(S=\mathrm{seed}\). For nested error \(d_e=\texttt{errorInput}(\ldots,Q,k,B',\upsilon,v)\), set \(H_e=\texttt{sourceRadius}(d_e)\), same input seed \(S\). By the pinned live-source and profile identities and the positive-annular support inherited from `Profiles a b`, the following subcases no longer require any `ZeroAt`/`PositiveAt` or extra conductor/height/mesh/seeded-power charge:

* Empty source when \(H_m<n\) or \(H_e<n\), for **all** physical radii K;
* Zero origin when \(H_m<n^6\) or \(H_e<n^6\), irrespective of Gaussian radius;
* Exactly zero entire Gaussian source when \(K_m\le1/2\) and \(H_m<n^6\), or \(K_e\le1/2\) and \(H_e<n^6\);
* For each \(1\le j\le5\) with \(H_s<n^{j+1}\), exact vanishing of the full source Gaussian polynomial on the sublattice \(S^j\).

These deductions can be used to prune the live child source case tree **before** invoking a sharp analytic estimate. They are compatible with the actual energy only because the forbidden-frequency zero is **pointwise on every source row**; this is unlike the false generic post-hoc coefficient projection from the previous audit.

**Substantive remaining obligation:** where \(H_s\ge n^6\) or the Gaussian radius is not restricted to \(K\le1/2\), the within-unit-sector composite correlation with exact \(M(I,J)\) factor and \(k+1\) allocation cost still must be paid in the four seeded Gaussian powers. No automatic lower bound on the seed \(n\) or sharp radial gap follows merely from `Ready`. The natural theorem remains unvalidated; there is no MATHCERT.

## E. Exact adversary and claim ledger

The accompanying no-dependency exact verifier `f003_seed_forbidden_sublattice_adversary.py` enumerates small genuine Eisenstein prime generators (q=7,13,37), squarefree seed subsets, prime exponent vectors and local valuations, and independently checks the norm cap implication, forbidden sublattice, j=1..5 cutoff, q-prime Gauss support and boundary witnesses. It uses the **exact actual pinned local support table**, but its symbolic coefficient/sourceRadius tests do not instantiate the source's full `Input` structure or replay a Lean proof; the mathematical proof in §B performs the general transport.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-SEED-RADIUS-FORBIDDEN-LATTICE/1
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
PINNED LEAN INPUT: original_column_mask, original_column_norm,
 column_nonzero_masks, actual sextic prime-power Gauss support,
 canonical supported CRT, ballProfile support, child input definitions
NEW MATH: five exact forbidden source sublattices; seed^6 radius
 origin exclusion; nontrivial exactly-zero small-physical-radius regime;
 row-wise sharpness of cutoff
NEW INDEPENDENT LEAN ELABORATION: NOT PERFORMED
SHARP FOUR MAIN/ERROR SEEDED POWERS: OPEN
FAMILY003 SEVEN-EIGHTHS: UNRESOLVED
MATHCERT: NONE
```
