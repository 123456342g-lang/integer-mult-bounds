# Audit: PR442 hosting windows and the partial width-seven rows of #1023 and #1281

**Adversarial audit: this package finds no new κ and changes no check.** Track 60–74 (adversarial audit), assignment seed 72
(OS CSPRNG via Python `secrets`). Card `uniform-transfer-audit` (a hosting implication), scope
**refined** in [TASK.json](TASK.json). Base `0b1cccf8`; the selected record frontier1094 (complex-bound)
is unchanged, and `verify.py` binds it to the PR589 record and engines it uses.

## The audited claims

- **#1023 (ours, merged, `research/bit589-width-packing`).** It publishes partial width-seven rows: converting k helpers per call to width 7 gives,
  for example, k = 37 optimistic 0.0017896275 (+3.24%). The rows are described as achievable
  placements in its slot model. They are reached by putting all 9k width-7 residuals in empty
  capacity-7 slots. Its README lists window timing as an unchecked obligation.
- **#1281 (mightyOil, merged, `research/bit-partial-width7-optimum`).** It proves the
  exact optimum for every k = 0..74 in its mixed-width slot relaxation, replica-local and pooled32.
  It openly disclaims temporal constraints. Its **open question 1** asks whether the relaxed optimum
  can be hosted in time order.

This package answers that question for the PR442/PR589 **replica-local** hosting format: the hosted
audit's `hosted[(stage, helper)]` map with per-replica windows `s in W[i]`.

## The windows

[windows.py](windows.py) rebuilds the nine-stage idle schedule from the recipe of `global_k.py`
(K = 4, L = 9) and computes the windows. Three implementations agree exactly: this code, PR442's
`hosting_core.windows`, and `audit_hosted_k.windows`, which enforces `s in W[i]` for every hosted
slot. All 14 frozen `selection9-p111` entries lie inside their windows.

| Idle child | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Capacity | 14 | **7** | 28 | **7** | 42 | **7** | 42 | 28 | 14 |
| Admissible stages | 0–1 | **2** | 0–3 | **4** | 0–5 | **6** | 3–8 | 5–8 | 7–8 |

**Each capacity-7 child admits exactly one stage.** Per replica, at most 3k of the 9k width-7
residuals can sit in 7-slots. The window-free rows of #1023 and #1281 use all 9k.

## Results ([RESULT.json](RESULT.json))

For every k = 0..74, the package computes the **exact window-respecting optimum**. For each k it
gives:

- an explicit residual-level placement. Every slot is checked for its window, its width and its
  offset, cells must be disjoint, and every (stage, helper) is hosted exactly once;
- that placement's bit endpoint under both of #1023's local brackets, using the pinned engines and
  the inherited surcharge;
- a **certificate that no window-feasible placement reaches the next 1e-24 grid point**. The
  certificate is tight: it equals the engine moment of the explicit histogram to 1e-50.

k = 0 reproduces the selected bit endpoint 0.001733427039589844234749.

Per-replica idle histograms and the width-7 distribution over children 0, 2, 4, 8, 7, 6 are in
RESULT.json for every k. Selected rows, with gain over the selected bit endpoint:

