# Existing Operations And Recovery

GIT_OPERATION_IN_PROGRESS blocks ordinary development, safe update, and push. It does not forbid an explicitly requested diagnosis/resolution of that same merge, rebase, cherry-pick, revert or sequencer operation.

Start with read-only inspection: local branch/HEAD/status, unmerged index entries, and Git-resolved operation markers (git rev-parse --git-path supports linked worktrees). The helper inspect reports the marker and state with exit 1; do not suppress it or treat it as a request to begin unrelated work. Record the operation's source/destination and what the user authorized. Recovery may legitimately be detached during rebase, but this does not permit detached ordinary development or pushing.

If the user asks "why is there a conflict", diagnose without edits, aborts, or continue commits. If they request resolution, preserve pre-existing edits and resolve only the identified operation. Inspect base/ours/theirs and relevant business contracts; material semantic ambiguity needs a choice rather than guesses. A conflict-resolution request can include normal completion when clear; an explicit no-commit constraint still takes precedence.

Use the matching continue command to preserve operation metadata. Abort/skip/reset/force require their own justified scope/authorization; never use them simply to clear a marker. If an operation disappears or its HEAD/source changes externally, re-observe before further mutation. No automatic retry or bypass of hooks.

For wrong-branch edits or undo requests, identify exactly the task-owned paths/hunks and existing index state. Create an appropriate recoverable backup, verify the intended destination and patch applicability, and preserve unrelated changes. Do not broadly restore or delete files because they look related. Verify source and destination afterward and report backup location plus what was restored. Stop when safe separation cannot be established.

Finish by checking operation markers, unmerged entries, branch/HEAD and remaining work. Re-enter the development workflow with its original target before feature work, and verify-push before any authorized push. Neither recovery nor diagnosis grants remote creation, shared-history rewriting, or business-scope changes.
