# A smaller exact coordinate-total circuit in complex factory block 5

**Finite local circuit improvement; no new κ.** One eight-register basis-change
window in Jeremy Kothe's PR622 raw K-triangle constructor falls from **87 to 35
scalar operations**. Replacing its literal inverse cleanup saves another 52:
**104 fewer scalar operations and 652 fewer real-component primitives per raw
invocation**, in either orientation. All arithmetic certificates are rational.

The exact base is `66849e1475c930fd7732b1a0067ffee7e1e95f60`. Its selected result is
PR626/PR543, κ = `51110230636731/31250000000000000`. This package does not change
that result or any existing repository file. `SOURCE-PINS.json` binds the actual
constructor, inputs, inherited auditors, review and selected assembly.

## Reproduce

From the repository root, Python 3.11+ and the standard library suffice:

```sh
python3 -B research/complex-factory5-resynthesis/verify.py
```

Expected:

```text
PASS_COMPLEX_FACTORY5_RESYNTHESIS gates=87->35 saved_with_cleanup=104 columns=716 controls=10
```

This takes about five seconds on the development macOS/Python 3.14 environment.
It freshly executes the **unchanged** pinned constructor, observes the chosen
window, rebuilds both raw words, checks the local certificate and runs the
inherited native audit, emitter and independent local auditor on both words.
It compares every deterministic receipt field with `RESULT.json`. Temporary
outputs are removed. To retain words and logs, add `--out /path/to/new-directory`.
The output directory must not already exist. `--write PATH` is a development
receipt-generation option; omitting it performs the frozen-result comparison.
Inherited subprocesses always run without optimization, even if this verifier
is called with `-I -O`. All new validation uses explicit exceptions.

The bounded search can be reproduced separately:

```sh
python3 -B research/complex-factory5-resynthesis/search.py
```

Expected: `PASS_SEARCH_FACTORY5 trials=1024 gates=87->35`. Search code is not
imported by the certificate verifier. No network, solver, NumPy or SymPy is used.

## Exact object and result

The operating-system assignment seed was **33**, selecting the complex track.
Block `33 mod 14 = 5`, in lexicographic order, has support `(0,3,4,7)`. The
constructor first normalizes eight retired donors to the source basis, then
applies a second invertible change putting the four coordinate totals first.
This experiment composes those two maps and resynthesizes their **entire**
8×8 rational map; it does not choose a different complementary basis or assume
that any helper starts at zero.

The pre-restriction ordered registers are
`[325,320,323,321,330,79,76,77]`; after the constructor's 112-port restriction they
are `[309,304,307,305,314,71,68,69]`. Five are helpers and three are source
registers. The window is the half-open, zero-based section-A slice `[723,810)`.
Every old and new gate is at the same rank-four frame
`span_F2(390,74,44,30)`. Every register enters at its pinned rank-three frame,
is touched at rank four, and exits at that same frame.

| Raw-word quantity | Before | After |
|---|---:|---:|
| Local window scalar operations | 87 | 35 |
| Full compensated scalar program | 16,972 | 16,868 |
| Emitted scalar macros, each orientation | 16,996 | 16,892 |
| Forward real-component primitives | 170,488 | 169,836 |
| Inverse-transpose real-component primitives | 170,536 | 169,884 |
| Forward positive prefix bound | 86,491,024,246 | 77,948,354,244 |
| Inverse-transpose positive prefix bound | 2,028,759,644,357 / 2 | same |
| Helpers / arbitrary input columns | 492 / 716 | same |
| Dirty-input compensation additions | 10,632 | same |
| Paid rank mass / distinct directed phase edges | 6,284 / 3,110 | same |

The raw word's paid histogram stays
`{1:2024, 2:760, 3:300, 4:168, 5:168, 6:44, 8:8}`.
These are raw-constructor quantities, **not** the selected optimized provider's
profile or global invoice.

## Cost and correctness boundary

The optimistic bill was evaluated before packaging: a fixed-frame exact-map
replacement can reduce scalar lowering work, but cannot improve the recurrence
exponent when all child widths remain unchanged. That is the measured outcome.
`PROOF.md` supplies the substitution argument and precise positive-envelope
comparison. The full replay covers arbitrary source, target and helper inputs,
private center clearing, both orientations and native frames.

Every source access is an explicit addition in the circuit. The primitive bill
includes Horner work initialization, source accumulation, doubling, halving,
signed accumulation and clearing. Each scalar scale is lowered into signed
binary operations. The new circuit uses no extra helper, persistent copy,
frame, route, recursive child or restoration assumption. The existing private
coefficient stream is reused. The main-plus-cleanup cost falls from
`2 components × 2 windows × 310 = 1240` primitives to
`2 × 2 × 147 = 588`.

