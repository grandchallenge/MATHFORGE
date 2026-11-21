# OAI-26 Family 003 — composite sextic Gram factors, exact hereditary conductor puncture, and allocation-loss accounting

**Assignment:** GCL-OAI26-F003-COMPOSITE-VALUATION-GRAM-PUNCTURE/1  
**Immutable source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Protected research predecessor:** MATHFORGE PR #583; main `1b1b7281097974ad8b4620edb96746f82f8293f6`  
**Scope:** actual source Gaussian rows and raw amplification error families, not independently Lean-elaborated new composite lemmas  
**Disposition:** `EXACT_COMPOSITE_GRAM_RECONSTRUCTED__EACH_MAIN_ERROR_CHILD_CONDUCTOR_PUNCTURED__ALLOCATION_CARDINALITY_AND_SHARP_POWERS_OPEN`  
**No seven-eighths completion or MATHCERT certification.**

## 1. Exact source binding and input assumptions

For a supported nonzero ideal \(I\subset O=\mathbb Z[\omega]\), set \(a_I=\texttt{sourceGenerator}(I)=\texttt{primaryGenerator}(I)\), so \((a_I)=I\). The genuine row in pinned `Moments/GaussEnergy.lean:gaussRow` (blob `200d3d5c9fb828b7bd1eb4e5a7160b10c5fd65bd`) is

\[
g_I(z)=\frac{\texttt{sexticGauss}(a_I,z)}{\sqrt{N(I)}}.
\]

The finite source set \(Q_s\) for an actual `Input` is \(\texttt{supportedColumns}(\texttt{finiteColumns}(\texttt{Fintype.piFinset}(s.\texttt{pools})))\), with \(c_I=\texttt{coefficient}(s,R,\texttt{seed},I)\cdot\texttt{heightCoeff}(s.\eta,s.t,I)\). Its real Gaussian energy is exactly

\[
E_s(K)=\frac1{V_s}\sum_{z\in O}\left|\sum_{I\in Q_s}c_I g_I(z)\right|^2
 \Phi\!\left(\frac{N(z)}K\right),\quad V_s=\texttt{volume}(s)>0,
\tag{1}
\]

where \(\Phi=\texttt{FirstAmplificationChoice.ballProfile}\in C_c^\infty\) is real, nonnegative, 1 on \([0,1]\), 0 on \([2,\infty)\). This is the *actual* main or nested-error child after instantiating the appropriate `Input`, `R`, seed, volume and physical radius; no synthetic replacement.

Source facts at the immutable pin:

| File / theorem | Source blob | Use |
|---|---|---|
| `Moments/Canonical.canonicalCRTCharacter_mk` | `91df584105ed95bc611b0c17ac584668b19b8a79` | Genuine supported character is prime-power CRT product |
| `Poisson/EisensteinLattice.quotientProdEquivPi` | `226813526b901f11057d4e4ae0f4be1a52957d4d` | General pairwise-coprime-power CRT decomposition |
| `Detector/Sextic.actualSextic_primePowerGauss_at_pow` | `7637e778920da530c04b8ca5dea16dfcede93bf1` | Exact local power-valuation Gauss table |
| `Detector/LocalPhysical.sexticGauss_prime_power` | `e936163fe9fc53cc0f3538331701fb4203a3fb62` | Actual Gaussian row equals pinned prime-power transform |
| `Detector/HighRowsSharpScalar.primeGauss_actual_pow_norm` | `62fc662a897ef22d6fea987e7df7a5990127afe4` | Exact \(\sqrt q\) norm for nonprincipal sextic powers |
| `Moments/SecondDiagonal.actual_zero_off_diagonal` | `0534f6de4bb31a92eafe40484a8776ba5fc4871d` | All distinct ideal zero Fourier modes vanish, including shared primes |
| `Eisenstein/UnitNormalization.idealRowHom_unit_norm` | `fa4c3434d200a7fd7e38c7daa619bfa4553ab1c8` | Six global-unit eigensectors, already admitted PR #582 |
| `Moments/AmplificationSourcePool.residualColumns_eq` | `4166c4c37e69826d2c4554712e528dfb207449c9` | Exact valuation-\(k\) error residual is \(p\)-free |
| `Moments/AmplificationErrorPool.residual_energy_eq_punctured` | `7a589ccfedd4d0dca61550015959b8c15003afbc` | True residual energy matches the punctured original |
| `Moments/OriginalChildEnergy.original_source_punctured_column` | `ee1338c7b068e68930073a0ef820df3e9168e296` | Its proof establishes **individual** child residual-coprimality, not just summed cancellation |
| `Moments/SourceCommonMask.column_nonzero_masks` | `8186f884a29ef58f3160bef5907cf369a3ca848a` | Each actual source coefficient is coprime to the current conductor and divisible by its seed |\n| `Moments/LiveSupport.live_column_original_support` | `b1b14b229ced32ad20d6e3dc0e9b8651a4db10fb` | Every allocated live nonzero coefficient is coprime to extracted C |\n| `Moments/AmplificationLiveMask.column_mask` | `c0b68ea2d09df9f552c9f82df9de69f85ffc8fbb` | Source mask preserves the individual puncture |\n| `Moments/AmplificationAllocationScale.frozenCoefficient_exact` | `10d65f66a2a211382657eac4aa3381788979fc45` | Under prime-slot coprimality every allocation scalar is the *same* 0/1 coprimality indicator |
| `Moments/AmplificationChildEnergy.actual_amplification_child_energy` | `e29c88fc2085ed5f3b0f2daead5a7b8bc11da7e6` | Current \(k+1\) child-energy charge |
| `Moments/AmplificationChildInput.normalizedGaussSource` | `90d172571cce6192d42d5751618619de302acd6a` | Exact normalized main/error source |

