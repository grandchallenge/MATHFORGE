# OAI-26 Family 003 — exact Gaussian diagonal, least-common-period remainder, and sextic prime-power exception

**Assignment:** GCL-OAI26-F003-EXACT-DIAGONAL-LCM-SEXTIC/1  
**Pinned source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Predecessor:** admitted MATHFORGE PR #578, commit `e2843d4ebfe0987ef30053066660cf7561b3b634`  
**Disposition:** EXACT_ZERO_DIAGONAL_SOURCE_LEAN_REDISCOVERED__LCM_GAUSS_BOUND_MATHEMATICAL_PROOF__SEXTIC_EXCEPTION_LOCALIZED__SHARP_NONZERO_ENERGY_OPEN  
**Authority:** MATHFORGE research reconstruction only. No MATHCERT or seven-eighths closure.

## A. Correction/strengthening of the previous research bound

PR #578 bounded the zero-frequency main term by blocks of columns sharing conductor primes. That bound was valid but non-sharp. In fact the **pinned upstream Lean source already proves complete off-diagonal vanishing at zero frequency**, not merely for coprime conductors:

- `Moments/SecondDiagonal.lean:full_zero_off_diagonal` (lines 14–47), blob `0534f6de4bb31a92eafe40484a8776ba5fc4871d`;
- `Moments/SecondDiagonal.lean:actual_zero_off_diagonal` (lines 75–89), which uses the source's canonical primary generators; and
- `Moments/SecondDiagonal.lean:secondZeroEnergy_bound` (lines 126–155), which already supplies the formal finite diagonal upper bound.

This is **not** a newly formalized theorem. This audit reconstructs and transports that exact existing theorem to the genuine normalized main and nested-error child source energies, and improves the PR #578 pair-period *analytic* error.

Let \(s\) be either genuine child `Input`, \(V_s=\texttt{volume}(s)>0\), \(Q_s\) its finite supported source columns and \(c_I=\beta_I\,\texttt{heightCoeff}\) with \(|c_I|=|\beta_I|\) (or \(\le\) suffices). The exact Gauss row from `Moments/GaussEnergy.lean` is

\[
g_I(z)=N(I)^{-1/2}\sum_{x\in O/I}\chi_I(x)\psi_I(zx),
\quad P_s(z)=\sum_{I\in Q_s}c_Ig_I(z).
\]

The character \(\chi_I\) has modulus one on residue units and zero on nonunits. The additive character \(\psi_I\) is the actual *primitive* `quotientTrace`, not the uncorrected integer trace. The canonical generator `sourceGenerator S I=primaryGenerator I` (source `Moments/SourceRow.lean`, blob `42584a9c87b0b8a983bcf7b21792aff05e4d1b8d`) determines the ideal uniquely, with \(\lambda^2\mid a_I-1\) from `Arithmetic/IdealMobius.lean:primaryGenerator_spec`.

The exact zero-mode Gram coefficient is

\[
H_{IJ}:=\mathbb E_{z\bmod(I\cap J)}
              g_I(z)\overline{g_J(z)}
=\begin{cases}
\varphi_O(I)/N(I),&I=J,\\
0,&I\ne J,
\end{cases}
\qquad
\varphi_O(I):=|(O/I)^\times|.
\]

**Independent derivation.** Expanding both finite Gauss transforms and averaging \(z\) reduces the mixed term to pairs of residue *units* \(x\bmod I\), \(y\bmod J\) with equal additive characters of \(z\). On the product period these satisfy \(b x-a y\in abO\), where \(I=(a),J=(b)\), using the source's `scaledResidue_congruence`. If \(\chi_I(x)\chi_J(y)\ne0\), then \((a,x)=(b,y)=1\); the congruence implies \(a\mid b\) and \(b\mid a\), hence \(I=J\). For \(I=J\), primitive pairing gives \(x=y\), so the surviving sum is precisely the number of residue units divided by \(N(I)\). This is the same arithmetic certified in the pinned Lean theorem, rather than a coprime-only inference.

Thus the **whole zero-frequency part** of the actual Gaussian energy is

\[
\boxed{\ E_{\mathrm{zero}}(s,K)
=\frac{c_\Phi K}{V_s}
 \sum_{I\in Q_s}|\beta_I|^2\frac{\varphi_O(I)}{N(I)}
\le \frac{c_\Phi K}{V_s}\sum_{I\in Q_s}|\beta_I|^2\ },
\]

where \(\Phi=\texttt{ballProfile}\in[0,1]\), \(\phi(x)=\Phi(|x|^2)\in C^\infty_c(\mathbb R^2)\) and \(c_\Phi=(2/\sqrt3)\int_{\mathbb R^2}\phi(x)\,dx\ge0\). For the child error source substitute its **actual** \(K_{\rm error}\) and \(V_{\rm error}\); no synthetic source is introduced.

