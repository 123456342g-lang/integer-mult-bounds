# Discovery record

These exploratory searches guided the choice of a provable local statement.
They do not certify the proposition. The submitted, standard-library checker
independently verifies its geometric premises, five-event order contradiction,
six-event example and paid controls. No solver is required to reproduce those
results. The exploratory search scripts are not part of this package.

## Assignment and domain

OS assignment seed: **23**, complex supplier. The recorded salt and three
candidate mechanisms are in `CLAIM.json`. SHA-256 ordering selected
cross-factory packet sharing, then pair `(6,7)`, sign `+1`, among 52 formed
pair/sign cases. The source pins identify the unmodified raw K492 constructor.

The discovery model had six read-only sources and six targets. Each target
needed the five sources outside its forbidden singleton. Sources started at
their rank-two leaver frames; targets started at zero, with rank-eight caps.
Every read propagated the frame join to **both** participants. Sources ended
at rank nine. Positive signal supports were disjoint when added: no signed
cancellation or repeated coefficient was allowed. Target dirt compensation
was deferred to a later exact replay if a candidate survived. Thus this was
an optimistic discovery model, not an admitted physical supplier.

## Heuristic runs

The random generator seed for both heuristics was the integer represented by
SHA-256 of `23|made, shell, arm, script, fix, tape|target-shared-decoder`:

```text
47441944177751120186235842501409826922933133093583107006176514245677426449285
```

- Beam searches stopped after the 30 delivered-coefficient layers, with at
  most six target-to-target additions. Width 600 expanded 13,220 states;
  width 900 with a necessary reachability filter expanded 15,804 states.
  Neither retained a completed circuit. State truncation makes both searches
  incomplete, including as searches for the already known direct circuit.
- A separate mutation run started from a legal direct 30-read schedule and
  attempted 18,000 seeded move/swap mutations. It accepted 3,493 legal moves
  and tested opportunities to replace later source reads by one available
  target sum. No shared candidate was found. The best complete local profile
  remained `48 H1 + 12 H2 + 6 H3`. This is neither an exhaustive neighborhood
  certificate nor a global cost claim.

## Bounded solver runs

Z3 5.1.0, random seed 23, checked a bit-vector encoding of the positive model.
At least one nonempty target-to-target read was required. For `n` sources,
there were at most `n(n-1)` active additions, with trailing no-ops permitted.
This bound covers positive disjoint-support additions in the no-helper model,
since each addition supplies at least one of the `n(n-1)` required entries.
The first shared edge and one shared signal were fixed by simultaneous
source/omitted-target relabeling.

| Sources | Frames enforced | Outcome | Recorded elapsed time |
| --- | --- | --- | --- |
| 3 | yes | UNSAT | 0.029 s |
| 4 | yes | UNSAT | 4.506 s |
| 5 | yes | unknown, 20 s timeout | 20.075 s |
| 6 | yes | unknown, 55 s timeout | 55.199 s |
| 6 | no | SAT | 0.234 s |

The small UNSAT results were diagnostic only; no independent solver proof
certificate is claimed. The missing-frame SAT run showed why source and
target frame propagation needed a separate test.

Two extensions allowed one helper with 28 additions or two helpers with 26.
Helpers could read sources and other helpers, while targets could also read
targets; helpers could not read targets. At least one helper had to combine
sources from different two-leaver factories. Helper cleanup and target dirt
compensation were omitted from these optimistic feasibility models. Both
Z3 runs returned unknown at 55 seconds. CVC5 1.4.2 independently parsed the
same exported formulas; both runs also returned unknown at 55 seconds.
These helper bounds do not cover all possible coded circuits.

No result about general multi-target coding, signed circuits or helper
optimality follows from these searches. The final proof instead fixes one
unordered target pair and allows arbitrarily many signed linear operations
and arbitrary read order. The two-helper control in the checker uses a
three-source projection and includes the compensation, cleanup and final
climbs absent from the discovery models.