The finite local formulas below apply only to **supported good prime powers** of the genuine local order-six character, with residue characteristic distinct from two. For arbitrary unsupported prime ideals they are not asserted.

## 2. Composite pointwise annihilation and exact finite Gram absolute mass

For every prime \(\mathfrak p\) of \(O\), let \(q=N(\mathfrak p)\) and \(a=v_{\mathfrak p}(I)\), \(b=v_{\mathfrak p}(J)\), including exponent \(0\) when \(\mathfrak p\nmid IJ\). Pinned source characters on the relatively-prime prime powers are glued by CRT. A primitive additive character of \(O/I\) decomposes into primitive additive characters on these prime powers, up to *unit frequency multipliers*. Those multipliers change complex phases, but not \(p\)-adic valuations or absolute Gauss row magnitudes. Thus the normalized absolute row product on \(O/(I\cap J)\) factors into independent local finite averages.

Define \(\mu_q(a,b)\) for \(a,b\ge0\) and \(c=\min(a,b),d=\max(a,b)\):

| Exponent case | Exact \(\mu_q(a,b)\) |
|---|---|
| \(a=b=0\) | \(1\) |
| \(a=b>0\) | \(1-q^{-1}\) |
| \(c=0<d,\ 6\nmid d\) | \((1-q^{-1})q^{(1-d)/2}\) |
| \(c=0<d,\ 6\mid d\) | \(2(1-q^{-1})q^{-d/2}\) |
| \(0<c<d,\ 6\nmid c\) | \(0\) |
| \(0<c<d,\ 6\mid c,\ 6\nmid d\) | \((1-q^{-1})^2q^{(c-d+1)/2}\) |
| \(0<c<d,\ 6\mid c,\ 6\mid d\) | \(2(1-q^{-1})^2q^{(c-d)/2}\) |

Here the local finite expectation is taken over \(O/\mathfrak p^{\max(a,b)}\) for the **normalized** local Gaussian rows; the case \(a=b=0\) has trivial period one. The above entries are all at most one for good prime \(q\ge7\).

**Proof:** For local exponent \(e>0\), the actual Gauss table gives normalized squared magnitudes

\[
|g_e(z)|^2 =
\begin{cases}
q^{e-1},&6\nmid e,\ v_p(z)=e-1,\\
q^{e-2},&6\mid e,\ v_p(z)=e-1,\\
(q-1)^2q^{e-2},&6\mid e,\ v_p(z)\ge e,\\
0,&\text{otherwise}.
\end{cases}
\tag{2}
\]

