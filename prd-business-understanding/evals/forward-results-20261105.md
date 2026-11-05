# Targeted forward test — 2026-11-05

The five new cases in [semantic-cases.json](semantic-cases.json) were evaluated in isolated Codex subagents using the session's default model, without a model override. Each agent read the Skill, the simulated user request and raw fixture only. Expected/disallowed assertions and prior review conclusions were withheld. Follow-ups were delivered separately in the same conversation; the main agent judged decisions by meaning. No agent was permitted to edit real application files or use user-question tools.

## Observed outcomes

| Case | Turns | Result and evidence |
| --- | ---: | --- |
| investigate-without-expanding-edit-scope | 2 | Passed. Distinguished the preserved input list from first-alias echo; after implementation permission, retained the exclusion of eligibility and calculation changes. |
| trace-field-conditions-and-final-overwrites | 2 | Passed. Identified the actual gateway DTO's missing field, conditional productCode fallback, serviceCode-based matching and the lookup's retained failure dependency. The follow-up correctly returned supplied P instead of asserting N. |
| update-decisions-without-losing-unaffected-contracts | 3 | Passed after refinement. Reconciled the sample, carried accepted carrier/pricing/field rules through two updates, mapped response and regression effects, and flagged duplicate conversion and expanded failure scope before migration. |
| shared-optional-data-preserves-failure-contract | 2 | Passed. Recommended removing the accidental mandatory-marker policy instead of inventing a query flag, preserved RPC failure, and rejected zero-price and authorization assumptions in the follow-up. |
| internal-design-without-extra-approval-ceremony | 2 | Passed. Proposed one responsibility-based adapter and explicit return data, reused boundary logs, and continued without requesting helper-by-helper approval. |

## Response evidence

**Scope.** The first answer explained that A and B remained in the input while the response intentionally echoed A. It described the eligibility mismatch as unverified. After the follow-up, it retained “现有准入、测算去重、报价数量和首别名还原逻辑”.

**Field adaptation.** The evaluator distinguished calculation output from gateway display output. It noted that a lookup whose output is overwritten still has the accepted RPC failure effect. For the follow-up it answered: “调用方传了非空 P，就返回 P；未传或空白才返回 N”. It did not claim multiple aliases alone proved lost input or a defect.

**Shared API.** The evaluator identified `marker == null` throwing an exception as the new failure condition, while absent optional data should preserve the result. After the colleague's follow-up suggestion, it stated that omission did not establish a permission failure, null was not zero, and RPC failure still failed the whole request.

**Internal design.** The proposed shared adapter reduced duplicated pure logic without new public endpoints, locks or persistence. It reused existing request/response logs and added only the configuration used. On implementation permission it continued without new approval and explicitly said the simulation had not modified files or run application tests.

**Changing decisions.** The final run first treated the product sample as unaccepted evidence. On confirmation it replaced only the fusion output rule and named regressions for both final codes, carrier, prices/fees, ALL/ordinary requests and RPC failure. The last follow-up retained “打标只改 productCode、保留 serviceCode” and the fixed fusion output, while retiring the ordinary-code exclusion. It correctly distinguished a duplicate lookup from safe migration and raised the unresolved consumer scope rather than reopening the settled field semantics.

## Refinement during evaluation

The first requirement-update run carried decisions forward but omitted concrete affected output stages and regression scenarios. The Skill was refined to require a lightweight impact mapping even when edits are deferred; the fixture was expanded with raw gateway assembly code.

A subsequent run produced the impact mapping, but its final follow-up reopened which field a marker writes after scenario scope expanded. The fixture now explicitly states the accepted marker field contract, and the Skill clarifies that scenario expansion alone does not reset settled field or failure semantics. A fresh three-turn run passed on this final revision. These earlier diagnostic runs are not counted as passing runs.

The five passing case sequences total 11 turns. The four other sequences did not depend on the requirement-update sentence refined during this run; the full changed requirement-update sequence was rerun from a fresh context.

## Deterministic checks and limits

- Skill Creator `quick_validate.py`: passed.
- Catalog validator: 23 cases valid, including 5 multi-turn cases and 6 follow-ups.
- Validator unit tests: 8 tests passed, covering schema 1 compatibility, schema 2 follow-ups, malformed versions/turns and CLI outcomes.
- The other 18 behavioral cases were not rerun with models in this task.

These are targeted text-only decision tests, not business-system integration or code-execution tests. They do not establish performance across all conversations or prove production compatibility. The deterministic tests validate the catalog tool, not model behavior.
