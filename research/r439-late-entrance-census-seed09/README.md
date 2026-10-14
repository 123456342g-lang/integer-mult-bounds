# Late-compensated helper entrances on the R439 bit word: a scoped census

**Scoped negative result with one open survivor. No construction and no new κ.**

- Track: 00–19 (bit supplier), assignment seed 9, drawn with the OS CSPRNG via Python `secrets`.
- Card: `bit-helper-contract`, with the scope **refined** in [TASK.json](TASK.json).
- Base: `0b1cccf8`. The selected record frontier1094 is complex-bound and unchanged.

## The question

The inherited H2/K interface requires every helper to start at frame 0, so that a frame-0 prefix D can supply all dirt compensation (N = K). An entrance would let a helper start at a nonzero frame E instead: a pivot p with the gauge q ^= p on a support c. Doing so changes the response by ρ = Kc, so the targets in T = supp ρ need extra compensation.

Merged work decides only the case T = ∅:
- #1179 found the one kernel entrance, the pair 444+470.
- #1253 showed it is the unique one among common-frame entrances, over all 366 closure classes.
- #1128 (PROOF §4) leaves "compensation moved after A" open.
- #1179 says its K e_J = 0 condition is "not a statement about arbitrary later compensation".

This package settles that open case for **compensation after the scatter**, on fixed A and scatter, one entrance at a time. It covers every support of #1253's closure: 4,954 supports from 5,548 (V, c) pairs, plus 5,212 source-donor entrances. The words are the selected PR589 word and the four merged star words: PR1062 (#1062), PR1122 (#1122), PR1188 (#1188) and PR1208 (#1208).

## The test

For each target t, W_t is the **dirt-only space**: the helper parts of all F2 combinations, with zero source part, of the values that t could legally read after the scatter. A support c is admitted only if every t ∈ T has some u ∈ W_t with u·c = 1. Otherwise it is **rejected**.

The test runs in three classes:

