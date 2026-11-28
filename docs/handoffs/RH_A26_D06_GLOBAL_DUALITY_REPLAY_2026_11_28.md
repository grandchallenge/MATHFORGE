# Original-source foundational duality replay

MATHFORGE #577, extending #641–643. No certification or promotion. Execution is CHAD OS-account-only, not independently attested. Archive SHA256 9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc; Lean 4.33.1 commit 819816b2e0a3bf405af45ae5c7af2491d8f5bee6; nine pinned dependency repositories clean, official dependency cache used rather than rebuilt. Identity receipt 4ce2bd691c62487da2e2f1e0c8806d3c.

Both global targets compiled (exit 0) after two bounded timeouts (124). Both target modules passed separate leanchecker (exit 0). Original global axiom audit exited 0. Initial auxiliary joined audit failed because theorem syntax lacked an explicit type; retained original failure, no original source changes. Corrected typed harness passed, receipt 76e68f7abced42daa7fc790310f1c298. Exact checked types:

- PositivityTheory.Lit1.PTN.poitouTateNormalised_holds : GlobalTheory.Published.PoitouTateNormalised
- GlobalTheory.PoitouTateConj.poitouTateDuality_of_normalised : GlobalTheory.Published.PoitouTateNormalised → GlobalTheory.Published.PoitouTateDuality
- gcl_original_poitou_tate_join : GlobalTheory.Published.PoitouTateDuality

All three axiom sets are exactly propext, Classical.choice, Quot.sound. No sorryAx. Together with #643 this closes the targeted original-source replay of the three explicit duality inputs of LemmaKOfLitN.

All 1927 distinct original source digests reverified; 1917 global, 312 local, overlap 302. All corresponding external artifact hashes agree across both MIT manifests. Local comparison: 1390 exact matches (1356 without warnings, 34 with warnings), 537 differences all in warning-bearing modules; zero warning-free differences. NormalisedHolds matches exactly; conjugation bridge differs with warnings and passed target kernel replay. Warning association is not a byte-level explanation. No claim of exhaustive independent local kernel replay.

Evidence SHA256:
- global-reconciliation.tsv: fd498e132e7c32b530afdcfc2c4985a2ba38bdc87adc3fa284d8b43f97af1a33 (retained as RH_A26_GLOBAL_DUALITY_COMPILED_HASHES.tsv)
- global-joined-exact.log: b0f2d834b6683ddb5ea5f29a0e4028f0c2e1560617f209a01868dec41185ee94
- global-axioms.log: a5b2d722fa74cf75d6a9a0dd5cb63dd18a5ad5fe6eee23250341f5aaea4c65e9
- global-target-checker.log: 23eeec7391dfb359d0e428ae3ff32ec575382d2af105dc72d85ae7e63f48ec94
- global-build-3.log: c4418b97a100ac16f11042bb93d30881abbb3fac801e8b21897f9c5986060691

Remaining distinct obligation: trace BOdd to its exact original discharge declaration, check its type and transitive axioms, and verify its composition with these three inputs through LemmaKOfLitN and the downstream RH/GRH proof spine, including semantic correspondence. No claim that this has been done here.
