"""Exact finite premises for the polarized P112 code bound. Apache-2.0.

Jose Manuel, with substantial OpenAI Codex assistance. The universal argument
is in README.md. No producer, solver, or predecessor verifier is imported.
"""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "research/direct-delivery504-global/inputs/hamming/PROTOTYPE.json"
PIN = "327d2a868043e846381aa58a33053c24425e8cad522ff401b10ec8af1d649a3f"
PAIRS8 = list(combinations(range(8), 2))
PAIRS9 = list(combinations(range(9), 2))
# Thiago Goulart's PR1744, pinned head a9ae6278ee6196fb0e59c8220c48349cc8e05513.
CLIQUES = [
    [2, 16, 57, 70, 78, 84, 100, 102],
    [10, 16, 57, 70, 78, 84, 108, 110],
    [2, 10, 16, 32, 34, 57, 70, 84],
    [16, 32, 57, 68, 70, 84, 100, 108],
]
QUADRIC = (((1 << 36) - 1) << 9) | sum(1 << i for i in (2, 4, 6, 7, 8))


def need(condition, message):
    if not condition:
        raise ValueError(message)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def canonical(row):
    row = tuple(row)
    return max(row, tuple(-x for x in row))


def binary_rank(rows):
    pivots = {}
    for value in rows:
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def modular_basis(rows, width, prime):
    # Incremental row echelon form, with explicit insertion-order pivots.
    pivots = []
    selected = []
    for original in rows:
        row = [x % prime for x in original]
        for pivot, basis in pivots:
            if row[pivot]:
                scale = row[pivot]
                row = [(x - scale * y) % prime for x, y in zip(row, basis)]
        pivot = next((i for i, value in enumerate(row) if value), None)
        if pivot is None:
            continue
        inverse = pow(row[pivot], -1, prime)
        pivots.append((pivot, [inverse * value % prime for value in row]))
        selected.append(list(original))
        if len(pivots) == width:
            break
    return selected


def modular_rank(rows, width, prime):
    return len(modular_basis(rows, width, prime))


