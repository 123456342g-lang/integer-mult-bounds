# Clean invariant encodings of selector lanes

This is a changed state-space contract, not a replacement in the selected
supplier. The input may be arbitrary inside the encoded subspace, but its
complement must be zero. No native recipe, physical owner assignment, fixed-tape
implementation, or improved multiplication exponent is asserted.

The kernel convention is

\[
C=((1+i)I+(1-i)X)/2,\qquad C_d=C^{\otimes d},\qquad C_0=I.
\]

Fix integers \(n,s\geq1\), put \(q=2^s\), \(N=n+s\), and let
\(B=I_q\otimes C_n\). The active dimension is \(D=2^N\).
The optional phase convention is \(i^uC_d\), with \(u\in\{0,1,2,3\}\);
the fixed convention means \(u=0\).

## Exact existence and least ambient dimension

For \(d\geq0\) define the four nonnegative integer multiplicities

\[
m_d(j)=\sum_{\substack{0\leq k\leq d\\k\equiv j\pmod4}}\binom dk,
\qquad j\in\mathbb Z/4\mathbb Z.
\]

**Claim.** A full-column-rank complex matrix \(E\) of size \(2^d\times D\)
with

\[
i^uC_dE=EB
\]

exists exactly when

\[
m_d(j-u)\geq q\,m_n(j)\quad\text{for all }j\in\mathbb Z/4\mathbb Z.
\tag{1}
\]

The eigenspace-capacity method and Walsh encoder are already explicit in Douglas
R. Colkitt's [PR665 spectral split](https://github.com/CrocSwap/integer-mult-bounds/blob/d0e4f1eb295e5cce508dc76c6937290a9175e42b/research/clean-residual-dilation/README.md).
Their use here is credited specialization, not a new general encoding theorem.
The new object is a single tensor host for repeated equal-width lanes, with its
sharp least-width boundary and phase dependence.

The eigenspaces of \(C\) on the two Walsh vectors have eigenvalues \(1,i\).
Tensoring gives eigenvalue \(i^{|y|}\) on the Walsh vector indexed by
\(y\in\{0,1\}^d\), so its multiplicity is \(m_d(j)\).
The target multiplicity is \(q m_n(j)\). An injective intertwiner sends each
target eigenspace into the matching ambient eigenspace, proving necessity.
Conversely, (1) permits an injection of each target eigenbasis into the matching
ambient eigenbasis, proving sufficiency. Both operators are diagonalizable;
there is no additional Jordan-block condition.

For each fixed \(u\), the least legal \(d\) is exactly one of \(N+1,N+2\):
test (1) at \(d=N+1\), taking that value if it passes and \(N+2\) otherwise.
If any of the four phases is permitted, test all four at \(N+1\); the least
dimension is \(N+1\) if one passes, otherwise \(N+2\).

Here is the uniform proof. Dimension forces \(d\geq N\). At \(d=N\), an
injective \(E\) would be invertible and give a full-space similarity. But

\[
|\operatorname{tr}(i^u C_N)|=2^{N/2},\qquad
|\operatorname{tr}(B)|=2^{s+n/2}>2^{N/2}.
\]

Thus \(d=N\) is impossible for every phase. This full-space obstruction is
credited to Arham's active [Discussion #1901](https://github.com/CrocSwap/integer-mult-bounds/discussions/1901);
it is an inherited lower endpoint here, not a new claim of priority.

To prove existence at \(N+2\), each residue class of weights is contained in
one parity class, giving \(m_n(j)\leq2^{n-1}\). The roots-of-unity filter, for
\(d>0\), gives

\[
m_d(j)=2^{d-2}+2^{d/2-1}
\cos(d\pi/4-j\pi/2).
\]

Consequently, since \(N\geq2\),

\[
\min_j m_{N+2}(j)\geq2^N-2^{N/2}\geq2^{N-1}
\geq q\max_jm_n(j).
\]

This proves (1) simultaneously for all four phases. These real expressions are
only the written bound; exact finite certificates can use the integer binomial
sums or the recurrence \(m_{d+1}(j)=m_d(j)+m_d(j-1)\).

