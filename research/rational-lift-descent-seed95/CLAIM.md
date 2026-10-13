# Local cycle claim

Claimed 2026-10-13 18:34 UTC. Finish by 19:07:23 UTC, with verification and
handoff beginning no later than 18:57:23 UTC.

- OS-random seed 95, research consolidation.
- Base `ba82555c64e1879e4b7decce28186f208fcb8262`.
- Branch `research/cycle06-seed95-rational-lift-descent`.
- Exact object: the fixed-reader single-lift identity for a rational matrix X,
  and the attainable supports of its original and added rank-one terms.
- Hypothesis: every lift over a characteristic-zero extension of Q has a
  rational lift preserving each term's support pair, hence every support-only
  copy cost. A finite-field example should show why descent needs a field-size
  condition.
- Method: consolidate the reciprocal-projection proof in the retained
  `p112-complex-single-lift` package into a finite-dimensional linear-functional
  argument over an infinite base field. Check exact quadratic-extension
  witnesses and a minimal F4-to-F2 failure independently of predecessor code.
- Deliverable: written theorem and boundaries, exact runnable certificates,
  source pins, negative controls, and a concise cycle handoff. No new kappa,
  supplier implementation, global regeneration, or selected-frontier edits.

Three candidates were considered. U8 terminal-cone cleanup is already covered
by PR988 and its reviewed package. The selected PR1042 invoice is covered by
PR1112, with cell semantics covered by PR1049 and owner maps by PR1091. Rational
descent of support patterns is distinct from these and from PR1098's label-free
Gram spectra. No reservation issue is opened. The immediately preceding scan
covered all 774 open PRs through #1120 and recent issue comments; the repository
has no pinned sprint issue. The claim therefore stays local.

Acceptance: a proof valid for every finite X over the stated field, exact
support equality for the finite examples, explicit rejection of wrong direct
projection and missing support constraints, and a valid finite-field boundary
counterexample. Finite examples alone will not be described as the theorem.
This is a support-only consolidation, so there is no optimistic paid supplier
to implement or cost improvement to claim. Precision, restoration, hosting,
tape, and compiler costs remain outside the theorem.
