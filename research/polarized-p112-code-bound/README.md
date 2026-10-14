# Polarized P112 decoders within the retained coordinate codes

We prove that changing the directed decoder support cannot reduce the binary
pairing rank below nine while both factors retain their original coordinate
codes. We allow nonsymmetric rational decoders and nonsymmetric binary pairings.
This extends the fixed-mask question to a specified family of changed masks.
We supply no new supplier, paid cost improvement or multiplication exponent.

## Theorem and scope

Let R be the 112-by-8 rational matrix whose rows are `root_lines[8:]/2`, and
let U be the 112-by-9 binary matrix from `binary_ports[8:]` in the pinned
[prototype](../direct-delivery504-global/inputs/hamming/PROTOTYPE.json).
Use least-significant-bit coordinate numbering for U. For arbitrary matrices
C over Q and M over F2, define

```
N = R C R^T,        B = U M U^T.
```

Suppose N and B have unit diagonal, and every off-diagonal entry with B_ij=1
has N_ij=0. Then **rank_F2(B)=9**. Neither C nor M needs to be symmetric.

The conclusion excludes an eight-dimensional directed pairing in this family.
It concerns both row and column spaces: each must stay inside its corresponding
retained code. It does not cover outside-code source or receiver factors,
different port sets, different rational decoder spaces, arbitrary block-valued
deformations, or a changed native interface. It gives no lower bound on the
complete paid cost of a supplier at window nine.

