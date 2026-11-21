# OAI-26 F003 — independent native mathlib Hecke model: exact conductor-normalization contract

**Record:** `GCL-OAI26-F003-NATIVE-MATHLIB-HECKE/1`.  
**Disposition:** `NEW_NATIVE_IDELE_HECKE_IMPLEMENTATION_FOUND__IMPRIMITIVE_UNCORRECTED_EQUALITY_REFUTED__CORRECT_EULER_CONTRACT_DERIVED__EXTERNAL_GLOBAL_BRIDGE_OPEN`.  
**Do not duplicate:** GCL previously proved the paper-level idèle/ray character reduction, and tested an exact quartic residue character and its imprimitive Euler deletion. See existing protected `WP03_F003_EXTERNAL_IDELE_RAY_AND_QUARTIC_EULER.md` (blob `37e53ef12e3c6255a4fe1e66c8d8f18a86ab9a54`) and PRs #567/#568. This report's **new evidence** is the previously unavailable, independently implemented native mathlib idèle-character Euler-product target and its precise comparison contract. No new claim of inventing the standard class-field-theory dictionary.

## Exact immutable source identities

**Source A: pinned OAI project under review**

- `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`, `lean/OAI/NumberTheory/DirichletL/Hecke/IdealBridge.lean`, Git blob `bcb15758326db111dd0b007b79a58103a4fa659e`.
- `Hecke/Family.lean`, blob `3d87da47cd57f0a4f11859c654e3e3202a519100`; `Hecke/FamilySeries.lean`, blob `445b25ae3b9c13d59ee0ac03c5c8d8b6777970d2`; `Hecke/Euler.lean`, blob `e5a4790fbd39d41b27c04efe8cfd45d238c189aa`.
- The project uses Lean `v4.34.1` and locked mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. At that **exact** mathlib commit, `Mathlib/NumberTheory/NumberField/HeckeLFunction.lean` does **not** exist (provider content lookup 404). Never assert that the native idèle-character code was available in the pinned upstream.
- GCL protected mathematical witness `f003_quartic_ray_euler_adversary.py` (blob `26159b1bb427dd5dd55ff8c31a139882c5e55146`) and the existing protected F003 external-idèle review give a modulus-\(5\) nontrivial ray character, exact Euler values and an imprimitive modulus-\(10\) comparison.

**Source B: independent native mathlib implementation, introduced November 15, 2026**

- `leanprover-community/mathlib4@6e96f3e25b9b23468a6f155342b5a1e5e33ac8f9`, `Mathlib/NumberTheory/NumberField/HeckeLFunction.lean`, Git blob **`9dcd9a2a11f1407d47b9b0a1000259d237bdfe64`**, 5,183 source characters, toolchain **`leanprover/lean4:v4.36.0-rc2`**.
- Author: Thomas Browning; genuine independent mathlib code, not another `OAI` namespace alias or GCL redefinition. Its type is `NumberField.HeckeCharacter R K := (IdeleClassGroup R K) →ₜ* ℂ`. The source expressly qualifies the mathematical interpretation by the required `[IsIntegralClosure ℤ R K]` and `[NumberField K]` assumptions. Our intended specialization takes \(R=\mathcal O_F\), \(K=F\), satisfying the number-field conditions.
- `χ.restrict v` is its local multiplicative character. `χ.IsUnramifiedAt v` tests triviality on local integer units. `χ.localValue v` evaluates at a uniformizer.
- `χ.localPolynomial v` is **`1 − C (χ.localValue v) * X`** when unramified, otherwise **`1`**. `χ.localPowerSeries v` is its inverse; `χ.localEulerFactor v` is the corresponding arithmetic function. `χ.LFunction` is a **natural-number-indexed `ArithmeticFunction ℂ`** assembled by `ArithmeticFunction.eulerProduct`, not the complex-valued meromorphic function `OAI.SevenEighths.HeckeFamily.LFunction`. `χ.LSeries s := LSeries χ.LFunction s` is its complex Dirichlet series.
- The new file **does not itself prove** a map from fixed-modulus ray characters to `IdeleClassGroup` characters, local value matching, equality of the resulting global Euler series with the OAI lattice continuation, or analytic continuation of `χ.LSeries` into \(\Re s>7/8\). Absence from this one file is not proof that mathlib's wider codebase lacks any related theorem.

## Exact normalisation theorem — the right comparison, not a false bare equality

