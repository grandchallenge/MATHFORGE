# YM-001 / YM-D003 / MRS MT1 — scalar critical-mass template dependency audit

## Record

- Campaign: `YM-001`
- Parent target: `YM-D003-MRS-R002-MT1 — EXACT_ZERO_MASS_COUNTERTERM_TUNING`
- Forge baseline: `90254084f3d06dcaad1a6a950039396ea85c23f9`
- Date: 2026-10-03
- Authority: source/provider dependency audit only.

## Purpose

Determine whether the scalar `phi^4_4` critical-mass construction cited by MRS supports treating exact mass tuning as a stand-alone one-dimensional fixed-point lemma, or whether its proof itself depends on renormalized two-point subgraph/polymer bounds.

## Primary scalar template

J. Feldman, J. Magnen, V. Rivasseau, R. Sénéor, “Construction and Borel summability of infrared phi^4_4 by a phase space expansion,” *Communications in Mathematical Physics* **109** (1987), 437–480, DOI `10.1007/BF01206146`.

### Inductive definition of the scalar mass subtraction

FMRS1 defines the mass counterterm scale by scale.

At scale `i`, the paper assumes that lower-scale mass counterterms and running couplings are already known. It then defines the scale-`i` mass contribution `delta m^2(x,i)` as a sum over sub-contributions.

Each contribution is the **negative zero-external-momentum value** of a sum of one-particle-irreducible two-point Mayer graphs of the relevant scale and subgraph structure.

Thus the scalar mass choice is not introduced as an abstract scalar parameter detached from the constructive expansion. It is defined from the local relevant projection of the renormalized 1PI two-point graph sector inside that expansion.

### Bound needed by the scalar recursion

FMRS1's renormalization-group section proves inductive bounds on the running quantities. Its Theorem III.1 includes a scale-dependent bound on the mass counterterm.

The paper explicitly derives the needed recursion estimates from Theorem III.2, which bounds the relevant two-point/four-point Mayer subgraph sums, with later sections proving those subgraph estimates.

Therefore the scalar critical-mass construction has the dependency shape:

`renormalized 1PI two-point Mayer-graph definition`
→ `uniform/local subgraph bounds`
→ `inductive mass-counterterm bound`
→ `critical mass selection`.

It is not source-supported to extract only “Banach fixed point” and discard the graph/subgraph bounds that make the map well-defined and controlled.

## Comparison with MRS

MRS cites this scalar construction as a method template for the Yang–Mills relevant mass operator.

However, in the inspected MRS paper:

- no Yang–Mills analog of the FMRS1 scale-by-scale 1PI two-point mass-subtraction recursion is stated;
- no theorem analogous to FMRS1 Theorem III.2 is stated for the MRS renormalized two-point Mayer/polymer sector;
- Section VII gives reasons for convergence and model-specific power-counting discussion, but the MRS paper explicitly does not provide the complete detailed convergence proof.

Hence the exact-mass-tuning problem is **not cleanly separable** from at least a local part of the missing MRS constructive convergence machinery.

It does not follow that MT1 requires the complete global Schwinger hierarchy before it can be solved. The scalar template shows a narrower requirement: theorem-grade control of the **renormalized local 1PI two-point polymer/subgraph sector** sufficient to define and bound the relevant mass recursion.

## Source disposition

`MT1_FIXED_POINT_NOT_STANDALONE__SCALAR_TEMPLATE_DEPENDS_ON_RENORMALIZED_1PI_TWO_POINT_SUBGRAPH_BOUNDS__MRS_ANALOG_NOT_THEOREMIZED`

## Smallest source-supported native residual

`YM-D003-MRS-R002-R2P1 — UNIFORM_RENORMALIZED_1PI_TWO_POINT_POLYMER_BOUND_AND_MASS_RECURSION`

A native proof of R2P1 should provide, in the MRS gauge/cutoff setting:

1. a local relevant projection for renormalized 1PI two-point polymer/subgraph amplitudes;
2. a scale-by-scale definition of the exact quadratic counterterm from that projection;
3. a theorem-grade bound on the two-point subgraph sector uniform in the ultraviolet cutoff depth required by the induction;
4. a response/nondegeneracy estimate sufficient to solve the exact zero-mass condition;
5. compatibility with the MRS background-field/Section VI stability normalization.

This is narrower than the full global polymer/Schwinger convergence theorem, but it is not reducible to a citation-only scalar fixed-point argument.

## Boundary

This audit does not prove or refute R2P1. It identifies the exact proof dependency exposed by the scalar source cited by MRS.
