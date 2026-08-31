# ASP-T8-NOISE-002 — Sub-Gaussian residual-energy certification

**Issue:** grandchallenge/MATHFORGE#115  
**Parent finite harness:** ASP-WP01 / PR #112 exact head `d3f7490a8e28c9a8e426856657506e679d42af4f`  
**Status:** theory candidate + finite confrontation specification; no theorem promotion  

## 1. Objective

Extend the T8 holdout certificate from bounded/noiseless residual observations to conditionally centered sub-Gaussian oracle noise without subtracting an unknown noise variance.

Let `V` be a `C`-dimensional subspace of `L2(mu)` with orthonormal basis `phi_1,...,phi_C` and reproducing kernel

\[
K(x,x')=\sum_{j=1}^C \phi_j(x)\phi_j(x').
\]

Write

\[
\Lambda=\sup_x K(x,x).
\]

For complete finite product-space degree classes used by ASP, `K(x,x)` is constant and `Lambda=C`.

A surrogate `g` is fixed independently of validation data and

\[
r=f-g\in V,\qquad |r(x)|\le R.
\]

Validation observations are

\[
Y_i=f(X_i)+\xi_i,\qquad X_i\stackrel{iid}{\sim}\mu,
\]

where conditionally on `X_i`, `E[xi_i|X_i]=0` and

\[
E[\exp(t\xi_i)\mid X_i]\le \exp(\sigma^2t^2/2)
\]

for every real `t`. Observations are independent across `i`.

Define

\[
Z_i=Y_i-g(X_i)=r(X_i)+\xi_i.
\]

## 2. Why ordinary squared holdout is inadequate

The naive statistic `m^{-1} sum Z_i^2` estimates

\[
\|r\|_2^2+E\xi^2,
\]

not `||r||_2^2`. Subtracting `sigma^2` is invalid because `sigma^2` is only a sub-Gaussian proxy and need not equal the noise variance. T8 therefore needs an estimator whose expectation removes the noise automatically.

Products of sub-Gaussian variables are sub-exponential, so quadratic residual statistics naturally leave the bounded/Bernstein regime of the noiseless note; this is standard concentration theory, not an ASP novelty claim.

## 3. T8.4 candidate — kernel U-statistic

Define

\[
\boxed{
U_m=
\frac{1}{m(m-1)}
\sum_{i\ne j} Z_i Z_j K(X_i,X_j).
}
\]

Equivalently this is the ordinary symmetric order-two U-statistic with kernel

\[
h(W_i,W_j)=Z_iZ_jK(X_i,X_j),
\]

where `W_i=(X_i,Z_i)`.

### Proposition 1 — unbiased residual energy

\[
\boxed{E U_m=\|r\|_2^2=:\mu.}
\]

**Proof.** For distinct observations, conditional centering gives

\[
E[Z_iZ_jK(X_i,X_j)\mid X_i,X_j]
=r(X_i)r(X_j)K(X_i,X_j).
\]

Since `r in V`, the reproducing identity gives

\[
E_{X_j}[r(X_j)K(X_i,X_j)]=r(X_i).
\]

A second expectation yields `E r(X_i)^2=||r||_2^2`. No noise variance is used. ∎

## 4. Exact Hoeffding decomposition

Let

