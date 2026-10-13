#!/usr/bin/env python3
"""Offline provenance/reconciliation integrity; --git-blobs checks retained source bytes.

This is not a multiplication-theorem verifier and does not replay historical CI.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path, PurePosixPath
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def require(ok, msg):
    if not ok:
        raise ValueError(msg)


def load(name):
    b = (HERE/name).read_bytes()
    return json.loads(gzip.decompress(b) if name.endswith('.gz') else b)


def oid(kind, raw):
    return hashlib.sha1(kind.encode()+b' '+str(len(raw)).encode()+b'\0'+raw).hexdigest()


def tree_oid(files):
    tree = {}
    for f in files:
        p = PurePosixPath(f['path'])
        require(not p.is_absolute() and '..' not in p.parts and str(p) == f['path'], 'Unsafe source path')
        node = tree
        for part in p.parts[:-1]:
            node = node.setdefault(part, {})
        require(p.name not in node, 'Duplicate source path')
        require(f['mode'] in ('100644', '100755'), 'Unexpected source mode')
        node[p.name] = (f['mode'], f['blob'])
    def encode(node):
        entries = []
        for name, value in node.items():
            directory = isinstance(value, dict)
            mode, sha = ('40000', encode(value)) if directory else value
            entries.append(((name+('/' if directory else '')).encode(), mode.encode()+b' '+name.encode()+b'\0'+bytes.fromhex(sha)))
        return oid('tree', b''.join(raw for key, raw in sorted(entries)))
    return encode(tree)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git-blobs', action='store_true')
    args = parser.parse_args()
    manifest = load('MANIFEST.json')
    for path, sha in manifest['files'].items():
        require(hashlib.sha256((HERE/path).read_bytes()).hexdigest() == sha, 'Changed evidence: '+path)
    for path, sha in manifest.get('integrated_files', {}).items():
        require(hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == sha, 'Changed integrated source: '+path)
    source = load('SOURCES.json.gz')['pull_requests']
    snapshot = {r['number']:r for r in load('STARTING-SNAPSHOT.json')['pull_requests']}
    decisions = {r['number']:r for r in load('DISPOSITIONS.json')['pull_requests']}
    review = load('REVIEW.json')
    coverage = load('FILE-DISPOSITIONS.json.gz')
    require(len(source) == len(snapshot) == len(decisions) == 92, 'Frozen batch cardinality')
    require(set(snapshot) == set(decisions) == {r['number'] for r in source}, 'Frozen batch identity')
    blobs = {}
    for r in source:
        n=r['number']; d=decisions[n]
        require(r['head'] == snapshot[n]['headRefOid'] == d['reviewed_head'], f'#{n}: head mismatch')
        require(r['metadata']['author'] == snapshot[n]['author'], f'#{n}: lost author')
        require(oid('commit', r['commit_object'].encode()) == r['head'], f'#{n}: commit authentication')
        require(r['commit_object'].startswith('tree '+r['tree']+'\n'), f'#{n}: commit tree')
        require(tree_oid(r['files']) == r['tree'], f'#{n}: complete original tree')
        require(str(n) in review and review[str(n)]['mechanism'], f'#{n}: missing scoped review')
        expected={(f['path'],f['status'],f['old_blob'],f['new_blob']) for f in r['changed_files']}
        actual={(f['path'],f['status'],f['old_blob'],f['new_blob']) for f in coverage[str(n)]}
        require(len(coverage[str(n)])==len(expected) and actual==expected, f'#{n}: incomplete original diff coverage')
        require(all(f['treatment'] for f in coverage[str(n)]), f'#{n}: file without treatment')
        flags=d['review_completion']
        require(set(flags)=={'changed_file_coverage','scoped_mechanism_review','required_execution_complete','published'}
                and all(type(v) is bool for v in flags.values()), f'#{n}: malformed completion flags')
        if d['disposition']=='incorporated':
            require(all(flags.values()) and d['unresolved_question'] is None, f'#{n}: premature incorporation')
        if d.get('closure'):
            require(d['github_state'] in ('CLOSED','MERGED'), f'#{n}: closure state')
            require(d['current_head']==r['head'], f'#{n}: closure on changed head')
        for f in r['files']:
            old=blobs.setdefault(f['blob'], (f['sha256'],f['bytes']))
            require(old==(f['sha256'],f['bytes']), 'Inconsistent source blob inventory')
    for receipt in load('EXECUTION.json')['receipts']:
        require(receipt['head']==snapshot[receipt['number']]['headRefOid'], 'Local receipt head differs')
        digest=receipt.get('sha256', receipt.get('log_sha256'))
        raw=gzip.decompress((HERE/receipt['retained_log']).read_bytes())
        require(hashlib.sha256(raw).hexdigest()==digest, 'Local log receipt differs')
    for row in load('CI-EVIDENCE.json.gz'):
        require(row['head']==snapshot[row['number']]['headRefOid'], 'CI receipt head differs')
        for run in row['runs']:
            require(run['head']==row['head'], 'CI run belongs to a different head')
        for log in row['inspected_logs']:
            raw=gzip.decompress((HERE/'logs'/log['file']).read_bytes())
            require(hashlib.sha256(raw).hexdigest()==log['log_sha256'], 'CI log receipt differs')
    archive=load('ARCHIVE.json')
    require(set(archive['parents'])=={r['head'] for r in source}, 'Source archive omitted a head')
    require(oid('commit',archive['commit_object'].encode())==archive['commit'], 'Archive commit authentication')
    require(set(x[7:] for x in archive['commit_object'].splitlines() if x.startswith('parent '))==set(archive['parents']), 'Archive parent binding')
    if args.git_blobs:
        proc=subprocess.Popen(['git','cat-file','--batch'],cwd=ROOT,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        try:
            for sha,(digest,size) in blobs.items():
                proc.stdin.write((sha+'\n').encode());proc.stdin.flush()
                header=proc.stdout.readline().decode().split()
                require(header==[sha,'blob',str(size)], 'Missing source object: '+sha)
                raw=proc.stdout.read(size);require(proc.stdout.read(1)==b'\n','Git protocol')
                require(oid('blob',raw)==sha and hashlib.sha256(raw).hexdigest()==digest, 'Changed source bytes: '+sha)
        finally:
            proc.stdin.close();proc.stdout.close();proc.wait()
    print(f'PASS 92 pinned full trees, {len(blobs)} distinct blobs, original-diff coverage, scoped decisions and evidence integrity; no theorem claim')


if __name__ == '__main__':
    main()
