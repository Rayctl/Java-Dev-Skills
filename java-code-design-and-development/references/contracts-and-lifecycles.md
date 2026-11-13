# Contracts And Lifecycles

Read when scoped code or proposed behavior coordinates multiple stages, correlated results, representation changes, side effects, resources, transactions, async work, retries, caches, compensation, concurrency-sensitive writes, or non-obvious failure policies. In planning, distinguish proposed ownership and paths from existing guarantees. For remote calls, load it only when those concerns apply; remote logging and downstream errors belong to [remote-calls.md](remote-calls.md). Skip trivial accessors, data holders, pure predicates, and mechanical edits without these concerns.

## Reconstruct The Behavior

Write down the actual stages before judging individual methods. A common shape is:

```text
entry -> resolve inputs/state -> validate -> transform -> execute side effects -> persist/publish -> respond
```

Treat consecutive calls as separate stages when they change processor responsibility, hand an intermediate result to the next operation, or introduce a different side-effect, ordering, or failure boundary. A shared receiver does not merge those stages. Inspect each stage separately; explain hidden preconditions, ordering, result use, or failure consequences at the relevant call site under [comments-and-javadoc.md](comments-and-javadoc.md). Separate hidden contracts need separate explanations; one comment can cover a cohesive shared invariant. Do not add a comment to every call merely to mark the stages. Stage checkpoints remain required even when the code needs no optional body comment

For each stage, identify:

- input ownership and null, empty, absent, disabled, and default semantics
- output contract and the next consumer
- state or configuration snapshot used
- validation owner and caller-visible failure behavior
- resource, transaction, retry, and cleanup owner
- authentication, authorization, and idempotency boundaries
- ordering constraints before irreversible side effects
- synchronous, asynchronous, and cross-module boundaries

Trace the happy path and meaningful absence, rejection, concurrency, and failure paths. Do not assume another layer enforces a contract without tracing the real call path.

## Follow Values To The Final Consumer

For a changed multi-stage contract, walk a representative concrete input through the actual caller, transformations, and final observable result. Trace related fields together: who supplies each value, whether the caller actually sets it, which default applies, which later step overwrites it, and how the next consumer uses it. A setter or similarly named DTO field does not establish the whole interface contract. Check the last effective assignment after adapters, enrichment, aggregation, and response assembly. Keep correlated identity, value, unit, detail, and status fields coherent; do not assume copying an object and replacing one field yields a valid final result.

Inspect changes in cardinality and identity. A one-value map cannot preserve every alias when several inputs resolve to one internal identity; deduplicating work does not itself define how original inputs appear in the response. Establish the permitted grouping, selection, ordering, and echo policy from the contract. Taking the first retained result also does not prove only one input was evaluated: check filtering, null/blank rules, short-circuit timing, exceptions, and side effects before changing evaluation.

Distinguish an omitted result, a null list element, a retained object with null fields, an empty collection, zero, false, and an explicit failure. Before adding fallback objects or claiming compatibility, confirm the concrete structure and which inputs qualify. A downstream omission alone cannot establish whether an item was rejected, skipped, failed, never requested, or simply produced no result. Preserve known distinctions and ask when the remaining ambiguity changes behavior; do not fabricate a reason or broaden fallback to all missing inputs.

For sorting, selecting, summing, or comparing values, verify common units, currency, time basis, precision, and grouping where relevant. Example logs with one unit are not proof of a universal guarantee. Reuse confirmed conversion or validation; do not invent a default currency, exchange rate, conversion, or rejection policy. Check that the selected value and its supporting details belong to the same result and that mutable copies do not corrupt other entries.

## Preserve Representation And Version Meaning

Identify whether a field comes from a saved snapshot, live configuration, or a derived value. Combining versions may be intentional, but requires an explicit compatible meaning; do not silently present historical fields and current properties as one consistent snapshot. First check whether the existing data owner already supplies the required information instead of reconstructing its model elsewhere.

Validate, sign, compare, or snapshot the representation the operation actually consumes. An intermediate object may differ from the final serialized request after defaults, type conversion, escaping, or encoding. Do not independently rebuild the same transformation in a script or helper to approximate unavailable final data. Reuse the correct existing stage or surface a necessary design choice.

When persistence or transport representation changes, check paired write/read paths, legacy interpretation, nested structures, key collisions, types, and caller-visible output. Claim reversibility only for supported inputs; retain format identity when needed to avoid decoding old values as a new format. Do not silently change public JSON shape to satisfy storage constraints or migrate unrelated historical data without authorization.

## Move Behavior With Its Boundaries

Before moving an operation across methods, loops, services, or layers, compare consumers, available context, invocation count, batching, ordering, catch scope, transaction scope, and deployment compatibility. A failure formerly propagated to the caller may become a swallowed per-item failure after a move, even when normal outputs match. Keep one intended owner and remove obsolete duplicate execution when migration is approved. Do not add flags or new APIs merely to contain an unnecessary failure branch introduced by the task; first reconsider that branch against the actual requirement. Preserve required safety checks and concurrency guarantees rather than removing them solely because contention seems unlikely.

