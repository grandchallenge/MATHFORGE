# BSD-001 R5-WIT source audit — Q2 good-ordinary local torsion

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#234`.
- Downstream theorem operation: `grandchallenge/MATHSOLVE#282`.
- Protected entering MATHFORGE: `cd814844128167d0e4cdb48f69f9d01c6c0be883`.
- Downstream protected R5-RECIP completion anchor: `grandchallenge/MATHSOLVE@9c9bd9077f8b269277366c7ee81dcdcd7f701217`.
- Claim class: bounded source interface only.

## Primary source

Yoshiyasu Ozeki and Manabu Yoshida, *Torsion of elliptic curves over Q_p with good reduction in cyclotomic extensions*, arXiv:2510.13172v2, dated 4 April 2026. The relevant statements are Theorem 1.1(2) and §2.2.1.

The source is a 2026 preprint. This audit admits only the precise classification statement below; it does not elevate the source to certification authority and does not import unrelated cyclotomic-extension claims.

## Admitted local classification

For an elliptic curve `E/Q_2` with good ordinary reduction, Ozeki–Yoshida classify the possible finite torsion groups `E(Q_2)_tor` as

- `Z/2Z`,
- `Z/4Z`,
- `Z/8Z`,
- `Z/2Z x Z/2Z`,
- `Z/2Z x Z/4Z`.

In particular, the `2`-primary torsion has order at most `8`, so if

`2^t_2 = #E(Q_2)[2^infinity]`,

then on a good-ordinary literal-`2` lane

`1 <= t_2 <= 3`

whenever the downstream theorem has independently established the existence of nontrivial local `2`-power torsion.

The source proof also uses the good-reduction exact sequence and the fact that for ordinary reduction at `2` the formal-group torsion has order at most `2`; the downstream R5-RECIP theorem independently proves the selected shallow formal `2`-torsion phenomenon and must remain the authority for that selected-lane fact.

## What this source does not determine

The classification is not a criterion selecting one of the five groups for an arbitrary global curve. It therefore does **not** determine the selected BSD-001 value of `t_2` by itself.

In particular, this audit does not authorize any inference that the BSD-001 hard filter (semistable, odd conductor, good ordinary at `2`, irreducible `E[2]`, analytic rank one) forces `t_2=1`. The source explicitly permits good-ordinary local groups with `2`-primary order `4` and `8`.

A downstream selected-curve or selected-class computation must still determine whether there is:

1. a second `Q_2`-rational point of order `2` outside the formal kernel;
2. a `Q_2`-rational half of the selected formal order-`2` point;
3. if order `4` occurs, a further rational half producing order `8`.

These questions can be tested by exact local division-polynomial / duplication equations, but this audit does not promote any particular computational implementation.

## Downstream consequence for R5-WIT

Protected R5-RECIP proves that the normalized Kurihara witness satisfies

`Delta_n^(2) = 2^t_2 * delta_tilde_n`

and that `t_2>=2` forces `Delta_n^(2)=0 mod 2` for every admitted finite derivative level. The present source therefore validates the need to stratify the selected lane by the exact local torsion exponent rather than assuming the direct witness route is uniformly available.

The only admitted source-level conclusion is:

`GOOD_ORDINARY_Q2_LOCAL_2PRIMARY_TORSION_ORDER_AT_MOST_8_WITH_FIVE_POSSIBLE_GROUP_STRUCTURES`.

## Claim firewall

This audit does not establish:

- the exact selected-lane value of `t_2`;
- a finite normalized Kurihara nonvanishing witness;
- residual Kato/Kolyvagin nonvanishing;
- `R5-RES` or `R5-PRIM`;
- `D2d` or `BSD-R2-A1`;
- novelty, priority, public certification, or MATHCERT certification.
