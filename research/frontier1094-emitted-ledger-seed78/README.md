# The selected complex rank ledger, rebuilt from the emitted program it certifies

**Independent verification. No new κ, and no check is changed or weakened.**
- Card: `independent-moment` (ledger method), with the scope refined in [TASK.json](TASK.json).
- Track 75–84, assignment seed 78 (OS CSPRNG via Python `secrets`).
- Base commit `dadfea6e8a78ff6ba901705f87532a71c6f5bbb8`. At that base the selected record is
  frontier1094, κ = 0.001672660197076918.

## The obligation

The selected certificate `research/community-frontier1094-audit/ASSEMBLY.json` (`1122cb3a…`) prices
the complex profile `{1:349604, 2:60192, 3:62585, 4:20448, 5:11808, 7:7, 8:1152, 48:4866}`. This is
the aggregate that the authors' controller audit (`OWNERS-AND-PROFILE.json`) derived from the
emitted hosted program `GLOBAL-TEMPLATE`, whose digest the certificate records.

The selected κ uses the native complex recurrence, with no bad-class surcharge. The
[PR552 review](../native-complex-moment552/PROOF.md) allows that only because the emitted controller
has an "exact exhaustive recursive-child profile":
- every positive-rank frame climb and centre descent is a recursive child;
- the profile is the sum over all complete local invocations plus every nonempty idle remainder;
- all other work is finite work paid by the invoice.

This package closes one link of that argument: **the emitted recursive children equal the priced
profile**, under the review's classification rule (line 17). It does **not** discharge the review's
"no good/bad q-adic selector" argument (line 24), nor the whole-owner hosting semantics. The selected
record pins the review as `research/complex-multicold/vendor/pr559/PROOF.md` (`d5d498ed…`, in
`proof_supplements`), which is byte-identical to `native-complex-moment552/PROOF.md`.

For #1094, only author code had checked that link:
- the authors' ASYNC audit (`audit_allcold`), which counts declared ranks;
- the in-package #858 `indep16`, which replays the canonical frames but binds the backward profile to
  the author-provided local replay receipt.
- The maintainers' `INDEPENDENT1094.json` comes from
  `research/community-batch1099-audit/check_frontier1094.py`. It audits the owner map and prices
  the profile. It takes the local factor (804384 of the 1041408 rank mass) from the word's
  self-reported `local_profile` (line 21), and it hard-codes `live=14336, calls=144` (line 32).
- Open #1209 audits the pending axes and the owner map against package inputs and a parent
  template.

Neither reads the emitted template or the dispatched programs.

## What only this package does

`verify.py` uses only the standard library. It reads the committed replay capsule's members in
memory, imports nothing from the repository and executes no package code.

**Byte binding (B1–B9).** Members are resolved by their full bound path. The capsule also holds
decoy copies (`split-centres/`, `global8/`), and the controls show that they are rejected.
- The capsule digest equals its integration pin. Its tar members are regular, unique and
  non-traversing.
- The repository certificate equals the capsule certificate. Both equal the record's
  `certificate_sha256`: a checkpoint once the frontier moves on, otherwise the selected record.
- The template digest equals `ASSEMBLY.template_sha256`, and the owner audit digest equals
  `ASSEMBLY.input_sha256.owner_audit`.
- `LOCAL-PROGRAMS`, `CANONICAL-WORD`, `DATA-PHASES` and `INDEPENDENT-LOCAL-REPLAY` equal the owner
  audit's `source_artifacts`. The data phases also equal the template's own pin.
- The literal remainder frames equal their receipt.
- The owner map equals `owner_map_sha256` and is listed in `SELECTED-SOURCE.json`.
- `FULL-WORD` equals the `SLOT-PINS-k8.json` word.

**The emitted calls (L1–L13).**
- Every `(local stage, replica)` is called exactly once.
- Orientation and pair follow the recipe.
- Each call is bound to its dispatched program by compact-JSON sha256.
- The program and schedule vocabularies are closed: program events are only `scalar`, `climb`,
  `adapter`, `residual_adapter`, `phase` and `center`, and the schedule has seven kinds. This is what
  makes "every positive-rank climb/centre, and nothing else" exhaustive.
