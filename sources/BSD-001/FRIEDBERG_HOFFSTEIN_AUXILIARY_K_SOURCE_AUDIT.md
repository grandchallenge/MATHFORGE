# BSD-001 source audit — prescribed-local quadratic-twist nonvanishing

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#132`.
- Screen date: `2026-09-08`.
- Disposition: `QUALIFIED_AUXILIARY_K_NONVANISHING_SOURCE`.
- Claim class: source/provider evidence only; no theorem promotion or certification.

## Primary result family

Solomon Friedberg and Jeffrey Hoffstein, *Nonvanishing theorems for automorphic L-functions on GL(2)*, Annals of Mathematics (2) 142 (1995), no. 2, 385–423.

- DOI: `10.2307/2118638`.
- The primary bibliographic identity is independently corroborated by the Annals/JSTOR issue record and the authors' publication lists.
- The current execution environment did not yield an independently inspectable byte-level copy of the full primary theorem text. Consequently this record does not claim a PDF SHA-256 or quote Theorem B from reconstructed memory.
- The bounded theorem semantics below are triangulated from multiple published applications that explicitly invoke Friedberg–Hoffstein Theorem B or Theorem B(2).

## Published applications fixing the theorem interface

### Ono–Skinner

Ken Ono and Christopher Skinner, *Non-vanishing of quadratic twists of modular L-functions*, Inventiones mathematicae 134 (1998), 651–660.

The paper fixes an arbitrary finite set of distinct primes `p_i` and arbitrary signs `epsilon_i in {+1,-1}`, and studies fundamental discriminants `D` satisfying

`chi_D(p_i) = epsilon_i`

for every prescribed prime. It explicitly invokes Friedberg–Hoffstein in this prescribed-local-sign setting to obtain nonvanishing quadratic twists. This establishes that the Friedberg–Hoffstein input is not restricted to an unconstrained family of discriminants.

### Jetchev–Skinner–Wan

Dimitar Jetchev, Christopher Skinner, and Xin Wan, *The Birch and Swinnerton-Dyer formula for elliptic curves of analytic rank one* (rank-one BSD paper).

In their auxiliary-quadratic-field construction they impose finitely many splitting/inertness conditions on an imaginary quadratic field `K'=Q(sqrt(D'))`, including splitting at the chosen ordinary prime, verify that the corresponding twist root number is `+1`, and then invoke Friedberg–Hoffstein Theorem B to choose `K'` with

`L(E^{D'},1) != 0`.

They explicitly note that the local requirements impose only finitely many congruence conditions on the discriminant. This is the closest published use to the present campaign interface.

### Ciperiani-type applications

Published applications citing Friedberg–Hoffstein Theorem B(2) choose negative integers `d` with specified congruence/local behavior, require primes dividing an elliptic-curve conductor to split in the resulting imaginary quadratic field, and simultaneously prescribe analytic rank zero or one of the quadratic twist. These applications corroborate that the theorem interface includes the archimedean sign together with finite local behavior, subject to the global sign compatibility condition.

## Qualified theorem interface

The source family supports the following bounded provider proposition.

Let `E/Q` be modular. Fix a finite compatible packet of local quadratic-character conditions, including an archimedean sign if desired, and suppose the packet lies in the root-number `+1` family for the quadratic twists of `E`. Then Friedberg–Hoffstein supplies quadratic characters/discriminants in that prescribed local packet for which the central twist value is nonzero.

For the selected BSD auxiliary-Heegner lane this can be applied to a packet requiring:

1. `D < 0`, so `K=Q(sqrt(D))` is imaginary quadratic;
2. `D` fundamental and coprime to `2N`;
3. `2` split in `K`;
4. every `ell | N` split in `K` for the classical all-split Heegner packet;
5. therefore the twist lies in the sign `+1` family.

The finite local packet is nonempty: the sign/splitting requirements are finitely many quadratic congruence conditions, and standard Dirichlet/Chebotarev existence supplies negative fundamental discriminants satisfying them before imposing L-value nonvanishing.

For an elliptic curve of exact analytic rank one, the functional equation gives

`w(E/Q) = -1`.

For the classical imaginary quadratic Heegner packet in which every prime dividing the conductor splits, the base-change sign is

`w(E/K) = -1`.

Using

`L(E/K,s) = L(E,s) L(E^D,s)`

and

`w(E/K) = w(E/Q) w(E^D/Q)`, 

we obtain

`w(E^D/Q)=+1`.

The qualified Friedberg–Hoffstein interface therefore permits selection of such a `D` with

`L(E^D,1) != 0`.

It follows formally that

`ord_{s=1} L(E/K,s) = ord_{s=1} L(E,s) + ord_{s=1} L(E^D,s) = 1`.

Thus the auxiliary-field existence and analytic-rank-one base-change requirements can be simultaneously met in the classical all-split lane.

## Exact downstream use that is supportable

This source may be used downstream to discharge the **auxiliary imaginary quadratic field existence/nonvanishing** sub-obligation for `BSD-R2-A1-2MU-RECIPROCITY`, provided the Solve package explicitly fixes a compatible local packet and verifies its sign computation.

The source does not select a unique discriminant. Existence is sufficient for the theorem interface.

## Remaining unsupported steps

This record does **not** establish:

- applicability of the corrected Disegni p-adic Gross–Zagier formula to the selected automorphic representation by itself;
- any integral p=2 main conjecture;
- equality of algebraic and analytic cyclotomic mu invariants;
- the height-one `(2)` component identified in BSD WP08;
- equality of a p-adic height with the WP00 Neron–Tate regulator;
- conversion of a p-adic L-derivative into the WP00-normalized complex derivative without all interpolation factors;
- exact 2-primary Heegner/Kolyvagin index or Tamagawa correction formulas;
- `BSD-R2-A1`;
- mathematical certification, novelty, or priority.

## Provenance limitation

The provider screen directly verified the primary bibliographic identity and inspected published papers that explicitly apply Friedberg–Hoffstein Theorem B/B(2) in the required prescribed-local setting. The full primary theorem bytes were not independently acquired in this runtime. This is a source-provenance limitation, not a license to strengthen the qualified theorem interface beyond the published applications recorded above.

## Provider disposition

`QUALIFIED_AUXILIARY_K_NONVANISHING_SOURCE`

Downstream use is limited to existence of an auxiliary quadratic field with the stated compatible local behavior and nonvanishing central twist. No stronger BSD, p=2 Iwasawa, reciprocity, or certification claim is imported.