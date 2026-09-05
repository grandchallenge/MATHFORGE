# ASP-T8-RECON-001 — Data-driven uniform residual certificates after peeling

**Campaign candidate:** `ASP-001`  
**Theory target:** `T8`  
**Issue:** `grandchallenge/MATHFORGE#113`  
**Owning pillar:** MATHFORGE  
**Exact base:** `ed8a65410336489ea5646808265c44f5387bebb8`  
**Status:** theory reconnaissance; no theorem promotion  

## 1. Question

ASP-WP00 identified the unresolved theory boundary as follows:

> obtain useful data-driven upper certificates on unresolved optimization-relevant surrogate error without paying the full cost of globally reconstructing the objective in `L_infinity`.

The June 2026 paper by van Doornmalen, Molina, Verdugo and Verschae, *Tight L-infinity Sample Complexity for Low-Degree and Sparse Boolean Polynomials* (`arXiv:2606.17319`), makes the obstruction precise: noisy global uniform reconstruction has dimension-dependent lower bounds even for adaptive learners.

The correct T8 objective is therefore not a dimension-free `L2 -> L_infinity` miracle. It is an **instance-dependent certificate whose dimension penalty shrinks under ASP restrictions**.

This note develops the strongest current candidate: independent holdout residual energy plus the exact evaluation norm of the residual function space.

## 2. Prior-art boundary

The central norm-transfer object is standard. For a finite-dimensional subspace `V` of `L2(mu)` with orthonormal basis `phi_1,...,phi_N`, the reciprocal Christoffel function / diagonal reproducing kernel is

\[
K_V(x)=\sum_{j=1}^N |\phi_j(x)|^2
      = \sup_{0\ne v\in V}\frac{|v(x)|^2}{\|v\|_2^2}.
\]

Christoffel functions are established tools in approximation theory and modern optimal-sampling analyses. See, for example:

- Ben Adcock, *Optimal sampling for least-squares approximation*, `arXiv:2409.02342`;
- Ling Guo, Akil Narayan, Liang Yan, Tao Zhou, *Weighted approximate Fekete points: Sampling for least-squares polynomial approximation*, `arXiv:1708.01296`;
- the broader randomized weighted least-squares literature cited therein.

ASP does **not** claim this machinery as novel. The research question is whether its composition with adaptive restriction, branch margins and product-space spectral structure yields a useful certified black-box optimizer.

## 3. T8.1 candidate — sharp evaluation-norm transfer

Let

\[
\Lambda_V^*:=\sup_x K_V(x).
\]

Then every `r in V` satisfies

\[
\boxed{
\|r\|_\infty\le \sqrt{\Lambda_V^*}\,\|r\|_2.
}
\]

### Derivation

For any `x`, expand

\[
r=\sum_j a_j\phi_j.
\]

Cauchy-Schwarz gives

\[
|r(x)|
\le
\left(\sum_j |a_j|^2\right)^{1/2}
\left(\sum_j |\phi_j(x)|^2\right)^{1/2}
=
\|r\|_2\sqrt{K_V(x)}.
\]

Taking the supremum over `x` gives the stated inequality.

The constant is exact. At a point `x_*` attaining the supremum, choose the normalized reproducing-kernel section

\[
r_*(\cdot)\propto \sum_j \overline{\phi_j(x_*)}\phi_j(\cdot).
\]

Then

\[
\frac{|r_*(x_*)|}{\|r_*\|_2}=\sqrt{K_V(x_*)}
=\sqrt{\Lambda_V^*}.
\]

**Provenance classification:** standard finite-dimensional Hilbert-space / Christoffel consequence. The ASP contribution, if any, begins with how `V` changes under peeling and how the resulting certificate interacts with optimization margins.

## 4. Product-space specialization — certificate dimension

Let the active product domain be

\[
\mathcal X_U=\prod_{i\in U}\mathcal X_i,
\qquad m_i:=|\mathcal X_i|,
\]

with the uniform product measure. For every coordinate choose any complete orthonormal basis

\[
\phi_{i,0}\equiv1,
\phi_{i,1},\ldots,\phi_{i,m_i-1}.
\]

Completeness implies, pointwise,

\[
\sum_{a=0}^{m_i-1}|\phi_{i,a}(x_i)|^2=m_i,
\]

and therefore

\[
\sum_{a=1}^{m_i-1}|\phi_{i,a}(x_i)|^2=m_i-1.
\]

Consider the complete Efron-Stein degree-`<=D` tensor subspace

\[
V_{\le D}(U)
=
\operatorname{span}\{\Phi_\alpha:
|\operatorname{supp}(\alpha)|\le D\}.
\]

Its diagonal kernel is

