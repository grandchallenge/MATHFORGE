# YM-001 / YM-D003 source audit — Balaban ultraviolet/large-field spine and Magnen–Rivasseau–Sénéor fixed-IR construction

## Record

- Campaign: `YM-001`.
- Parent debt: `YM-D003`.
- Protected Forge baseline: `267670385485b88be0556f6993dc171127139ae1`.
- Audit date: `2026-09-18`.
- Purpose: acquire exact bibliographic/theorem-body scope for the four-dimensional Balaban RG/large-field sequence and the Magnen–Rivasseau–Sénéor `YM_4` fixed-infrared-cutoff construction; determine which D003 obligations they actually close.
- Authority: source/provider audit only. MATHFORGE does not certify downstream theorems or change Programme/Solve claim status.

## Provenance state

The browser-accessible primary/author-hosted surfaces and publisher/DOI metadata were inspected directly.

The following source identities are fixed bibliographically by journal, volume, pages, DOI, title, and author. Direct independent PDF byte acquisition was attempted where a public author copy was exposed; the ResearchGate PDF endpoint returned a dead/404 object in this runtime. Therefore this tranche does **not** claim publisher-PDF or author-PDF SHA-256 byte locks.

This is a provenance limitation, not permission to strengthen any source interface. Only claims supported by the inspected theorem/abstract/body surface below are admitted.

## Source records

### YM-SRC-021 — Balaban RG II: cluster expansions

Tadeusz Balaban, “Renormalization group approach to lattice gauge field theories — II. Cluster expansions,” *Communications in Mathematical Physics* **116** (1988), 1–22.

- DOI: `10.1007/BF01239022`.
- Public metadata surface: Rutgers/OpenAIRE DOI-indexed record.
- Acquired source-level conclusion: the fluctuation field integral from Part I is represented by an exponentiated cluster expansion; the expansion terms satisfy the inductive assumptions; this completes the sequence of effective actions **in the small-field approximation**.
- Exact boundary: small-field completion only. It does not close four-dimensional large fields, ultraviolet-limit existence, infinite volume, OS reconstruction, or mass gap.

Disposition:

`ADMIT_SMALL_FIELD_CLUSTER_COMPLETION_ONLY`.

### YM-SRC-022 — Balaban convergent renormalization expansions

Tadeusz Balaban, “Convergent renormalization expansions for lattice gauge theories,” *Communications in Mathematical Physics* **119** (1988), 243–285.

- DOI: `10.1007/BF01217741`.
- Public metadata surface: Rutgers/OpenAIRE DOI-indexed record.
- Acquired source-level conclusion: introduces an inductive description of complete effective densities including large-field domains and proves preservation of the density form under renormalization transformations.
- The abstract states that this completes RG analysis and gives convergent expansions **for superrenormalizable models**.
- Exact boundary: the convergence conclusion in the inspected abstract is qualified to the superrenormalizable case; it is not by itself the completed four-dimensional pure-gauge ultraviolet-stability theorem.

Disposition:

`ADMIT_COMPLETE_DENSITY_LARGE_FIELD_ARCHITECTURE__4D_UV_COMPLETION_NOT_FROM_THIS_SOURCE_ALONE`.

### YM-SRC-023 — Balaban Large Field Renormalization I

Tadeusz Balaban, “Large field renormalization. I. The basic step of the R operation,” *Communications in Mathematical Physics* **122** (1989), 175–202.

- DOI: `10.1007/BF01257412`.
- Public primary metadata surfaces: INSPIRE; Crossref/OpenAIRE; OSTI/ETDE.
- Acquired source-level conclusion: constructs the `R` renormalization operation for expressions associated with large-field regions.
- The source states that this removes the main obstacle to proving ultraviolet stability of four-dimensional gauge field theories.
- The source explicitly defers completion of the proof to Part II.

Disposition:

`ADMIT_4D_LARGE_FIELD_R_OPERATION__COMPLETION_DEFERRED_TO_PART_II`.

### YM-SRC-024 — Balaban Large Field Renormalization II

Tadeusz Balaban, “Large field renormalization. II. Localization, exponentiation, and bounds for the R operation,” *Communications in Mathematical Physics* **122** (1989), 355–392.

