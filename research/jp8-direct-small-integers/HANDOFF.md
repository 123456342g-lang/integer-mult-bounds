# Review handoff

Status: **finite complex-supplier construction; no new kappa**.

Base: `007664306fff84fbb1c9a1b4053b69f439764034`.
Branch: `research/complex-coefficient-seed29`.
Scope: only `research/jp8-direct-small-integers/`.

The completed result replaces all historical PR626 JP8 coefficients ±2/±3
with direct target accumulation and a paid work clear. Counts fall by 2,848
real primitives in each orientation, with exact scalar boundary, dirty-input,
prefix, grid, source-access and unchanged-paid-profile evidence.

Apply the delivered Git patch to a clean checkout at the base commit:

```sh
git switch -c research/jp8-direct-small-integers 007664306fff84fbb1c9a1b4053b69f439764034
git am /path/to/jp8-direct-small-integers.patch
python3 -I -O -B research/jp8-direct-small-integers/verify.py
python3 -I -O -B research/jp8-direct-small-integers/test_package.py
```

Expected: `PASS_JP8_DIRECT_SMALL_INTEGERS macros=1424+1424 saved=2848/2848 columns=725 no_new_kappa`, followed by six passing tests.

Final validation: a fresh temporary Git index based at the exact base accepted
the patch and produced the same tree as the staged contribution. A minimal
export from that Git tree (this package plus its six pinned inputs) passed the
optimized isolated verifier without Git or network access. Python syntax,
JSON parsing and staged whitespace checks also passed.

Suggested PR title:
**Finite complex construction: direct JP8 integer updates save 2,848 primitives per orientation (no new kappa)**.

The patch is ready for an independently scoped review; production adoption is
separate. Read `README.md` for the proof, complete cost/access comparisons,
predecessor credit and unresolved physical/compiler/analytic obligations.
`EXPECTED.json` is the exact finite certificate; `SOURCES.json` pins all six
consumed inputs; `VALIDATION.md` records executed checks.

Publication resumed after the contributor created `zewelor/integer-mult-bounds`.
The result is published on `research/jp8-direct-small-integers-seed29` in that
writable fork, preserving the exact research base. The upstream PR submission
attempt returned HTTP 403: `Resource not accessible by integration`. No PR is
open yet. A verified public comparison is available at:

https://github.com/CrocSwap/integer-mult-bounds/compare/main...zewelor:integer-mult-bounds:research/jp8-direct-small-integers-seed29?expand=1

The prepared title/body are supplied in the conversation link for manual
submission. The former patch-only handoff is superseded by the published branch.
No pinned coordination issue existed, so the claim is recorded locally.
Refreshed upstream main is `1b59b624d21924f8e3537cdc1ac52d3be6eda2fe`; all six
consumed inputs are unchanged. Related PR999/1036/1064 are credited and the
additional JP8 scope is explained in `README.md` and `OVERLAP.json`.

Prepared by Michał Ciemięga (@zewelor), with substantial OpenAI Codex assistance.
Apache-2.0. No independent human review, full multiplication proof, global
invoice/assembly run, or new kappa is claimed.
