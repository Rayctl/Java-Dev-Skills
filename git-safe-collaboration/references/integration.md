# Branches And Integration

Read only for a requested branch operation, merge, or history reconstruction. The ff-only restriction of automatic development updates is not a ban on an explicitly authorized integration merge. It is also not authorization to integrate anything.

## Bind This Operation

Keep confirmed development branch, integration source SHA/branch, destination branch and remote comparison target separate. A request to merge development into test authorizes work on that destination for the integration, not future feature development there.

Before mutation inspect exact source/destination refs, HEAD, existing operation markers and staged/unstaged/untracked work. Recheck expected branch/HEAD before mutation. If another operation exists, route to recovery.md; do not start a competing one.

For a destination that must track an existing remote, check that selected existing target and follow the readiness rules. A local historical source being replayed/merged need not itself have an upstream; inspect its immutable commits without falsely declaring it remotely current. This is not a local-only feature-development or new-remote-branch exception. No remote creation/restoration. Do not pick an obsolete or integration branch as a substitute development baseline.

Branch creation/switching must follow the user's requested name and base or repository requirements. Do not invent a codex/ branch on master merely to get a check to pass. Confirm meaningful ambiguity; never force checkout or overwrite existing work.

## Merge Or Reconstruct

Before replay/reconstruction inspect affected shared branches and existing integration history. Distinguish commit ancestry, equivalent patch content, and final file-tree equality. Explain likely downstream costs, including changed merge bases, add/add conflicts and persistent old author attribution. Do not infer "no future conflict" from identical trees.

Prefer an isolated worktree for history reconstruction or a risky integration when practical. Keep original refs and unrelated files recoverable. Isolation does not itself authorize a new destination, force push, or replacement of shared history.

For an authorized merge inspect both parents and the merge base, resolve conflicts by each side's intent, preserve destination-side independent changes, and load applicable language checks before editing source. Do not blanket-select ours/theirs or overwrite an entire file based only on one tip. An available verified integration tree is a useful cross-check, not proof that business behavior is correct.

Verify result parents/ancestry, intended changes, preserved destination changes, unresolved paths, and task-scoped tests (or explicit limitations). If provenance is part of the goal, use commits.md as well. Do not silently change merge direction to influence blame.

## Exit And Delete

Report current branch, operation state, merge/replay commit(s), validation and whether anything was pushed. Keep the development target unchanged in the task observation. If left on the integration branch, say so; before the next feature edit verify against the confirmed development branch. Return only when already authorized and safe; otherwise stop for the target choice, never automatically carry dirty changes across.

Deletion requires an exact ref and explicit local/remote scope. Preserve unique commits/recovery refs as appropriate; check all linked worktrees. A successful branch -d, tree equality, or upstream containment alone does not prove integration into the intended destination. Check the intended history and explain unique histories before deletion. If local vs remote scope is ambiguous, ask; never silently extend local deletion to the remote. Remote deletion is a separately authorized destructive action, not supported by verify-push.
