# PRD Business Understanding

Use this skill for PRD-driven planning and implementation. It helps establish old behavior, requested changes, compatibility, and unresolved business decisions, then explains behavior-changing code in context.

Use the user's wording to select the working mode: a clear request to discuss or align the requirement means 一起梳理业务; a clear request for an implementation plan means 直接规划. Ask only when the intent is genuinely ambiguous. Answer narrow questions about current behavior with evidence even before giving a plan.

Before proposing a material decision, inspect current code, tests and formal contracts, and trace the affected entry points. Separate verified facts, accepted requirements, proposed solutions and unresolved decisions. Investigation may extend beyond edit scope: conditional risks do not automatically become defects to repair. Preserve accepted behavior and contracts; confirm unresolved changes to business policy or external guarantees. Internal helpers and responsibility-based extraction within that scope do not need a separate approval.

For the affected scenarios, map current behavior, requested change, compatibility, open decisions and verification. Keep important terms such as order, shipment, package and successful purchase request consistent with the observed counting unit. AI authorship alone neither invalidates nor verifies a PRD statement. When authoritative evidence settles a current-state fact, note the discrepancy and proceed from that evidence. Ask one focused question at a time only for material decisions evidence cannot settle, and continue unaffected work.

For cross-service adaptation, trace actual caller fields, defaults, matching and final overwrites rather than assuming a name has one meaning everywhere. When decisions change, say what they supersede and update affected code and verification while retaining unaffected decisions. Shared APIs must keep existing callers' failure behavior when optional data is added. Prefer existing contracts and collaborators, explicit return data and the observations needed for the decision over extra layers, mutable output parameters or repeated queries.

During implementation, explain only business-significant changes. Finish with a short mapping from scenarios to changed locations and verification. The skill does not apply to unrelated work or replace existing brainstorming, planning, or code-quality skills.

## Install

PowerShell:

    Copy-Item -Recurse -Force ".\prd-business-understanding" "$env:USERPROFILE\.codex\skills"

Git Bash:

    cp -R ./prd-business-understanding "$HOME/.codex/skills/"

The skill entrypoint is ~/.codex/skills/prd-business-understanding/SKILL.md.

## Semantic evaluation

The evals/semantic-cases.json catalog includes single-turn cases and ordered follow-ups for scope, field adaptation, evolving requirements, shared API behavior and internal design. Use a clean conversation for each case and deliver follow-ups one at a time. See [evals/README.md](evals/README.md) for the procedure and recorded forward-test evidence.

The catalog validator checks structure only. Passing it or Skill Creator's quick_validate.py does not demonstrate model behavior; behavioral evaluation requires running the cases with a model and reviewing its responses.
