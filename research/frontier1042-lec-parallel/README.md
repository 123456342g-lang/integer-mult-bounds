# Parallel layer-end controls for the frontier1042 leaver chain (opt-in, byte-identical receipts)

**Status: tooling improvement (verification engineering). No new κ, and no check is changed or
weakened.** It extends merged PR1059, whose runner is pinned to the T37 variant only, to the
leaver variant that the frontier1042 chain runs five times.
Track 85–94 (verification engineering), assignment seed 89 (OS CSPRNG via Python `secrets`).
Base commit `ce7ad1b6ab09452c3478723a2e96ed5ff212dc08` (selected κ = 0.001672660197076918,
frontier1094).

## What it speeds up

A cold `make frontier1094-verify` first runs `scripts/verify_frontier1042.py` as its
`baseline1042-cold` stage, and so does `make frontier1042-verify`. The recorded frontier1042 run
took 1162 s, with the #799 baseline reused. Its `chain` stage (`reproduce_leaver_chain.py
--id k8`) took 711 s of that, and **530 s of the chain are its five layer-end-control steps**:

| Step | Word (payload) | Recorded seconds |
|---|---|---:|
| `lec-p6n` | p6n `25c40614…` | 139.8 |
| `lec-promo` | promoted `84d4da2e…` | 115.5 |
| `lec-jx` | jx `84d4da2e…`: the k8 X4 exchange is the identity, so this is the promoted word again | 116.3 |
| `lec-hyb` | hybrid `c836d892…` | 78.5 |
| `lec-frames` | final `db2c7cfb…` | 79.4 |

Each step runs the Q6Reviewer-signed `layer_end_controls_leaver.py` v2 (`4ba676f1…`) through
the pinned `run_portable.py` launcher (`322d29d4…`). The script audits the unmutated word and 95
mutated words with PR635's `hpe_audit_and_transport.run` (`c9a05ff2…`). Every mutant must be
rejected for its pinned reason, and the not-applicable sites must equal the declared ones. The 96
audits are independent pure computations.

The runner also accepts the T37-type variant `layers_p6n/layer_end_controls.py` (`fc58c569…`),
which is merged PR1059's target, and checks it against the archived T37 receipt. That variant is run by the T37 replay's `u8-native` stage (77 s recorded) and
once by the #799 native stage that a cold `make frontier1042-verify` rebuilds
(`gauge44-frames-x/construction/jx/reproduce_jx.py:79`). Scripts are accepted **by digest**, so
every byte-identical copy is covered: three copies of `4ba676f1` and ten of `fc58c569` on main, plus the
`4ba676f1` copies in open claims PR1104 and PR1107 (`research/gauge44-ends7-t16`).

Who runs these steps today: every cold `frontier1094-verify` or `frontier1042-verify`, and every
chain rebuild, such as a batch's shared candidate replay. The recorded frontier1094 replay
(58 s) reused the completed frontier1042 baseline. Claims that reuse the k8 chain as ancestry do
not rerun these steps.

## How

`lec_parallel.py` is a drop-in for one step. It takes the same arguments and environment
(`PR635_CODE`, plus `LEC_REASON_PINS` for the leaver variant), uses the same interpreter settings
as the chain, and prints the same output. It parallelizes the audits **without editing or
re-implementing the pinned launcher, script or audit**:

1. **Record.** The pinned launcher runs the pinned script once with a stand-in
   `hpe_audit_and_transport` that only records the exact gzip bytes of each trial word. The first
   (unmutated) word gets success, and every other word gets a placeholder rejection, so this pass
   decides nothing. Its receipt goes to a scratch directory and is discarded. As each word is
   recorded, the real audit of it starts in a worker process.
2. **Evaluate.** Every distinct word is audited by the real, digest-checked PR635 `run` in a
   worker. The worker captures exactly the outcome `trial()` would see (success, or the
   `AssertionError` arguments) and the audit's printed output.
3. **Replay.** The pinned launcher runs the unchanged script again. Its stand-in prints the
   captured output and returns or raises the real outcome for the identical bytes. The script's
   own assertions then accept or reject every control, check every pinned reason and the
   not-applicable sites, and write `COLD-END-CONTROLS.json`. The sequence of trial words must
   equal the recorded one, and a word the record pass never saw is an error.

Outcomes are keyed by the sha256 of the exact trial bytes and the resolved routing path.
`chain_lec.py` runs the five steps as `lec()` does, sharing one worker pool and one outcome
table. Because `lec-jx` builds exactly `lec-promo`'s 96 trial words, it reuses those outcomes and
audits nothing.

`chain_lec.py` also checks each step:
- **Before.** It binds the word's payload to the recipe pin that the chain asserts when it builds
  that word (`COLD-LAYERS-RECIPE-P6N`, `PROMO-RECIPE`, `RECIPE-X4`, `RECIPE-U8`,
  `FRAME-RECIPE-LV`).
- **After.** It applies `lec()`'s own checks against `CHAIN-PINS-k8.json`: the pins-file digest,
  PASS status, 95 rejected controls and the declared not-applicable sites.

## Benchmark (same machine, same inputs; descriptive only)

Machine: macOS 26.5.2 arm64, 10 cores, Python 3.14.8, `--jobs 10`. There were two full
`verify.py --serial` runs on a shared machine (load average 5–15). The full data is in
[`BENCHMARK-macos-arm64.json`](BENCHMARK-macos-arm64.json). It was measured at `ba82555c`, and every pinned
input is unchanged at the base commit.

| Step | Recorded serial (maintainer) | Pinned serial, run 1 / run 2 | Parallel, run 1 / run 2 |
|---|---:|---:|---:|
| `lec-p6n` | 139.8 s | 52.6 / 63.8 s | 22.8 / 26.7 s |
| `lec-promo` | 115.5 s | 53.4 / 65.2 s | 23.2 / 27.7 s |
| `lec-jx` | 116.3 s | 53.1 / 53.9 s | 14.1 / 17.6 s (0 audits: reused) |
| `lec-hyb` | 78.5 s | 53.5 / 53.5 s | 18.1 / 30.4 s |
| `lec-frames` | 79.4 s | 54.2 / 57.1 s | 18.9 / 41.2 s |
| **five steps** | **529.5 s** | **266.7 / 293.5 s** | **97.1 / 143.6 s (2.7× / 2.0×)** |
| T37 `layer_end_controls.py` (secondary) | 77.0 s | – / 59.7 s | – / 20.0 s (3.0×) |

What remains is the pinned script's own mutant construction: a deep copy, JSON and gzip of each
word. By design it runs twice, once in the record pass and once in the replay (the
`record_seconds` and `replay_seconds` in the receipt). The audits finish while the record pass is
still running: the wait for them is 0–2 s per step. On a busy machine, the single-threaded record
and replay passes compete with the workers, which explains the spread between the two runs.

## Evidence of equivalence

`make frontier1042-lec-parallel-verify` checks the following:

- **Archived maintainer receipts.** All five `COLD-END-CONTROLS.json` from the parallel run equal
  the receipts in the selected replay archive (`selected-replay.tar.gz`, `22c3f4dc…`, every member
  digest pinned) **byte for byte**. One field is rewritten first: `word`, the input path the
  pinned script records, goes from `/private/tmp/batch1047-selected/chain/…` to this run's
  directory, and the archived receipt must contain that path exactly once. The T37 variant gets
  the same check against the T37 replay archive (`t37-replay.tar.gz`, `48285025…`), on its barch
  word bound to PR870's `RECIPE-U8` pin.
- **Pinned serial reference** (`--serial`, which is also `make frontier1042-lec-parallel-benchmark`).
  All six receipts are byte-identical to those of the pinned launcher and script, run serially
  on the same paths with one process per step as the chain runs them. The step logs are identical
  except for the audit's own wall-clock `"seconds"` value.
- **Controls** on the final word, through the same runner. None of them may leave a receipt:
  - C1: a corrupted unmutated word (one gate coefficient doubled) fails at the pinned script's
    own first assertion, `unmutated cold-end word must pass`.
  - C2: a forged acceptance of one mutant's outcome makes the pinned script fail with
    `cold-end mutation accepted`. Real outcomes decide, not the record pass.
  - C3: a forged rejection with an unrelated message makes it fail with `rejected for the wrong
    reason`. The pinned reasons are still checked.
  - C4: a one-byte change to the pinned script, or to PR635's audit, is refused before any work.
- **`test_package.py`** checks the following:
  - the placeholder semantics and the pins;
  - the recipe bindings, including that the k8 X4 word equals the promoted word;
  - that `run_pinned` restores `sys.argv`, `sys.path`, the stand-in module, `sys.stdout`,
    `Path.write_text` and `gzip.compress`;
  - that the launcher's portable gzip header reaches the trial words;
  - that the real audit accepts the final word and rejects a corruption.

## Using it

```sh
make frontier1042-lec-parallel-verify      # archives, parallel runs, 6 receipt matches, C1-C4, unit tests
make frontier1042-lec-parallel-benchmark   # also runs the pinned serial references
python3 -B research/frontier1042-lec-parallel/chain_lec.py --chain WORK/chain --out NEW_DIR
                                           # the five steps on a completed reproduce_leaver_chain.py output
