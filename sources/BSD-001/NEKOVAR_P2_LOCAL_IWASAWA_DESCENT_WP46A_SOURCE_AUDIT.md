# BSD-001 source audit — Nekovář local Iwasawa descent at literal `p=2`

## Record

- Campaign: `BSD-001`.
- Downstream operation: `BSD-R2-A1-WP46A-STRICT-KUMMER-POSTNIKOV-OBSTRUCTION`.
- Protected MATHFORGE predecessor: `d7114e8c61ff0fb414e95a162800a7199f1dec0a`.
- Protected MATHSOLVE predecessor: `5f7ea71f2d86457575b2bc2f1e8c281f09ce4b87`.
- Primary source: Jan Nekovář, *Selmer complexes*, Astérisque 310 (2006), Chapter 8, especially Proposition 8.4.8.1 and Corollary 8.4.8.2 in the final numbering.
- Official bibliographic identity: DOI `10.24033/ast.717`, NUMDAM item `AST_2006__310__R1_0`.
- Text checked against a searchable transcription of the final Astérisque version; the official source identity is already protected by earlier BSD-001 Nekovář audits.
- Disposition: `QUALIFIED_LITERAL_P2_LOCAL_IWASAWA_DESCENT`.
- Claim class: bounded source/formalism admission only; no strict/Kummer lift, BSD, or certification promotion.

## Source-access note

The searchable final-version transcription exposes the complete Chapter-8 descent statement and the surrounding prime conventions. The official large NUMDAM PDF is not reliably materializable by the present renderer. An independent page-image check was also attempted against the Benois–Berger paper that cites the prepublication version of the same result; the screenshot backend failed with a cache error. No page-image lock or independently recomputed PDF digest is claimed.

Benois–Berger is **not** used as the prime-range authority here: that paper globally assumes `p` odd. It is used only as a bibliographic cross-check that its local-Iwasawa proposition is cited as a special case of Nekovář's Chapter-8 result.

## Exact downstream question

Protected WP46A reduces the missing strict-to-Kummer Iwasawa comparison to the ordinary local higher cohomology module

`Z_w^str := H^2(U_{w,infty}^{+,str})`.

At `w|2` the strict Greenberg local condition is the Iwasawa cochain complex attached to the ordinary sublattice `T_w^+`. Downstream needs a literal-`p=2` descent theorem relating Iwasawa cohomology of `T_w^+` to finite-layer local cohomology, without importing an odd-prime theorem.

The narrow query is:

> In Nekovář's general Iwasawa formalism, for `Gamma ~= Z_p`, is derived augmentation to a finite/base layer exact in the stated sense and does it yield the short exact descent sequences
>
> `0 -> H_Iw^j(T)_Gamma -> H^j(T) -> H_Iw^{j+1}(T)^Gamma -> 0`,
>
> with no hypothesis `p>2`?

The final Chapter-8 source answers this affirmatively.

## Prime range

Chapter 8 is formulated for a complete local noetherian coefficient ring with finite residue field of characteristic `p` and a pro-`p` Iwasawa group. The general setup does not impose `p != 2`.

The same final volume explicitly distinguishes the `p=2` cyclotomic convention in its general Iwasawa setup: where the usual cyclotomic parameter is `q=p` for `p!=2`, it uses `q=4` for `p=2`. Separate later parity results add `p!=2` only where required; no such restriction appears in Proposition 8.4.8.1 or Corollary 8.4.8.2.

Thus the Chapter-8 descent statement is a literal `p=2` formal theorem. No odd-prime specialization is made downstream.

## Proposition 8.4.8.1 — derived augmentation/descent

In the source notation let `G` be the relevant profinite Galois group, `H` the subgroup corresponding to the Iwasawa extension, and

`Gamma=G/H ~= Z_p^r`.

For an admissible finite-type complex `T`, Proposition 8.4.8.1(ii) gives a canonical derived augmentation isomorphism

`RΓ_Iw(G,H;T) derived_tensor_R R_base ~= RΓ_cont(G,T)`,

where the tensor product is taken through the augmentation map of the Iwasawa algebra.

The proof is explicit: for topological generators `gamma_i`, the elements `gamma_i-1` form a regular sequence and the source iterates the two-term augmentation complexes before identifying the result with base Galois cohomology.

This is the same derived augmentation mechanism already used on the protected strict side in WP43A, now source-bound in the general Chapter-8 descent form needed for local higher cohomology.

## Corollary 8.4.8.2 — one-variable short exact sequences

For

`Gamma ~= Z_p`,

Corollary 8.4.8.2(i) states that the descent spectral sequence degenerates to short exact sequences. In adapted cohomological notation:

`0 -> H_Iw^j(G,H;T)_Gamma
   -> H_cont^j(G,T)
   -> H_Iw^{j+1}(G,H;T)^Gamma
   -> 0`.

The statement is formal for the one-variable Iwasawa group and carries no odd-prime restriction.

The same construction applies after replacing the base by an open subgroup `Gamma_n`; Proposition 8.4.8.3 and Corollary 8.4.8.4 give the corresponding finite-layer descent statement.

## Exact bounded interface admitted downstream

After protection, MATHSOLVE may use the following statements for the selected local cyclotomic `Z_2` tower.

1. For a finite free `Z_2` Galois lattice `T'`, the local Iwasawa cochain complex has canonical derived augmentation to every finite layer.
2. For every finite layer `F_n` and every cohomological degree `j`, one has the exact one-variable descent sequence

   `0 -> H_Iw^j(F_0,T')_{Gamma_n}
      -> H^j(F_n,T')
      -> H_Iw^{j+1}(F_0,T')^{Gamma_n}
      -> 0`.

3. If the local Iwasawa complex has no cohomology in degree `3`, then

   `H_Iw^2(F_0,T')_{Gamma_n} ~= H^2(F_n,T')`.

4. These statements apply literally with `p=2` and `T'=T_w^+` in the protected good-ordinary lane.

Finite-layer local Tate duality and the already-protected WP39 ordinary quotient normalization remain separate protected inputs; this audit does not re-admit or alter them.

## Downstream consequence that is permitted but not proved here

Because `K_{infty,w}/K_w` is totally ramified and the ordinary discrete quotient `A_w^-` is unramified, MATHSOLVE may combine the above descent theorem with its protected finite-layer local-duality calculation. If the finite groups

`H^2(K_{n,w},T_w^+)`

are thereby shown to have the same order at every layer, the downstream proof may use the constant finite coinvariant sizes to determine the structure of `H_Iw^2(K_w,T_w^+)`. That determination is a MATHSOLVE theorem obligation, not a source assertion made by this audit.

## What this source does not establish

This audit does not prove:

- a value or module structure for `H_Iw^2(K_w,T_w^+)`;
- vanishing of the WP46A Postnikov obstruction;
- existence or uniqueness of a strict-to-Kummer Iwasawa comparison lift;
- `B_w^Kum=0`;
- cancellation of the formal universal-norm term;
- any height nondegeneracy statement;
- D1c or the remaining Disegni/WP00/descent normalizations;
- `BSD-R2-A1`;
- theorem novelty, priority, or MATHCERT certification.

## Provider conclusion

Nekovář's final Chapter-8 descent formalism supplies the exact one-variable local Iwasawa derived augmentation and short exact finite-layer descent sequences needed by WP46A, literally at `p=2`.

**Disposition:** `QUALIFIED_LITERAL_P2_LOCAL_IWASAWA_DESCENT`.

The downstream mathematical work must still compute the ordinary strict `H^2` module and the resulting Postnikov obstruction exactly.