## B. Stronger minimal-period Poisson remainder

The product \(g_I(z)\overline{g_J(z)}\) is periodic modulo the **ideal intersection** \(L_{IJ}=I\cap J=\operatorname{lcm}(I,J)\), not merely modulo \(IJ\). This is the *smallest common period ideal* of the two row periods; \(\,N(L_{IJ})=N(I)N(J)/N(I+J)\,\) in the Eisenstein PID. This can be substantially smaller than \(N(IJ)=N(I)N(J)\) at shared prime factors.

For all \(A>0\) there is a constant \(C_{A,\Phi}\), independent of all active columns, such that for \(K\ge1\),

\[
\boxed{\left|
\sum_{z\in O}g_I(z)\overline{g_J(z)}\Phi(N(z)/K)
-c_\Phi K\,\mathbf 1_{I=J}\,\frac{\varphi_O(I)}{N(I)}
\right|\le C_{A,\Phi}\,K\,N(L_{IJ})
     \left(1+\sqrt{K/N(L_{IJ})}\right)^{-A}.}
\]

**Proof.** Work on the finite quotient \(O/L_{IJ}\), of cardinal \(N(L_{IJ})\). The normalized finite Fourier coefficient of the periodic product \(g_I\overline{g_J}\) has absolute value at most its mean absolute value, which by Cauchy–Schwarz and finite Plancherel is at most 1. Expand into at most \(N(L_{IJ})\) characters. On the Eisenstein lattice \(\Lambda=\mathbb Z[\omega]\), each nonzero dual character lies at Euclidean distance at least \(c/\sqrt{N(L_{IJ})}\) from \(\Lambda^*\). This follows because multiplication by the generator of \(L_{IJ}\) is a similarity. For \(K\ge1\), lattice Poisson summation and arbitrary-order Schwartz decay of \(\widehat{\phi}\) bound each nontrivial twisted sum by \(C_{A,\Phi}K(1+\sqrt{K/N(L_{IJ})})^{-A}\), with \(C_{A,\Phi}\) independent of the lattice generator. The trivial character contributes \(c_\Phi K H_{IJ}\) plus a remainder obeying the same bound. Sum coefficients by the triangle inequality and substitute the *exact diagonal* \(H_{IJ}\) from §A.

This yields the **unconditional source-specific high-radius estimate**

\[
\boxed{\begin{aligned}
0\le E_s(K)\le \frac K{V_s}\bigg[
 &c_\Phi\sum_{I\in Q_s}|\beta_I|^2\frac{\varphi_O(I)}{N(I)}\\
 &+C_{A,\Phi}\sum_{I,J\in Q_s}|\beta_I\beta_J|\,
 N(I\cap J)\left(1+\sqrt{\frac{K}{N(I\cap J)}}\right)^{-A}
\bigg],\quad K\ge1.
\end{aligned}}
\]

For \(K=Z^\rho\), \(N(I\cap J)\le Z^d\), \(Z>1\), \(0\le d<\rho\), the pair remainder multiplier is \(\le Z^{d-A(\rho-d)/2}\). **No implication from upstream `Ready` to \(d<\rho\) is claimed.** For \(0<K<1\), the PR #576 lattice count remains available.

## C. Genuine sextic local obstruction: complete annihilation before a sixth-power plateau

The pinned source contains considerably more arithmetic than general Fourier orthogonality:

- `Detector/Sextic.lean:actualSextic_pow_eq_one_iff` (blob `7637e778920da530c04b8ca5dea16dfcede93bf1`): under the good-prime and residue-characteristic hypotheses, the actual local sextic character has exact order six.
- `Detector/GaussValuation.lean` (blob `6a36e548dcdcd3ea39d326e5351c15c5db11619b`): exact primitive/nonprincipal and principal prime-power Gauss sums at valuations.
- `Detector/LocalPhysical.lean:sexticGauss_prime_power` (blob `e936163fe9fc53cc0f3538331701fb4203a3fb62`): source `sexticGauss(p^(n+1),h)` equals the preceding local prime-power transform.
- `Moments/Unequal.lean:unequal_prime_power_support` (blob `d927000b2f6157f9cf72931cb3455e7d2b435289`): a **nonzero** correlation for unequal powers \(p^c,p^d\), \(c<d\), forces the smaller exponent \(c\) to be divisible by six, with the designated divisibility and nonunit exclusion on the Fourier frequency.
- `Moments/SecondLedger.lean:actual_secondSaving_lower` (blob `9c26887bfeb21911c6c8ca8dd6c00f4734b90e94`): conditional \(1/3\) local saving on every surviving correlation, including forcing/nonunit cases.

