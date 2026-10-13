# Ordered dirty echo under a scratch budget

- Track: recursive interfaces; OS-random assignment seed **56** (`secrets.randbelow(100)`).
- Base: `66849e1475c930fd7732b1a0067ffee7e1e95f60`.
- Claim time: 2026-10-13 04:42 UTC; expected finish: 05:17 UTC.
- Object: the ordered multiway dirty echo from PR #673 at
  `bfff94e78f0e75ebd2593e3cc7710ae5290e8be3`.
- Method: exact interval dynamic programming for ordered binary/ternary
  composition trees, with arbitrary positive integer leaf costs and a hard
  peak scratch-array budget. No factor permutation or new leaf operation.
- Deliverable: written complete cost recurrence, a small reproducible optimizer,
  exact witnesses, and independent nonlinear restoration/linear product checks.
- Stop rule: one package; finish experimentation by 05:07 UTC and reserve the
  remaining ten minutes for verification and handoff.

No pinned coordination issue existed at the initial GitHub check. This local
claim replaces a public reservation. Open PRs were checked through #709.

Three candidates considered: common Fourier boundary fusion (the existing
`fourier-boundary-fusion/REPORT.md` already supplies a strong obstruction),
Gaussian RHS boundary batching (#481 already supplies that construction), and
scratch-budgeted ordered dirty composition. The third was chosen because
#663 establishes the binary count and #689 optimizes balanced ternary uniform
costs, but #689 explicitly excludes unbalanced splits and unequal leaf costs.
Seed 56 selects the binary/ternary mixed-tree class (2 + 56 mod 3 = 4 is the
first scratch-budget probe); it is not used as evidence of novelty.

The selected conditional result is
`51110230636731/31250000000000000 = 0.001635527380375392`, as bound by
`certificates/selected-result.json` to #626 and its maintainer review.
This work does not change that record or `upstream/` and does not assert a
new multiplication exponent.

Prepared for Sagar Thakrar (@thakrarsagar), with substantial OpenAI Codex
assistance. Apache-2.0. Predecessor attribution and exact source pins will
accompany the completed result.
