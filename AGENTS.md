# Agent entry point

For open-ended requests such as “contribute,” “use spare inference,” or
“improve the bound,” start with [autoresearch.md](autoresearch.md). It contains
the current research priorities, task-selection procedure, overlap rules and
bounded stopping criteria. Explicit user tasks take precedence over that default
assignment; do not reroll an already assigned task.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before making changes. Resolve the current
result, review, source manifest and reproduction command through
`certificates/selected-result.json`. Historical research notes may use “current”
for an obsolete checkpoint.

Keep `upstream/`, frozen source archives and pinned evidence unchanged. Put new
research in its own scoped directory and retain predecessor attribution.
Distinguish a finite certificate, a scoped proof, a search failure and a complete
multiplication theorem. They are different claims.

Use an isolated branch/worktree when sharing a checkout. Run checks relevant to
the change; do not run concurrent artifact-regenerating suites in one worktree.
Record exact sources, commands, environments and any unrun proof obligations.

For donated-compute contributions, prepare one focused, reviewable result.
Do not change the selected frontier, merge or close others' PRs, or post public
coordination messages without user authorization. Existing explicit maintainer
authorization remains valid; these defaults do not require asking again.
