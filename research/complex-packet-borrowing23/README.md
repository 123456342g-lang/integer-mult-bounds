# A frame obstruction to borrowing one pair of complex targets

**Scoped negative result; no new κ.** In the six-leaver all-K packet cell,
using one pair of targets to share source-dependent partial sums cannot
replace the raw reads when the source values stay fixed and there are no
additional carriers. The obstruction allows arbitrary own-read order,
repeated pair interactions, signed coefficients and cancellation. It is
caused by the frames carried by reads, not by a failed circuit search.

An explicit two-carrier circuit escapes the obstruction in its three-source
projection. Helpers are restored on arbitrary dirty inputs, but its paid profile is worse
than the direct circuit on the same stock. This comparison concerns that
control circuit, not every possible two-carrier construction.

## Reproduce

From the repository root, with Python 3.11 or later and no third-party packages:

```sh
python3 -B research/complex-packet-borrowing23/verify.py
```

Expected first line:

```text
PASS_COMPLEX_PACKET_PAIR_BORROWING_OBSTRUCTION_AND_PAID_ESCAPE
```

The command checks the source pins, rebuilds the unmodified raw 492-helper
constructor with assertions enabled, and checks eight signed all-K cells.
It enumerates 504 nonempty leaver joins and binds 3,600 possible shared
supports to the chronology obstruction. A separate rational scalar/frame
replay examines all 720 orders of a six-event three-source example.
Of these, 120 have the required arbitrary-input scalar map and none has
legal frames. Omitting source-frame propagation incorrectly accepts 60.

The finite enumeration checks the example and the ordering certificate.
The proof below supplies the statement about arbitrarily many interactions
within one target pair; it is not inferred from a bounded search.

## The selected cell

The OS assignment seed was **23**, assigning the complex-supplier track.
The secondary string was `23|made, shell, arm, script, fix, tape`.
Three independently specified mechanisms were ranked by SHA-256; the
cross-factory packet-sharing experiment was selected. Hash ordering of the
52 formed pair/sign cases selected **pair (6,7), sign +1**. The base is
`66849e1475c930fd7732b1a0067ffee7e1e95f60`.

The cell has two leavers from each of the factories `(0,1,6,7)`,
`(2,3,6,7)` and `(4,5,6,7)`. Normalize the six target labels so that target
`Y_i` omits source `X_i`. For each source, its rank-two initial frame is
`E_i`; target `Y_i` has a rank-eight cap `H_i`. Exact XOR-span enumeration
checks

```text
E_i is contained in H_j if and only if i != j.
```

The required local source-to-target increment has a zero diagonal and
nonzero entries everywhere else. The coefficient signs need not agree for
the proof. All eight signed all-K cells have the same incidence pattern.
The checker derives their roles and coefficients from the pinned constructor,
then checks the subspaces independently by explicit XOR closure.

## Proposition and proof

Let there be `n >= 3` sources and targets with
`E_i` contained in `H_j` exactly when `i != j`, as above. Consider any finite
linear circuit with these conditions:

1. The `X_i` values are independent source variables and are not modified.
   A source frame can grow when the source is read.
2. Targets start with independent arbitrary values at frame zero. Each
   target must acquire a nonzero coefficient of every other source.
3. Every two-register operation lifts both registers to a common frame
   containing their previous frames. Frames never shrink, and target `Y_i`
   must stay inside `H_i`.
4. Apart from source reads `X_i -> Y_j`, operations may rescale targets or
   mix the targets of one unordered pair `{a,b}`. There are no additional
   carriers. Other target-to-target operations are allowed only as
   source-free preconditioning at frame zero.

Then the pair cannot interact after either target has accessed a source.
This excludes a shared partial sum and a two-target basis-change circuit,
including repeated interactions interleaved with source reads.

Suppose otherwise. Let `T` be the last interaction of the pair. Since an
earlier interaction followed source access, at `T` both target frames
contain some `E_k`. Necessarily `k` differs from `a` and `b`, since the
common frame must fit both target caps.

