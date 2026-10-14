# SPDX-License-Identifier: Apache-2.0
"""The PR442/PR463 hosting windows of the nine-stage PR589 bit template, rebuilt independently.

The idle schedule follows global_k.py's recipe (K = 4 bank pairs, L = 9 stages): a local cover sweep
per stage, the idle children it inserts, and the bridges. A child's window is the set of stages whose
sweep falls strictly after the child's pair was last touched and before the child is inserted, on
another pair. The result is cross-checked against BOTH vendored predicates (PR442
hosting_core.windows and the hosted audit's audit_hosted_k.windows) and against the frozen PR589
hosting selection. Standard library only.
"""
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VENDOR = ROOT / 'research/e8-bit-p111-tuned/vendor/pr510/e8-r480-nine-stage/vendor'
HOSTING_CORE = VENDOR / 'idle-axis-hosting/hosting_core.py'
AUDIT_HOSTED = VENDOR / 'e8-r715-eleven-stage-whole/code/audit_hosted_k.py'
SELECTION = ROOT / 'research/e8-bit-p111-tuned/data/selection9-p111.json'
K, L = 4, 9


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def schedule():
    events = [('local', 0, 0)]
    stage = 1
    for j in range(K):
        events.append(('local', stage, j)); stage += 1
        if j < K - 1:
            events.append(('bridge', j, j + 1))
        events.append(('local', stage, j)); stage += 1
        if j < K - 1:
            events.append(('bridge', j, j + 1))
    for j in reversed(range(K - 1)):
        events.append(('bridge', j + 1, j))
    sched, level = [], [-1] * K
    for e in events:
        if e[0] == 'local':
            _, s, p = e
            level[p] = s
            sched.append(dict(kind='local_cover_sweep', stage=s, pair=p))
            if s % 2 == 1 and s <= 2 * K - 3:
                j = (s + 1) // 2; level[j] = s; sched.append(dict(kind='idle', pair=j, rank=7 * (s + 1)))
            elif s % 2 == 0 and 2 <= s <= 2 * K - 2:
                j = s // 2; level[j] = s; sched.append(dict(kind='idle', pair=j, rank=7))
            elif s == 2 * K:
                for j in range(K):
                    sched.append(dict(kind='idle', pair=j, rank=7 * (2 * K - level[j]))); level[j] = 2 * K
        else:
            sched.append(dict(kind='bridge', dst=e[1], src=e[2]))
    sched.append(dict(kind='exchange'))
    i = 0
    for e in sched:
        if e['kind'] == 'idle':
            e['idx'] = i
            i += 1
    return sched


def windows(sched):
    out, last, seen = {}, {}, []
    for pos, e in enumerate(sched):
        if e['kind'] == 'local_cover_sweep':
            seen.append((pos, e['stage'], e['pair'])); last[e['pair']] = pos
        elif e['kind'] == 'bridge':
            last[e['dst']] = pos; last[e['src']] = pos
        elif e['kind'] == 'idle':
            out[e['idx']] = (e['pair'], e['rank'],
                             tuple(sorted(s for q, s, p in seen if last.get(e['pair'], -1) < q < pos and p != e['pair'])))
    return out


def checked_windows():
    """{child: (capacity, stages)} for the children that can host, after the three-way cross-check."""
    sched = schedule()
    mine = windows(sched)
    hc = _load('pr442_hosting_core', HOSTING_CORE)
    ah = _load('audit_hosted_k', AUDIT_HOSTED)
    hc_sched = [dict(e, kind='local') if e['kind'] == 'local_cover_sweep' else e for e in sched if e['kind'] != 'exchange']
    theirs = {i: (p, r, tuple(sorted(st))) for i, (p, r, st) in hc.windows(hc_sched).items()}
    W, rank, pair = ah.windows(sched)
    audit = {i: (pair[i], rank[i], tuple(sorted(W[i]))) for i in W}
    if not (mine == theirs == audit):
        raise ValueError('window predicates disagree')
    win = {i: (r, st) for i, (p, r, st) in mine.items() if r > 0 and st}
    for i, w, s, n in json.loads(SELECTION.read_text())['bit']['stages']:
        if s not in win[i][1]:
            raise ValueError('frozen selection entry outside its window')
    return win
