# Exact substitution, frames and finite costs

Prepared for alluri-ritual with substantial OpenAI Codex assistance. Apache-2.0.

## 1. Fixed-map substitution

Let `z` be the ordered vector of eight registers specified in `CIRCUIT.json`.
An addition is the elementary map `z_t <- z_t + q z_s`, `t != s`; a scale is
`z_t <- q z_t`, `q != 0`. The old 87-gate and new 35-gate products are both

```text
 1   1    1    1   -2  -2   2   2
 1   1   -1   -1   -2  -2  -2  -2
-1   1    1   -1    2  -2   2  -2
 1  -1   -1    1    2  -2   2  -2
 0  1/2   0    0    0   0   0  -1
 0   0   1/2   0    0  -1   0   0
 1   0  -1/2   0    0  -1   0   0
 0   0   1/2   0    0  -1   2   0
```

This equality is verified on all eight basis columns with rational arithmetic.
Because the programs are linear, equality on these columns is exact equality
on every vector in Q^8 and C^8; the registers may include arbitrary helper
dirt and correlated source values. This is a finite matrix identity, not a
finite sample of a nonlinear or all-size theorem. Every gate is invertible,
so both products are invertible, without requiring a separate determinant
calculation. Embedding the same map in the ambient 716 registers preserves
the entire surrounding forward scalar map.

Writing `E_1,...,E_k` in execution order, the matrix is `E_k ... E_1`.
Reversing the word and inverting each gate gives its inverse. Replacing every
gate with `E_i^(-T)` in the original execution order gives its inverse
transpose. The verifier checks main, inverse cleanup, inverse-transpose main
and inverse-transpose cleanup separately. It also checks every lowered gate
on all eight register columns and on the incoming private-work column.

The surrounding program's non-target cleanup is regenerated as the literal
inverse of the non-target A/B computation. No target is touched by the chosen
window. Thus the substitution preserves that inverse and the dirty target
response, so the zero-frame compensation is identical. Both original and
replacement raw words are freshly admitted by the inherited arbitrary-input
checker and emitted-program checker. They implement the same data shear and
restore all helpers, in both orientations.

## 2. Physical frames and child cost

For each of the eight registers, the pinned entry frame is a rank-three
subspace of `F = span_F2(390,74,44,30)`, which has rank four. Both words touch
every register and every gate is at F. Consequently each register climbs
exactly once, from its own entry frame to F, in either factorization. No
interleaved external read occurs inside this contiguous window. Delaying a
register's first touch within the window cannot affect its externally visible
state or require an additional climb. Cleanup is at FULL as in the original.

The verifier constructs spans as explicit sets of binary vectors, independent
of the constructor's row-reduction routine. It checks the literal boundary
frames and derives the same eight rank-one climbs. The full native and emitted
replays separately verify the entire word's chronology, paid histogram,
compensation, initial/final frames and phase-edge inventory.

All recursive widths are therefore unchanged. The retained recurrence's
homogeneous child-cost term is unchanged: scalar resynthesis alone does not
supply a larger certified exponent. There is no new supplier/assembly claim.

## 3. Scalar lowering and workspace

For an addition with `q = a / 2^d`, `a != 0`, initialize the existing private
coefficient register to zero. Read the bits of `abs(a)` most-significant first,
doubling the work register between bits and adding the source for each 1 bit.
Halve d times, add or subtract the result into the destination, and clear the
work register. This is the inherited Horner realization. Its real-component
cost is

`3 + (bit_length(abs(a))-1) + popcount(abs(a)) + d`.

The three fixed operations are the initial clear, signed destination
accumulation and final clear. A signed binary scale costs the absolute binary
exponent plus one if negative. No extra persistent helper, copy or frame is
introduced. Each source read and each intermediate coefficient operation is
counted. Complex arithmetic uses two real components.

The checker explicitly emits this primitive sequence and evaluates its action.
Private work starts with an independent test column as an additional negative
leak check, is cleared before use and ends at zero; it is **private cleared
work**, not a claim of restoring arbitrary public helper data by erasure.

Each of the old main, old cleanup and their two dual words costs 310 real
primitives; each replacement costs 147. Thus main plus cleanup saves
`2 * (310-147) * 2 = 652` real-component primitives per complete raw invocation.
The inherited emitted-program bill independently records this same decrease.

## 4. No hidden coefficient-growth increase

Replace each coefficient by its absolute value and replay from the eight
nonnegative formal input magnitudes. The resulting nonnegative transfer
matrix bounds each outgoing magnitude for every nonnegative incoming vector.
For all four words above, the new matrix is entrywise at most the old matrix.

Endpoint domination alone would not bound intermediate precision. The checker
also records the nonnegative row for every register update and the largest
Horner work row at every addition. The latter is
`abs(a) * (current source row)` before halving; earlier Horner prefixes and
subsequent halvings are bounded by it. Binary scales have their largest
magnitude at an endpoint, so recording their input and output suffices.

For **each** new prefix row the checker finds **one actual old prefix row**
that dominates it entrywise. Hence for every nonnegative input bound vector u,
`max_new(row dot u) <= max_old(row dot u)`. This is stronger than comparing
only a unit-input maximum or independent coordinatewise maxima. It permits
the unchanged surrounding scalar program to retain its old precision bill.
The full raw emitted-program audit additionally recomputes its original
prefix bounds, including all private work and both orientations.

## 5. What is proved, checked and left open

The written linearity, inverse, fixed-frame and envelope arguments justify
substitution of the finite checked circuit. The exact certificates establish
the stated matrix equalities, inequalities and concrete lowering counts.
Neither component asserts a minimum gate count. The 1,024-trial Gaussian
search only nominated the witness; its failure to find fewer than 35 gates
is not an impossibility theorem.

Applying this edit after transported prefix/entrance/cold-end stages requires
new index mappings, constructor binding and full admission. This package does
not infer that compatibility from the raw-word result. Complete hosting,
phase lowering, full invoices, outer assembly, uniform tape/compiler and
analytic interfaces remain outside its proof boundary.
