# BSD-001 R5-RES source audit — literal-p=2 Colmez–Wang determinant-variable repair

## Record

- Campaign: `BSD-001`.
- Provider operation: `grandchallenge/MATHFORGE#248`.
- Downstream objective: continuing `BSD-R5-RES`; historical tracker `grandchallenge/MATHSOLVE#273` remains closed because its witness-based reopening condition is not yet met.
- Exact downstream protected head entering this audit: `grandchallenge/MATHSOLVE@30bd26d970b1e25a42424aeec959e851c4158652`.
- Protected MATHFORGE base: `5f683563d7580eecb3bc5b2582d9a4577cbb4add`.
- Protected predecessor provider record:
  `sources/BSD-001/R5_RES_COLMEZ_WANG_P2_COMPLETED_COHOMOLOGY_SOURCE_AUDIT.md`.
- Claim class: bounded source/applicability evidence only.

## 1. Source identities and continuity lock

Primary source A:

Pierre Colmez and Shanwen Wang, *Une factorisation de la cohomologie complétée et du système de Beilinson-Kato*, immutable arXiv version
`arXiv:2104.09200v2`, dated 27 February 2024.

The audited author PDF is
`https://webusers.imj-prg.fr/~pierre.colmez/KE.pdf`.
The immutable identity for this audit is the arXiv version above; the author URL is an access path, not the immutable identifier.

Primary source B:

Eknath Ghate and Narasimha Kumar, *Control theorems for ordinary 2-adic families of modular forms*, in *Automorphic Representations and L-Functions*, Tata Institute of Fundamental Research Studies in Mathematics 22 (2013), 231–261.

Author access copy:
`https://mathweb.tifr.res.in/~eghate/2adic.pdf`.

Primary source C:

Patrick B. Allen, *Modularity of nearly ordinary 2-adic residually dihedral Galois representations*,
`arXiv:1301.1113v2`, Compositio Mathematica 150 (2014), no. 8, 1235–1346.

Search/reconstruction questions used in this audit:

1. What exact odd-prime algebra enters Colmez–Wang §15.1?
2. Does published 2-adic Hida theory replace it integrally?
3. Does a 2-adic nearly ordinary `R=T` architecture provide the missing full deformation family?
4. Is the later denominator-removal use of `p!=2` logically independent?
5. What is the first deterministic downstream algebraic replay?

No generated computational witness is produced by this provider audit.

## 2. Exact Colmez–Wang prime restriction

At the start of Chapter 15, immediately before the determinant/cyclotomic-variable separation, Colmez–Wang state explicitly:

`On suppose p != 2 dans ce qui suit.`

The restriction governs the proof of Theorem 0.12 after extension to `Fr(T)`.

The relevant odd-prime algebra has two layers.

### 2.1 Finite-character splitting

For odd `p` they write

`Z_p^* = mu_{p-1} x (1+pZ_p)`

and consequently

`Lambda = Lambda_0 tensor Z_p[Gal(Q(mu_p)/Q)]`.

Because the finite factor has order prime to `p`, its group ring decomposes as a direct sum over its characters. This lets the proof reduce `Lambda`-modules to one-variable `Lambda_0`-modules character by character.

At `p=2`, the correct unit decomposition is instead

`Z_2^* = {+1,-1} x (1+4Z_2)`.

The finite factor has order two, equal to the residue characteristic. Therefore

`Z_2[C_2]`

is not the integral semisimple product of its two character rings. The odd-prime direct-sum argument cannot be copied verbatim.

The Colmez–Wang text itself says that inclusion of `p=2` would require additional care.

### 2.2 Square-root descent of the determinant variable

Colmez–Wang §15.1.2 next uses the decomposition

`Z_S^* = Delta x (1+pZ_p)`

with `Delta` of prime-to-`p` type and proves that a continuous character `eta` has a unique factorization

`eta = eta_0 eta_p^2`,

where `eta_0` is finite on the cyclotomic principal-unit direction and `eta_p` is the principal-unit square root.

This yields the factorization

`T_m = Lambda_0 completed_tensor T_0`

and the corresponding descent of the universal representation to fixed determinant.

The algebraic reason this works for odd `p` is that multiplication by two is an automorphism of the pro-`p` character group of `1+pZ_p`.

