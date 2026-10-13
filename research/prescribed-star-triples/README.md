# Exact deletion budgets for three prescribed graph-star targets

**Scoped structural decoder result; no new κ.** In the signed two-port
proper-star model, three specified targets can cost more than three freely
chosen targets. For p>=5 original coordinate pairs, we classify the exact
cost using the nonempty proper stars:

| Target pattern | Minimum deleted ports |
| --- | ---: |
| Triangle | Impossible |
| Three sides of the four-cycle on two complete original pairs | 6p-11 |
| Every other three-edge forest | 6p-12 |

For example, with five pairs, targets `{0,2}, {0,3}, {1,2}` need **19**
deletions, although the selectable-target minimum is **18**. Original
mates are `{0,1}, {2,3}, ...`. [PROOF.md](PROOF.md) gives a uniform proof,
explicitly separating information recovery from paid supplier costs.

This extends the prescribed-target criterion in Sam Sung's
[PR669](https://github.com/CrocSwap/integer-mult-bounds/pull/669), pinned at
`7d526020fc368ce4157cd436995c2f4fcf683318`. Its selectable-target hierarchy
and graph-code interpretation are credited predecessor results. The new
claim is the complete prescribed-triple classification in this graph
case, including the exceptional one-unit penalty.

## Reproduce

From the repository root, offline with Python 3.10+ and its standard library:

```sh
python3 -I -B research/prescribed-star-triples/verify.py
```

Expected first line:

```text
PASS_PRESCRIBED_STAR_TRIPLES: 44100 target triples; 37 orbits; 645606 partitions; budgets 18/19 and 24/25; triangles impossible; no new kappa
```

The checker compares the complete regenerated receipt to
[CERTIFICATE.json](CERTIFICATE.json), verifies the retained source hashes,
checks literal decoder identities on every surviving source column, and
rejects every one-edge restoration of every finite representative's
attaining deletion set. It also rejects singular target rows, corrupted
coefficient rows and deleted targets. A positive boundary control shows
why granting the excluded global-sum observation changes the result.
`--output /new/path.json` writes a verified receipt without overwriting an
existing file; `--certificate /path.json` checks an alternate receipt.
Checks remain active under `-O` and work outside the repository directory.

| Finite domain | All target triples | Symmetry orbits | Four-block partitions | Ordinary / exceptional / impossible triples |
| --- | ---: | ---: | ---: | ---: |
| p=5, 40 ports | 9,880 | 18 | 34,105 | 9,760 / 40 / 80 |
| p=6, 60 ports | 34,220 | 19 | 611,501 | 34,000 / 60 / 160 |

Orbits use sign flips and permutations of the original matched pairs.
Every partition is visited; a candidate that cannot improve an existing
minimum is safely skipped. There is no time limit or incomplete search in
these finite domains. Assignment seed 41 selected the structural track and
orders an illustrative ordinary witness; mathematical coverage is exhaustive.

An independent C++17 coefficient-label search and Python row-space checker
are supplied separately; see [VALIDATION.md](VALIDATION.md) for their command,
actual results and packaging controls. That search allows all eight binary
three-component coefficient labels and does not use the four-block reduction.

## Scope and provenance

Base: `91a2094f2e022930069e8cfdc810a3ea1b81cd09`. Exact context and predecessor
pins are in [SOURCES.json](SOURCES.json). No predecessor executable code is
imported. The two pinned predecessor proof texts are retained verbatim under
`reference/`; their relative links refer to the original PR669 package.
[NOTICE](NOTICE) retains attribution and AI-assistance disclosure.

The theorem assumes arbitrary independent surviving inputs and supplied
nonempty proper-star observations. Exact nonlinear postprocessing of those
same observations is covered. The empty star, changed observations,
higher-k ports and a complete physical implementation are outside scope.
The result supplies no cost-free preparation, source access, helper,
copy/restoration, frame, recursive-child or hosting interface. At the recorded
base, the selected construction was #799. Upstream subsequently selected #890;
see [VALIDATION.md](VALIDATION.md) for the pinned follow-up context. This package
changes neither construction and does not re-audit either multiplier.
