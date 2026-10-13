# Local sprint claim: transposed private work

- Track: complex supplier; fresh OS-random seed **25** (`secrets.randbelow(100)`).
- Exact base: `c290b7b919790300e14004a75d8d24b55ca3c5b5`.
- Current accepted result: #741/#589, conditional kappa
  `1661202643272239/1000000000000000000`; read its certificate, construction
  and maintainer review. This experiment deliberately uses historical #626.
- Exact object: the inverse-transpose companion of the fixed-source JP8
  cleanup blocks constructed in #811, including varying magnitudes and
  positive numerator-changing source reads.
- Method: transpose each literal private-work circuit in reverse order,
  reverse the sign of updates into the original source, and check all dirty
  native/private inputs, complete prefix envelopes and all costs. Compare
  with #751's equal-coefficient reverse-Horner result. No larger search.
- Deliverable: standalone pinned companion construction, finite exact
  certificate, independent block check, negative controls and cost note.
- Expected finish: 06:45 UTC on 2026-10-13; handoff before 06:54 UTC.

Three candidates: (0) CK numerator-changing forward reuse; (1) JP8
inverse-transpose continuation; (2) transport coefficient reuse into #741.
Seed `25 % 3 = 1` selects the second. Candidate 0 repeats the recent forward
mechanism; candidate 2 requires a wider interface audit. This claim concerns
the backward dual, not another forward coefficient search.

Checked open metadata through #811, #751 at
`7a1a3a319da359ec8b6e83230a7fcf7733fac8e5`, #739, #793 and the review ledger.
#751 handles 999 equal-magnitude fan-in runs; #739/#811 report no backward
same-source join. This extends the backward circuit class to the transposes
of their varying-magnitude continuations. #793 changes compensation order.
There is no pinned sprint issue; the issue list only contains #650 about
Discussions. This file is the local coordination fallback. #811 will be
pinned at its completed historical-assembly update, with full attribution.

Contributor: Ryan Haines (@Ryan-Haines), with substantial OpenAI Codex
assistance. Apache-2.0. Result and handoff will be recorded once after checks.