That exact step fails over the unmodified literal-2 weight coordinate.

## 3. Exact literal-2 weight algebra

Ghate–Kumar develop ordinary Hida theory at `p=2` using

`Gamma = 1+4Z_2`

and

`Lambda = Z_2[[Gamma]]`.

They track the residual finite sign information separately through the mod-4 cyclotomic character.

Their Theorem 8.1 proves the ordinary `p=2` control theorem, and Theorem 9.4 proves that every ordinary 2-stabilized newform occurs in a unique Hida family up to Galois conjugacy.

Thus the following source interface is admitted:

`GHATE_KUMAR_P2_ORDINARY_WEIGHT_COORDINATE_AND_CONTROL`.

In particular, there is no source-level obstacle to using a one-variable ordinary weight algebra at `p=2`.

However this does **not** supply the Colmez–Wang determinant square root.

For

`Gamma = 1+4Z_2`,

the squaring map is not an automorphism of `Gamma`; its image is

`1+8Z_2`.

Hence a general universal character on `1+4Z_2` cannot be divided by two inside the same integral weight algebra.

This last statement is a downstream elementary algebraic fact, not a theorem attributed to Ghate–Kumar.

## 4. Why an ordinary Hida family alone does not repair Chapter 15

Colmez–Wang's analytic-continuation argument uses the full deformation space and the Zariski density of classical points whose local representation at `p` is absolutely irreducible.

The selected BSD lane is good ordinary at two, so its classical local representation is reducible.

A Ghate–Kumar ordinary Hida family through that point remains in the ordinary/reducible local locus. It therefore cannot replace the dense locally irreducible classical points used by Colmez–Wang to extend the comparison to the reducible classical point.

Accordingly:

`P2_HIDA_CONTROL_DOES_NOT_BY_ITSELF_REPLAY_COLMEZ_WANG_FULL_DEFORMATION_ANALYTIC_CONTINUATION`.

This is a scope distinction, not a defect in Ghate–Kumar's theorem.

## 5. Allen's residually dihedral p=2 architecture

Allen proves a 2-adic modularity-lifting theorem for nearly ordinary representations whose residual representation is absolutely irreducible with solvable, hence residually dihedral, image.

The source emphasizes that residual distinguishedness is not assumed. This is important for elliptic curves at `p=2`, where the usual residual ordinary characters cannot be distinguished over `F_2`.

The paper constructs a large deformation ring and a nearly ordinary Hecke algebra, and proves modularity through a 2-adic patching argument.

This supplies a genuine source interface:

`ALLEN_P2_RESIDUALLY_DIHEDRAL_NEARLY_ORDINARY_DEFORMATION_ARCHITECTURE`.

But Allen's local deformation condition at places above two is still reducibility/nearly ordinarity. Therefore it does not supply the nonordinary/full-deformation locus with dense locally absolutely irreducible classical points that Colmez–Wang use for analytic continuation.

Moreover, Allen has a technical condition involving the quadratic field cutting out the residual dihedral representation when that field is CM. This audit does not assert that every selected BSD instance satisfies that auxiliary condition.

Thus Allen is retained as relevant p=2 deformation architecture but not as a direct discharge of the Colmez–Wang bridge.

## 6. The first algebraic repair candidate

The odd-prime factorization

`eta = eta_0 eta_p^2`

suggests two literal-2 repairs.

### Route A — ramified square-root weight cover

Let `Gamma=1+4Z_2` and choose a topological generator `gamma`.
If the universal weight character sends `gamma` to `U`, adjoin a variable `V` subject to

`V^2=U`.

This is a finite integral cover of the ordinary weight algebra, ramified modulo two.

On such a cover a universal half-character exists tautologically. A downstream proof would have to show that the required Colmez–Wang Hecke/deformation modules, completed-cohomology factorization, classical-point density and global-local comparison survive the base change with all integrality statements retained.

No audited source proves this replay.

### Route B — avoid fixed-determinant descent

Theorem 0.12 is formulated over the full Hecke/deformation algebra `T`.
A second possible repair is to re-run the Chapter-15 Poitou–Tate/globalization argument directly over `T`, keeping the cyclotomic determinant variable instead of replacing `T` by

