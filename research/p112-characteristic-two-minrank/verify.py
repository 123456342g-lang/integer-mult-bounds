"""Prepared for Thiago with OpenAI GPT-6 Astra and Codex assistance. Apache-2.0.

Independent exact audit of the pinned P112 characteristic-two certificate.

Only the Python standard library is used.  This module imports no producer,
search code, or other verifier.  The source supplies integer roots and binary
upper-bound labels; the six displayed clique lists are certificate data.

Proof over ANY field K of characteristic two: row-normalize a fitting matrix
to M_ii=1.  An eight-clique gives rank(M)>=8.  If rank(M)=8, factor M=U V^T.
For every eight-clique C, U_C V_C^T=I_8, hence V_C^T U_C=I_8.  Thus the
outer products P_i=v_i^T u_i sum to I_8 on C, without assuming symmetry.
The six clique equations have even right-hand side and odd incidence only
at 0 and 1.  Consequently P_0=P_1.  Sandwiching with u_0 and v_0^T gives
1=M_00^2=M_01 M_10=0.  The checker independently verifies that final scalar
polynomial reduction.  The nine binary labels embed in every such field.
This proves minrank nine for the specified constraints, not a new exponent.
"""
from collections import Counter
from copy import deepcopy
import hashlib
from itertools import combinations
import json
from pathlib import Path

PIN='327d2a868043e846381aa58a33053c24425e8cad522ff401b10ec8af1d649a3f'
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[1]/'research/direct-delivery504-global/inputs/hamming/PROTOTYPE.json'
BLOCKS=[
    [0,8,9,24,32,56,64,88], [0,8,16,24,32,40,56,57],
    [1,8,9,24,33,56,65,88], [1,8,17,24,25,56,65,72],
    [1,8,17,24,33,40,56,57], [0,8,16,24,25,56,64,72],
]


def require(condition,message):
    if not condition:
        raise ValueError(message)


def pinned(raw):
    require(hashlib.sha256(raw).hexdigest()==PIN,'source SHA-256 mismatch')
    return json.loads(raw)


def graph(roots):
    require(len(roots)==112,'P112 vertex count')
    require(all(len(r)==8 and all(type(x) is int for x in r) and sum(x*x for x in r)==4
                for r in roots),'eight integer coordinates and squared norm four')
    edges=set()
    for i,j in combinations(range(112),2):
        dot=sum(roots[i][k]*roots[j][k] for k in range(8))
        require(dot in (-2,0,2),'distinct root lines with normalized Gram in {-1,0,1}')
        if dot:
            edges.add((i,j))
    return edges


def lower(edges,blocks):
    require(len(blocks)==6,'six clique equations')
    for block in blocks:
        require(len(block)==8 and len(set(block))==8,'eight distinct clique vertices')
        require(all(tuple(sorted((i,j))) in edges for i,j in combinations(block,2)),
                'clique requires zeros on BOTH directed off-diagonal matrix entries')
    counts=Counter(v for block in blocks for v in block)
    require(sorted(v for v,c in counts.items() if c%2)==[0,1],'odd incidence is precisely 0 and 1')
    require((0,1) in edges,'the residual two vertices require off-diagonal zeros')
    # Sandwich sum_C sum_i(v_i^T u_i)=6I by u_0 and v_0^T.
    # Each surviving term is M_0i*M_i0, with distinct ordered symbols.
    polynomial=Counter({():len(blocks)%2})
    for i,count in counts.items():
        if count%2:
            if i==0:
                polynomial[()]+=1                 # M_00*M_00 = 1
            elif tuple(sorted((0,i))) not in edges:
                polynomial[((0,i),(i,0))]+=1       # no symmetry assumed
    residual={monomial:c%2 for monomial,c in polynomial.items() if c%2}
    require(residual=={():1},'the derived scalar equation must reduce to 1=0')
    return counts


def binary_basis(rows):
    pivots={};indices=[]
    for index,row in enumerate(rows):
        x=row
        while x:
            p=x.bit_length()-1
            if p in pivots:
                x^=pivots[p]
            else:
                pivots[p]=x;indices.append(index);break
    return indices


