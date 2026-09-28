# OM26-H1 upper-bound source audit

**Date:** `2026-09-27`  
**Question:** What upper bound is actually justified for the hill's unrestricted semantics, which allow parallel lines and intersections of multiplicity three or more?

## Disposition

`UNRESTRICTED_95_PRIMARY_PROOF_FOUND__94_CURRENTLY_REPORTED__94_PRIMARY_TRANSFER_CHAIN_UNRESOLVED`

## Primary source A — Clément and Bader (2007)

The cached paper `Tighter Upper Bound for the Number of Kobon Triangles` explicitly treats configurations of straight lines and discusses multiple intersections/common-side triangles. Its Theorem 1 gives

`K(n) <= floor(n(n-2)/3) - 1` for `n mod 6 in {0,2}`.

For `n=18`, this proves the unrestricted bound `K(18) <= 95`.

The proof is not restricted to simple arrangements: its segment-count argument explicitly handles intersections of more than two lines and the segment savings/losses caused by them.

Source: `https://oeis.org/A006066/a006066.pdf`.

## Primary source B — Bartholdi, Blanc, Loisel (2007/2008)

`On simple arrangements of lines and pseudo-lines in P^2 and R^2 with the maximum number of triangles` defines an affine arrangement as one in which every pair of pseudo-lines intersects exactly once, and then states that its sole interest is **simple arrangements**, meaning no multiple intersections.

Theorem 1.1 proves, for even `n`,

`a_3^s(n) <= floor(n(n - 7/3)/3)`.

For `n=18`, this is 94.

However, the theorem's stated subject excludes parallel pairs and multiple intersections. The AutoLab hill explicitly allows both. Therefore the theorem is not, by itself, a source-complete proof that the hill-global optimum is at most 94.

Source: `https://arxiv.org/html/0706.0723v1`.

## Current status surfaces

OEIS A006066, current internal revision timestamped 2026-09-14, records `n=18: >=93, upper bound 94 [Bader]`. MathWorld also presents 94 as the even-n Kobon upper bound. These are useful status signals, but the audited surfaces do not expose an unrestricted proof upgrading the Clément-Bader 95 theorem to 94.

Sources:

- `https://oeis.org/A006066`
- `https://oeis.org/A006066/internal`
- `https://mathworld.wolfram.com/KobonTriangle.html`

## Consequence for GCL

The campaign may use 94 as a **reported external target**, but not yet as a GCL-admitted hill-global theorem.

At present the proof-status ladder is:

- exact GCL construction lower bound: `K(18) >= 93`;
- primary-source unrestricted theorem: `K(18) <= 95`;
- externally reported current upper bound: `94`;
- missing bridge: a primary unrestricted 94 proof, or a rigorous transfer theorem showing the simple-arrangement 94 bound applies to every hill-admissible degenerate arrangement.

Thus a 94 construction would improve the GCL lower bound to 94, but GCL must not call it globally optimal until the upper-bound bridge is independently closed and certified.

## High-value residual

The bound problem is now narrow. Any hypothetical 95-triangle arrangement must evade the simple-arrangement theorem through degeneracy. A useful next proof route is therefore a defect-budget classification of arrangements capable of supporting 95 triangles, rather than a re-proof of the entire even-n theorem.

Segment accounting suggests only very low-defect degeneracy patterns can remain candidates; this observation is a research route, not yet a theorem.

## Claim boundary

This audit corrects source scope. It does not lower the unrestricted proved upper bound below 95, does not prove 94 globally, and does not certify optimality of the 93 construction.