\[
\mu=E h(W,W').
\]

The first projection is

\[
\begin{aligned}
h_1(W)
&=E[h(W,W')\mid W]-\mu\\
&=Zr(X)-\mu\\
&=r(X)^2-\mu+r(X)\xi.
\end{aligned}
\]

The canonical second-order component is

\[
\boxed{
h_2(W,W')=
ZZ'K(X,X')-Zr(X)-Z'r(X')+\mu.
}
\]

It satisfies

\[
E[h_2(W,W')\mid W]=0.
\]

Hence

\[
\boxed{
U_m-\mu
=
\frac{2}{m}\sum_{i=1}^m h_1(W_i)
+
\frac{2}{m(m-1)}\sum_{i<j} h_2(W_i,W_j).
}
\]

This decomposition is the central noisy T8 object. The first term is signal-adaptive; the second is a degenerate quadratic-noise term that remains even when the surrogate is exact.

## 5. Variance structure

Because `|r|<=R` and `Var(xi|X)<=sigma^2`,

\[
\boxed{
Var(h_1)\le (R^2+\sigma^2)\mu.
}
\]

Indeed, `Var(r^2)<=E r^4<=R^2 mu`, the cross term vanishes by conditional centering, and `E[r^2 xi^2]<=sigma^2 mu`.

For the full kernel,

\[
E[h(W,W')^2]
=E[(r(X)^2+v(X))(r(X')^2+v(X'))K(X,X')^2],
\]

where `v(X)=E[xi^2|X]<=sigma^2`.

Projection-kernel identities imply

\[
E_{X'}K(X,X')^2=K(X,X)\le\Lambda,
\]

and

\[
E K(X,X')^2=C.
\]

Therefore

\[
\boxed{
E h^2
\le
\sigma^4 C+(2\sigma^2+R^2)\Lambda\mu.
}
\]

Orthogonality of the Hoeffding components gives `Var(h_2)<=Var(h)<=E h^2`. Thus the standard order-two U-statistic variance formula yields

\[
\boxed{
Var(U_m)
\le
\frac{4(R^2+\sigma^2)\mu}{m}
+
\frac{2\{\sigma^4C+(2\sigma^2+R^2)\Lambda\mu\}}
{m(m-1)}.
}
\]

### Exact null variance

If `r=0` and the noise is homoscedastic with variance `nu^2`, then `h_1=0` and

\[
\boxed{
Var(U_m)=\frac{2\nu^4 C}{m(m-1)}.
}
\]

Hence the exact-surrogate noise floor is

\[
SD(U_m)\asymp \frac{\nu^2\sqrt C}{m}.
\]

This already falsifies a universal noisy `C/Gamma^2` law for this energy-certificate route unless noise is asymptotically negligible.

## 6. High-confidence certificate without delicate U-statistic tail constants

Direct canonical U-statistic exponential inequalities are available in the literature (Giné–Latała–Zinn; Houdré–Reynaud-Bouret). For the first governed implementation we use a simpler route whose constants are explicit and which needs only the variance bound above: **median of independent block U-statistics**.

Split the validation sample into `B` independent blocks of equal size `q>=2`. In block `b`, compute `U_q^(b)`. Let

\[
M=\operatorname{median}_b U_q^{(b)}.
\]

For one block, define

\[
A_q
=
4(R^2+\sigma^2)
+
\frac{4(2\sigma^2+R^2)\Lambda}{q},
\]

and

\[
D=4\sigma^4C.
\]

Using `1/[q(q-1)]<=2/q^2`,

\[
Var(U_q)\le \frac{A_q\mu}{q}+\frac{D}{q^2}.
\]

Chebyshev gives

\[
P\left(
|U_q-\mu|>
2\sqrt{A_q\mu/q+D/q^2}
\right)\le1/4.
\]

If `B` is odd, a Hoeffding bound on the number of bad blocks gives

\[
P(\text{median block is bad})\le e^{-B/8}.
\]

Thus `B>=8 log(1/delta)` is sufficient for confidence at least `1-delta`.

On that event,

\[
\mu
\le M+2\sqrt{A_q\mu/q+D/q^2}.
\]

Using `sqrt(a+b)<=sqrt(a)+sqrt(b)` and

\[
2\sqrt{A_q\mu/q}\le\mu/2+2A_q/q,
\]

we obtain the explicit upper confidence bound

\[
\boxed{
\mu
\le
U_2^{noise}
:=
2M_+
+
\frac{4A_q}{q}
+
\frac{4\sqrt D}{q},
}
\]

where `M_+=max(M,0)`.

Since `sqrt(D)=2 sigma^2 sqrt(C)`,

\[
\boxed{
U_2^{noise}
=
2M_+
+
\frac{16(R^2+\sigma^2)}{q}
+
\frac{16(2\sigma^2+R^2)\Lambda}{q^2}
+
\frac{8\sigma^2\sqrt C}{q}.
}
\]

This bound is intentionally conservative but fully explicit, variance-adaptive in the proof, and does not require known noise variance.

## 7. Uniform residual certificate

T8.1 gives

\[
\|r\|_\infty\le\sqrt{\Lambda\mu}.
\]

Therefore with probability at least `1-delta`,

\[
\boxed{
\|f-g\|_\infty
\le
\epsilon_{noise}
:=
\sqrt{\Lambda U_2^{noise}}.
}
\]

This can be inserted into T6 unchanged. If an observed surrogate branch-minimum gap exceeds `2 epsilon_noise`, that inferior branch may be pruned safely on the certificate event.

For automatic certification from a true branch margin `Gamma`, the conservative sufficient target remains

\[
\epsilon_{noise}<\Gamma/4.
\]

Equivalently,

\[
U_2^{noise}<\frac{\Gamma^2}{16\Lambda}.
\]

## 8. Scaling consequence

Ignoring the realized `M_+` term in the near-exact-surrogate regime and lower-order `q^{-2}` terms, the block size sufficient to push the deterministic radius below the T6 energy threshold scales as

\[
q
\gtrsim
\frac{\Lambda(R^2+\sigma^2)}{\Gamma^2}
+
\frac{\sigma^2\Lambda\sqrt C}{\Gamma^2}.
\]

For the complete ASP degree classes, `Lambda=C`, so

\[
\boxed{
q
\gtrsim
\frac{R^2C}{\Gamma^2}
+
\frac{\sigma^2C^{3/2}}{\Gamma^2}
}
\]

up to universal constants and the `B=O(log(1/delta))` confidence multiplier.

Thus the candidate certification-cost predictor is not a single ratio. It has two regimes:

\[
\boxed{
P_{struct}=\frac{R^2C}{\Gamma^2},
\qquad
P_{noise}=\frac{\sigma^2C^{3/2}}{\Gamma^2}.
}
\]

The original

\[
C/\Gamma^2
\]

is recovered in bounded/noiseless or sufficiently low-noise conditions. Under persistent observation noise, an additional `sqrt(C)` penalty appears for this residual-energy route.

## 9. Route-specific lower boundary

At `r=0` the exact variance identity

\[
Var(U_m)=2\nu^4C/[m(m-1)]
\]

shows that the `nu^2 sqrt(C)/m` stochastic scale is not an artifact of the median-of-means proof. To make residual-energy uncertainty smaller than

\[
a=\Theta(\Gamma^2/C),
\]

this estimator necessarily needs

\[
m=\Omega(\nu^2C^{3/2}/\Gamma^2)
\]

at constant signal-to-noise confidence.

This is an **estimator/energy-route obstruction**, not yet a universal minimax lower bound over every possible ASP certificate. Quadratic-functional estimation and signal-detection theory indicate that such degenerate-noise effects are standard; any stronger minimax claim requires a separate reduction and independent review.

## 10. Provenance boundary

The ingredients are established mathematics:

- sub-Gaussian and sub-exponential concentration;
- reproducing-kernel / Christoffel norm transfer;
- Hoeffding decomposition and variance formula for U-statistics;
- canonical order-two U-statistic exponential inequalities;
- quadratic-functional estimation/testing theory.

The candidate ASP contribution is the composition

\[
\text{spectral peeling}
\to C_t\downarrow
\to \text{noise-aware residual-energy certificate}
\to \Gamma_t\text{-safe branch pruning}.
\]

No novelty disposition is made here.

## 11. Finite confrontation

The executable successor must independently vary `C`, `Gamma`, `sigma`, residual energy and residual geometry, and compare at least:

\[
P_0=C/\Gamma^2,
\]

\[
P_1=\sigma^2C^{3/2}/\Gamma^2,
\]

and

\[
P_{comb}=(R^2C+\sigma^2C^{3/2})/\Gamma^2.
\]

Primary outcomes:

1. empirical coverage of `U_2^noise`;
2. false T6 pruning rate against exact exhaustive optimum;
3. minimum queries to certify;
4. log-log exponent of certification cost in `C` in low-noise and noise-dominated regimes;
5. whether restrictions reduce realized certification cost in concert with `C_t`.

A result near exponent `3/2` in the noise-dominated regime is a **disconfirmation** of `C/Gamma^2` as a universal noisy predictor, not a failure of ASP.

## 12. Governance disposition

This note is a MATHFORGE candidate under issue #115. Promotion, theorem certification, MATHSOLVE/MATHCERT routing, ASP-001 activation, novelty and publication claims remain closed. Exact-head CI is confrontation evidence only; independent non-author theory review remains required before any theorem promotion.
