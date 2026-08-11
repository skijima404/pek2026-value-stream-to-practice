---
name: finalize-analysis-node
description: Finalize persisted repository Observation, Hypothesis Episode, or Pattern nodes after explicit human intent review by rechecking publication safety, recording reviewed metadata, preserving epistemic and validation state, regenerating analysis projections, and validating the repository. Use only when a later human message confirms the saved content of an exact existing OBS/HYP/PAT node ID or link. Do not use for permission to create, update, record, sanitize, or proceed; approval of a proposed outline before persistence; or the same assistant turn that saved or meaningfully changed the node.
---

# Finalize Analysis Node

Read the required `00_meta/` contracts in the order defined by `AGENTS.md` before
editing. This skill does not finalize Raw Notes; use `$finalize-raw-note` for them.

## Preconditions

- Resolve exactly the persisted node IDs or links previously handed off and now
  explicitly confirmed by the human.
- Require a later human message, after that handoff, stating that the saved node
  represents their intended meaning. Permission to create, update, sanitize,
  record, or proceed is not review. Agent review, validation, Git authorship, and
  publication-safety review are not substitutes.
- Never create, meaningfully update, sanitize with wording changes, and finalize
  the same node in one assistant turn. If the chronology cannot be established,
  keep the node `proposed`, hand off its exact ID or link, and stop.
- If the human requests a meaning-changing correction, apply it but keep the node
  `proposed`, hand off the corrected node, and wait for a later explicit review.
- Accept `observation`, `hypothesis_episode`, and `pattern` only. Refuse Raw Notes,
  External Inputs, Artifacts, rejected nodes, and superseded nodes.

## Workflow

1. Inspect Git status and history without printing sensitive values.
2. Read each target and every source node needed to assess its composed meaning.
3. Confirm that relations use canonical types and point to existing node IDs.
4. Preserve `knowledge_basis`, `confidence`, `hypothesis_level`, the lightweight
   validation approach, disposition, and result, and any Extended Validation
   Component Coverage, Finding, Applicability, and residual uncertainty. Human
   intent review does not change `not_tested` or establish factual validity.
   Confirm that `knowledge_basis` reflects the cited sources without inferring
   experience scope, case counts, or validation.
5. Review the complete node for customer, project, personal, commercial,
   internal-system, credential, and combined re-identification information.
6. If sensitive content exists in a committed revision, stop and report that Git
   history remediation is required without repeating the value.
7. Sanitize an uncommitted node when needed. If sanitization changes wording or
   meaning, keep it `proposed`, hand off the persisted result, and stop. A later
   human message must confirm the sanitized content before finalization.
8. Run the bundled script for each confirmed node:

   ```bash
   python3 .agents/skills/finalize-analysis-node/scripts/finalize_analysis_node.py \
     <path> --confirmed-persisted-id <OBS|HYP|PAT-ID> \
     --reviewed-by human:<id> \
     --sanitization-result <not_needed|sanitized> \
     [--human-confirmed-after-sanitization]
   ```

   Include `--human-confirmed-after-sanitization` only when a later human
   message explicitly confirmed the already-persisted sanitized wording. Never
   use the flag for confirmation that preceded sanitization.

   The script is idempotent. A complete, already-reviewed node remains unchanged.
9. Run `python3 scripts/generate_analysis_views.py`. Do not edit generated
   projections directly.
10. Run `python3 scripts/validate_repository.py` and `git diff --check`.

## Safety and Epistemic Boundaries

- `status: reviewed` means intent alignment only.
- Never change an analysis node to `accepted`.
- Never adopt content into `03_artifacts/` during this workflow.
- Never convert planned validation into a completed result.
- Never raise confidence merely because a human reviewed the wording.
- Never create a Risk Decision or convert a human risk response into Evidence,
  a component Finding, a hypothesis result, or Artifact adoption.
- Never remove `practitioner_experience` merely because independent validation is
  unavailable, and never convert it into `explicit_validation` during finalization.
- Do not rename node IDs or filenames.
- Summarize removed material by category only and never repeat removed values.

## Handoff

Report finalized node IDs, reviewer, publication-safety result, preserved validation
state, projection regeneration, and repository validation. If no change was needed,
state that the node was already finalized. If later review is required, return the
exact persisted node ID and link without claiming finalization.
