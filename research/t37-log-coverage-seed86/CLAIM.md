# T37 execution-log coverage claim

Claimed 2026-10-13 17:24 UTC. OS-random seed 86 selects verification
engineering under the user's 85-94 mapping. Cycle began 17:17:25 UTC;
verification and handoff start by 17:47:25 UTC; finish by 17:57:25 UTC.
Base main: `2921874911956718fcaaaf9396fe8267b3cfa9f0`, fetched and confirmed
fast-forwarded from CrocSwap. Prior checkout and branches are preserved.
Branch: `research/cycle04-seed86-t37-log-coverage`.

Three candidates were considered:

1. Check all T37 stage logs, including the eight native logs whose existence
   is not checked by the frozen final binder. Chosen.
2. Audit receipt scalar types in isolation. Deferred; type checks belong to
   the concrete stage-evidence admission boundary in the chosen scope.
3. Reduce repeated source hashing. Rejected without a demonstrated bottleneck.

Exact object: the four stage indexes and 34 logs in
`research/community-frontier942-audit/t37-replay.tar.gz`, produced by
Jonathan Capalbo's selected PR942 T37 construction and its pinned U8 ancestry.
Hypothesis: a portable supplementary evidence check can reject every omitted
log, including native omissions that the frozen native-stage predicates do
not inspect, while accepting the unchanged archived stage evidence.

Method: inspect the actual producers and final binder; bind their exact source
bytes; verify complete ordered indexes, exact integer success codes, required
log presence and each digest that the producer records. Demonstrate the
native omission boundary using the unmodified source predicates, with a
clearly stated component-level scope. Exhaust all single-log omissions and
run changed-log, sequence, type and source-pin controls. Do not equate a
receipt or a log with authenticated execution or a full theorem proof.

Deliverable: a small standard-library checker, reproducible archive audit and
exact control receipt, source pins, scope/credit/license documentation and
handoff. No mathematical improvement is proposed. The optimistic effect on
the complete selected invoice and kappa is zero. No stronger supplier or
kappa is assumed. No selected record, source package, or upstream file changes.

Coordination: immediately before this claim, checked all 753 open PR bodies
through #1058, recent repository comments and pinned issues. No pinned issue
or matching active claim exists, so this claim is local. Relevant existing
work includes #865's PR799 evidence contract, #851's bridge coverage, #991's
different T37 witness/payload controls and #1006's owner-audit bitmap speedup.
None covers this current T37 log inventory. The review ledger and retained
negative scopes were read; no closed mathematical search is reopened.

Stopping rule: finish the declared archive and control census; if useful
evidence or relevant checks fail, preserve the patch and an honest handoff.
At most one focused PR; refresh metadata and overlap before submission.

Prepared for Sagar Thakrar with substantial OpenAI Codex assistance.
New files are Apache-2.0; predecessor notices and source licenses remain.
