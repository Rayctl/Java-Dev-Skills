# Commits And Provenance

Read only when a commit or commit transfer is requested/authorized. Coding, CR, passing checks, or an automatic safe update does not authorize an ordinary commit or push. Preserve repository hooks and required review/PR workflows.

## New Task-Owned Commit

1. Confirm repository, expected local branch and current HEAD with the local guard. Inspect staged, unstaged and untracked changes; identify the task-owned scope. Existing staged content is not automatically in scope.
2. Review the final intended diff and run applicable task checks. Stage explicit paths or narrowly owned hunks; do not use a blanket git add when unrelated work exists. If changes overlap inseparably, ask rather than resetting the user's index/worktree.
3. Follow explicit user/repository message rules first. Otherwise use Conventional Commits with an English type and Chinese subject, e.g. fix(git): 保留开发分支与集成目标. Add a body for non-obvious reasons, impact or validation limitations; avoid unsupported claims of testing.
4. Preserve source messages on cherry-pick/replay; do not translate original history merely for the new-commit language preference. A required repository merge-message template also takes precedence.
5. After committing verify the actual parent(s), tree, author/committer, message, changed paths and remaining worktree. Report the SHA, target branch and excluded work. Commit success is not push authorization.

Do not bypass hooks, falsify review labels, change identity, amend prior commits, or rewrite history to repair failures without authorization.

## User Requests Cherry-Pick

The requested operation is a provenance requirement, not just a request for equivalent code. Resolve the source to immutable commit SHA(s), inspect author, parents and change scope, and identify destination branch and replay order. Check whether commits or equivalent patches are already present before applying.

Use an actual git cherry-pick, normally with -x for a source trace. Preserve original Author; the acting identity is Committer. When conflicts occur, resolve only in the authorized transfer scope and use cherry-pick --continue so source metadata is retained. Keep later task-specific adaptations separate from the migrated commit.

Do not silently use git show/copy/manual edits or cherry-pick --no-commit plus a new mixed commit as a substitute. If the user forbids commits, wants a squash, or source dependencies make faithful transfer impossible, explain the tradeoff and obtain a choice before changing the requested history semantics. Do not promise a conflict-free replay.

Verify each resulting source-to-destination SHA mapping, Author and source trace, and explain conflict-resolution/adaptation differences. An empty or already-applied commit needs diagnosis, not automatic skip, duplicate commit, or invented provenance.

## Authorship Is Not One Property

Report separately when relevant:

- Author: who originally authored the commit.
- Committer: who created this commit object here.
- Source trace: which original commit was migrated.
- Line attribution (blame): what the actual destination history reports.

Tree equality does not establish history equality or blame equality. A later merge preserves existing historical commits; never promise that merging a correctly authored replay will replace old attribution. Inspect the actual destination blame when that is the user's goal. Prefer explaining the limitation over rewriting shared history for a display change.
