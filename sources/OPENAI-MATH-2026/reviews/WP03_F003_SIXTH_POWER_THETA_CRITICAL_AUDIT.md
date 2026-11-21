# OAI-26 F003 — exact sixth-power mixed Gaussian kernel and global-unit selection

**Assignment:** `GCL-OAI26-F003-SIXTH-POWER-THETA-CRITICAL/1`  
**Pin:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Predecessor:** MATHFORGE PR #579, protected `ca69d3b9de4ddf98cd8de0df024bfa82f5f1d4c7`  
**Disposition:** `SIXTH_POWER_PAIR_KERNEL_EXACT_MATH_PROVED__GLOBAL_UNIT_SELECTION_AND_CRITICAL_RADII_EXPLICIT__GENERAL_SHARP_CHILD_ENERGY_OPEN`  
**Certification:** NONE; no MATHCERT or independent new Lean elaboration.

## A. Exact pure-prime-power mixed Poisson kernel

Fix a **source-supported** good maximal prime ideal \((p)\) of Eisenstein \(O=\mathbb Z[\omega]\), with \(\texttt{goodLambda}\notin(p)\), \(\operatorname{char}(O/(p))\ne2\), norm \(q=N((p))>1\), and the actual local order-six sextic multiplicative character \(\chi=\texttt{actualSextic}((p))\). Write \(g_c(z)=\texttt{gaussRow}(p^c,z)\) normalized by \(q^{c/2}\), and take \(1\le c<d\) with \(6\mid c\). These are genuine source rows, **not** imaginary independent variables. The integer exponent \(c,d\) here labels *column valuations*, not automatically the error-family parameter \(k\in\{1,6,7\}\).

For any Schwartz \(W\) of the pinned source and \(K>0\), denote

\[
\mathcal P_{d,c}(W,K)=\sum_{z\in O}g_d(z)\overline{g_c(z)}W(N(z)/K),
\quad G_W=\texttt{paperRadialFourier}(W).
\]

Then the following identity is **exact**:

\[
\boxed{\displaystyle
\mathcal P_{d,c}(W,K)=
K(1-q^{-1})q^{(c-d)/2}
\sum_{k\in O}\chi^d(-k)\,
G_W\!\left(\frac{K\,N(k)}{q^d}\right).
}
\tag{A1}
\]

*Independent reconstruction from pinned formulas.* `Moments/GaussEnergy.lean:gaussEnergy_poisson` (blob `200d3d5c9fb828b7bd1eb4e5a7160b10c5fd65bd`) expresses a pair kernel as \(K/q^{(c+d)/2}\) times the actual full correlation at Fourier frequency \(-h\), weighted by \(G_W(K N(h)/q^{c+d})\). Pinned `Moments/Unequal.lean:unequal_prime_power_support` (blob `d927000b2f6157f9cf72931cb3455e7d2b435289`) makes that correlation zero unless \(h=p^c k\); `unequal_prime_power_factor` makes its surviving value

\[
\operatorname{actualCorrelation}(p^d,p^c;p^c k)
 =\chi^d(k)\,
 \overline{\sum_{y\bmod p^c}\chi^c(y)}
 =\chi^d(k)(q^c-q^{c-1}),
\]

since \(\chi^c\) is principal on the **units** and zero on nonunits when \(6\mid c\). Replace \(h=p^c k\), noting \(N(p^c)=q^c\), and simplify exactly to (A1). The minus sign in \(\chi^d(-k)\) is essential and retained. Pinned `Detector/Sextic.lean:actualSextic_pow_eq_one_iff`, blob `7637e778920da530c04b8ca5dea16dfcede93bf1`, supplies exact order six.

This is an actual single-pair identity. No claim is made that the whole main/error child source already decomposes into independently bounded copies of (A1).

## B. Exact radial unit-orbit selection: most nonprincipal sixth-power survivors vanish in aggregate

Pinned `CubicSieve/CutoffOrders.lean:actualSextic_unit_euler`, blob `f913c9856cfa3939f6d2339b839271002186bbfb`, says for each Eisenstein global unit \(u\in O^\times\),

\[
\chi(u)=\operatorname{eisEmbedding}\left(u^{(q-1)/6}\right).
\tag{B1}
\]

The unit group \(O^\times\) is cyclic of order six, and the embedding is faithful. Put \(m=(q-1)/6\). Therefore the restriction of \(\chi^d\) to all global units is trivial **if and only if**

\[
\boxed{6\mid d\,m.} \tag{B2}
\]

