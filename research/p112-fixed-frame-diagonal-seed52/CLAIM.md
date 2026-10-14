# Seed 52 claim: alternate supports for a fixed P112 frame cover

- **Track / assignment seed:** Structural decoder, OS-random seed 52.
- **Base:** `bce54fb3f895cbe5cd4c0eb477c3afeed100190f`.
- **Predecessor:** PR #1347 (`64fd5f9e91961dedc16118fcc7ad71ee82efe28f`), especially its exact frame-only `COVERING.json` and bounded `DIAGONAL-SEARCH.json`.
- **Coordination claim:** [discussion #1163, comment 18911792](https://github.com/CrocSwap/integer-mult-bounds/discussions/1163#discussioncomment-18911792).
- **Recent overlap check:** refreshed open PRs and the pinned coordination discussion at 2026-10-14 00:05 UTC. PR #1347's refinement kept one first-enumerated representative per frame pattern; no current claim covers all representatives for its fixed ten patterns. Nearby claims #1316 (one odd free rectangle with a coordinate term), #1360 (rank-nine factorizations), and #1342 (one asymmetric-unit replay) concern other domains.

## Candidate selection

Three bounded candidates were compared. Seed `52 mod 3 = 1` selects candidate 2.

1. Jointly select ten maximum-hit frame patterns from the complete 5,376-pattern dictionary while imposing diagonal coverage. Deferred: this broadens PR #1347's explicitly open full-dictionary next question.
2. Keep the ten frame-hit masks in PR #1347's fixed `COVERING.json`; enumerate every maximum-hit rank-six support representative in each mask class, then decide whether one representative per class can cover all 112 live diagonals. **Selected.** This varies the omitted support representatives while holding the frame cover exactly fixed.
3. Extend the P112 two-coordinate free-rectangle audit to the first open 24-row support size. Deferred because it is adjacent to PR #1375 and active claim #1316.

## Hypothesis and exact scope

For the ten distinct frame-hit masks induced by the ten terms in PR #1347's `COVERING.json`, replacing each term by any other rank-six support triple with the same frame-hit mask preserves all 1,260 frame counts exactly. The question is whether one such triple per mask can make the union of the ten diagonal support masks equal the full 112-live-line set.

Enumerate the complete finite domain: 7,616 rank-seven tagged parent pairs, each with its 127 nonzero cut words (967,232 parent/cut cases). Retain precisely the cases with 1,120 frame hits and one of the fixed ten frame masks. Within each mask class, support triples whose diagonal mask is a subset of another triple's mask are safely dominated for this coverage question; keep the inclusion-maximal masks and exhaustively solve the one-per-class coverage problem with exact bit masks.

This is a support-only necessary-condition audit. A feasible tuple would not solve coefficient equations or produce a decoder. An infeasible result applies only to these ten fixed frame masks and says nothing about other ten-pattern covers, lower-hit terms, helper costs, or kappa.

- **Expected artifact:** source-pinned exact enumerator and verifier, complete candidate and Pareto counts, exact feasible tuple or exhaustive negative certificate, mutation controls, scope/assumption statement, and a concise handoff.
- **Reproducible entry point (planned):** `python3 -I -O -B research/p112-fixed-frame-diagonal-seed52/verify.py`.
- **Expected finish:** 2026-10-14 01:15 UTC; claim expires 02:05 UTC.
