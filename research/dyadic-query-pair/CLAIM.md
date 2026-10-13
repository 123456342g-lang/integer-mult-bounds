# Seed 54: fuse two completed native BIT shears

Claim recorded 2026-10-13 at 06:20 UTC (01:20 America/Chicago).
OS randomness (`secrets.randbelow(100)`) returned **54**: recursive interfaces.
Exact fresh `origin/main` base: `7ee02b7c96d85f22b38d28bd7ed49bb8c1aeb261`.
Primary checkout observed at PR756 head `4fad623a1e4ca06959f4326e221c2f8d9125c269`;
it and PR805's branch/worktree are reserved for their existing workers.
This work uses the isolated managed `seed54-boundary-interface` worktree.

## Selection and hypothesis

Three narrow candidates were considered: a shared-output dirty echo, a new
Gaussian boundary batch interface, and fusion of two completed native BIT
address shears. PR714/730/744/758/784/788 already cover many echo/checkpoint
classes; PR481 already prices the Gaussian batching mechanism. The third
candidate has a different object and permission contract and is selected.

PR521 supplies a one-child native unipotent query `h`. PR677 completes the
DATA shear `S_h: x ^= (h+I)y` with two queries on the target and no private
row. Investigate the completed pair `S_(h^a) S_(h^-a)` for `a=2^j`, using
the explicit six-affine/one-child lowering of `h^k` at dyadic `k`. Hypothesis:
`h^-a; XOR_y; h^(2a); XOR_y; h^-a` replaces four children by three and four
XOR scans by two, restoring every input except the prescribed target.

Method: derive the literal lowering over the rationals and every odd residue
ring; prove the endpoint over F2-valued full arrays; check full small ADDRESS
domains by a separate coordinate/permutation implementation; prove a
three-query lower bound in an explicitly scoped query/XOR model. Seed 54
selects the large fixed coefficient fixture `a=2^54`. Coverage includes
`j=0..54`, both signs, full-order/shorter/fixed orbits and dyadic modular
specializations. No randomized search or stronger-bound search is planned.

Price the optimistic complete typed recurrence before implementation:
three ordinary ADDRESS children, each on full BIT volume `V/3` and width
`N/3`, eighteen ordered affine scans, two aligned XOR scans, coefficient
preparation, primitive work, source access, routing and all head returns.
Compare against the completed four-child pair, including its twenty-four
affine scans and four XORs. No clean/disposable/borrowed full private row.
Primitive and child workspace remain paid. Growing `j` is not free.

Expected deliverable: scoped recursive-interface construction and written
query bound, standalone exact checker/certificate, full cost/storage limits,
source pins, negative controls and one focused PR; **no new kappa**.
Expected finish: by 07:15 UTC (02:15 America/Chicago). Reserve at least the
final quarter for verification, overlap refresh and handoff.

## Coordination and concrete non-overlap

No pinned issue exists (GitHub GraphQL `pinnedIssues` returned empty).
Immediately before this claim, live metadata covered 627 open PRs through
#814. No centered native query-pair fusion was found. The review ledger
marks PR521 and PR481 unreviewed; citation does not imply maintainer approval.
The selected record is PR741, conditional kappa `0.001661202643272239`;
its review, actual SW4 construction and source manifest were inspected.

PR756 is a performance change to a historical balanced-Fano enumeration.
This package touches no such checker, searches or performance receipts.
PR805 changes real rational cyclic leaves and restoration of one dirty
array plus a scalar. This package instead concerns exact odd-ring ADDRESS
permutations acting on F2 VALUE arrays, with queries on the genuine DATA
target and no full private row; it imports none of PR805's leaf construction,
restoration interface, code or verification. Both live PR descriptions and
relevant diffs were read. Neither existing PR will be changed.

Prepared for **Wentao Li** (GitHub `VictorLiwentao`) with substantial OpenAI
Codex assistance. Predecessor names and notices will be retained. Apache-2.0.
