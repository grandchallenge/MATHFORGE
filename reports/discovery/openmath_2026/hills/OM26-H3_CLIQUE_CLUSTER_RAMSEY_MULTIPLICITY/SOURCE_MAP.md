# OM26-H3 — Clique-cluster Ramsey multiplicity: semantic source map

**Campaign binding:** OM26-H3  
**Exact organizer hill:** `alejandrozu/clique-cluster-ramsey-multiplicity`  
**Version:** `1.0.0`

## Protected source chain

- Forge source lock: `reports/discovery/openmath_2026/unassigned_sources/clique-cluster-ramsey-multiplicity/SOURCE_LOCK.json`
- Slot binding: `reports/discovery/openmath_2026/SLOT_BINDING.json`
- Protected source capture: `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90`
- README, `LIFTING.md`, `SOURCES.md`, hill manifest, evaluator, tests, and supplied examples are captured in the protected public-file manifest.

## Source-derived mathematical target

For a red/blue coloring of a complete graph, let (M_4(G)) count four-vertex subsets whose six edges have one color. The README defines the Ramsey multiplicity constant
[
c_4=lim_{n	oinfty}min_{|V(G)|=n} M_4(G)/inom n4.
]

The hill asks for a weighted two-color blow-up certificate whose exact limiting monochromatic (K_4) density (P(A,w)) is strictly below the frozen reference
[
B^*=10486266368/768^4.
]

A certificate consists of integer block weights and a symmetric binary color matrix, with the diagonal specifying the color of the clique inside each block. Repeated template indices are part of the exact limiting count.

## Success semantics

- Search progress: lower exact (P).
- Hill target: exact (P < B^*), which yields a checked candidate upper bound (c_4le P<B^*) through the source-supplied lifting argument.
- Parent problem resolution is explicitly outside this construction evaluator; it always reports `parent_problem_resolved=false`.

## Metrics

1. `reference_beaten` — maximize; 1 iff exact (P<B^*).
2. `density_ppt` — minimize; (lceil10^{12}Pceil).

## Semantic boundary

The source itself requires novelty, attribution, and the approved proof/certificate trust boundary before calling a candidate a new research result. This map adds no independent literature claim.
