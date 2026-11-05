# Verify Every Actual Push

First establish authorization and repository PR rules. Passing verification neither authorizes a push nor proves write permission/protected-branch acceptance. Support only current HEAD to a single existing destination branch.

Identify the actual remote, destination branch and expected local branch/HEAD for this push; the destination can differ from development upstream. Announce and run:

```text
py -3 "<skill-directory>\scripts\git_latest_code.py" verify-push --repo "<repository>" --remote "<remote>" --branch "<destination>" --expect-branch "<source-local-branch>" --expect-head "<current-full-SHA>"
```

The helper reads git remote get-url --push --all and queries the actual push address, not necessarily the fetch address. Multiple addresses, complex/multiple refspecs or destinations require a single explicit target first. Do not change configuration or silently choose.

Only CURRENT/AHEAD exit 0 permits the already-authorized push. Missing destination, BEHIND, DIVERGED, REMOTE_DIFFERS, unfinished operations, wrong branch, changed HEAD, or errors stop the push, even when dirty. Dirty alone does not prohibit pushing committed content. Missing remote objects yield REMOTE_DIFFERS and require further verification; this helper must not fetch.

Report status, repository/source branch, exact remote destination, commits and dirty state before pushing. Push exactly the verified HEAD and target, without relying on default push refspecs. If HEAD/target changes or an update completes, reverify; never reuse a development check as push verification. Follow an actual rejection, do not force past it.

No automatic new remote branches or restoration of deleted branches. A local branch without upstream is not permission to publish it. Requests outside this supported boundary need an explicit policy choice, not a hidden bypass.

After push report the actual result and confirm the destination tip when available. Remote movement after observation is possible. Record final local branch and preserve development-target identity; push success does not establish deployment, tests, or business completion.
