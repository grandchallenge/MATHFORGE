# OAI-26 F003 — exact global-unit eigensectors for genuine composite Gaussian child energies

**Assignment:** GCL-OAI26-F003-COMPOSITE-GAUSSIAN-UNIT-SELECTION/1  
**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Predecessor:** protected MATHFORGE PR #581, commit `27c867f6f2dd15eb1b2784a5ae5966245b063922`  
**Disposition:** `GENUINE_COMPOSITE_RADIAL_GAUSS_SIX_ORTHOGONAL_EIGENSECTORS_MATHEMATICAL_PROOF__WITHIN_SECTOR_SHARP_ENERGY_OPEN`  
**Certification:** NONE. Bounded mathematical reconstruction, no newly Lean-elaborated theorem or MATHCERT.

## 1. The actual pinned arithmetic unit theorem

Use the pinned source, not an inferred local phase:

- `Eisenstein/UnitNormalization.lean:idealRowHom_unit_norm` (blob `fa4c3434d200a7fd7e38c7daa619bfa4553ab1c8`) proves, for every supported nonzero Eisenstein ideal \(I\) and global unit \(u\),
  \[
  \texttt{idealRowHom}(u,I)=\operatorname{eisEmbedding}
  \big(u^{(N(I)-1)/6}\big).
  \tag{1}
  \]
  Its `ideal_norm_mod_six_of_good` also proves \(N(I)\equiv1\pmod6\). Both follow because every prime factor of a `Supported` ideal is good and has residue norm \(1\bmod6\).
- `Detector/CalibrationRemoval.lean:sexticGauss_unit_scale` (blob `d672bbf9e4dc9756683957368dc913afde06ebb1`) proves
  \[
  \mathrm{sexticGauss}(a,u z)=
  \texttt{idealRowHom}(u,(a))^{-1}\,
  \mathrm{sexticGauss}(a,z)
  \tag{2}
  \]
  when \(u\) is a global unit, and the modulus \((a)\) is supported.
- `Moments/SourceRow.lean:sourceGenerator` (blob `42584a9c87b0b8a983bcf7b21792aff05e4d1b8d`) identifies \(a_I=\texttt{primaryGenerator}(I)\) with ideal \(I\), so this applies to *every genuine supported original source column*.
- `Moments/GaussEnergy.lean:gaussRow_pair_summable` (blob `200d3d5c9fb828b7bd1eb4e5a7160b10c5fd65bd`) justifies all infinite weighted pair sums, and `Moments/OriginalChildEnergy.lean:sourceGaussEnergy` (blob `ee1338c7b068e68930073a0ef820df3e9168e296`) is the exact actual main/error child energy.

The unit group \(U=O^\times\) has exactly six elements. Fix the primitive sixth root \(\varepsilon=1+\omega\). Every supported ideal has one of exactly **six** permissible residues \(N(I)\bmod36\in\{1,7,13,19,25,31\}\). Define the sector label

\[
\gamma(I):=\frac{N(I)-1}{6}\bmod6
\quad\in\mathbb Z/6\mathbb Z .
\tag{3}
\]

This division is integer-valued because \(N(I)\equiv1\bmod6\). Formula (1) gives
\(\chi_I(\varepsilon)=\varepsilon^{\gamma(I)}\) after complex embedding. Formula (2) implies that the **actual normalized Gaussian row** \(g_I\) has unit-rotation covariance

\[
\boxed{\displaystyle g_I(\varepsilon z)=
\varepsilon^{-\gamma(I)}g_I(z).}
\tag{4}
\]

This covariance does **not** assume prime powers, squarefree columns, independent CRT factors, a favorable Gaussian radius, or a nonprincipal local sixth-power exponent.

## 2. Complete composite cross-sector annihilation

For any supported ideals \(I,J\), any \(K>0\), and any source-admissible smooth radial \(W\), define

\[
B_{IJ}(W,K)=\sum_{z\in O}
 g_I(z)\,\overline{g_J(z)}\,W(N(z)/K).
\]

The change of variable \(z\mapsto\varepsilon z\) is a bijection of \(O\), fixes \(N(z)\) and therefore preserves the radial weight. From (4),

\[
B_{IJ}(W,K)
=\varepsilon^{\gamma(J)-\gamma(I)}B_{IJ}(W,K).
\]

As \(\varepsilon\) has **exact order six**, if \(\gamma(I)\ne\gamma(J)\), the multiplier differs from 1, giving the exact theorem

\[
\boxed{
N(I)\not\equiv N(J)\pmod{36}
\quad\Longrightarrow\quad
B_{IJ}(W,K)=0\qquad\text{for all }K>0.
}
\tag{5}
\]

This is valid for **all composite supported source columns**, not merely primes, and for *every radial smoothing*, not just `ballProfile`. It strengthens the norm-37 selection for \(p^6/p^7\) from admitted PR #580: q≡1(mod36) means the two power norms have equal class, so unit-orbit cancellation cannot be invoked; for q=7,13,19,31 their classes differ and (5) explains the exact zero directly.

