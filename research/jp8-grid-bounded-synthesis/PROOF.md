# Proof and scope of the grid-bounded coefficient search

This note concerns the frozen historical PR626 JP8 scalar event streams. It
does not modify the selected supplier or establish a new multiplication
constant. The claim is a finite circuit result in the explicitly defined
single-work-register class below. The executable certificate and independent
checker supply the finite coverage evidence; this note explains why those
checks establish that claim.

## 1. Register contract and admissible words

An addition macro with nonzero dyadic coefficient

\[
q=\sigma a/d,\qquad \sigma\in\{-1,1\},\quad a>0,\quad
d=2^k,\quad \gcd(a,d)=1
\]

has the complete boundary map

\[
(T,S,W)\longmapsto(T+qS,S,0).
\]

The three registers are distinct. Their incoming values are arbitrary and
may be correlated; in particular, `W` is not assumed initially zero. The
source and target stay untouched while the coefficient is prepared. A word
in the searched class consists of:

1. One paid copy `W <- S`.
2. Any finite sequence of `W <- W + S`, `W <- W - S`,
   `W <- 2 W`, `W <- W/2`, or `W <- -W`.
3. One signed target accumulation, using the final `W`.
4. One paid clear `W <- 0`.

At every preparation prefix, including immediately after the copy,
`W = c S` for a dyadic `c` satisfying

\[
c\in d^{-1}\mathbb Z,\qquad |c|\le a.
\]

The terminal coefficient is either `a/d` or `-a/d`. If it is
`epsilon * a/d`, the target update uses sign `sigma * epsilon`. This makes
the final map exactly the displayed contract for either sign of `q`.

Here the bound is on the **magnitude of the coefficient** `|c|`, not on the
reduced numerator of `c` and not on the scaled graph coordinate defined
below. The source range is reduced `a <= 127`, `d <= 16`; the actual corpus
contains 49 nonunit absolute coefficients. The coefficient `|q| = 1` uses
the established direct circuit `T <- T +/- S; W <- 0`, costing two
primitives. Its special two-instruction circuit is outside the mandatory
copy/preparation/accumulation/clear form.

Every instruction uses the macro's original frame. No source modification,
source restoration, extra register, helper, frame transition, recursive
child, or transfer of work across macro boundaries is allowed in this
search. The optimality claim does not cover circuits allowing any of those
operations, multiple target updates, different initialization, or a larger
grid or magnitude envelope.

## 2. Exact finite graph

Write `c = m/d`. The vertex set, initial vertex and terminal set are

\[
V_{a,d}=\{-ad,-ad+1,\ldots,ad\},\qquad m_0=d,\qquad
G=\{-a,a\}.
\]

There is a unit-cost directed edge for each admitted operation:

| Work instruction | Graph edge | Additional condition |
| --- | --- | --- |
| `W += S` | `m -> m+d` | destination belongs to `V` |
| `W -= S` | `m -> m-d` | destination belongs to `V` |
| double | `m -> 2m` | destination belongs to `V` |
| halve | `m -> m/2` | `m` is even and destination belongs to `V` |
| negate | `m -> -m` | destination belongs to `V` |

The parity condition is necessary: halving an odd `m` would produce a
coefficient on a strictly finer grid. Halving can be legal when the source
happens to have special divisibility, but such input-dependent shortcuts
are deliberately excluded: the macro must work for arbitrary source input.

Induction on instructions gives a cost-preserving correspondence between
admissible preparation words and directed walks from `d` to `G`. The
graph therefore contains every preparation word in the stated class, not
merely binary, signed-digit or monotone words. Conversely, each graph edge
is one legal primitive. Removing a repeated-vertex cycle never increases
cost; hence the finite graph suffices even though words of unbounded length
are allowed. There are `2ad+1` vertices, at most 4,065 under the stated
parameter bounds.

If `L(a,d)` is the shortest distance from `d` to `G`, the optimal nonunit
macro cost in this class is exactly

\[
C(a,d)=1+L(a,d)+1+1=L(a,d)+3.
\]

The three charged instructions outside the graph are initialization,
target accumulation and final clearing. Source additions and subtractions,
doublings, halvings and negations each cost one, even if a particular
implementation could combine them. Complex streams execute the same real
coefficient circuit on their real and imaginary components, so their
charged cost is twice the real-component cost.

## 3. Independently checkable optimality certificate

Breadth-first search with unit edge weights finds a shortest witness. The
independent checker does not import that search. It enumerates every vertex
and successor, computes a potential by synchronous Bellman relaxation from
both goals, and checks the following conditions over the entire graph:

* `h(v)` is a nonnegative integer and is zero exactly on `G`.
* Every directed edge `v -> w` satisfies `h(v) <= 1 + h(w)`.
* Every nongoal has a successor with `h(w) = h(v)-1`.