\[
\begin{aligned}
K_{\le D}(x)
&=
\sum_{|\operatorname{supp}(\alpha)|\le D}
|\Phi_\alpha(x)|^2\\
&=
\sum_{\substack{S\subseteq U\\|S|\le D}}
\prod_{i\in S}
\left(\sum_{a_i=1}^{m_i-1}|\phi_{i,a_i}(x_i)|^2\right)\\
&=
\boxed{
\sum_{\substack{S\subseteq U\\|S|\le D}}
\prod_{i\in S}(m_i-1)
}.
\end{aligned}
\]

It is constant in `x`. Define this quantity as the **ASP certificate dimension**

\[
\boxed{
C_D(U):=
\sum_{\substack{S\subseteq U\\|S|\le D}}
\prod_{i\in S}(m_i-1).
}
\]

It equals `dim V_{<=D}(U)`.

For equal cardinality `q` and `k=|U|`,

\[
\boxed{
C_D(k,q)=\sum_{j=0}^D {k\choose j}(q-1)^j.
}
\]

For a complete degree band `d < degree <= D`, the same calculation gives

\[
C_{(d,D]}(U)
=
\sum_{\substack{S\subseteq U\\d<|S|\le D}}
\prod_{i\in S}(m_i-1).
\]

### Consequence for peeling

Restriction removes coordinates from `U` and folds interactions downward in degree. Both effects can reduce certificate dimension.

Thus ASP has a new trajectory variable:

\[
\boxed{
C_t=\Lambda_{V_t}^*.
}
\]

This is statistically distinct from interaction treewidth `w_t`:

- `C_t` controls how costly it is to convert residual `L2` evidence into uniform safety;
- `w_t` controls how costly it is to optimize the retained factorized surrogate.

A low-width model can still have a large certificate dimension, and vice versa.

## 5. Full-space boundary and T9 needle obstruction

Take `D=|U|`. Then

\[
C_D(U)
=
\prod_{i\in U}m_i
=|\mathcal X_U|=:M.
\]

Hence every arbitrary function on the active uniform domain satisfies

\[
\|r\|_\infty\le\sqrt M\,\|r\|_2.
\]

This cannot be improved in worst case. Let

\[
r(x)=\mathbf 1\{x=x_0\}.
\]

Then

\[
\|r\|_\infty=1,
\qquad
\|r\|_2=M^{-1/2},
\]

so

\[
\frac{\|r\|_\infty}{\|r\|_2}=\sqrt M.
\]

This is the finite-domain "needle" obstruction in its sharpest norm-transfer form.

### Interpretation

T8 does not evade global `L_infinity` lower bounds. Without a smaller residual class, its safety factor is exactly the active-domain size penalty one should expect.

Peeling is useful only if it makes `C_t` materially smaller **before** margin certification becomes necessary.

This gives a falsifiable programme condition rather than a rhetorical benefit.

## 6. T8.2 candidate — independent holdout certificate

Assume initially a noiseless bounded oracle

\[
f:\mathcal X\to[-B,B].
\]

Let a surrogate `g` be fitted on data independent of the validation sample. Clip it pointwise to `[-B,B]`; clipping cannot increase `|f-g|`.

Set

\[
r=f-g,
\qquad
Z=r(X)^2,
\qquad X\sim\mu.
\]

Then

\[
0\le Z\le R:=4B^2,
\qquad
\mathbb E Z=\|r\|_2^2.
\]

For independent validation points `X_1,...,X_m`, define

\[
\widehat\mu
=
\frac1m\sum_{j=1}^m r(X_j)^2.
\]

A standard one-sided Bernstein inequality gives, with `L=log(1/delta)`,

\[
\mu-\widehat\mu
\le
\sqrt{\frac{2\operatorname{Var}(Z)L}{m}}
+
\frac{RL}{3m}.
\]

Since `0 <= Z <= R`,

\[
\operatorname{Var}(Z)\le\mathbb E Z^2\le R\mu.
\]

Therefore

\[
\mu
\le
\widehat\mu+
\sqrt{\frac{2R\mu L}{m}}
+
\frac{RL}{3m}.
\]

Using

\[
\sqrt{2\mu a}\le\frac\mu2+a,
\qquad a:=\frac{RL}{m},
\]

we obtain the conservative explicit upper confidence bound

\[
\boxed{
\|r\|_2^2=\mu
\le
U_2
:=
2\widehat\mu+
\frac{8RL}{3m}
=
2\widehat\mu+
\frac{32B^2}{3m}\log\frac1\delta
}
\]

with probability at least `1-delta`.

If `r in V`, T8.1 immediately gives