- Every register's frame is **replayed** in both orientations, from the word's `start` to its
  `final` frames:
  - each climb must leave the register's current frame for a strictly larger frame containing it;
  - its rank is recomputed by F2 elimination, and declared ranks are only compared;
  - centre *i* must run from `center_frames[i]` to the empty frame (forward), or back (backward),
    with its carrier register sitting at that frame.

  This is the first non-author, frame-derived recount of the dispatched `LOCAL-PROGRAMS` events bound
  to the selected template. The programs are also checked to equal those embedded in the template
  itself.
- The data routes are the active pair's 224 families, and all 704 owners of a call are distinct.
- Each helper route equals its hosted slot: family, child, offset, width and the structural
  spectator count.
- Each helper's climb total equals its hosted width and the template's width vector.
- W, N and m are read from the program.

**The emitted remainders (L19–L20).**
- The template's `idle_children` equal, one for one, the recount: each idle cover sweep's
  `DATA-PHASES` pending child minus its contiguous hosted prefix.
- Every literal `IDLE-REMAINDER-FRAMES` entry is the exact suffix of its pending axes, with full
  F2 rank. This checks the consistency of an auxiliary output that does not feed the ledger.
- The pending axes of sibling children are checked to be jointly **F2-orthonormal** on every
  `(pair, side, port)`, by pairwise dot products. That implies the direct sum.

**The chain to the certificate (L21–L25).**
- Every live family carries exactly m−1 = 72 data or pending units, so rank mass = (m−1)W + 64N.
  This is a checked accounting identity that pins any error to a single family. It also explains
  why D is invariant under repacking.
- The rebuilt ledger equals `ASSEMBLY.complex_profile`, the owner audit's `paid_profile` and
  `INDEPENDENT1094.owner.profile`.
- Helper climb totals equal the width vector of the `SLOT-PINS`-pinned `FULL-WORD`. This is a
  width-vector match, not a frame-by-frame comparison.
- The per-call ledgers equal the in-lineage local replay receipt.

The receipt also provides the fields requested in discussion #1200 (item 3), derived from the
emitted program: `local_profile_per_call`, `idle_histogram`, `families_per_call` and
`calls_per_family_by_pair`.

## Results ([RESULT.json](RESULT.json), reproduced byte for byte on every run)

The same unchanged code checks four records in the T16/T8 gauge44 layout:

| Case | W | N | Rebuilt ledger | Idle remainders | Rank mass | D = W − 64N |
|---|---:|---:|---|---:|---:|---:|
| **frontier1094 (selected)** | 14336 | 144 | {1:349604, 2:60192, 3:62585, 4:20448, 5:11808, 7:7, 8:1152, 48:4866} | 7526 | 1041408 | 5120 |
| frontier1042 (previous checkpoint) | 14336 | 144 | {1:349577, 2:60193, 3:62608, 4:20448, 5:11808, 7:3, 8:1152, 16:47, 48:4850} | 7550 | 1041408 | 5120 |
| slots T8 (in the 1042 capsule) | 7168 | 72 | {1:174763, 2:30105, 3:31283, 4:10224, 5:5904, 7:54, 8:576, 16:23, 48:2419} | 3783 | 520704 | 2560 |
| leaver T8 (in the 1042 capsule) | 7168 | 72 | {1:174763, 2:30105, 3:30275, 4:12240, 5:4896, 7:54, 8:576, 16:23, 48:2419} | 3783 | 520704 | 2560 |

For the selected record:
- The per-call ledger is `{1:2412, 2:418, 3:432, 4:142, 5:82, 8:8}` in both orientations, with 80
  forward and 64 backward calls.
- Families of pairs 0/1/2/3 are called 3/2/2/2 times each.
- Rank mass 1041408 = 144 × (1792 data + 3730 hosted-helper + 64 centre units) + 237024
  idle-remainder units. Equivalently, the pending mass 774144 = 537120 hosted + 237024 remainder.

In each of the four records, the profile the certificate prices is exactly the recursive-child
ledger of the program it binds.

The frontier1042 case shares its programs, word and phases with #1094, so it mainly exercises the
hosting and idle layer. The T8 cases change W and N, and the leaver case also has a different word
and programs. The constants are read from the data (`v`, `h`, `R`, the pairs in the recipe, `m`,
`live`), not hard-coded.