If an arbitrary scalar phase \(\lambda\) is proposed, the target has a nonzero
eigenspace of eigenvalue 1. Intertwining into \(\lambda C_d\) therefore forces
\(\lambda i^k=1\) for some integer \(k\). Thus the four phases above exhaust
all scalar phases that can satisfy the exact encoding equation.

## Explicit injective Walsh encoding and restoration

Let \(W_d[x,y]=(-1)^{x\cdot y}\) be the unnormalized Walsh matrix. Then
\(W_d^2=2^dI\) and \(C_dW_d=W_d\operatorname{diag}(i^{|y|})\).
Write \(W=I_q\otimes W_n\). Under (1), choose distinct labels
\(f(\ell,y)\in\{0,1\}^d\), one for each lane and data eigenlabel, such that

\[
|f(\ell,y)|\equiv |y|-u\pmod4.
\]

Choosing unused labels in increasing integer order makes this deterministic.
Let \(J_f\) inject the target standard basis into those ambient labels. The
exact dyadic-rational matrices

\[
E=2^{-n}W_dJ_fW,\qquad L=2^{-d}WJ_f^TW_d
\]

satisfy \(LE=I\) and \(i^uC_dE=EB\). No square-root coefficients are needed.
An isometric version also exists by using normalized Walsh matrices; its
implementation costs are not assumed free.

Extend the selected labels to a permutation of all ambient labels. This extends
\(E\) to an invertible encoder \(P\) whose inverse is an exact decoder, and

\[
P^{-1}(i^uC_d)P=B\oplus D_{\mathrm{comp}},
\]

where the complement block is diagonal with the remaining fourth-root phases.
Hence encoding \((x,0)\), applying the child, and decoding returns \((Bx,0)\)
for every complex input \(x\), including correlated lane values. The complement
is algebraically restored to zero. For arbitrary dirty complement \(z\), the
endpoint is instead \((Bx,D_{\mathrm{comp}}z)\); it generally does not restore
\(z\). This clean contract does not establish the predecessor's arbitrary-dirty
padding contract. An additional dirty restoration must be proved and charged if
that stronger contract is required.

## Sixteen-lane example and explicit volume charge

For \(n=1,s=4\), target multiplicities are \((16,16,0,0)\). The exact ambient
vectors at \(d=5,6,7\) are respectively

\[
(6,6,10,10),\quad(16,12,16,20),\quad(36,28,28,36).
\]

The fixed-phase least dimension is 7: dimensions 5 and 6 fail and dimension 7
passes. Its 128 ambient states are four times the 32 active states. If the
phase \(u=2\) is permitted, dimension 6 passes using ambient classes 2 and 3,
whose multiplicities are 16 and 20. This uses 64 ambient states, twice the active
dimension, and the global sign must be included in the complete implementation.

Let \(V\) be one original lane's volume, including spectator fibers. The
original \(q\) children have the inherited numerical budget
\(A V q n^\sigma\), where \(0<\sigma<1\). A child on the encoded ambient
array has volume \(2^{d-n}V\), so its budget alone is

\[
A V\,2^{d-n}d^\sigma,
\qquad
\frac{\text{ambient-child budget}}{\text{original budget}}
=2^{d-N}(d/n)^\sigma>2.
\]

This inequality holds for every allowable phase because \(d\geq N+1\).
It grants the encoder, decoder, clean-space preparation, routing, phase work,
coefficient storage, precision and restoration for free. Charging those
nonnegative costs cannot improve this particular comparison. The comparison is
between inherited upper-bound expressions, not a lower bound on actual runtime
or a prohibition of other recursion algorithms.

The dimensions here are literal tensor dimensions. If data width is scaled to
\(nf\) while the number of lanes remains \(2^s\), recompute the criterion with
\(nf\) in place of \(n\): the ambient dimension is \(nf+s+1\) or \(nf+s+2\).
The finite example \(C_7\) must not be relabeled \(C_{7f}\) while retaining its
constant fourfold volume. Scaling selector width as well changes the lane
count and must charge that volume explicitly.

The retained [selector-batching note](../selector-batching/README.md) supplies
the kernel convention, monomial support obstruction, arbitrary-dirty-padding
restoration and volume accounting. This result changes its hypothesis to a
clean invariant subspace and characterizes that algebraic contract exactly.
It supplies no new owner assignment, restored-work or precision theorem,
supplier admission, or improved \(\kappa\).
