# OM26-H2 — Busy Beaver 6 certificates: semantic source map

**Campaign binding:** OM26-H2  
**Exact organizer hill:** `alejandrozu/busy-beaver-6-certificates`  
**Version:** `0.1.0`  
**Source-lock state:** protected exact source, slot-bound; this semantic map does not certify a result.

## Protected source chain

- Forge source lock: `reports/discovery/openmath_2026/unassigned_sources/busy-beaver-6-certificates/SOURCE_LOCK.json`
- Slot binding: `reports/discovery/openmath_2026/SLOT_BINDING.json`
- Protected public source capture: `grandchallenge/MATHSOLVE@4ab1f45089ff6be6f70772d0441fe88afd930f90`
- Statement/README: `work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/busy-beaver-6-certificates/PUBLIC_SOURCE/README.md`
- Hill manifest: `.../busy-beaver-6-certificates/PUBLIC_SOURCE/hill.yaml`
- Evaluator: `.../busy-beaver-6-certificates/PUBLIC_SOURCE/eval.py`

## Source-derived task semantics

The task is to submit one complete six-state, two-symbol Turing-machine transition table. The evaluator starts from state A on an all-zero bi-infinite tape and simulates the machine exactly. A candidate passes only if it halts within the applicable private execution budget and all six non-halting states A–F were reached.

Every passing candidate is therefore an exact finite lower-bound witness for the six-state Busy Beaver function (S(6)). Its `steps` value is the exact number of transitions executed before halting. The hill explicitly does not treat a long-running machine as a proof of the exact value of (S(6)).

## Submission object

A single regular UTF-8 `solution.json` containing exactly a `transitions` object. Each of states A–F has entries for symbols 0 and 1, each entry encoded as `[write, move, next_state]`.

## Metrics

Lexicographic metrics from the protected hill manifest:

1. `steps` — maximize.
2. `ones` — maximize.
3. `tape_span` — maximize.

## Semantic boundary

A passing evaluator result proves only the submitted machine's exact halting run and the resulting finite lower bound. It does not prove optimality, the exact Busy Beaver 6 value, novelty, competition acceptance, or MATHCERT certification.
