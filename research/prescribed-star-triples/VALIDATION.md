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

The pre-submission refresh inspected **721 open PRs through #931**. Main
and PR669's pinned head were unchanged. No matching prescribed-triple
classification was found. PR669's selectable hierarchy and minimum-cost
criterion are credited; the new contribution closes only its remaining
k=2 prescribed-triple budget question without the empty star. PR732/772
concern different global thresholds and ranks. No pinned coordination
issue existed at selection or refresh; the claim was recorded locally.

Only this research package is added. `upstream/`, the selected certificate,
existing generators and supplier artifacts are unchanged. The applicable
focused checks and selected-record integrity pass. The repository-wide
regenerating suite and full selected-supplier cold replay were not repeated.
Both checkers also passed isolated optimized replay from an export of the
staged Git blobs, launched outside the checkout. Staged whitespace checks
passed. No hosted CI, independent human review or proof-assistant verification
is claimed. Paid implementation, all-size/compiler, hosting, precision/tape
and analytic obligations remain outside this information-threshold result.

The next useful review is of the four-block concentration argument and
the exceptional two-pair path, followed by consideration for integration
as a scoped research note. Granting the empty star is a different open
classification, not an implication of this theorem.
