# Sprint claim

- Track: verification engineering. OS-random assignment seed: 94.
- Base: `66849e1475c930fd7732b1a0067ffee7e1e95f60`.
- Object: PR621's standard-library prime-power cyclic-inverse verifier,
  specifically zero-coefficient row updates in exact cyclotomic elimination.
- Method: compare the original and a zero-skipping implementation on the same
  eight shipped cases, then exercise singular and pivot-swap controls. Seed 94
  selects the additional right-hand sides `(zeta_q^94, 94)` at q=3,4,5.
- Deliverable: one scoped tooling improvement, exact receipt comparisons,
  same-input timings, and a reproducible command. No new mathematical bound.
- Expected finish: 2026-10-13 05:26 UTC, 10:56 IST.
- Coordination: no pinned issue existed when checked. Open PRs through #720
  were inspected. #668's modular CRT resultants extend coverage to larger
  orders; this task accelerates the existing exact elimination and retains
  its Bezout solve. #662/#667/#672/#707/#709 concern other kernels.
- Candidates considered: selected-source hashing, independent owner-check
  arithmetic, and cyclotomic elimination. Hashing was already short, and owner
  arithmetic overlapped pending work. Seed 94 directs this run to the older
  exact verifier rather than another selected-frontier kernel.

Prepared by thakrarsagar with substantial OpenAI Codex assistance.
