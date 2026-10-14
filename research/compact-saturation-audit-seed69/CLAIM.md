# Compact saturation audit claim

Claimed 2026-10-14 01:04 UTC. Track: adversarial mathematical audit.
OS-random assignment seed: 69, drawn with Python `secrets.randbelow(100)`.
Base: `410026dc5513b87db92ae98571d1d5984c69a983`.
Expected finish: 2026-10-14 01:47 UTC; hard session budget ends 01:57 UTC.
Verification and handoff start by 01:42 UTC at the latest.

Question: for the unchanged earlier-source compact-control word, what is the
exact complete-map agreement criterion when temporary digits may saturate,
and what is the largest subset of that agreement set invariant under the
intended selected-bit XOR? Test whether agreement alone suffices for repair.

Dependencies: Douglas Colkitt's retained movement note and physical simulator;
Hanson Sun / bbMisk's PR1219 at
`dfb453c88b03868d346014867a091d36e7b16589`; the adjacent one-digit PR1108 at
`b76bb2853be4e7001508582b10913e32ad7aba9f`. PR1247 at
`392316a45197ef213cff4febd24aa7fd5e16237f` is later-source work outside this scope.

Method: derive target/compact carry recurrences, exact weighted transfer
counts, then compare an independent integer implementation with complete
small permutations and the original physical interpreter. The all-n domain
is n>=1, G>=1, K>=G+1, 0<=rho<K. Finite domains and seed-69 samples will be
recorded separately. Seed69 chooses G=1+(69 mod 2)=2 for the headline fixture.
Stop after the proof, finite-domain checks and one scoped package; do not
search supplier profiles or claim a runtime or kappa improvement.

Three candidates considered: this saturation/invariance boundary; PR1197's
two-total quotient obstruction; PR1367's tangent-to-orbit regularity step.
The latter is already a second audit in a busy rigidity family. The former
changes PR1219's explicit nonsaturation hypothesis and targets multi-digit
compact carries, distinct from PR1108's one-digit law and PR1247's two-pass
later-source guard. It is not another nonsaturated guard census.

No pinned coordination issue exists, so this is the local claim authorized by
the task. The immediately preceding overlap report covered 823 open PRs and
158 discussion records with complete pagination, fetched at 01:01:21 and
01:01:51 UTC. It found PR1108, PR1219 and PR1247 as the relevant predecessors.
The review ledger and local research notes were also inspected. Text search
does not establish novelty. Refresh metadata before submission.

Expected deliverable: written scoped proof, exact counts and counterexamples,
one reproducible standard-library verifier, pinned sources and negative
controls. Prepared by Sagar Thakrar with substantial OpenAI Codex assistance.
Apache-2.0. No subagents or independent human review.
