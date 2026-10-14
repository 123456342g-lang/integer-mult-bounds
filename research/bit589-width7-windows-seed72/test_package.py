# SPDX-License-Identifier: Apache-2.0
"""Controls for the width-7 window audit (about 15 s).

Run: python3 -I -B -m unittest discover -s research/bit589-width7-windows-seed72 -p test_package.py -v
"""
import copy
import itertools
import json
import sys
import unittest
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify as V  # noqa: E402
import windows  # noqa: E402
import wopt  # noqa: E402

RESULT = json.loads((HERE / 'RESULT.json').read_text())


class Windows(unittest.TestCase):
    def test_capacity7_children_admit_one_stage_each(self):
        ah = windows._load('audit_hosted_k', windows.AUDIT_HOSTED)
        W, rank, _ = ah.windows(windows.schedule())
        sevens = {i: sorted(W[i]) for i in W if rank[i] == 7 and W[i]}
        self.assertEqual(sevens, {1: [2], 3: [4], 5: [6]})

    def test_cw1_window_free_k1_uses_nine_seven_slots(self):
        # #1023's partial placement (packing.width7_partial_idle) fills 9 capacity-7 copies per replica
        # with one width-7 residual from each of the 9 stages; the vendored windows admit only stages
        # 2, 4 and 6 there, so at least 6 of the 9 residuals sit outside their window.
        model = wopt.P.slot_model(wopt.P.pinned_json('bit_record'), wopt.P.pinned_json('selection'))
        idle = wopt.P.width7_partial_idle(model, 1)
        self.assertEqual(Counter(model['idle_rep'])[7] - idle[7], 9)
        admitted = {s for i in wopt.SEVEN for s in wopt.WIN[i][1]}
        self.assertEqual(len(set(range(9)) - admitted), 6)


class Certificates(unittest.TestCase):
    def test_k0_reproduces_the_selected_endpoint_and_is_tight(self):
        row = RESULT['rows']['0']['optimistic']
        self.assertEqual(Q(row['endpoint']), Q(wopt.P.pinned_json('bit_record')['nine']['bit_lower']))
        self.assertTrue(row['same_argmin_at_bound'])

    def test_cw2_window_free_local_rows_exceed_the_bound(self):
        for k in ('1', '2', '10', '37', '74'):
            for b in ('optimistic', 'pessimistic'):
                r = RESULT['rows'][k][b]
                self.assertGreaterEqual(Q(r['windowfree_endpoint']), Q(r['certified_bound']))
                self.assertLess(Q(r['endpoint']), Q(r['certified_bound']))

    def test_cw3_pr1281_local_and_pooled_rows_exceed_the_per_replica_bound(self):
        priced = RESULT['pr1281']['priced_cases']
        self.assertEqual(len(priced), 9)
        for key, row in priced.items():
            if key != 'k0_optimistic':
                self.assertTrue(row['unreachable'], key)
        self.assertEqual(RESULT['pr1281']['idle_optima_matched'], 75)

    def test_pr1023_partial_rows_all_unreachable(self):
        rows = RESULT['pr1023_partial_rows']
        self.assertEqual(len(rows), 8)
        self.assertTrue(all(r['unreachable'] for r in rows.values()))

    def test_cw4_all_width7_optimum_is_window_feasible(self):
        lo, hi, n = RESULT['all_width7']['feasible_sextet_splits']
        self.assertGreater(n, 0)
        x4 = lo
        cps = {i: ([wopt.CAP[i] // 7] * wopt.N if wopt.CAP[i] in (7, 14, 28) else []) for i in wopt.WIN}
        cps[4] = [6] * x4
        cps[6] = [6] * (103 - x4) + [3]
        x = V.maxflow_assign({s: wopt.R for s in range(9)}, {i: sum(cps[i]) for i in wopt.WIN},
                             {i: set(wopt.WIN[i][1]) for i in wopt.WIN})
        self.assertIsNotNone(x)


class Reduction(unittest.TestCase):
    def test_brute_force_matches_the_chains(self):
        n, agree = V.brute_force_reduction(2)
        self.assertEqual(n, agree)

    def test_cw5_dropping_a_chain_constraint_breaks_agreement(self):
        original = V.chain_ok
        try:
            V.chain_ok = lambda B, k: (B[0] + B[2] <= 3 * k and B[0] + B[2] + B[4] <= 4 * k and B[8] <= 2 * k
                                       and B[8] + B[7] <= 3 * k and B[8] + B[7] + B[6] <= 4 * k
                                       and B[0] + B[2] + B[4] + B[8] + B[7] + B[6] == 6 * k)   # B0 <= 2k dropped
            n, agree = V.brute_force_reduction(1)
            self.assertLess(agree, n)
        finally:
            V.chain_ok = original

    def test_cw5_a_perturbed_window_changes_the_structure(self):
        saved = dict(wopt.WIN)
        try:
            wopt.WIN[0] = (14, (0, 1, 2, 3))              # child 0 would also admit stages 2 and 3
            with self.assertRaises(AssertionError):
                wopt.check_chain_reduction(1)
        finally:
            wopt.WIN.clear()
            wopt.WIN.update(saved)

    def test_hall_width8_conditions_are_vacuous_in_range(self):
        self.assertTrue(all(V.w8_vacuous(k) for k in (0, 1, 37, 74)))


if __name__ == '__main__':
    unittest.main()
