# RH-A26 D05 — prime-to-index eigenspace transfer: independent lemma and failure case

Date: 2026-11-21. Source identity: original 14-part Alpöge–Claude Lean archive SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`. This document independently proves an abstract, conditional cohomological mechanism. It does not validate the original Lean archive, the author's local/global comparison, or RH/GRH.

## Source-located claim

- `Development/AutomorphicArithmetic/AutomorphicVarieties/CharacterLevelBounds/EigV.lean` SHA-256 `4d076154ed063735fd06a0aa883bfb28c0815ca5773458976d19ed5f12217763` proves `UpperTheory.V.Chr.eigV` for a normal open subgroup `U` on which a character is trivial, assuming the prime `l` does not divide the subgroup index. It concludes an equality of the two *defined* cohomological eigenspace lengths `eigL l e U ψ = V l e ψ`.
- `.../GaloisLibrary/SelmerTransport/SelEigBase.lean` SHA-256 `da8c33be3bde62eec61ade2414f1cd4dfc3152a7bcdc344cd99484d847f1ddf4`: `selEigBase` gets the equality by a twisting equivalence `selTwist` and `selUnit`, then `LinearEquiv.length_eq`.
- `.../SelmerTransport/SelUnit.lean` SHA-256 `d053b8632233b96146b17e5870bf8e351c121df4df11cc80eff8c13da3f7df0a`: `selUnit` explicitly states injectivity and onto-invariants for restriction on Selmer cohomology under an invertible finite index. It uses `kerResSmul`, `corInv` and index divisibility for local subgroups. The unit hypothesis is necessary.
- `.../SelmerTransport/SelTwist.lean` SHA-256 `fcb47447b7c63183606f6c3ff1245deb1276916ad0581cb364be9d54b01f1bb3`: the twist equivalence preserves character eigenspace length, given the representation actions agree on `U`.
- `.../PrimitiveFrobeniusFixed/PsiOf.lean` SHA-256 `be81f7279d28d67f9be81ade8a028375c11be57c11a5559f82240c14009ebd63`: `ML.psiOf` uses `eigV` after proving that the subgroup-index exclusion follows from the `l ∤ [E:ℚ]` hypothesis and that the character actions match.

## Independently proved abstract lemma

**Finite-index descent for first cohomology.** Let `U` be normal of finite index `m` in `G`. Let `R` be a commutative ring where `m` is a unit and `M` a `G`-module with suitable cohomology. The restriction `H¹(G,M)→H¹(U,M)` is injective, because corestriction followed by restriction acts as multiplication by `m` on `H¹(G,M)` (in the standard restriction-corestriction arrangement). Furthermore, the Hochschild–Serre five-term exact sequence shows the image is exactly the `G/U`-invariant subgroup: the outer groups `H¹(G/U,M^U)` and `H²(G/U,M^U)` vanish when `m` is invertible. Indeed, for a finite group `Q` of order `m` the averaging idempotent `m^{-1}\sum_{q∈Q}q` makes taking invariants an exact functor, hence all higher derived functors vanish. Therefore restriction identifies `H¹(G,M)` with `H¹(U,M)^{G/U}` when all those hypotheses apply.

**Local-condition preservation is additional.** Identifying Selmer *submodules* instead of entire `H¹` requires local restriction and corestriction to respect the actual chosen local conditions at every decomposition subgroup. In the original Lean proof, this is the work of `selUnit`, `restriction_mem_invariant_H1`, `corInv`, and `relIndex_inf_dvd`; the arithmetic soundness of those imported local conditions is NOT independently proved by the abstract argument.

**Failure if the index is not a unit.** For `G=C_3`, `U=1`, `M=𝔽_3` with trivial action, `H¹(C_3,𝔽_3)=Hom(C_3,𝔽_3)≅𝔽_3`, but `H¹(1,𝔽_3)=0`. Restriction is not injective. Thus discarding `l∤m` can demonstrably destroy the conclusion. This is an exact counterexample to *the unjustified generalized transfer claim*, not to the original qualified theorem.

## Original-source correspondence: precise obligations

The source `eigV` proof uses a representation `rho l e ψ` and a character twist, as opposed to abstract group cohomology alone. Its use in `ML.psiOf` requires the following independently audited bridges:

1. Authenticity of `shaEig` and `LocSel` as the intended geometric/arithmetic local conditions; preservation of the same `Sha` object under `eigV`.
2. The `galOf ℚ E Ω` subgroup is normal/open, is inside the character kernel, and its index is exactly the field degree `[E:ℚ]`. `ML.psiOf` uses `galEmbTop` and `galQuot`.
3. No factor of `l` divides that index, exactly as assumed by `PsiBound`.
4. Valuation comparison `ML.vChar` from `ML.recip`, involving the genuine Bernoulli value `alN`, still needs independent arithmetic validation. Abstract finite-index descent does not provide a valuation bound.

## Executable exact-field fixture

`tests/rh_a26_eigen_transfer_cyclic_h1.py` enumerates cyclic `C_m` actions on one-dimensional `𝔽_p` for `p∈{2,3,5,7,11,13}` and `1≤m≤25`. For valid scalar actions `a^m=1 (mod p)`, all 1-cocycles are `z∈𝔽_p` with `(∑_{i<m}a^i)z=0`; coboundaries are `z=(a−1)b`. The fixture independently checks `Z¹=B¹` whenever `p∤m` and preserves `H¹(C_3,𝔽_3)≠0` as a negative control. **318 valid actions PASS** from the exact GitHub-hosted script, SHA-256 `455a3862365929fc0eebd07b6e8d14c56db18f130a594eef77dd25c9a475a9d0`; CHAD OS-local receipt `a867b22403e74a6f9fa0dbf8d315abeb`. This is a finite model test; the general abstract lemma above is separately proved by averaging and Hochschild–Serre, and neither is original-source Lean replay.

**Disposition:** `RH-A26-D05_PRIME_TO_INDEX_H1_TRANSFER_INDEPENDENTLY_RECONSTRUCTED__LOCAL_SEL_EIGENLENGTH_AND_BERNOULLI_VALUATION_OPEN`. No MATHCERT certification or theorem promotion.
