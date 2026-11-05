# Development Readiness And Safe Update

Read for substantive code planning/modification, not as a prerequisite for an explicit history transfer, integration, or conflict-recovery task.

## Choose The Development Target

Use the task's confirmed local development branch, independently of the remote comparison target. Without upstream, require a user-selected existing remote target; never infer one, set upstream, create/restore a remote branch, or waive this requirement because the worktree is dirty. If an explicit target differs from configured upstream, report both and ask once unless the task already confirms the choice.

Read branch.remote/merge even if cached tracking refs were pruned. The helper queries the remote and preserves custom fetch mapping. Choosing a comparison target does not switch branches or authorize merging its content into the local branch.

Run:

```text
py -3 "<skill-directory>\scripts\git_safe_collaboration.py" check --repo "<repository>" --expect-branch "<development-branch>"
```

Pass an explicitly selected --remote / --branch pair consistently to subsequent check/update calls. The helper accepts that pair as caller-confirmed, not as an interactive choice.

## Interpret Results

| Status | Clean worktree | Dirty worktree |
| --- | --- | --- |
| CURRENT | Continue the established task | Continue only after confirming related work |
| AHEAD | Inspect/report extra commits and their task ownership | Also confirm existing changes are related |
| BEHIND | Announce and attempt one safe fast-forward | Warn, freshness unconfirmed; related existing work only, no update |
| REMOTE_DIFFERS | Stop; request approval for one safe update attempt | Same warning-only exception as BEHIND |
| DIVERGED | Stop; user resolves history | Same warning-only exception; do not merge/rebase automatically |
| REMOTE_UNAVAILABLE | Stop; report network/auth/timeout/response issue | Only temporary access failure may warn for related existing work |
| REMOTE_BRANCH_MISSING | Always stop; ask for correct existing target | Always stop, no dirty exemption |
| NO_UPSTREAM | Stop; ask for an existing target | Always stop |
| GIT_OPERATION_IN_PROGRESS | Stop ordinary development; route explicit recovery to recovery.md | Same |
| WRONG_BRANCH / unexpected HEAD | Stop this action and resolve target ambiguity | Same |
| DETACHED / ERROR | Stop ordinary development | Same |

AHEAD contains the remote tip plus local commits, not proof that all commits belong to this task. Inspect a bounded log of remote-SHA..HEAD and preserve unrelated work; never redefine the task to absorb it.

BEHIND requires that the remote object is already local and ancestry is known. Missing objects yield REMOTE_DIFFERS, not BEHIND. The read-only check never fetches.

## Reuse Observations Without Missing Branch Drift

Within continuing work on the same confirmed repository, development branch, and comparison target, reuse the remote observation across follow-up messages. A new chat turn alone is not a new task. Recheck local branch/HEAD and operation state before each edit batch and after integration/recovery; this local guard does not access the remote.

Repeat the remote check when the user requests it, the repository/branch/target changes, a successful update requires refreshed verification, or concrete evidence invalidates the previous observation (for example a reported deletion or force-update). After an interrupted session/handoff or external integration, check afresh if the prior observation cannot safely be treated as continuous work. An intentional local commit needs local reinspection and extra-commit ownership checks, not an automatic network round trip. Missing context requires recovering the prior observation or checking afresh, not inventing confirmed freshness. Push verification is independent and always repeated before pushing.

## One Safe Update

Only clean BEHIND authorizes one automatic attempt under the standing policy. Announce first: repository, branch, target, actual observed status, available local/remote short commits, clean state, one selected fetch plus merge --ff-only if safe. Clean REMOTE_DIFFERS requires task-specific approval and must be described as uncertain ancestry. In a mutation-prohibiting mode, defer the update.

```text
py -3 "<skill-directory>\scripts\git_safe_collaboration.py" update --repo "<repository>" --expect-branch "<development-branch>" --expect-head "<observed-full-SHA>"
```

Retain the same explicit target pair if used during check. Reject all staged, tracked, and untracked changes. The helper rejects unfinished operations, unresolved/deleted targets, divergence, non-fast-forward rewrites, concurrent local/remote movement; it distinguishes branch absence from access failure before fetch, after fetch failure, and after merge. No retry. Never substitute stash, reset, rebase, forced fetch, ordinary merge, branch switch, or upstream configuration for this update.

Update failure may occur after HEAD moved. Report the latest observed commit, stop the attempt, retain task context, and do not claim unchanged code without evidence.

## Handoff

Carry repository/worktree, development branch, current full local SHA, remote comparison target/SHA, freshness and observation context alongside business requirements and progress. CURRENT/AHEAD/successful UPDATED gives remoteFreshness: confirmed for that observation; permitted dirty warnings gives unconfirmed. Blockers do not satisfy readiness.

After UPDATED refresh the observed HEAD, retain the old SHA if useful for changed-code review, reread applicable rules and affected source, and revalidate affected conclusions only. Never replace a fixed commit/PR/tag comparison base or accepted business decisions. A permitted unconfirmed local observation cannot refresh Java project-guidance metadata baselines; downstream correctness checks still apply.
