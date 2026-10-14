# P112 fitting rank is nine in every characteristic-two field

For the pinned 112-port graph, **every matrix with nonzero diagonal and zeros
on the required pairs has rank at least nine over every field of characteristic
two**, finite or infinite. Symmetry is not assumed. The existing binary labels
give the matching upper bound. Six eight-cliques on just 17 vertices certify the
lower bound. The same induced 17-vertex graph therefore has minimum rank nine.

This is a scoped obstruction to a rank-eight label replacement. It supplies no
new circuit, helper inventory, multiplication theorem or improved exponent.

## Exact object and graph convention

Use root_lines[8:] and binary_ports[8:] from
[PROTOTYPE.json](../direct-delivery504-global/inputs/hamming/PROTOTYPE.json).
The removed first eight roots are exactly twice the coordinate vectors. The
remaining roots are integer vectors in eight dimensions, of squared norm four;
their distinct-pair dot products are in {-2,0,2}.

Indices below are zero-based **after** removing the first eight rows. Put an
edge between distinct indices i and j exactly when their integer root dot
product is nonzero. These are the 2,912 unordered **required-zero** pairs.
A fitting matrix here has M_ii nonzero and M_ij = M_ji = 0 on each such pair;
all other off-diagonal entries are free.

Some Haemers-bound literature instead calls a matrix fitting when its zeros
are on graph nonedges. Our required-zero graph is the complement of the
corresponding induced E8 orthogonality graph. This convention matters.

The exact source commit is 0b1cccf86e2f5132ed286a26ef0a681a495740ea.
The input SHA256 is
327d2a868043e846381aa58a33053c24425e8cad522ff401b10ec8af1d649a3f.
[SOURCES.json](SOURCES.json) also pins the Git blob and historical catalogue and
selected record. Those provenance files are not changed by this package.

## Six-clique certificate

Each row is an eight-clique in the required-zero graph:

~~~text
C1 = 0, 8, 9, 24, 32, 56, 64, 88
C2 = 0, 8, 16, 24, 32, 40, 56, 57
C3 = 1, 8, 9, 24, 33, 56, 65, 88
C4 = 1, 8, 17, 24, 25, 56, 65, 72
C5 = 1, 8, 17, 24, 33, 40, 56, 57
C6 = 0, 8, 16, 24, 25, 56, 64, 72
~~~

Their union has 17 vertices and 106 induced required-zero pairs. In the six
rows, exactly vertices 0 and 1 occur an odd number of times. They are adjacent.
These elementary integer facts are all the finite input needed for the lower
bound.

## Proof for arbitrary fitting matrices

Let F be any field of characteristic two and M any fitting matrix. Multiplying
each row by the inverse of its diagonal entry preserves rank and required
zeros, so assume M_ii = 1. Every eight-clique gives an identity principal
submatrix, hence rank(M) is at least eight.

Suppose rank(M) = 8 and factor M = U V^T, where U and V have eight columns.
Write their i-th rows as u_i and v_i. For each displayed clique C,

~~~text
U_C V_C^T = I_8, so V_C^T U_C = I_8.
~~~

Thus the rank-one matrices P_i = v_i^T u_i sum to I_8 on each clique.
Sum all six equations. Characteristic two cancels their right sides and every
even-incidence P_i, leaving P_0 = P_1. Multiplication on the left by u_0 and
on the right by v_0^T gives

~~~text
1 = (u_0 v_0^T)^2 = u_0 P_0 v_0^T
  = u_0 P_1 v_0^T = (u_0 v_1^T)(u_1 v_0^T) = M_01 M_10 = 0.
~~~

This contradiction proves rank(M) at least nine without assuming symmetry,
a Gram representation or a finite field. The argument uses only the displayed
17 vertices.

For the upper bound, decode each retained binary label as a vector b_i in
F_2^9. The checker verifies odd self-dot product and zero dot product on every
required pair, as well as the complete Gram identity

~~~text
b_i . b_j = 1 + (root_i . root_j)/2  (mod 2).
~~~

Consequently their binary Gram matrix is a fitting matrix of rank at most
nine over every characteristic-two field. The checker also computes rank nine
for that matrix and verifies that the 17 retained labels span nine dimensions.
Together with the lower bound this proves the claimed equality for both graphs.

## Block-rank corollary and its limit

