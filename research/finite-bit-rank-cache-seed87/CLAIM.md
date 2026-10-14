# Finite-bit repeated-transition rank cache

Claim recorded 2026-10-14 03:05 UTC. Expected finish 03:37 UTC.
Track: verification engineering. OS-random assignment seed: 87.
Base: `680967accfd4311f3241dc154e1f434869747b43`.

Investigate exact repeated frame-pair ranks inside
`scripts/finite_bit_contract.py:inspect_candidate`. Intern normalized rational
frames and reuse a rank only for an identical ordered pair within one call.
Preserve validation, every physical edge, edge order and the full result.
Deliver an opt-in source-pinned patch, complete same-input differential replay,
failure controls and before/after measurements. Frozen scripts and certificates
stay unchanged; this is verifier tooling, with no new kappa claim.

Three candidates considered: repeated finite-bit edge ranks; Fano graph
reachability; prime-subset exact arithmetic. The complete Fano profile spent
0.305 of 0.430 profiled seconds in `inspect_candidate`. Prime-subset screening
took 0.068 seconds and scalar Fano replay 0.008 seconds. The selected target
has repeated work across larger rank-product and block-core fixtures too.
Seed 87 fixes the rational perturbation/mutation test stream.

Initial overlap: 719 open PRs with complete pagination, cached at 03:02 UTC;
local package notes and review ledger; 83 discussion threads and their comments
refreshed immediately before this claim. No pinned coordination issue exists,
so this claim is local as requested. PR808 changes cyclic routing-state search,
not exact edge-rank evaluation. PR1234 and PR1459/1461 address rational span
normalization/containment, not this checker. No matching active claim found.
Titles alone were not used: the repository overlap helper searched PR bodies,
cached discussion comments/replies and local package metadata. Its live refresh
timed out, so the direct discussion inventory supplied the freshness check.

Acceptance: full receipt equality on unchanged Fano and nonzero rational
rank-product/block-core fixtures; all existing relevant tests on both engines;
invalid input and between-call mutation controls; same-input alternating-order
wall-clock benchmark. No timing threshold is a mathematical acceptance rule.
Stop implementation by 03:27 UTC, reserving the final ten minutes for checking
and handoff. Contributor: Sagar Thakrar, with substantial OpenAI Codex assistance.