Indeed, multiplying every \(k\) in (A1) by a global unit \(u\) permutes the Eisenstein lattice, preserves \(N(k)\), and multiplies the theta series by \(\chi^d(u)\). If that scalar is not one, the entire series must vanish, for **every \(K>0\)** and every radial \(W\):

\[
\boxed{6\nmid d(q-1)/6\quad\Longrightarrow\quad
\mathcal P_{d,c}(W,K)=0\ \ (\forall K>0).}
\tag{B3}
\]

For the first nontrivial power pair \((c,d)=(6,7)\), this becomes

\[
\boxed{q\not\equiv1\pmod {36}\ \Longrightarrow\
\mathcal P_{7,6}(W,K)\equiv0.}
\]

**Important distinction:** the *pointwise* product \(g_7(z)\overline{g_6(z)}\) can be nonzero even if the **radially weighted lattice sum is identically zero**. The q=7,13,19,31 examples fall into this unit-annihilated class. This is not a forbidden claim that all unequal prime powers are pointwise orthogonal.

## C. The surviving q=37 example is genuine; global-unit cancellation is not universal

Let \(p=7+3\omega\), for which \(N(p)=49-21+9=37\), so \((p)\) is a good maximal ideal, its characteristic is 37, and \(m=(37-1)/6=6\). Hence \(\chi\) is **trivial on global units**, although nonprincipal on the finite residue field.

For the actual ball profile \(\Phi=\texttt{FirstAmplificationChoice.ballProfile}\), pinned `ballProfile_one` proves \(\Phi(x)=1\) on \([0,1]\), and the compact-support lemma proves \(\Phi(x)=0\) for \(x\ge2\). Take \(K=q^6\). The \(g_7\) row is nonzero only at \(z=p^6u\) with \(p\nmid u\); the radial window demands \(N(u)<2\). The Eisenstein elements of norm \(1\) are exactly the **six global units**, and there are no elements of norm \(2\). Their \(\chi\)-values are all 1.

By the exact local Gauss valuation formula (pinned `Detector/LocalPhysical.lean`, blob `e936163fe9fc53cc0f3538331701fb4203a3fb62`; `Detector/GaussValuation.lean`, blob `6a36e548dcdcd3ea39d326e5351c15c5db11619b`),

\[
\boxed{\displaystyle
\mathcal P_{7,6}(\Phi,q^6)
=6(1-q^{-1})q^{11/2}\tau(\chi;1)\ne0\quad(q=37).
}
\tag{C1}
\]

Nonvanishing uses the standard nonprincipal prime-field Gauss norm \(|\tau(\chi;1)|=\sqrt q\), which is also present in the pinned `HighRowsSharpScalar` prime-Gauss results. Thus **no general all-radius vanishing theorem is possible** for the \(p^6,p^7\) pair. This is a concrete obstruction, not a formal or source inconsistency.

## D. Two different radial regimes, with a sharp low-radius caveat

For the fixed, genuine \(\Phi=\texttt{ballProfile}\), \(\operatorname{supp}\Phi\cap[0,\infty)\subset[0,2)\). The local prime-power frequency tables yield:

- **Nonprincipal larger exponent:** If \(6\nmid d\), then \(g_d(z)\ne0\) implies \(\nu_p(z)=d-1\), hence every nonzero term has \(N(z)\ge q^{d-1}\). Therefore

\[
\boxed{6\nmid d,\quad2K\le q^{d-1}
\quad\Longrightarrow\quad \mathcal P_{d,c}(\Phi,K)=0.}
\tag{D1}
\]

- **Principal larger exponent:** If \(6\mid d\), the row \(g_d\) is also nonzero at \(z=0\). For the same low radius, the mixed pair is **not zero**; it consists of exactly the lattice-origin term,

\[
\boxed{6\mid d,\quad2K\le q^{d-1}
\quad\Longrightarrow\quad
\mathcal P_{d,c}(\Phi,K)
=(1-q^{-1})^2q^{(c+d)/2}.}
\tag{D2}
\]

This origin contribution is a **genuine analytic obstruction** to an over-broad compact-support argument. The claimed cutoff in (D1) must never be applied to two principal sixth-power exponents.

For *either* type of \(d\), the theta expression (A1) gives a strong uniform **high-radius** estimate. As \(\chi^d(0)=0\) and \(G_W\) has arbitrary-order rapid decay, for each real \(B>1\) there is a constant \(C_{B,W}\), independent of the good prime and powers, such that if \(K\ge q^d\),

