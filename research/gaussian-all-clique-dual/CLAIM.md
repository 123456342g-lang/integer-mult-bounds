# Local sprint claim

Contributor: William Lawyer, with substantial OpenAI Codex assistance.
Start: 2026-10-13 07:54:33 UTC. Expected finish: by 09:54:33 UTC.
Track: structural decoder research. Assignment seed: **40**, one operating-system
draw using Python `secrets.randbelow(100)`.
Base: `f567884aeb8851b6e794af1184119a3bfbe1e631`.

Three narrow candidates were considered:

1. Test a mixed partial-hyperplane rectangle decoder on the Gaussian E8 unit.
   PR767 leaves partial supports open, but a positive supplier would require
   a new complete cost and realization argument.
2. Test PR770's explicit hyperplane-pair dual on **all** nonorthogonal cliques,
   including non-maximal cliques. Its inspected proof expressly excludes them.
3. Extend the Gaussian scalar floor to fixed-support nonlinear messages.
   PR785 supplies this mechanism on Hurwitz geometry; that transfer offers
   less separation from existing work than the all-clique certificate gap.

Selected candidate: **2**. Seed 40 selects the second candidate by `seed % 3`;
its useful diversification is the previously excluded certificate domain.
Object: the 60 Gaussian E8 lines and PR770's 900 ordered orthogonal-normal
hyperplane pairs. Hypothesis: each nonempty nonorthogonal clique Q meets both
hyperplanes in at least `45 |Q|` ordered pairs. Test by complete integer
clique enumeration, with a separately constructed geometry and traversal.
Deliverable: a solver-free exact dual certificate closing this method's gap,
or an explicit failed-dual witness; no new kappa claim.

The live inventory retrieved at 07:58:21 UTC contains 654 open PRs through
#857 and no open issues or pinned coordination issue. Scope overlaps were
checked in PR738, PR767, PR770, PR785, PR798 and PR801; their exact inspected
heads will be retained with the result. The ledger marks PR620 partially
reviewed; pending PR claims are not accepted supplier results.
No external reservation issue is opened. This local claim is the reservation.

Research will stop by 09:24:33 UTC, leaving the final 30 minutes for verification
and handoff. One evidence-driven pivot is allowed if the proposed dual fails.

## Result update

Pending.
