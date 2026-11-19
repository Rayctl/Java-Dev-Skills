# Planning, Analysis, Implementation, And Review

Read for planning or analysis of concrete Java backend code, or when mode, scope, or verification boundaries need clarification. Determine the mode from the requested outcome; do not ask the user to select a mode when the request is clear. A mixed task can use different modes in sequence without repeating approved decisions.

## Shared Scope And Evidence

An explicitly named existing method, class, or bounded module is a valid analysis or review target even without a diff. For an implementation plan, scope includes the proposed behavior and the existing paths it would affect. For implementation or a diff review, retain the chosen change surface; unrelated unchanged collaborators remain context. If the user asks broadly for improvements, start with the identified responsibility or a small relevant path and state that coverage. Ask only when materially different scope choices would change the usefulness of the result; never silently audit the whole repository.

Inspect enough callers, collaborators, data sources, configuration, contracts, and tests to explain the decision. Use [evidence-and-verification.md](evidence-and-verification.md) when behavior, related fields, diagnostics, or conflicting evidence require semantic investigation. Source proves what exists; requirements and confirmed contracts determine what should happen. Do not manufacture a requirement from a preferred design, or replace accepted requirements with current implementation behavior.

Apply reference rules to the concern under assessment, including unchanged target code. Instructions phrased as "before/after editing" govern actual edits; they do not authorize edits or require implementation artifacts in a read-only task. A reference's use of "changed" does not exclude the explicitly requested analysis target. Do not load references merely because a dependency elsewhere contains the same construct.

## Lifecycle Handoffs

The entry's six concerns describe what to inspect; task stages determine when and with what evidence. Stages can overlap or repeat. Do not force every request through all stages or create mandatory documents, approval rounds, or six-part reports.

| Stage in the actual task | Relevant decision and evidence |
| --- | --- |
| Understand requirements | Identify accepted outcomes, allowed behavior changes, representative inputs/results, and material unknowns; distinguish current facts from intended behavior |
| Choose an approach | Compare responsibilities, data/failure flow, existing capabilities, and tradeoffs; plan verification before committing to the design |
| Implement | Use prechecks and meaningful stage checkpoints; preserve contracts and revalidate conclusions affected by new evidence |
| Test and review | Compare actual normal, boundary, failure, and compatibility behavior with accepted examples; state what mocks or unavailable environments leave unverified |
| Prepare delivery | For affected configuration, storage formats, schemas, APIs, or events, assess required defaults/migration, coexistence of versions, release order, and rollback compatibility |
| Respond to runtime feedback | Separate symptoms, plausible paths, and demonstrated causes; make a scoped repair and add a useful regression check where practical |

Use a concrete acceptance example when it resolves ambiguity, not a checklist detached from the task. For a new optional field, relevant cases may include absence, old stored data, and old callers. Do not invent desired values from the new implementation. A simple rename needs no release plan or performance investigation unless evidence shows a relevant contract.

Delivery assessment identifies code-related prerequisites and risks; it never proves deployment readiness from unit tests alone or authorizes a migration, rollout, rollback, or production access. Report unresolved compatibility or data-conversion decisions when material. Actual release checks and approvals belong to the project's delivery workflow. In an ordinary code task, surface relevant conditions without expanding into release execution.

PRD collaboration supplies accepted business decisions; Java quality checks their implementation and verification. Git collaboration governs repository operations. Reuse established decisions and handoffs rather than re-asking questions or rerunning workflows; missing optional Skills do not prevent ordinary scoped code analysis.

Read [evidence-and-verification.md](evidence-and-verification.md#quality-requirements-and-acceptance-evidence) for acceptance, workload, or security concerns. Detailed ownership, naming, documentation, failure, and lifecycle rules retain their existing reference owners.

The emphasis on small steps and feedback draws on [Fowler's refactoring guidance](https://refactoring.com/) and [The Pragmatic Programmer's public tips](https://pragprog.com/tips/). Stage names and Skill boundaries here are local organization choices, not a claim that those sources prescribe this workflow.

## Planning

Before settling on an implementation approach, check the proposed responsibility, caller-visible contract, data flow, meaningful side effects, validation and failure order, diagnostics, and applicable lifecycle ownership. Trace a representative case for multi-stage or boundary changes. Use actual evidence for existing paths; label proposed paths, assumptions, and missing evidence instead of inventing method names or guarantees.

State the approach, its business or contract basis, important tradeoffs, unresolved decisions, and how the changed behavior would be verified. Match detail to complexity; a simple local change needs no design document. Identify future documentation needs for hidden contracts without reporting missing JavaDoc or stage comments in code that has not been written. Planned tests and current-version tests do not prove the proposed implementation correct.

Resolve evidence locally first. If a remaining ambiguity changes behavior, data, failures, diagnosis, lifecycle, or architecture beyond approved decisions, explain the concrete options and impact and ask before finalizing that dependent choice. Continue independent analysis where useful.

Before proposing new required fields, local restrictions, configuration, or layers, verify their need and existing owners under [evidence-and-verification.md](evidence-and-verification.md). A recommendation is not an accepted requirement. Keep caller readiness concrete: trace where required inputs come from and how the consumer uses synchronous results, task handles, errors, or file content; compilation alone does not settle those contracts.

## Analysis

For explanation, trace the actual scoped behavior and the business reason supported by evidence. Do not force an optimization report when the user only asks how code works. For an optimization request, distinguish:

- an evidenced defect or violated requirement, with its condition and consequence
- an unverified risk, with the missing evidence or focused check
- an optional improvement, comparing the current valid approach with an alternative and its cost

Explain why leaving the code unchanged is reasonable when no concrete benefit is established. Use [structure-choice.md](structure-choice.md) only for a requested structural assessment with real variation; do not turn another valid design into a `P2`/`P3` finding. Analysis provides recommendations, not permission to rewrite source or initialize project hints.

## Implementation And Review

Implementation retains the precheck, complexity-based stage checkpoints, documentation rules, final-method/diff readback, deterministic checker, and appropriate tests. Before crossing from a read-only task into editing, confirm that the user requested or already authorized that work; no extra approval is needed when implementation is already part of the request. Reassess only conclusions invalidated by new evidence.

Review examines the selected final code or diff without editing. Findings require evidence and actual impact under the Skill's severity rules. Existing correctness, ownership, naming, documentation, method-design, and lifecycle rules still apply; do not launch an unsolicited design-pattern proposal or grade valid alternatives as defects.

## Verification By Mode

Planning, analysis, and review do not mechanically run the style checker or a full test suite. Use an explicit file/range check, focused test, or isolated reproduction only when it answers a concrete question and fits task permissions; preserve the worktree in a read-only task. Do not contact live services or change business data just to validate an idea.

Planning distinguishes proposed checks from checks already run on current code. Analysis/review state the evidence inspected, actual checks and their limits, and remaining uncertainty. Once authorized Java edits occur, the implementation's checker and final-state verification requirements apply. A clean repository, passing checker, or valid semantic-case JSON never proves business correctness or model behavior.
