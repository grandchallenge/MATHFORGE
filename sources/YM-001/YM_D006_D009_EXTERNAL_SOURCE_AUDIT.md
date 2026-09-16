# YM-001 source audit — external-source debts D006 through D009

## Record

- Campaign: `YM-001`.
- Provider authority: `grandchallenge/MATHFORGE`.
- Protected Forge baseline: `770f95d1f8e7cfdd3facbd9242bf3c21c0e8b074`.
- Audit date: `2026-09-16`.
- Protected predecessor debt record: `grandchallenge/MATH-PROGRAMME:campaigns/yang_mills/WP02_THEOREM_LEDGER/04_DEPENDENCY_DEBT_GATE.json`.
- Audited debts: `YM-D006`, `YM-D007`, `YM-D008`, `YM-D009`.
- Disposition: `TARGET_SELECTION_AMBIGUITY_REMOVED__NO_EXTERNAL_SOURCE_BRIDGE_ADMITTED`.
- Claim class: bounded source/theorem-interface audit only.

## Purpose

The protected WP02 ledger leaves four external-source debts whose resolution can change the first native Solve theorem frontier. This audit reads the exact current or identified source versions far enough to determine whether any supplies a composable theorem interface into the protected four-dimensional existence, reconstruction, regulator-survival, or physical-gap obligations.

This audit does **not** certify the sources globally. It identifies the first material non-composition point for each source. Once a necessary step fails or the source explicitly stops short of the required bridge, further line-by-line review is not required to decide the current target-selection frontier. A materially revised source may reopen its corresponding audit.

## Protected campaign comparison surface

The relevant protected debts remain:

- `YM-D001`: regulator-survival spectral bridge;
- `YM-D002`: full limiting Osterwalder–Schrader hierarchy;
- `YM-D003`: four-dimensional continuum construction;
- `YM-D004`: renormalized local gauge-invariant observables with ultraviolet concordance;
- `YM-D005`: converse Euclidean-decay to physical-Hamiltonian-gap bridge.

A source is useful for target selection only to the extent that an exact theorem can compose into one of these obligations without a fixed-regulator, finite-volume, strong-coupling, perturbative, lower-dimensional, positivity-only, one-channel-decay, or unverified-complete-solution substitution.

---

## YM-D006 / YM-SRC-016 — Etesi near-vacuum partition function

### Source identity

Gabor Etesi, *The four-dimensional Yang–Mills partition function in the vicinity of the vacuum*, Letters in Mathematical Physics (2023), DOI `10.1007/s11005-023-01662-2`.

Audit uses the published theorem body.

### Exact mathematical terrain

The main theorem concerns pure `SU(2)` Yang–Mills on Euclidean `R^4` in a neighbourhood of the flat connection, with a small-curvature restriction of the form `||F||_{L^2}<epsilon`. The construction compactifies to a round `S^4` of radius `R` and studies a **truncated** partition function in a weak-coupling / near-vacuum regime. The functional integral is treated formally and evaluated after spectral/zeta regularization.

The source itself distinguishes the local/truncated calculation from a full partition function. It also describes the underlying infinite-dimensional integration measure as formal rather than as a constructed probability measure.

### First missing implication

No theorem in the audited source constructs the full nonperturbative four-dimensional Euclidean measure or a single limiting gauge-invariant Schwinger hierarchy satisfying the complete OS profile. Consequently the source does not supply:

- `YM-D002` full limiting OS data;
- `YM-D003` a nontrivial continuum construction with large-field and infinite-volume control;
- `YM-D004` the required local-observable renormalization interface;
- `YM-D001` or `YM-D005` a physical spectral-gap bridge.

### Campaign disposition

`YM-D006` is **dispositioned for target selection as non-composable**. The source remains relevant background on a regularized/truncated near-vacuum partition-function calculation, but it does not change the protected theorem frontier.

---

## YM-D007 / YM-SRC-017 — Jacobsen SU(3) complete-solution claim

### Source identity

D. C. Jacobsen, *A Constructive Proof of Existence and Mass Gap for Pure SU(3) Yang-Mills in Four-Dimensional Space-Time*, arXiv `2506.00284`.