For \(e=0\), \(g_0\equiv1\). On \(O/\mathfrak p^d\), the probabilities are \(\Pr(v_p(z)=v)=(q-1)/q^{v+1}\) for \(v<d\) and \(\Pr(v_p(z)\ge d)=q^{-d}\). Inserting (2) and summing the at most two surviving valuation shells gives every entry of the table **exactly**, with no averaging assumption.

Set

\[
\boxed{M(I,J):=\prod_{\mathfrak p\mid IJ}
       \mu_{N(\mathfrak p)}(v_{\mathfrak p}(I),v_{\mathfrak p}(J)).}
\tag{3}
\]

Then, writing \(L=I\cap J\), the **exact finite-period absolute Gram mass** is

\[
\boxed{\frac1{N(L)}
 \sum_{z\in O/L}|g_I(z)\overline{g_J(z)}|=M(I,J).}
\tag{4}
\]

In particular, whenever some shared prime has unequal positive valuations with \(6\nmid\min(v_p(I),v_p(J))\),

\[
\boxed{g_I(z)\overline{g_J(z)}=0\quad\text{for every }z\in O.}
\tag{5}
\]

This pointwise annihilation now applies to **arbitrary composite supported source columns**, not only pure prime powers. Even when \(I\) and \(J\) have the same norm modulo 36, (5) may kill their mixed pair. Example: for norm-37 prime \(\mathfrak p\), \(\mathfrak p^1\) and \(\mathfrak p^7\) have the same norm modulo 36, yet (5) forces their mixed product to vanish; \(\mathfrak p^6\) and \(\mathfrak p^7\) can survive.

**Do not confuse (4) with a Gaussian energy bound:** a radial window on the *infinite* Eisenstein lattice is not uniform over the finite period, especially at small K. This distinction is a substantive constraint.

## 3. An improved nonzero-Fourier bound with explicit conductor separation

For any finite character \(\xi\) of \(O/L\), the normalized Fourier coefficient of \(z\mapsto g_I(z)\overline{g_J(z)}\) obeys, by (4),

\[
|\widehat{g_I\overline{g_J}}(\xi)|\le M(I,J).
\tag{6}
\]

At frequency zero, the pinned `SecondDiagonal.actual_zero_off_diagonal` supplies the **exact** coefficient:

\[
\widehat{g_I\overline{g_J}}(0)=
 \mathbf1_{I=J}\frac{\varphi_O(I)}{N(I)},\quad
\varphi_O(I)=|(O/I)^\times|.
\tag{7}
\]

Use the **least common period** \(L=I\cap J\) from PR #579, not the larger product period \(IJ\). For every \(A>0\), Schwartz decay of the radial source gives a uniform \(C_{A,\Phi}\) such that, for **K≥1**,

\[
\boxed{\begin{aligned}
\bigg| \sum_{z\in O} g_I(z)\overline{g_J(z)}
 \Phi\!\left(\frac{N(z)}K\right)
 -c_\Phi K\,\mathbf1_{I=J}\frac{\varphi_O(I)}{N(I)}\bigg|
 \le{}& C_{A,\Phi}\,K\,N(L)\,M(I,J)\\
 &\ \cdot\left(1+\sqrt{\frac K{N(L)}}\right)^{-A}.
\end{aligned}}
\tag{8}
\]

Here \(c_\Phi=\texttt{paperRadialFourier}(\Phi)(0)>0\), inclusive of the Eisenstein dual covolume factor \(2/\sqrt3\). The proof is finite Fourier expansion over \(O/L\), coefficient bound (6), then periodic Poisson summation and rapid decay for each nontrivial dual class (plus nonzero frequencies of the trivial class). Its geometric constants are independent of I,J because each ideal generator acts as a Euclidean similarity. The \(M(I,J)\) factor is **new relative to the admitted PR #579 bound**. It yields exact zeros at the valuation barriers and explicit powers of prime norms at six-divisible but separated exponents.

Together with the **six-sector unit selection** from PR #582, a fully source-bound, unconditional (but not yet sharp) inequality follows for either genuine main or nested-error child:

\[
\boxed{\begin{aligned}
0\le E_s(K)\le \frac K{V_s}\bigg[
 &c_\Phi\sum_{I\in Q_s}|c_I|^2\frac{\varphi_O(I)}{N(I)}\\
 &+C_{A,\Phi}\sum_{\substack{I,J\in Q_s\\
                  N(I)\equiv N(J)\ (\mathrm{mod}\ 36)}}
 |c_Ic_J|\,N(I\cap J)\,M(I,J)
 \left(1+\sqrt{\frac K{N(I\cap J)}}\right)^{-A}
 \bigg],\qquad K\ge1 .
\end{aligned}}
\tag{9}
\]

