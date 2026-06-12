# MATHFORGE

MATHFORGE is the discovery and witness-generation pillar of the Grand Challenge mathematics stack.

It is responsible for turning promising mathematical structure into durable artifacts: search traces, exact-computation outputs, counterexample candidates, witness objects, and certificate payloads that can later be consumed by MATHSOLVE and checked by MATHCERT.

## Algebraic witness export

MATHFORGE now includes an algebraic-witness export lane for polynomial subclaims. The lane is deliberately downstream-compatible with the MATHCERT algebraic certificate lane:

```text
MATHFORGE  -> generate candidate algebraic witnesses
MATHSOLVE  -> decide when to invoke them tactically
MATHCERT   -> check, certify, and preserve the proof boundary
```

MATHFORGE may use SageMath, SymPy, Singular, Magma, or custom exact arithmetic to discover witnesses. Those outputs are not proofs. They become trustworthy only after replay or Lean-kernel checking in MATHCERT.

See `docs/algebraic_witness_export.md`.
