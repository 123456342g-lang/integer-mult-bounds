# Sprint claim and handoff

Initial claim posted on the coordination board: [D#1163, comment 18911281](https://github.com/CrocSwap/integer-mult-bounds/discussions/1163#discussioncomment-18911281).

- **Track / seed:** complex supplier, OS seed 25.
- **Base:** `bce54fb3f895cbe5cd4c0eb477c3afeed100190f`.
- **Question:** exact temporal-gauge minima on PR1263 eligible helpers whose static exponent is zero.
- **Coverage:** all 19 helpers in both orientations; exact all-integer one-coordinate schedule DP; complete L359 invoice and endpoint replay.
- **Result:** L359 uniquely minimizes the scoped census, saving 242 real / 484 complex scalar primitives per invocation over PR1263 in each orientation. Every zero-static coordinate's best constant exponent has zero change. No new κ or combined multi-coordinate claim.
- **Reproduction:** `python3 -I -O -B research/k8-zero-static-temporal-seed25/verify.py`.

The result is complete and awaits a focused pull request link. This handoff does not claim supplier admission, whole-hosted improvement, or a formal multiplication proof.
