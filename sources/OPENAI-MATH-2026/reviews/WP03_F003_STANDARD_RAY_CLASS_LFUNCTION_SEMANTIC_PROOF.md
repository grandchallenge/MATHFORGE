# OAI-26 F003 — fixed-modulus ray-class and analytic Hecke-\(L\) semantic correspondence

**Record:** `GCL-OAI26-F003-STANDARD-RAY-CLASS-SEMANTICS/1`  
**Outcome:** `MATHEMATICAL_FIXED_MODULUS_RAY_CORRESPONDENCE_DERIVED__FORMAL_CORRESPONDENCE_ASSEMBLED_FROM_EXISTING_PROOFS__FULL_PAPER_ADJUDICATION_OPEN`  
**Source pin:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`; upstream tree `45074722c918576d65b4c8be9686c76f508ba696`; Lean 4.34.1, Lake manifest SHA-256 `cf6105a25d9dca2f166b241d9191bd12c7e13305890dc9c4d0952351cccc0794`.  
**Protected predecessor:** `grandchallenge/MATHFORGE@1f9f2926c313c66874456eff5d952b53059a8464` (PR #588); already admitted F003 source-specific finite ray bridges and pinned compilation precede this report.  
**Statement source:** `preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`, pinned Git blob `268c4e3206d460c617d3d2129742a72b831b3def`; read directly, NOT inferred from the declaration title. Lines 50–64 explicitly define a finite-order Hecke character modulo a nonzero integral ideal as a **character of the ray class group modulo that ideal extended by zero to noncoprime ideals**, with \(L_F(s,\eta)=\sum_{\mathfrak a\ne0}\eta(\mathfrak a)/(N\mathfrak a)^s\) for \(\Re s>1\). Lines 1455–1471 give the residue-character lattice theta representation with the six global units. Lines 6705–6754 distinguish primitive and imprimitive presentations and finite deleted Euler factors.

## 1. Elementary exact sequence and the genuinely intended domain

Let \(F=\mathbb Q(\sqrt{-3})=\mathbb Q(\zeta_3)\), \(\mathcal O=\mathbb Z[\zeta_3]\), and let \(\mathfrak f\ne0\) be any integral ideal, *including the unit ideal*. The source's `Hecke/Family.lean`, blob `3d87da47cd57f0a4f11859c654e3e3202a519100`, uses `K := CyclotomicField 3 ℚ` and `O := NumberField.RingOfIntegers K`; the pinned `Hecke/IdealBridge.lean` instantiates `IsPrincipalIdealRing O := IsCyclotomicExtension.Rat.three_pid K`. Thus the mathematical \(\mathcal O\) is a PID and the ordinary ideal class group \(\mathrm{Cl}(\mathcal O)\) is trivial.

Define

* \(F_{\mathfrak f}^{\times}:=\{x\in F^\times:v_{\mathfrak p}(x)=0 \text{ for every }\mathfrak p\mid\mathfrak f\}\).
* \(F_{\mathfrak f,1}^{\times}:=\{x\in F_{\mathfrak f}^{\times}:x\equiv1\bmod\mathfrak f\}\), congruence taken in the localizations at the primes dividing \(\mathfrak f\).
* \(\mathcal I_{\mathfrak f}\): group of nonzero fractional ideals with valuation zero at every \(\mathfrak p\mid\mathfrak f\).
* \(\mathrm{Cl}_{\mathfrak f}:=\mathcal I_{\mathfrak f}/\{(x):x\in F_{\mathfrak f,1}^{\times}\}\), the *ordinary finite ray class group*. No real-place sign condition occurs, since \(F\) has no real embeddings.

**Lemma A — explicit fixed-modulus ray-class isomorphism.**
\[
\boxed{\quad\mathrm{Cl}_{\mathfrak f}(F)\ \simeq\
   (\mathcal O/\mathfrak f)^\times/\operatorname{im}
   \bigl(\mathcal O^\times\to(\mathcal O/\mathfrak f)^\times\bigr).\quad}
\]

**Proof (both directions, including the kernel).**
1. Reduction of locally integral units defines \(\mathrm{red}_{\mathfrak f}:F_{\mathfrak f}^{\times}\to(\mathcal O/\mathfrak f)^\times\). For \(x=a/b\), one may choose \(a,b\in\mathcal O\) both coprime to \(\mathfrak f\), and set \(\mathrm{red}(x)=\bar a\bar b^{-1}\); this is well-defined. The kernel is exactly \(F_{\mathfrak f,1}^{\times}\). This reduction is surjective: a unit residue has a lift \(a\in\mathcal O\) coprime to \(\mathfrak f\), and \(a\ne0\) may always be chosen (for \(\mathfrak f=\mathcal O\), use \(a=1\)).
2. Every fractional ideal of \(\mathcal I_{\mathfrak f}\) has a generator \(x\in F_{\mathfrak f}^{\times}\) because \(\mathcal O\) is principal. The kernel of \(x\mapsto(x)\) is precisely \(\mathcal O^\times\). Thus \(\mathcal I_{\mathfrak f}\simeq F_{\mathfrak f}^{\times}/\mathcal O^\times\).
3. Divide this isomorphism by the principal ray subgroup (image of \(F_{\mathfrak f,1}^{\times}\)). The third isomorphism theorem gives
   \[
   \mathrm{Cl}_{\mathfrak f}\simeq
   F_{\mathfrak f}^{\times}/(\mathcal O^\times F_{\mathfrak f,1}^{\times})
   \simeq(\mathcal O/\mathfrak f)^\times/\mathrm{red}_{\mathfrak f}(\mathcal O^\times).
   \]
   Equivalently, the forward map sends a coprime fractional ideal \((x)\) to the residue class of \(x\) modulo the image of global units; its inverse takes a unit residue \(\bar a\) to the ray class of \((a)\). The preceding kernel computations prove both choices are immaterial. QED.

This elementary argument is the class-number-one specialization of Milne, *Class Field Theory*, Chapter V, **Theorem 1.5**, which gives \(0\to U/U_{\mathfrak f,1}\to F_{\mathfrak f}^{\times}/F_{\mathfrak f,1}^{\times}\to \mathrm{Cl}_{\mathfrak f}\to\mathrm{Cl}(\mathcal O)\to0\), and \(F_{\mathfrak f}^{\times}/F_{\mathfrak f,1}^{\times}\simeq(\mathcal O/\mathfrak f)^\times\). Independent source: https://www.math.ucsd.edu/~csorense/teaching/math204B_W19/Milne_CFT.pdf (Chapter V, §1, Ray Class Groups). **The paper's own definition and the elementary PID computation—not a conjectural Hecke bridge—are enough for this domain correspondence.**

## 2. Entire finite-ray character dictionary, including the conductor's zero extension

Take complex-valued multiplicative characters \(\eta:\mathrm{Cl}_{\mathfrak f}\to\mathbb C^\times\). By Lemma A, they correspond **bijectively** to group homomorphisms
\[
\psi:(\mathcal O/\mathfrak f)^\times\longrightarrow\mathbb C^\times,\qquad
\psi(\bar u)=1\quad(u\in\mathcal O^\times).
\]
All such characters have finite image because the quotient group is finite.

Extend \(\psi\) to a multiplicative character \(\widetilde\psi\) of the **whole finite residue ring** \(R=\mathcal O/\mathfrak f\): put \(\widetilde\psi(r)=\psi(r)\) when \(r\in R^\times\) and \(\widetilde\psi(r)=0\) otherwise. This extension is multiplicative: in a commutative ring a product is a unit iff both factors are units. Conversely, a `MulChar R ℂ` restricts to a unit-group homomorphism and vanishes on nonunits, and global-unit triviality yields a character of the quotient. The unit-ideal edge case \(R=\{0=1\}\) simply produces the trivial character and has **no nonunits**. There is no extra finite-order restriction to add: the domain of the unit-group character is finite.

**The precise source formal counterparts already exist:**

* `RayOrthogonality.lean:globalUnits` and `:rayCharacters`, blob `1f6e3be50cf095a0f91f241d182bf393b9b3b7ab`, define \(\mathrm{im}(\mathcal O^\times)\) and the subgroup of residue `MulChar` trivial there. `:mem_rayCharacters_iff` proves precisely the global-unit condition.
* GCL independent Lean `sources/OPENAI-MATH-2026/formal/F003IndependentRayQuotient.lean`, blob `1e6f0c0998b0073d9b6966981f741836d0fc0533`, explicitly constructs the **two-sided equivalence** `rayCharacterEquiv` between homomorphisms \((R^\times/H)\to\mathbb C^\times\) and unit-trivial `MulChar R ℂ`, plus `fromQuotient_nonunit_zero`. Exact protected run [44520596357](https://github.com/grandchallenge/MATHFORGE/actions/runs/44520596357) is `completed/success` (read back this session).
* `Hecke/Family.lean:Character` packages **exactly** a nonzero ideal modulus, a `MulChar (O ⧸ modulus) ℂ`, the global-unit triviality, and an auxiliary positive integer period lying in the modulus. `Character.ofResidue` constructs this package for **every** such residue character, using the quotient ring's finite cardinal. In particular, the period is a *presentation device*, not an additional ray character.
* `Hecke/RayFamily.lean:character`, blob `5d7d3f9ca263d8165393e4b35b3c4dc1354565f7`, maps the source's full `rayCharacters M` into a formal `Character` by `ofResidue`. Conversely, for any formal \(\chi\), take \(M=\chi.\mathrm{modulus}\) and the ray-subtype member \(\langle\chi.\mathrm{residue},\chi.\mathrm{unit\_trivial}\rangle\); this has **the same element coefficient at every \(z\in\mathcal O\)** by unfolding `elementCoeff`, `RayFamily.character`, and `ofResidue`. This inverse is a direct definitional-level mathematical reconstruction, **not** a new compiled Lean lemma, and does not identify two structure records with different auxiliary periods.
* GCL `F003PeriodAndRayBridge.lean`, blob `f28199b3653bd2eeee1d6d5a3ef20de0f56c599b`, proves `gcl_LFunction_eq_of_elementCoeff_eq` for \(0<\Re s,\ s\ne1\), plus `gcl_LFunction_period_choice_immaterial`, and a separate exact ray ideal-series equality. Protected workflow [44507526666](https://github.com/grandchallenge/MATHFORGE/actions/runs/44507526666) is `completed/success` (read back this session). The pair of previous formal modules was read **directly**, not inferred from test names alone.

**Consequence:** within the paper's *fixed-modulus ray-class definition*, there is no missing finite-order-character species in the formal `Character` **because \(\mathcal O\) has class number one**. This is a mathematically justified fixed-modulus completeness statement, not yet an end-to-end Lean theorem stating the exact ray-class-group isomorphism from the classical ideal group.

## 3. Coefficient-by-coefficient equality, not merely a name match

Let \(I\) be a nonzero integral ideal and let \(\eta\) be the ray character corresponding to \(\widetilde\psi\) as above.

* If \(I\) is coprime to \(\mathfrak f\), write \(I=(a)\) with \(a\ne0\). Then \(a\) is a unit modulo \(\mathfrak f\), and the paper's \(\eta(I)\) equals \(\psi(\bar a)\). Choosing \(a'=ua\) with \(u\in\mathcal O^\times\) does not change this value by unit triviality. The pinned `IdealCharacter.ofResidue_span`, blob `b07c7b3e309678863c8d3161a0e3cbadf307cefc`, and `Hecke/IdealBridge.lean:idealCoeff_span` prove that the source's `idealCoeff χ I` is **exactly** this same value.
* If \(I\) is *not* coprime to \(\mathfrak f\), its generator is a **nonunit residue**, so \(\widetilde\psi(\bar a)=0\), matching the manuscript's explicit zero extension. The pinned `IdealCharacter.isUnit_mk_iff_isCoprime` and `MulChar.map_nonunit` give this case. (The irrelevant zero ideal is also assigned coefficient zero by `idealCoeff_zero`.)
* Both descriptions are multiplicative on ideals; no extra generator choices, unproved norm phases, or loss factors intervene.

Thus the complete ideal coefficient functions are identical at **every integral ideal** for the same chosen modulus, including primes artificially appended to an imprimitive modulus.

## 4. Equality of analytically continued \(L\)-functions in the target half-plane

On \(\Re s>1\), the manuscript's *definition* (paper.tex 59–64) is
\[
L_F(s,\eta)=\sum_{0\ne I\subset\mathcal O}\eta(I)N(I)^{-s}.
\]
The pinned source `Hecke/IdealBridge.lean:continuedLattice_eq_six_ideal_tsum` and `:LFunction_eq_ideal_tsum` (blob `bcb15758326db111dd0b007b79a58103a4fa659e`) prove
\[
L_{\rm formal}(s,\chi)=\frac{\mathrm{continuedLattice}(\chi,s)}6
  =\sum_{I}\frac{\mathrm{idealCoeff}(\chi,I)}{N(I)^s},
\]
and `Hecke/Euler.lean:LFunction_eq_series` (blob `e5a4790fbd39d41b27c04efe8cfd45d238c189aa`) identifies the Euler/ideal-series presentation on that half-plane. The 6 is exactly the **six units** in \(\mathcal O^\times\): each nonzero ideal has six generators, as the paper says in paper.tex 1455–1471. It does not create a new scalar zero or change normalization.

For \(D=\{s\in\mathbb C:\Re s>0,\ s\ne1\}\), the source's `Hecke/IdealBridge.lean:LFunction_differentiableAt` proves the formal function is holomorphic at each \(s\in D\) (since \(s\ne0,1\)), while `:LFunction_entire_nonprincipal` proves more for nonprincipal characters. The paper's \(L_F\) is, by its explicit definition, the meromorphic continuation of the same Dirichlet series; on \(D\) it is holomorphic. The domain \(D\) is connected, and \(\Re s>1\subset D\) is a nonempty open subset. **Uniqueness of analytic continuation (identity theorem)** therefore gives
\[
\boxed{\quad L_{\rm formal}(s,\chi)=L_F(s,\eta)
 \quad\text{for every }\,\Re s>0,\ s\ne1.\quad}
\]
In particular the strict \(7/8\) region away from the allowed principal pole is included. This inference is a rigorous *mathematical argument combining the source's kernel-checked equalities with the manuscript's standard-analytic definition*, **not** a newly compiled Lean bridge to a separate external `HeckeCharacter` definition.

The same-modulus principal/nonprincipal predicate is exact: the ray character is trivial iff the unit-group quotient character is trivial iff \(\chi.\mathrm{residue}=1\); this matches `Hecke/RayFamily.lean:principal_iff`. The theorem's exception is exactly principal and \(s=1\), not every \(s=1\).

## 5. Change of modulus, primitive induction, and Euler-factor nonvanishing

The manuscript intentionally distinguishes **primitive conductor** from **defining modulus/zero-extension support**. An imprimitive character on modulus \(\mathfrak f\), induced by a primitive character of conductor \(\mathfrak f_0\mid\mathfrak f\), has
\[
L_{\mathfrak f}(s,\eta)=L_{\mathfrak f_0}(s,\eta^*)
  \prod_{\substack{\mathfrak p\mid\mathfrak f\\\mathfrak p\nmid\mathfrak f_0}}
    \left(1-\eta^*(\mathfrak p)(N\mathfrak p)^{-s}\right).
\]
This follows by Euler products on \(\Re s>1\), then meromorphic uniqueness. Every factor is nonzero when \(\Re s>0\): for each prime \(N\mathfrak p\ge2\) and \(|\eta^*(\mathfrak p)|\le1\),
\[
|\eta^*(\mathfrak p)(N\mathfrak p)^{-s}|
 \le (N\mathfrak p)^{-\Re s}<1.
\]
Consequently **imprimitive presentations cannot create zeros** in the target region. This justifies the manuscript's paper.tex 171–177 and 6715–6754 conventions, without asserting a false equality of primitive and imprimitive \(L\)-functions. The *fixed-modulus* coefficient equivalence in §3 is exact; changing modulus requires these explicit finite Euler factors.

A continuous finite-order idele-class character has trivial complex archimedean component because \(\mathbb C^\times\) is connected and a continuous map into a finite group is constant there. Its finite-component kernel contains a sufficiently deep congruence subgroup for some finite modulus; diagonal \(F^\times\)-invariance imposes global-unit triviality. Thus the usual finite-order idelic convention reduces to the paper's *finite-ray-class* convention, as the paper explicitly states (paper.tex lines 52–57). This paragraph invokes standard global class-field/local-topology theory; it is **not independently formalized in this GCL Lean proof**.

## 6. Adversarial conditions and exact trust boundary

1. **Would class number \(>1\) break the bridge?** Yes. For a general number field, \((\mathcal O/\mathfrak f)^\times/\mathrm{im}(\mathcal O^\times)\) is only the kernel of \(\mathrm{Cl}_{\mathfrak f}\twoheadrightarrow\mathrm{Cl}\), not the whole ray group. In *this* field the source has an explicit PID instance, eliminating that obstruction. Reusing this result for non-PID number fields would be an invalid generalization.
2. **Would using primitive conductors instead of the supplied moduli preserve exact coefficients?** No. Deleted Euler factors must be accounted for. §5 respects the actual zero-extended representation; no arbitrary mask is dropped. The factor nonvanishing requires \(\Re s>0\), not a claim about the whole complex plane.
3. **Would replacing the formal \(L\)-function by an unproved identically-named function suffice?** No. The actual source proves its six-to-one lattice/ideal equality on \(\Re s>1\) and analytic continuation on the region of interest. The manuscript defines the external function by precisely that ideal Dirichlet series and continuation. The identity theorem is essential.
4. **Could a nontrivial finite-order infinity-type be missing?** Not for the *continuous finite-order* characters stipulated by the paper over the one-complex-place field \(F\). The connectedness argument excludes them. Infinite-order Grössencharacters are outside the paper's claim and source's formal character type.
5. **Does this prove the seven-eighths theorem independently?** No. It verifies the mathematics of the **character/\(L\)-function dictionary**, conditional on the already kernel-checked source equalities and the standard ray-class/analytic-continuation definitions. It does not rederive the high-radius Gaussian energy estimates, the detector's uniform conductor bounds, the entire 199-page analytic argument, the October 1/5 editions, or novelty.
6. **Is a classical ray-class isomorphism now separately Lean-kernel-checked?** No. The full \(\mathrm{Cl}_{\mathfrak f}\simeq R^\times/U\) ideal-class construction and the idelic-to-ray bridge in §1 and §5 are independently written mathematical derivations here, not newly compiled Lean. The **abstract quotient-to-MulChar** correspondence, lattice-period invariance, formal ideal-series equality and final zero-free statements *have* their separately admitted pinned source/Lean checks.

## Disposition

**Mathematically resolved within the manuscript's stated convention:** Every finite-ray character over \(F=\mathbb Q(\sqrt{-3})\) and fixed nonzero modulus is represented by a unit-trivial residue character of the precise formal type; their zero-extended ideal coefficients agree; their continued \(L\)-functions agree on \(\Re s>0\) away from \(s=1\); imprimitive Euler-factor deletions introduce no zeros in that region. This is a **mathematical definition-correspondence proof**, *not* a new analytic nonvanishing theorem.

**Still open:** explicit Lean formalization/replay of the *classical ideal ray-class group* isomorphism (as opposed to GCL's already replayed abstract unit quotient), a separate complete idèle-character implementation/bridge if required for formal semantic closure, and **independent audit of the source's extraordinary analytic seven-eighths proof and manuscript variants**. No MATHCERT certification and no automatic family-level promotion.

```text
RESULT/1
ASSIGNMENT_ID: GCL-OAI26-WP03-F003-RAY-SEMANTICS
PIN: openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a
MATH: FIXED_MODULUS_RAY_CLASS_ISOMORPHISM_AND_L_CORRESPONDENCE_DERIVED
ALREADY_LEAN_REPLAYED: 44520596357; 44507526666; F003 final targets 43/145/199
NEW_LEAN_PROOF: NONE
FAMILY_WIDE: SOURCE_ANALYTIC_AND_OTHER_EDITIONS_UNRESOLVED
MATHCERT: NONE
```
