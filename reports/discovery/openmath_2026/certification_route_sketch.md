# OPENMATH-2026 certification-route sketch

This file sketches downstream routes only. It is not certification.

For each exact hill or independently meaningful subclaim, choose the weakest sufficient replay route after the statement is locked.

- Lean / equivalent proof assistant: kernel-checked theorem plus semantic-fidelity audit.
- Exact finite computation: minimized certificate plus independent verifier.
- SAT/SMT: proof-producing artifact plus replay.
- Computer algebra: exact witness translated into a replayable certificate; raw CAS output is insufficient.
- Interval/analytic computation: explicit assumptions, interval certificate, and replay.
- Counterexample: exact witness plus formal or independently replayable verification that it satisfies the hill hypotheses and violates the claimed conclusion.

Every claim-bearing MATHSOLVE packet should hand MATHCERT:

1. exact claim text;
2. exact source/hill identity;
3. exact formal/certificate artifact;
4. dependency and axiom ledger;
5. producer provenance;
6. independent replay path;
7. semantic-fidelity hazards;
8. acceptance and rejection criteria.

Competition acceptance and GCL certification remain distinct states.
