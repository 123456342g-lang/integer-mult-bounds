# Sprint claim

- Track: complex supplier; OS-random assignment seed **27** (Python `secrets.randbelow(100)`). Odd seed selects JP8 rather than CK.
- Exact base: `66849e1475c930fd7732b1a0067ffee7e1e95f60`.
- Selected result: #626 with #543, conditional kappa 0.001635527380375392. Larger pending PR titles are not accepted frontiers.
- Start: 2026-10-13 05:22 UTC (October 12, 10:22 p.m. Pacific).
- Finish target: 2026-10-13 06:55 UTC (October 12, 11:55 p.m. Pacific); stop experimentation by 06:32 UTC for verification/handoff.

## Three narrow candidates

1. JP8 B-phase frame reassignment with fixed boundary frames (related to CK #698; risks duplicating an adjacent finite-domain census).
2. CK cleanup dependency-preserving source grouping followed by coefficient reuse (related to #719/#750/#769; more involved dependency and prefix proof).
3. **Chosen:** commute the selected JP8's 8,800 zero-frame compensation additions to batch same-source coefficient preparations. Targets and sources are disjoint, so this is a rectangular additive panel with no source writes. Retain the selected native circuit and price an executable local lowering, including source access, scaling, accumulation and clearing. Check both orientations and exact prefix envelopes. No kappa claim.

## Method and bounded domain

Read the pinned #626 JP8 canonical word and local programs. Validate all compensation gates, target/source disjointness and the exact location/frame of the panel. Group its entire finite domain by source and coefficient magnitude; consider a bounded dyadic coefficient route per source. Prove the commutation/substitution identities, recount both complete local programs, and provide exact scalar checks and negative controls. No search over new helpers, frames, recursive calls, owner allocations or pending record constructions.

Expected deliverable: one isolated research construction package with verifier, exact receipt, source pins, scoped proof/cost note, independent checks and attribution.

## Coordination and overlap

GitHub GraphQL reported no pinned issue; the open issue list contains only #650 (Discussions). Claim recorded locally as instructed. The live queue refresh at selection covered 591 open PRs through #772. Relevant #698, #719, #696, #722, #734, #739, #749, #750, #755 and #769 were inspected. In particular, #739/#769 reuse coefficient work while preserving update order; #755 shares consecutive same-source magnitudes in all scalar phases; #749 changes and restores the target basis. This task explicitly changes the commuting compensation order to enable cross-target batching without a target basis change. No pending code is imported and no additive saving with concurrent work is assumed.

Prepared for @Varun-Mittal-1001 with substantial OpenAI Codex assistance. New work is Apache-2.0. Delegated checks stay within this compensation-batching scope.