Let \(\mathfrak m\ne0\) be the **defining zero-extension modulus** of a formal OAI `HeckeFamily.Character` \(\eta_{\mathfrak m}\), and let \(\xi\) be a **continuous finite-order** native idèle-class character for the *same underlying ray class character* (not a character merely matching the group order). Suppose the **orientation-specific local matching** holds: for each prime ideal \(\mathfrak p\nmid\mathfrak m\), \(\xi\) is unramified at \(\mathfrak p\) and
\[
  \xi_{\mathfrak p}(\varpi_{\mathfrak p})
    =\eta_{\mathfrak m}(\mathfrak p).
\]
Put \(E_{\mathfrak p}(s)=1-\xi_{\mathfrak p}(\varpi_{\mathfrak p})(N\mathfrak p)^{-s}\) at any unramified prime, and \(E_{\mathfrak p}(s)=1\) if \(\xi\) is ramified there. Then the **correct mathematical absolute-convergence-domain contract** is
\[
\boxed{\quad
  L_{\mathrm{OAI},\mathfrak m}(s)
  =L_{\mathrm{native}}(\xi,s)
    \prod_{\substack{\mathfrak p\mid\mathfrak m\\
                      \xi\ {\rm unramified\ at}\ \mathfrak p}}
      \left(1-\xi_{\mathfrak p}(\varpi_{\mathfrak p})
                 (N\mathfrak p)^{-s}\right),
  \qquad\Re s>1.
\quad}
\]
Here `L_native` is the conventional Euler product represented by the *new* mathlib arithmetic Euler factor specification. At \(\mathfrak p\nmid\mathfrak m\) the local Euler polynomials coincide by the **required** local matching hypothesis. At \(\mathfrak p\mid\mathfrak m\), the OAI defining-modulus zero extension deletes the local factor, independently of whether \(\xi\) is actually ramified; the native polynomial is already \(1\) if ramified and must be multiplied by its polynomial if unramified. Absolute convergence for \(\Re s>1\) then proves the product identity. This proof **does not** assume the requested global idèle-to-ray map: its existence and local normalization are *explicit hypotheses still requiring a separately checked cross-implementation implementation*. The coefficient-to-Euler-product representation in the native implementation is taken from its **actual definitions**, not claimed as a newly replayed Lean global identity.

The correction factor has no zeros for \(\Re s>0\) when the character is finite-order: at each unramified place \(|\xi_{\mathfrak p}(\varpi_{\mathfrak p})|=1\), so
\(|\xi_{\mathfrak p}(\varpi_{\mathfrak p})(N\mathfrak p)^{-s}|
=(N\mathfrak p)^{-\Re s}<1\).
Thus, once both sides are **independently meromorphically continued** with matching normalizations, the identity theorem would extend the equality away from poles, and the correction cannot change the target \(7/8\) zero set. **This last continuation step is not available by simply evaluating mathlib's `LSeries` at \(7/8<\Re s\le1\): a raw L-series definition does not certify continuation to that strip.**

### Actual source-specific falsifier of the uncorrected statement

The protected GCL quartic character \(\psi\) of \(\mathcal O/(5)\simeq\mathbb F_{25}\), invariant under all six global units, has:
\[
 \psi((2))=-1,\qquad N((2))=4,\qquad
 \psi((3+\omega))=i,\quad N((3+\omega))=7.
\]
Here \((2)\) is **inert** and unramified for the character of primitive conductor \((5)\). Represent the same ray character on the **larger zero-extension modulus** \((10)\), so the OAI model deletes the \((2)\) factor, while the intrinsically unramified native idèle character does **not** delete it. The native local polynomial is
\[
  E_{(2)}(s)=1-(-1)4^{-s}=1+4^{-s}.
\]
Consequently,
\[
 \boxed{L_{(10)}(s,\psi)
      =(1+4^{-s})\,L_{(5)}(s,\psi)
      \ne L_{(5)}(s,\psi)\quad(\Re s>1).}
\]
For example, \(s=2\): the two local factors are \(1\) versus \(16/17\), with multiplier \(17/16\). **Any raw cross-implementation theorem claiming `OAI LFunction of χ_m = native idèle LSeries of ξ` for all moduli is false.** This failure is not a flaw in either implementation. It is the explicit, required **imprimitive Euler-deletion correction**.

### Orientation countertest

Another source-specific prime has \(\psi((3+\omega))=i\). The inverse ray character instead has value \(-i\). Therefore the *numerical orientation* of the map from `IdeleClassGroup` and local uniformizers to ray-class ideals must be tested: a conventional Artin reciprocity or inversions-of-idèles convention can silently reverse characters. A map that merely creates an abstract isomorphism of ray-character groups but sends \(i\) to \(-i\) is **insufficient** to establish equality for the *specified* target character. The exact quartic prime is a canary for the first independent native-idèle bridge.

## Newly relevant version and governance boundary

The new native implementation is pinned to **Lean 4.36.0-rc2**, whereas OAI's source proof is pinned to **4.34.1**. Do not alter `openai/math`, secretly advance its mathlib manifest, or insert a v4.36 module into v4.34 source and call it an exact pinned replay. A future genuinely independent cross-implementation Lean proof needs a **separate version-locked sidecar**, one of:
1. a native mathlib v4.36 model and a theorem proving the needed idèle-to-ray/local-value map **in that environment**, plus a strictly versioned source-independent statement comparison to the old OAI representation; or
2. a fully source-locked compatibility port of the new mathlib module into the older environment with all imports and semantic changes audited.

The first is preferable for genuine model independence. In either route the next missing **mathematical theorem** is a conductor-aware **local-character correspondence and prime-uniformizer orientation**, not yet another abstract quotient-character equivalence, normalized Gaussian bound, or repeat of the existing 7/8 Lean endpoint.

**Technical source/finite arithmetic validation** is performed by the companion `f003_native_mathlib_hecke_contract_adversary.py`: it binds the exact Git blobs, confirms the actual old/new API shape, imports the **previously checked** quartic coefficient evidence rather than re-deriving all class-field theory, and verifies the norm-\(4\) deletion and split-prime orientation countertests. A passing test is source-integrity/finite arithmetic evidence **only**, not a Lean proof or analytic theorem.

**Disposition:** `NATIVE_MATHLIB_INDEPENDENT_HECKE_MODEL_FOUND__LOCAL_EULER_CONDUCTOR_CORRECTION_PROVED_MATHEMATICALLY__SIDE_CAR_GLOBAL_IDELE_BRIDGE_NOT_FORMALIZED`. No MATHCERT certification, no family-wide proof promotion.