`Y_b` still requires `X_a`. Its paired target `Y_a` can never read `X_a`,
and no other target can supply it under condition 4. Thus a direct read
`A: X_a -> Y_b` is required. It must occur **after T**: an earlier read
would put `E_a` into the common frame at `T`, violating `Y_a`'s cap.
Likewise a direct read `B: X_b -> Y_a` must occur after `T`.

At `A`, source `X_a` acquires `E_k` from `Y_b`. It cannot subsequently
be read by `Y_k`. Hence the required direct read `C: X_a -> Y_k` occurs
before `A`. Similarly `D: X_b -> Y_k` occurs before `B`.

If `C` precedes `D`, the read at `D` puts `E_a` into the frame of `X_b`.
That forbids its later required read `B` into `Y_a`. If `D` precedes `C`,
the read at `C` puts `E_b` into `X_a`, forbidding its later read `A` into
`Y_b`. Both strict orders are impossible.

Cancellation, rescaling and repeated reads cannot remove a frame already
acquired. Earlier reads or extra frame promotions only add restrictions.
The five-event checker explicitly examines all 120 strict orders; 16 satisfy
the four required precedences, and the two contradictions reject eight each.

## A paid escape and controls

Use three sources and targets, where `Y_i` needs the other two sources.
Introduce dirty helpers `H0,H1`. At frame zero, apply

```text
Y1 -= Y0; Y0 -= H1; Y1 += H1; Y1 -= H0.
```

Then run these operations at the joins of their current frames:

```text
H0 += X0; H1 += X1;
Y0 += X2; Y1 += Y0;
Y0 += H1; Y1 += H0;
Y2 += X0; Y2 += X1.
```

Climb every source and helper to the full nine-dimensional frame and each
target to its own cap. Restore `H1 -= X1; H0 -= X0` at the full frame.
Exact rational replay checks all eight arbitrary input columns in both
forward and inverse-transpose orientations. The helpers retain their original
dirty values. Omitting cleanup or compensation, or doubling the shared read,
is rejected.

The escape's profile is `6 H1 + 5 H2 + 3 H5 + 3 H6 + 2 H7`.
A direct six-read circuit with the same two helpers left idle has profile
`6 H1 + 3 H2 + 3 H5 + 3 H6 + 2 H9`. Both have rank mass 63. Their difference is

```text
2 H2 + 2 H7 - 2 H9.
```

For the recursive moment `sum_r H_r r^s`, every `0 < s < 1` gives a strict
loss: `2^s + 7^s > 9^s`. Thus the added carriers are not free in this control.
This is a local comparison with fixed stock and unchanged surrounding work;
it does not assert a new globally hosted supplier or an outer exponent.

A second positive control drops one required off-diagonal entry. It admits
the formerly blocked target broadcast, showing why the all-but-one demand
is part of the proposition rather than a dispensable assumption.

## Relation to prior work and limits

[PR #651](https://github.com/CrocSwap/integer-mult-bounds/pull/651) studies
raw-face sharing and target hosting with an own-first
restriction. This argument permits own-read movement and repeated coded
operations on one target pair.
[PR #683](https://github.com/CrocSwap/integer-mult-bounds/pull/683) studies mixed K/M bypass with pure
carriers; this package concerns all-K cells and a target-pair mechanism.
Neither those broader titles nor the present proposition establishes a
barrier for arbitrary network coding.

The proposition does not cover additional carriers, mutable source values,
source-dependent coupling through three or more targets, register lifetime
resets, different decoder demands, or different geometry. Exploratory
six-source searches with broader target coupling and one or two coded helpers
timed out; those runs establish no impossibility result. The two-carrier
control does not establish a minimum carrier count or an optimal circuit.

The [local claim](CLAIM.json) records the draw and candidate selection.
[SEARCH-LOG.md](SEARCH-LOG.md) records exploratory domains and stopping rules;
those searches are not dependencies of the proof or checker.
The [source pins](SOURCE-PINS.json), [exact finite evidence](EXPECTED.json) and
[attribution](NOTICE.md) accompany this note.
No selected certificate, existing supplier or `upstream/` source is changed.
All inherited all-size, physical realization and analytic assumptions remain.
This is not a complete formal proof of integer multiplication.
