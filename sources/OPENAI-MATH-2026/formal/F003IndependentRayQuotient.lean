import Mathlib.NumberTheory.MulChar.Duality
import Mathlib.GroupTheory.QuotientGroup.Basic

/-!
# OAI-26 F003: independent abstract ray-quotient character dictionary

This theorem works for ANY commutative monoid R and subgroup H of its units.
It does not import the OAI Hecke or ray-family implementation. It gives
a mathematically independent, exact alternative model of ray characters
as homomorphisms from the quotient of unit groups, and explicitly proves
both directions. In the Eisenstein application use R = O / M and
H = image(O^× → (O/M)^×).

It does not construct arbitrary finite-order idèle-class characters and
does not prove the seven-eighths analytic nonvanishing theorem.
-/

namespace GCL.OAI26.F003

variable {R : Type*} [CommMonoid R] (H : Subgroup Rˣ)

/-- Independent ray-quotient model. -/
abbrev QuotientRayCharacter := (Rˣ ⧸ H) →* ℂˣ

/-- Unit-trivial multiplicative characters, formulated without any source
    OAI definitions or ring-of-integers hypotheses. -/
def UnitTrivialCharacter :=
  {χ : MulChar R ℂ // ∀ u : Rˣ, u ∈ H → χ (u : R) = 1}

/-- Extend a character of the quotient of unit groups by zero on nonunits. -/
noncomputable def fromQuotient
    (ψ : QuotientRayCharacter H) : MulChar R ℂ :=
  MulChar.ofUnitHom (ψ.comp (QuotientGroup.mk' H))

theorem fromQuotient_trivial
    (ψ : QuotientRayCharacter H) (u : Rˣ) (hu : u ∈ H) :
    fromQuotient H ψ (u : R) = 1 := by
  have hquot : (u : Rˣ ⧸ H) = 1 :=
    (QuotientGroup.eq_one_iff u).2 hu
  simp [fromQuotient, MulChar.ofUnitHom_coe, hquot]

/-- The quotient-character model embeds in the unit-trivial multiplicative
    character model, with the expected nonunit-zero convention. -/
noncomputable def toUnitTrivial
    (ψ : QuotientRayCharacter H) : UnitTrivialCharacter H :=
  ⟨fromQuotient H ψ, fromQuotient_trivial H ψ⟩

/-- A unit-trivial residue character factors uniquely through the quotient. -/
noncomputable def toQuotient
    (χ : UnitTrivialCharacter H) : QuotientRayCharacter H :=
  QuotientGroup.lift H χ.val.toUnitHom (by
    intro u hu
    apply Units.ext
    simpa only [MulChar.coe_toUnitHom, Units.val_one]
      using χ.property u hu)

theorem toQuotient_fromQuotient
    (ψ : QuotientRayCharacter H) :
    toQuotient H (toUnitTrivial H ψ) = ψ := by
  apply MonoidHom.ext
  intro x
  obtain ⟨u, rfl⟩ := QuotientGroup.mk'_surjective H x
  simp [toQuotient, toUnitTrivial, fromQuotient]

theorem fromQuotient_toQuotient
    (χ : UnitTrivialCharacter H) :
    toUnitTrivial H (toQuotient H χ) = χ := by
  apply Subtype.ext
  apply (MulChar.equivToUnitHom).injective
  apply MonoidHom.ext
  intro u
  simp [toUnitTrivial, fromQuotient, toQuotient]

/-- No existence or uniqueness axiom: an explicit two-sided equivalence. -/
noncomputable def rayCharacterEquiv :
    QuotientRayCharacter H ≃ UnitTrivialCharacter H where
  toFun := toUnitTrivial H
  invFun := toQuotient H
  left_inv := toQuotient_fromQuotient H
  right_inv := fromQuotient_toQuotient H

/-- Nonunit-zero rule is intrinsic to the quotient character construction. -/
theorem fromQuotient_nonunit_zero
    (ψ : QuotientRayCharacter H) {r : R} (hr : ¬ IsUnit r) :
    fromQuotient H ψ r = 0 :=
  MulChar.map_nonunit _ hr

end GCL.OAI26.F003
