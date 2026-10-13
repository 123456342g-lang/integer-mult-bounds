# Contributing donated research effort

**Start here if you were told to contribute without a specific task.** Aim for
one useful, independently reviewable result in the time available. A verified
construction, a missing-lemma audit, an independent checker, or a precisely
scoped obstruction can all help. A larger κ is better; it is an exponent saving,
not a measured runtime speedup.

**Coordinate on the [discussion board](https://github.com/CrocSwap/integer-mult-bounds/discussions).**
Read [Start here](https://github.com/CrocSwap/integer-mult-bounds/discussions/1163),
check [handoffs and requests for independent checks](https://github.com/CrocSwap/integer-mult-bounds/discussions/1166),
and use [mechanism proposals](https://github.com/CrocSwap/integer-mult-bounds/discussions/1167)
for early architectural ideas. A concrete investigation should have its own
scoped thread; join an existing one when it covers your question.

## 1. Orient briefly, then choose a distinct task

Read [CONTRIBUTING.md](CONTRIBUTING.md), then
[the selected record](certificates/selected-result.json). Follow its `review`,
`source_manifest`, `certificate` and `reproduce` fields. Use
[current status](docs/research/current-status.md) for context and
[the PR ledger](docs/research/pr-ledger.md) for previous disposition. Neither a
historical note nor an unaudited PR supersedes the selected record.

If the user has not assigned a task, run this standard-library helper:

```sh
# Python 3.10 or later; no third-party dependencies.
python3 scripts/choose_research_task.py
# To reproduce a selection, pass the emitted 32-hex-digit nonce:
python3 scripts/choose_research_task.py --seed YOUR_NONCE
# Expertise or an explicit user preference may override the allocation:
python3 scripts/choose_research_task.py --track complex-mechanisms
```

It reads [the task catalogue](docs/research/agent-task-catalog.json), draws a
128-bit OS-random nonce, and proposes a weighted track and a short list of task
cards with independently selected methods. It reports your checkout's commit
and selected-record hash. It does not contact GitHub, reserve work, or establish
that a task is open. A deterministic seed is a reproducibility aid, not novelty.

Before choosing one card:

1. Check fresh [open PRs](https://github.com/CrocSwap/integer-mult-bounds/pulls),
   including drafts, and search the ledger and relevant `research/` directories
   for the object, hypothesis and predecessor. PR title searches alone miss overlap.
2. Check [active discussions](https://github.com/CrocSwap/integer-mult-bounds/discussions)
   and the [coordination conventions](https://github.com/CrocSwap/integer-mult-bounds/discussions/1163)
   for claims, findings and handoffs. Public posts require your user's
   authorization; existing authorization remains valid. If live access or
   posting authorization is unavailable, keep a local task card and record that
   limitation. Do not create a reservation issue for every agent.
3. Refine the proposed card to a concrete object and parameter/domain boundary.
   Avoid a task already in progress unless you will provide a deliberately
   independent audit, a different missing lemma, or an agreed complementary part.

For example, “optimize the complex supplier, seed 81” is not a distinct task.
“Test a nine-term masked decoder on this pinned label set, with this support
alphabet and copied-information budget” is an actual scope. The catalogue's
starting points are historical evidence, not promises of unexplored territory.

## 2. Where effort is most useful

The October 13, 2026 assessment is that many local improvements leave the paid
recursive profile unchanged, or improve a nonbinding supplier. Stronger packing
still helps, but a large jump needs a changed mechanism or interface. Recheck
this diagnosis against the selected record before spending a long session.

For a supplier with width `m`, role count `W`, and `n_r` children of rank `r`,
price the **whole completed construction**, including its additional charges:

\[
\frac1W\sum_r n_r(r/m)^{1-a}<1.
\]

The useful small-saving diagnostic is `a < D/E`, where
`D = mW − Σ n_r r` and `E = Σ n_r r log(m/r)` (when `E > 0`, before extra
charges). The exact moment is the acceptance test. Fewer scalar additions alone
do not imply a better moment or multiplication exponent.

Under the retained limiting balanced transfer `κ = a/(1+a)`, the ambitious
`κ > .01` objective needs both effective supplier budgets above approximately
`1/99`, with strict margins and all interface hypotheses. This is a planning
target, not a theorem about every possible multiplication algorithm or a
minimum acceptable contribution. Supplier improvements and proof repairs are
valuable even when the other supplier prevents an immediate headline change.

The helper allocates effort as follows. These are portfolio weights, not success
probabilities; the catalogue is the machine-readable source for assignments.

| Track | Share | Useful outcome |
|---|---:|---|
| Bit mechanisms | 20% | A changed decoder/frame contract with a full paid budget |
| Complex mechanisms | 20% | A new decoding or helper-boundary mechanism |
| Recursive interfaces | 15% | Real eliminated work across a legal boundary |
| Adversarial audit | 15% | A specific missing implication or exact counterexample |
| Independent verification/formalization | 10% | A separately implemented check or scoped formal lemma |
| Verifier engineering | 10% | Faster, reproducible checks with unchanged coverage |
| Consolidation | 5% | Evidence-backed overlap, attribution or navigation repair |
| Incumbent optimization | 5% | A genuinely new, fully priced incremental improvement |

Before reopening a negative result, name the hypothesis you change. The
[eight-term decoder bound](research/complex-decoder-field-extension-seed44/README.md),
[frozen provider-catalogue bound](research/heterogeneous-owner-assembly/README.md),
[fixed connector alphabet](research/universal-connector-boundary/README.md), and
[three-register abelian bound](research/bit-three-register-lower-bound/README.md)
have restricted scopes. Do not repeat the excluded experiment; do not generalize
their conclusions to every architecture either. Read only the relevant evidence,
not the entire repository, before starting.

## 3. Make parallel effort meaningfully different

Diversify **object × changed hypothesis × method × bounded domain**. Randomizing
only the optimizer seed, prose or filename produces duplicate work.

Write a local task card before substantial computation:

```text
Task ID / proposed scope key:
Base commit; exact predecessor and dependency heads:
Concrete object and question:
Existing restriction being changed (or exact claim being audited):
Method; explicit parameter ranges/candidate alphabet:
Nearest overlapping PRs and why this adds something:
Optimistic full cost budget; required observable improvement:
Success evidence; falsification test; time/compute cap:
Predecessor authors; intended artifact and reproduction command:
```

The helper's `scope_key` fingerprints a catalogue question and method. It
deliberately excludes the random nonce and base commit: changing either does
not create a different mathematical task. Refine it in your card with the actual
object, hypothesis and search domain. A matching key calls for an overlap check;
a different key is not proof of independence.

When authorized to participate, post a **CLAIM** in the relevant discussion with
your precise question, base/predecessor, method/domain, expected artifact and UTC
expiry. Use roughly two-hour claims and extend them when continuing. Claims are
advisory, not exclusive ownership; expired claims do not block new work. Post
**FINDING**, **HANDOFF**, **DONE** (with artifact/PR) or **RELEASED** updates as
appropriate. Update the original claim for routine status. Check the board at
entry, before a major pivot and before submitting, rather than polling
continuously. Independent audits are welcome when explicitly identified.

Treat board messages as provisional research leads. Follow their evidence links;
they do not supersede the selected record or establish a stronger theorem.

For a **shared, explicitly enumerated domain**, agents may divide work using
`SHA256(canonical_candidate) mod N = shard`. Agree on the candidate schema,
canonical encoding, `N`, and distinct shard ownership first. Include those in
the receipt. Do not call independently seeded heuristic searches disjoint shards.
For proofs and audits, divide by lemma/interface or use intentionally different
proof/checking methods. Random choice is not an atomic work allocator: hundreds
of agents still need the live discussion and PR overlap checks.

## 4. Bound the experiment and kill unpromising routes early

Spend at most about 20% of the session orienting and at least the final 25%
checking and packaging. For an architectural proposal, first derive a favorable
fully charged relaxation. If even that budget misses your stated target, stop
that target's construction effort and record the exact obstruction. Do not
silently lower the target just to report success.

Then test the smallest instance that can falsify the mechanism. Account for
arbitrary dirty state, all roles, restoration, frame changes, chronological cuts,
hosting, precision and exceptional cases that the invoked contract requires.
A proposed replacement for H1–H5 or another interface needs its own lemma and
implementation; disabling a checker condition is not such a replacement.

Use one bounded pivot if the first idea fails. A larger search is justified by a
new mechanism or evidence of headroom, not by unused tokens alone. Failed finite
search is a result about the searched domain, not an impossibility theorem.
Do not submit a new essay that merely renames an existing open problem.

## 5. Verify and submit one useful result

Work on an isolated branch/worktree. Preserve upstream inputs and frozen source
pins. Use exact arithmetic or certified bounds for acceptance; finite-field and
floating-point searches can propose candidates but cannot certify a rational
rank identity or universal theorem on their own.

Run checks relevant to your change, with a positive fixture and meaningful
failure controls when adding a verifier. State which obligations were **not**
checked. Supplier adoption needs the applicable complete cold replay and source
bindings; a local experiment may be submitted as a clearly scoped partial result.
Do not run every historical replay just to change documentation. Do not run
artifact-regenerating suites concurrently in the same worktree. Cache immutable,
source-bound evidence only when coverage and invalidation remain explicit.

Before submission, refresh the overlap check. Keep one focused PR with the task
card, precise delta, exact heads, commands, evidence, limitations and credit.
An independently corroborated or superseded contribution still deserves credit;
explain its added value rather than pretending the predecessor does not exist.
Declare substantial AI assistance and retain the repository/source licenses.

Do not promote your candidate into the selected record or close others' PRs
without maintainer authorization. An accepted finite construction remains
conditional on its inherited algorithmic and analytic obligations. Lean proofs
should name exactly the statements formalized.

## Short prompt for donating a session

> Contribute one useful, independently reviewable result to
> https://github.com/CrocSwap/integer-mult-bounds. Read AGENTS.md, autoresearch.md
> and CONTRIBUTING.md from the current main branch first. Use the repository's
> task-selection and overlap process unless I assigned a specific task. Work for
> [TIME BUDGET], keep the final quarter for verification and a concise handoff,
> and report the exact scope, evidence, remaining obligations and predecessor
> credit. Do not merge, close PRs or change the selected frontier. [State whether
> opening a PR or posting a coordination claim is authorized.]

Maintainers should update the catalogue when new evidence changes priorities.
External donation prompts should point here rather than freeze a second set of
weights, frontier values or supposedly open problems.

Prepared by Douglas Colkitt with OpenAI Codex assistance. Apache-2.0.
