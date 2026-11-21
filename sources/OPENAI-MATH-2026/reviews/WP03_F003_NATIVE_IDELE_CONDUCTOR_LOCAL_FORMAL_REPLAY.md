# OAI-26 F003 — independent native-idèle conductor-local Lean replay

**Record:** `GCL-OAI26-WP03-F003-NATIVE-IDELE-LOCAL/1`  
**Disposition:** `NATIVE_HECKE_LOCAL_CONDUCTOR_CORRECTION_KERNEL_VERIFIED__EXACT_HEAD__GLOBAL_IDELE_TO_RAY_AND_ANALYTIC_CONTINUATION_OPEN`  
**Source:** GCL [MATHFORGE PR #593](https://github.com/grandchallenge/MATHFORGE/pull/593), protected merge `0a0900a71fa0c9400559f0a088c854d7980e1812` (confirmed `main` readback). Candidate exact head `ad3c89d7317988ca7fe2a495dda1c215269da7dd`.  
**Scope:** Four **new Lean 4.36 lemmas** about the actual native mathlib idèle Hecke-character local Euler polynomial, not a rewrite or recertification of the upstream OAI seven-eighths theorem.

## 1. Independent source/version identity

**New native environment:** `leanprover-community/mathlib4@6e96f3e25b9b23468a6f155342b5a1e5e33ac8f9`, Git source tree `b2c8b308b3b161ad602b52f65b125c724e060536`, Lean `leanprover/lean4:v4.36.0-rc2`, `lake-manifest.json` SHA256 `de0f8c1467a6b313a7116d73cd3bcb390261d3d0a36bf246a13dbc0ad032d762`. Original native source `Mathlib/NumberTheory/NumberField/HeckeLFunction.lean`, Git blob `9dcd9a2a11f1407d47b9b0a1000259d237bdfe64`. The definition `NumberField.HeckeCharacter R K = IdeleClassGroup R K →ₜ* ℂ` belongs to **independent native mathlib** and is not the historical OAI `HeckeFamily.Character` type.

**Frozen earlier OAI:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`, Lean `v4.34.1`, pinned mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. That older mathlib did **not** contain the native HeckeLFunction module. This sidecar never upgrades or modifies the original OAI environment.

**Protected GCL code:** `sources/OPENAI-MATH-2026/formal/F003NativeHeckeConductorFactors.lean`, Git blob `63dda7aaf3e08dbc0dacc3bd5f2e3f544da5c38b`, raw SHA256 `b280e28da53c92910f0b986c563373400acc09ca5ad4bf885aa82768c985aab6`. Dedicated CI workflow `.github/workflows/oai26-f003-native-idele-conductor.yml`, Git blob `67755bc92f27ed4b35351460cd482ca028e9a1d1`; GH-OS routing registry blob `492120398754a17eee08e0063784740bafa99424`. The corresponding external routing, policy, CI and security checks PASS on candidate head. No broad trigger for unrelated OAI research files was added.

## 2. Exact formally checked propositions

The Lean source imports the native `HeckeLFunction` module and uses `χ : NumberField.HeckeCharacter R K` and the actual native place type `IsDedekindDomain.HeightOneSpectrum R`. Let \(S\) be any set of places representing the prime support of a **chosen zero-extension modulus**. Define \(\mathrm{presentationPolynomial}(\chi,S,v)\) to be \(1\) when \(v\in S\) and \(1-a_vX\) otherwise, and \(\mathrm{deletionCorrection}(\chi,S,v)\) to be the native \(\chi.\mathrm{localPolynomial}(v)\) when \(v\in S\) and \(1\) otherwise.

**Theorem A — exact local presentation/native factorization.**
\[
\forall v,\quad \big(v\notin S\Rightarrow \chi\text{ unramified at }v\big)
\quad\Longrightarrow\quad
\chi.\mathrm{localPolynomial}(v)
=\mathrm{presentationPolynomial}(\chi,S,v)\,
 \mathrm{deletionCorrection}(\chi,S,v).
\]
Formal name `GCL.OAI26.F003.NativeConductor.localPolynomial_presentation_times_correction`. It does **not** assume a nonexistent global idèle-to-ray isomorphism; it states the exact local factorization *conditional on the actual native character being unramified outside the designated modulus*.

**Theorem B — ramified correction is one.** If \(\neg\chi.\mathrm{IsUnramifiedAt}(v)\) then \(\mathrm{deletionCorrection}(\chi,S,v)=1\), independent of \(S\). Formal name `deletionCorrection_of_ramified`. This is the critical distinction: a prime dividing an **imprimitive** defining modulus may nonetheless be unramified and require a nontrivial deletion factor.

**Theorem C — elementary zero-exclusion.** For \(a,z\in\mathbb C\), if \(|a|\le1\) and \(|z|<1\), then \(1-az\ne0\). Formal name `one_sub_mul_ne_zero_of_norm_lt_one`.

**Theorem D — native correction cannot vanish in disk.** For any genuine native \(\chi\), any \(S,v,z\), if \(|\chi.\mathrm{localValue}(v)|\le1\) and \(|z|<1\), then
\[
\mathrm{eval}_z\bigl(\mathrm{deletionCorrection}(\chi,S,v)\bigr)\ne0.
\]
Formal name `deletionCorrection_eval_ne_zero`. Its \(|a_v|\le1\) hypothesis is explicit. It **does not** itself prove that an arbitrary continuous native idèle character has finite image; the intended finite-order specialization must be supplied by a *separate verified character bridge*.

**Relation to existing finite arithmetic:** Protected [PR #590](https://github.com/grandchallenge/MATHFORGE/pull/590) independently demonstrates why bare native/OAI L-function equality is false for an imprimitive modulus: the quartic \(5\to10\) Eisenstein character deletes the unramified norm-four prime \((2)\), whose correction is \(1+4^{-s}\). These four Lean theorems now check the exact structural rule **at the actual native Hecke-character API**, but do not themselves instantiate that quartic character as an idèle-class character. The orientation canary \(\chi((3+\omega))=i\), rather than \(-i\), remains a future global-map requirement.

## 3. Independent execution and hash-locked receipt

**Exact source-head run:** [GitHub Actions #44959280278](https://github.com/grandchallenge/MATHFORGE/actions/runs/44959280278), job `native-idele-conductor`, terminal `completed / success`. Run head **`ad3c89d7317988ca7fe2a495dda1c215269da7dd`**.

An explicit checkout `ref: github.event.pull_request.head.sha || github.sha` and exact `git rev-parse HEAD` assertion ensure the compiled bytes are bound to **the candidate commit**, not GitHub's synthetic pull-request merge commit. `receipt.json:gcl_head` and `receipt.json:expected_head` both equal the candidate SHA. The receipt also records `github_event_sha` separately to avoid confusing these identities.

The workflow checked the exact native mathlib commit, source tree, module Git blob, manifest SHA256 and toolchain. It restored the pinned mathlib cache and explicitly built `Mathlib.NumberTheory.NumberField.HeckeLFunction`, which was absent as a prebuilt olean in the cache. The complete pinned mathlib native build reported **7,184 jobs**. The new Lean file was elaborated by `lake env lean`, exit **0**, and `#check`/`#print axioms` were executed for all four declarations. Every one reports *exactly* the permitted foundational axioms:

```text
[propext, Classical.choice, Quot.sound]
```

No additional axioms or `sorryAx` appear. The archive `oai26-f003-native-idele-conductor` had **8/8 receipt-listed files** independently checked for SHA-256 and exact byte lengths, including the compiler output and source-head receipts. Digest evidence:

- `receipt.json` SHA256: `436d0ab86ed8067cb4fd892316b81c7ae497406c6c53b532ffef7233169de82d`.
- `compiler.log` SHA256: `e766dc8fb6c794ca0d4e33e7a3f630991c8f3a2153c1b8c1c59e43c69a62da26`.
- Candidate source raw SHA256: `b280e28da53c92910f0b986c563373400acc09ca5ad4bf885aa82768c985aab6`.
- Local exact-readback capture ID: `d130519dceed4d3fb8638556b2ea2291`, CHAD OS account, **not independently authenticated human mathematical review**.

All mandatory PR checks PASSED: native-idèle-conductor (1m17s), policy, routing-enforcement, security, CodeQL, reconnaissance, actions/python analysis.

**Recovered diagnostics, not scientific failures:**
1. Initial run [44958502593](https://github.com/grandchallenge/MATHFORGE/actions/runs/44958502593) lacked the newly introduced native `HeckeLFunction.olean`. Recovery added an exact `lake build Mathlib.NumberTheory.NumberField.HeckeLFunction` prerequisite.
2. Run [44958660634](https://github.com/grandchallenge/MATHFORGE/actions/runs/44958660634) compiled the native module but identified an unknown `HeightOneSpectrum` namespace. Corrected to `open IsDedekindDomain`.
3. Run [44958833599](https://github.com/grandchallenge/MATHFORGE/actions/runs/44958833599) exposed Lean's implicit argument and classical decidability constraints; the definitions now carry explicit character parameters and local classical evaluation.
4. Run [44959067224](https://github.com/grandchallenge/MATHFORGE/actions/runs/44959067224) compiled the four propositions with standard axioms, but its receipt's checkout resolved GitHub's synthetic PR merge SHA. The final exact-head replay above corrects this evidence identity.
5. All repair steps preserved original native pin and re-ran fresh exact-head CI. The first true exact-head bound success is **44959280278**, not any earlier partial run. No manual waivers.

## 4. Scientific and governance boundary

**Established:** actual independent native-idèle-character **local conductor correction** and zero-freeness of each correction polynomial under the stated unit-disk and norm bounds, Lean kernel checked under the new pinned mathlib toolchain, protected-admitted in MATHFORGE.

**NOT established by this PR:** existence of a continuous finite-order native idèle-class character for every original `OAI.SevenEighths.HeckeFamily.Character`; an actual global map out of the idèle class group with an exact **ray-class/conductor kernel**; matching local uniformizer values (and potential inverse convention) at all primes; a full finite Euler product identity under that map; native `HeckeCharacter.LSeries` analytic continuation from its absolute-convergence half-plane to \(\Re s>7/8\); independent verification of the original OAI sharp Gaussian bounds; or MATHCERT certification. The newest mathlib module supplies the idèle-class character and local Euler API but not the global reciprocity/ray-class comparison maps needed to close these points.

**Next substantive proof target:** construct and **Lean-prove a source-independent global idèle-to-ray character correspondence** for \(\mathbb Q(\zeta_3)\), based on local finite idele factorization and the ray class kernel, with a conductor-aware primitive/imprimitive Euler-factor theorem and *orientation-sensitive* quartic local-value instance. Keep native v4.36 and frozen OAI v4.34.1 in separate environments, then establish exact cross-implementation statement correspondence. Treat the missing global map as a **substantive mathematical formalization boundary**, not a transient CI defect.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI26-WP03-F003-NATIVE-IDELE-LOCAL
SOURCE_GCL_MAIN: 0a0900a71fa0c9400559f0a088c854d7980e1812
NATIVE_MATHLIB: 6e96f3e25b9b23468a6f155342b5a1e5e33ac8f9
LEAN_RUN: 44959280278
EXACT_CANDIDATE_HEAD: ad3c89d7317988ca7fe2a495dda1c215269da7dd
DISPOSITION: FOUR_NATIVE_LOCAL_LEMMAS_KERNEL_CHECKED__STANDARD_AXIOMS_ONLY
GLOBAL_IDELE_RAY_MAP: NOT_CONSTRUCTED
ANALYTIC_CONTINUATION_BRIDGE: OPEN
MATHCERT: NONE
```