## Controls ([test_package.py](test_package.py): 33 tests, about 10 s)

Each control mutates the decoded inputs and must be rejected **by the named check**. Program edits
are consistent forgeries: the template's embedded copy and every call hash follow the edit.

**Frame replay:**
- A climb's declared rank is relabelled (L6).
- A climb is retargeted to a non-nested frame (L5).
- A climb is moved to another register, with the same rank and mass (L5).
- A climb is made descending (L5).
- A climb's from-frame is replaced by a different frame of the same dimension that is still nested
  (L5 chain).
- A centre's direction is flipped (L7).
- An unknown program event, or an unknown schedule kind, is added (L4).

**Calls:**
- The embedded programs differ from the dispatched ones (L3).
- A program hash is swapped (L3).
- An orientation is swapped and rehashed (L2). This is a consistency check only, since both
  orientations have the same per-call ledger.
- A call is duplicated (L1).
- W is changed (L9).
- A data route's family is duplicated (L10).
- A helper route is moved to another family (L11).
- Spectators are shortened (L12).
- **A whole pair-0 local stage is dropped consistently**, together with its recipe, calls and sweeps.
  Every structural check passes, and only per-family conservation sees it (L21).

**Hosting and remainders:**
- A label-disjoint but F2-dependent pending axis is introduced (L15).
- **A rank-0 child is made pending with an axis that keeps every sibling union orthonormal**. Only
  the recount against the emitted remainders sees it (L19).
- A slot gap is introduced and kept consistent across the owner map, template and route (L18).
- An owner-map field that no other check reads is changed (L16).
- An idle child is dropped, or a mass-preserving hosted/rank shift is applied (L19).
- A remainder frame is made dependent (L20).

**Certificate:**
- The certificate profile is tampered with (L23).
- The independent profile is tampered with (L23).

**Packaging:**
- The decoy `split-centres` programs (B6) or template (B4) are substituted.
- Another record's owner map is substituted (B7).
- One capsule byte is flipped (B1).
- Duplicate or `..` tar members are added (B2).

**Positives:** the four records, plus invariance under reordering the idle children and the
remainder frames at the decoded level.

## Reproduce

```sh
python3 -I -B research/frontier1094-emitted-ledger-seed78/verify.py        # ~2 s; PASS_FRONTIER1094_EMITTED_LEDGER
python3 -I -B -m unittest discover -s research/frontier1094-emitted-ledger-seed78 -p test_package.py
python3 scripts/research_package.py --package research/frontier1094-emitted-ledger-seed78 --check-only
python3.12 scripts/research_package.py --package research/frontier1094-emitted-ledger-seed78
```

The checks need only standard-library Python 3.10 or later; the generic replay uses 3.12. They need
no network, and they pass under `-O` because they use `need()`, not `assert`. Source commits, Git
blobs and SHA256 pins are in [SOURCES.json](SOURCES.json), and the case configuration is in
[CASES.json](CASES.json). No Makefile target is added, because the batch1099 audit pins the Makefile
by digest.

## Overlap, prior work and credit for shared checks

- **Open #1209** (akiva8201-dotcom, head `d1ba2631`, `research/selected1094-pending-axis-audit`)
  already checks these:
  - the cross-child F2 direct sum on all 896 pending bases, with an XOR-dependent-axis control;
  - frame-derived helper widths and contiguous prefixes;
  - the idle suffix profile and the complete profile.

  Our L15, L13, L18, the idle recount and the L15 control **replicate these as cross-checks**; they
  are not claimed as new. #1209 works from package inputs and a parent template. It does not read
  the capsule, the emitted template, the programs or the certificate.
- **The authors' in-lineage local replay** (`hpe_audit_local.py`, the "PR514/PR433 independent
  replay", pinned in `SELECTED-SOURCE.json`; capsule receipt `INDEPENDENT-LOCAL-REPLAY.json`) already
  recounts both dispatched programs. Open **#1184** (woklerx, head `2f1c9e0e`) ports that checker.
  - Our recount is **code-disjoint**. L25 compares against that receipt, which is never used as
    input.
  - That the scalar operations inside the programs respect their frames is covered by that
    in-lineage replay and by #1198, not here.
