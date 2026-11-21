# OAI-26 F003 — exact seed-valuation sectorization and source-specific physical Gaussian lattice bound

**Assignment:** `GCL-OAI26-F003-SEED-VALUATION-PHYSICAL-GAUSSIAN-LARGESIEVE/1`  
**Immutable primary source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Protected predecessor:** MATHFORGE PR #585, protected merge `0598852b2a7cbf0c1f1cdb700a90b6803ac3765a`  
**Scope:** genuine `CanonicalMainGaussian` and `CanonicalErrorGaussian` child-source functions.  
**Status:** independently reconstructed mathematical theorem from pinned source premises; NOT newly Lean-elaborated. No MATHCERT or seven-eighths completion.

## A. Pin identities, gates, and exact child inputs

The **actual** source in pinned `Moments/AmplificationChildInput.lean:normalizedGaussSource` (blob `90d172571cce6192d42d5751618619de302acd6a`) is the normalized real part of

\[
E_s(K)=\frac{1}{V_s}\sum_{z\in O}
  \left|\sum_{I\in Q_s} c_I\,g_I(z)\right|^2\Phi(N(z)/K),
\tag{1}
\]

where \(O=\mathbb Z[\omega]\), \(V_s=\texttt{volume}(s)>0\), \(Q_s=\texttt{supportedColumns}((\texttt{original}\ s\ T\ S).\texttt{columns})\), \(c_I=(\texttt{original}\ s\ T\ S).\beta(I)\cdot\texttt{heightCoeff}(s.\eta,s.t,I)\), \(g_I(z)=\texttt{sexticGauss}(\texttt{primaryGenerator}(I),z)/\sqrt{N(I)}\), and \(\Phi=\texttt{FirstAmplificationChoice.ballProfile}\). This cutoff is real and \(0\le\Phi\le1\) (pinned `FirstAmplificationChoice.ballProfile_nonneg/le_one`, blob `1e7a23d2f1319bd7a025a0ee8148a577c685b52d`); its **strict** support is \(\Phi(x)\ne0\Rightarrow x<2\) for \(x\ge0\) (pinned `AmplifiedRetainedRadius.ballProfile_support_upper`, blob `f6d0c98a4212c85ac9de0c0ce7de35f519383d89`). The strict inequality is essential at \(K=1/2\).

Assume the actual \(S\ne0\) is squarefree, the two plain profiles \(s.W_1(0)=s.W_2(0)=0\), \(K>0\), \(H=\texttt{sourceRadius}(s)\ge0\). Pinned `SourceCommonMask.column_nonzero_masks` (blob `8186f884a29ef58f3160bef5907cf369a3ca848a`) and `OriginalCommonHarmonic.original_column_norm` (blob `420e446b72c8a1a5084d120b4bbeaa7b82eed634`) establish for every nonzero coefficient \(c_I\):

\[
\boxed{ S\mid I,\qquad \operatorname{IsCoprime}(I,T),\qquad I\ne0,\qquad N(I)\le H.}
\tag{2}
\]

\(\beta(I)\ne0\) follows from \(c_I\ne0\), so no extra height-character hypothesis is needed.

