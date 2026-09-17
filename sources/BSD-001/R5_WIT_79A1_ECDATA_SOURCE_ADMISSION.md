# BSD-001 R5-WIT source admission — pinned ecdata record for 79a1

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#232`.
- Downstream theorem operation: `grandchallenge/MATHSOLVE#282` (`BSD-R5-WIT`).
- Reconciled protected provider base: `grandchallenge/MATHFORGE@2a112e28026d33062ea314c55e69c157bf9ae863`.
- Original source candidate: `a04b7359540b48480a42748849144d77c1df5156`, authored from entering provider `cd814844128167d0e4cdb48f69f9d01c6c0be883`.
- External data repository: `JohnCremona/ecdata`.
- Exact external commit: `25cec5ecfec8b9f016eb1631ac633194c2bed39f`.
- Claim class: exact external data admission only; no local-torsion or BSD theorem is imported.

## Exact admitted records

At the pinned external commit, `docs/curves.1-1000.html` records the conductor-79 curve `79 A 1` with minimal model

`[1,1,1,-2,0]`,

rank `1`, and rational torsion order `1`.

At the same pinned commit, `allbsd/bsd.1-1000` records the rank-one row for `79 A 1`. The pinned `docs/index.html` format documentation identifies the compact columns as conductor, class id, rank, real period, `L^(r)(1)/r!`, regulator, rational factor, and analytic Sha.

Downstream use of this row is limited to the rank-one campaign qualification already used in BSD-001 reconnaissance. No approximate period, L-value, regulator, rational factor, or analytic-Sha field is used as arithmetic evidence.

## Permitted downstream deductions

MATHSOLVE may use the admitted external bytes only as fixed input data:

- conductor `N=79`;
- model `[1,1,1,-2,0]`;
- rank-one record;
- rational torsion order `1`.

The following are **not** admitted as external conclusions and must be independently proved/recomputed downstream:

- squarefree-conductor semistability;
- good ordinary reduction at `2` and `a_2`;
- irreducibility of `E[2]`;
- any local `Q_2` torsion statement;
- `#E(Q_2)[2^infinity]` or `t_2`;
- any Kurihara/Kato nonvanishing statement;
- R5-RES, R5-PRIM, D2d or BSD-R2-A1.

## Source disposition

`R5_WIT_79A1_ECDATA_INPUT_ADMITTED`.

This admission is deliberately narrower than a theorem audit. Its purpose is to make the exact selected-instance input independently reproducible while leaving all mathematical work to MATHSOLVE.

## Claim firewall

This record is not a proof of BSD, local torsion, residual Kato/Kolyvagin nonvanishing, R5-RES, R5-PRIM, novelty, priority, public certification or MATHCERT certification.