\[
\boxed{
\|f-g\|_\infty
\le
\sqrt{\Lambda_V^* U_2}
}
\]

with the same confidence.

### Why this is materially different from uniform reconstruction

The validation stage never estimates the individual coefficients of `r` and never reconstructs `r(x)` at every point. It estimates one scalar residual-energy quantity and combines it with a deterministic function-class evaluation norm.

This can only be useful when `Lambda_V^*` is sufficiently small. The method exposes that dependency explicitly instead of hiding it in an exact-sparsity assumption.

## 7. Margin-dependent certification cost

Suppose branch pruning at a restricted state requires uniform error

\[
\varepsilon_t<\Gamma_t/4,
\]

where `Gamma_t` is the true conditional branch margin sufficient to force the observable T6 certificate.

The holdout condition is

\[
\Lambda_t U_{2,t}<\Gamma_t^2/16.
\]

In the idealized near-zero-residual regime `\widehat\mu_t\approx0`, it suffices schematically that

\[
m_t
\gtrsim
\frac{B^2\Lambda_t}{\Gamma_t^2}
\log\frac1{\delta_t}.
\]

With the explicit conservative constant derived above,

\[
m_t
>
\frac{512}{3}
\frac{B^2\Lambda_t}{\Gamma_t^2}
\log\frac1{\delta_t}
\]

makes the confidence term alone smaller than `Gamma_t^2/(16 Lambda_t)`.

The exact constant is not the research claim; the structural scaling is:

\[
\boxed{
\text{certification effort}
\sim
\frac{\text{certificate dimension}}{\text{branch margin}^2}.
}
\]

This is precisely the type of dependence sought in ASP-WP00.

If the empirical residual-energy term `2 \widehat\mu_t` already exceeds the margin budget, no amount of confidence tightening can certify the branch using that surrogate. ASP must relearn, peel further, retain both branches, or switch certification strategy.

## 8. Approximate-subspace extension

Exact membership `r in V` need not be required.

Suppose

\[
r=v+h,
\qquad v\in V,
\qquad \|h\|_\infty\le\eta.
\]

Then

\[
\boxed{
\|r\|_\infty
\le
\sqrt{\Lambda_V^*}\,\|v\|_2+\eta.
}
\]

This recovers a role for a structural tail budget, but it is weaker than exact sparse recovery:

- `v` may be dense inside `V`;
- validation estimates its aggregate energy rather than every coefficient;
- the remaining `eta` is explicit rather than silently inferred from small `L2` error.

When no justified `eta` exists, use the full active function space. Then the certificate remains valid with `Lambda=M`, albeit potentially too expensive to be useful.

## 9. Boolean and categorical consequences

### Boolean Walsh

For any known Walsh index set `I`, every character has unit magnitude, so

\[
K_I(x)=|I|
\]

for every `x`. Therefore

\[
\|r\|_\infty\le\sqrt{|I|}\,\|r\|_2
\]

whenever the residual lies in that span.

No sparse coefficient recovery is required for this conversion; only a justified residual subspace is required.

### Mixed finite categorical spaces

For complete Efron-Stein degree classes, `C_D(U)` is basis-independent within each coordinate's nonconstant subspace and is computable directly from coordinate cardinalities.

This means the WP01 Helmert basis is not essential to the theorem; it is merely one convenient real orthonormal realization.

## 10. Relation to the 2026 global lower bound

The recent `L_infinity` lower bound should be treated as a design constraint, not an adversary to be rhetorically bypassed.

For a large global residual class, `Lambda_V^*` is correspondingly large. The holdout certificate then pays the same kind of dimension penalty that the minimax theory says must appear.

The ASP opportunity is sequential:

\[
\text{cheap structural scouting}
\to
\text{restriction}
\to
C_t\downarrow
\to
\text{holdout uniform certification}
\to
\text{margin-safe pruning}.
\]

Thus the question becomes empirical and instance-dependent:

> does `C_t / Gamma_t^2` fall rapidly enough along real restriction trajectories to justify the cost of discovering those trajectories?

WP02 and later work packages can answer that.

## 11. Noise boundary

The explicit bound in Section 6 is presently for a noiseless bounded oracle.

For observations

\[
Y=f(X)+\xi
\]

with centered sub-Gaussian `xi`, the observed squared residual

\[
(Y-g(X))^2
\]

has expectation at least `||f-g||_2^2` but is unbounded and sub-exponential rather than bounded. A valid T8 noisy extension therefore requires an explicit robust/sub-exponential upper-confidence construction.

This note deliberately does **not** insert an unproved noise constant.

Candidate routes include:

- a sub-exponential Bernstein bound with a known sub-Gaussian scale;
- median-of-means / robust mean bounds for squared residuals;
- replicated oracle evaluations to estimate and separate observation variance where replication is operationally sensible.

