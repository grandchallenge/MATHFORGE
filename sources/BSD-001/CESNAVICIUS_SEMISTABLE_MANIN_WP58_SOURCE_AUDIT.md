# BSD-001 source audit — semistable optimal Manin constant for WP58

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP58A-MODULAR-DIFFERENTIAL-2UNIT`.
- Protected MATHFORGE predecessor: `ed91d13e13ec3577493548466b1411fc70b2693d`.
- Protected MATHSOLVE anchor at preflight: `ae694de9c18c6c2ff3e46002bc8ed008f7b4fb01`; WP57A candidate `dc5431b048cf867e4b8528b168d573cde07e527b` is a separate downstream gate.
- Primary source: Kęstutis Česnavičius, *The Manin constant in the semistable case*, Compositio Mathematica 154 (2018), 1889–1920; arXiv:1703.02951.
- Exact source loci: Introduction, Conjecture 1.1 and Theorem 1.2; notation §1.5; semistable proof in §2.
- Disposition: `QUALIFIED_EXACT_SEMISTABLE_OPTIMAL_MANIN_CONSTANT`.
- Claim class: source/normalization admission only; no BSD or MATHCERT promotion.

## Exact source setup

Let

`pi : J_0(N) -> E_0`

be the new elliptic optimal quotient attached to a normalized weight-two newform `f` of conductor `N`. Let `omega_0` be a Néron differential on `E_0`. The source defines the Manin constant `c_pi` by

`pi^*(omega_0) = c_pi * f`

when the normalized newform is identified with its differential on the modular Jacobian. Equivalently on the modular curve, after the standard `q=e^{2*pi*i*z}` identification,

`phi_0^*(omega_0) = +/- c_pi * 2*pi*i*f(z) dz`

for the induced optimal modular parametrization `phi_0:X_0(N)->E_0`.

The source's Conjecture 1.1 is that for a new elliptic optimal quotient the two integral differential lattices agree. Theorem 1.2 proves this in particular when `E_0` is semistable, equivalently when its conductor `N` is squarefree. The theorem is uniform in the prime `p`; its conclusion includes the prime `2`.

Therefore, for semistable `E_0/Q`,

`c_pi = +/-1`.

After choosing the positive scalar convention used in the BSD-001 CST ledger, the optimal modular-parametrization scalar is exactly

`C_opt = 1`.

This is an exact integral statement, not a statement only after inverting `2` and not an unspecified-unit comparison.

## Match to the protected BSD lane

The protected `BSD-R2-A1` selected class is semistable, so its conductor `N` is squarefree. Every curve in its `Q`-isogeny class has the same conductor and is semistable. Hence the strong-Weil/optimal quotient `E_0` in the selected isogeny class satisfies the source hypotheses.

The admitted source interface is therefore:

> For the optimal curve `E_0` in the protected selected isogeny class, there exists an optimal modular parametrization `phi_0:X_0(N)->E_0` with
>
> `phi_0^*(omega_0)=+/- 2*pi*i*f(z)dz`
>
> for a Néron differential `omega_0` and the normalized newform `f` attached to the isogeny class.

No odd-prime restriction remains in this interface.

## Downstream isogeny transport is not a source claim

Protected MATHSOLVE may combine this interface with its own selected residual hypothesis and elementary isogeny algebra.

If

`psi:E_0 -> E`

is a `Q`-isogeny from the optimal curve to the selected curve and

`psi^*(omega_E)=a_psi omega_0`

for Néron differentials, then `a_psi` is a nonzero integer. If `hat psi` is the dual isogeny and

`hat psi^*(omega_0)=b_psi omega_E`,

then

`a_psi b_psi = deg(psi)`

because `hat psi o psi=[deg psi]` and multiplication by `n` pulls an invariant differential back by `n`.

The source audit does not itself assert that `deg(psi)` is odd. The intended downstream WP58A proof may establish oddness using the already-protected globally irreducible/surjective `E[2]` representation and a minimal-degree isogeny argument. If that argument is valid, then `a_psi` is odd and the composite parametrization

`phi = psi o phi_0 : X_0(N) -> E`

has CST differential scalar

`C_phi = |a_psi|`

with

`ord_2(C_phi)=0`.

The distinction matters: the source proves `C_opt=1`; MATHSOLVE must prove the selected-curve `2`-unit conclusion.

## Exact downstream interface admitted after protection

MATHSOLVE may use only the following source statement from this audit:

For a semistable elliptic curve `E_0/Q` that is the new elliptic optimal quotient of `J_0(N)`, the Manin constant of the optimal `X_0(N)` parametrization is exactly `+/-1`; in the positive scalar convention, `C_opt=1`. This statement includes the prime `2`.

## Boundaries retained

This audit does not prove or assume:

- that the selected curve `E` itself is optimal;
- that every modular parametrization of `E` has Manin scalar one;
- that every isogeny in the selected isogeny class has odd degree;
- that the selected composite scalar `C_f` equals one;
- Heegner primitivity or oddness of `m_K(f)`;
- any value or `2`-adic unit property of `lambda_D=L(E^D,1)/Omega(E^D)`;
- rank-zero BSD for the twist;
- fixed-`2` p-adic-height nondegeneracy;
- a height-one `(2)` analytic determinant generator;
- the final WP06 normalization descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

## Source-access note

The arXiv text of arXiv:1703.02951 was inspected at the exact theorem and notation loci. The published Compositio record identifies the same result: the Manin conjecture is proved for semistable elliptic curves. The theorem explicitly treats a prime `p` and states the semistable Manin conclusion without excluding `p=2`; the paper highlights that the semistable result is uniform for all primes.

## Provider disposition

`QUALIFIED_EXACT_SEMISTABLE_OPTIMAL_MANIN_CONSTANT`

The source is admitted only for the exact optimal semistable Manin constant. Transport from the optimal curve to the selected nonoptimal curve, including any `2`-unit conclusion for the selected `C_f`, remains a downstream MATHSOLVE theorem obligation.
