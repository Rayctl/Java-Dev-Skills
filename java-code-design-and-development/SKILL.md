---
name: java-code-design-and-development
description: Plan, analyze, implement, or review specific Java backend code with scoped quality checks and progressive references
---

# Java 代码设计与开发

Use for concrete Java backend production/test code or proposed implementations. Generic Java questions and unrelated document work do not trigger it.

## Scope And Authority

Repository/user rules take precedence. Use current contracts and evidence; local patterns and Skill preferences are not project facts.

Explicitly requested existing code is in scope without a diff. Implementation/diff review cover task-owned staged, unstaged, and untracked changes or selected files, ranges, commits, or branches. Collaborators supply context. Exclude unrelated history, generated, vendored, and third-party code from findings.

## Task Modes

Infer the mode; preserve approved requirements, decisions, and scope across modes. Planning, analysis, and review do not authorize edits.

| Mode | Purpose |
| --- | --- |
| Planning | Assess contracts, responsibilities, failure paths, complexity, and verification |
| Analysis | Explain behavior or assess requested improvements with evidence and tradeoffs |
| Implementation | Authorized edits with prechecks, stage checkpoints, and final verification |
| Review | Assess selected code/diff and report evidenced findings |

Read [task-modes.md](references/task-modes.md) for planning/analysis or unclear scope/verification. Inspect the semantic neighborhood. Simple edits need precheck/final checks; multi-stage, I/O, state, error, diagnostic, transaction, async, retry, or lifecycle boundaries need implementation checkpoints. Recompute scope/references as concerns appear; ask only about material unresolved choices.

## Git Baseline And Project Hints

Reuse Git's `local`/freshness; do not repeat remote checks. Check hints against current HEAD, later commits, and worktree. Refresh needs confirmed freshness, HEAD descending from/equal to `local`, and committed relevant infrastructure; see the reference for missing handoffs/history.

In confirmed worktrees, read [project-guidance.md](references/project-guidance.md) for relevant project logging, utilities, remote calls, exceptions, build, or style hints. Any mode may read existing sections; only implementation offers initialization/refresh, once unless authorized. Masking is not automatically mandatory. Routine formatting, renames, comments, local branches, and CRUD do not initialize hints.

## Reference Routing

Load references for the scoped concern before deciding, assessing, or editing; do not route by unrelated collaborators:

- [method-design.md](references/method-design.md): helpers, compact fields or constants, wrappers, diagnostic scaffolding, deferred work, parameter meaning, new or edited nested types, or method granularity
- [structure-choice.md](references/structure-choice.md): real variation during planning/implementation, or explicitly requested structural optimization in analysis; no unsolicited pattern-selection exercise in review
- [comments-and-javadoc.md](references/comments-and-javadoc.md): Java class/method/doc edits, requested documentation/stage-coverage analysis, or planning independent actions and hidden contracts; no comment defects in unwritten code
- [naming.md](references/naming.md): vague or unfamiliar words, state/collection names, enum lookups, renames, `normalize`, or unclear responsibility
- [exception-communication.md](references/exception-communication.md): failure messages, failure logs, `catch`, `finally`, or error mapping under assessment
- [remote-calls.md](references/remote-calls.md): HTTP, Feign, RPC, external SDK, or their logging, response parsing, error mapping, and provider failures
- [contracts-and-lifecycles.md](references/contracts-and-lifecycles.md): multi-stage contracts, correlated results, transactions, cross-store/async work, retries, caches, compensation, locks, resources, or failure policy
- [control-flow.md](references/control-flow.md): ternaries, branches, repeated decisions, structural literals, loops, braces, or long expressions
- [evidence-and-verification.md](references/evidence-and-verification.md): existing behavior/data, related fields, business diagnostics, legacy logic, evidence conflicts, or file-rewriting tools
- [checker.md](references/checker.md): advanced scope, exact CLI behavior, errors, or rule identifiers

## Quality Gates

Apply these quality gates to the scoped code or proposed behavior; distinguish current defects from proposed risks:

- preserve caller-visible semantics the task does not authorize changing; implement approved behavior changes and update affected callers and tests rather than treating old code as the specification
- make names and call sites reveal the subject, action, result, parameter meaning, and meaningful side effects; expose collection key/cardinality and duplicate policy
- trace related values through validation, mapping, serialization, persistence, remote calls, caches, logs, errors, and outputs; preserve permitted evidence of key inputs, changes, and results needed for diagnosis
- assign clear owners and safe ordering for validation, state transitions, persistence, cleanup, delayed work, retries, compensation, and resources
- do not hide meaningful I/O, mutation, fallback, retry, compensation, cleanup, or lifecycle changes inside an apparently pure calculation
- document independent public or application-defined business actions and hidden stage contracts with plain, evidence-backed intent comments; keep primary state writes and diagnostic stages distinguishable while preserving audit and failure order, without annotating obvious adjacent one-line logs
- compare short helpers, fields, and constants with writing them at use sites; reuse count, JavaDoc, or a clear name alone does not justify extraction
- comment behavior-changing `catch` branches before fallback, degradation, retry, suppression, continuation, compensation, or exception conversion; transparent direct rethrows are exempt
- keep error code, exception type, message, actual failure reason, and effective recovery action aligned
- distinguish third-party business rejection, protocol failure, parse failure, and transport failure while preserving useful provider diagnostics; do not invent mappings or disclosure policy without evidence
- after Java edits, run the deterministic checker, appropriate tests, and final-state readback after the last file-changing tool; without edits, select checks only when they answer the task's question

These are default coding preferences, subordinate to project formatter, `AGENTS.md`, formal documentation, and explicit user rules:

- comments do not end with Chinese or English full stops
- exactly one blank line separates method declarations
- control-flow bodies use braces
- collection variables expose `List`, `Set`, or `Map` where that improves call-site reading
- prefer familiar, precise words in names
- use braced `if` for dense ternaries and wrap lines for project limits and scanability
- prefer direct values or independent types over nested classes, local classes, and nested enums unless nesting clearly improves cohesion or satisfies a contract

A preference-only violation is at most `P3`; behavioral, lifecycle, diagnostic, security, or maintenance risks follow actual impact. Stronger repository evidence prevails.

## Structure Advisory

Compare direct and structured options for real variation. This advisory creates no findings. Explain material interfaces, class families, or flow reorganization; obtain a choice before implementing unless already selected. Read-only comparison needs no approval; review skips the advisory.

## Verification And Findings

Test changed input, output, absence, failure, and state semantics during implementation. Follow [evidence-and-verification.md](references/evidence-and-verification.md); reread final files/diff and rerun invalidated checks after mutating tools. Read the whole scoped path and assess diagnostics in every mode. Separate evidence, inference, optional improvements, and risks. Plans propose verification; analysis/review report executed checks and mock/integration limits.

Findings require evidenced violations or concrete problems, not another valid design or a requested improvement. Use `P0` for data loss, security exposure, or system-wide outage; `P1` for likely wrong behavior, leaks, or broken contracts; `P2` for hidden semantics, misleading recovery, unsafe disclosure/maintenance; `P3` for local clarity or style. Recheck scope, callers, names, methods, JavaDoc, stages, catches, errors, diagnostics, remote/lifecycle rules, applicable tests/checker, and residual risks.

Valid `evals/` JSON is not behavioral validation. Semantic decisions, prose, naming, structure, and diagnostic policy require Skill review, beyond the checker.