- DOI: `10.1007/BF01238433`.
- Public primary metadata surfaces: Rutgers/OpenAIRE/Crossref.
- Acquired source-level conclusion: concludes the basic properties and bounds for the `R` operation and states that this **completes the proof of ultraviolet stability of four-dimensional pure gauge field theories, as formulated in Theorem 1**.
- This materially strengthens the current protected YM ledger, which stops at the 1987 small-field result.
- Exact non-overreach boundary: the source-level statement is ultraviolet **stability**. It must not be silently promoted to uniqueness/existence of all continuum Schwinger functions, removal of the infinite-volume/infrared cutoff, OS reconstruction, a physical reference scale, or a mass-gap theorem.

This boundary is independently corroborated by the 1993 Magnen–Rivasseau–Sénéor discussion of Balaban: they describe the block-spin programme as keeping the resulting effective action bounded as the lattice spacing tends to zero, and state that an ultraviolet limit for gauge-invariant observables should follow at least through a compactness/subsequence argument, while uniqueness requires further work.

Disposition:

`ADMIT_4D_PURE_GAUGE_ULTRAVIOLET_STABILITY__NOT_FULL_CONTINUUM_CONSTRUCTION`.

### YM-SRC-025 — Magnen–Rivasseau–Sénéor `YM_4` with fixed infrared cutoff

Jacques Magnen, Vincent Rivasseau, Roland Sénéor, “Construction of `YM_4` with an infrared cutoff,” *Communications in Mathematical Physics* **155** (1993), 325–383.

- DOI: `10.1007/BF02097397`.
- Public author-uploaded body surface inspected through ResearchGate; journal identity independently corroborated by DOI/CMP metadata.
- Model: pure `SU(2)` Yang–Mills in four dimensions, trivial topological sector, regularized axial gauge.
- Regulator profile: fixed infrared cutoff; ultraviolet cutoff removed in the source-stated construction.
- Large-field mechanism: axial-gauge positivity plus a small-/large-field phase-space decomposition, background-dependent gauge/propagator control, stabilizing momentum cutoffs, and nonperturbative treatment of large-background contributions/counterterms.
- Source-stated end result: ultraviolet limit of the Schwinger functions exists and the limiting functions satisfy the corresponding Slavnov identities for the chosen fixed infrared cutoff.
- Critical proof-completeness qualification from the source body: the authors explicitly say they do **not** provide a detailed proof of convergence of the expansion in all details; they present the elements needed for such a proof and describe a fully self-contained write-up as a substantial further task.
- Infrared boundary: the authors explicitly say they do not attempt to remove the infrared cutoff; this is associated with large coupling/nonperturbative confinement-scale effects beyond their constructive method.
- OS boundary: they explicitly do not establish the full Osterwalder–Schrader axiom set; they discuss OS positivity as plausible with additional work rather than as a proved conclusion of this paper.
- Topological boundary: nontrivial large gauge transformations/topological effects such as instantons are not treated.

Disposition:

`ADMIT_SOURCE_STATED_UV_CUTOFF_REMOVAL_AT_FIXED_IR__EXPLICIT_PROOF_COMPLETENESS_AND_IR_OS_LIMITATIONS`.

Do **not** relabel this record as a fully self-contained theorem closing D003.

## Composition audit against YM-D003

Protected D003 requires:

> control the four-dimensional ultraviolet limit, infinite-volume limit, and large-field sector along a physical continuum trajectory; uniform estimates must construct and identify a nontrivial four-dimensional continuum theory.

The newly acquired sources change that debt decomposition materially.

### D003-A — four-dimensional large-field control

Balaban `YM-SRC-023` and `YM-SRC-024` directly address the large-field obstruction through the `R` operation.

Disposition:

`SUBSTANTIALLY_SUPPLIED_BY_BALABAN_R_OPERATION`.

The exact downstream use must remain within the UV-stability theorem's finite-volume/lattice RG framework and source hypotheses.

### D003-B — four-dimensional ultraviolet stability

Balaban `YM-SRC-024` explicitly states completion of the proof of ultraviolet stability for four-dimensional pure gauge theories.

Disposition:

`SUPPLIED_AS_ULTRAVIOLET_STABILITY`.

