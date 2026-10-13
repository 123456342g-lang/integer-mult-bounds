# Seven grid-preserving JP8 coefficient circuits

**Finite complex-supplier circuit construction; no new kappa.**

Seven coefficients in the historical PR626 JP8 scalar programs admit a shorter
single-scratch circuit than any of PR837's four binary/NAF Horner variants.
The new circuits interleave halvings and repeated source additions. Their
intermediate magnitudes and fractional grids stay within the original binary
lowering's bounds, and private work is cleared after every addition macro.

For example, prepare `5S/2` with `W=S; W/=2; W+=S; W+=S`, then perform the
signed target update and clear `W`. The complete macro costs six primitives per
real component, versus seven for each of the four Horner comparators. The
initial copy, both source additions, final accumulation and clearing are paid.

| Complete JP8 scalar projection | Accepted PR696 lowering | Replacement | Saved |
| --- | ---: | ---: | ---: |
| Forward | 200,380 | 200,276 | 104 |
| Backward / inverse-transpose | 200,396 | 200,292 | 104 |

Each orientation changes 44 macros. At those occurrences the saving versus
the **best of all four PR837 variants** is 88 real-component primitives.
The full PR837 program is not composed here; all other macros retain PR696's
accepted lowering. These are distinct comparisons, not additive savings.
The original pre-PR696 bills are 257,232 / 257,280. This package claims only
the additional 104 / 104 improvement over PR696.

The additional **92 real source reads per orientation** are explicitly counted
and paid as copy/add/subtract instructions; fewer shifts more than offset them
in this primitive cost model. There is no additional helper, source mutation,
restoration, frame transition or recursive child. This is an operation count,
not a measured runtime result or a refreshed global invoice.

## Reproduce

From the repository root, Python 3.11+ and the standard library:

```sh
python3 -I -B research/jp8-grid-bounded-synthesis/verify.py
```

Expected final line:

```text
PASS_JP8_GRID_BOUNDED_SYNTHESIS coefficients=49 improved=7 extra_vs_four_horner=88,88 columns=716+9 kappa=unchanged
```

The command is offline, writes nothing, freshly rebuilds every search result,
checks the independent distance certificates and complete scalar traces, and
compares every receipt field with [EXPECTED.json](EXPECTED.json). A typical
local run takes several seconds. `--json` prints the checked receipt; the
development option `--write PATH` refuses existing output.

```sh
python3 -I -B research/jp8-grid-bounded-synthesis/crosscheck.py --self-test
python3 -I -B research/jp8-grid-bounded-synthesis/test_package.py
```

## Completed search and evidence

The OS assignment seed is **33**. The prespecified domain is every nonunit
absolute coefficient `a/d` in both frozen JP8 programs with reduced
`a <= 127`, `d <= 16`. There are **49**; the unit coefficient is handled by
the established direct update and paid clear. Seed 33 rotates traversal order
and selects JP8 by parity; all domain coefficients are covered.

The work coefficient lies on `d^-1 Z` with magnitude at most `a`. Starting
with the paid copy `W=S`, each search edge is one signed source addition,
doubling, exact halving or negation. Both terminal signs are allowed, followed
by one signed accumulation and one clear. The search stops only after the
finite graph is exhausted, with no timeout or randomized pruning.

[CERTIFICATE.json](CERTIFICATE.json) contains every shortest word. A separately
implemented checker enumerates **3,703 vertices and 14,311 distinct directed
edges** across the 49 graphs. It uses synchronous Bellman relaxation and checks
an integer potential and descending witness at every vertex. This establishes
optimality in the explicitly bounded single-scratch class, not general circuit
optimality. The other 42 coefficients supply no strict improvement over the
minimum of the four Horner comparators in this class; this says nothing about
larger grids, another initialization, more registers or multiple target updates.

The seven improvements are `9/4`, `5/2`, `11/4`, `13/4`, `7/2`, `15/4`, `17/4`.
The [proof](PROOF.md) gives the words, full cost recurrence and substitution
argument. Every graph witness is checked on arbitrary target/source/work inputs
for both coefficient signs, even when it is not installed as a replacement.

Both complete scalar projections are executed as actual primitives on all
**716 logical plus nine arbitrary private input columns**, comparing the
original, PR696 and replacement words at every macro boundary. All 492 helper
columns restore, and all nine private registers erase. The exact maximum
fractional denominator exponents stay **4 forward / 27 backward** in all three
traces. The original positive prefix bounds remain valid within the inherited
192-bit allocation; the proof covers magnitude and denominator nonincrease.

Non-scalar events and macro frames are retained by construction and recorded
with indexed hashes; paid profiles match the pinned receipts. Those preservation
checks are not an independent physical frame or wrapper replay. Eleven macro
rejection controls, four graph rejection controls and package corruption tests
separate endpoint, grid, magnitude, optimality, provenance and invoice failures.

## Provenance, related work and limits

Base commit: `f567884aeb8851b6e794af1184119a3bfbe1e631`. The selected record at
that base is PR799 with conditional kappa `0.001661634653669567`; this package
uses the **historical PR626 JP8** provider and makes no transport claim to X4.
[SOURCES.json](SOURCES.json) binds the official PR626 checkpoint, its SPEC,
emitter, accounting code, programs and receipts. Compressed source pins cover
decompressed payloads; the two vendored code files are pinned byte for byte.

- **Sagar Thakrar, PR696:** accepted copy/unit lowering and arbitrary-dirty
  scratch contract, retained verbatim. The coefficient/primitive lineage
  credits icekylinx, Jeremy Kothe's PR622, Chafik Boukhalfa's PR626 packaging,
  DreamingOfClouds, Rohan Arun, eumemic and their retained predecessors.
- **Gareth Davidson, PR837**, head `0a2977195efc8fb2a918fbfb694ec8d294387f08`:
  the four comparator circuits are vendored verbatim. Forward signed digits
  credit PR723 and PR787. We do not claim priority for shift/add synthesis.
- **Chris Pagolu, PR734**, head `ba76ba3321d000c8996b0b254bcf0d7260e1bbb6`:
  numerator-bounded signed-Horner recurrence and integer digit-graph
  crosscheck. Our class also admits halves interleaved with repeated additions.
- **Gareth Davidson, PR866**, head `5ae580bf68516f1cbe3b2dd3cb646be55170288f`:
  the fractional-grid audit motivates preserving this distinct precision
  quantity. Here it is constrained during synthesis and proved not to increase.
- PR811/PR860 reuse coefficients across macro boundaries; this package retains
  every original scratch-clearing boundary. Their savings are not combined.

Production-emitter integration, typed frame/phase admission, refreshed global
owner/invoice/assembly receipts and full compiler precision remain separate
obligations. The inherited all-size compilation, common-label/mutable-source,
whole-call hosting, precision/tape and analytic hypotheses remain. Finite
scalar replay and finite optimality are not a formal multiplication theorem.
`upstream/`, the selected frontier, and all existing files are unchanged.

Prepared for **Philipp (@mightyOil)** with substantial **OpenAI Codex assistance**
in research, implementation, proof writing, verification and packaging.
Separate AI workers implemented the graph checker and complete scalar replay
and reviewed the proof. This is not independent human review. New material is
Apache-2.0; predecessor source headers and notices are retained.

See [CLAIM.json](CLAIM.json), [VALIDATION.md](VALIDATION.md) and
[OVERLAP.json](OVERLAP.json) for the local sprint record and submission checks.
