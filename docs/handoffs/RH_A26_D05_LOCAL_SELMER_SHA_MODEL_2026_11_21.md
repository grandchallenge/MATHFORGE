# RH-A26 D05 — local Selmer transfer and genuine Sha model source audit

**Date:** 2026-11-21. Original Alpöge–Claude Lean archive: assembled SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`. Paths are relative to its `lean/src`. This is a mathematically independent reconstruction of a *conditional algebraic sublemma*, plus an original-source crosswalk. It is **not** independent Lean replay or validation of RH/GRH.

## A. The exact Selmer local condition

Original `Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/SelmerTransport/RestrictionMemInvariantH1.lean`, SHA-256 `ce8f72b24a82c174407e098f09a79a4ecea035dbeb2e1026422e794551031efb`, defines
```lean
def LocSel (ρ : Representation R G M) (U : Subgroup G) (𝒟 : Set (Subgroup G)) :
    Submodule R (H1U ρ U) :=
  ⨅ D ∈ 𝒟, LinearMap.ker (resU ρ (inf_le_left : U ⊓ D ≤ U))
```
So a class is locally Selmer iff it restricts to zero on `U∩D` for **every** prescribed local subgroup `D`. `resU_mem_locSel` proves restriction preserves these zero local conditions, using functoriality of nested restriction.

Source `.../SelmerTransport/ConjStableShaFam.lean`, SHA-256 `d601228f26cb82f2f228b44b6ab97a6dd8e35ff8ca0b32d3e3ec9b13dae14aad`, defines
```lean
shaFam k Ω l =
 {D | (∃ A, A.valuation (l:Ω)<1 ∧ D=Dec_k(A)) ∨
      (∃ A, D=Ine_k(A))}.
