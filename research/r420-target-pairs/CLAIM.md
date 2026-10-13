# R420 target-pair compensation claim

- Track: bit supplier. Assignment seed: **13**, drawn from OS randomness on
  2026-10-13 at 04:23:54 UTC.
- Base: `66849e1475c930fd7732b1a0067ffee7e1e95f60`.
- Object: the 120 target rows of the frame-zero D compensation matrix in
  eumemic's PR543 R420 word, source commit
  `2065fe4f72a914d907f1046603f5a36f17018535`.
- Method: score all 120 × 119 oriented target pairs, then use seed 13 to
  break ties in one greedy disjoint matching. Restore the target basis inside
  D and charge both target-to-target gates per pair. Check the full dirty-input
  operator, unchanged frame paths, scalar counts and positive-prefix growth.
- Deliverable: one frozen finite circuit, exact reproducible checker, mutation
  controls and a scoped research note. No new kappa or hosted invoice claim.
- Finish target: 2026-10-13 05:04 UTC. Verification and handoff begin by 04:54.

The three candidates were fixed-order phase-B frame optimization, phase-A quad
synthesis, and target-row compensation factoring. PR661 already closes the
first class; PR691 and PR670/674/688 cover quad/block circuit synthesis.
PR686/694 factor helper columns in D. This claim factors target rows while
leaving every helper untouched. Older target-factoring work, including PR476,
is checked for relevant precedent and credited in the final note.

At selection, GitHub reported no pinned issues. An overlap refresh inspected
all 520 open PRs and searched their titles and bodies for target-pair, target
basis and row-factoring work. The claim is local because no pinned coordination
issue exists. Delegated work stays within this D-stage construction.

Contributor: Sagar Thakrar, with substantial OpenAI Codex assistance.
