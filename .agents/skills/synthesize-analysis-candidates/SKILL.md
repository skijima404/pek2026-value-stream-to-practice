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
     When the claim contains multiple decision-relevant uncertainties, add stable
     Validation Components and keep Coverage, Finding, Applicability, and residual
     uncertainty distinct.
   - Pattern: require at least two distinct Episodes by default and record the
     counterexample search. Do not create a Pattern merely to fill the index.
6. Assign every applicable `knowledge_basis` value from the cited sources and
   completed activities. Preserve practitioner experience as a real basis without
   converting it into independent validation. Use `case_recollection` for a
   specific remembered episode without an inspectable primary record, and never
   infer experience scope or case counts.
7. Rank candidates by source support, distinctness from existing nodes, potential
   reuse, and ability to be tested. Do not rank by rhetorical appeal alone.
8. Before writing, review the complete composition for publication safety,
   including re-identification risk created by combining otherwise ordinary facts.
   If sensitive content exists in Git history, stop and report that history
   remediation is required without repeating the value.
9. When authorized, create the smallest useful set of nodes from the repository
   templates. Use `status: proposed`; never infer human intent review.
10. Set confidence from the available evidence, not prose quality or agent effort.
   Preserve `not_tested` unless identifiable evidence was actually checked.
    Do not summarize `practitioner_experience` plus `not_tested` as unsupported.
    Component Evidence refs normally cite Observation nodes so their
    `knowledge_basis` and source relations remain traceable. Never calculate a
    truth percentage from component Coverage.
11. Add only canonical typed relations. A derived claim must cite its source node
    IDs, and a child result must not transitively validate a parent.
12. When source nodes were created or changed, run
    `python3 scripts/generate_analysis_views.py`. Do not edit generated projections
    directly.
13. Run `python3 scripts/validate_repository.py` and `git diff --check`, including
    for assessment-only work. These checks are read-only and reveal whether the
    inspected repository was already inconsistent.

## Boundaries

- Never edit, move, rename, or delete a Raw Note during promotion.
- Never set a new analysis node to `reviewed`; use
  `$finalize-analysis-node` only after explicit human intent confirmation.
- Never use `status: accepted` for analysis.
- Never create or update an Artifact without an explicit adoption decision.
- Never create a Risk Decision while synthesizing candidates. Use
  `$record-risk-decision` only after an explicit human response to documented
  residual risk.
- Do not treat GenAI synthesis, source polish, repeated wording, or plausibility as
  validation evidence.
- Do not fabricate Episodes or external support for an experienced practice.
  Practitioner guidance may remain independently untested and still be proposed
  for explicit human adoption with its basis and limitations intact.
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
