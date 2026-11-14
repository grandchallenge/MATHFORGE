# Agent instructions

**Engineering architecture and reliability:** Adopt [GCL-ENGINEERING-001 v1.0.0](https://github.com/grandchallenge/gcl-standards/blob/2a3cfed9419ba9b74eeaaee70b9db8c3f47f3c9b/standards/GCL-ENGINEERING-001.md), pinned at protected `gcl-standards` commit `2a3cfed9419ba9b74eeaaee70b9db8c3f47f3c9b`. Engineering agents own architecture, necessity, integration, tests, deploy/readback and retirement; reuse GitHub and existing components before inventing infrastructure. Do not duplicate workflow authority or mistake CI/merge for live completion. Preserve this repository's superior, reserved, and domain-specific policies. Cross-repository adoption requires explicit readback, never assumption.

MATHFORGE discovers and reconstructs candidates. It does not certify or promote
claims. Under `GCL-AGENT-STAFFING-001` version `1.0.0`, one Codex system may
implement, staff distinct non-reserved logical audit passes, merge through
satisfied protected controls, and read back the result. Authoring-system
Adversary and Referee passes are declared `non_authoring_read_only`. Automation
may not write directly to protected branches, manufacture reserved authority,
or infer certification or promotion from CI or integration.

MATHFORGE adopts `GCL-AGENT-CONTINUITY-001@1.0.0` from
`grandchallenge/INTELLECT/governance/agent_execution/GCL-AGENT-CONTINUITY-001.md`.
For interruption-prone discovery or reconstruction, continuity checkpoints must
preserve material source/provider identity, immutable source or byte-digest
identity, provider-manifest state, transcribed/normalized/reconstructed
distinctions, search/reconstruction parameters, generated witness identities,
failed routes, and the deterministic next evidence action. A successor agent
must rebind live repository state; agent substitution does not create
independent verification. Discovery evidence and generated witnesses are not proof, certification, or promotion.
Routine short operations are not universally checkpoint-required.
