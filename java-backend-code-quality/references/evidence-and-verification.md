# Evidence, Context, And Final Verification

Read when planning, analyzing, implementing, or reviewing existing behavior or data semantics, when business decisions need diagnostic evidence, when evidence is missing or conflicting, or when tools may change files after an edit. Investigate the requested semantic neighborhood in any mode; the implementation loop and final-state readback below apply when files are actually edited. See [task-modes.md](task-modes.md) for read-only output and verification boundaries.

## Incremental Implementation Loop

Use a light loop for simple changes and a checkpoint loop for complex changes. Complexity is semantic, not a line-count threshold.

Preserve the user's approved requirements and behavior changes throughout discovery and verification. Source and tests establish previous behavior; they do not veto an authorized contract change. Preserve unaffected semantics, update affected callers and tests, and ask only about remaining material conflicts that the accepted requirements do not resolve.

A change is usually simple when it is a local rename, direct assignment, getter, pure conversion, isolated branch, or test-data adjustment with no external call, persistent state, cross-field invariant, lifecycle, error-policy, or diagnostic change. Read the target neighborhood, route only triggered references, make the edit, then reread the changed method and final diff. Do not pause after every line or load unrelated references.

Treat a change as complex when it has multiple business stages, changes a boundary call, reads or writes a database, cache, file, queue, or remote service, crosses a transaction or asynchronous boundary, changes state or lifecycle, has retries or compensation, changes error or logging behavior, or relies on related fields jointly expressing a contract. A simple task becomes complex as soon as the edit introduces one of these concerns. Do not downgrade the checks merely because an individual statement is short.

Before the first edit of a complex task:

1. Record the trigger, affected callers, data sources, stage outputs, failure paths, diagnostics, and tests needed to explain the existing behavior
2. Classify the stages and load only references whose triggers are present
3. Identify assumptions that would require a user decision if the evidence remains unresolved

For adaptation, compatibility, aggregation, or ownership moves, walk one representative input to the final output before choosing the edit. Include only the branch combinations that can change the contract; a compact example or reasoning note is enough. Use [contracts-and-lifecycles.md](contracts-and-lifecycles.md) for defaults, later overwrites, identity/cardinality, absence, units, versions, and failure boundaries. Do not turn this into a mandatory document for simple local changes.

Implement complex work in meaningful slices. After each meaningful stage or boundary call, and before moving to a new responsibility:

1. Read the code just written together with the next consumer
2. Confirm input source, output handoff, validation order, state changes, side effects, error category, recovery path, and diagnostic ownership
3. Check that local names and comments still describe the current behavior and that no helper or constant hides needed branch evidence
4. Recompute the change scope and reference triggers; if a new logging, exception, remote, lifecycle, parameter, or structure concern appeared, load its reference before editing that part

Do not write all stages first and postpone these checks until the final diff. A slice may contain the small statements needed to complete one responsibility, but it must leave a readable handoff to the next consumer before implementation continues. A database write followed by a remote notification, for example, is two checkpoints even if each call is one line.

If a checkpoint reveals that the requirement, data relationship, error meaning, or existing special handling was misunderstood, stop at that boundary. Report the evidence, the changed interpretation, the concrete options and impact, and ask when the remaining choice would change behavior beyond the user's approved requirements. Preserve already-correct stages and discard only conclusions invalidated by the new evidence.

The final pass is not a substitute for checkpoints. It rereads the complete changed path, verifies cross-stage invariants and final callers, runs the deterministic checker and focused tests, and records checks that could not run. For a simple change it may be the only post-edit review; for a complex change it confirms every checkpoint rather than relying on a final diff glance.

Derive meaningful expected results from the accepted contract and concrete examples, not solely by copying the implementation's current assignments into test assertions. When requirements change, update the affected expectations and dependent conclusions while preserving unaffected decisions. Discovering a related historical risk does not authorize repairing it; distinguish a proven regression from a hypothesis and explain any change required outside the agreed scope. An exclusion for one planning or commit operation does not silently become a permanent review exclusion.


## Map The Semantic Neighborhood

The symbol named in the request is an investigation starting point, not automatically the full change boundary. Before proposing, explaining, judging, or editing existing behavior, follow only the paths needed to understand:

- the trigger, relevant callers, and downstream consumers
- input sources, transformations, validation, serialization, persistence, remote calls, caches, outputs, and failure paths
- logs and error details used to diagnose the behavior
- tests, configuration, and contracts that define or preserve it
- other values that participate in the same invariant, decision, identity, state, or diagnostic event

Two fields can be semantically related without referencing each other. If field A and field B jointly determine a validation result, mapping, log event, cache key, state transition, duplicate policy, or caller-visible response, a change to A must explicitly decide whether B and their shared invariant also change. Searching only for A is not sufficient.

