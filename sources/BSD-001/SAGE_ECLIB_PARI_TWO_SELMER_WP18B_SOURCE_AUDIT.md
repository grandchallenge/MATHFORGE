# BSD-001 — Sage/PARI/eclib 2-Selmer computation interface audit

## Disposition

`QUALIFIED_WP18B_TWO_SELMER_COMPUTATION_INTERFACE`

This record qualifies a narrow computational interface for the diagnostic WP18B finite-level atlas. It does not certify BSD, analytic Sha, higher `2^n`-Selmer groups, or any mathematical claim outside the explicit 2-Selmer computation below.

## Downstream question

For the protected WP18A curves `53a1` and `203b1`, compute independently of BSD the dimension over `F_2` of

`Sel_2(E/Q)`

and therefore its order. Both protected controls have no rational 2-torsion.

## Primary software documentation

SageMath 10.8 documentation exposes

`EllipticCurve(...).selmer_rank(algorithm='pari')`

and states that it returns the rank of the 2-Selmer group. The same public interface accepts `algorithm='mwrank'` as the alternate implementation.

Reference:

- SageMath 10.8 elliptic-curve reference, `selmer_rank(algorithm='pari')`:
  `https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html`

Sage's eclib interface separately documents

`mwrank_EllipticCurve(...).selmer_rank()`

as returning the 2-Selmer rank, and explains that for curves without rational 2-torsion the mwrank rank upper bound is the 2-Selmer rank.

Reference:

- SageMath/eclib interface:
  `https://doc.sagemath.org/html/en/reference/libs/sage/libs/eclib/interface.html`

The eclib/mwrank interface is the Sage binding to John Cremona's eclib two-descent implementation. The PARI route is a separate Sage-exposed implementation path. Agreement between these paths is required by the WP18B computation contract.

## Runtime pin

The computation lane is to use the official SageMath Docker image tag

`sagemath/sagemath:10.8`.

The official Docker registry currently exposes this release tag. The run must record `sage --version` and the exact GitHub Actions run/job identity. The tag is a runtime selector, not an immutable content digest; the retained version output and raw run evidence are therefore mandatory.

Reference:

- official SageMath Docker tags:
  `https://hub.docker.com/r/sagemath/sagemath/tags`

## Exact interpretation admitted

For an elliptic curve over `Q`, the return value

`r_2 := E.selmer_rank(...)`

is admitted as the software-computed `F_2`-dimension of `Sel_2(E/Q)`.

Therefore

`#Sel_2(E/Q) = 2^r_2`.

For the WP18A controls, protected odd rational torsion gives `E(Q)[2]=0`. No additional torsion correction is needed when translating the returned Selmer dimension into the group order.

WP16A then defines, at `n=1`,

`s_1(E) = ord_2 #Sel_2(E/Q) - 1 = r_2 - 1`.

This last equality is an elementary downstream derivation from the protected definition plus the computation; it is not a software claim.

## Mandatory execution checks

A governed WP18B-1 result must:

1. instantiate each curve by its protected minimal `a`-invariants, not by a mutable online database lookup;
2. run `selmer_rank(algorithm='pari')`;
3. run `selmer_rank(algorithm='mwrank')`;
4. additionally record the direct eclib `mwrank_EllipticCurve(...).selmer_rank()` result when available;
5. require exact agreement of all successful routes;
6. record Sage version, exact curve invariants, returned ranks, and process exit status;
7. retain raw machine output before interpretation.

Any disagreement, exception, heuristic/probabilistic-only completion, or missing implementation route is a failed evidence run and must not be silently resolved by analytic Sha or BSD data.

## Explicit exclusions

This audit does **not** qualify:

- `Sha(E/Q)[2]` inferred from analytic BSD data;
- `Sel_4`, `Sel_8`, or any higher `2^n`-Selmer computation;
- FourDescent/EightDescent interfaces;
- Cassels-Tate pairing computation;
- p-adic L-function values;
- numerical `delta_2(E)`;
- any claim of eventual stabilization from the `n=1` result.

A higher 2-power computation requires its own exact interface audit or a protected derivation reducing it to already-qualified evidence.

## Claim boundary

The admitted conclusion is only:

> A successful pinned SageMath 10.8 run, with exact agreement between the documented PARI and mwrank/eclib 2-Selmer interfaces on the protected curve model, is qualified as reproducible diagnostic evidence for the computed dimension and order of `Sel_2(E/Q)` in WP18B.

This is not MATHCERT certification and does not promote `BSD-R2-A1`.
