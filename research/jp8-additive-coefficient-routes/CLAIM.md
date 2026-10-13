# Local sprint claim

- Track: complex supplier; fresh OS-random assignment seed **31**, generated
  with Python `secrets.randbelow(100)` on 2026-10-13.
- Exact base: `66849e1475c930fd7732b1a0067ffee7e1e95f60`.
- Object: consecutive same-source additions in the selected #626 JP8
  `full_frame_cleanup`, keeping the existing operation order and frame 1.
- Hypothesis: between different odd numerators, a positive unit source read
  bracketed by dyadic shifts can cost less than clearing and rebuilding the
  existing private coefficient stream.
- Method: enumerate routes `w *= 2^u; w += x; w *= 2^v`,
  `-16 <= u,v <= 16`, alongside existing power-of-two reuse; charge every
  source read, shift, accumulation and boundary clear. Admit only routes
  within the original positive prefix envelope and strictly cheaper than
  reset. Stop after this finite route class and the exact replay.
- Deliverable: executable finite construction, exact full scalar-projection
  replay, source pins, cost certificate, negative controls and scoped note.
- Expected finish: 2026-10-13 06:40 UTC; hard handoff before 06:54 UTC.

Three narrow candidates were considered: (0) CK cleanup additive transitions,
(1) JP8 cleanup additive transitions, and (2) private-center quarter-coefficient
factoring. Seed `31 % 3 = 1` selected JP8; #786 already covers candidate 2
and reports a larger conservative local invoice. The additive transition
class differs from #739's power-of-two-only reuse and its explicitly excluded
odd-numerator transitions. #769 covers CK power-of-two ladders; #793 instead
permutes commuting frame-zero compensation. #722, #734, #751, #755 and #787
cover equal-magnitude reuse, individual signed Horner circuits, target fan-in,
other phases, or composition. None of their implementations is imported.

Before claiming, read the selected record, construction/review, contribution
instructions, review ledger and preserved-research index. Checked open PR
metadata through #799 at 05:53 UTC. GitHub returned no pinned coordination
issue; the only open issue was #650 about Discussions. This file records the
claim under the requested fallback. No separate reservation issue is opened.

Contributor: Ryan Haines (@Ryan-Haines), with substantial OpenAI Codex
assistance. New material is Apache-2.0. Result and handoff will be recorded
once after verification.
