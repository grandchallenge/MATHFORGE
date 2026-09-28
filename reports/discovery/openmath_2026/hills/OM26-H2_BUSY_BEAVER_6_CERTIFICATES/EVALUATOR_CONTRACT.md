# OM26-H2 — evaluator contract

**Protected evaluator:** `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90:work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/busy-beaver-6-certificates/PUBLIC_SOURCE/eval.py`

## Input validation

- Requires regular `solution.json`, maximum 16,384 bytes.
- JSON contains only `transitions`.
- States are exactly A–F; each defines symbols 0 and 1.
- Every transition is `[write, move, next_state]`.
- `write` is 0 or 1; `move` is L or R; next state is A–F or H.

## Exact execution

The evaluator uses the standard six-state/two-symbol blank-tape model:
- start state A;
- head at 0;
- bi-infinite zero tape;
- exact deterministic transition simulation.

Validation and final modes use separate private step limits. The evaluator rejects a machine that does not halt within the relevant budget. The private budget schema is constrained by the evaluator to 10 through 2,000,000 steps.

A passing machine must also have reached every non-halting state A–F before halting.

## Outputs

For a passing machine:
- `steps`: exact transitions before halt;
- `ones`: number of 1 cells at halt;
- `tape_span`: inclusive span between leftmost and rightmost visited positions.

## Trust boundary

The accepted mathematical fact is the exact run of the submitted finite machine under this evaluator model. Resource rejection is not a proof of non-halting. Passing is not an optimality, novelty, competition-admission, or MATHCERT claim.