python3 -B research/frontier1042-lec-parallel/lec_parallel.py WORD ROUTING OUT [--script PINNED_SCRIPT]
                                           # one step, drop-in (environment as for the step)
```

The expected last line is `PASS_FRONTIER1042_LEC_PARALLEL`. It needs standard-library Python 3.11
or later, no network, and no inputs outside the repository.

**Not wired.** `reproduce_leaver_chain.py` and `verify_frontier1042.py` are unchanged and still
run the serial steps. They are manifest-pinned, so wiring is the maintainers' call. In `lec()`,
the step's command would become `lec_parallel.py WORD ROUTING OUT`, run without the launcher
prefix, because the runner executes the pinned launcher itself. The chain's three `phases` steps
(469 s recorded) call the same pinned `phases_full.py` and `clifford_exact.py` as the merged
PR1041 runner, so that runner takes them unchanged. It was not re-measured on these words in this
package.

## Relation to other work

- **PR1059** (ours, merged) applies the same record/evaluate/replay design to the T37 variant
  only. Its runner hardcodes that digest, and its verify, pins and receipts are bound to T37.
  This is a separate package, so PR1059's pinned files stay untouched. It does the following:
  - accepts both variants, by digest;
  - runs the five leaver steps of the frontier1042 chain;
  - adds execution through the pinned launcher;
  - captures the audit output, so step logs match;
  - shares one outcome table across steps;
  - adds the recipe bindings, the `CHAIN-PINS` checks, and the forged-outcome controls C2 and C3.
- **PR1137** (Wronskode, open) targets the same five steps differently. It provides a faster exact
  re-implementation of PR635's audit, cross-checked against the pinned one: 2.53× in a single
  process. This package instead runs the pinned audit **unchanged** and uses more cores. The two
  compose only partly. Under this runner the audits already finish inside the record pass, so its
  floor is the pinned script's own mutant construction. That construction runs twice, and a
  faster audit does not shorten it.
- **PR1041** (ours, merged) covers `phases`. PR853 (navinor, merged) and PR1101 (rcfc-jreed, open)
  run independent stages of the #741 replay concurrently. This package parallelizes inside a step
  and composes with all of them.

## Scope

This package accelerates individual steps. It discharges no mathematical obligation, the selected
κ is untouched, and the timings are local measurements. An audit worker failure other than an
`AssertionError` makes the replay fail with a `RuntimeError`, where the serial script would fail
with the original exception; both are failures.

## Credit

- Q6Reviewer: `layer_end_controls_leaver.py` v2 and the signed `layers_p6n/layer_end_controls.py`.
- DreamingOfClouds: the original `layer_end_controls.py`, adapted from PR635's cold-end controls.
- PR635's authors: `hpe_audit_and_transport.py`.
- LeaverSAT and LeaverSAT2: the k8 leaver cells and recipes.
- ColdWitness: `reproduce_leaver_chain.py`.
- icekylinx: the gauge44 package.
- Jeremy Kothe, Rohan Arun and Hao Yan: the frontier1042 composition.
- Jeremy Kothe and NewBArch: the PR869/PR870 barch word.
- Jonathan Capalbo: the PR942 replay.
- Douglas Colkitt, with OpenAI Codex assistance: maintainer orchestration and the replay archives.
- Prior concurrency tooling: PR853 and PR921 (navinor), PR1101 (rcfc-jreed), PR1041 and PR1059.
- Wronskode: PR1137, the concurrent exact fast-audit approach to the same steps.
- Prepared by Sagar Thakrar (thakrarsagar) with substantial AI assistance from Claude (Anthropic)
  via Claude Code. Candidate selection used parallel read-only scouting and judging subagents. New
  material is Apache-2.0.
