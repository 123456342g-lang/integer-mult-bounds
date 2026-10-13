# Local sprint claim

- Track: bit supplier; assignment seed **1**, sampled with the operating system's
  cryptographic RNG by rejecting bytes >= 200 and reducing modulo 100.
- Draw time: 2026-10-13 15:43:50 UTC.
- Base: `407d52ff15b2217b6e22bce44728b4c3907b6515`.
- Selected result at base: conditional kappa `1661960547713947/10^18`,
  PR942 T37 with unchanged PR589/555 bit supplier. Followed the selected
  source manifest, assembly, batch952 maintainer review and PR ledger.
- Object: composition of the retained phase-B frame 507/508/519/524 schedules
  from PR880/873/908/914 on the actual PR589 word, including literal cleanup.
- Method: deterministic exact integer maps, positive reverse domination,
  full dirty-column and exported-record replay; enumerate all 16 subsets of
  these four replacements and price the complete word. No circuit search.
- Expected deliverable: source-pinned finite composition witness and verifier,
  explicit cost and precision accounting, mutation controls and scoped note.
- Expected finish: 2026-10-13 16:24 UTC (09:24 America/Los_Angeles).

Three alternatives considered: (1) another single-frame positive factorization;
(2) changing the frozen PR589 gate-frame assignment; (3) composing disjoint,
reviewed, reverse-dominated phase-B schedules. The third was chosen because
single frames are crowded and the fixed-word frame-only search is already
closed. Seed 1 chose the phase-B, reverse-dominated composition route from
these alternatives; it did not license repeating the existing seed-1 frame267
search. The bounded object is these four schedules, not all possible splices.

Coordination checked through Curiosity Bot's GitHub issues/PR provider and live
issue listing. No pinned sprint issue was present (only issues 913 and 650), so
this is a local claim. Reviewed the retained batch932/batch952 ledgers and
negative results in r439-bsection-survey and bit589-frame-optimum. The former
excludes single-write whole-block searches on several frames, not composition
of their already constructed factors. Recent PR973 changes frame509; PR980
changes phase A and explicitly does not compose phase B; PR941/965/967 change
D. None of those pending implementations is consumed here. Live PR metadata
will be checked again before handoff.

One delegated worker checks only these four block maps independently. Another
prepares only their native multistage harness. Substantial OpenAI Codex AI
assistance is disclosed; no independent human review is claimed.
