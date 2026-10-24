# Family 342: independent definition audit and corrected cone counterexample

**Review ID:** `MF-OAI-MATH-2026-F342-SEM-001`  
**Reviewed source:** `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`  
**GCL evidence predecessor:** `MATHFORGE@2cd84491ccced5f86769416393c7ba9f2c79852c`, protected Comparator and Lean pass from run `40041645086`  
**Scope:** Definition-level mathematical concordance and independent exact exterior-algebra replay for the *October 6, 2026 corrected* four-torus example. No new inference about the truth of the main existence theorem, peer-reviewed publication, or mathematical priority.

## 1. Precise model and theorem

Pinned Lean `lean/OAI/Geometry/TamingCompatibility/Model.lean` represents a 4-dimensional smooth manifold by `ChartedSpace Space X`, `IsManifold Model ∞ X`, where `Space := EuclideanSpace ℝ (Fin 4)` and `Model := 𝓘(ℝ, Space)`. The main theorem adds `T2Space X`, `SecondCountableTopology X`, `CompactSpace X`, and `ConnectedSpace X`. These are the conventional topological and differentiability conditions for a closed, connected, second-countable, Hausdorff smooth four-manifold (without prescribed orientation or integrability). A smooth almost-complex structure induces an orientation; the paper requires no initial choice for the main existence theorem.

`TwoForm X` is a section of *continuous alternating bilinear forms on tangent spaces*, but **the raw section is not assumed smooth**. Smoothness and closedness are supplied via `IsSymplectic α` and quantified local pullback tests:

```lean
noncomputable def pullback (α : TwoForm X) (f : Space → X) :
    Space → Space [⋀^Fin 2]→L[ℝ] ℝ :=
  fun y => (α (f y)).compContinuousLinearMap (mfderiv Model Model f y)

def IsSmooth (α : TwoForm X) : Prop :=
  ∀ (f : Space → X) (U : Set Space), IsOpen U →
    ContMDiffOn Model Model ∞ f U → ContDiffOn ℝ ∞ (pullback α f) U

def IsClosed (α : TwoForm X) : Prop :=
  ∀ (f : Space → X) (U : Set Space), IsOpen U →
    ContMDiffOn Model Model ∞ f U → ∀ y ∈ U,
      extDerivWithin (pullback α f) U y = 0
```

A pullback is computed with `mfderiv`; by multilinearity, the same derivative is applied to both arguments. The domain is an open subset of ℝ⁴, so `ContDiffOn` and `extDerivWithin` are the coordinate expressions of smoothness and exterior closure, *provided* the Lean library theorems implementing pullback naturality and chart invariance establish the standard differential-geometric correspondence.

### Directly established from displayed definitions

1. **Alternation:** the type `[⋀^Fin 2]→L[ℝ]` is an alternating 2-linear map; evaluation as `α x ![u,v]` has the usual skew-symmetry.
2. **Taming:** `Tames α J := ∀ x v, v ≠ 0 → 0 < eval α x v (J.endomorphism x v)` is precisely strict positivity on complex lines.
3. **Invariant + positive:** `Compatible α J := Tames α J ∧ IsInvariant α J`, where `IsInvariant` asserts `α(Ju,Jv)=α(u,v)`, encodes a J-positive invariant two-form.
4. **Nondegeneracy:** for any alternating form, taming *implies* `IsNondegenerate`: if `v` lies in the radical, then `α(v,Jv)=0`; strict taming forces `v=0`. Thus the explicit nondegeneracy conjunct in `IsSymplectic` does **not** narrow the taming hypothesis.
5. **Fixed structure and unprescribed class:** the theorem uses exactly the same `J` on both sides and does not constrain `[η]` to equal `[α]`. This agrees with the unchanged main existence theorem in the September 23 and October 6 introductions (lines 23–32).

### Still not independently machine-proved

- **SEM-342-01, local-chart smoothness bridge:** for a section of alternating tangent bilinear maps, prove that `IsSmooth α` is equivalent to conventional smoothness as a differential two-form. One direction uses inverse charts among the universally quantified smooth maps; the other uses smooth pullback by arbitrary local smooth maps.
- **SEM-342-02, exterior derivative bridge:** assuming smoothness, prove `IsClosed α ↔ dα=0` for the intrinsic smooth de Rham exterior derivative. The key step is the library-level naturality of `extDerivWithin (pullback α f)` and invariance on overlaps of smooth charts.
- **SEM-342-03, metric compatibility bridge:** derive symmetry and positive definiteness of `g(u,v)=α(u,Jv)` from `Compatible α J`, and conversely. The elementary algebra is clear; the required Lean theorem has not been replayed independently.
- **SEM-342-04, theorem model equivalence:** establish the exact round-trip between the paper's manifold/structure hypotheses and the Lean typeclass/structure setup, including model manifold and tangent bundle smoothness; reject implicit stronger constraints or missing topological conditions.

**Disposition:** `DEFINITION_LEVEL_STRUCTURAL_ALIGNMENT_WITH_FORMAL_BRIDGE_OPEN`. These obligations are *not* discharged by the successful Comparator run; do not mark `SEMANTICALLY_REVIEWED`.

## 2. The corrected four-torus example, independently checked

Pinned source: `preprints/Taming-implies-compatibility-on-four-manifolds-October-6-2026/build/sections/08-cones.tex`, `\begin{example}[Strict inclusion on the four-torus]` (lines approximately 375–420).

On `T⁴=ℝ⁴/ℤ⁴` let `e^{ij}=dx_i∧dx_j`, with standard metric and orientation, and set