**Source-dependent caveat:** equality of norms mod 36 does *not* imply a nonzero mixed pair. It merely means global-unit symmetry does not force vanishing. Pinned `SecondDiagonal.actual_zero_off_diagonal` still kills **all** distinct ideals at zero Fourier frequency. Global-unit and zero-mode orthogonality are independent constraints.

## 3. Exact six-sector decomposition of both genuine child families

For the actual input \(s\), its finite original supported source columns \(Q_s\), seed, normalization modulus \(R\), coefficients \(c_I=\beta_I\,\texttt{heightCoeff}(s.\eta,s.t,I)\), and real nonnegative radial source bump \(\Phi=\texttt{ballProfile}\), let

\[
P_{s,r}(z)=\sum_{\substack{I\in Q_s\\ \gamma(I)=r}}c_I g_I(z),
\qquad
P_s(z)=\sum_{r\in\mathbb Z/6\mathbb Z} P_{s,r}(z).
\]

By (5) and finite summability,

\[
\boxed{\displaystyle
\texttt{normalizedGaussSource}(s,R,\mathrm{seed},\Phi,K)
=\sum_{r\in\mathbb Z/6\mathbb Z}
\frac1{\operatorname{volume}(s)}
\sum_{z\in O}|P_{s,r}(z)|^2\Phi(N(z)/K),
\qquad K>0.
}
\tag{6}
\]

Every summand is **nonnegative**, because \(\Phi\) is real nonnegative. There are **at most six** sectors, with no dependence on the size of the source pool, seed, conductor, nested error \(k\), height, mesh, or radius. The decomposition is therefore valid for the genuine main `child` and nested `errorInput`, with their respective **actual** \(K_\mathrm{main}, K_\mathrm{error}\), positive volumes and `Ready` gates, once those input objects are instantiated.

A concrete way to see the selection is to average each polynomial over the six rotations:

\[
\Pi_r P_s(z)=\frac16\sum_{j=0}^{5}
\varepsilon^{rj}P_s(\varepsilon^j z).
\]

By the exact geometric sum, \(\Pi_rP_s=P_{s,r}\). These are six mutually orthogonal projectors in the weighted Gaussian-energy inner product, not six fictitious independent stochastic blocks.

## 4. Quantitative limits and next missing proof

For each sector the bound of PR #579 can still be used, **now with all cross-sector pairs deleted exactly**:

\[
0\le E_s(K)\le \frac{K}{V_s}\left[
c_\Phi\sum_I|\beta_I|^2\frac{\varphi_O(I)}{N(I)}
+
C_{A,\Phi}
\sum_{\substack{I,J\in Q_s\\\gamma(I)=\gamma(J)}}|\beta_I\beta_J|
 N(I\cap J)\left(1+\sqrt{\frac{K}{N(I\cap J)}}\right)^{-A}
\right],\ K\ge1.
\tag{7}
\]

This is a genuine-source sharpening over the unrestricted lcm double sum, with exactly the same mathematical proof status as the predecessor. It is **not** a bound independent of the number/weights of within-sector pairs; cannot be claimed to yield the four sharp seeded factors by itself. The last nonzero classes include prime powers with exponents divisible by six, q=37 critical characters, and the principal-larger-power origin/lattice discrepancy. These require the actual source's CRT-sector and `ZeroAt`/`PositiveAt` estimates.

## 5. Adversarial test, source and claim ledger

The committed `f003_composite_unit_mod36_adversary.py` performs exact integer Eisenstein norm and unit algebra, verifies that supported product ideal norm labels add mod six, tests the six orthogonal geometric sums, checks the q=7/13/19/31/37 examples and q^6/q^7 gate, and checks the basic *unit equivariance* of genuine-shaped finite character Gauss transforms on Eisenstein prime quotient examples, using exact cyclotomic arithmetic. The finite tests use a chosen primitive additive character of the finite quotient, **not** a claim to have recreated the pinned `quotientTrace` function byte-for-byte; the universal covariance is proved mathematically in §1 from the pinned source theorem. No testing of actual composite child pool enumeration or new Lean elaboration is claimed.

```text
RESULT/1
ASSIGNMENT: GCL-OAI26-F003-COMPOSITE-GAUSSIAN-UNIT-SELECTION/1
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
SOURCE LEAN: idealRowHom_unit_norm; sexticGauss_unit_scale; gaussRow summability
NEW MATHEMATICAL PROOF: exact norm mod36 composite unit selection; six-sector
 nonnegative energy identity for actual main and nested-error child families;
 cross-sector deletion in genuine lcm Gaussian bound
NEW LEAN ELABORATION: NOT PERFORMED
WITHIN-SECTOR SHARP MAIN/ERROR ENERGY: OPEN
SEVEN-EIGHTHS: UNRESOLVED
MATHCERT: NONE
```