For d-by-d blocks, suppose M_ii = I_d and M_ij = M_ji = 0 on all required
pairs. Write r = rank(M) and factor its blocks as M_ij = U_i V_j, with U_i of
size d by r and V_i of size r by d. Each P_i = V_i U_i is a rank-d idempotent.
On an eight-clique the P_i are pairwise mutually annihilating, so their sum
S_C is an idempotent of rank 8d. Therefore E_C = I_r - S_C has rank r - 8d.

The same six-clique cancellation gives P_0 + P_1 = sum_C E_C. Since P_0 and
P_1 are mutually annihilating rank-d idempotents, their sum has rank 2d.
Rank subadditivity gives

~~~text
2d <= 6(r - 8d), hence r >= ceil(25d/3).
~~~

Invertible diagonal blocks can be normalized first. This is a human proof of
a normalized block-rank lower bound of 25/3; it does **not** prove a fractional
minimum of nine or rule out every block-valued interface. The finite checker
verifies the common clique certificate, not a formalization of the rank lemmas.

## Reproduce and coverage

From the repository root, with Python 3.12 and no external dependencies:

~~~sh
python3.12 scripts/research_package.py --package research/p112-characteristic-two-minrank --check-only
python3.12 scripts/research_package.py --package research/p112-characteristic-two-minrank
~~~

The registered replay runs verify.py with -I -B -O. Every acceptance check
uses an explicit exception and remains active with assertions disabled. The
script rewrites the deterministic [VERIFIED.json](VERIFIED.json) receipt.

The independently written verifier imports no search program or producer.
It checks the exact input hash, source indexing, every clique edge and incidence,
the scalar sandwich reduction, all 2,912 required-zero pairs, all 12,544 binary
Gram entries, and the rank-nine upper construction. Seven negative controls
alter source bytes, a clique vertex, the clique count, the edge convention,
an upper label's diagonal, an upper label while preserving odd norm, and the
label dimension. All seven must be rejected.

The universal field statements follow from the proof above; a finite solver
search is neither needed nor used in this replay. No full supplier or selected
frontier replay is claimed. This is not a Lean formalization.

## Overlap, relevance and attribution

[Discussion 1713](https://github.com/CrocSwap/integer-mult-bounds/discussions/1713)
records the finding and its strengthening from symmetric representations to
arbitrary fitting matrices. The complete remote overlap refresh on
2026-10-14 at 08:19 UTC covered 418 open PRs and 371 Discussions, including
comments and replies. Local overlap coverage was limited by this sparse
checkout. [PR1471](https://github.com/CrocSwap/integer-mult-bounds/pull/1471),
head 3695ad16e7bc4c0f6248a9e5a64fc069fa096733, audits the odd-characteristic
portability of a particular P112 tensor proof. The present theorem instead
bounds every fitting matrix in characteristic two. An overlap search does not
establish novelty, and no priority claim is made here.

The rank-nine upper construction is known: Debbie Leung, Laura Mancinska,
William Matthews, Maris Ozols and Aidan Roy,
[Entanglement can increase asymptotic rates of zero-error classical communication over classical channels](https://arxiv.org/abs/1009.1195),
Theorem 9 and section 4, explain the binary symplectic upper bound and the E8
embedding, crediting Peeters for the symplectic-graph result. We credit that
literature rather than treating the inherited labels as a new construction.
The contribution here is the explicit six-clique lower certificate, its
source binding and the independently replayable checks; no literature-wide
novelty claim for the underlying rank obstruction is asserted.

The concrete input is retained from icekylinx's
[direct-delivery504-global](../direct-delivery504-global/README.md) package,
prepared with OpenAI GPT-6 Astra assistance. Its Hamming/root inputs descend
from the PR523/514/507/425/433 lineage credited in that package's
[NOTICE.md](../direct-delivery504-global/NOTICE.md) and source ancestry. This
package references the existing input without modifying or re-vendoring it.

Prepared for Thiago with substantial OpenAI GPT-6 Astra and Codex assistance
for exploration, proof review, independent checking and packaging. New work
is Apache-2.0; retained source attribution and licenses remain applicable.

## Open next questions

Can a changed graph or a genuinely block-valued interface improve a complete
paid supplier budget? The fixed scalar rank-eight premise is closed, but the
block corollary leaves a gap between 25/3 and nine. A useful first step is to
write the changed constraints and an optimistic complete paid budget before
building a circuit. The missing native word, restoration/phase proof and
global owner invoice are the current blockers. [TASK.json](TASK.json) records
this question and explicitly labels this package as a side result of the
helper-inventory investigation.
