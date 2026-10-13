# Local sprint claim

- Track: independent verification (assignment seed **80**, drawn with
  `secrets.randbelow(100)` from OS randomness on 2026-10-13).
- Exact base: `66849e1475c930fd7732b1a0067ffee7e1e95f60`.
- Claimed at 2026-10-13 04:45 UTC; expected finish by 05:05 UTC.
- Object: the 120-by-420 dirty-helper correction map of the accepted PR543
  R420 bit word, consumed unchanged by selected PR626.
- Method: independently propagate target observables backward through
  A/scatter/B (transpose circuit, rather than forward register expressions).
  Compare the resulting helper coefficients with D; certify rank by an
  explicit invertible minor and derive the entire right kernel. Seed 80
  rotates the helper-column pivot order and selects control targets.
- Deliverable: source-pinned standard-library verifier, exact certificate,
  rejecting controls, and a scoped linear-summary dimension consequence.
  No new circuit, runtime saving, kappa, or full multiplication theorem.

Three candidates considered: selected cold-wrapper identities (overlaps
#702 and our #712), selected moment inequalities (overlaps #678/#706),
and this correction-map rank/kernel certificate (chosen). Existing PR543
`xcheck.py` already verifies K=D by forward symbolic propagation; this run
adds a different propagation direction and explicit full-rank/kernel evidence.
The recent #686/#694 helper-basis and #713/#716 target-basis constructions
optimize D but do not claim this certificate. #612 formalizes boundaries/B;
its D compensation equality remains open. None of those pending patches is
consumed here. The fixed-frame search #661 does not exclude circuit changes.

The refreshed open-PR queue included #716. There were no pinned issues and
Discussions was disabled; no separate reservation issue was opened. No
workers were delegated. Scope is a fixed finite object, not a search for a
stronger bound. Stop after exact rank/kernel and control checks are complete.
The first 20% is reserved for selection and the final 25% for verification
and handoff.
