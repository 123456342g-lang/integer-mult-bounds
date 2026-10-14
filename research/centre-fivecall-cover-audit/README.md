# An independent audit of the five-call center pilot's cover obstruction

**Corroboration of [discussion 1636](https://github.com/CrocSwap/integer-mult-bounds/discussions/1636), no new κ.** The discussion gives an exact five-call local shear identity and then reports that inherited fresh-window cover routing prevents it from being a supplier. This package independently proves the route's same-port condition, reconstructs the 112 sign-line Gram identity and checks the stated rational matrices. It is conditional on the discussion's five-call coefficients and proposed four-stage route; no candidate implementation or global controller package was available in the offline source tree.

## The inherited route condition

The retained [complex geometry proof](../split-centres-global/proofs/INHERITED-COMPLEX-GEOMETRY.txt) defines a local 9-space and a fresh 8-space `E_s`. Every port `q` has odd weight and a zero coordinate. Its orthogonal `U_q` maps `e_0` to `q`, and columns 1–8 span `q^perp`. The involution `rho_(s,q)` fixes `q`, exchanges `q^perp` with `E_s`, and fixes the other fresh spaces.

Consider a port transition `rho_(s,p) rho_(s,q)`. The first image of `E_s` is `q^perp`. The second map sends a local vector entirely back into `E_s` precisely when it lies in `p^perp`. Thus the product preserves `E_s` iff `q^perp` is contained in `p^perp`. Both are 8-dimensional hyperplanes, so they are equal; their nonzero normal lines over F₂ are equal, hence `p=q`. Conversely `p=q` gives the identity. Other stage factors fix `E_s` pointwise and preserve its complementary local-plus-other-stage space. They therefore cannot erase a nonzero component outside `E_s`. A product with one transition at each fresh stage can return to the original cover class only when every stage transition has the same port at both ends. This last statement depends on the one-transition-per-fresh-stage form stated in discussion 1636; it is not asserted for arbitrary routing words that revisit a stage.

The selected source manifest pins the archived 112-port `DATA-PHASES.json`. Our checker independently implements the swap-plus-even-transvection construction of `U_q`, proves its 9×9 orthogonality for each port, constructs `rho` on a 41-bit space with four fresh 8-spaces, checks every `rho` on all 41 basis vectors is involutive, and tests all `4·112² = 50,176` ordered stage/port pairs. Exactly 448 pairs (same port at each of four stages) preserve the fresh space; 49,728 do not. For example stage 1, `(p,q)=(11,19)` sends fresh basis vector 0 to a vector with nonzero local image 11.

## The five-call scalar failure

The retained [Hamming packet proof](../split-centres-global/proofs/PR425-COMPLEX.txt) describes 112 sign lines on 14 weight-four Hamming blocks. Independently construct each block as an affine plane in F₂³ and take its eight sign choices modulo overall sign. Each integer row has four ±1 entries, so its normalized row `r/2` has squared norm one. The exact 8×8 sum of outer products is `R^T R=14I`: each coordinate appears in seven blocks, and mixed signs cancel within each block. Hence `M=I−RR^T` has eigenvalues 1 and −13, and every diagonal entry `M_pp=0`. The checker reconstructs all 112 rows and tests every Gram entry. This depends on the stated Hamming sign-line geometry, not a byte-level recheck of PR370's historical table order.

For this `M` and `K = I − M`, the discussion's chronological word is

`L(M/12), U(−12M/13), L((143M+131K)/144), U(−12M/13), L(M/12)`.

With `L(t)=[[1,0],[t,1]]` and `U(t)=[[1,t],[0,1]]`, direct exact multiplication gives the desired exchange `[[0,−1],[1,0]]` at both eigenvalues. On a same-port/same-cover block `M_pp=0`, so the word reduces to `L(131/144)=[[1,0],[131/144,1]]`. It is not the exchange. This is a failure of that five-call candidate under the specified inherited routing, not a barrier for a different global geometry, a paid intertwiner, or another word.

There is a slightly broader necessary condition for any **single-pass fresh-stage word** in this same two-stream shear model. On its same-cover projection, every `L(cM+dK)` or `U(cM+dK)` becomes `L(d)` or `U(d)`. A pulse with `d=0` becomes the identity; call `d≠0` center-bearing. Zero or one such pulse cannot be the exchange. With two pulses of the same orientation both diagonal entries stay 1; with opposite orientations one diagonal entry stays 1. The exchange has both diagonal entries 0. Thus at least **three center-bearing shears** are necessary, whatever the number of center-free `M` pulses. The bound is sharp for this projected 2×2 problem: chronological `L(1), U(−1), L(1)` gives the exchange. The checker verifies the two-pulse statement symbolically over integer polynomials in two independent coefficients and the three-pulse rational witness. This counts pulses, not recursive rank mass: a proposed supplier must still price a physical realization. Multi-pair gates, revisiting fresh stages, or a changed global route are outside this lemma.

## Reproduce and limits

```sh
python3.12 -I -B research/centre-fivecall-cover-audit/verify.py
python3.12 scripts/research_package.py --package research/centre-fivecall-cover-audit
```

`verify.py` checks source hashes and the selected route manifest, 112 distinct admissible port labels, orthogonal `U_q`, four-stage involutions, all 50,176 products, the 112-row normalized Gram matrix, the rational shear word, the symbolic two-pulse obstruction and `RESULT.json`. Four controls reject a duplicate port, a corrupt `U_q` column, a changed middle coefficient and an off-spectrum substitution. The checker is standard-library only and does not import the historical route implementation. Its result is conditional on the discussion's unarchived five-call coefficients, one transition per fresh stage and the inherited route formula. It does not replay 704 local dirty columns, exact complex phases, helper hosting, coefficient precision or any supplier invoice. The selected frontier is unchanged.

## Open next questions

1. **Can a different global geometry implement this local identity?** A first step is an explicit stage route or paid intertwiner with exact cover-class and same-port blocks, followed by a full controller and invoice. The inherited `rho` route fails the necessary block above.
2. **Can the local pilot be bound to an on-disk candidate?** The discussion gives the rational word and reports a 704-column local replay, but no package/head was available in the offline cache. A first step is to pin such a package and recheck its coefficients and port routing before treating this audit as a candidate-specific review. Until then the conclusion is conditional on the stated model.

## Credit

The local identity and first obstruction are from discussion 1636; this is independent corroboration, not a priority claim. The route formula and source geometry come from the retained split-centers complex proof and the selected #1094 lineage. Prepared by Josie Elliston with substantial OpenAI Codex assistance. No independent human review. Apache-2.0.
