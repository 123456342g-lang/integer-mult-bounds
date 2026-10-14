# SPDX-License-Identifier: Apache-2.0
"""Controls for the independent RecipesExact check (about 20 s).

Run: python3 -I -B -m unittest discover -s research/frontier1094-recipes-exact-seed76 -p test_package.py -v
"""
import ast
import io
import json
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import clifford as C  # noqa: E402
import verify as V  # noqa: E402

DATA, BINDING = V.load()
CHILDREN, ADAPTERS, _ = V.inventory(DATA)
WORD = DATA['word']
FRAMES = WORD['frames']
BY_KEY = {(c['old'], c['new']): c for c in CHILDREN}
RESULT = json.loads((HERE / 'RESULT.json').read_text())


class Independence(unittest.TestCase):
    def test_kernel_and_verifier_import_only_the_standard_library(self):
        allowed = {'argparse', 'gzip', 'hashlib', 'io', 'json', 're', 'sys', 'tarfile', 'time', 'collections',
                   'pathlib', 'clifford'}
        for name in ('verify.py', 'clifford.py'):
            tree = ast.parse((HERE / name).read_text())
            mods = {a.name.split('.')[0] for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
            mods |= {n.module.split('.')[0] for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)}
            self.assertLessEqual(mods, allowed, name)
            names = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
            self.assertFalse(names & set(V.FORBIDDEN), name)


class Comparator(unittest.TestCase):
    def test_k1_a_projective_comparator_would_accept_a_global_phase_error(self):
        c = BY_KEY[(0, 174)]
        bad = V._mutate(c, ('left', 'phase'), lambda p: (p + 1) % 4)
        c1, c2 = V.child_circuits(bad, FRAMES)
        self.assertFalse(C.same_operator(c1, c2))                       # the exact comparator rejects it
        k1, k2 = C.c_gates(c1), C.c_gates(c2)
        beta = C.radix(max(k1, k2))
        s1, s2 = C.run(c1, beta), C.run(c2, beta)
        rotated = C.run(c2 + [('PH', 1)], beta)                          # side2 times i
        self.assertTrue(C.equal(s1, k1, rotated, k2, beta))             # equal up to the unit i: projectively equal

    def test_k2_a_column0_comparator_would_accept_an_input_character_error(self):
        c = BY_KEY[(0, 2)]
        bad = V._mutate(c, ('right', 'linear_Z4'), lambda a: a[:5] + [(a[5] + 2) % 4] + a[6:])
        c1, c2 = V.child_circuits(bad, FRAMES)
        self.assertFalse(C.same_operator(c1, c2))
        k = max(C.c_gates(c1), C.c_gates(c2))
        beta = C.radix(k)
        col1 = C.columns(C.run(c1, beta), beta)
        col2 = C.columns(C.run(c2, beta), beta)
        sc1, sc2 = 1 << (k - C.c_gates(c1)), 1 << (k - C.c_gates(c2))
        scale = lambda col, s: {y: (re * s, im * s) for y, (re, im) in col.items()}  # noqa: E731
        self.assertEqual(scale(col1[0], sc1), scale(col2[0], sc2))       # column 0 alone cannot see it
        self.assertNotEqual(scale(col1[32], sc1), scale(col2[32], sc2))  # column e5 does

    def test_k3_radix_guard(self):
        s = C.run([], 4)
        with self.assertRaises(ValueError):
            C.equal(s, 1, s, 1, 3)

    def test_signed_digit_lemma_boundary(self):
        # beta = 2K + 2 keeps every scaled digit difference below 2^beta: a single C gate on |0> gives
        # numerators of size 1, and K = 1 needs beta = 4
        self.assertEqual(C.radix(1), 4)
        self.assertEqual(C.radix(16), 34)


