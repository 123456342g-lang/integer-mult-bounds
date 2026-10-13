#!/usr/bin/env python3
"""Bounded nomination only; verify.py checks the resulting circuit separately.

Prepared for alluri-ritual with substantial OpenAI Codex assistance. Apache-2.0.
"""
import copy
from fractions import Fraction as Q
import json
from pathlib import Path
import random
from collections import Counter

N = 8


def identity():
    return [[Q(i == j) for j in range(N)] for i in range(N)]


def apply(a, e, positive=False):
    t = e[1]
    if e[0] == 'add':
        q = Q(e[3], e[4])
        q = abs(q) if positive else q
        a[t] = [u + q*v for u, v in zip(a[t], a[e[2]])]
    else:
        q = Q(e[2], e[3])
        q = abs(q) if positive else q
        a[t] = [q*u for u in a[t]]


def matrix(events, positive=False):
    a = identity()
    for e in events:
        apply(a, e, positive)
    return a


def inverse(events):
    result = []
    for e in reversed(events):
        e = copy.deepcopy(e)
        if e[0] == 'add':
            e[3] *= -1
        else:
            e[2], e[3] = e[3], e[2]
        result.append(e)
    return result


def power2(x):
    return x > 0 and x & (x-1) == 0


def allowed(events):
    for e in events:
        q = Q(e[3], e[4]) if e[0] == 'add' else Q(e[2], e[3])
        if not power2(q.denominator):
            return False
        if e[0] == 'scale' and not power2(abs(q.numerator)):
            return False
    return True


def eliminate(target, order, rng, frame):
    a, ops = copy.deepcopy(target), []

    def emit(e):
        apply(a, e)
        ops.append(e)

    left = set(range(N))
    for c in order:
        choices = [r for r in sorted(left) if a[r][c]
                   and power2(abs(a[r][c].numerator))
                   and power2(a[r][c].denominator)]
        if not choices:
            return None
        r = c if c in choices else rng.choice(choices)
        if r != c:
            emit(['add', c, r, 1, 1, frame])
            emit(['add', r, c, -1, 1, frame])
            emit(['add', c, r, 1, 1, frame])
            emit(['scale', r, -1, 1, frame])
        q = 1 / a[c][c]
        if q != 1:
            emit(['scale', c, q.numerator, q.denominator, frame])
        for r in range(N):
            if r != c and a[r][c]:
                q = -a[r][c]
                emit(['add', r, c, q.numerator, q.denominator, frame])
        left.remove(c)
    if a != identity():
        raise ValueError('Elimination did not reach identity')
    return inverse(ops)


def nominate(original, seed=33, trials=1024):
    rng = random.Random(seed)
    target, best, counts = matrix(original), original, Counter()
    original_positive = [matrix(original, True), matrix(inverse(original), True)]
    improvements = []
    for trial in range(trials):
        order = list(range(N))
        rng.shuffle(order)
        candidate = eliminate(target, order, rng, original[0][-1])
        if candidate is None:
            counts['no_binary_pivot'] += 1
            continue
        if not allowed(candidate):
            counts['non_dyadic'] += 1
            continue
        counts['admissible'] += 1
        if len(candidate) >= len(best):
            continue
        if matrix(candidate) != target:
            raise ValueError('Incorrect candidate')
        pairs = zip([matrix(candidate, True), matrix(inverse(candidate), True)],
                    original_positive)
        if all(x <= y for aa, bb in pairs for a, b in zip(aa, bb) for x, y in zip(a, b)):
            best = candidate
            counts['improvements'] += 1
            improvements.append({'trial_zero_based': trial, 'gates': len(best)})
    return best, dict(counts), improvements


if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    cert = json.loads((here / 'CIRCUIT.json').read_text())
    candidate, counts, improvements = nominate(cert['original'])
    if (candidate, counts, improvements) != (cert['replacement'], cert['search']['counts'],
                                           cert['search']['improvements']):
        raise ValueError('Frozen search did not reproduce')
    print('PASS_SEARCH_FACTORY5 trials=1024 gates=87->35')
