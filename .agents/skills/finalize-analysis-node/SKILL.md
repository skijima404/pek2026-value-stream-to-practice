---
name: finalize-analysis-node
description: Finalize one or more repository Observation, Hypothesis Episode, or Pattern nodes after explicit human intent review by rechecking publication safety, recording reviewed metadata, preserving epistemic and validation state, synchronizing the analysis index, and validating the repository. Use when the user says an analysis node is reviewed, asks to finalize or finish an OBS/HYP/PAT node, confirms that derived wording matches their intent, or requests data-cleansing checks before marking analysis reviewed.
---

# Finalize Analysis Node

Read the required `00_meta/` contracts in the order defined by `AGENTS.md` before
editing. This skill does not finalize Raw Notes; use `$finalize-raw-note` for them.

## Preconditions

- Resolve exactly the node IDs explicitly confirmed by the human.
- Require an explicit human statement that the node represents their intended
  meaning. Agent review, validation, Git authorship, and publication-safety review
  are not substitutes.
- If the human requests a meaning-changing correction, apply it but keep the node
  `proposed` until the corrected meaning is explicitly confirmed.
- Accept `observation`, `hypothesis_episode`, and `pattern` only. Refuse Raw Notes,
  External Inputs, Artifacts, rejected nodes, and superseded nodes.

## Workflow

1. Inspect Git status and history without printing sensitive values.
2. Read each target and every source node needed to assess its composed meaning.
3. Confirm that relations use canonical types and point to existing node IDs.
4. Preserve `confidence`, `hypothesis_level`, validation method, and result.
   Human intent review does not change `not_tested` or establish factual validity.
5. Review the complete node for customer, project, personal, commercial,
   internal-system, credential, and combined re-identification information.
6. If sensitive content exists in a committed revision, stop and report that Git
   history remediation is required without repeating the value.
7. Sanitize an uncommitted node when needed. If sanitization changes meaning, obtain
   fresh human intent confirmation before continuing.
8. Run the bundled script for each confirmed node:

   ```bash
   python3 .agents/skills/finalize-analysis-node/scripts/finalize_analysis_node.py \
     <path> --reviewed-by human:<id> \
     --sanitization-result <not_needed|sanitized>
   ```

   The script is idempotent. A complete, already-reviewed node remains unchanged.
9. Synchronize status, confidence, result, title, and relations in
   `02_analysis/README.md`. Do not add new interpretation to the index.
10. Run `python3 scripts/validate_repository.py` and `git diff --check`.

## Safety and Epistemic Boundaries

- `status: reviewed` means intent alignment only.
- Never change an analysis node to `accepted`.
- Never adopt content into `03_artifacts/` during this workflow.
- Never convert planned validation into a completed result.
- Never raise confidence merely because a human reviewed the wording.
- Do not rename node IDs or filenames.
- Summarize removed material by category only and never repeat removed values.

## Handoff

Report finalized node IDs, reviewer, publication-safety result, preserved validation
state, index synchronization, and repository validation. If no change was needed,
state that the node was already finalized.
