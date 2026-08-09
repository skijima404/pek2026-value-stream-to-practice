---
name: record-risk-decision
description: Record an explicit human response to residual risk in a Hypothesis Episode validation component while preserving Evidence Coverage, findings, hypothesis results, review state, and Artifact adoption as separate axes. Use when the user asks to record risk acceptance or says to proceed with risk, investigate more, mitigate, avoid, transfer, revisit, replace, or supersede a previous residual-risk decision for a HYP component.
---

# Record Risk Decision

Read the required `00_meta/` contracts in the order defined by `AGENTS.md` before
editing. Use `templates/risk-decision.md` as the structural source.

## Preconditions

- Require an explicit human response. If the response is undecided, do not create
  a node; report the unresolved component instead.
- Resolve exactly one existing Hypothesis Episode and one stable Validation
  Component ID such as `U1`.
- Require the target component to document its residual uncertainty. Do not invent
  a residual risk, response, decision scope, rationale, condition, or review trigger.
- Resolve the human decision-maker as an explicit `human:*` identifier. Do not infer
  identity from Git authorship or platform account.

## Canonical responses

- `investigate_more`: gather additional Evidence before the affected decision.
- `mitigate`: continue only with a guardrail, limitation, or impact reduction.
- `proceed_with_risk`: knowingly continue within the declared scope and conditions.
- `avoid`: do not pursue the hypothesis, intervention, or affected scope.
- `transfer`: move management responsibility to another identified party or system.

Never use `accept` or `undecided`. `proceed_with_risk` is a decision, not Evidence,
hypothesis support, Analysis acceptance, or Artifact adoption.

## Workflow

1. Inspect Git status and the target Hypothesis Episode.
2. Read every Observation named in the component's `Evidence refs`. Preserve each
   Observation's `knowledge_basis`; do not restate experience or research as a
   stronger form of Evidence.
3. Confirm that Coverage, Finding, Applicability, and residual uncertainty are
   internally consistent. If they are not, stop and fix or report the Hypothesis
   schema issue before recording a decision.
4. Check `04_decisions/risk-decisions/` for a current decision targeting the same
   `(target_node, target_component_id)` pair.
5. Create a new `RSK-YYYYMMDD-HHMMSS-short-slug.md` from the template. Record:
   target, response, decision sufficiency, human decision-maker and time, bounded
   scope, rationale, conditions or mitigations, and review triggers.
6. Add exactly one `evaluates` relation to the Hypothesis Episode. Add `informed_by`
   only for Observation Evidence the human decision actually considered.
7. If the new decision replaces a current one, add `supersedes` to the new node,
   set the old node to `decision_status: superseded`, and add `superseded_by` from
   the old node. Never overwrite the old decision body.
8. Perform a fresh publication-safety review. Sanitize customer, project, personal,
   commercial, internal-system, credential, and combined re-identification details
   before commit without retaining removed values elsewhere.
9. Run `python3 scripts/generate_analysis_views.py`. Do not edit generated
   projections directly.
10. Run `python3 scripts/validate_repository.py` and `git diff --check`.

## Decision sufficiency

Use only the human's stated decision threshold:

- `insufficient`
- `sufficient_for_next_step`
- `sufficient_with_conditions`
- `sufficient_for_current_scope`

Decision sufficiency belongs to the Risk Decision. Never copy it into Evidence
Coverage or infer it from the number of checked components.

## Protected boundaries

- Do not change the target Hypothesis Episode's `status`, `confidence`,
  `knowledge_basis`, component Finding, Applicability, or overall `result` merely
  because a Risk Decision was made.
- Do not create or modify an Artifact during this workflow.
- Do not convert `proceed_with_risk` into `supports`.
- Do not compute a truth percentage from component counts.
- Do not renumber or reuse a component ID after a Risk Decision references it.

## Handoff

Report the Risk Decision ID, target component, response, decision sufficiency,
decision scope, whether it superseded an earlier decision, preserved hypothesis
state, publication-safety result, and repository validation result.
