# BSD-001 R5-RES source audit — literal-p=2 full-deformation classical density

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#250`.
- Downstream objective: continuing the Colmez–Wang route toward a legitimate residual Kato witness for historical `BSD-R5-RES`.
- Exact MATHSOLVE protected head entering this audit: `grandchallenge/MATHSOLVE@e7c67802acf31012f923eb820e080d9586b45bd6`.
- Exact MATHFORGE protected base: `716979bcae4e67a82c52f15c99b20da555fcdfca`.
- Protected predecessor provider:
  `sources/BSD-001/R5_RES_COLMEZ_WANG_P2_DETERMINANT_VARIABLE_SOURCE_AUDIT.md`.
- Protected downstream half-weight result:
  `BSD-R5-CW-P2-HALF-WEIGHT-005`.
- Entering successor boundary:
  `MISSING_P2_COLMEZ_WANG_SQUARE_ROOT_COVER_CHAPTER15_GLOBALIZATION_COMPATIBILITY`.
- Claim class: bounded source/applicability evidence only.

## 1. Exact question

The protected half-weight theorem removes the first literal-`2` algebraic defect in Colmez–Wang Chapter 15 by replacing the unavailable odd-prime character halving with the finite-flat ramified cover

`Lambda_half ~= Z_2[[S]],  T -> 2S+S^2`.

The remaining Chapter-15 proof uses a Zariski-dense set of classical points at which the local characteristic-zero representation at `p` is absolutely irreducible.  The source question is:

> Is there a source theorem, valid at literal `p=2` and on the protected residual `S_3 ~= GL_2(F_2)` lane, that supplies Zariski density of such locally absolutely irreducible classical modular points on the full global deformation space?

This audit distinguishes:

- local crystalline density from global modular density;
- modularity of one local condition from density in the unrestricted deformation space;
- ordinary/reducible classical points from the locally absolutely irreducible points required by the Colmez–Wang analytic-continuation step;
- nonsolvable residual hypotheses from the protected selected residual image `S_3`, which is solvable.

## 2. Protected selected residual input

Protected MATHSOLVE WP12 proves on the selected BSD lane

`im(bar rho_{E,2}) = GL_2(F_2) ~= S_3`.

This fact matters twice.

First, it excludes any source theorem whose global `p=2` modularity hypothesis requires nonsolvable residual image.

Second, it gives a downstream repair of a different Chapter-15 use of `p != 2`: after restriction to the cyclotomic `Z_2`-extension, the residual image is a normal subgroup of `S_3` with pro-`2` quotient, hence is `S_3` or `A_3`.  The natural two-dimensional `F_2` representation remains irreducible on `A_3=C_3`, because a nontrivial order-three element has irreducible minimal polynomial `X^2+X+1`.

That second statement is a downstream elementary deduction; this provider record does not promote it as a new source theorem.

## 3. Böckle 2001: density theorem is odd-prime

Gebhard Böckle, *On the density of modular points in universal deformation spaces*, Amer. J. Math. 123 (2001), 985–1007.

The paper proves Zariski density of modular points in unrestricted two-dimensional deformation spaces under its stated hypotheses.

However its setup begins by fixing the critical prime `l` to be an **odd prime**.

Therefore the classical Böckle density theorem is not a literal-`2` source interface for this campaign.

Disposition:

`BOECKLE_2001_DENSITY_NOT_ADMITTED_AT_LITERAL_P2`.

## 4. Emerton local-global compatibility: global theorem assumes p>2

Matthew Emerton, *Local-global compatibility in the p-adic Langlands programme for GL_2/Q*.

The relevant global local-global compatibility / Fontaine–Mazur consequences in the source explicitly assume

`p>2`.

For example the theorem describing the mod-`p` multiplicities in completed modular-curve cohomology imposes `p>2`, and the global theorems used in the older unrestricted-deformation density route sit in that same odd-prime architecture.

Thus Emerton's source cannot simply replace Böckle at literal two.

Disposition:

`EMERTON_GLOBAL_DENSITY_ARCHITECTURE_NOT_ADMITTED_AT_LITERAL_P2`.

## 5. Paškūnas: literal-2 modularity, but nonsolvable residual image

Vytautas Paškūnas, *On 2-dimensional 2-adic Galois representations of local and global fields*, arXiv:`1509.00332`.

Theorem 1.1 is genuinely a literal-`p=2` global modularity-lifting theorem.

Its first hypothesis is that the residual representation is modular with **non-solvable image**.

The selected BSD residual image is

`S_3`,

which is solvable.

Therefore this theorem does not supply the required modularity of unrestricted lifts on the selected lane.

Disposition:

`PASKUNAS_P2_GLOBAL_MODULARITY_EXCLUDES_SELECTED_SOLVABLE_S3_RESIDUAL_IMAGE`.

## 6. Tung: important local p=2 repair, but not the missing selected global density theorem

Shen-Ning Tung, *On the modularity of 2-adic potentially semi-stable deformation rings*, arXiv:`1908.06174`.

Tung proves that patched modules meet every irreducible component of the relevant **local** potentially semi-stable deformation ring and removes a local restriction in Paškūnas' Fontaine–Mazur argument.

This is a strong literal-`2` local modularity/deformation result.

It does not remove the separate global residual-image hypothesis that excludes the selected solvable `S_3` branch from the Paškūnas global theorem, and it does not state the full global unrestricted-deformation Zariski-density theorem required here.

Disposition:

`TUNG_P2_LOCAL_COMPONENT_MODULARITY_NOT_GLOBAL_SELECTED_S3_DENSITY`.

