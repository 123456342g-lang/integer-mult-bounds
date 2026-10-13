# Sprint claim: output-borrowed fanout

- Track: recursive interfaces; OS assignment seed **59** (`secrets.randbelow(100)`).
- Exact base: `bbc600db2fc15007b7c914f4f2b2ed55fa909c87`.
- Selected certificate followed: PR942, conditional kappa `1661960547713947/10^18`; U8/T37 owner construction and maintainer batch952 review. Not changed.
- Object: arbitrary-dirty fanout `y_i += A_i B x`, with at least two outputs, where a pending/final output can be borrowed and restored as the connector. Compare with PR889's dedicated-connector star.
- Hypothesis: eliminate the dedicated connector for `4 C(B) + 2 sum_i C(A_i)` complete child calls, preserving arbitrary dirty outputs and noncommutative factor order. Prove a query bound only in an explicit unit-generator alphabet; do not claim general circuit optimality.
- Method: written algebra and restricted lower bound; independent free noncommutative symbolic replay, dense exact noncommuting matrices, literal recursive lowering, complete work/storage recurrence, deliberate failed restorations.
- Seed diversification: seed 59 selects heterogeneous factor lengths and prices and three outputs; not another fixed-space tree or signed-incidence search.
- Expected deliverable: one self-contained research construction with exact certificates, pins, controls, and complete cost recurrence; no new kappa.
- Claimed at: 2026-10-13 15:29 UTC. Expected finish: 2026-10-13 16:04 UTC (40-minute total budget from 15:24; final ten minutes for verification/handoff).
- Coordination: GitHub pinnedIssues returned no pinned issue; local claim per sprint instructions. Queue inspected through PR971, including recursive-interface PR889/822/934/943/944/953/951. Immediate targeted overlap checks recorded in handoff.

## Three candidate tasks and selection

1. Heterogeneous ordered dirty-echo connector reuse: PR730/822 already cover this mechanism; not reopened.
2. Remove cyclic-inverse data connectors with additive filters: active PR951 already directly addresses it; not duplicated.
3. Borrow an output of a multi-output common-factor product shear as the connector: selected. Changes the allowed scratch ownership contract, unlike PR889's dedicated connector and PR822's recursive sibling connector reuse. New complete price, no assumption of a better bound.