Two source states are material:

- `arXiv:2506.00284v1`: substantive manuscript used for theorem-body inspection;
- current arXiv record (`v2`): withdrawn by arXiv administration for failure to meet arXiv research-content quality standards.

The withdrawal is provenance/status evidence only; it is not, by itself, a mathematical refutation. The mathematical non-composition finding below comes from the v1 theorem body.

### Claimed route

The manuscript claims a four-dimensional pure `SU(3)` construction, Osterwalder–Schrader reconstruction, and a positive mass gap. A core weak-coupling step invokes a polymer/Kotecký–Preiss convergence estimate.

### Fatal proof defect in the displayed convergence estimate

In the manuscript's Appendix A, the displayed plaquette-activity estimate gives

`|K_p| <= 1.5 beta + 1.125 beta^2`

and, with its Wilson-coupling substitution, rewrites this as

`9/g_0^2 + 40.5/g_0^4`.

For the manuscript's claimed weak-coupling limit `g_0 -> 0`, this expression diverges. The next displayed step instead treats the activity as `A g_0^2` and uses that small quantity to derive the Kotecký–Preiss convergence threshold.

The second scaling does not follow from the preceding bound. Therefore the displayed argument does not establish the weak-coupling polymer convergence on which the later continuum chain relies.

### First missing implication

The route fails before a regulated construction is shown to possess the uniform weak-coupling control required for a continuum limit. It therefore supplies no admitted bridge into `YM-D002` through `YM-D005`, and no regulator-survival theorem for `YM-D001`.

### Campaign disposition

`YM-D007` is **dispositioned for target selection as a falsified complete-solution route as written**. This does not assert that every subsidiary statement in the manuscript is false. It records that a necessary displayed proof step for the claimed construction fails, so the manuscript cannot be imported as a complete-solution theorem interface.

A materially revised manuscript that repairs the convergence argument may reopen the source debt.

---

## YM-D008 / YM-SRC-018 — Faizal–Shabir reflection-positive SU(N) complete-solution claim

### Source identity

Mir Faizal and Arshid Shabir, *Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement*, arXiv `2606.19362v1`; published composite version in *Fortschritte der Physik* 74 (2026), e70097.

Audit uses the current v1/composite theorem body and, in particular, the stated continuum spectral-gap theorem.

### Claimed route

The source combines fixed-regulator reflection positivity and clustering with a multiscale/RG argument intended to propagate a positive gap through refinement to the continuum theory.

The central continuum gap statement (Theorem 11.1 in the audited composite text) assumes an interscale operator inequality of the form

`T_{k+1} >= Pi_k T_k Pi_k - R_k`,

with `R_k >= 0` and summable norm defects.

### Fatal direction error in the displayed spectral step

The proof then estimates the excited-state spectral radius using an **upper** quadratic-form inequality of the form

`<f, T_{k+1} f> <= <f, Pi_k T_k Pi_k f> + epsilon_k ||f||^2`.

That upper bound does not follow from the stated lower operator bound

`T_{k+1} >= Pi_k T_k Pi_k - R_k`.

A lower bound controls `T_{k+1}` from below; it cannot, under the displayed hypotheses, supply the upper bound required to keep the excited spectral radius away from the vacuum eigenvalue. Hence the proof as written does not establish its gap-persistence conclusion.

### First missing implication

The manuscript therefore does not supply a valid regulator-survival spectral bridge (`YM-D001`) or the resulting continuum physical-gap conclusion. The fixed-regulator reflection-positive and clustering material remains nonterminal and cannot be substituted for the failed continuum step. No conclusion here certifies or rejects unrelated subsidiary results in the composite manuscript.

### Campaign disposition

`YM-D008` is **dispositioned for target selection as a non-composable complete-solution route as written** because the central continuum spectral theorem contains an unclosed operator-inequality step.

A revised theorem with hypotheses strong enough to justify the required upper spectral estimate may reopen this source debt.

---

## YM-D009 / YM-SRC-019 — Faria da Veiga–O'Carroll four-dimensional lattice correlator manuscript

### Source identity

