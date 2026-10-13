# Validation record

Date: 2026-10-13. Base `f567884aeb8851b6e794af1184119a3bfbe1e631`.
Local macOS arm64, CPython **3.14.7** and **3.11.15**; standard library only.
No remote Linux, full repository suite or Lean result is claimed.

## Executed checks

1. `python3 -I -B research/jp8-grid-bounded-synthesis/verify.py` and the same
   command under `python3.11`: PASS. All 49 nonunit coefficients reconstructed;
   seven strict improvements; 88 additional real primitives saved versus the
   four-Horner comparator at the replaced occurrences in each orientation.
   The complete source closure and exact receipt match.
2. Independent Bellman/potential checker: PASS for 3,703 vertices and 14,311
   distinct directed edges, exact coefficient coverage, four adverse controls,
   eight elementary distance checks and all five preparation primitive types.
   `crosscheck.py --self-test` also passed standalone.
3. Complete three-way primitive replay: PASS on both orientations, each with
   716 logical and nine arbitrary private input columns, 22,693 scalar macro
   boundaries, restored 492 helper columns and erased private registers.
   The historical, PR696 and replacement bills are respectively
   `257232/200380/200276` forward and `257280/200396/200292` backward.
   Exact maximum scalar fractional denominator exponents agree at 4 and 27.
4. `python3 -I -B research/jp8-grid-bounded-synthesis/test_package.py`: nine
   tests PASS; repeated under CPython 3.11.15: nine PASS. This includes an
   optimized (`-I -O -B`) minimal checkout without Git metadata in a path with
   spaces, a different working directory and recompressed gzip input. Package
   controls reject source/reference byte changes, a missing source pin,
   omitted coefficients, an altered path and a forged invoice. Existing output
   is preserved. The independent coverage checker separately rejects an
   omitted coefficient.
5. `make selected-record-check`: PASS, current PR799 exact kappa
   `1661634653669567/1000000000000000000` and source/proof inventory.
6. Staged whitespace and scope checks: PASS. Only this new research directory
   is included. `upstream/`, existing source packages and selected certificates
   match the exact base commit.

The first package-test run exposed an overly narrow expected error-message
regex (`coverage` versus the actual `does not cover`); it was corrected, and
both complete nine-test runs passed. The checker correctly rejected the
omission throughout; no mathematical or source-coverage failure was suppressed.

## Interpretation

The full scalar replay executes primitives; it does not interpret frame changes
or recursive children as physical numerical operators. Event/frame hashes are
preservation evidence by construction, and paid profiles are checked against
the pinned receipt. The nonincrease of magnitude and scalar fractional depth
also follows from the local substitution proof, separately from finite tests.
All source accesses in the primitive model are charged, including 92 more real
source reads per orientation in the replacement.

No full `make verify`, selected cold reconstruction, regenerated global invoice,
owner admission, native phase/wrapper rebuild, production compiler integration,
remote CI or formal multiplication theorem is asserted. None of those artifacts
is modified. Those inherited or integration obligations remain outside this
finite research contribution. The selected kappa is unchanged.

The [overlap record](OVERLAP.json) records the final metadata refresh through
PR880 and the unchanged base head. No pinned sprint coordination issue was
available, so the claim and result are recorded locally.
