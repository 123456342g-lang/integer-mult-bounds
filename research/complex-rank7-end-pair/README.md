# Two rank-seven helper ends: conditional κ = 0.001661712108827881

This construction increases PR799's conditional κ from
`0.001661634653669567` to **`0.001661712108827881`**. The exact increase is
`38727579157 / 500000000000000000`, approximately **0.00466138%** of the
preceding κ. This compares asymptotic exponent savings, not measured runtime.

The change has two parts. Helpers 588 and 589 finish in dimension seven instead
of eight. Eight B frames and two early-cleanup frames change with those ends.
An explicit new owner assignment then combines the released space into
rank-48 residuals. All raw scalar gates, their order, the ports, the center
interface, and the 72-call schedule retain their PR799 values.

| Quantity | PR799 | This construction |
| --- | ---: | ---: |
| Local rank-one children | 2548 | 2542 |
| Local rank-two children | 338 | 352 |
| Local rank-three children | 430 | 422 |
| Local rank-four / five / eight children | 194 / 56 / 8 | 194 / 56 / 8 |
| Helper width per call | 3778 | 3776 |
| Global idle profile | `{1:1, 3:1, 44:1, 48:2396}` | `{48:2400}` |

The complete global profile is
`{1:183024, 2:25344, 3:30384, 4:13968, 5:4032, 8:576, 48:2400}`.
Its rank mass is 520704. The certified complex endpoint is
`0.001664477992062168466854`; the retained PR589 bit endpoint is
`0.001733427039589844234749`. The complex supplier remains the limiting one.
The conservative complex calculation separately gives
`κ = 0.001661712105945928`.

From the repository root, use Python 3.11 or newer and Git:

```sh
python3 -B research/complex-rank7-end-pair/reproduce.py --work /tmp/rank7-end-pair
```

Use a new output directory. The command fetches the three exact source commits
in `SOURCES.json` into that directory. It rebuilds the PR741 ancestry and PR799
word, applies the twelve changed annotations, rebuilds the owner assignment,
and runs complete native and global admission. No optimizer or Python package
installation is required. If a local repository already contains the pinned
commits, add `--git-repository /absolute/path/to/repository` to use its objects
without fetching. Source files are extracted into the output directory in
either case.

Expected final output:

```text
PASS_COLD_RANK7_END_PAIR_COMPLETE_ADMISSION 0.001661712108827881
```

The required checks include every 728-input column in both orientations,
all 2,950 phase edges, exact residual wrappers, 25 native controls, and the
89 applicable inherited cold-end controls. Dedicated controls cover the new
dimension-seven ends and their frame changes. The independent point audit
uses explicit subsets of the 512-point frame space. Owner checks cover all
36,288 roles, complete availability windows, distinct families per call,
capacity, and disjoint compact coordinate prefixes. Discovery is followed by
frozen strict admission, 69 admission controls, 12 bit-supplier controls,
seven independent owner controls, and both exact moment engines with all 47
outer inequalities. `data/EXPECTED.json` pins the resulting word, programs,
phase recipes, owner map, profile, and κ.

A complete cold run on Python 3.14.7 and macOS arm64 passed in 685 seconds.
`evidence/VALIDATION.json` records its environment, coverage, and input hashes.

`evidence/ASSEMBLY.json.gz` preserves the unchanged assembler's complete
output. Its historical descriptions and comparison labels refer to its
predecessors. The profile, moment endpoints, κ, and outer inequalities are
the computed results for this candidate.

`PROOF.md` explains the end frames, the packing certificate, and the complete
cost change. `SEARCH.json` records how the finite search found this candidate.
Search optimality is not needed to verify the construction.

This is a finite conditional witness for
`T(n) = O(n (log n)^(1-kappa))`. The inherited all-size compiler,
common-label and mutable-source realization, whole-call hosting, precision,
tape, exact-recovery, analytic-transfer, and bit H1–H5 assumptions remain.
The command reprices the pinned PR589 bit supplier; it does not repeat its
bit-circuit construction. Finite replay does not prove the full multiplication
theorem. The selected certificate is outside this contribution's scope.

The contribution is independent of PR784. See `NOTICE.md` for predecessor
credit, licensing, and the disclosure of AI assistance.
