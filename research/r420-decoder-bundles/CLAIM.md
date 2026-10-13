# Local sprint claim

- Track: bit supplier. Assignment seed 19, drawn with Node crypto.randomInt(100), backed by operating-system randomness.
- Base: `66849e1475c930fd7732b1a0067ffee7e1e95f60`.
- Started: 2026-10-13 04:49 UTC. Expected finish: 05:30 UTC. Final verification begins no later than 05:20 UTC.
- Object: the nine FULL-frame phase-A decoder totals of eumemic's PR543 R420 bit word.
- Hypothesis: restored bundles of at least three non-retained operand registers can improve on the disjoint-pair mechanism in PR708, after paying preparation, restoration and literal reverse cleanup.
- Method: exact enumeration of small bundles, followed by one bounded disjoint selection. Preserve every frame path and arbitrary dirty inputs; recompute positive scalar growth. Seed 19 fixes tie ordering.
- Deliverable: one frozen circuit and exact verifier, or a scoped negative result if the paid budget fails. No new kappa claim.
- Three candidates considered: phase-B block resynthesis, phase-A quad synthesis, and decoder bundles. PR670/674/688 cover block rewrites and PR691 covers quad synthesis. Bundles change the search class beyond PR708's pair matching.
- Coordination check: GitHub pinnedIssues returned an empty list; no separate issue opened. Open PR metadata inspected through PR720. PR708 is the direct predecessor and will be credited and pinned; PR686/694 cover frame-zero compensation, a different circuit.
- Contributor: Sagar Thakrar (@thakrarsagar), with substantial OpenAI Codex assistance. Apache-2.0.