\[
\boxed{\left|\mathcal P_{d,c}(W,K)\right|
\le C_{B,W}\,K(1-q^{-1})q^{(c-d)/2}
\left(\frac{q^d}{K}\right)^B.}
\tag{D3}
\]

Proof: bound \(|G_W(t N(k))|\) by \(D_{B,W} t^{-B}N(k)^{-B}\), \(t=K/q^d\ge1\), and use \(\sum_{k\in O\setminus\{0\}}N(k)^{-B}<\infty\). No estimate for a growing number of source columns is implicitly added.

Thus for the \(p^6,p^7\) nonprincipal pair with \(q\equiv1\bmod36\), the only **uncontrolled relative-radius region** of this local argument is

\[
\boxed{\frac12 q^6<K<q^7.}
\tag{D4}
\]

The high-radius estimate (D3) remains valid even there if one accepts a non-saving factor; the word "uncontrolled" means not assigned a uniform power-saving, not that a finite sum is undefined.

## E. Exact finite critical-range reduction

The local valuation formulas give actual **primal** identities, with no global character-sum estimates substituted:

For \(6\mid c<d\) and \(6\nmid d\),

\[
\boxed{\mathcal P_{d,c}(\Phi,K)=
(1-q^{-1})q^{(c+d)/2-1}\tau(\chi^d;1)
\sum_{u\in O}\overline{\chi^d(u)}\,
\Phi\!\left(\frac{q^{d-1}N(u)}K\right).}
\tag{E1}
\]

For \(6\mid c<d\) and \(6\mid d\), let \(u\) run through Eisenstein elements not divisible by \(p\):

\[
\boxed{\begin{aligned}
\mathcal P_{d,c}(\Phi,K)=&(1-q^{-1})q^{(c+d)/2-1}\bigg[
 (q-1)\sum_{v\in O}\Phi\!\left(\frac{q^d N(v)}K\right)\\
 &-\sum_{\substack{u\in O\\p\nmid u}}
 \Phi\!\left(\frac{q^{d-1} N(u)}K\right)\bigg].
\end{aligned}}
\tag{E2}
\]

These identities follow by inserting the exact normalized principal/nonprincipal prime-power Gauss rows, separating \(z=p^{d-1}u\) with \(p\nmid u\) from \(z=p^d v\) and changing variables. The \(\overline{\chi^d(u)}\) in (E1) uses the multiplicative change of variables in the **actual** primitive finite-field Gauss sum; no unit or phase factor is suppressed.

If \(K\le q^d\), the first sum in (E1) involves **only \(N(u)<2q\)**. This exposes a finite, short sextic Eisenstein character sum as the remaining genuinely oscillatory critical-range input. In (E2) the problem is instead a signed **geometric lattice-counting discrepancy** and an explicit origin term. Distinct analytic methods are appropriate.

## F. Externalization of evidence and limits

The companion `f003_sixth_power_theta_adversary.py` checks exact Eisenstein norms for explicit norm-7, norm-13, norm-37 prime elements, the global-unit norm congruence gate, the exact \(q\)-adic valuation support/cutoff and origin formulas for a finite radial step-profile surrogate, and symbolic finite-field multiplicative change-of-variables (not floating-point complex Gauss phases). The step-profile checks test **algebraic formula identities for radial weights**; they are **not a replay of the smooth source's infinite sums**. The smooth-\(\Phi\) claims are mathematical deductions from its pinned `ballProfile_one` and support theorems.

**Next obligation:** insert the exact local theta/geometry reductions (A1/E1/E2) into the **genuine composite source columns** with the pinned CRT phase conventions, then prove the \(\frac12q^{d-1}<K<q^d\) critical character-sum/geometry estimates *uniformly* under `ZeroAt`, `PositiveAt`, `Ready`, nested \(\upsilon\)-modulus gates and conductor/height/mesh losses. A large origin term for principal 6–6 pairings cannot be discarded. The full four seeded Gaussian powers and seven-eighths certification remain **open**.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-SIXTH-POWER-THETA-CRITICAL/1
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
MATHEMATICAL PROOF: exact local mixed theta identity; global-unit selection;
 concrete q=37 nonzero radial witness; nonprincipal low-radius zero;
 principal low-radius origin anomaly; high-radius rapid decay;
 separate short character sum and lattice-discrepancy critical regimes
NEW INDEPENDENT LEAN FORMALIZATION: NONE
GLOBAL MAIN/ERROR SHARP ENERGY: OPEN
SEVEN-EIGHTHS: UNRESOLVED
MATHCERT: NONE
```
