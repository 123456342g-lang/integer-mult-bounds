# Seed-71 sprint claim

- Contributor: William Lawyer, with substantial OpenAI Codex assistance.
- Track: adversarial mathematical audit. Fresh OS-random seed **71**, from
  one `secrets.randbelow(100)` draw.
- Exact base: `7ee02b7c96d85f22b38d28bd7ed49bb8c1aeb261`.
- Start: 2026-10-13 06:32:08 UTC. Finish by 08:32:08 UTC
  (00:32:08 to 02:32:08 America/Denver). Final 30 minutes reserved for
  verification and handoff, beginning no later than 08:02:08 UTC.
- Subject: the integer-power norm assumption in PR803, Result and Section 5,
  at `d213ac12d4a1ab8f717d942e844df318ceb395fb`.
- Exact question: can cycle-product magnitude one and small local deviations
  from unit weights replace pointwise unit magnitude when transferring a
  scalar circle bound to the induced infinity norm of a weighted permutation?
- Method: derive a cycle-local power-norm criterion, construct exact rational
  near-unit balanced cycles, and compare independently computed resolvents
  with the inherited degree/circle-gap bound. Include a sufficient perturbation
  guard and positive unit-phase cases. No floating arithmetic proves a claim.
- Expected deliverable: a scoped hypothesis audit, explicit exact witnesses,
  a standalone checker and meaningful invalid-shortcut controls. No new kappa,
  implementation speedup or defect in PR803 is presumed.

## Selection

Three candidate obligations in PR803 were inspected: (0) the Hardy/Schur
coefficient inequality and its infinite limit; (1) the rational projection
crossing count in the arc-length argument; (2) the operator substitution and
unit-phase premise under weight perturbation. Seed `71 mod 3 = 2` selects
candidate (2). The first two already have elementary proofs and supporting
finite checks in that package. The selected question adds a distinct
operator-admission boundary, rather than repeating its analytic proof.

The required contribution guide, selected certificate, current status and
central review ledger were read. The certificate was followed to the #741
construction, its maintainer review, and the #589 bit construction. The accepted
conditional kappa at that base was `0.001661202643272239`; this audit does not change or
re-audit that construction.

The ledger's retained scope and negative-result index were inspected. PR673's
priced all-role adapter is a closed negative result and is not reopened.
Related PR692 already supplies the standard cycle-local geometric resolvent
and bilinear dual for unit phases; PR764 sharpens scan rounding; PR805 changes
the dirty-leaf contract. PR803 itself rejects a nonunit constant phase and an
incorrect scalar-to-matrix norm shortcut. This audit instead targets arbitrarily
small nonunit deviations with *exactly unit cycle products* and quantifies the
missing power-norm factor. PR832's concurrent Sobolev bound retains unit
operators and addresses another analytic estimate.

An immediate pre-claim inventory contained 646 distinct open PRs through #833.
Targeted searches for nonunit/nonnormal/weighted-cycle/power-bounded/holonomy
work found no matching claimed scope in the inspected titles and bodies.
This is a metadata overlap check, not a claim about all unpublished work.
The only open issue was #650, which requests Discussions; no pinned sprint
coordination issue was visible. This local claim follows the permitted
fallback. No reservation issue or remote claim is posted.