| Class | What t may read | Status of a REJECT |
|---|---|---|
| **LC-fav** | any register whose frame at the scatter cut lies in t's final frame t⊥, plus the nine COPY snapshots | **Sound for the whole class** of any post-scatter program with monotone frames and the stated premises ([PROOF.md](PROOF.md)). This is the necessary test. |
| **A6** | B ++ C unchanged, plus inserted target reads with a carrier check (the reading and the read register must both fit inside the gate's frame) and read-only relays | Sound for A6. A6 is contained in LC-fav. |
| **A6R** | A6 plus storage relays, where a target that received reads may be read later; relay restoration is ignored | An over-approximation, used only to show that a survivor is *not* excluded. |

The scout's original "strict" class is also reported, for traceability only. It has no carrier check, so it is not physical, and on these words it equals LC-fav.

## Results ([RESULT.json](RESULT.json); identical on all five words)

| | LC-fav | A6 |
|---|---|---|
| Supports admitted | 2: 444+470 (T = ∅, #1179's kernel pair) and **444+470+578** (\|T\| = 8) | 1: 444+470 (T = ∅) |
| Single helpers | 0 / 439 | 0 / 439 |
| New pairs | 0 / 1,569 | 0 / 1,569 |
| Source donors (5,212) | 0 kernel, 0 late | 0 kernel, 0 late |
| Linear relaxation (366 classes) | 1 nonzero class (frame 79's line), kernel {444+470, 578}, 84 rows kept | 1 nonzero class, kernel {444+470}, 94 rows kept |
| max dim W_t | 5 | 4 |
| K incidences covered | 98 / 18,085 | 47 / 18,085 |

**So, apart from the kernel pair:**
- No late-compensated entrance exists in A6.
- In the sound LC-fav class, only the triple **444+470+578** survives. Its targets are 113, 118, 150, 153, 192, 197, 214 and 219.

**The triple is OPEN.**
- A6 covers only targets 150 and 197.
- A6R covers all 8.
- A6R restricted to relays inside T covers 150, 153, 192 and 197.

So a realisation would have to park content carrying x₇₇ in targets outside T, and those targets would later have to cancel it. This package hands that question on (open question 1).

**The structural reason.** After the scatter, no register carries helper dirt free of source columns beyond a space of dimension at most 5 per target (4 in A6). Each target can therefore repair at most a few helper directions late.

## Two engines and the controls

**Engine 1** ([census.py](census.py)) does the raw replay and computes K, first contacts and the closure L. For each class it builds W_t, runs the parity census of every support, the linear relaxation per class, the source donors and A6R.

**Engine 2** ([engine2.py](engine2.py)) shares no code with engine 1:
- set-valued replay;
- rational-annihilator geometry;
- a closure that also equals #1253's `CERTIFICATE.json`;
- LC-fav by a kernel method;
- A6 by per-pair change points.

It agrees with engine 1 on K, the closure, every W_t (LC-fav and A6) and every verdict. Engine 2 also checks that every frame is closed, so label inclusion equals rational containment.

**Controls** (recorded in RESULT.json, and covered by 20 tests in [test_package.py](test_package.py)):
- **Pre-A window.** If every helper is readable at frame 0 before A, all 4,954 supports are admitted.
- **The kernel pair.** 444+470 has T = ∅ and is admitted by every class.
- **A synthetic positive word.** `W_syn` is PR589 plus three reads into target 150, with its D edited to match.
  - The census admits 444+470 there as a late entrance, at target 150, in LC-fav and A6.
  - Its built witness passes the merged `wlib.replay` and saves the pivot's first climb (1:1322 vs 1:1323): start[444] = 79, a shear at the head of A and its inverse at the end of C, and D without 444.
  - `W_syn` with its D unedited fails replay at register 150.
  - Both words are rebuilt deterministically and checked by their canonical sha256.
- **Mutations.**
  - Flipping one K bit rejects 444+470.
  - Clearing K's column 578 admits 578.
  - Letting register 77 be read at FULL admits the triple in A6.
  - Emptying target 150's reads rejects the triple.
- **Binding.** A byte flip or a wrong pin is rejected.

## Scope

**What the result covers.** For each single common-frame entrance on these five words, with A and the scatter fixed, no pre-scatter wires and the endpoint required on all 661 columns:
- the LC-fav REJECTs are proofs for the whole post-scatter class;
- the A6 REJECTs are proofs for insertion-only compensation.

**What it does not cover:**
- a changed A or scatter, or a new COPY;
- gauge shears after A or at more than one frame;
- source-dependent basis changes other than the donor shear;
- several simultaneous entrances;
- recursive interfaces or hosting.

**No κ either way.** The bit side does not bind. An entrance would at most save the pivot's first climb (−H1), and width-8 hosting cancels that with +H1 (#1179, #1253).

## Reproduce

```sh
python3 -I -B research/r439-late-entrance-census-seed09/verify.py          # about 3 min; PASS_R439_LATE_ENTRANCE_CENSUS
python3 -I -B -m unittest discover -s research/r439-late-entrance-census-seed09 -p test_package.py
python3 scripts/research_package.py --package research/r439-late-entrance-census-seed09 --check-only
python3.12 scripts/research_package.py --package research/r439-late-entrance-census-seed09
```

`--no-a6r` skips the A6R runs and stops before RESULT.json is checked. It needs standard-library Python 3.10 or later. It was run on Python 3.14.8 (macOS 26.5, arm64).

## Open next questions

1. **Can the triple 444+470+578 be realised with storage relays?** It is the only support that survives LC-fav, and A6R covers its 8 targets only through relays outside T that must later cancel their x₇₇ content.
   - First step: record which relay reads A6R uses for each target, build a candidate word from them, and test it with `wlib.replay` and #1179's literal stream checks.
   - Blocked by: restoring those relay targets.
2. **Do simultaneous entrances admit late compensation where single ones do not?** The joint test needs (K_t·c_i)_i ∈ {(u·c_i)_i : u ∈ W_t} for every t.
   - First step: run it over pairs of disjoint supports in the same class V.
3. **Does a changed scatter enlarge W_t enough to admit a late single entrance?** The dim W_t ≤ 5 bound belongs to this scatter.
   - First step: add snapshot terms to scatter rows (already inside the class), then move one retained total, priced with #1128 §5.

## Relation to earlier work and credit

- **#1128** (aliromman): the width-seven boundary obstruction. Its PROOF §4 names the case decided here, and its cone lemma (§2) is used in PROOF.md.
- **#1179** (adamgall): the 444+470 kernel entrance, whose literal stream checks are reused as a witness check.
- **#1253** (mightyOil): all-support common-frame kernel entrances, the closure L and its certificate, which is reproduced here.
- **#1194** (woklerx) and **#1311** (Arham-Tahir64): the semantic-D contract. The star words come from **#1062** (thakrarsagar), **#1122** and **#1188** (bitplane) and **#1208** (ToikY).
- **Precedents:** #254 (Dugongue) and #382 (chafreaky) for kernel entrances.
- **Different mechanisms:** open #1810 (RossRichardson; dirty workspace on B), and open #1580/#1592 (Arham-Tahir64; terminal star compensation).
- **PR589 and the replay library `wlib.py`:** DreamingOfClouds and the PR555/PR589 lineage.

Prepared by Sagar Thakrar (thakrarsagar) with substantial AI assistance from Claude (Anthropic) via Claude Code.
- Parallel read-only scout and judge subagents selected the question.
- Reader subagents and a synthesizer audited the scout's criterion. They found the triple the scout missed and the missing carrier check in its strict class, and they specified the classes.
- The engines, the proof note and the controls were then written fresh.

No claim was posted to Discussions. New material is Apache-2.0.
