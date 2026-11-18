# OAI-26 WP03 — Family 005, pinned Catalan-constant source audit

**Record:** `GCL-OAI26-WP03-F005/1`  
**Pilot family:** 005 — irrationality of Catalan's constant  
**Exact upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**Disposition:** `UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH` (not a theorem refutation, not a proof replay, and not a global statement that no formalization exists).

## Exact source and crosswalk

The family has one indexed PDF, `preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf`, September 24, 2026. Its exact source identity was independently retrieved and checked:

- PDF: 44 pages, 574,388 bytes, Git blob SHA-1 `ecbe60eb89d2d25c1d07da6232f8d9869e6c0c1d`; SHA-256 `4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e`.
- GCL index: `sources/OPENAI-MATH-2026/MANUSCRIPT_INDEX.json`, Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`.
- Crosswalk: `sources/OPENAI-MATH-2026/FORMALIZATION_CROSSWALK.json`, Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`, pinned source `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
- In the crosswalk's 173 `source_papers` and 200 `main_results` entries, there are **zero** exact manuscript-path matches. A textual search of those 200 main-result entries for `catalan`, `irrational`, `dirichletbeta` and `beta.function` yielded **zero** candidate declarations. This is bounded evidence about that indexed catalogue, not an exhaustive repository-wide Lean search.

## Mathematical claim and proof structure (source inspection only)

Physical PDF page 1, Theorem 1.1, states that Catalan's constant
`G = beta(2) = sum_{j>=0} (-1)^j/(2j+1)^2`
is irrational. This is a claim **about the individual real number**, not merely the known existence of irrational members among families of even beta-values.

The source proposes determinants `Delta_N` of size `48N`; their entries involve rational linear combinations of `1`, `G` and `zeta(2)`. The text asserts that a Taylor-contact construction eliminates the `zeta(2)` component; if `G` is rational, `Delta_N` are rational. In the source's argument, Proposition 4.1 supplies nonzero determinants along sufficiently large prime `N=p`; Proposition 3.4 supplies the rationality-conditional lower limit; Proposition 7.1 supplies the upper limit. The argument explicitly uses a **mixed signed** determinant, so positivity/nonvanishing cannot be presumed from the usual positive Hankel-determinant method.

Pages 3 and 42 state that on the prime subsequence, for the normalized log determinant

```text
L_N = log|Delta_N| / (48 N)^2 - (1/2) log 2,
```

the claimed lower bound under rationality is

```text
liminf L_p > -2.29084,
```

whereas the claimed upper bound is

```text
limsup L_p <= -2.290939875 < -2.2909.
```

The order of the constants is arithmetically incompatible, since `-2.290939875 < -2.29084`, conditional on all claimed hypotheses and estimates holding. This verifies the final **implication from the stated bounds**, not the truth of the determinant identities, nonvanishing, denominator estimates, analytic upper bounds, or finite rational certificates. Page 41 describes a root-bracketing and derivative-bound certificate; that certificate was **not independently replayed**.

## Crosswalk result and critical witnesses

- **Positive source witness:** physical page 1 explicitly defines the constant and states `G` is irrational. Page 42 presents a contradiction argument from nonzero prime-scale determinants and the asserted opposed limits.
- **Bounded negative witness:** the exact PDF path has no indexed association in the crosswalk's 173 source-paper entries or 200 main-result entries; no Catalan/irrationality-related declaration is returned by the tested name filters. There is consequently **no source-backed candidate Lean declaration to compare semantically in this WP03 pass**.
- **Important distinction:** “not indexed” is **not** “proved unformalized” and is **not** a Lean compiler failure. Likewise the source's numeric contradiction is not a verification of its deep analytic inputs.

## Required next steps and limits

WP00 should confirm the exact family-to-declaration mapping or record a source-backed absence of correspondence. If a candidate formalization exists outside the 200-entry index, first identify its pinned source and theorem declaration; only then compare exact ambient objects, assumptions, quantifiers, definitions and conclusion. WP01 owns exact toolchain replay and axiom inspection. A non-authoring mathematical critic should independently examine determinant nonvanishing at prime scales, rational denominator clearing, and the real-place global extremum certificate before stronger claims.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F005
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH
EVIDENCE: exact PDF blob ecbe60eb89d2d25c1d07da6232f8d9869e6c0c1d; crosswalk blob 5fc50adc9430a91f22f1c3913bdfec62fe75acda; 44-page paper source and determinant-bound witnesses
REPLAY: PINNED_PDF_AND_CROSSWALK_STATIC_REVIEW; NO_LEAN_KERNEL_OR_FINITE_CERTIFICATE_REPLAY
UNRESOLVED: exact Lean mapping; source determinant and certificate checks; independent critic; protected admission
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