For a good prime element \(p\), \(q=N((p))>1\), residue characteristic other than 2, and \(c\ge1\), write \(g_c=g_{(p^c)}\). If \(\nu_p(z)\) is the prime valuation (the residue \(z=0\bmod p^c\) means \(\nu_p(z)\ge c\)), then the exact Gauss valuation formulas imply:

\[
\begin{array}{c|c|c}
&\text{support in }z& |g_c(z)|^2\\\hline
6\nmid c & \nu_p(z)=c-1&q^{c-1}\\
6\mid c & \nu_p(z)=c-1&q^{c-2}\\
6\mid c & \nu_p(z)\ge c&(q-1)^2q^{c-2}\\
\text{otherwise}&\text{—}&0.
\end{array}
\]

The nonprincipal line uses the usual *primitive finite-field Gauss norm* \(|\tau(\chi^c)|^2=q\); the principal lines follow from the exact Ramanujan sum at \(p^c\). Hence for **unequal** positive exponents \(c\ne d\),

\[
\boxed{\,6\nmid\min(c,d)\quad\Longrightarrow\quad
g_c(z)\overline{g_d(z)}=0\quad\text{for all }z\in O.\,}
\]

This is stronger than just zero mixed *average*. It is a separate mathematical deduction from the actual source local formulas; we do **not** claim that this new pointwise formulation has received an independent Lean elaboration. Its hypothesis is strictly local (a good unramified maximal prime, genuine sextic residue character with exact order six), not a blanket theorem on arbitrary composite column conductors.

**Sharp hostile witness:** \(c=6,d=7,z=p^6\) is not covered. At this frequency, the unnormalized \(p^6\) row is \((q-1)q^5\ne0\) and the \(p^7\) row is \(q^6\tau(\chi)\ne0\). Thus there is a **genuine surviving mixed-prime-power product**. An attempted theorem that all unequal powers are pointwise orthogonal would be false.

A quantitative local mean-absolute-product consequence, for \(1\le c<d\), is

\[
\boxed{\mathbb E_{z\bmod p^d}|g_c(z)g_d(z)|=
\begin{cases}
0,&6\nmid c,\\
(1-q^{-1})^2q^{(c-d+1)/2},&6\mid c,\ 6\nmid d,\\
2(1-q^{-1})^2q^{(c-d)/2},&6\mid c,\ 6\mid d .
\end{cases}}
\]

It bounds every normalized finite Fourier coefficient of the mixed product and gives additional power savings as \(d-c\) increases. The adjacent \(c=6k,\ d=6k+1\) case has **no \(q\)-power saving** from this norm alone. Multiplying such local bounds across arbitrary real source sectors requires checking the source's CRT phases and the actual `Family` gates; that global extension is **not claimed**.

## D. Exact bounded adversary and status

The companion `f003_exact_diagonal_lcm_sextic_adversary.py` is a no-dependency exact-arithmetic test. It checks genuine Eisenstein norm/trace pairing for unramified integer quotient *examples*, distinguishes coincident/different conductors even with shared prime factors, verifies the reduction from product to least-common-period norm, verifies prime-power support identities and local means at allowed \(q\equiv1\bmod6\), and contains the nonzero \(p^6/p^7\) hostile witness. This is finite independent checking of algebraic mechanisms, **not** an independent implementation of the source's completed sextic characters and not an infinite-lattice proof or Lean replay. All mathematical and execution claims must remain so labeled.

**Remaining sharp analytic obligation:** the general child-energy theorem must control all *nonzero* Fourier modes after applying the actual local sixth-power survivor filters, Cauchy/annular decompositions, `ZeroAt`/`PositiveAt` and conductor/height/mesh losses. The source's `Ready` does not by itself supply a favorable least-common-period/radius ratio. No synthetic-source replacement is authorized. The four seeded Gaussian powers and full seven-eighths theorem remain **not independently validated**.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-EXACT-DIAGONAL-LCM-SEXTIC/1
SOURCE: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
FOUND IN PINNED LEAN: exact zero-mode offdiagonal vanishing for all distinct ideals
INDEPENDENT MATHEMATICAL DERIVATION: true zero diagonal; least-common-period analytic bound;
 sextic unequal-power pointwise annihilation outside sixth-power plateau;
 exceptional p^6/p^7 surviving witness; quantified local mixed-L1 exponent
LEAN ELABORATION OF NEW SPECIALIZED CLAIMS: NOT PERFORMED
SHARP NONZERO MAIN/ERROR GAUSSIAN ENERGIES: OPEN
SEVEN-EIGHTHS: UNRESOLVED
MATHCERT: NONE
```
