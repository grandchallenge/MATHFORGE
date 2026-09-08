# BSD-001 source audit — corrected Disegni p-adic Gross–Zagier interface

## Record

- Campaign: `BSD-001`.
- Provider operation: `MATHFORGE#130`.
- Screen date: `2026-09-08`.
- Disposition: `QUALIFIED_RECIPROCITY_SOURCE`.
- Claim class: source/provider evidence only; no theorem promotion or certification.

## Primary article

Daniel Disegni, *The universal p-adic Gross–Zagier formula*, Inventiones mathematicae 230 (2022), 509–649.

- DOI: `10.1007/s00222-022-01133-w`.
- Public author PDF inspected: `https://disegni-daniel.perso.math.cnrs.fr/univ.pdf`.
- The paper states in its setup: “Fix throughout the rest of this paper a rational prime p.”
- The current source screen located no global hypothesis `p>2` or “p odd” in the theorem setup.
- Theorem B states a p-adic Gross–Zagier identity for an ordinary, locally distinguished, non-exceptional automorphic representation, relating a p-adic height of Heegner classes to the derivative of a p-adic L-function times explicit interpolation/test-vector factors.
- In the paper, “locally distinguished” is an automorphic/toric distinction condition. It is not the residual ordinary condition that the two diagonal residual characters be distinct.

## Published correction

Daniel Disegni, *Correction to: The universal p-adic Gross–Zagier formula*, Inventiones mathematicae 243 (2026), 243–244.

- DOI: `10.1007/s00222-025-01391-4`.
- Publisher preview inspected through the published correction record.
- The correction defines `S_{p,ns}` to be the p-adic places of the totally real field that are nonsplit in the CM quadratic extension.
- Condition `(star)`: for every `v` in `S_{p,ns}`, `v` is inert and the local Hecke character is unramified.
- After the correction, Theorem B is established only for ordinary, locally distinguished, potentially crystalline, non-exceptional representations of trivial weight satisfying `(star)`.
- The correction states that Theorem B and Theorem B^ord of Section 7.1.1 require `(star)`.

## Consequences for the selected BSD auxiliary-quadratic lane

The selected campaign has good ordinary reduction at `2`.

1. Good reduction gives a crystalline 2-adic representation, so the potentially crystalline requirement is compatible with the selected local reduction type.
2. If the auxiliary imaginary quadratic field `K/Q` is chosen so that `2` splits, there is no nonsplit place above `2`; hence the correction's condition `(star)` imposes no 2-adic condition at that split place.
3. The source's “locally distinguished” condition does not conflict with WP07's theorem that standard residual ordinary 2-distinguishedness is impossible. They are different notions.
4. For good reduction the local automorphic representation at `2` is not the special/Steinberg case appearing in the source's characterization of exceptional representations. This is concordant with non-exceptionality, but exact downstream application must still bind the chosen automorphic representation and local character to the source's conventions.

## Exact downstream use that is supportable

Subject to exact verification of the auxiliary representation, local distinction, trivial-weight convention, non-exceptionality, Hecke character, test vectors, and normalizations, this source is a candidate interface for

`p-adic height of a Heegner class  <->  derivative of a p-adic L-function`

at the selected prime `p=2`.

This is a material reduction of the BSD reciprocity search. It does not supply the complete selected BSD leading-term identity.

## Remaining unsupported steps

This source record does **not** establish any of the following:

- existence of a single auxiliary imaginary quadratic field satisfying every campaign splitting, Heegner-sign, and analytic-rank requirement;
- the WP08 height-one `(2)` / relative-mu component of a cyclotomic main conjecture;
- an integral equality between a characteristic/Fitting element and the analytic p-adic L-function at the prime `(2)`;
- identification of the source's p-adic height with the WP00 Néron–Tate regulator;
- the exact conversion from the p-adic L-function derivative to the WP00-normalized complex derivative `L'(E,1)`;
- the complete Tamagawa, period, Manin, isogeny, Euler, interpolation, and local-index correction ledger;
- an exact 2-primary Kolyvagin/Heegner index formula for the selected class;
- `BSD-R2-A1`;
- mathematical certification.

## Source-lock limitation

The public PDF was inspected through the web source surface, but an independent byte download through the current execution environment did not complete. This record therefore locks the bibliographic identities, DOI identities, public PDF location, theorem locators, and corrected hypothesis surface; it does not claim an independently recomputed SHA-256 of the publisher or author PDF bytes.

A later byte-level source lock may strengthen provenance without changing the theorem-hypothesis disposition recorded here.

## Provider disposition

`QUALIFIED_RECIPROCITY_SOURCE`

The source may be used downstream only for the bounded p-adic Gross–Zagier interface after an exact applicability check. It may not be cited as a proof of the complex BSD valuation, a p=2 main conjecture, mu equality, or MATHCERT certification.