def integer_determinant(rows):
    """Independent fraction-free determinant with integer row pivots."""
    matrix = [row[:] for row in rows]
    n = len(matrix)
    need(all(len(row) == n for row in matrix), "square integer minor")
    previous, sign = 1, 1
    for k in range(n - 1):
        pivot_row = next((i for i in range(k, n) if matrix[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            matrix[k], matrix[pivot_row] = matrix[pivot_row], matrix[k]
            sign = -sign
        pivot = matrix[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = matrix[i][j] * pivot - matrix[i][k] * matrix[k][j]
                need(numerator % previous == 0, "exact fraction-free division")
                matrix[i][j] = numerator // previous
            matrix[i][k] = 0
        previous = pivot
    return sign * matrix[-1][-1]


def check_roots(roots):
    need(len(roots) == 112, "112 roots")
    need(all(len(row) == 8 and all(type(x) is int for x in row) for row in roots),
         "integer eight-coordinate roots")
    need(len({canonical(row) for row in roots}) == 112, "distinct projective roots")
    groups = defaultdict(set)
    for row in roots:
        support = tuple(i for i, x in enumerate(row) if x)
        need(len(support) == 4 and all(abs(row[i]) == 1 for i in support), "signed tetrads")
        groups[support].add(canonical(tuple(row[i] for i in support)))
    signs = {canonical(row) for row in product((-1, 1), repeat=4)}
    need(len(groups) == 14 and all(rows == signs for rows in groups.values()),
         "fourteen complete sign tetrads")
    need(all(sum(i in t for t in groups) == 7 for i in range(8)), "seven tetrads per coordinate")
    need(all(sum(i in t and j in t for t in groups) == 3 for i, j in PAIRS8),
         "three tetrads per coordinate pair")
    need(all(dot(a, b) in (-2, 0, 2) for a, b in combinations(roots, 2)), "root inner products")
    return groups


def check_root_quadratics(roots):
    features = [[x * x for x in row] + [row[i] * row[j] for i, j in PAIRS8] for row in roots]
    gram = [[sum(row[i] * row[j] for row in features) for j in range(36)] for i in range(36)]
    expected = [[(32 * (i == j) + 24 if i < 8 and j < 8
                  else 24 * (i == j) if i >= 8 and j >= 8 else 0)
                 for j in range(36)] for i in range(36)]
    need(gram == expected, "rational quadratic Gram identity")
    # Its eigenvalues are 224, seven copies of 32, and 28 copies of 24.
    need(modular_rank(features, 36, 101) == 36, "rational quadratic rank 36")


def check_labels(roots, labels):
    need(len(labels) == 112 and all(type(x) is int and 0 < x < 512 for x in labels),
         "nine-coordinate binary labels")
    need(binary_rank(labels) == 9, "binary label span nine")
    need(all(x.bit_count() % 2 for x in labels), "odd binary labels")
    gram = []
    for i, u in enumerate(labels):
        row = 0
        for j, v in enumerate(labels):
            value = (u & v).bit_count() % 2
            need(value == (1 + dot(roots[i], roots[j]) // 2) % 2, "full binary Gram identity")
            row |= value << j
        gram.append(row)
    need(binary_rank(gram) == 9, "rank-nine positive fixture")
    return gram


def check_cliques(roots, cliques):
    for clique in cliques:
        need(len(set(clique)) == 8 and all(0 <= x < 112 for x in clique), "eight distinct clique vertices")
        need(all(dot(roots[i], roots[j]) != 0 for i, j in combinations(clique, 2)),
             "predecessor required-zero clique")
    counts = Counter(i for clique in cliques for i in clique)
    odd = sorted(i for i, count in counts.items() if count % 2)
    need(odd == [34, 68, 102, 110], "predecessor odd-incidence set")
    need(all(dot(roots[i], roots[j]) != 0 for i, j in combinations(odd, 2)),
         "predecessor odd-incidence four-clique")


def binary_features(labels):
    return [u | sum((((u >> i) & (u >> j) & 1) << (9 + k))
                    for k, (i, j) in enumerate(PAIRS9)) for u in labels]


def check_binary_quadratics(labels, quadric=QUADRIC):
    features = binary_features(labels)
    stars = [sum(1 << (9 + k) for k, (i, j) in enumerate(PAIRS9) if a in (i, j))
             for a in range(8)]
    relations = stars + [quadric]
    need(binary_rank(features) == 36, "binary quadratic feature rank 36")
    need(binary_rank(relations) == 9, "nine independent quadratic relations")
    need(all((row & relation).bit_count() % 2 == 0 for row in features for relation in relations),
         "quadratic relations vanish on all ports")
    need(quadric >> 9 == (1 << 36) - 1, "canonical quadric polar")
    # The polar is (sum u)(sum v)+u dot v = 1+B0 on the odd affine hyperplane.
    need(all(sum((((u >> i) & 1) * ((v >> j) & 1))
                 ^ (((u >> j) & 1) * ((v >> i) & 1)) for i, j in PAIRS9) % 2
             == 1 ^ ((u & v).bit_count() % 2) for u in labels for v in labels),
         "quadric polar equals one plus B0")


def check_cuts(roots, labels):
    zero_pairs = [(i, j, [roots[i][a] * roots[j][b] - roots[i][b] * roots[j][a] for a, b in PAIRS8])
                  for i, j in combinations(range(112), 2) if dot(roots[i], roots[j]) == 0]
    need(len(zero_pairs) == 3304, "orthogonal root-pair count")
    classes, determinants = Counter(), []
    for functional in range(1, 256):
        cut = [(functional & u).bit_count() % 2 for u in labels]
        rows = [wedge for i, j, wedge in zero_pairs if cut[i] != cut[j]]
        for prime in (101, 103):
            need(modular_rank(rows, 28, prime) == 28,
                 f"full skew-constraint rank for cut {functional}, prime {prime}")
        minor = modular_basis(rows, 28, 101)
        determinant = integer_determinant(minor)
        need(determinant != 0, f"nonzero integer skew minor for cut {functional}")
        determinants.append(determinant)
        classes[sum(cut)] += 1
    need(classes == {52: 112, 56: 24, 60: 112, 64: 7}, "complete nonconstant cut classes")
    need(integer_determinant([[0, 1], [1, 0]]) == -1, "signed determinant control")
    need(integer_determinant([[1, 2], [2, 4]]) == 0, "singular determinant control")
    digest = sha256(json.dumps(determinants, separators=(",", ":")).encode()).hexdigest()
    return dict(sorted(classes.items())), digest


def check_sign_character_identity():
    signs = list(product((-1, 1), repeat=3))
    characters = [(0, 0), (0, 1), (0, 2), (1, 2)]
    values = [[1] + [s[i] * s[j] for i, j in characters[1:]] for s in signs]
    need([[sum(row[i] * row[j] for row in values) for j in range(4)] for i in range(4)]
         == [[8 * (i == j) for j in range(4)] for i in range(4)], "independent sign characters")
    need(all(3 * degree != 7 for degree in range(8)), "integer tetrad-incidence contradiction")


def small_positive_control():
    # One tetrad lacks the 7-versus-3 incidence obstruction.
    roots = sorted({canonical(row) for row in product((-1, 1), repeat=4)})
    matrix = [[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]]
    checked = 0
    for u, v in combinations(roots, 2):
        if abs(dot(u, v)) == 2:
            value = sum(u[i] * matrix[i][j] * v[j] for i in range(4) for j in range(4))
            need(value * value == 4, "single-tetrad positive skew control")
            checked += 1
    need(checked == 16, "positive skew control pair count")
    return checked


def rejected(name, fn):
    try:
        fn()
    except ValueError as error:
        return {"control": name, "outcome": "REJECTED", "reason": str(error)}
    raise ValueError("corruption accepted: " + name)


def check_pin(raw):
    need(sha256(raw).hexdigest() == PIN, "prototype SHA256")


def main():
    raw = SOURCE.read_bytes()
    check_pin(raw)
    data = json.loads(raw)
    roots, labels = data["root_lines"][8:], data["binary_ports"][8:]
    check_roots(roots)
    check_root_quadratics(roots)
    gram = check_labels(roots, labels)
    check_cliques(roots, CLIQUES)
    check_binary_quadratics(labels)
    classes, minor_digest = check_cuts(roots, labels)
    check_sign_character_identity()
    positive = small_positive_control()
    need(all(not ((gram[i] >> j) & 1) or dot(roots[i], roots[j]) == 0
             for i, j in combinations(range(112), 2)), "N0,B0 positive fitting fixture")

    bad_roots = [row[:] for row in roots]
    bad_roots[0][0] += 1
    duplicate = roots[:]
    duplicate[1] = roots[0]
    bad_labels = labels[:]
    bad_labels[0] ^= 1
    bad_cliques = [row[:] for row in CLIQUES]
    bad_cliques[0][0] = bad_cliques[0][1]
    controls = [
        rejected("source bytes altered", lambda: check_pin(raw + b" ")),
        rejected("root coordinate altered", lambda: check_roots(bad_roots)),
        rejected("projective sign pattern duplicated", lambda: check_roots(duplicate)),
        rejected("one root omitted", lambda: check_roots(roots[:-1])),
        rejected("binary label altered", lambda: check_labels(roots, bad_labels)),
        rejected("binary labels truncated", lambda: check_labels(roots, [x & 255 for x in labels])),
        rejected("extra quadric coefficient altered", lambda: check_binary_quadratics(labels, QUADRIC ^ 1)),
        rejected("predecessor clique corrupted", lambda: check_cliques(roots, bad_cliques)),
    ]
    print(json.dumps({
        "status": "PASS_POLARIZED_P112_CODE_BOUND",
        "prototype_sha256": PIN,
        "ports": 112,
        "rational_quadratic_rank": 36,
        "binary_quadratic_rank": 36,
        "binary_quadratic_relations": 9,
        "binary_quadric_mask": QUADRIC,
        "nonconstant_cuts": 255,
        "cut_weight_classes": classes,
        "skew_constraint_ranks": {"101": 28, "103": 28},
        "nonzero_integer_minors": 255,
        "integer_minor_determinants_sha256": minor_digest,
        "orthogonal_pairs": 3304,
        "nonorthogonal_pairs": 2912,
        "tetrads": 14,
        "tetrads_per_coordinate": 7,
        "tetrads_per_coordinate_pair": 3,
        "single_tetrad_positive_pairs": positive,
        "controls": controls,
        "scope": "Written theorem for N=R C R^T over Q and B=U M U^T over F2; no new supplier or exponent.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
