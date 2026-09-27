# OM26-H1 source map — Kobon triangles

| Surface | Bound source | Source-lock interpretation |
| --- | --- | --- |
| Hill identity | authenticated AutoLab URL `/hills/alejandrozu/kobon-triangles` | canonical external identity |
| Object | opening paragraph | exactly `n` distinct straight Euclidean lines |
| Counted face | opening paragraph | bounded, nonzero-area triangle, interior crossed by no arrangement line |
| Non-count | opening paragraph | larger triangle subdivided by another line does not count |
| Objective | construction-task paragraph | maximize verified count; no optimality inference |
| Submission schema | `Submission` | one `solution.json`, only field `lines`, integer triples `[a,b,c]` |
| Line semantics | `Submission` | `a*x+b*y+c=0`; proportional triples are duplicates |
| Degeneracies | `Submission` | parallelism and >=3-line concurrence allowed |
| Arithmetic | post-validation paragraph | exact rational geometry; no tolerance or area threshold |
| Metric | `Metric and parameters` | `triangles`, maximize |
| Parameter | `Metric and parameters` | `n` in 3..100, default 18, compared only at same `n` |
| Inspection output | `Metric and parameters` | zero-based supporting-line triples for counted triangles |
| Search budget | `Metric and parameters` | generation/search runtime unscored; evaluator watchdog 120 s |
| Hidden data | `Validation and private checks` | no hidden target; private files are evaluator regression fixtures |
| Baseline | `Baseline and local verification` | 18-line family `2*i*x-y-i*i=0`, score 16 |
| Local evaluator command | `Baseline and local verification` | `hills==0.11.0` command displayed; package pin only |

## Version qualification

The authenticated render does not expose an immutable AutoLab hill-version token. The exact source lock is therefore the content-addressed captured body, plus URL and capture date. A live concordance check is mandatory before final submission.

## Campaign cardinality clarification

The rendered sidebar showed `7 hills`; the Human Steward states that the sprint contains six and that the displayed seven-count is a typo. Campaign cardinality remains six. No seventh slot is created.