## 7. Allen density/automorphic-points results remain odd-prime

Patrick B. Allen, *On automorphic points in polarized deformation rings*, arXiv:`1601.03752`.

The Hilbert modular / two-dimensional section explicitly assumes

`p>2`.

The paper repeatedly uses odd-prime character square roots and odd-prime deformation identifications.  Its unrestricted automorphic-point density result therefore does not directly apply at literal two.

Allen's separate 2014 nearly ordinary residually dihedral theorem is a genuine `p=2` architecture but, as recorded in the predecessor audit, imposes a nearly ordinary/reducible local deformation condition.  It does not furnish the locally absolutely irreducible classical locus required for Colmez–Wang analytic continuation.

Disposition:

`ALLEN_DENSITY_ODD_PRIME_AND_ALLEN_P2_NEARLY_ORDINARY_TOO_NARROW`.

## 8. Thorne 2026: literal-2 advance is ordinary, not the required locus

Jack A. Thorne, *Towards the Fontaine–Mazur conjecture for GL(2)*, arXiv:`2608.07186v1` (7 August 2026).

The new theorem is deliberately prime-uniform: `p` may be two.  It proves potential modularity for irreducible representations satisfying, at every place above `p`, a potentially crystalline **ordinary** condition with Hodge–Tate weights `{0,1}`, together with the stated global hypotheses.

This is materially relevant progress at literal two, including settings not covered by older residual-image hypotheses.

But ordinary two-dimensional local representations are reducible.  Hence this theorem does not construct, let alone prove density of, the locally absolutely irreducible classical points denoted `X_0^{cl,+}` in the Colmez–Wang Chapter-15 continuation argument.

Potential modularity is also weaker than the required statement that modular points are Zariski dense in the specific unrestricted global deformation space over `Q`.

Disposition:

`THORNE_2026_P2_ORDINARY_MODULARITY_NOT_LOCALLY_IRREDUCIBLE_FULL_DEFORMATION_DENSITY`.

## 9. Local crystalline density does not close the global gap

Recent work proves very strong density statements for crystalline/regular points in **local** deformation spaces at `p`, including literal-`2` cases and very general residual representations.

Those results materially support the local geometric plausibility of finding irreducible characteristic-zero lifts.

They do not by themselves prove that those local points globalize to modular points in the specific global unrestricted deformation space through the selected residual representation.

The missing implication is global modularity/globalization, not local abundance.

Accordingly:

`LOCAL_P2_CRYSTALLINE_DENSITY_DOES_NOT_IMPLY_GLOBAL_MODULAR_DENSITY`.

## 10. What is no longer a source obstruction

The protected downstream square-root cover changes the status of several Chapter-15 ingredients.

Conditional on the needed global modular-density input:

1. after inverting two, the square-root weight cover is finite étale, so smooth classical points and Zariski density pull back along the cover;
2. flat base change preserves the exact algebraic Poitou–Tate modules and finite-generation/torsion-annihilator arguments used in the globalization step;
3. Colmez–Wang Proposition 15.20 uses the all-prime parts of Kato's input — `H^1_Iw` torsion-freeness and `X^2_Iw=0` — rather than the odd-prime integral freeness upgrade;
4. the selected protected `S_3` residual image supplies the cyclotomic-tower irreducibility needed in the relevant residual step by the elementary normal-subgroup argument recorded in §2.

These are downstream proof obligations and deductions, not new provider theorems.  They should be replayed formally in MATHSOLVE after this source audit is admitted.

## 11. Exact provider disposition

The literature audited here does **not** presently supply the exact theorem required by the selected Colmez–Wang route:

`MISSING_P2_FULL_DEFORMATION_LOCALLY_IRREDUCIBLE_CLASSICAL_DENSITY_ON_SELECTED_S3_LANE`.

Provider disposition:

`QUALIFIED_P2_LOCAL_AND_ORDINARY_MODULARITY_WITH_FULL_DEFORMATION_DENSITY_GAP`.

This is a positive narrowing, not a no-go theorem.

The missing result can be discharged by either:

1. a source theorem proving the required literal-`2` global density on the selected `S_3` lane;
2. a new downstream proof of that density using modern literal-`2` modularity/local-global inputs;
3. a different direct classical-point continuation argument that avoids requiring full Zariski density.

No audited source currently establishes one of these in the exact required form.

## 12. Deterministic next action

After provider admission, return to MATHSOLVE and prove the maximal conditional Chapter-15 replay:

- import the protected square-root-cover theorem;
- prove the finite-flat/generic-fibre base-change lemmas explicitly;
- prove the selected `S_3` cyclotomic residual irreducibility lemma explicitly;
- replay Proposition-15.20-type localization injectivity from the already protected literal-`2` Iwasawa inputs;
- isolate the density theorem above as the only remaining Chapter-15 globalization assumption, unless a second independent obstruction appears during exact replay.

Do not reopen historical R5-RES until an actual protected residual Kato/Kolyvagin nonvanishing witness exists.

## 13. Firewall

This audit does not establish:

- the missing global density theorem;
- the literal-`2` Colmez–Wang family Kato comparison;
- denominator removal at literal two;
- a nonzero residual modular-symbol component;
- `c_Q^Kato mod 2 != 0`;
- `R5_RES_ESTABLISHED`;
- `R5_PRIM_ESTABLISHED`;
- D2d;
- BSD-R2-A1;
- novelty or priority;
- public certification;
- MATHCERT certification.