For any walk `v_0,...,v_l` ending at a goal, telescoping the edge inequality
gives `h(v_0) <= l`. Following decreasing successors gives a walk of
exactly `h(v_0)` edges to a zero-potential goal. Thus these checks establish
the exact distance at every vertex, including `v_0=d`. Replaying the
submitted instruction sequence separately checks that it attains that
distance with its claimed terminal sign. Duplicate operations leading to
the same successor and self-loops do not change a unit-cost shortest path.

Coverage requires the coefficient census as well as graph checks. Extract
the reduced absolute coefficients from **both** frozen JP8 orientations,
filter by `a <= 127` and `d <= 16`, and compare that set to the certificate
entries. There are 50 absolute coefficients including the special unit,
100 signed coefficients in their union, and 90 signed coefficients in each
orientation. The filtered occurrence counts are 21,566 forward and 21,574
backward, out of 22,211 and 22,219 additions respectively. A seed may order
this finite corpus; it cannot replace complete coverage.

## 4. Endpoint substitution and exact arithmetic cost

After initialization, the invariant `W=cS` follows directly from the five
instruction rules. The chosen signed accumulation gives the required
target value; the source is unchanged and the final clear erases any work.
The initialization overwrites arbitrary incoming private dirt. This is a
three-register linear identity, so checking independent formal input
columns proves it for all real inputs, including correlated inputs. Applying
the identity to both components proves it for complex inputs as well.

Replace a scalar macro only by a word with the same complete boundary map.
Induction over the unchanged event stream preserves every later macro's
inputs and the complete scalar endpoint. Reuse of the existing scratch is
valid because every replacement clears it at the boundary. Frames, child
calls, adapters and paid-event inventories are untouched by this local
substitution; their inherited physical interpretation is a separate matter.

The reference original binary-Horner cost per real component is

\[
B(a,d)=3+\lfloor\log_2 a\rfloor+\operatorname{popcount}(a)+k.
\]

It pays one initial clear, the leading source addition, all binary shifts
and remaining source additions, `k` halvings, the signed target accumulation,
and the final clear. The accepted copy-based nonunit lowering costs
`B(a,d)-1`; the unit lowering costs two. Scale, copy and clear macros that
are not selected for replacement retain their existing costs.

For a selected replacement set `R` and orientation-specific occurrence
counts `N_o(q)`, the saving against the accepted copy-based baseline is

\[
2\sum_{q\in R}N_o(q)\left(C_{\rm copy}(q)-C_{\rm new}(q)\right).
\]

The factor two charges both real components. A saving against the best of
four Horner comparators is a different quantity; it must be computed with
that comparator's cost in place of `C_copy`. Comparing complete circuit
lengths, including initialization and clearing, avoids assigning a saving
to an uncharged source read. No unchanged child, adapter or wrapper cost
may be removed from a global invoice because a local coefficient is cheaper.

The seven selected absolute coefficients have the following positive
witnesses. `H` means halve and `A` means add the unchanged source. Each
displayed preparation starts immediately after the paid copy `W=S` and is
followed by the paid signed target update and final clear.

| `|q|` | Preparation | Complete new cost | Copy-binary cost | Occurrences in each orientation |
| --- | --- | ---: | ---: | ---: |
| `9/4` | `H H A A` | 7 | 9 | 2 |
| `5/2` | `H A A` | 6 | 7 | 25 |
| `11/4` | `H A H A A` | 8 | 10 | 1 |
| `13/4` | `H H A A A` | 8 | 10 | 1 |
| `7/2` | `H A A A` | 7 | 8 | 10 |
| `15/4` | `H A H A A A` | 9 | 11 | 4 |
| `17/4` | `H H A A A A` | 9 | 10 | 1 |

These are 44 macro occurrences per orientation, saving 52 primitives on
one real component and therefore 104 on both components against the
copy-binary baseline. Each new circuit is also one real-component
primitive shorter than the best of the four pinned PR837 Horner
comparators for that coefficient; the incremental saving against those
comparators at these occurrences is therefore 88 per orientation. That
second figure is a comparator calculation, not an assertion that the
complete PR837 implementation is composed into this package.

## 5. Magnitude bound inherited from original binary Horner

The original binary-Horner preparation explicitly reaches `W=aS` before
its terminal halvings. Every candidate preparation value obeys

\[
|W|=|cS|\le a|S|.
\]

The source is unchanged; the target stays at its incoming value until one
final update, after which it equals the original final target. The arbitrary
incoming work and the final zero also occur in the original trace. Therefore
the maximum absolute value over all registers and prefixes in a replacement
macro is no larger than in that macro's original binary-Horner trace, for
each input separately.

