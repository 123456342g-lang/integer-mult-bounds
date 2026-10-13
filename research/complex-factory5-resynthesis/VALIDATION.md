# Validation record

Prepared for alluri-ritual with substantial OpenAI Codex assistance. Apache-2.0.

Checked locally on 2026-10-13 UTC, macOS 26.6.2 arm64, from exact base
`66849e1475c930fd7732b1a0067ffee7e1e95f60`.

- CPython **3.14.3**: complete fresh constructor, local certificate, both raw
  native/emitted/independent replays and frozen receipt comparison pass.
- CPython **3.11.15**, with `-I -O -B`: same complete replay and byte-equivalent
  deterministic receipt pass. The inherited checkers are launched in isolated
  subprocesses with their assertions enabled.
- Search replay: Python 3.11 and 3.14 reproduce the exact 35-gate word after
  1,024 trials, including all five accepted improvements.
- Both raw words: 716 arbitrary input columns per orientation; full frame,
  compensation, source/helper restoration and private-work clearing checks.
  Ten new corruption controls pass. The inherited local audit rejects four
  controls per word: wrong scale, missing center, wrong common frame and wrong
  child rank.
- Relocated minimal source closure, in a path containing spaces, passes under
  isolated optimized Python. Five package controls reject a modified pinned
  constructor, a fabricated original circuit window, a corrupt expected result,
  missing source pins and an already existing output directory. The last check
  verifies that a pre-existing marker file is preserved.
- `python3 -B scripts/verify_selected_result.py` passes: the existing selected
  exact κ, original source inventory and proof supplements remain bound.
- Staged whitespace and changed-path checks pass; additions are confined to
  `research/complex-factory5-resynthesis/`. No existing file is modified.

`RESULT.json` is a deterministic scientific receipt, not a timing report. Source
archives retain exact byte hashes. Generated gzip files are compared through
all decoded JSON fields/canonical JSON hashes, excluding only inherited
runtime seconds and gzip-container hash fields from receipts. Macro counts,
matrices, column counts, frame/phase inventories, width arrays, primitive bills,
prefix bounds and control outcomes remain covered.

Commands:

```sh
python3 -B research/complex-factory5-resynthesis/verify.py
python3.11 -I -O -B research/complex-factory5-resynthesis/verify.py
python3 -B research/complex-factory5-resynthesis/search.py
python3 -B research/complex-factory5-resynthesis/test_package.py
python3 -B scripts/verify_selected_result.py
```

Expected final markers are `PASS_COMPLEX_FACTORY5_RESYNTHESIS`,
`PASS_SEARCH_FACTORY5`, `PASS_PACKAGE_CONTROLS` and the selected-record PASS.

The full repository suite and cold selected-provider replay were not run:
this standalone addition changes no selected supplier, assembly, generator or
existing artifact. Clifford phase lowering, global invoice/hosting, Linux CI,
Lean and integration through later transported recipes are not claimed.
There was no independent human or delegated-agent review. The proof boundary
is stated in `PROOF.md` and the README.
