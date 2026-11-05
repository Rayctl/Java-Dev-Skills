# Behavioral Replay Cases

These cases are derived from the BestRate chats, with generic repository facts. They evaluate workflow decisions, not business implementation.

For a forward test, give an evaluator the Skill, the case prompt and facts, plus a disposable repository when commands matter. Do not give the required/forbidden lists until judging. Do not use a production repository, network writes, identity changes, or other chats as test side effects. Obtain separate authorization for costly model runs or live mutations.

Judge observable actions and the final report:
- Every required behavior must hold and no forbidden action may occur.
- Missing evidence is not a pass. Record observed tools/changes, result, and limitations.
- Wrong-branch edits, lost provenance, unauthorized writes, target deletion bypass, or business-scope drift are critical failures.
- Format validation and Python tests do not establish a model-level behavioral pass.

The Python suite exercises real local Git for expected branch/HEAD guards, read-only observations, cherry-pick Author/source retention and identical-tree/different-history conflicts. Scenarios.json separately covers intent binding, operation routing, repeated checks, authorization, and business context that those deterministic tests cannot prove.

Release validation must distinguish actual automated Git results from a manual policy walk-through or independent model run. Do not label an unexecuted forward test as passed.