## Correctness And Contracts

Check for behavior that can change caller-visible results:

- inconsistent absence contracts across layers
- branch ordering that changes the result or error
- ambiguous null, empty, disabled, absent, and default semantics
- stale or mixed state snapshots
- validation against a different state than the state eventually written
- authentication or authorization against the wrong identity or after a protected side effect
- retries, callbacks, or concurrent requests that can repeat non-idempotent work
- persistence conditions that fail to repeat concurrency-sensitive preconditions
- transaction or asynchronous boundaries that outlive state or resources they depend on
- timeout, retry, and circuit-breaker layers that multiply attempts or obscure the final failure owner

Confirm contracts from source, repository documentation, or supplied configuration. Label runtime assumptions that cannot be verified.

## Resource And Side-Effect Lifecycles

Assign each resource and delayed action to one visible owner:

- release locks and temporary resources on success, rejection, conversion failure, and unexpected exceptions
- give delayed persistence, publication, or cache candidates one final consumer
- prevent `finally` cleanup from duplicating deeper cleanup or masking the original failure
- perform admission or commit only after all required conditions succeed
- avoid holding a lock across remote I/O unless the contract explicitly requires it
- align transaction propagation with the actual unit of work
- do not let asynchronous work depend on a caller transaction or request resource that has ended
- expose compensation boundaries and crash windows when side effects cannot be atomic
- bound outbound calls and make retries consistent with idempotency

Prefer a visible acquire/use/commit-or-cancel lifecycle. Flag cleanup or compensation spread across unrelated layers when ownership becomes ambiguous.

Determine whether the current boundary owns a resource, borrows it, or transfers ownership to a later consumer. Do not close an injected client, shared connection, caller stream, or asynchronous handoff solely because it implements `AutoCloseable`. For resources this boundary actually owns, prefer try-with-resources when the project's Java version and API support it. Check acquisition and reverse close order, partial acquisition failure, and every exit path. Keep the primary failure and any suppressed close failures available for diagnosis; a throwing `finally` or replacement exception must not erase them. Closing a resource does not roll back already completed external side effects

For remote timeouts and repeated attempts, apply [remote-calls.md](remote-calls.md). A timeout does not prove that the provider rejected the request or performed no side effect

## Validation Ownership

Separate purposes before reusing a predicate: structural validity, fields required by the current consumer, permission to execute, eligibility for reuse or caching, business success, and committed state have different contracts. A globally optional field can still be required by a particular operation; a later business failure does not by itself prove earlier data is invalid. Share checks only when their subject, time, absence semantics, and failure consequence agree. Preserve an explicitly approved policy that deliberately links these decisions rather than replacing it with a generic default.

Locate one authoritative owner for each rule:

- distinguish unconditional protocol or safety checks from optional data-shape validation
- do not duplicate downstream validation unless the current layer owns a different caller-visible contract
- retain validation that protects irreversible side effects, security, cache safety, or persistence consistency
- make validation paths and messages identify the real caller-visible field or state
- keep configuration-time and runtime semantics aligned when they enforce the same rule
- when validation is non-blocking, ensure its result controls only the intended later action

Reuse mechanism separately from scenario policy. Sharing a parser, exporter, task loop, or converter does not establish that its caller-specific type whitelist, size cap, identity restriction, or failure transition applies to another entry point. Compare each consumer's accepted input, purpose, authority, and failure consequence before sharing the entire validation path. Keep genuinely common security and format checks; retain separate policies when the contracts differ. For example, a general document import may reuse a provider-result parser without inheriting that provider's supported-operation list. Verify shared behavior and, when policies differ, a case that must remain different; removing duplication alone is not proof of compatibility.

## Deep Verification

Map tests to the changed contracts and lifecycles that apply:

- null, empty, absent, disabled, invalid, and default cases
- expected fallback or degradation versus unexpected exception propagation
- retry, timeout, repeated-attempt, and idempotency behavior
- lock release, cleanup, commit, cancel, and compensation paths
- concurrent state changes enforced at the final side-effect boundary
- authentication and authorization rejection before protected work
- transaction rollback, propagation, and asynchronous boundaries
- stale references after behavior, names, or ownership move

## Sources And Applicability

[Oracle's try-with-resources tutorial](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html) explains owned-resource cleanup, close order, and suppressed exceptions. It is a JDK 8-era tutorial; verify the actual Java version and API ownership contract. [AWS's timeout and retry guidance](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/) informs the remote lifecycle checks. These sources do not require closing borrowed resources, adding retries, or claiming atomicity. Source links are background, not mandatory reading for every task
