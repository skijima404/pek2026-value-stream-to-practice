---
name: synthesize-analysis-candidates
description: Inspect accumulated Raw Notes, External Inputs, and existing analysis in this repository to find traceable candidates for Observation, Hypothesis Episode, or Pattern promotion. Use when the user asks whether stored information should be promoted, wants promising ideas summarized for later comparison or rejection, requests a current reasoning synthesis, or asks to create derived analysis without deciding the talk content or adopting an Artifact.
---

# Synthesize Analysis Candidates

Read the required `00_meta/` contracts in the order defined by `AGENTS.md` before
interpreting or creating repository content.

## Workflow

1. Inspect Git status and preserve all unrelated or pre-existing changes.
2. Inventory Raw Notes, External Inputs, existing analysis nodes, Artifacts, and
   the typed relations between them.
3. Determine whether the user requested assessment only or authorized creating
   derived nodes. For assessment-only requests, report candidates without writing.
4. Identify repeated, well-bounded, or decision-relevant material that is not
   already represented by an equivalent analysis node.
5. Classify each candidate:
   - Observation: extract only bounded source statements, cite precise locations,
     and keep ambiguity visible.
   - Hypothesis Episode: state a falsifiable or assessable causal claim, expected
     and challenging signals, planned validation, actual result, and limitations.
   - Pattern: require at least two distinct Episodes by default and record the
     counterexample search. Do not create a Pattern merely to fill the index.
6. Rank candidates by source support, distinctness from existing nodes, potential
   reuse, and ability to be tested. Do not rank by rhetorical appeal alone.
7. Before writing, review the complete composition for publication safety,
   including re-identification risk created by combining otherwise ordinary facts.
   If sensitive content exists in Git history, stop and report that history
   remediation is required without repeating the value.
8. When authorized, create the smallest useful set of nodes from the repository
   templates. Use `status: proposed`; never infer human intent review.
9. Set confidence from the available evidence, not prose quality or agent effort.
   Preserve `not_tested` unless identifiable evidence was actually checked.
10. Add only canonical typed relations. A derived claim must cite its source node
    IDs, and a child result must not transitively validate a parent.
11. Update `02_analysis/README.md` as a navigation view without introducing claims
    that do not exist in source nodes.
12. Run `python3 scripts/validate_repository.py` and `git diff --check`, including
    for assessment-only work. These checks are read-only and reveal whether the
    inspected repository was already inconsistent.

## Boundaries

- Never edit, move, rename, or delete a Raw Note during promotion.
- Never set a new analysis node to `reviewed`; use
  `$finalize-analysis-node` only after explicit human intent confirmation.
- Never use `status: accepted` for analysis.
- Never create or update an Artifact without an explicit adoption decision.
- Do not treat GenAI synthesis, source polish, repeated wording, or plausibility as
  validation evidence.
- Do not force every promising idea into a node. Leave overlapping, highly
  speculative, or scope-drifting material in Raw Notes and state why it was
  deferred.

## Handoff

Report:

- nodes created or candidates recommended;
- source IDs and key typed relations;
- candidates deliberately deferred and why;
- validation status;
- that `proposed` means neither human-reviewed nor adopted.
