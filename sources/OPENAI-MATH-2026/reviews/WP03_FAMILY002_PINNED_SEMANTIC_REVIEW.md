# WP03 Family 002 — BSD/Selmer scope separation

**Pinned upstream:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
**Catalogue identities:** `MANUSCRIPT_INDEX.json` Git blob `7a0b00eb9bfdeb59b157a98ee6522fc685580152`; `FORMALIZATION_CROSSWALK.json` Git blob `5fc50adc9430a91f22f1c3913bdfec62fe75acda`.
**Disposition:** `UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH`. This is a bounded source-and-index review, not a claim that no Lean formalization exists anywhere, not a theorem refutation, and not MATHCERT.

## Independently pinned manuscript editions

1. **Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank** — `preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/exact-bsd-low-selmer-corank.pdf`; 94 pages, 874353 bytes; Git blob `4621d1c197766f11d416b7e149343d938fcd9697`; SHA-256 `64b46603e174462e5bb32d242852eb7f0afe6e519f26534e42fd3f178a16b885`; exact paper-path crosswalk matches: **0**.
2. **The Selmer converse for elliptic curves at every prime** — `preprints/The-Selmer-converse-for-elliptic-curves-at-every-prime-October-7-2026/main.pdf`; 82 pages, 869458 bytes; Git blob `384525874a5e9989e574a5f9ce7c9883258cc732`; SHA-256 `bdb2f21b345a4f0fc9943a4e39bee27fedae5cf1e6842c40b3a77bd528ddea01`; exact paper-path crosswalk matches: **0**.
3. **The two-primary Birch–Swinnerton-Dyer formula in Selmer corank at most one** — `preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/paper.pdf`; 164 pages, 1279386 bytes; Git blob `9c1827e35640033bf16eac9fa88136079b1cc2de`; SHA-256 `734e4050dc8416c0f9ea7c9e15a29c6a8627feb53073e40b456d118f68d4dc5a`; exact paper-path crosswalk matches: **0**.

All document digests were calculated from actual pinned PDF bytes. The checked corpus crosswalk contains 173 `source_papers` and 200 `main_results` entries. Exact PDF paths above do not match its `source_papers`; no candidate source-to-Lean theorem equivalence is established by this index. Path absence is not proof of unformalization.

## Source-derived mathematical analysis

The October 7 exact BSD paper claims an entire leading-term formula (including all prime factors) when full q-power Selmer corank is 0 or 1 for some q. The separate every-prime Selmer converse claims rank equality and finite Sha, not the full leading coefficient. The October 6 paper claims only the two-primary BSD formula. These are three different conclusions and cannot be certified by one undifferentiated rank declaration.

**Mathematical verification still required:** Verify every prime q and full Selmer corank quantifier, finite Sha, leading coefficient/regulator conventions and exact prime factors; no indexed Lean mapping is established. Formal proof dependencies, exact Lean source and compiler replay, axioms and independently adjudicated mathematical correctness were not established in this source review. Distinguish the manuscripts' claims from verified theorems.

## Critical scope test

**Positive witness:** the named pinned edition(s) make the distinct mathematical claims and conditions just recorded in their opening definitions, abstracts and theorem sections. **Countervailing witness:** no exact indexed source paper correspondence exists, so asserting that a particular crosswalk comparator verifies any of these manuscript statements would be unsupported. The review is a deliberately source-edition-bound `UNRESOLVED` verdict, which WP03 explicitly permits.

**Reproduction:** obtain each PDF at the upstream pinned commit, recompute its Git blob SHA-1 and SHA-256, compare its initial theorem/assumption statements, and match exact PDF paths against the crosswalk. Obtain a named Lean declaration and full semantic definition bridge before any `PROPOSITION_LEVEL_ALIGNMENT` promotion. WP01 separately owns Lean and axiom replay; WP04 independently criticizes mathematical validity.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI-26-WP03-F002
SOURCE_SHA: 1581d4cbdd69a0faf34b2089614fe2a814316a6a
DISPOSITION: UNRESOLVED__NO_INDEXED_FORMALIZATION_MATCH
EVIDENCE: 4621d1c197766f11d416b7e149343d938fcd9697; 384525874a5e9989e574a5f9ce7c9883258cc732; 9c1827e35640033bf16eac9fa88136079b1cc2de
REPLAY: PINNED_PDF_STATIC_REVIEW_ONLY; LEAN_NOT_RUN
UNRESOLVED: Verify every prime q and full Selmer corank quantifier, finite Sha, leading coefficient/regulator conventions and exact prime factors; no indexed Lean mapping is established.
CLAIM_BOUNDARY: NO_MATHCERT_CERTIFICATION
```