Keep the investigation proportional. Stop following a path when it no longer affects the requested behavior, its contract, or the evidence needed to make the decision. Explicitly requested unchanged code is in scope; unrelated historical defects are not. Do not read an entire module by default or turn context discovery into an unrequested refactor.

Before editing, identify the affected nodes that need a decision. After editing, revisit each node and confirm that it was updated or deliberately preserved with its invariant still valid.

## Explain Existing Behavior Before Changing It

For a non-obvious log field, compatibility branch, special value, ordering rule, or other legacy behavior, first seek its purpose in current callers, tests, configuration, comments, contracts, and comparable implementations. Use focused Git history only when current evidence cannot explain why the behavior exists and changing it could alter results, compatibility, lifecycle guarantees, or diagnostic capability.

Treat logs as diagnostic behavior rather than decoration. Before adding, removing, or changing logged fields, identify the failure or investigation scenario, how the fields correlate to locate it, which layer owns the record, and whether the resulting event still supports that investigation. A request that names field A does not justify dropping or ignoring field B when both fields make the event understandable.

If the purpose remains unknown and materially different changes are possible, pause before editing. State the evidence inspected, the exact unresolved relationship, the concrete options and effects, and a recommendation. Do not ask broad questions such as "What is the business logic here?"

## Trace Important Business Changes And Results

During planning and at meaningful stage checkpoints, ask whether the permitted evidence can explain which inputs and rules produced an important result, what changed, and where a failure occurred. Apply this to ordinary business processing as well as integrations: parameter overrides, mapping or calculations, rule selection, state transitions, automatic repair, and validation failures. Missing logs in the current implementation are not a reason to skip the assessment. Add diagnostics for a concrete evidence gap; do not log every assignment, getter, loop item, or pure conversion merely because it has input and output.

Choose fields for the actual investigation, following the repository's logging entry point, event format, levels, production enablement, and owning layer:

- overrides and repairs: the business identifier, relevant prior and resulting values, and the reason or selected source
- calculations, mapping, and rule selection: the inputs that determine the outcome, the applied rule when it can vary, and the actual result
- state transitions: the prior state, triggering decision, and the outcome at the boundary that was actually reached
- failed validation: the affected object, relevant actual value and expected condition, and the specific failure reason

Capture prior values before mutation. A second reference to the same mutable object, or a shallow copy whose nested values later change, is not a reliable before snapshot. Capture the necessary stable scalar values or a suitably isolated representation within the agreed logging scope; do not deep-copy whole objects by default. For asynchronous or deferred logging, ensure later mutation cannot rewrite either recorded snapshot. Preparing diagnostics must not trigger extra business reads, alter evaluation order, or change transaction/failure behavior merely to obtain log fields. A pre-write value is only the value this operation observed; do not claim a global or atomically verified prior state without that guarantee.

Distinguish intended values, in-memory results, attempted operations, confirmed outcomes, and committed state. Setting a request field does not mean the request was sent; a successful repository call inside a transaction does not prove the transaction committed; a timeout does not prove a remote write failed. Label the observed stage accurately and preserve failure evidence when the success path is not reached. If a completion record is required, use the existing lifecycle owner rather than inventing a success claim or a new transaction/logging framework.

Keep records attributable to the same operation and, where applicable, the same retry attempt. Reuse an existing trace or business identifier with sufficient scope; do not assume an order ID distinguishes concurrent attempts. One change event can contain before/after values, or correlated records can show inputs and results. Reuse existing diagnostics or retained evidence when they already cover the need; do not require paired logs or duplicate complete infrastructure. Keep the real state write visible and use the existing stage-comment rules for a substantial diagnostic block. Do not introduce distant null variables or an outer `finally` solely to assemble a summary; see [method-design.md](method-design.md) when such scaffolding appears.

Recording scope remains a repository/user decision. Reuse confirmed policies for fields, payload size, level, access, masking, and retention; this preference authorizes neither arbitrary full objects nor a universal masking requirement. When scope is unresolved, show the needed fields, risks, and relevant choices, then ask before broadening logs. Reuse [project-guidance.md](project-guidance.md) only for applicable hints and [remote-calls.md](remote-calls.md) when a remote boundary is involved. Consider record volume and hot paths; a bounded record at the responsible boundary may explain the outcome better than per-item logging.

Verify changed diagnostics against representative success and failure paths. When snapshot timing, correlation, or outcome labels matter, use log capture or inspect the actual logging path; tests that assert only business results do not prove those properties. Logs help investigation and observation but do not replace validation, assertions, or tests of input/output correctness. Missing necessary diagnostic evidence or false success claims are normally `P2` when they materially mislead investigation; a preference for additional harmless detail is not automatically a finding.

## Classify Evidence

Do not treat every nearby example as a project rule. Classify what supports a decision:

- **authority**: explicit user and repository instructions, published API or schema contracts, compatibility commitments, and approved product decisions
- **observed behavior**: current source, executable tests, configuration, call paths, generated output, and reproducible tool results
- **external contract**: official protocol, provider, framework, or dependency documentation confirmed for the version in use
- **local convention**: repeated nearby patterns that are consistent but not declared as a contract
- **local guidance**: deliberately recorded `.codex/project-guidance.md` hints that reduce repeated discovery but remain below current repository evidence
- **recommendation**: a Skill default or engineering preference used when stronger evidence does not decide the issue

Authority defines intended constraints; observed behavior establishes what the system currently does. Existing behavior does not veto an explicit approved change. Surface unresolved conflicts between authoritative requirements or newly discovered compatibility obligations and explain their impact; do not ask again merely because the old code or tests describe the previous behavior. Tests may preserve a bug, source may violate a published contract, and a common local pattern may still be unsafe.

Before adding a configuration option, default threshold, account-selection rule, or duplicated validation, establish why this boundary needs it and whether an existing owner already supplies it. A nearby implementation is a comparison point, not proof that its identity, scope, failure contract, or time budget fits this call. Separate the need for a new option from the repository rule for where such an option belongs; a required configuration class is not itself needless abstraction. Explain consequential unverified defaults and ask only when the remaining choice changes behavior beyond approved requirements.

When applying a rule, state material evidence in the reasoning or finding. Do not present local guidance or a recommendation as an existing repository standard. Local guidance may direct targeted verification and may beat a generic recommendation when stronger evidence is silent, but it cannot create a finding by itself. Examples illustrate a rule; they do not create a universal ban.

## Decide Under Uncertainty

Resolve low-risk, reversible readability choices using the Skill default and the surrounding style, and disclose a consequential assumption in the result. Ask the user only when missing or conflicting evidence leaves materially different outcomes, including:

- public API, persistence, event, or error-contract compatibility
- authorization, privacy, disclosure, data-loss, or irreversible side effects
- transaction, retry, idempotency, compensation, or resource ownership
- third-party error mapping, logging scope, or loss of diagnostic capability
- the meaning or relationship of data that drives validation, mapping, state, persistence, or output
- a new cross-cutting abstraction or architectural boundary

Before asking, report the evidence found, the unresolved decision, the concrete options, their costs, and a recommendation. If an established extension point or contract already resolves the choice, follow it without pausing.

Report a missed semantic relationship according to its actual effect: likely incorrect behavior or a broken contract is `P1` or `P2` depending on certainty and impact, loss of material diagnostic capability is normally `P2`, and unnecessary navigation or local understanding cost is `P3`.

## Keep Diagnosis And Verification Claims Bounded

Distinguish a defect that exists in code, a plausible failure path, and evidence that this incident followed that path. Matching elapsed time or a nearby success log cannot by itself establish causality. State the observed facts, missing link, and a focused check that could distinguish alternatives. A missing branch log does not by itself prove either that the branch ran or that it did not. Identify existing defects as existing; investigate them only when relevant to the task, without silently expanding a repair into unrelated history.

Map verification claims to what actually executed. Tests that mock token acquisition can verify the adapter's handling of a token or exception, but cannot prove real cache, lock, or refresh behavior. Tests that assert an HTTP body or returned error do not establish log coverage unless they inspect the diagnostic path. Report compilation, deterministic style, contract tests, semantic review, and unverified integration behavior separately when the distinction matters. Preserve useful test evidence without turning a pass count into a blanket quality conclusion.

## Read Back The Final State

The code produced by an edit is provisional until later tools finish. Formatters, code generators, test repairs, IDE actions, Git hooks, and external tools can alter code, filenames, comments, imports, or generated contracts after an earlier review.

After the last mutating tool for the task:

1. reread repository status, the final task-owned diff, and every affected file whose behavior or documentation matters
2. include task-owned renamed, staged, and untracked files; validate affected generated outputs or contracts when relevant, without turning generated files into style-review targets
3. recompute reference triggers when the final code introduces a helper, exception, remote call, lifecycle boundary, control-flow change, or other routed concern
4. rerun checks invalidated by the final changes, including compilation, focused tests, and the deterministic style checker where applicable
5. distinguish checks that passed from checks that did not run, could not start, or observed only part of the final surface

Do not claim success from the intended patch, an earlier diff, stale test output, or a hook's exit code alone. If a commit or other tool rewrites files, read back the resulting files and metadata before reporting the outcome. Any later change invalidates the earlier verification for the affected surface.

## Semantic Evaluation

The deterministic checker proves only its documented rules. Use the cases under `evals/` to forward-test whether an agent makes the required semantic decisions without requiring exact wording. A case passes only when all expected decisions are present, no disallowed decision is made, and the answer stays within the stated scope.

Do not describe structural validation of the case file as proof that model behavior passed. Behavioral confidence requires running the cases with a fresh evaluator or manually reviewing the resulting decisions.