Paulo A. Faria da Veiga and Michael O'Carroll, *On Charge Conjugation, Correlations, Elitzur's Theorem and the Mass Gap Problem in Lattice SU(N) Yang-Mills Models in d=4 Dimensions*, arXiv `2509.03513v2`.

Audit uses current `v2`.

### Exact mathematical terrain

The manuscript studies four-dimensional Euclidean Wilson lattice `SU(N)` Yang–Mills with lattice spacing `a` in a fixed regulated model and a strong-coupling regime (`beta = 1/g^2` small in the manuscript's convention). It develops charge-conjugation, correlation, Elitzur-type, and local Haar-measure structure. Thermodynamic/infinite-volume correlation statements are tied to the regulated lattice theory and cited strong-coupling machinery.

The manuscript explicitly states that the positive local Haar-measure mass term **does not prove the mass gap**. Its conclusion separately identifies survival of mass gaps through renormalization / the continuum limit `a -> 0` as work still to be proved.

### First missing implication

The exact non-overlap is therefore explicit:

- fixed-regulator structure is not `YM-D001` regulator survival;
- regulated correlation decay is not `YM-D005` physical-Hamiltonian gap without the converse reconstruction/spectral bridge;
- no full limiting OS hierarchy is supplied for `YM-D002`;
- no four-dimensional continuum construction is supplied for `YM-D003`.

### Campaign disposition

`YM-D009` is **audited and dispositioned as fixed-regulator / strong-coupling lattice terrain with an explicit continuum non-claim**. It does not alter the protected continuum theorem frontier.

---

## Aggregate dependency effect

The four unresolved external-source records do **not** supply a missing implication into `YM-D001` through `YM-D005`:

| Debt | Exact source-audit result | Frontier effect |
|---|---|---|
| `YM-D006` | formal/truncated near-vacuum `SU(2)` partition-function calculation; no full constructed measure/OS hierarchy/gap bridge | no composable continuum interface |
| `YM-D007` | current record withdrawn; v1 weak-coupling polymer convergence uses an internally inconsistent scaling bound | claimed complete-solution route non-composable |
| `YM-D008` | continuum gap theorem uses an upper spectral estimate not implied by its stated lower interscale operator bound | claimed regulator-survival/gap bridge unproved |
| `YM-D009` | fixed-regulator strong-coupling lattice analysis; source explicitly leaves continuum persistence open | exact fixed-regulator boundary established |

This removes the live source ambiguity relevant to restricted-target selection. It does **not** prove `YM-D001` through `YM-D005`, open the WP02 downstream gate by itself, or authorize a new theorem target without the remaining protected promotion/debt disposition required by the Programme gate.

## False-proof firewall classification

The audited sources trigger protected WP01 route boundaries rather than bypassing them:

- `YM-D006`: truncated/formal near-vacuum control -> nonperturbative existence substitution is rejected;
- `YM-D007`: unreviewed complete-solution claim with a failed necessary proof step is rejected;
- `YM-D008`: reflection positivity/fixed-regulator control -> continuum physical-gap substitution is rejected, and the proposed bridge proof is incomplete;
- `YM-D009`: fixed-regulator/strong-coupling -> continuum substitution and correlation-decay -> complete physical-gap substitution are explicitly rejected.

## Downstream composition

The native Solve frontier should therefore be selected from the genuinely open protected debts `YM-D001` through `YM-D005`, not from an asserted external complete solution. Source audit alone does not choose among them.

Before a restricted target opens, the Programme's remaining lawful gate conditions must be reconciled against this audit and the already protected WP01/WP02 review/CI evidence. If that reconciliation opens target selection, MATHSOLVE should freeze the smallest exact theorem attacking one of `YM-D001` through `YM-D005` and begin proof/falsification immediately.

## Claim boundary

This audit:

- does not construct four-dimensional quantum Yang–Mills theory;
- does not prove a positive physical mass gap;
- does not establish confinement or an area law;
- does not establish regulator-independent continuum control;
- does not certify or globally refute every statement in any audited manuscript;
- does not render a MATHCERT disposition;
- does not claim novelty or priority.

It establishes only the exact current source-composition boundary needed for the next campaign decision.