\[
 U=e^{12}+e^{34},\quad V=e^{13}-e^{24},\quad W=e^{14}+e^{23},
 \quad f={1\over4}\sin(2\pi x_1),\quad k={1\over4}\sin(2\pi x_2),
 \quad r=\sqrt{1+f^2+k^2}.
\]

The smooth self-dual form `F=(U+fV+kW)/r` has squared norm 2 and determines an orthogonal almost-complex structure `J`. Define

\[
 \eta=U+2f\,e^{13}+2k\,e^{23},\qquad \tau_\pm=U\pm V.
\]

Independent rational-polynomial exterior algebra and matrix calculations (`tests/test_openai_math_342_torus.py`, nine tests, no third-party dependencies) establish the following *identities for arbitrary formal real* `f,k`:

1. `*U=U`, `*V=V`, `*W=W`; `U∧U=V∧V=W∧W=2 vol`; all their mixed wedge products vanish.
2. `(η+*η)/2=U+fV+kW=rF`; `(η−*η)/2=f(e^{13}+e^{24})+k(e^{23}−e^{14})`. Its magnitude has squared norm `2(f²+k²)`.
3. The matrix of the unnormalized almost-complex endomorphism `rJ` satisfies `(rJ)²=−r² I` and `(rJ)^T(rJ)=r² I`; thus `J²=−I` and `J` is orthogonal.
4. The `J`-invariance equation for `η` holds exactly: `(rJ)^T B_η(rJ)=r² B_η`, with `B_α` denoting the skew matrix of a two-form `α`.
5. The symmetric matrix `S=(B_η(rJ)+(B_η(rJ))^T)/2` obeys `(S−r²I)²=r²(f²+k²)I`. Hence the Hermitian eigenvalues of `η(·,J·)` are `r±√(f²+k²)`, strictly positive because `r²−(f²+k²)=1`.
6. For `τ_±`, the symmetric part of `B_{τ_±}(rJ)` is `(1±f)I`. Since `|f|≤1/4`, both `τ_+` and `τ_-` strictly tame `J` at every nonzero tangent vector.
7. The cohomology intersection pairing is `[τ_+]·[τ_-]=[U]^2−[V]^2=0`, although both `τ_±` are tame. The compatibility of `η` in class `[U]` proves that `K_J^c` is nonempty.
8. The dependence of the form coefficients on coordinates enforces `dη=0`, `dτ_±=0`. More explicitly, for the globally periodic one-form `β=−(cos(2πx_1)+cos(2πx_2))/(4π) dx_3`, `η−U=dβ`, so `[η]=[U]`.

### Geometric step distinct from polynomial checks

A closed anti-invariant two-form on this orthogonal almost-Hermitian four-torus is self-dual; consequently `dα=0` implies `d*α=0`. Hence it is harmonic. Harmonic two-forms for the standard flat torus are constant. Every constant self-dual two-form is `aU+bV+cW`, and anti-invariance to `J` imposes `a+bf(x_1)+ck(x_2)=0` for all points. The independent functions `1`, `sin(2πx_1)` and `sin(2πx_2)` force `a=b=c=0`. Thus `H_J^-=0` (a standard analytic argument, not yet kernel formalized).

If the class `[τ_+]` admitted a J-compatible symplectic representative `σ`, then `σ∧τ_-` would be a strictly positive four-form everywhere, so its integral would be positive. But de Rham pairing gives

\[
 \int_{T^4}\sigma\wedge\tau_-=[\tau_+]\cdot[\tau_-]=0,
\]

contradiction. The same argument interchanges `+` and `−`. Therefore both tame classes lack compatible representatives, despite `H_J^-=0` and nonempty compatible cone:

\[
  \mathcal K_J^c+H_J^-=\mathcal K_J^c\subsetneq\mathcal K_J^t.
\]

This is a **concrete obstruction to the superseded September 23 unconditional cone-sum claim**. It does not obstruct the unchanged main *existence* theorem, which demands only that *some* compatible class exist. It agrees with the October 6 corrected strict positivity characterization: `[τ_+]·[τ_-]=0`, so each violates the proposed positivity test using the other class.

## 3. Claims and next formal proof obligations

- `TORUS_EXACT_POLYNOMIAL_CHECKS_PASS`: nine locally reproduced tests of wedge, Hodge, `J²`, invariance, positive eigenvalue discriminant, both taming forms, intersection pairing, and coefficient-dependent closedness.
- `TORUS_GEOMETRIC_ARGUMENT_DOCUMENTED`: use standard closed/self-dual ⇒ harmonic ⇒ constant argument for anti-invariant forms, plus positive wedge pairing for compatible-versus-taming forms; the argument has **not** been implemented in Lean.
- `SEPTEMBER_UNCONDITIONAL_CONE_SUM_REFUTED_FOR_DISPLAYED_EXAMPLE`: conditional on standard torus de Rham/harmonic identification; no claim of any refutation of the main existence theorem.
- `OCTOBER_CONE_ASSERTIONS_NOT_KERNEL_VERIFIED`: the corrected cone-duality theorem as a whole remains unformalized and not independently proved in this tranche.
- `LEAN_GEOMETRIC_SEMANTIC_BRIDGE_OPEN`: prove SEM-342-01 through SEM-342-04 before theorem-level paper ↔ Lean semantic admission.

The proofs and tests in this file establish neither research priority nor MATHCERT certification. They do not change the source catalog's `SOURCE_LOCKED` status.