The summands with \(M(I,J)=0\) are identically zero for all K; they can be omitted without loss. The bound (9) is **not** the four `seededFactors` powers. It does not count the remaining pairs sharply or prove a favorable K/N(L) ratio from the actual `Ready`, `ZeroAt`, or `PositiveAt` conditions. In particular, coprime squarefree pairs may have \(M(I,J)\) close to one and demand true oscillatory cancellation.

An alternative fully nonasymptotic inequality follows from the **exact surviving-pair graph** \(\Gamma_s\) whose edges satisfy both mod-36 equality and no forbidden unequal-sixth-power valuations. Let \(D_I(K)=\sum_z |g_I(z)|^2\Phi(N(z)/K)\) and \(d_I\) be the graph degree counting the self-edge. Weighted Cauchy–Schwarz and \(2xy\le x^2+y^2\) give

\[
\boxed{E_s(K)\le \frac1{V_s}\sum_{I\in Q_s}d_I|c_I|^2D_I(K).}
\tag{10}
\]

Both inequalities are genuine Gaussian-source estimates; neither replaces the missing analytic conductor budget.

## 4. The complete composite lattice-origin identity, and a necessary sharp-energy test

For any supported \(I=\prod\mathfrak p^{e_{\mathfrak p}}\), the actual multiplicative source character is principal **if and only if** every positive exponent \(e_{\mathfrak p}\) is divisible by six. Hence

\[
\boxed{
g_I(0)=
\begin{cases}
\varphi_O(I)/\sqrt{N(I)}, &6\mid v_{\mathfrak p}(I)\ \forall\mathfrak p\mid I,\\
0, &\text{otherwise}.
\end{cases}}
\tag{11}
\]

The empty product \(I=O\) satisfies the first case and contributes 1. This is a **real positive** number, not merely its absolute value: the additive trace at z=0 is 1 and the principal character sums to the number of units.

As \(\Phi(0)=1\) and \(\Phi\ge0\), for **every K>0**,

\[
\boxed{E_s(K)\ge
\frac1{V_s}
\left|\sum_{\substack{I\in Q_s\\
6\mid v_{\mathfrak p}(I)\ \forall\mathfrak p\mid I}}
 c_I\frac{\varphi_O(I)}{\sqrt{N(I)}}\right|^2 .}
\tag{12}
\]

When \(2K\le1\), all nonzero Eisenstein lattice points lie outside the support of the genuine \(\Phi\), so (12) becomes **an equality**. This is an explicit necessary condition on any proposed sharp `actual_main_gaussian_from_bands` or `actual_error_gaussian_from_bands` RHS: that RHS must pay this exact coherent origin amplitude. It is **not** a counterexample to either theorem without an actual admissible source with verified coefficients and gates.

A concrete **projection-no-go witness** uses actual prime-power rows at a good norm-q prime: \(g_1(0)=1\) and \(g_{\mathfrak p^6}(0)=(q-1)q^2\). Choose coefficients \(c_1=1\), \(c_{\mathfrak p^6}=-1/[(q-1)q^2]\). For \(0<K\le1/2\), the Gaussian energy of this two-column polynomial is **zero** (the origin amplitudes cancel), whereas deleting the \(\mathfrak p^6\) column makes its Gaussian energy **one** (with unit volume). Thus

\[
\boxed{\text{Coefficientwise prime-coprime projection is not
nonexpansive in small-radius physical Gaussian energy.}}
\]

This is an exact source-row algebraic example, **not** a claim that the chosen coefficients arise from an admissible F003 `Input`.

## 5. Stronger source fact: **each** genuine child is conductor-punctured

