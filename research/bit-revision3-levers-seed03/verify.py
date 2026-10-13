#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Bit-side revision-3 levers: certified budgets for the selected PR589 bit supplier at a = 1/99.

Usage: python3 -I -B research/bit-revision3-levers-seed03/verify.py [--write]

1. Binds the selected record -> frontier1094 ASSEMBLY -> PR589 EXPECTED.json -> the bit word, and
   reproduces the selected bit endpoint (accepted, next 1e-24 grid point rejected, surcharge included)
   with code-disjoint exact arithmetic (levers.py).
2. Replays the bit word's frame itineraries: the local histogram, its class split (sources, targets,
   helpers, retained totals, rank-7 copies) and the coverage law  mass = (m-1)W + cst N, D = W - 63N.
3. Prices the revision-3 levers on the bit side in the coverage-law relaxation (fixed local word, all
   idle mass at the halving-guard cap R = 45, fractional counts, no surcharge: all favorable), with
   certified root brackets, multipliers and certified verdicts at a = 1/99.
4. Certifies the joint budget surface: the largest number of helpers (each one climb of rank equal to
   its width) that a per-call copy charge leaves room for at a = 1/99, as k passes / k+1 fails.
5. Complex cross-check: reproduces #1240's complex word ceiling and prices #1272's combined lever
   inside and beyond the complex stage window.