For symbolic source row `s`, the same argument gives
`norm_1(c*s) = |c| norm_1(s) <= a norm_1(s)`. Thus the inherited maximum-row
norm or nonnegative original-Horner envelope remains an upper bound under
successive substitutions. This does **not** assert that each replacement
row literally occurs in the original trace, or that all simultaneous
transfer matrices satisfy an entrywise order. New fractional coefficients
usually prevent literal prefix-trace containment.

## 6. What the fractional-grid constraint guarantees

Locally, if macro-entry `T`, `S` and `W` are on `2^-p Z`, every candidate
value is representable on `2^-(p+k) Z`, with an unbounded integer part.
The coefficient grid does not by itself fix `p`, total register width,
overflow behavior, rounding-error amplification, or the precision needed by
the physical compiler.

There is also a stronger **scalar-projection** comparison with the original
word. Replay scalar primitives as exact dyadic linear maps on the original
formal input columns, leaving physical frame operators outside this model.
Let `s_j` be a coefficient in the current source row. A candidate scratch
coefficient is `m*s_j/2^k`.

If `k>0`, reduction of `a/2^k` means `a` is odd. For nonzero `s_j`, the
2-adic valuation satisfies

\[
\nu_2(m s_j/2^k)\ge\nu_2(s_j)-k
 =\nu_2(a s_j/2^k).
\]

Consequently its reduced binary denominator exponent cannot exceed that
of the original terminal scratch coefficient `q*s_j`. A zero coefficient
has no denominator requirement. If `k=0`, every candidate multiplier is an
integer, so its denominator exponent cannot exceed that of `s_j`; the
original leading-source state `W=S` already attains that bound. These
arguments also cover source rows whose integer coefficients are all even;
it would be incorrect to assume that the clipped denominator depth always
increases by exactly `k`.

All remaining registers, the arbitrary incoming work and the target before
and after its single update have the same values as before. Hence each
replacement has no larger scalar-prefix denominator depth than its original
macro, and boundary induction extends this to the complete scalar
projection. This comparison is against the original/copy binary lowering;
it does not imply that the chosen word minimizes denominator depth among
all shortest words.

The conclusion does not evaluate frame/phase operators, normalization,
recursive children, tape interfaces or floating-point arithmetic. It is
not a full compiler precision certificate or a proof of the all-size
integer multiplication theorem. The distinction matters because a
coefficient on a depth-`k` local grid can be applied to a source already
carrying additional fractional depth from previous macros.

## 7. Adverse checks and review boundaries

Endpoint checks alone would miss several false claims. The implemented
controls exercise distinct failures with the recorded failure reason:

* Remove the initial copy while retaining arbitrary incoming work: the
  three-register endpoint must fail.
* Remove the final clear: private dirt must be
  detected even if the target endpoint is correct.
* Flip the target accumulation sign or the claimed terminal sign: the
  target identity must fail.
* Insert enough halving and inverse doubling to cross the allowed grid
  and restore the original endpoint: the grid check must fail.
* Insert a doubling excursion beyond `|c|<=a` followed by its inverse:
  the magnitude check must fail despite the correct endpoint.
* Insert two negations into a valid optimum: a legal equal-endpoint path
  must fail optimality or exact cost, not arithmetic correctness.
* Understate a potential entry: the full-graph optimality check must fail.
* Omit one corpus coefficient or change a pinned source payload: coverage
  or provenance must fail.
* Supply zero, a nondyadic coefficient or
  aliased source/target/work: domain or register-contract validation must
  reject it.

The reproducible verifier output and validation record identify the controls
actually executed. Independent implementation here
means a separate algorithm and interpreter, not independent human review
or formal verification of the full theorem.

## 8. Relation to the closest prior work

PR696 already supplies the copy/unit lowering and dirty-work contract.
PR734 supplies numerator-bounded signed-Horner circuits, a proof within its
restricted recurrence, and a Dijkstra crosscheck. Its crosscheck uses
positive integer states with transitions `c -> 2c+e`, `e` in `{-1,0,1}`,
cost `1+|e|`, and bounded doubled and final states; halving follows after
integer preparation. PR837 chooses among
forward/reverse binary and NAF Horner circuits. PR866 demonstrates why exact
endpoints and small magnitudes do not alone control fractional grids.

The incremental search class here permits arbitrary interleaving of paid
source additions/subtractions and shifts, while preserving both the
original magnitude envelope and coefficient grid. Its finite optimality
claim must be stated relative to this class and corpus. General shift/add
synthesis, bounded Horner optimization, copy initialization, and grid-guard
analysis are not claimed as new ideas. Savings already available from a
prior candidate family must not be presented as an additional improvement
over that family; the certificate should distinguish them from words that
strictly beat every named comparator.

No result here automatically transports to another supplier or to the
currently selected frontier. No new kappa, asymptotic complexity bound,
runtime speedup, physical admission certificate or production integration
is claimed.