The [format-limits C.6 interface](../format-limits/README.md#c6-asymmetric-pairing-uniqueness-at-the-e8-pattern-c6_asympy)
uses the same directed zero condition. Thiago Goulart's
[PR1744](https://github.com/CrocSwap/integer-mult-bounds/pull/1744) proves rank
nine for arbitrary fitting matrices on the original zero mask. Here N may
change that mask. We use and recheck PR1744's four-clique certificate only in
the cases that reduce to the original mask.

## Proof

### 1. Unit diagonal forces a skew perturbation

Write r_i for the unnormalized integer root rows, so R_i=r_i/2. For each row
form its eight square coordinates and 28 cross products. The resulting
112-by-36 matrix F satisfies

```
F^T F = diag(32 I_8 + 24 J_8, 24 I_28).
```

Its eigenvalues are 224, seven copies of 32, and 28 copies of 24. Thus the
diagonal measurements span all symmetric 8-by-8 matrices over Q. Since
R_i R_i^T=1, the condition N_ii=1 forces

```
C = I + A,        A^T = -A.
```

The checker reconstructs F and its full Gram matrix from the roots. In
particular, we do not assume the skew form as an extra restriction on C.

### 2. Classify the possible binary polar forms

Put L(u)=sum_i u_i. Each retained binary label has L(u)=1. Let H contain the
45 degree-one and square-free degree-two evaluations on the 112 labels.
Exact binary elimination gives rank(H)=36. Its nine-dimensional relation
space has the following basis: the eight independent relations

```
u_j (L(u)+1) = 0,       0 <= j < 8,
```

and

```
q(u) = sum_(i<j) u_i u_j + u_2+u_4+u_6+u_7+u_8 = 0.
```

For the first eight expressions, replace u_j squared by u_j. We verify both
the rank and all relation evaluations. Consequently every M satisfying
u_i^T M u_i=1 has, on the retained labels, the polar identity

```
B_ij + B_ji = lambda (1+B0_ij) + f_a(i)+f_a(j),
B0 = U U^T,        f_a(i)=a dot u_i,
```

for lambda in F2 and one representative a with its ninth coordinate zero.
There are 256 representatives. Adding the all-ones vector to a exchanges the
two cut classes and leaves the polar form unchanged. The formula follows by
polarizing the nine relations; the polar of q on odd labels is 1+u_i dot u_j.

### 3. Every nonconstant cut forces A=0

For a pair with r_i dot r_j=0, the retained Gram identity gives B0_ij=1.
If f_a(i) differs from f_a(j), the preceding formula gives B_ij+B_ji=1,
regardless of lambda. One of N_ij,N_ji must therefore vanish. Its symmetric
part already vanishes, so

```
r_i^T A r_j = 0.
```

For each of the 255 nonconstant representatives, the checker forms these
homogeneous equations in the 28 skew entries of A. Each coefficient matrix
has rank 28 modulo 101 and modulo 103. A nonzero minor modulo either prime
is a nonzero integer minor, so these are exact rational rank certificates.
We also select 28 original rows for each cut and compute their nonzero
determinants with separate fraction-free integer elimination.
Thus A=0 for every nonconstant cut.

The complete enumeration has 112 cuts of weight 52, 24 of weight 56,
112 of weight 60 and seven of weight 64. We enumerate this finite binary
parameter space; we do not sample rational A or infer a universal statement
from a failed rational search.

### 4. Handle the two constant-cut cases

If a=0 and lambda=0, then B is symmetric. If B_ij=1, both N_ij and N_ji
vanish, so their sum gives r_i dot r_j=0. Hence B fits the original mask.
The same conclusion holds when step 3 gives A=0, without requiring B to be
symmetric.

For completeness, PR1744's characteristic-two certificate uses four
eight-cliques of nonorthogonal root pairs whose odd-incidence set T is a
four-clique. An eight-clique already requires b>=8. Factor a fitting B of rank b as B_ij=x_i y_j and set
P_i=y_i x_i. These are rank-one idempotents; the idempotents on each clique
annihilate one another. For each eight-clique D, put E_D=I-sum_(i in D)P_i.
Then rank(E_D)=b-8. In characteristic two,

```
sum_D E_D = sum_(i in T) P_i,
4 <= 4(b-8),        b >= 9.
```

We reproduce the four clique lists from the pinned predecessor and verify
their pairs and incidences against the source. This step retains PR1744's
credit; it is not a new fixed-mask rank theorem.

It remains to exclude a=0, lambda=1. In that case B_ij+B_ji=1 whenever
r_i dot r_j is nonzero. One direction of each such pair must vanish in N,
which would require

```
(r_i^T A r_j)^2 = 4       whenever r_i dot r_j = +/-2.
```

### 5. Tetrad incidences exclude the remaining skew form

The roots contain all eight projective sign patterns on each of fourteen
four-coordinate supports. Fix a coordinate k and a support T containing it.
Take a sign vector u on T and flip coordinate k to form v. Then u dot v=2.
Skewness and the preceding squared identity give

```
(sum_(j in T, j != k) A_kj u_j)^2 = 1
```

for all eight choices of the other three signs. Comparing their independent
sign characters yields pairwise products A_ki A_kj=0 and the sum of squares
equal to one. Therefore exactly one of these three entries is nonzero, and
its value is +1 or -1.

Each coordinate belongs to seven supports; each coordinate pair belongs to
three. If d_k counts the nonzero entries in row k of A, counting the chosen
neighbors over these supports gives

```
3 d_k = 7,
```

which no integer d_k satisfies. The checker verifies the complete sign
patterns, both incidence counts, and the sign-character independence.
A single-tetrad positive control admits a skew form with the required
squared values, confirming the role of the global incidence condition.

We have reduced each possible polar class to the fixed-mask bound or a
contradiction. Finally rank(B)<=rank(U)=9, so rank(B)=9, as claimed.

## Reproduce and limits of verification

From the repository root:

```sh
python3.12 -I -O -B research/polarized-p112-code-bound/verify.py
python3.12 scripts/research_package.py --package research/polarized-p112-code-bound
```

The verifier uses the Python standard library and explicit exceptions, which
remain active under `-O`. It imports no search code or predecessor verifier.
It checks the source hash, root and binary quadratic ranks, complete relation
basis, all 255 cut systems over two primes and 255 exact integer minors, the tetrad and clique certificates,
two positive fixtures, and eight corruptions. It prints a deterministic JSON
receipt without rewriting files. A local modular rank certificate establishes
a rational nonzero minor; it is not a floating-point estimate.

The written proof supplies the universal reductions between those finite
facts. We have not formalized them in Lean, replayed the selected supplier,
or proved any improved multiplication theorem.

## Open next questions

A directed decoder could change at least one coordinate code. A first test
would construct explicit source and receiver factors outside U's column
space, verify the full zero condition and ranks, and price all centre and
side work before attempting global assembly. We have no such candidate.
Changing only matrix coefficients inside both retained codes cannot help.
[TASK.json](TASK.json) records this question and its acceptance boundary.

## Attribution and coordination

Jose Manuel (@jmbarrancoml) prepared this contribution with substantial
OpenAI Codex assistance in exploration, proof, exact checking and writing.
Read-only subagents derived the tetrad contradiction and checked source
geometry. We claim no independent human review. New work is Apache-2.0.

The unchanged root and binary-label input comes from icekylinx's
[direct-delivery504-global](../direct-delivery504-global/NOTICE.md), with the
PR523/514/507/425/433 ancestry retained there. We credit the format-limits
authors for the directed pairing interface. We credit Thiago Goulart (@Tuafo)
for PR1744's four-clique certificate and fixed-mask theorem, consumed at
`a9ae6278ee6196fb0e59c8220c48349cc8e05513`. Its later head
`78033981ec296b545b3cb50435668fe98e764e65` adds the selected P111 corollary;
our result and input remain P112. We neither copy nor modify predecessor
packages.

[Discussion1803](https://github.com/CrocSwap/integer-mult-bounds/discussions/1803)
records the scope. The source manifest pins base
`0b1cccf86e2f5132ed286a26ef0a681a495740ea`. The complete overlap refresh at
10:21–10:22 UTC on October14 covered 464 open PRs and 439 Discussion records.
That metadata search does not establish literature-wide novelty.