**Genuine main child:** \(s=\texttt{child}(src,C,R_0,B,\tau,t)\) with \(T=R_0C\) and its own \(K=K_{\rm main}\).  
**Genuine nested error child:** \(s=\texttt{errorInput}(src,C,R_0,B,\tau,t,Q,k,B',\upsilon,v)\), \(k\in\{1,6,7\}\), with \(T=(R_0C)Q^k\) and its own \(K=K_{\rm error}\). Their actual source identity, slots, seed and positive profile assumptions are inherited via pinned `AmplificationChildInput.child_columns/child_profile` and `FirstSecondActiveErrorGates.errorInput`. No `Ready` condition alone is silently substituted for the explicit \(s.W_i(0)=0\) hypothesis.

Powers \(\mathfrak p^e\) in (2) are **ideal prime powers**, never powers of integer \(N(\mathfrak p)\).

## B. Exact six-class physical Gaussian support at each seed prime

Let \(P(S)\) be the finite set of prime ideals dividing squarefree S. For \(\mathfrak p\in P(S)\), let \(q_{\mathfrak p}=N(\mathfrak p)\ge7\). At each active supported ideal \(I\), \(e_{\mathfrak p}(I):=v_{\mathfrak p}(I)\ge1\). Assign the **truncated valuation**

\[
\sigma_{\mathfrak p}(I)=\min(e_{\mathfrak p}(I),6)\in\{1,2,3,4,5,6\}.
\tag{3}
\]

For physical lattice coordinate \(z\in O\), let \(v_{\mathfrak p}(z)\in\mathbb N\cup\{\infty\}\), with \(v_{\mathfrak p}(0)=\infty\). Define
\[
\sigma_{\mathfrak p}(z)=
\begin{cases}
v_{\mathfrak p}(z)+1,&v_{\mathfrak p}(z)\le4,\\
6,&v_{\mathfrak p}(z)\ge5.
\end{cases}
\tag{4}
\]

**Theorem S4 (pointwise seed-class selector).** Every supported actual row satisfies
\[
\boxed{c_Ig_I(z)\ne0\quad\Longrightarrow\quad
\sigma_{\mathfrak p}(I)=\sigma_{\mathfrak p}(z)
\quad\text{for every }\mathfrak p\mid S.}
\tag{5}
\]

**Proof.** The pinned true prime-power sextic table `Detector/Sextic.actualSextic_primePowerGauss_at_pow` (blob `7637e778920da530c04b8ca5dea16dfcede93bf1`), together with `Detector/PrimePower.primePowerGauss_support/nonprincipal_extra_divisibility` (blob `5bad3212e490b99f8212f1c1d669e2efb4eaa023`) and `Detector/LocalPhysical.sexticGauss_prime_power` (blob `e936163fe9fc53cc0f3538331701fb4203a3fb62`), says: for exponent \(1\le e\le5\), the normalized genuine local Gauss row vanishes unless the physical frequency has valuation exactly \(e-1\); for \(e\ge6\), whether principal \(6\mid e\) or nonprincipal, it vanishes when physical valuation is \(<5\). Prime-power CRT `Moments/Canonical.canonicalCRTCharacter_mk` (blob `91df584105ed95bc611b0c17ac584668b19b8a79`) and `Poisson/EisensteinLattice.quotientProdEquivPi` (blob `226813526b901f11057d4e4ae0f4be1a52957d4d`) multiply these local transforms, up to **unit cofactor frequency phases** that cannot alter valuation support or local magnitudes. This yields (5), including \(z=0\) in class six at every seed prime. \(\square\)

For each seed-vector \(\sigma\in\{1,\dots,6\}^{P(S)}\), let \(\mathcal C_\sigma\subseteq Q_s\) be its *actual active* ideals, and \(P_\sigma(z)=\sum_{I\in\mathcal C_\sigma}c_Ig_I(z)\). Then (5) proves the following **pointwise identity** with no spectral approximation:

\[
\boxed{\forall z:\quad
\left|\sum_{\sigma}P_\sigma(z)\right|^2
=\sum_{\sigma}|P_\sigma(z)|^2.}
\tag{6}
\]

Indeed, at most **one** sector can contribute at a given physical \(z\). Thus for any K>0

\[
\boxed{E_s(K)=\sum_{\sigma}E_{s,\sigma}(K),\quad
 E_{s,\sigma}(K):=\frac1{V_s}\sum_z|P_\sigma(z)|^2\Phi(N(z)/K).}
\tag{7}
\]

This exact decomposition **does not pay a \(6^{\omega(S)}\) loss**. Unlike the already-admitted norm-mod-36 unit eigensectors (PR #582), the seed sectors are disjoint on **every** physical lattice row, not just after sixfold orbit averaging.

When S=1, the index set is empty, there is one sector, and (6)–(7) reduce to the original source identities. No fictitious seed prime is added.

## C. Exact two-gate source/physical feasibility and local norm gain

For a sector \(\sigma\), let

\[
\begin{split}
D_\sigma&:=\prod_{\mathfrak p\mid S}\mathfrak p^{\sigma_{\mathfrak p}-1},\\
d_\sigma&:=N(D_\sigma)=\prod_{\mathfrak p\mid S}q_{\mathfrak p}^{\sigma_{\mathfrak p}-1},\\
\Lambda_\sigma&:=\{\mathfrak p\mid S:\sigma_{\mathfrak p}\le5\},\\
n_{\rm low}(\sigma)&:=\prod_{\mathfrak p\in\Lambda_\sigma}q_{\mathfrak p},\qquad
n=N(S)=\prod_{\mathfrak p\mid S}q_{\mathfrak p}.
\end{split}
\tag{8}
\]

Empty products are 1. For any active \(I\in\mathcal C_\sigma\), every seed prime occurs with exponent at least \(\sigma_{\mathfrak p}\); therefore \(S D_\sigma\mid I\) and

\[
\boxed{\mathcal C_\sigma\ne\varnothing \Longrightarrow n\,d_\sigma\le H.}
\tag{9}
\]

The same local sextic table gives \(|g_{\mathfrak p^e}(z)|^2=q^{e-1}\) on its allowed shell for \(1\le e\le5\), and for any exponent \(e\ge6\) \(|g_{\mathfrak p^e}(z)|^2\le q^e\). At other supported primes the same trivial normalized upper bound \(q^e\) holds. Using CRT **absolute magnitude** factorization gives the genuinely uniform *seed-sensitive* pointwise estimate

\[
\boxed{|g_I(z)|^2\le \frac{N(I)}{n_{\rm low}(\sigma)}
\quad \text{for all }I\in\mathcal C_\sigma,\ z\in O.}
\tag{10}
\]

Thus every low seed-prime class supplies a **real factor \(q_{\mathfrak p}^{-1}\) in the squared row bound**, and every active sector is physically supported on the prime-power sublattice

\[
z\in D_\sigma,\qquad
v_{\mathfrak p}(z)=\sigma_{\mathfrak p}-1\ \text{for }\mathfrak p\in\Lambda_\sigma.
\tag{11}
\]

When \(\Lambda_\sigma\ne\varnothing\), this support excludes \(z=0\). It therefore has **no contribution** for \(2K\le d_\sigma\): the cutoff is strictly zero outside \(N(z)<2K\), while every nonzero \(z\in D_\sigma\) has \(N(z)\ge d_\sigma\). Thus the second **exact feasibility gate** is

\[
\boxed{E_{s,\sigma}(K)>0,\ \Lambda_\sigma\ne\varnothing
\Longrightarrow d_\sigma<2K.}
\tag{12}
\]

Together, (9) and (12) imply a nonzero nonprincipal sector requires
\[
\boxed{d_\sigma\le H/n\quad\text{and}\quad d_\sigma<2K.}
\tag{13}
\]

The all-high sector \(\sigma_{\mathfrak p}=6\) for every seed prime is the only one whose support can include the origin. It has \(d_\sigma=n^5\), so by (9) it is absent whenever \(H<n^6\), recovering the PR #585 zero-origin result without an additional estimate.

## D. Exact Eisenstein inclusion-exclusion count; no large-sieve constants

Define a **strict** lattice ball count
\[
A_{<}(x)=\#\{w\in O:N(w)<x\},\quad x>0.
\tag{14}
\]
The normalized Eisenstein lattice has Euclidean quadratic norm \(N(a+b\omega)=a^2-ab+b^2\); hence \(A_<\) is exactly finite for finite \(x\).

For \(\sigma\) and K>0, define
\[
\begin{aligned}
\mathcal N_\sigma(K)
&:=\#\{z\in O:N(z)<2K,\ 
v_{\mathfrak p}(z)=\sigma_{\mathfrak p}-1 \ \forall \mathfrak p\in\Lambda_\sigma,\ 
v_{\mathfrak p}(z)\ge5\ \forall\mathfrak p\mid S,\ \sigma_{\mathfrak p}=6\}\\
&=\sum_{J\subseteq\Lambda_\sigma}(-1)^{|J|}
 A_<\left(\frac{2K}{d_\sigma\prod_{\mathfrak p\in J}q_{\mathfrak p}}\right).
\end{aligned}
\tag{15}
\]

**Proof of exact inclusion-exclusion.** Every z allowed by the sector lies in the principal ideal \(D_\sigma\); write \(z=d_\sigma^{\rm gen}w\) for its generator, so \(N(z)=d_\sigma N(w)\). At each *low* seed prime, exact valuation \(\sigma_{\mathfrak p}-1\) is equivalent to \(w\) **not divisible** by that prime ideal; at each high prime, no restriction on w remains. Apply finite inclusion-exclusion over the low primes. For a subset J, requiring \(\prod_{\mathfrak p\in J}\mathfrak p\mid (w)\) scales the Eisenstein lattice by precisely \(\prod q_{\mathfrak p}\); the underlying ring is a PID. This gives (15) with strict \(<\), and notably includes the unit-seed case. \(\square\)

For each active sector set
\[
B_\sigma:=\sum_{I\in\mathcal C_\sigma}|c_I|\sqrt{N(I)}.
\]
Combining (6), (10), exact physical support and \(0\le\Phi\le1\) yields the explicit, unconditional **genuine source Gaussian-energy estimate**

\[
\boxed{\displaystyle
0\le E_s(K)\le
\frac1{V_s}\sum_{\substack{\sigma\in\{1,\ldots,6\}^{P(S)}\\
                n\,d_\sigma\le H}}
\frac{\mathcal N_\sigma(K)}{n_{\rm low}(\sigma)}
\,B_\sigma^{\,2},
\qquad K>0.}
\tag{16}
\]

This is a deterministic **seed-sensitive lattice large-sieve-type bound** with exact finite lattice counts, not an asymptotic Schwartz/Poisson estimate. It is stricter than the previous source-independent coarse row bound because it (a) **splits distinct sectors exactly**, avoiding cross-term Cauchy, (b) excludes sectors with impossible source conductor-norm geometry, (c) applies the local \(1/n_{\rm low}\) amplitude reduction, and (d) counts only exact congruence shells, not the entire lattice disk. All constants and terms are explicitly defined; it is valid at **every** positive physical K, including K below one.

**No unearned induction assertion:** (16) does not bound \(B_\sigma\) by the four `seededFactors` powers. To do so requires the actual coefficient norms and previous-stage `ZeroAt/PositiveAt` estimates with height/mesh, \(\upsilon\) conductor, radial Euler, seed and \(k+1\) allocation budgets. In particular, different allocated children may occupy the **same** seed sector, and the \(k+1\) Cauchy factor from `AmplificationChildEnergy.actual_amplification_child_energy` is not automatically removed by (6). A toy family of \(m\) identical polynomials saturates abstract Cauchy and shows why stronger child-specific information is needed, without purporting to be a genuine Input counterexample.

## E. Sharp zero-regime and exact-head adversarial replay

If \(H<n\), every source coefficient is zero. If \(H<n^6\) then the all-high sector is impossible; at \(0<K\le1/2\), every low sector has no nonzero physical Eisenstein lattice points in cutoff support and (16) gives \(E_s(K)=0\) exactly (also proved independently in PR #585). More generally, the only possible active sectors are those satisfying \(n\,d_\sigma\le H\), and among them the only nonzero nonprincipal sectors at physical K satisfy \(d_\sigma<2K\). This is strictly stronger case pruning than a global test \(H<n^6\).

**Finite adversary:** `f003_seed_valuation_sector_adversary.py` independently enumerates normalized local sextic square magnitudes for residue norms q=7,13,37 and exponents 1..15; tests all \(10^3\) three-prime exponent vectors against all \(12^3\) valuation vectors including origin; exhaustively checks six-class support and local square-root bounds; calculates the **actual Eisenstein norm lattice** \(a^2-ab+b^2\); verifies the exact inclusion-exclusion count (15) **against direct lattice-point enumeration** for every seed subset of the three primes, all \(6^{|P(S)|}\) tags, and eight positive physical K choices. Tests source H feasibility, unit seed and sharp support endpoint \(K=1/2\). The **first** replay deliberately caught the erroneous choice \(N(z)\le2K\); the test was corrected to **strict** \(N(z)<2K\) using the pinned source cutoff theorem, and a fresh exact-head replay succeeded. This adversarial correction is material and preserved in the evidence.

The verifier is an exact finite arithmetic check, **not** an independent Lean elaboration of (5)–(16), actual source evaluation with analytic coefficients, or a verification of the full Family 003 seven-eighths conclusion.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-SEED-VALUATION-PHYSICAL-GAUSSIAN-LARGESIEVE/1
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
SOURCE_FACTS: column_nonzero_masks; original_column_norm;
 actualSextic_primePowerGauss_at_pow; primePowerGauss_support;
 sexticGauss_prime_power; canonicalCRTCharacter_mk;
 quotientProdEquivPi; ballProfile_nonneg/le_one/support_upper
NEW MATHEMATICAL PROOF: pointwise disjoint 6-class seed-sector decomposition;
 exact joint radius/column norm gates; local sqrt-q gain;
 exact Eisenstein ideal-shell inclusion-exclusion;
 explicit unconditional bound (16) for genuine main/error normalized source
NEW LEAN ELABORATION OF COMPOSITE THEOREM: NOT PERFORMED
SHARP FOUR SEEDED GAUSSIAN POWERS: OPEN
FAMILY003 SEVEN-EIGHTHS: UNRESOLVED
MATHCERT: NONE
```