The noisy theorem remains open until one route is fully derived and tested.

## 12. Exact enumeration fallback

For an active finite domain of size `M_t`, ASP can always evaluate every active point when the cost is acceptable. This gives exact noiseless uniform residual information and removes statistical uncertainty.

A practical certification policy should compare:

\[
N_{\mathrm{holdout}}(\Lambda_t,\Gamma_t,\delta_t)
\quad\text{against}\quad
M_t.
\]

If the residual class is the full function space, `Lambda_t=M_t`, so holdout certification may offer little or no advantage over exhaustive evaluation. If `Lambda_t << M_t`, holdout becomes potentially valuable.

This comparison is an explicit reversal condition for the T8 route.

## 13. New peelability profile component

ASP-WP00 proposed

\[
\Pi(f)=\{n_t,d_t,s_t,\tau_t,w_t,\gamma_t,\Gamma_t\}_{t=0}^T.
\]

T8 suggests adding

\[
\boxed{C_t=\Lambda_{V_t}^*.}
\]

A more operational profile is therefore

\[
\boxed{
\Pi_{\mathrm{cert}}(f)
=
\{n_t,d_t,s_t,\tau_t,w_t,\gamma_t,\Gamma_t,C_t\}_{t=0}^T.
}
\]

Interpretation:

- `gamma_t`: expected spectral simplification available from the next peel;
- `tau_t`: unresolved structural approximation budget;
- `w_t`: exact surrogate optimization complexity;
- `Gamma_t`: conditional branch separability;
- `C_t`: cost of turning residual-energy evidence into uniform safety.

This five-way separation should replace any single "effective dimension" scalar in the mature theory.

## 14. Required finite confrontation extension

After ASP-WP01 is independently reviewed, a successor implementation should add the following tests without rewriting the already-confronted WP01 head:

1. compute `K_V(x)` exactly from an arbitrary declared spectral index set;
2. verify `max_x K_V(x)` against brute-force `sup ||r||_infinity^2/||r||_2^2` on small subspaces;
3. verify the closed-form `C_D(U)` for Boolean and mixed-cardinality complete degree classes;
4. construct the reproducing-kernel extremizer and full-space needle equality fixture;
5. simulate independent holdout UCBs and measure certificate tightness versus `C_t`;
6. compare holdout cost against exact enumeration;
7. insert the certified `epsilon_t` into T6 branch intervals and require zero false pruning in exact finite truth;
8. deliberately reuse training residuals in a negative control and demonstrate why that procedure is not accepted as a certificate.

## 15. Council reconnaissance findings

### Axiomatist

The useful T8 theorem needs an explicit residual function class `V`; if no smaller class is justified, `V` must be the complete active function space. The theory may not infer low certificate dimension from observed good fit alone.

### Cartographer

Christoffel/evaluation complexity is a distinct axis from treewidth, influence and margin. This removes an ambiguity in the original peelability profile.

### Experimentalist

The finite laboratory can measure the proposed factor exactly and can construct its sharp extremizers, making T8 unusually easy to falsify at small scale.

### Adversary

The needle residual is the principal mandatory negative control. Any proposed certificate that reports small uniform uncertainty after seeing no needle but without paying its appropriate complexity penalty is unsound.

### Formalist

T8.1 is standard and essentially complete. The noiseless bounded T8.2 skeleton is derivable from a standard one-sided Bernstein inequality. The sub-Gaussian noisy form is not yet admitted as derived.

### Steward

Alternative B is worth continuing because it produces a measurable benefit condition `C_t/Gamma_t^2`, not an unconditional efficiency claim. It should be terminated if empirical peeling does not reduce this ratio on target classes.

### Referee

**UNRESOLVED.** No author-side finding in this note substitutes for independent exact-revision review.

## 16. Current disposition

The strongest current T8 candidate is:

`CHRISTOFFEL_AMPLIFIED_HOLDOUT_CERTIFICATE__NOISELESS_CORE_DERIVED__NOISY_EXTENSION_OPEN__NOVELTY_UNASSESSED`

This is not theorem certification.

The key conceptual advance is that ASP no longer needs to choose between:

1. unsafe `L2` learning; and
2. complete global `L_infinity` reconstruction.

There is an intermediate certified regime:

\[
\boxed{
\text{independent residual-energy evidence}
\times
\text{exact residual-space evaluation complexity}
\to
\text{uniform error certificate}.
}
\]

Its worst-case dimension factor is unavoidable, but adaptive peeling can reduce that factor before certification is attempted. Whether it does so fast enough is now an executable research question rather than an unstated hope.
