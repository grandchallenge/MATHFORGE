# OM26-H1 problem card — Kobon triangles

Construct exactly `n` distinct straight lines in the Euclidean plane and maximize the evaluator-verified number of bounded triangular faces. The operative sprint setting is the hill default `n=18` unless a route explicitly studies another `n` for reconnaissance.

## Competition object

A candidate is an actual rational straight-line arrangement represented by integer triples `[a,b,c]` for `a*x+b*y+c=0`. Abstract pseudoline arrangements do not satisfy the submission contract.

## Primary research target

Produce replayable `n=18` arrangements with verified score strictly above the displayed baseline 16, while preserving exact evaluator semantics.

## Secondary research targets

- reproduce the baseline score independently;
- characterize local moves that change the triangular-face count;
- identify symmetry/normal-form reductions that shrink search without excluding realizable high-score arrangements;
- use small-`n` regimes to discover motifs and to falsify search heuristics;
- preserve exact witnesses and negative route information.

## Success without optimality

A higher exact verified score is a valid construction improvement. It must not be described as optimal unless a separate upper-bound argument is proved and certified.

## Critical semantic hazards

- counting triangular 3-cycles that are not faces;
- counting a triangle whose interior is crossed/subdivided;
- treating nearly concurrent/intersecting floating geometry as exact;
- importing pseudoline solutions that are not stretchable to straight lines;
- comparing scores across different `n`;
- conflating evaluator acceptance with novelty or certification.