There are ten new rejection controls: omitted gate, wrong sign, wrong source,
wrong frame, non-dyadic addition, non-binary scale, exact-map-neutral growth
inflation, endpoint-envelope-neutral prefix inflation, exact-map-neutral cost
inflation and omitted cleanup. The inherited
four local controls also run for each raw word. Gate counts alone are not used
to infer a primitive or precision improvement.

This package does **not** transport the edit through PR622's later prefix,
gauge, frame-regroup and cold-end recipes. Those recipes refer to scalar words
and indices and need separate reconstruction. It does not rerun phase lowering,
residual wrappers, whole-owner hosting, the 47-inequality assembly, the full
repository suite or Lean. An unchanged phase-edge inventory is checked; it is
not represented as a fresh Clifford proof. All-size/compiler/common-label/
mutable-basis, precision/tape, analytic-transfer and selected bit-supplier
assumptions remain inherited. This is neither a multiplication theorem nor a
claim of optimal gate count, practical speedup or a larger κ.

## Search and overlap

`CLAIM.json` records the three candidates considered and the local claim.
There was no pinned coordination issue; the only open issue was #650 requesting
Discussions. The method changes the scalar factorization while fixing the
complete rational map. It does not reopen the decoder, delivery or owner-map
searches closed or pursued by #620/#651 and the newer construction chain.

The completed search used `random.Random(33)`, 1,024 trials, eight-column
permutations, diagonal pivots when possible and randomly chosen feasible
binary-rational pivots otherwise. Both diagonal-scale factors and inverse
scales must be signed powers of two; additions must be dyadic. All 1,024 trials
were admissible. Only shorter words with exact map equality and entrywise
nonnegative transfer dominance in both directions were retained. Improvements
occurred at zero-based trials 10, 39, 87, 695 and 784; the last had 35 gates.
The stopping rule was 1,024 trials, not exhaustion. Only block 5 was searched.
Full prefix, primitive, dual and native checks were performed on the winner.

PR645 changes the factory's arbitrary-helper-input map and complementary basis;
this contribution preserves both. PR670 and concurrent PR674 independently
simplify circuits in the **F2 bit supplier**, at blocks 3 and 5 respectively;
this package uses rational complex arithmetic, signed scales, Horner lowering
and the different PR622 coordinate-total circuit. Neither bit PR is a
code/certificate dependency. Older target-prefix resynthesis (#411 and related
work) changes delivery prefixes rather than this exact retired-row map.

## Attribution and license

Prepared for **alluri-ritual (Alluri)** with substantial **OpenAI Codex**
assistance in task selection, implementation, mathematical analysis,
verification and writing. No delegated agent or independent human review is
claimed. Apache-2.0, under the repository [LICENSE](../../LICENSE).

The construction and source material are credited to:

- **Jeremy Kothe / jeremykothe2, PR622**: K-triangle constructor and schedule;
  its notices credit AtomScout, Port480, GlobalR, Stack492 and ColdBeyond, with
  Claude Code assistance. Reviewed source head:
  `f69477f4f6d3c7eb1f740b166881bffed4ffa9f6`.
- **icekylinx, PR531 and PR425/433/523 lineage**: same-partition factory,
  retired-row coordinate totals, scalar architecture and native replay; these
  sources disclose OpenAI assistance.
- **DreamingOfClouds, PR484/604 and predecessors**: gauge/paid-wrapper interfaces,
  emitter and independent local verification, with Anthropic Claude assistance.
- **Dugongue, PR514/522, and the credited PR507 ancestry**: Hamming/scalar
  modules and coordinate-total rank-sector work.
- **Chafik Boukhalfa / chafreaky, PR626**, reviewed head
  `660de893d27bb7abd1d5b01b1640207528a5c851`: the retained owner-repair package
  hosting the unchanged constructor/checkers consumed here.
- **eumemic, PR543**, and the contributors in the selected review: the accepted
  bit supplier and cumulative selected-result lineage, used as context only.

Original files and their notices are read in place, never rewritten or copied
without attribution. See the pinned [full predecessor notice](../complex-k492-owner-repair/NOTICE.md),
[PR531 construction](../direct-delivery504-global/proof/LOCAL-CONSTRUCTION.md)
and [maintainer review](../../docs/research/community-k492-review.md).