```
It includes full decomposition groups at primes over `l` and inertia groups at all places, a recognizable unramified-outside-the-l-primes local condition. `conjStable_shaFam` says the family is Galois-conjugation invariant, required to form a compatible representation on Selmer classes.

## B. Independent proof: local Selmer kernel transfer when the index is invertible

Let `G` be a group, `U' ◁ U≤G` a normal subgroup of finite index `m`, and `R` a commutative ring in which `m\cdot 1_R` is a unit. Let `M` be a continuous discrete `G`-module. Define `S(U)\subseteq H¹(U,M)` by requiring restriction to `U∩D` to vanish for every subgroup `D` in a conjugation-stable family `𝒟`; similarly define `S(U')`.

**Claim.** Restriction gives a linear isomorphism
```text
S(U) ≅ S(U')^(U/U')
```
(where the invariants are taken under the natural conjugation action), provided the standard continuous inflation–restriction and corestriction theorems apply and the chosen local restrictions obey their functoriality.

**Independent proof.** In the continuous Hochschild–Serre sequence, invertibility of `m` kills `H¹(U/U',M^{U'})` and `H²(U/U',M^{U'})` by averaging, so restriction identifies `H¹(U,M)` with the invariant part of `H¹(U',M)`. Restriction preserves `S` because for each `D`, the map to `H¹(U'∩D,M)` factors through `H¹(U∩D,M)`.

Conversely take an invariant `y∈S(U')` and its unique antecedent `x∈H¹(U,M)`. For every `D∈𝒟`, the subgroup `U'∩D` is normal in `U∩D`. Its index `m_D=[U∩D:U'∩D]` divides `m`, hence `m_D` is also a unit in `R`. The kernel of
```text
H¹(U∩D,M) → H¹(U'∩D,M)
```
is therefore zero (another application of finite-index averaging). As `x|_{U'∩D}=y|_{U'∩D}=0`, injectivity forces `x|_{U∩D}=0`. Since `D` was arbitrary, `x∈S(U)`. This proves the stated isomorphism and its local-condition preservation.

This is a genuine all-subgroup abstract proof, **not** merely a finite model regression. Its hypotheses are essential; it does not identify the *number-theoretic* original `Sha(D,e)` with `S(U)` without a separate source comparison.

## C. Original source implementation of the local proof

- `.../SelmerTransport/KerResSmul.lean`, SHA `831e3fe6fb2bfd29ab8fe881febc447e50f119677474540b15901d60170a094e`, proves the restriction-kernel is annihilated by the index. It calls `UpperTheory.Reformulated.B.Qi36.aux` from `.../IntegralCasts/CapelliIdentities/ImportsMoreSide.lean`, which constructs an explicit coset-sum primitive for a cocycle vanishing on the subgroup. This provides a direct alternative to merely citing abstract Hochschild–Serre.
- `.../SelmerTransport/CorInv.lean`, SHA `2bc03800bb31e69bd87512e6aaf8653ee885f1d35ba7df54887b17b38db5d7b3`, proves an invariant class times the index lies in restriction's range, using a continuous corestriction cocycle and a finite coset sum.
- `.../SelmerTransport/SelUnit.lean`, SHA `d053b8632233b96146b17e5870bf8e351c121df4df11cc80eff8c13da3f7df0a`, combines both with the lemma `(U'∩D).relIndex (U∩D) ∣ U'.relIndex U`. This is exactly the key step in the independent argument above, and produces both injectivity and image=trivial-character eigenspace of `S(U')`.
- This entire local transfer *does not require Poitou–Tate or Bernoulli input*. Those are separate, downstream arithmetic claims and should not be merged into this result.

## D. Source construction bridging to the original arithmetic Sha

The previous review had left open even the existence of a bridge from the archive's genuine `Sha D e` to the subgroup `ShaU`. The new source audit locates an explicit construction:

- `.../SelmerTransport/ShaModel.lean`, SHA `2c74ff73930693c0476dce67072d98f6389bacb7358a3dae47589f977550a415`, proves **source-level** theorem `UpperTheory.V.Base.shaModel`, whose statement constructs `Φ : Sha D e ≃ₗ[ℤ_[l]] ShaU (qzG k Ω l e) l (galOf k E Ω)` with a cocycle inflation compatibility property.
- It factors through `sha_exists_cocycle_lift_whole`, `mem_shaAbs_iff_resH1_whole_mem_locSel`, `selTransport`, `galEmbFam`, and `shaInfl`.
- `.../GaloisLibrary/GaloisCohomologyLength/ShaInfl.lean`, SHA `06bb706e6043a9f1fc60087b0a394041979989f1716bc3dfa8af0a339dd986ca`, proves source-level transport from a kernel of local `resH1` maps on the ramification-restricted Galois quotient to `ShaAbs` on the full Galois group, using `infUnram` and the place comparison.
- `.../SelmerTransport/Places.lean`, SHA `3ee60f53524a02a4eb57466f3d1d1abe331c29cb95ee10b991632800e82f8306`, identifies valuations at finite primes and isolates the special top valuation; `GalEmbFam.lean`, SHA `094f7f6ff784faecefcb02a102bb4776f2238446713e23eb440805ef6108a21a`, proves that decomposition/inertia families and cyclotomic twists pull back along the extension's Galois embedding.
- `.../SelmerTransport/ShaLenEq.lean`, SHA `77cc17f54620c295c60629531a6144c04796bdd4ae250841ca0078fb07a81e1e`, then states both equality of the original `shaLen` and the subgroup-Selmer module length, **and** equality of genuine Galois-action eigenspace lengths under a specified lift. This is more than a matching name or type: it is an explicit *claimed* linear-equivalence and eigenaction transport in the original archive.

**Evidence classification:** These exact source claims eliminate a former **source-location gap**. They do **not** independently prove mathematical correctness of the full arithmetic comparison, the source's imported `shaInfl` and `infUnram`, or the original Lean kernel replay. There is no claim that `Sha` has been replaced by a toy group.

## E. Exact finite local test and invalid-index witness

GitHub-hosted `tests/rh_a26_selmer_local_restriction.py` was independently fetched and executed on CHAD. SHA-256 `ad6c5184756aec567237c8f243850b1d6c30c24fd895bf0c7d7f0b6773b70206`. Receipt `c157c95294f347b69396138a165af1a2` (OS-local, not independently authenticated), result:

```text
PASS 7448 prime-to-index local kernel comparisons;
     1306 excluded-index failures; C3/F3 witness
```

The test uses trivial `𝔽_p` coefficients for cyclic `G=C_n`, `U'=⟨m⟩`, and a local subgroup `D=⟨d⟩` for each divisor `d,m|n`. Cocycle classes are `z\in 𝔽_p` with `nz=0`. Local triviality is `dz=0`. After restriction, `y=mz`, and the `U'∩D` local condition is `(lcm(m,d)/m)y=0`. Every tested prime-to-index case preserves the exact kernel, while excluded-index controls demonstrate why the unit condition cannot be removed. This is a test of the mathematical *mechanism*, not the full `shaInfl` theorem.

## F. Precise remaining proof debt

1. Independently establish that the original `Sha1` (local decomposition groups over `l`) and the full-group `ShaAbs` (local decomposition at `l`, inertia outside) really correspond through `shaInfl` for the author's actual quotient representation, including unramified-quotient continuity and place identification.
2. Independently validate `shaModel`, `selTransport` and `shaLenEq` across field embeddings, topological Galois groups and genuine action-eigenspace decompositions.
3. Independently establish the valuation/character inequality `ML.vChar`, derived from `Rec` and generalized Bernoulli integrality, not supplied by local Selmer transfer.
4. Replay pinned original Lean archive in Lean 4.33.1; inspect axiom provenance and proof dependencies at the exact revision. No RH/GRH certificate.

**Disposition:** `RH-A26-D05_LOCAL_SEL_TRANSFER_INDEPENDENTLY_PROVED__GENUINE_SHA_MODEL_LOCATED__INFLATION_AND_BERNOULLI_VALUATION_NOT_INDEPENDENTLY_PROVED`.