This is stronger than the currently protected `YM-T-090` small-field-only record.

### D003-C — ultraviolet-cutoff-free Schwinger functions

MRS `YM-SRC-025` states a construction of `SU(2)` four-dimensional Schwinger functions with fixed infrared cutoff and no ultraviolet cutoff, with Slavnov identities.

Disposition:

`SOURCE_STATED_AT_FIXED_IR__PROOF_COMPLETENESS_QUALIFIED`.

This source may be used downstream as a qualified constructive interface, not as a fully self-contained D003-closing theorem.

### D003-D — infrared cutoff / infinite volume

Neither the Balaban large-field UV-stability record nor MRS supplies removal of the physical infrared cutoff/infinite-volume limit needed for the full Clay-target continuum theory.

MRS says explicitly that this cutoff is never lifted.

Disposition:

`OPEN__MISSING_IR_REMOVAL_AND_INFINITE_VOLUME_CONSTRUCTION`.

### D003-E — uniqueness/identification of the full continuum theory

The inspected sources do not establish a unique full four-dimensional continuum Yang–Mills theory satisfying the required nonperturbative identification contract.

MRS's discussion of Balaban explicitly warns that a compactness/subsequence UV limit for gauge-invariant observables would not by itself establish uniqueness.

Disposition:

`OPEN__MISSING_UNIQUENESS_AND_FULL_CONTINUUM_IDENTIFICATION`.

### D003-F — complete OS/reconstruction profile

Not supplied. MRS expressly does not establish the full OS axiom set; this remains coupled to `YM-D002`.

Disposition:

`OPEN_D002_COUPLED`.

### D003-G — non-circular physical reference scale

No source in this tranche proves a finite, nonzero, non-circular four-dimensional physical reference scale after infrared/infinite-volume removal.

Disposition:

`OPEN_D001_FACING_SUBOBLIGATION`.

## Corrected D003 frontier

The previous broad label

`MISSING_4D_NONPERTURBATIVE_CONTINUUM_AND_LARGE_FIELD_CONTROL`

is now too coarse.

The source-audited frontier is:

`BALABAN_4D_UV_STABILITY_AND_LARGE_FIELD_CONTROL_AVAILABLE__FULL_IR_REMOVAL_UNIQUENESS_OS_AND_PHYSICAL_IDENTIFICATION_OPEN`.

For a native Solve composition theorem, the smallest exact question is:

> Given Balaban's admitted 4D ultraviolet-stability/large-field theorem and MRS's qualified fixed-IR ultraviolet-cutoff-free Schwinger construction, which D003 obligations are now closed as interfaces, and can the remaining D003 debt be reduced to infrared-cutoff/infinite-volume removal plus uniqueness/physical identification without importing any unproved OS or mass-gap claim?

## Source-provenance limitations

- No source PDF byte is committed by this tranche.
- No independently recomputed publisher/author PDF SHA-256 is asserted.
- The Balaban theorem-body interface admitted here is bounded by public DOI-indexed abstract/source metadata and the exact source-level conclusion stated by Part II.
- The MRS audit used an author-uploaded full-body web rendering; its direct PDF endpoint was unavailable in this runtime.
- Any later downstream argument needing an equation-, lemma-, or theorem-number-exact internal hypothesis beyond the interfaces above must reopen Forge for a deeper source-body/byte audit.

## Provider boundary

MATHFORGE admits source interfaces only.

This tranche does not:

- certify Balaban or MRS;
- claim that D003 is discharged;
- claim existence of the full four-dimensional theory;
- remove the infrared cutoff;
- establish OS reconstruction;
- establish a physical mass gap;
- establish a non-circular reference scale;
- establish confinement, novelty, priority, or Clay-problem resolution.

## Recommended Programme records

If protected, Programme may register:

- `YM-SRC-021` through `YM-SRC-025` with the boundaries above;
- a new theorem-interface record for Balaban 4D ultraviolet stability / large-field completion;
- a separate qualified construction record for MRS fixed-IR UV-cutoff removal;
- a revised D003 composition state that marks large-field/UV-stability debt as materially reduced while preserving infrared removal, uniqueness, OS, and physical-scale obligations.
