---
name: java-code-design-and-development
description: Plan, analyze, implement, or review specific Java backend code with scoped quality checks and progressive references
---

# Java 代码设计与开发

One entry for scoped Java backend production/test code and proposed implementations. Six concerns share one workflow with selective references. Generic Java questions and unrelated document work do not trigger it.

## Scope And Authority

User/repository rules take precedence. Source establishes observed behavior, not intended requirements. Preserve accepted decisions across modes; distinguish facts, requirements, proposals, and assumptions. Planning/analysis/review are read-only unless edits are authorized.

Explicit existing-code targets are in scope without a diff. Implementation/diff review cover task-owned staged, unstaged, untracked changes or selected files/ranges/commits/branches. Collaborators supply context; exclude unrelated history, generated, vendored, and third-party code from findings and cleanup.

## Six Quality Concerns

Apply relevant concerns together:

1. **Change basis (改动依据).** Inspect triggers, callers, data, configuration, tests, and special handling before deciding or editing. Derive expected outcomes from accepted requirements/examples. Do not invent limits, defaults, or business reasons. Investigate first; ask about material unresolved choices and pause dependent work.
2. **Business behavior (业务行为).** Preserve caller-visible behavior unless change is authorized; update affected callers/tests. Trace related fields through validation, mapping, serialization, storage, remote calls, caches, logs, errors, and outputs. Check relevant absence/defaults, identity/cardinality, duplicates, units, versions, final assignments, and failures.
3. **Readability and maintenance (理解与维护).** Expose subject, action, result, parameters, and effects at calls. Compare helpers, constants, callbacks, and types by reading and maintenance cost, not counts. Do not hide I/O, mutation, fallback, or lifecycle changes as pure calculation.
4. **Useful documentation (有效注释).** Explain caller-needed contracts and hidden stage intent with accurate, evidence-backed comments. Distinguish state writes from substantial diagnostic stages. Explain hidden catch policy; obvious statements, clear rethrows/conversions need no redundant prose. Counts prompt review, not filler.
5. **Understandable and diagnosable failure (失败与排障).** Align code/type, message, reason, and recovery. Preserve permitted inputs, changes, results, causes, and correlation. Distinguish provider business, protocol, parsing, and transport failures; retain provider evidence. Follow logging/disclosure contracts; do not invent mappings.
6. **Execution reliability and verification (执行可靠性与验证).** Check ownership/order for state, transactions, cross-store work, caches, retries, compensation, locks, and resources. Assess relevant workload/security risks. Test accepted behavior, states, and failures; reread after mutating tools. Identify relevant rollout/compatibility conditions without authorizing deployment.

PRD discovery, Git operations, and release/approval execution retain their workflows. Consume confirmed decisions and assess code consequences without assuming another Skill is available or granting release approval.

## Rule Strength

- **Requirements:** uphold accepted contracts, correctness, ownership, diagnostics, and truthful verification. Findings need evidence and impact.
- **Judgment:** compare methods, comments, names, types, and flow in context. Valid designs may remain; requested improvements are not proof of defects.
- **Preferences:** absent stronger project/user rules, prefer comments without Chinese/English full stops, one blank line between methods, braced control bodies, helpful List/Set/Map suffixes, familiar precise words, readable value choices, and wrapping within project limits. Project formatter, AGENTS.md, formal docs, and user choices prevail. Optional preferences are suggestions; applicable style violations are at most P3.

The checker detects patterns, not rule authority or business correctness. Use advisory mode by default, inspect every candidate, and enforce only explicitly binding mechanical rules; read checker.md before selecting enforcement. Exit 0 may include advisory candidates.

## Apply Across The Task

Infer the mode from the request. Read task-modes.md for planning/analysis, unclear scope, acceptance, delivery impact, or maintenance feedback; its lifecycle table requires no document set.

Before Java edits, inspect context and load all matching references. Simple edits need precheck/final checks; multi-stage, I/O, state, error, diagnostic, transaction, async, retry, or lifecycle changes need stage checkpoints under evidence-and-verification.md. Recompute scope/routes as concerns appear; refresh affected conclusions, preserving accepted intent.

After the last Java-changing tool, reread changed methods/final diff, check applicable rules, run the checker and appropriate tests, and report limits. Without edits, run focused checks only when useful; current-code tests do not validate unwritten plans.

Structure advice creates no findings. For real variation in planning/implementation or requested analysis, explain material new interfaces/classes or flow reorganization; obtain a choice unless selected already. Reuse established extensions; pure review skips this advisory.

## Git Baseline And Project Hints

Reuse Git local/freshness; do not repeat remote checks. Check hints against HEAD, later commits, and worktree. Refresh needs confirmed freshness, HEAD equal to/descending from local, and committed relevant infrastructure; see the reference for missing handoffs/history.

In confirmed worktrees, read project-guidance.md for relevant facility/style hints. Any mode reads related sections; only implementation offers initialization/refresh, once unless authorized. Routine formatting, renames, comments, local branches, and CRUD do not initialize hints. Hints are not authority or cached code facts; masking is not automatically mandatory.

## Reference Routing

Read complete relevant sections before decisions/edits; previews are not coverage. References own details; entry/README provide navigation. Skip unrelated concerns:

- [task-modes.md](references/task-modes.md): task boundaries and lifecycle handoffs as above
- [evidence-and-verification.md](references/evidence-and-verification.md): existing behavior, related fields, new restrictions/defaults, diagnostics, quality evidence, acceptance, or file-rewriting tools
- [contracts-and-lifecycles.md](references/contracts-and-lifecycles.md): multi-stage contracts/results, transactions, cross-store/async work, retries, caches, compensation, locks, or resources
- [method-design.md](references/method-design.md): helpers, compact fields/constants, wrappers, diagnostic scaffolding, callbacks, deferred work, parameters, types, placement, or granularity
- [naming.md](references/naming.md): vague/unfamiliar words, state/collection names, enum lookups, renames, or unclear responsibility
- [control-flow.md](references/control-flow.md): ternaries, branches, repeated decisions, structural literals, loops, braces, or long expressions
- [comments-and-javadoc.md](references/comments-and-javadoc.md): class/method/doc edits, documentation or stage-coverage analysis, or planned independent actions/hidden contracts; no missing-comment defects in unwritten code
- [exception-communication.md](references/exception-communication.md): failure messages/logs, catch/finally, exception conversion, or error mapping
- [remote-calls.md](references/remote-calls.md): HTTP, Feign, RPC, external SDK, logging, parsing, mapping, or provider failures
- [structure-choice.md](references/structure-choice.md): conditional structure advisory as above
- [project-guidance.md](references/project-guidance.md): relevant local project hints as above
- [checker.md](references/checker.md): enforcement selection, advanced scope, CLI behavior/errors, or rule identifiers

## Findings And Completion

Distinguish evidenced defects, unverified risks, and optional improvements. Grade actual conditions, reach, and impact: P0 for critical widespread urgent harm; P1 for likely wrong behavior, leaks, or broken contracts; P2 for hidden semantics, misleading recovery, unsafe disclosure or maintenance; P3 for concrete local clarity or applicable style issues.

Briefly report relevant checks, actual evidence/tests, and material gaps; simple work needs no six-part checklist. Distinguish compilation, style, semantic review, and integration evidence when limits matter. Valid evals JSON checks structure, not model behavior. Git state, checker exit, counts, and planned tests do not prove completion.