`Lambda_0 completed_tensor T_0`.

This would avoid the universal square root, but the source proof is organized after the `T_0` descent. A downstream proof must reconstruct all density, torsion-obstruction and specialization steps over the unreduced parameter space.

Again, no audited source supplies this replay as a theorem.

## 7. Theorem 17.10 is a separate literal-2 replay

Colmez–Wang Theorem 17.10 removes denominators and obtains the integral family Kato element.

Its proof explicitly says that, because `p!=2`, `Z_p^*` is procyclic, and chooses one generator in the Ash–Stevens argument.

At `p=2`,

`Z_2^* = {+1,-1} x (1+4Z_2)`

is not procyclic.

This is a second literal-2 issue. It is logically later than the determinant-variable descent: Proposition 15.28 already constructs the required global multiple before Theorem 17.10 removes the remaining poles.

A plausible replay would use a finite generating set for `Z_2^*` and intersect the corresponding no-kernel conditions, but that argument is not contained in the audited sources and is not promoted here.

Record the later independent obligation:

`MISSING_P2_COLMEZ_WANG_DENOMINATOR_REMOVAL_WITH_NONPROCYCLIC_UNITS`.

## 8. Exact provider disposition

The broad predecessor boundary

`MISSING_P2_REDUCIBLE_ORDINARY_COMPLETED_COHOMOLOGY_TO_KATO_INTEGRAL_SPECIALIZATION`

is sharpened.

Published literal-2 Hida theory resolves the existence of a correct one-variable ordinary weight coordinate, and Allen resolves important p=2 nearly ordinary deformation issues including residual nondistinguishedness.

Neither supplies the exact family construction used by Colmez–Wang.

The first downstream theorem obligation on this route is therefore:

`MISSING_P2_COLMEZ_WANG_DETERMINANT_SQUARE_ROOT_DESCENT_OR_FULL_T_GLOBALIZATION`.

Provider disposition:

`QUALIFIED_P2_HIDA_AND_DEFORMATION_ARCHITECTURE_WITH_COLMEZ_WANG_DETERMINANT_DESCENT_GAP`.

If that first obligation is closed, the next independent obligation is the Theorem-17.10 non-procyclic-unit replay recorded above.

## 9. Ruled-out shortcuts

The following routes were checked and are not sufficient as stated.

1. **Use the ordinary Hida family directly.**  
   Insufficient because it remains in the locally reducible ordinary locus and does not reproduce the dense locally irreducible classical points used by Colmez–Wang.

2. **Use Allen's nearly ordinary `R=T` architecture directly.**  
   Insufficient for the same local-locus reason; it is a nearly ordinary/reducible deformation problem.

3. **Pretend `Z_2^*=1+2Z_2` is a one-variable procyclic group and divide characters by two.**  
   False integrally. The correct principal one-variable group is `1+4Z_2`, and squaring does not map it onto itself.

4. **Infer Kato mod-2 nonvanishing from completed-cohomology injectivity before the bridge is repaired.**  
   Still unauthorized.

## 10. Deterministic next evidence action

After protection of this provider record:

1. rebind live MATHSOLVE and MATHFORGE protected heads;
2. in MATHSOLVE, prove the exact elementary literal-2 weight-cover algebra:
   - `Z_2^*={+1,-1}x(1+4Z_2)`;
   - squaring maps `1+4Z_2` isomorphically onto `1+8Z_2`;
   - construct the minimal finite flat square-root cover of the universal `1+4Z_2` character;
3. test, one dependency at a time, which Colmez–Wang §15 constructions commute with that cover;
4. if a material source theorem is needed for full-deformation density or completed-cohomology base change, return source-first to MATHFORGE rather than importing it silently;
5. do not reopen R5-RES until an actual protected residual witness satisfies its historical reopening condition.

## 11. Firewall

This audit does not establish:

- the literal-2 Colmez–Wang family Kato comparison;
- a nonzero residual modular-symbol component;
- `c_Q^Kato mod 2 != 0`;
- `R5_RES_ESTABLISHED`;
- `R5_PRIM_ESTABLISHED`;
- D2d;
- BSD-R2-A1;
- novelty or priority;
- public certification;
- MATHCERT certification.
