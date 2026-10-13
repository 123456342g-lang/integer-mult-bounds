# Sprint claim: archived asynchronous inventory bound

- Track: research consolidation; assignment seed **95**.
- OS randomness: `od -An -N4 -tu4 /dev/urandom` returned `2227208895`.
  This is below `floor(2^32/100)*100 = 4294967200`; reduction modulo 100
  gives 95 without modulo bias (a value above that cutoff would be redrawn).
- Exact base: `66849e1475c930fd7732b1a0067ffee7e1e95f60`, freshly cloned
  and confirmed by `git pull --ff-only`.
- Candidates, in order: reconcile selected #626 Linux evidence; bind family
  review decisions to the ledger; reconcile the archived 146-profile
  asynchronous inventory bound with its source records. Seed `95 % 3 = 2`
  selects the third; #695 and #704 already cover the first two.
- Exact scope: the finite profile/width menu and exact dual receipts in
  `research/experiment-log/negative-searches/async505-inventory-wall/`.
  Resolve whether its portable replay binds the 146 rows to the archived
  result files and detects invalid evidence. Check both exact engines.
- Method: exhaustive comparison of the 146 retained menu entries and their
  source result files; exact replay; controlled source/receipt mutations.
  No new allocation, word, timing, or supplier search.
- Expected deliverable: an offline, reproducible evidence reconciliation
  checker and a scoped report, with source pins and negative controls.
- Time box: 35 minutes from 2026-10-13 04:41:33 UTC; finish by 05:16:33 UTC.
  Orientation ends before 04:48:33; final verification/handoff begins by
  05:07:48 UTC (the final quarter).
- Coordination check: GitHub's pinned-issue query returned no issues;
  refreshed open-PR metadata through #716 showed no matching inventory-wall
  reconciliation. #630 corrects a different archived E6 screen. No separate
  reservation issue was opened.
- Contributor: Alexander Templeton (`azide0x37`), with substantial OpenAI
  Codex assistance. Original archive, search, and arithmetic authors retain
  their attribution. Apache-2.0.