An independent read of the **proof body** of pinned \`Moments/OriginalChildEnergy.original_source_punctured_column\` corrects a weaker earlier interpretation: in its noncoprime branch (lines 32–43) it proves directly, **for every individual allocation B**,

\[
\neg\operatorname{IsCoprime}(C,I)\ \Longrightarrow\
 \texttt{finiteColumnCoefficient}(\texttt{liveBox}_B,\texttt{liveProfile}_B)(I)=0.
\tag{13}
\]

It invokes pinned \`Moments/LiveSupport.live_column_original_support\` (blob \`b1b14b229ced32ad20d6e3dc0e9b8651a4db10fb\`). Pinned \`Moments/AmplificationLiveMask.column_mask\` (blob \`c0b68ea2d09df9f552c9f82df9de69f85ffc8fbb\`) multiplies the live coefficient by a 0/1 mask; it cannot create a nonzero coefficient at an excluded residual ideal. **The individual masked child is already coprime to C at its nonzero coefficient support.** It is NOT merely a prime-free property of the coherent sum.

There is an even stronger **hereditary** restriction, requiring no new projection. Pinned \`Moments/SourceCommonMask.column_nonzero_masks\` (blob \`8186f884a29ef58f3160bef5907cf369a3ca848a\`) proves for every actual source:

\[
\boxed{\texttt{(original s T seed).beta}(I)\ne0
\ \Longrightarrow\ \operatorname{IsCoprime}(I,T)
 \ \wedge\ \mathrm{seed}\mid I.}
\tag{14}
\]

Proof: every nonzero source coefficient has a nonzero contributing tuple; its **actual** \`profileCoefficient\` enforces \(\operatorname{IsCoprime}(I,T)\) and seed divisibility. This is a pre-existing *Lean theorem*. The following are independently reconstructed instantiations into the exact Family 003 objects using \`AmplificationChildInput.child_columns\`/\`child_profile\`, \`FirstSecondActiveErrorGates.errorInput\`, and \`FirstAnnularActiveInput.original_active\`:

* **Genuine main child** \(d_m=\texttt{child}(s,C,R_0,B,\tau,t)\) has source \(\texttt{original}(d_m,R_0C,\mathrm{seed})\). Every nonzero coefficient satisfies
  \[
  \boxed{\operatorname{IsCoprime}(I,R_0 C),\quad \mathrm{seed}\mid I.}
  \tag{15}
  \]
* **Genuine nested error child** \(d_e=\texttt{errorInput}(s,C,R_0,B,\tau,t,Q,k,B',\upsilon,v)\), \(k\in\{1,6,7\}\), has source \(\texttt{original}(d_e,(R_0C)Q^k,\mathrm{seed})\). Every nonzero coefficient satisfies
  \[
  \boxed{\operatorname{IsCoprime}(I,(R_0C)Q^k),\quad \mathrm{seed}\mid I.}
  \tag{16}
  \]
  The \(\upsilon\)-dependent child is the **actual** \`CanonicalErrorGaussian\` input, not a synthetic replacement.

Consequently, for *every active pair of nonzero coefficients* \(I,J\) in the main/error energy, their common period \(L=I\cap J\) is coprime **as an ideal** to the full input conductor in (15)/(16). In particular Q cannot appear as an ideal factor of either residual error column or pair period. No claim is made that the **integer norms** of coprime ideals are necessarily coprime (two prime ideals may lie above one rational prime).

**Exact empty-case gate:** If the seed is not coprime to the respective full input conductor, (14) forces all original coefficients to vanish and the Gaussian source energy equals zero. This follows from the actual masks, not from a newly imposed hypothesis.

## 6. The remaining real loss: allocation cardinality and within-sector correlation

For the upstream error stages \(n\in\{0,5,6\}\), set \(k=n+1\in\{1,6,7\}\) and \(P=(p)\). The pinned theorem \`AmplificationSourcePool.residualColumns_eq\` separately proves that **raw** error extraction takes exactly p-valuation k before division, leaving only p-free residual ideals:

\[
\texttt{residualColumns}(S,p,k)=
\{I\in\texttt{supportedColumns}(\texttt{residualPool}(P^k,S)):
\operatorname{IsCoprime}(I,P)\}.
\tag{17}
\]

By (13)–(16), the *individual actual allocated children* already respect the conductor puncture too. The exact polynomial allocation decomposition is \(\sum_{B\in\mathcal A} f_BP_B\). Under the prime-slot coprimality gate, pinned \`AmplificationAllocationScale.frozenCoefficient_exact\` says

\[
f_B=
\begin{cases}
1,&\operatorname{IsCoprime}(P^k,R),\\
0,&\text{otherwise},
\end{cases}
\quad\text{independent of }B,
\qquad m:=|\mathcal A|\le k+1.
\tag{18}
\]

For the nonzero case, the **actual physical Gaussian** norm \(\|\cdot\|_\Phi\) gives the source's Cauchy inequality

\[
\left\|\sum_B P_B\right\|_\Phi^2
\le m\sum_B\|P_B\|_\Phi^2\le(k+1)\sum_B\|P_B\|_\Phi^2.
\tag{19}
\]

An exact Hilbert variance identity identifies the possible gap:

\[
\boxed{m\sum_B\|P_B\|_\Phi^2-\left\|\sum_B P_B\right\|_\Phi^2
=\sum_{\{B,B'\}\subset\mathcal A}\|P_B-P_{B'}\|_\Phi^2\ge0.}
\tag{20}
\]

The factors \(k+1=\mathbf{2,7,8}\) remain the **actual** paid allocation costs unless the allowed source profiles and radii force a positive variance gap or a sharper coherent estimate. **Projector stability is not a missing obligation**: every individual child is already masked to the correct conductor. The generic two-Gauss-row projection counterexample in §4 remains correct but is **not** a counterexample to the Family 003 child construction and is not needed for the proof.

**Conductor reduction for the new exact local Gram bound:** In (9), restrict to coefficients nonzero under (15)/(16). Neither the extracted C nor Q can divide \(I\cap J\) in the relevant child. Thus they contribute **no local factor** to \(M(I,J)\), nor a norm factor to the minimal source period \(N(I\cap J)\). This is a genuine exact-conductor fact from the pinned source, not a free saving in the final power of Z: all \(\upsilon\)-modulus, \(ZeroAt/PositiveAt\), height, mesh, radius, and seed losses must still be accounted for.

## 7. Exact adversarial replay and remaining target

Companion `f003_composite_valuation_gram_puncture_adversary.py` uses exact arithmetic \(\mathbb Q+\mathbb Q\sqrt q\), not floating point, to independently evaluate both the source local valuation-shell probabilities and the closed table \(\mu_q(a,b)\) for all 0≤a,b≤18 and q∈{7,13,19,31,37}; checks two-prime CRT products, six-sector interaction examples, the q37 same-sector but pointwise-disjoint \((p,p^7)\) case, exact sixth-power origin values and the two-column projection counterexample, plus raw k∈{1,6,7} valuation and plain allocation counts. The checks **do not** independently elaborate the composite CRT theorem in Lean or replay the infinite Schwartz Poisson estimate.

**Remaining proof obligation:** bound the *surviving* source-specific weighted within-sector composite CRT pair sum in (9) using genuine `ZeroAt`/`PositiveAt` induction and conductor/height/mesh losses. Establish source-dependent control of the punctured allocation variance or projector-stable child bound, including the exact origin in (12); recover all **four** seeded Gaussian powers with the canonical \(C_0,C_1\), \(\upsilon\)-conductor, seed and radius payments. The sharper finite Gram factors and independently transported exact conductor puncture are analytic ingredients, **not** by themselves the sharp Family 003 seven-eighths proof.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-COMPOSITE-VALUATION-GRAM-PUNCTURE/1
SOURCE: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
PINNED FORMAL INPUT: genuine prime-power Gauss table; canonical CRT character;
 exact residualColumns_eq, residual_energy_eq_punctured,\n column_nonzero_masks, live_column_original_support and frozenCoefficient_exact;
 secondDiagonal zero mode; source normalized Gauss energy
NEW MATHEMATICAL RECONSTRUCTION: exact composite pairwise local L1 Gram factors;
 pointwise valuation-annihilation graph; improved Fourier remainder with M(I,J);
 exact composite origin obstruction; exact inherited input-conductor puncture\n of every nonzero main/error child coefficient; allocation Hilbert variance identity
NEW INDEPENDENT LEAN ELABORATION: NOT PERFORMED
SHARP FULL MAIN/ERROR CHILD GAUSSIAN ENERGY: OPEN
FAMILY 003 SEVEN-EIGHTHS: UNRESOLVED
MATHCERT: NONE
```
