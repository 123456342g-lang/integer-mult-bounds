# Bit-side revision-3 levers: certified budgets for the PR589 bit supplier at a = 1/99

**Scoped obstruction plus a screening table. No new κ; the selected record is unchanged.**

- **Track:** 00–19, bit supplier; assignment seed 3 (OS CSPRNG via Python `secrets`).
- **Card:** `bit-helper-contract`, scope **changed** (see [TASK.json](TASK.json)).
- **Base:** `bce54fb3`. The selected record is frontier1094: κ = 0.001672660197076918, complex side binding.

## Question

Priority revision 3 (#1272, built on #1240) aims new effort at the centre path, the rank shape and the
coverage law. It quantifies those levers for the **complex** supplier only. It also says a large
jump needs the bit side to advance, and #1293 leaves the bit word's realizability-aware ceiling
open.

This package asks three questions about the selected PR589 bit supplier:
- Which revision-3 levers can reach the planning target a = 1/99?
- How many helpers, of what width, does a given per-call copy charge leave room for?

## The model, and why it is favorable

Every number is an exact rational interval, computed by [levers.py](levers.py) using only the
standard library, with no repository engine imported:
- ln uses atanh prime chains;
- exp uses a Taylor series with a remainder bound;
- rounding is outward and dyadic.

For one call, the bill at saving a is B(a) = (1/w) Σ n_r (r/m)^(1−a). This is the bit side of the
coverage-law relaxation of #1240:

- **Coverage law (checked).** Per call, the paid rank mass is (m − u)·w + cst.
  - On the selected record, m = 64, w = 888/9 live families per call, u = 1 unpaid coordinate, and the
    copy charge is cst = 63 (nine rank-7 copies).
  - Then total mass = 63W + 63N = 1,808,352, and D = W − 63N = 10,272. Both equal the record (R3).
  - This is the bit form of the coverage identity of #1012.
- **Children.**
  - The local children are either the replayed word itself, or its most favorable in-window
    shapes. In those shapes each data register is one rank-7 climb, and each helper is one climb
    whose rank equals its width.
  - All remaining mass goes to idle children at one rank R, with fractional counts allowed.
- **Idle cap.** R = 45, the largest rank allowed by the halving guard m² > 2·maxchild². The guard
  comes from `global_k.py`'s `halving_integer_inequality=[M**HD,2*max(paid)**HD]` with the record's
  `halving_depth` = 2. Cap 63 is reported as a robustness bound only, because it violates the guard.
- **Surcharge omitted.**

Each relaxation step can only **lower** the bill:
- the cost per unit mass r^(−a)·m^(a−1) decreases in r, so idle mass is cheapest at the cap;
- r^(1−a) is subadditive, so merging a register's climbs into one climb is cheaper;
- the bill is linear in the counts, so fractional counts form a superset;
- the surcharge is a positive term.

`test_package.py` checks each step at a = 1/99. So a certified "fail" in the relaxation rules out
every construction that satisfies the premises, and a "pass" is only an upper target.

**Relation to the merged `research/format-limits`.** Under its accounting axioms, format-limits
section A already proves bit a ≤ X* = 6.0005·10⁻³ < 1/99. This model keeps the coverage law and the
in-window child shapes. It drops the per-stage window climb (Win), the B_K schedule (Sch), the
stage count s and slot domination. So its ceilings are weaker but cover a broader scope:
- the helper-free ceiling under O1 is 0.006794 rather than 0.0060005;
- unlike format-limits A.7's one-at-a-time multipliers, it prices **joint** budgets on the actual
  PR589 word.

## Results ([RESULT.json](RESULT.json); verdicts certified at a = 1/99, idle cap 45)

| Lever (bit, PR589 word) | Root a (certified bracket in receipt) | × ceiling | At 1/99 |
|---|---:|---:|---|
| Word as shipped, ideal idle packing (**packing ceiling**) | 0.001955918756 | 1 | fail |
| Centre path free (no rank-7 copies, cst 0) | 0.005419644435 | 2.771 | fail |
| Centre path shared by two calls (cst 31.5) | 0.003686367065 | 1.885 | fail |
| Two unpaid coordinates per family | 0.007312036734 | 3.738 | fail |
| Rank-8 children (window h = 8) | 0.003211353255 | 1.642 | fail |
| Rank-16 children (**beyond the window**) | 0.004730915412 | 2.419 | fail |
| Centre free + rank-8 children | 0.008938289238 | 4.570 | **fail** |
| Centre free + rank-16 children | 0.01316705483 | 6.732 | pass |
| Centre free + two unpaid coordinates | 0.01075873179 | 5.501 | pass |

**Packing ceiling.** With the local word fixed, no idle repacking lifts the bit supplier above
0.0019559, which is +12.8% over the selected bit endpoint 0.0017334. The cap-42 value is 0.0019475;
the cap-63 robustness value is 0.0019982. Open #1293's certified D/E value, 0.0017386, is the bound
for the **fixed** full histogram. Its screening extremum, 0.0161, ranges over all rank-mass-preserving
repackings, including the local word. The value here sits between the two because only the idle
part moves.

**O1 (copy charge 63).**
- Configuration: no helpers at all, every data register a single rank-7 climb, idle mass at the
  cap.
- The bill exceeds 1 at a = 1/99 at caps 42, 45 and 63. At cap 45 the helper-free ceiling is
  0.006794.
- So **as long as the bit copy charge stays at 63 per call, no helper design, data shape or idle
  packing reaches 1/99** under these premises.

**O2 (centre path shared by two calls, copy charge 31.5, cap 45).** The largest helper counts that
still reach 1/99 are certified as boundaries: k passes, and k + 1 fails.

| Helper width | 8 | 7 | 6 | 4 | 2 |
|---|---:|---:|---:|---:|---:|
| Max helpers | 104 | 110 | 118 | 148 | 229 |

The comparison uses the design-free helper floors of format-limits section D: at least 138 (strict)
and at least 212 (sink-only targets) bit helpers. Those floors are cited as argued premises, not
re-proved here. Against them:
- **Sharing the centre path is not enough with width-8 helpers.** It leaves room for at most 104,
  fewer than either floor.
- Only helpers of width ≤ 4 can meet the strict floor, and only width 2 can meet the sink-only
  floor.
- At the robustness cap 63, the width-8 bound becomes 181 helpers.

**Joint surface (width-8 helpers, cap 45).** The table gives the maximum number of helpers
(including totals) at a = 1/99 for each copy charge per call. "Ideal data" means every data register
is a single rank-7 climb; "shipped data" keeps the replayed shapes.

| Copy charge per call | 0 | 7 | 14 | 21 | 28 | 31.5 | 35 | 42 | ≥ 49 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Ideal data | 332 | 281 | 230 | 180 | 129 | 104 | 78 | 28 | none |
| Shipped data | 215 | 164 | 113 | 63 | 12 | none | none | none | none |

The receipt also gives the cap-63 columns and the width sweep at copy charges 0 and 31.5.

**The complex side and #1272.** The same code reproduces #1240's complex word ceiling, 0.0016900541090
(m = 73, w = 896/9, cst 64, cap 51). It then prices #1272's combined lever, "centre free and rank-16":
- The combined lever gives 0.011008 (×6.514, matching #1272's 6.5×). This **requires rank-16 local
  children**, larger than the complex stage window h = 9.
- Inside the window, with rank-9 children, the same combination gives **0.008128 < 1/99**.

The bit side behaves the same way: centre free + rank-8 children gives 0.00894 < 1/99. Read either
way, **a 1/99-scale gain from these levers needs a wider local frame window, or a second unpaid
coordinate, on top of freeing the centre path.**

## Bindings and replay

The bindings are checked in this order (B1–B5):
1. A record names the frontier1094 certificate. This is the selected record, or a checkpoint once
   the frontier moves.
2. The certificate pins `PR589-EXPECTED.json` (`b9f0e5ca…`).
3. That record pins the bit word `bitE8mut-p111-tuned.json.gz` (`e3e301e6…`), the bit profile, the
   endpoint and the halving depth.
4. The halving-guard source line is required verbatim.

**Positive control (P1).** Using the full selected bit profile with the inherited surcharge, the new
code accepts the endpoint 0.001733427039589844234749 and rejects the next 1e-24 grid point. Without
the surcharge, it would also accept that next point.

**Replay (R1–R3).**
- Every register's frame itinerary is replayed through D, A, B and C, with frame dimensions computed
  as rational ranks of the E8 line sets. Every frame change is a climb.
- The local histogram equals the record: `{1:1323, 2:1342, 3:79, 4:44, 5:102, 6:11, 7:19}`, mass 5,129.
- Class split:
  - sources `{1:317, 2:209, 3:10, 4:3}` and targets `{1:10, 2:92, 5:92, 6:10, 7:9}`, mass 777 each;
  - 430 helpers `{1:969, 2:1041, 3:69, 4:41, 5:1, 6:1, 7:1}`, mass 3,440;
  - 9 retained totals `{1:27, 5:9}`, mass 72;
  - 9 rank-7 copies.
- The profile is exactly 288 × the local word plus idle children `{2:13920, 4:14208, 6:14208,
  7:21312, 42:288}`.

## Controls ([test_package.py](test_package.py), 12 tests, < 2 s)

- **Interval engine.** It contains the float values.
- **Selected endpoint.** It is accepted, the next grid point is rejected, and omitting the surcharge
  would accept the next point.
- **Favorable-relaxation steps.**
  - One rank-7 climb is cheaper than a 3 + 4 split.
  - Idle mass at rank 45 is cheaper than at rank 42, and rank 63 is cheaper than rank 45.
  - The surcharge only raises the bill.
- **Guards.** Excess local mass is rejected by the coverage law. An idle child of rank 64 is
  rejected. The cap is 45, since 46 violates the guard.
- **O1 and O2.** O1 fails at caps 42, 45 and 63. The O2 boundary is certified: 104 passes and 105
  fails.
- **Replay.** A gate moved to the empty frame is rejected, and so is a tampered record histogram.
- **Receipt.** The receipt values are reproduced.

## Reproduce

```sh
python3 -I -B research/bit-revision3-levers-seed03/verify.py           # ~8 s; PASS_BIT_REVISION3_LEVERS (RESULT.json byte-identical)
python3 -I -B -m unittest discover -s research/bit-revision3-levers-seed03 -p test_package.py
python3.12 scripts/research_package.py --package research/bit-revision3-levers-seed03
```

## Scope and what is not claimed

- **A relaxation, not a construction.** A "pass" row is an upper target that any real mechanism must
  meet with its full paid budget. It is not a construction.
- **Premises of the fail rows.** They hold under the coverage law, the in-window child shapes, the
  idle cap and the copy charge carried as rank-7 copies. O2 also depends on format-limits section D's
  floors, which are argued there and given the crossing lemma.
- **Rank-16 children** are stated as being beyond the current stage windows, h = 8 for bit and
  h = 9 for complex, as in format-limits (Win). A changed window is a different architecture.
- **Inherited conditions.** All-size/compiler, hosting, precision/tape, analytic-transfer and
  PR589 H1–H5 conditions are inherited and untouched.

## Overlap and credit

**Overlap**

- **#1240** (Douglas Colkitt / Mister-Meeseeks): the complex local-word ceiling and `levers.py`.
  This package is the bit-side analogue in independent code and reproduces #1240's complex ceiling.
- **#1272** (Mister-Meeseeks): director revision 3. Its levers are quantified here for the bit side,
  and its combined lever is located relative to the stage window.
- **#1293** (navinor): the a < D/E diagnostic and the bit screening extremum, reconciled above.
- **`research/format-limits`**: the format ceiling X* (section A), the scope multipliers (A.7) and
  the helper floors (section D, cited as premises).
- **#974** (avirazza): the interface budget and bit headroom, including COPY deletion alone, which is complementary.
- **#1023** (ours) and **#1281** (mightyOil): width-7 hosting relaxations. Both ignore stage windows,
  and the widths here are local-shape widths only.
- **#1194, #1311, #1179, #1253 and #1128**: these saturate the card's helper-interface question.
- **Discussion #1317** (bitplane): an active claim on the register-model card.

**Credit**

- DreamingOfClouds (PR589) and eumemic (PR555): the bit supplier.
- DaysSky and the PR510/PR442 template and hosting lineage.
- The format-limits authors.
- Douglas Colkitt (#1240, #1272) and navinor (#1293).

Prepared by Sagar Thakrar (thakrarsagar) with substantial AI assistance from Claude (Anthropic) via
Claude Code. Parallel read-only scout and judge subagents proposed and ranked this question. New
material is Apache-2.0.

## Open next questions

1. **Does the idle-rank cap change with halving depth?** Every verdict is reported at the
   halving-guard cap 45.
   - First step: re-derive the guard for halving depths 2 and 3 from `global_k.py` and re-run the
     surface.
2. **Can a bit centre-path-sharing mechanism keep every data register a single rank-7 climb?** The
   shipped-shape rows show how much the ideal-data rows assume.
   - First step: replay a two-call shared-centre toy on a small E8 sub-word.
3. **What would a rank-16 local window cost?** On both sides, the 1/99 combinations need children
   beyond today's windows.
   - First step: price a window-16 stage in format-limits' (Win)/(Dfc) accounting, including its
     invoice.