class Semantics(unittest.TestCase):
    def test_all_semantic_controls_reject(self):
        out = V.semantic_controls(CHILDREN, ADAPTERS, WORD)
        self.assertEqual(out, RESULT['controls'])
        self.assertEqual(len(out), 12)

    def test_rank_off_by_one_is_rejected_structurally_and_by_the_evaluator(self):
        c = dict(BY_KEY[(0, 174)], rank=2)
        bad = {'children': [c if (x['old'], x['new']) == (0, 174) else x for x in CHILDREN],
               'endpoint_adapters': ADAPTERS}
        with self.assertRaisesRegex(V.Reject, 'I3 child rank'):
            V.inventory(dict(DATA, recipes=bad))
        self.assertFalse(C.same_operator(*V.child_circuits(c, FRAMES)))

    def test_swapped_matrix_rows_and_adapter_phase_are_rejected(self):
        c = V._mutate(BY_KEY[(0, 415)], ('left', 'matrix_rows'), lambda G: [G[1], G[0]] + G[2:])
        self.assertFalse(C.same_operator(*V.child_circuits(c, FRAMES)))
        x = V._mutate(ADAPTERS[1], ('left', 'phase'), lambda p: (p + 1) % 4)
        self.assertFalse(C.same_operator(*V.adapter_circuits(x, WORD)))

    def test_every_rank_class_has_a_rejected_phase_mutant(self):
        seen = set()
        for c in CHILDREN:
            if c['rank'] in seen:
                continue
            seen.add(c['rank'])
            bad = V._mutate(c, ('left', 'phase'), lambda p: (p + 1) % 4)
            self.assertTrue(C.same_operator(*V.child_circuits(c, FRAMES)), c['rank'])
            self.assertFalse(C.same_operator(*V.child_circuits(bad, FRAMES)), c['rank'])
        self.assertEqual(seen, {1, 2, 3, 4, 5, 8})


class Binding(unittest.TestCase):
    def test_d1_decoy_recipes_rejected(self):
        with self.assertRaisesRegex(V.Reject, 'B6 provider file digest: recipes'):
            V.load(member_overrides={'recipes': V.CASES['decoys']['recipes']})

    def test_d2_decoy_word_rejected(self):
        with self.assertRaisesRegex(V.Reject, 'B6 provider file digest: canonical_word'):
            V.load(member_overrides={'canonical_word': V.CASES['decoys']['canonical_word']})

    def test_d3_one_phase_digit_changed_in_the_recipe_bytes(self):
        raw = V.canonical_bytes(DATA['recipes'])
        i = raw.index(b'"phase":0')
        flipped = raw[:i] + b'"phase":1' + raw[i + 9:]
        with self.assertRaisesRegex(V.Reject, 'B6 provider file digest: recipes'):
            V.load(byte_overrides={'recipes': flipped})

    def test_d4_duplicate_json_key(self):
        with self.assertRaisesRegex(V.Reject, 'duplicate JSON key'):
            V.strict_loads(b'{"a":1,"a":2}')

    def _archive(self, mutate):
        raw = (V.ROOT / V.CASES['archive']['path']).read_bytes()
        return mutate(raw)

    def test_archive_byte_flip(self):
        with tempfile.TemporaryDirectory() as d:
            raw = self._archive(lambda b: b[:-1] + bytes([b[-1] ^ 1]))
            p = Path(d) / 'a.tar.gz'
            p.write_bytes(raw)
            with self.assertRaisesRegex(V.Reject, 'B1 archive digest'):
                V.load(archive_path=p)

    def test_unsafe_archive_members(self):
        for name in ('../escape', 'dup'):
            buf = io.BytesIO()
            with tarfile.open(fileobj=buf, mode='w') as tar:
                for n in ([name] if name != 'dup' else ['dup', 'dup']):
                    info = tarfile.TarInfo(n)
                    info.size = 0
                    tar.addfile(info, io.BytesIO(b''))
            buf.seek(0)
            with tarfile.open(fileobj=buf, mode='r') as tar:
                with self.assertRaisesRegex(V.Reject, 'B2'):
                    V.safe_members(tar)

    def test_binding_is_recorded(self):
        self.assertEqual(BINDING, RESULT['binding'])
        self.assertTrue(BINDING['global8_twin_byte_identical'])


class Coverage(unittest.TestCase):
    def test_result_covers_every_record_and_column(self):
        ev = RESULT['evaluation']
        self.assertEqual((ev['children'], ev['adapters'], ev['columns']), (2896, 224, 512))
        self.assertTrue(ev['global_phase_included'])
        self.assertEqual(sum(ev['K_histogram'].values()), 2896)

    def test_subset_run_on_two_children_and_one_port(self):
        out = V.evaluate(CHILDREN, ADAPTERS, WORD, subset='pair=0:174,ports=5')
        self.assertEqual((out['children'], out['adapters']), (1, 2))


if __name__ == '__main__':
    unittest.main()