- **The per-family coverage identity** 8k_f + 1 + hosted_f + idle_f = 73, giving mass = 72W + 64N,
  is from our open **#1012**, where it is shown on T37/T21.
  - Our merged **#1069** observed D = W − 64N on 16 claims.
  - Open **#1240** (Mister-Meeseeks) uses the identity as the premise of its packing ceiling and
    re-checks it arithmetically on the #1094 profile. Its #1042 idle histogram matches our second
    case.
  - L21 is the T16 source-level check of that identity on the emitted #1094 and #1042 programs, so
    it provides source-level evidence for the premise #1240 assumes.
- **The maintainers' `INDEPENDENT1094.json`** recounts the idle remainders from the owner map. Our
  recount is a cross-check of it.
- **#1091** (Josie Elliston, seed67) audits the owner map and excludes the emitted controller.
- **Open #1255** (bitplane, head `add1e267`, `research/selected1094-chart-phase`; claimed in
  discussion #1237) audits the exact phase of #1094's residual charts. Our L11–L12 bind only the
  route structure and spectator counts. Spectator charts and phases are **not** validated here.
- **Complementary work:** #1112 checks the PR1042 invoice, guards, bootstrap and outer slacks;
  #1142 checks PR1042 capsule closure; #1149 checks the canonical-frame rank identity.

## Trusted, and not checked here

- **Event classification.** That positive-rank climb and centre events are recursive children, and
  that scalar, adapter, phase and residual-adapter events are finite work, is PR552's semantics.
  Closed vocabularies make the classification exhaustive; they do not re-prove it.
- **Pending axes.** The `DATA-PHASES` pending axes are taken as the inherited PR558 idle-child
  subspaces. They are checked for rank, port independence and direct sum.
- **Family layout.** The layout `replica·896 + (2·pair+side)·112 + port` follows #1091's rule R3.
  Per-family conservation holds only if this layout is right.
- **Capsule provenance.** The capsule bytes are bound by hash, not re-executed.
- **Downstream pricing.** Moments, the κ reduction, the invoice, guards, bootstrap and the 47 outer
  inequalities are not checked. #1069 prices this profile, and #1112 covers the #1042 invoice.
- **Inherited assumptions.** The all-size/compiler, hosting, precision/tape, analytic-transfer and
  PR589 H1–H5 assumptions are untouched.

## Open next questions

1. **Does the rebuild hold for the mixed-provider T37 templates of the open claims at
   0.0016756–0.0016758?**
   - Why it matters: those claims would replace the selected record, and their layout differs from
     the T16/T8 gauge44 layout assumed here.
   - First step: generalize the provider-dispatch and family-layout bindings, then run the checker
     on one claim's maintainer capsule.
   - Blocked by: no such capsule exists on main yet.
2. **Can the event-kind semantics be checked from the compiler rules, rather than only their
   exhaustiveness? Can the review's no-q-adic-selector argument (line 24) and the whole-owner
   hosting semantics be checked?**
   - First step: state each kind's operator from `notes/general-clifford-frames.tex` and test its
     fixed-frame action on a toy word.
3. **Do the 73-axis spectator charts and residual phases match the routes bound here?**
   - First step: combine #1255's chart-phase criterion with this package's call and route
     bindings, so the charts are checked on exactly the routes that are priced.

## Credit

- Rohan Arun, with OpenAI Codex assistance: #1094.
- jeremykothe2, with Claude assistance: PR1087 and the T16 owner-packing lineage.
- FanPUYen: PR858.
- rohanarun: PR987/PR1018.
- PR1005, NewBArch PR869, and the retained PR799/741/685/645/589 lineage.
- The PR552 native-complex review, the PR558 data phases and the PR514/PR433 local replay.
- Josie Elliston: seed67 (#1091).
- akiva8201-dotcom: #1209.
- woklerx: #1184 and #1149.
- Mister-Meeseeks: #1240.
- bitplane: #1237/#1255.
- Douglas Colkitt, with OpenAI Codex assistance: the maintainer replay capsules and the independent
  pass.

Prepared by Sagar Thakrar (thakrarsagar) with substantial AI assistance from Claude (Anthropic) via
Claude Code. Parallel read-only scout and judge subagents selected and designed the check. Two
adversarial judges and a live Discussions sweep found the overlaps above. New material is
Apache-2.0.