def upper(roots,labels,edges):
    require(len(labels)==112 and all(type(x) is int and 0<x<512 for x in labels),'nine binary coordinates')
    require(all(x.bit_count()%2==1 for x in labels),'nonzero diagonal in the binary Gram matrix')
    require(all((labels[i]&labels[j]).bit_count()%2==0 for i,j in edges),'all required directed zeros')
    require(all((labels[i]&labels[j]).bit_count()%2 ==
                (1+sum(a*b for a,b in zip(roots[i],roots[j]))//2)%2
                for i in range(112) for j in range(112)),
            'the complete normalized integer-Gram identity holds, including nonedges')
    basis=binary_basis(labels)
    require(len(basis)==9,'the known labels span nine dimensions')
    require(len(binary_basis([sum(((labels[i]&labels[j]).bit_count()%2)<<j
                                 for j in range(112)) for i in range(112)]))==9,
            'the explicit fitting matrix itself has rank nine')
    return basis


def reject(name,fn):
    try:
        fn()
    except ValueError as exc:
        return dict(control=name,outcome='REJECTED',reason=str(exc))
    raise ValueError('corruption was accepted: '+name)


def main():
    raw=SOURCE.read_bytes();source=pinned(raw)
    require(source['root_lines'][:8]==[[2*int(i==j) for j in range(8)] for i in range(8)],
            'source offset eight removes exactly the coordinate root lines')
    roots=source['root_lines'][8:];labels=source['binary_ports'][8:]
    edges=graph(roots);counts=lower(edges,BLOCKS);basis=upper(roots,labels,edges)
    vertices=sorted(counts)
    restricted_basis=[vertices[i] for i in binary_basis([labels[i] for i in vertices])]
    require(len(vertices)==17 and len(restricted_basis)==9,'the induced 17-vertex graph already has rank nine')
    controls=[reject('source byte changed',lambda:pinned(raw+b' '))]
    bad=deepcopy(BLOCKS);bad[0][0]=1
    controls.append(reject('clique vertex changed',lambda:lower(edges,bad)))
    controls.append(reject('one clique omitted',lambda:lower(edges,BLOCKS[:-1])))
    inverted=set(combinations(range(112),2))-edges
    controls.append(reject('edge convention reversed',lambda:lower(inverted,BLOCKS)))
    bad_labels=labels[:];bad_labels[0]^=1
    controls.append(reject('upper diagonal corrupted',lambda:upper(roots,bad_labels,edges)))
    bad_labels=labels[:];bad_labels[0]^=3
    controls.append(reject('upper label changed with odd norm preserved',lambda:upper(roots,bad_labels,edges)))
    controls.append(reject('upper labels truncated to eight coordinates',
                           lambda:upper(roots,[x&255 for x in labels],edges)))
    result=dict(status='PASS_INDEPENDENT_GENERAL_CHAR2_MINIMUM_FITTING_RANK_NINE',
                source_sha256=PIN,source_vertex_offset=8,vertices=112,
                required_zero_unordered_edges=len(edges),symmetric_matrix_assumed=False,
                diagonal_normalization='left multiply by diag(M_ii^-1); preserves rank and every required zero',
                factor_orientation='M_ij=u_i*v_j^T; P_i=v_i^T*u_i; U_C*V_C^T=I implies V_C^T*U_C=I',
                certificate_vertices=vertices,cliques=BLOCKS,
                incidence_counts=dict(sorted(counts.items())),residual_vertices=[0,1],
                induced_required_zero_edges=sum(i in counts and j in counts for i,j in edges),
                symbolic_sandwich_residual='1=0',upper_dimension=9,
                upper_basis_vertex_indices=basis,induced_upper_basis_vertex_indices=restricted_basis,
                field_scope='Every field of characteristic two, finite or infinite; no symmetry assumption.',
                corruption_controls=controls,
                scope='Exact finite certificate and elementary field-independent proof; no novelty, native circuit, or exponent claim.')
    out=HERE/'VERIFIED.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