Expected last line: PASS_BIT_REVISION3_LEVERS
"""
import argparse
import gzip
import hashlib
import json
import sys
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from levers import Reject, dec, max_count, need, relaxed, root, verdict, bill  # noqa: E402

RECORDS = ('certificates/selected-result.json', 'certificates/checkpoints/frontier1094.json')
ASSEMBLY = 'research/community-frontier1094-audit/ASSEMBLY.json'
EXPECTED = 'research/e8-bit-p111-tuned/tune/EXPECTED.json'
GUARD = ('research/e8-bit-p111-tuned/vendor/pr510/e8-r480-nine-stage/vendor/e8-r715-eleven-stage-whole/code/global_k.py',
         'halving_integer_inequality=[M**HD,2*max(paid)**HD]')
TARGET = Q(1, 99)
M = 64


def sha(data):
    return hashlib.sha256(data).hexdigest()


def frac(s):
    return Q(s) if '/' in str(s) else Q(str(s))


def bind():
    asm_raw = (ROOT / ASSEMBLY).read_bytes()
    bound = None
    for record in RECORDS:
        p = ROOT / record
        rec = json.loads(p.read_text()) if p.is_file() else {}
        if rec.get('certificate') == ASSEMBLY and rec.get('certificate_sha256') == sha(asm_raw):
            bound = record
            break
    need(bound is not None, 'B1 a record binds the frontier1094 certificate')
    asm = json.loads(asm_raw)
    exp_raw = (ROOT / EXPECTED).read_bytes()
    need(asm['input_sha256']['package:inputs/PR589-EXPECTED.json'] == sha(exp_raw), 'B2 certificate pins the PR589 record')
    exp = json.loads(exp_raw)
    word_path = ROOT / 'research/e8-bit-p111-tuned' / exp['word']['file']
    word_raw = word_path.read_bytes()
    need(sha(word_raw) == exp['word']['file_sha256'] and sha(gzip.decompress(word_raw)) == exp['word']['content_sha256'],
         'B3 record pins the bit word')
    need(frac(asm['bit_lower']) == frac(exp['nine']['bit_lower']), 'B4 certificate bit endpoint equals the PR589 record')
    guard_text = (ROOT / GUARD[0]).read_text()
    need(GUARD[1] in guard_text and exp['nine']['bit']['halving_depth'] == 2, 'B5 halving guard M^2 > 2 maxchild^2')
    return dict(record=bound, assembly=ASSEMBLY, assembly_sha256=sha(asm_raw), expected=EXPECTED, expected_sha256=sha(exp_raw),
                word=str(word_path.relative_to(ROOT)), word_sha256=sha(word_raw)), asm, exp, json.loads(gzip.decompress(word_raw))


def line_rank(vectors):
    rows = [[Q(x) for x in v] for v in vectors]
    rank = 0
    for c in range(len(rows[0]) if rows else 0):
        piv = next((i for i in range(rank, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][c] != 0:
                f = rows[i][c] / rows[rank][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def replay(word, exp):
    """Frame itinerary of every register through D, A, B, C (start and final frames included)."""
    lines = word['lines']
    dims = [line_rank([lines[i] for i in f]) if f else 0 for f in word['frames']]
    v, R = word['v'], word['R']
    n = 2 * v + R
    path = {r: [word['start'][r]] for r in range(n)}
    for phase in ('D', 'A', 'B', 'C'):
        for gate in word[phase]:
            f, dst, srcs = gate[0], gate[1], gate[2]
            for r in [dst] + list(srcs):
                if path[r][-1] != f:
                    path[r].append(f)
    for r in range(n):
        if path[r][-1] != word['final'][r]:
            path[r].append(word['final'][r])
    retained = set(word['ret'])

    def cls(r):
        return 'sources' if r < v else 'targets' if r < 2 * v else 'totals' if r in retained else 'helpers'
    split = {k: Counter() for k in ('sources', 'targets', 'helpers', 'totals')}
    descents = 0
    for r in range(n):
        for a, b in zip(path[r], path[r][1:]):
            if dims[b] > dims[a]:
                split[cls(r)][dims[b] - dims[a]] += 1
            elif dims[b] < dims[a]:
                descents += 1
    copies = Counter(exp['word']['copy_ranks'])
    local = sum(split.values(), Counter()) + copies
    need(descents == 0, 'R1 every frame change is a climb')
    need({str(k): c for k, c in sorted(local.items())} == exp['word']['local_histogram'], 'R2 replay equals the recorded local histogram')
    need(sum(r * c for r, c in local.items()) == exp['word']['legality']['rank_mass'], 'R2 local rank mass')
    return local, split, copies


def show(H):
    return {str(r): str(n) for r, n in sorted(H.items())}


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--write', action='store_true')
    a = ap.parse_args()
    out = {}
    binding, asm, exp, word = bind()
    out['binding'] = binding

    # --- positive control: the selected bit endpoint, full profile, surcharge included
    profile = {int(r): n for r, n in exp['nine']['profile'].items()}
    W = exp['nine']['bit']['live']
    c0 = frac(exp['nine']['bit_lower'])
    need(verdict(profile, M, W, c0, surcharge=True) == 'pass'
         and verdict(profile, M, W, c0 + Q(1, 10 ** 24), surcharge=True) == 'fail', 'P1 selected bit endpoint reproduced')
    out['selected_bit_endpoint'] = dict(endpoint=str(c0), accepted=True, next_grid_rejected=True)

    # --- replay and coverage law
    local, split, copies = replay(word, exp)
    v = word['v']
    T = W // (8 * v)
    stages = 9
    N = stages * T
    cst = sum(r * c for r, c in copies.items())
    w = Q(W, N)
    need(W == 8 * v * T and exp['nine']['bit']['rank_mass'] == (M - 1) * W + cst * N, 'R3 coverage law mass = (m-1)W + cst N')
    idle_total = Counter(profile)
    idle_total.subtract({r: c * N for r, c in local.items()})
    need(all(c >= 0 for c in idle_total.values()) and max(r for r, c in idle_total.items() if c) <= exp['nine']['bit']['maxchild'],
         'R3 the profile is N local words plus idle children')
    cap = max(r for r in range(1, M) if M * M > 2 * r * r)
    need(cap == 45, 'B5 halving-guard cap')
    out['replay'] = dict(
        v=v, replicas=T, stages=stages, calls=N, live=W, w=str(w), copy_charge_per_call=cst,
        local_histogram=show(local), local_mass=sum(r * c for r, c in local.items()),
        class_split={k: show(c) for k, c in split.items()}, copies=show(copies),
        class_mass={k: sum(r * c for r, c in s.items()) for k, s in split.items()},
        deficit=M * W - exp['nine']['bit']['rank_mass'], deficit_identity='D = W - %d N' % cst,
        idle_children_total=show(+idle_total), halving_guard_cap=cap)

    # --- revision-3 levers on the bit side (fixed local word unless stated; idle at the cap)
    mass = sum(r * c for r, c in local.items())
    no_copies = Counter(local)
    no_copies.subtract(copies)
    half_copies = {r: Q(c) - (Q(copies.get(r, 0), 2)) for r, c in local.items()}

    def lever(name, H_local, c, u=1, R=cap):
        lo, hi = root(relaxed(H_local, M, w, c, R, u), M, w)
        return dict(lever=name, root_lo=str(lo), root_hi=str(hi), root=dec(lo), idle_cap=R,
                    at_1_over_99=verdict(relaxed(H_local, M, w, c, R, u), M, w, TARGET))
    levers = [
        lever('PR589 bit word, ideal idle packing (packing ceiling)', local, cst),
        lever('centre path free (no rank-7 copies, copy charge 0)', +no_copies, 0),
        lever('centre path shared by two calls (copies and charge halved)', half_copies, Q(cst, 2)),
        lever('two unpaid coordinates per family', local, cst, u=2),
        lever('rank-8 children (local mass at rank 8 = window h)', {8: Q(mass, 8)}, cst),
        lever('rank-16 children (beyond the window h = 8)', {16: Q(mass, 16)}, cst),
        lever('centre free + rank-8 children', {8: Q(mass - cst, 8)}, 0),
        lever('centre free + rank-16 children', {16: Q(mass - cst, 16)}, 0),
        lever('centre free + two unpaid coordinates', +no_copies, 0, u=2),
    ]
    base = Q(levers[0]['root_lo'])
    for row in levers:
        row['multiplier'] = dec(Q(row['root_lo']) / base, 4)
    out['levers'] = levers
    out['cap_curve'] = [lever('PR589 bit word, ideal idle packing', local, cst, R=R) for R in (42, 45)] + \
        [dict(lever('PR589 bit word, ideal idle packing', local, cst, R=63), note='beyond the halving guard; robustness only')]

    # --- joint budget surface at a = 1/99: helpers (one climb of rank = width) per copy charge
    data_ideal = {7: Q(2 * v)}                          # each data register a single rank-7 climb
    data_shipped = split['sources'] + split['targets']
    surface = []
    for c in (0, 7, 14, 21, 28, Q(63, 2), 35, 42, 49, 56, 63):
        base_ideal = dict(data_ideal)
        base_ideal[7] = base_ideal.get(7, 0) + Q(c, 7)       # the copy charge carried as rank-7 copies
        base_ship = {r: Q(n) for r, n in data_shipped.items()}
        base_ship[7] = base_ship.get(7, 0) + Q(c, 7)
        row = dict(copy_charge=str(c))
        for label, b in (('ideal_data', base_ideal), ('shipped_data', base_ship)):
            for R in (cap, 63):
                res = max_count(b, 8, M, w, c, R, TARGET, 600)
                row['%s_width8_cap%d' % (label, R)] = None if res is None else dict(max_helpers=res[0], next=res[2])
        surface.append(row)
    widths = []
    for c in (0, Q(63, 2)):
        b = dict(data_ideal)
        b[7] = b.get(7, 0) + Q(c, 7)
        for width in (8, 7, 6, 4, 2):
            for R in (cap, 63):
                res = max_count(b, width, M, w, c, R, TARGET, 2000)
                widths.append(dict(copy_charge=str(c), helper_width=width, idle_cap=R,
                                   max_helpers=None if res is None else res[0], next=None if res is None else res[2]))
    out['joint_surface'] = surface
    out['helper_width'] = widths
    # obstruction rows, restated as certified verdicts
    o1 = {R: verdict(relaxed({7: Q(2 * v) + Q(cst, 7)}, M, w, cst, R), M, w, TARGET) for R in (cap, 63)}
    need(o1 == {cap: 'fail', 63: 'fail'}, 'O1 copy charge 63 cannot reach 1/99 in the relaxation')
    o1_lo, o1_hi = root(relaxed({7: Q(2 * v) + Q(cst, 7)}, M, w, cst, cap), M, w)
    out['O1'] = dict(statement='copy charge 63 per call, no helpers, every data register one rank-7 climb, idle at cap R',
                     verdicts={str(R): v_ for R, v_ in o1.items()}, helper_free_ceiling_cap45=dec(o1_lo),
                     helper_free_ceiling_bracket=[str(o1_lo), str(o1_hi)],
                     format_limits_bit_X_star='6.0005e-3 (research/format-limits section A, stronger axioms)')
    # O2: centre path shared by two calls against the design-free helper floors of research/format-limits section D
    floors = dict(strict=138, sink_only=212)
    shared = [r for r in widths if r['copy_charge'] == str(Q(63, 2)) and r['idle_cap'] == cap]
    need(next(r for r in shared if r['helper_width'] == 8)['max_helpers'] < floors['strict'], 'O2 shared centre leaves too few width-8 helpers')
    out['O2'] = dict(statement='copy charge 63/2 per call (centre path shared by two calls), every data register one rank-7 climb, '
                               'helpers one climb of rank = width, idle at the cap 45; floors from research/format-limits section D (argued premises)',
                     floors=floors,
                     max_helpers_by_width={str(r['helper_width']): r['max_helpers'] for r in shared},
                     widths_meeting_strict_floor=[r['helper_width'] for r in shared if r['max_helpers'] is not None and r['max_helpers'] >= floors['strict']],
                     widths_meeting_sink_only_floor=[r['helper_width'] for r in shared if r['max_helpers'] is not None and r['max_helpers'] >= floors['sink_only']])

    # --- complex cross-check (#1240) and #1272's combined lever inside / beyond the window
    cw = {1: 2412, 2: 418, 3: 432, 4: 142, 5: 82, 8: 8}
    cmass = sum(r * n for r, n in cw.items())
    cxw, ccst, ccap = Q(896, 9), 64, max(r for r in range(1, 73) if 73 * 73 > 2 * r * r)
    clo, chi = root(relaxed(cw, 73, cxw, ccst, ccap), 73, cxw)
    need(Q('0.0016900541090') < chi and clo < Q('0.0016900541091'), 'X1 #1240 complex word ceiling reproduced')
    rows = []
    for name, H, c in (('complex word ceiling (#1240)', cw, ccst),
                       ('centre free', {r: n for r, n in cw.items() if r != 8}, 0),
                       ('centre free + rank-9 children (window h = 9)', {9: Q(cmass - ccst, 9)}, 0),
                       ('centre free + rank-16 children (beyond the window)', {16: Q(cmass - ccst, 16)}, 0)):
        lo, hi = root(relaxed(H, 73, cxw, c, ccap), 73, cxw)
        rows.append(dict(lever=name, root_lo=str(lo), root_hi=str(hi), root=dec(lo), multiplier=dec(lo / clo, 4),
                         at_1_over_99=verdict(relaxed(H, 73, cxw, c, ccap), 73, cxw, TARGET)))
    out['complex_crosscheck'] = dict(m=73, w=str(cxw), copy_charge=ccst, idle_cap=ccap, rows=rows)

    text = json.dumps(dict(status='PASS_BIT_REVISION3_LEVERS', **out), indent=1, sort_keys=True) + '\n'
    target = HERE / 'RESULT.json'
    if a.write:
        target.write_text(text)
    elif text != target.read_text():
        raise SystemExit('FAIL RESULT.json differs from this run')
    for row in levers:
        print('%-62s a = %s  x%s  at 1/99: %s' % (row['lever'], row['root'], row['multiplier'], row['at_1_over_99']))
    print('PASS_BIT_REVISION3_LEVERS')


if __name__ == '__main__':
    try:
        main()
    except Reject as e:
        raise SystemExit('FAIL ' + str(e))