| k | Bracket | Window-respecting optimum | Window-free optimum (#1281) | Retained |
|---|---|---|---|---|
| 1 | optimistic | 0.001734347102 (+0.053%) | 0.001734846264 (+0.082%) | 0.648 |
| 1 | pessimistic | 0.001734104523 (+0.039%) | 0.001734603545 (+0.068%) | 0.576 |
| 2 | optimistic | 0.001735271920 (+0.106%) | 0.001736327170 (+0.167%) | 0.636 |
| 2 | pessimistic | 0.001734786312 (+0.078%) | 0.001735840971 (+0.139%) | 0.563 |
| 10 | optimistic | 0.001743225534 (+0.565%) | 0.001748291126 (+0.857%) | 0.659 |
| 10 | pessimistic | 0.001740777922 (+0.424%) | 0.001745829269 (+0.715%) | 0.593 |
| 37 | optimistic | 0.001770809187 (+2.157%) | 0.001789671631 (+3.245%) | 0.665 |
| 37 | pessimistic | 0.001761884716 (+1.642%) | 0.001780556367 (+2.719%) | 0.604 |
| 74 | optimistic | 0.001809907119 (+4.412%) | 0.001849754238 (+6.711%) | 0.657 |
| 74 | pessimistic | 0.001792188010 (+3.390%) | 0.001831249661 (+5.643%) | 0.601 |

Decimals are truncated. The certified bound for each row is the next 1e-24 grid point above the
window-respecting endpoint.

- **#1023:** all 8 published partial rows (k = 1, 10, 37, 74; optimistic and pessimistic) are
  **unreachable** under the windows. Each lies above its certified bound.
- **#1281, replica-local:** every row (k = 1..74, both brackets) is unreachable. The window-free
  optimum is re-derived here and matches #1281's merged `EXPECTED.json` (digest-pinned, read as
  data; no #1281 code is run). All 75 idle optima agree, and all 9 priced cases agree exactly in
  endpoint and full histogram.
- **#1281, pooled32:** its 8 priced rows with k > 0 also lie above the per-replica bound. Pooling
  moves residuals between replicas, so it is not replica-local hosting. These rows are unreachable
  for replica-local placements only; see the cross-replica caveat below.
- **#1023's all-width-7 optimum `{42:340, 21:1}` stays window-feasible.** 104 sextet splits are
  feasible by max-flow, so its +17–23% figure is not affected by the windows.

Across the whole range, the window-respecting optimum keeps **63.6–67.1%** of the window-free
gain, or 56.3–60.7% under the pessimistic bracket. For small k, the window-free rows overstate the gain
by about 1.5×. None of this changes κ: the selected record is complex-bound, and these are bit
headroom figures.

## Why it is exact (proof sketch; the code asserts each checked fact)

1. **Lemma A (exchange): some optimum puts every stage-2, 4 and 6 width-7 residual alone in a copy
   of child 1, 3 or 5.**
   - Cost per copy is F(r) = 64^a r^(1−a) + λ for r > 0, with F(0) = 0. Here λ ≥ 0 is the
     per-child surcharge term.
   - F is subadditive on r ≥ 0: r^(1−a) is concave with value 0 at 0, and λ is counted once.
   - A capacity-7 copy cannot hold a width-8 residual and holds at most one width-7 residual. Child
     1 has 222 > k copies.
   - Moving a stage-2 width-7 residual from a copy with r unused units into an empty copy of child 1
     changes the cost by F(r + 7) − F(r) + F(0) − F(7) ≤ 0.
2. **Width-8 placement is unconstrained (checked for every k ≤ 74).** The windows are stage
   intervals, so Hall's condition for the stage → child transport reduces to intervals. For every
   proper interval J, the full width-8 capacity of the children whose windows lie in J is at most
   the width-8 supply of J.
3. **The width-7 residuals reduce to two nested chains.** After Lemma A, 6k width-7 residuals remain,
   from stages 0, 1, 3, 5, 7 and 8, over children 0, 2, 4, 6, 7 and 8. A distribution B is feasible
   exactly when all of the following hold:
   - B0 ≤ 2k, B0 + B2 ≤ 3k, B0 + B2 + B4 ≤ 4k;
   - B8 ≤ 2k, B8 + B7 ≤ 3k, B8 + B7 + B6 ≤ 4k;
   - ΣB = 6k.

   This is derived from all 45 interval Hall constraints (asserted for every k). It is also
   confirmed by brute force: every distribution for k = 1 and 2 is checked by max-flow against the
   chain predicate, all agreeing.
4. **Exact lower bound.** Cost splits three ways: copies holding width-7 residuals (a per-child
   knapsack over copy types), copies holding only width-8 slack (#1281's periodic V(S), recomputed
   and checked at each a), and the 7-slots. An integer DP over (chain sums, slack mod 5), with
   outward-rounded lower bounds of F at 2^−200 from the pinned engine, drops the copy limits and
   S ≥ 0. It is therefore a relaxation, which gives a rigorous lower bound.
5. **Attainment and certificate.** The DP minimiser is expanded into the explicit placement above,
   whose cost equals the DP value exactly. At a′ = c* + 1e−24, the local moment lower bound plus 32
   times the DP bound exceeds 1. Every replica-local placement, uniform across replicas or not,
   therefore has an endpoint below a′. This is grid optimality at each row's own endpoint.

## Controls ([test_package.py](test_package.py), 11 tests)

- **C-W1.** #1023's k = 1 placement fills 9 capacity-7 copies per replica, one per stage. The vendored
  windows admit only stages 2, 4 and 6 there, so at least 6 residuals sit outside their window.
- **C-W2.** The window-free local rows lie above the certified bound, while the window-respecting
  endpoints lie below it.
- **C-W3.** #1281's local and pooled32 priced rows (k > 0) lie above the per-replica bound, and all
  75 idle optima match.
- **C-W4.** The all-width-7 optimum is window-feasible.
- **C-W5 (dropped constraint).** Dropping the chain constraint B0 ≤ 2k breaks the brute-force
  agreement.
- **C-W5 (perturbed window).** Widening child 0's window to stages 0–3 breaks the chain structure.

Also covered: #1023's eight rows are all unreachable, k = 0 reproduces the selected endpoint, the
brute-force reduction holds at k = 2, and the width-8 Hall conditions are vacuous.

## Reproduce

```sh
python3 -I -B research/bit589-width7-windows-seed72/verify.py        # ~2.5 min on one idle core; PASS_BIT589_WIDTH7_WINDOWS
python3 -I -B -m unittest discover -s research/bit589-width7-windows-seed72 -p test_package.py
python3 scripts/research_package.py --package research/bit589-width7-windows-seed72 --check-only
python3.12 scripts/research_package.py --package research/bit589-width7-windows-seed72
```

Standard-library Python 3.10 or later. The pinned engines, record and slot model come from merged
#1023's `packing.py`, which is imported read-only. `verify.py --kmax K` runs a partial check
(`PASS_PARTIAL`).

## Scope and remaining obligations

- **Hosting format.** This applies to the PR442/PR589 nine-stage template (the 2P + 1 stage format
  with P = 4; #743) with replica-local hosting, whole residuals, no banks and the frozen stage
  recipe. A changed recipe, split residuals or banks lie outside it. Open #1487 (ianlibanio) varies
  the nine-stage recipe for width-8 hosting; its recipes may have other capacity-7 windows, which
  this package does not check.
- **Cross-replica owner maps are open.** The selected complex T16 supplier uses cross-replica
  interleaved owner maps (`owner_replica ≠ replica`). Such a map could admit other replicas' calls
  at other stages into the 7-slot windows. That case is **not** ruled out here.
- **Windows are necessary, not sufficient.**
  - Projector compatibility is still open. #1307's caveat applies: slots that split q⊥ lie outside
    its completion-free argument, and that covers width-7 residuals in 14-, 28- and 42-slots.
  - Owner inactivity is still open.
  - A physical width-7 helper is still open (#1128, #1271, #1256, #1362).

  So the window optimum is itself only an upper bound for real hosting, while the unreachability
  direction holds.
- **Pricing assumption.** The prices keep #1023's assumption that each converted helper removes
  one unit from one local child.
- **Uniqueness.** Histograms are not shown to be unique; ties exist, for example at k = 2.

## Relation to #1023 and #1281

- **#1023.** Its partial rows are window-free relaxation values, and this package gives the
  window-respecting values. #1023's frozen files are left untouched.
- **#1281.** Its optima are correct for the relaxation it states. This package answers the window
  part of its open question 1: the relaxed optimum cannot be hosted chronologically by any
  replica-local placement. It gives the exact window-respecting optimum instead. The physical
  helper, source access and restoration parts of that question stay open.

## Open next questions

1. **Can cross-replica (T16-style) interleaved owner maps lift the one-stage 7-slot windows for the
   bit supplier?** That would make #1281's pooled rows a real target.
   - First step: compute windows on an interleaved bit timeline and rerun the DP.
2. **Does another nine-stage recipe widen the capacity-7 windows?** #1487 enumerates recipes for
   width-8 hosting only.
   - First step: feed each of #1487's recipes to `windows.windows` and rerun `wopt.solve` at k = 1
     and k = 37.
3. **Do the window-respecting placements pass projector compatibility (#1307) for mixed-width
   slots?**
   - First step: run the projector check on the k = 1 explicit placement.

## Credit

- #1023: Sagar Thakrar.
- #1281: mightyOil (Philipp), with OpenAI Codex GPT-6 Astra assistance.
- #743: 0xjohnnydev, the 2P + 1 stage bound. #1487: ianlibanio. #1128: aliromman. #1307: commdata2338.
- PR442: DaysSky, the hosting windows.
- PR463, PR510 and PR589: DreamingOfClouds, the hosted audit and the bit supplier.
- PR555: eumemic.
- The retained moment-engine authors.

Prepared by Sagar Thakrar (thakrarsagar) with substantial AI assistance from Claude (Anthropic) via
Claude Code. Parallel read-only scout and judge subagents found and checked the window obstruction.
New material is Apache-2.0.
