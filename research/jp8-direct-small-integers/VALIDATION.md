# Executed validation

Linux x86_64, CPython 3.12.14, 13 October 2026. Exact base:
`007664306fff84fbb1c9a1b4053b69f439764034`.

- `python3 -I -O -B research/jp8-direct-small-integers/verify.py --write NEW_PATH`
  generated the exact receipt; the same command without `--write` compares it.
- Both complete primitive projections passed all 725 formal input columns at
  every macro boundary and at the final expected shear. The source pin and
  SPEC/program bindings passed. All 1,424 replacements in each orientation
  were checked, with cost/access counts and unchanged prefix/grid metrics.
- All 13 dense mathematical/interface rejection controls passed, alongside
  four early-clear positives and four reduced-coefficient positives.
- `python3 -I -O -B research/jp8-direct-small-integers/test_package.py`:
  **6 tests passed** in 11.194 seconds. Includes 3,000 integer-row arithmetic
  crosschecks, source corruption, gzip recompression, optimized minimal offline
  relocation in a path with spaces, typed-receipt corruption and existing-output
  preservation. The timing is a local test duration, not a performance claim.
- `make selected-record-check`: passed, selected conditional kappa remains
  `1661957774647029/1000000000000000000`.
- `python3 -B -m unittest discover -s tests -p 'test_selected_result.py' -v`:
  **5 existing tests passed** in 0.740 seconds.

No existing generator, production lowerer, selected artifact, workflow or
upstream source is modified. Full `make verify`, native physical/phase/owner
replay, cold supplier reconstruction, global invoice/assembly, Lean, a second
platform and hosted CI were not run. Their inherited scope is not represented
as newly verified. Relevant focused checks are used for this isolated package.

Final patch application, clean export and whitespace results are recorded in
`HANDOFF.md`. `OVERLAP.json` records the final metadata refresh and exact heads.
