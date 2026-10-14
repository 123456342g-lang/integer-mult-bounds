# A commuting source code cannot log the complete query at this interface

The local source encoder in PR1862 is valid and its unchanged replay passes.
This note rules out one shortcut for carrying that code: keeping the same
operator across the individual source output frames. It does not rule out
changed charts, different encoders, paid transports or a complete supplier.
In particular, it is not a lower bound for every zero-native-cost circuit.

Let V=C^512 be the local nine-bit address space. At port i, write

    C_qi=((1+i)I+(1-i)X_qi)/2,
    S_i=F C_qi^-1,   F=product_{a=0}^8 C_(2^a).

The retained source output frame is S=diag(S_i). These are the frames in
PR1862's proof; they must not be replaced by a common full frame. Put
D=diag(C_qi). Its eight-by-112 R, 112-by-eight Z, and eight-port selector L
are those of the pinned PR1862 replay. Every row of Z is a nonzero scalar
multiple of the corresponding row of K=R^T/4: the multiplier is -12 on the
eight compensation ports and one elsewhere.

Allow B to be an arbitrary eight-by-112 matrix of complex linear operators
on V. Thus this includes address-valued coefficients, not just dyadic scalar
matrices. Consider G=I+ZB. The proposed complete logger condition is

    L G=R tensor I_V.

There is no such G commuting with D. There is also no such G commuting
with S. Invertibility of G is not needed for this obstruction.

## One Fourier output character suffices

In the binary Fourier basis indexed by x in F2^9, C_qi has eigenvalue
i^(qi dot x). Fix output character x=1. For either bit b=0 or b=1, the
rows of Z with qi dot x different from b have rank eight. The checker
gives explicit nonzero minors:

| Excluded eigenbit b | Eight port rows | Determinant of Z minor |
| --- | --- | --- |
| 0 | 0,1,2,3,4,5,6,12 | -3/512 |
| 1 | 25,26,27,28,29,30,31,44 | -3/1024 |

For fixed input port j and input character y, let b_j(x,y) in C^8 be the
corresponding coefficients of B. Commutation with D requires

    (i^(qi dot x)-i^(qj dot y)) Z_i b_j(x,y)=0

for every row i. The eigenbit qj dot y is either zero or one. Its excluded
rows have rank eight, forcing b_j(x,y)=0. This holds for every j and y.
Consequently G-I has no output at character x.

For S, its eigenvalue at output character x is i^(|x|-qi dot x), hence
either i or 1. The input eigenvalue of S_j is one of 1,i,-1,-i. If it is
1 or i, one of the same two full-rank row sets forces b_j(x,y)=0. For
either other phase, all rows are excluded; they have rank eight as well.
Again G-I has no output at character x.

Therefore L G equals L, rather than R, on that output character. This
contradicts the required logger identity: query row zero has coefficient
one at source port zero, while L is supported on the eight selected query
ports and has coefficient zero there. The checker records this coefficient
witness directly from the pinned replay.

## Tensor powers and scope

For any positive tensor power t, use output character (1,0,...,0). The
output eigenvalues of each tensor-powered C_qi or S_i still have just the
two phases used above. An arbitrary input character gives one of four
phases. The same two minors, or the entire rank-eight row set, again force
every coefficient b_j at that output character to vanish. The obstruction
therefore persists for arbitrary address-linear B on V^tensor t.

This concerns commutation with the unchanged output operator. A compiler
could instead change the code under a monomial conjugacy, carry it through
later compulsory native work, use a different response space, or pay for
transport. None of those possibilities is priced or excluded here. The
actual PR1862 local construction and its arbitrary-helper restoration are
not contradicted.

## Reproduce and credit

`python3 -I -O -B research/sourcecode-commutant/verify.py` reads the frozen
PR1042 archive directly and checks its compressed and decoded member hashes.
It reconstructs R by a separate exact scalar-prefix replay, checks the disjoint
coordinate minors and RZ=LZ=I, and matches canonical to physical line labels.
No PR1862 implementation, local Git database or network is required at runtime.
The rank and determinant computations use separate integer and rational
elimination methods. All 512 characters are inspected as supplementary evidence:
494 have rank eight in both groups, eight have ranks (7,8), eight have (8,7), and
the two constant characters have (0,8) and (8,0). The single explicit witness
already proves the statement. Four actual mutations reject a constant character,
a zeroed matrix row, a false determinant and a changed source archive.

PR1862 head 7649d9ceecec949541bec4bbde5929344166ba59 supplies the encoder,
fixed-support response space and pinned historical complex supplier.
Its sources and notices retain the PR1042/PR1094, gauge44, E8, frame and
native-checker lineage. This note adds the fixed-frame commutant obstruction;
it claims no independent human review, complete native supplier or kappa.

The next useful question is a paid or conjugated chart transition with an
explicit invoice. Requiring the original encoder to commute with the line
frames cannot supply that transition.
