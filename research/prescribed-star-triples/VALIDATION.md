# Validation and handoff

Verified on 2026-10-13 in the prepared Linux Codex Cloud environment:
CPython 3.12.14 and g++ 14.2.0. Python checkers use only the standard
library. The independent search also needs a C++17 compiler. No packages
were installed for this contribution.

From the repository root:

```sh
python3 -I -B research/prescribed-star-triples/verify.py
python3 -I -B research/prescribed-star-triples/run_independent.py
python3 -I -O -B research/prescribed-star-triples/test_package.py
make selected-record-check
```

All four commands passed. Actual output is retained in [evidence/](evidence/).
The primary result is 44,100 target triples, 18+19 symmetry orbits and
645,606 four-block partitions. It checks 3,060 literal surviving-source
columns, 740 one-port-restoration rejections and three other invalid-decoder
controls. Its complete deterministic receipt matches CERTIFICATE.json.

The independent optimizer completes **306,446,336** normalized coefficient
assignments across p=5,6, permitting all eight labels. Its separate orbit
canonicalization and binary row-space checks agree with the primary minima
and orbit sizes. It independently rejects 740 restored ports in those two
domains. Additional p=2,3,4 finite checks are recorded separately; all 224
prescribed triples at p=2,3 also pass an exhaustive deletion-mask comparison.
The p=3 empty-star control changes a target triangle from impossible to a
five-deletion decoder. This is a boundary control, not a classification of
the larger observation model at p=5,6.

The three packaging tests pass in isolated optimized Python. They reject
an underpriced exceptional receipt, preserve the absence of output after
failure, reject modified predecessor bytes, and reproduce byte-identical
receipts after relocation into a path containing spaces. Existing output
files are preserved. The independently implemented search also passed a
full optimized replay and rejection of corrupted receipts, existing output
paths and out-of-range parameters. C++ compilation with
`-std=c++17 -O2 -Wall -Wextra -pedantic` produced no warnings.

Separate AI-assisted adversarial review checked the uniform proof, the
connected-optimum qualification, all forest shapes and the empty-star
counterexample. Its separate scratch implementation checked bridge versus
binary-row recovery on all 4,096 retained p=3 graphs (24,576 retained-edge
comparisons), all three-target vertex-basis choices at p=5,6,7, and all
35 feasible primary witnesses against direct row-space recovery. Those
supplementary scratch checks and reviews are retained in the recovery
archive; the submitted theorem does not depend on unshipped scratch code.
Agent agreement is supporting evidence, not a proof.

## Sources, overlap and limits

Exact base is `91a2094f2e022930069e8cfdc810a3ea1b81cd09`.
The two retained PR669 proof texts are SHA256-pinned in SOURCES.json;
their Git blob IDs were also checked against GitHub's contents API at
head `7d526020fc368ce4157cd436995c2f4fcf683318`. No predecessor executable
code or solver is imported. The latest ledger has no scoped exact-head
review of that pending PR; attribution here does not imply its acceptance.
The needed argument is rederived in PROOF.md.

A follow-up compliance audit consulted the exact [contributor guide at
47481c8](https://github.com/CrocSwap/integer-mult-bounds/blob/47481c89fd30a43f8f882eb4b391e89c29273fd0/CONTRIBUTING.md).
It is byte-identical to the guide read at the base commit (SHA256
`1cae543effcabab91dab7f78423ee9283e60fb504f10848483d153331cd72bc4`).
The referenced [contribution-review index](../../docs/research/contribution-review.md)
was consulted during this follow-up, rather than before building on PR669.
It explicitly records historical triage through PR40, is not the current
queue, and contains no PR669 acceptance or conflicting prescribed-triple
finding. Source pins, attribution, mathematical scope, README/proof consistency,
negative controls, Apache-2.0 notices and substantial AI disclosure were
checked against the guide. No closure or integration of predecessor work
is implied by this audit.

The initial pre-submission refresh inspected **721 open PRs through #931**;
main and PR669's pinned head were unchanged at that time. The follow-up
refresh, completed after the broad checks at **2026-10-13 15:01 UTC**, inspected
**715 open PRs through #962**, plus the previously inspected closed PR932/935
bodies. No matching prescribed-triple classification was found. Nearby PR939
and PR954 study E8 punctures with different geometry and cost objectives;
PR958 uses k=5 quadratic geometry and explicitly excludes punctures. The
physical scalar target forests of PR961 and supplier construction of PR962
also use different contracts. The dirty-connector query schedules in
PR934/938/943/944 use different observations and interfaces. PR669 remains
open at the same pinned head; fresh source responses match both retained files.
Its selectable hierarchy and minimum-cost
criterion are credited; the new contribution closes only its remaining
k=2 prescribed-triple budget question without the empty star. PR732/772
concern different global thresholds and ranks. No pinned coordination
issue existed at selection or refresh; the claim was recorded locally.

During this work upstream advanced to
`007664306fff84fbb1c9a1b4053b69f439764034`, selecting PR890 with conditional
κ `1661957774647029/10^18` (source
`4b3bd8cbe8e3e81c44161017c9b72c905a8040a8`). The current status, selected
record, maintainer review, ledger and contribution index were consulted at
that revision. The #799 context in SOURCES.json describes the original
research base; the follow-up snapshot is recorded separately. Neither
selected supplier is a mathematical or executable dependency of this note.

Only this research package is added. `upstream/`, the selected certificate,
existing generators and supplier artifacts are unchanged. The applicable
focused checks and selected-record integrity pass. The repository-wide
`make verify` suite **passed (exit 0)** in an isolated local clone at contribution
commit `70484032ff4ae960b19acc8e159622e7e6ac8bac`: all 18 sequential groups,
87 isolated test modules and 20 historical patch checks completed in
4,840.266 seconds. The [compact receipt](evidence/make-verify.json) records
the tested head, timestamps and full-log SHA256; the log is in the recovery
archive. This is a run on the original base, not current-main integration.
The later edits only add documentation, context metadata and evidence;
proofs, executable checkers, certificates and predecessor bytes are unchanged.

The historical PR741 cold replay included in that suite also passed current
main's supported `scripts/verify_replay_coverage.py --frontier 741` gate,
using its existing output. The exact current-main checker validates the
22-stage/44-artifact contract, bridge controls and original composition
bindings; its [receipt](evidence/current-main-741-coverage.json) reports
`PASS_COMPLETE_PR741_REPLAY_COVERAGE`. The historical driver, binder and
supplier packages are byte-identical at the original base and `0076643`.
This additional admission check did not rerun producers or validate PR890.
The #799 and current #890 selected-supplier cold replays were not run because
this contribution changes neither construction.
Both checkers also passed isolated optimized replay from an export of the
staged Git blobs, launched outside the checkout. Staged whitespace checks
passed. No hosted CI, independent human review or proof-assistant verification
is claimed. Paid implementation, all-size/compiler, hosting, precision/tape
and analytic obligations remain outside this information-threshold result.

The next useful review is of the four-block concentration argument and
the exceptional two-pair path, followed by consideration for integration
as a scoped research note. Granting the empty star is a different open
classification, not an implication of this theorem.
