# Research priority decisions

This log records allocation decisions, not mathematical frontier changes.
The active machine-readable portfolio is [agent-task-catalog.json](agent-task-catalog.json).
Follow [the director review procedure](../../autoresearch.md#6-maintainerdirector-priority-review)
when changing it. Preserve old entries so later agents can see why a route was
prioritized, narrowed or retired.

## Revision 1 — 2026-10-13: initial diversified portfolio

**Evidence base:** `ce7ad1b6ab09452c3478723a2e96ed5ff212dc08`, the selected #1094
record and [batch-1099 review](community-batch1099-review.md). The onboarding
portfolio was introduced in `c0e3631dc24e3c24a861f7d3d79e0608481cccec`; discussion
breadcrumbs followed in `e208d5e77a204252f92b395aae271679cc3a56f0`.

**Allocation:** bit mechanisms 20%, complex mechanisms 20%, recursive interfaces
15%, adversarial audit 15%, independent verification 10%, verifier engineering
10%, consolidation 5%, incumbent optimization 5%. This establishes the initial
repository-owned allocation; this entry does not change its weights.

**Reasoning:** local scalar improvements can leave the paid recursive profile
unchanged, and incumbent packing improvements alone have not established a
large-jump mechanism. The selected construction is complex-limited, but a large
improvement also needs the bit supplier to advance. Allocate substantial effort
to mechanisms on both sides and changed interfaces, while keeping verification
and useful incremental work represented. Existing evidence includes the
[scoped decoder bound](../../research/complex-decoder-field-extension-seed44/README.md),
[frozen provider-catalogue bound](../../research/heterogeneous-owner-assembly/README.md)
and [helper-contract gap](../../research/r439-bsection-stars-seed01/README.md).

**Limits:** weights are research judgment, not measured success probabilities.
The listed obstructions have restricted hypotheses. No universal barrier, new
supplier, or stronger κ is established by this allocation. No systematic
post-launch yield measurement is available yet.

**Next experiments:** use the catalogue cards to identify a changed premise,
price a favorable complete budget, and run a bounded falsification or construction
test. Independent work should target specific proof or verification obligations.

**Next review trigger:** a reviewed frontier/bottleneck change, a new decisive
obstruction, the next substantial PR reconciliation, or evidence of duplicate
assignments on the live board. In an active influx, review roughly daily.

## Template for the next decision

```text
Revision / UTC date:
Exact base and selected source record:
Evidence links and verification status:
Current bottleneck; what changed:
Track/card decisions (continue / narrow / expand / pause / replace):
Old allocation -> new allocation:
Paused scope and evidence that would reopen it:
Next bounded experiment and stop rule:
Uncertainties and useful work preserved:
Next review trigger:
```

Prepared by Douglas Colkitt with OpenAI Codex assistance. Apache-2.0.
