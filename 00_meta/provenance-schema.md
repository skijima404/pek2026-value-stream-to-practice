# Provenance Schema

All governed Markdown documents begin with YAML frontmatter.

## Raw Note required fields

| Field | Type | Allowed values or rule |
| --- | --- | --- |
| `id` | string | Must match the filename stem and naming convention |
| `type` | string | `raw_note` |
| `title` | string | Human-readable; may be provisional |
| `content_language` | string | `ja` |
| `created_at` | string | ISO 8601 timestamp with timezone |
| `content_origin` | string | `human_direct`, `assist_a_generated`, `mixed` |
| `created_by` | string | Person or agent identifier; never guessed |
| `source_platform` | string | `local`, `chatgpt`, `codex`, `other` |
| `capture_mode` | string | `direct`, `copy_paste`, `transcript`, `import`, `assisted` |
| `imported_by` | string | Identifier or `none` |
| `review_status` | string | `unreviewed`, `reviewed`, `corrected` |
| `sanitization_status` | string | `not_reviewed`, `not_needed`, `sanitized` |
| `sanitization_checked_at` | string | ISO 8601 timestamp with timezone or `none` |
| `sanitization_checked_by` | string | Agent identifier or `none` |
| `tags` | YAML list | Zero or more stable, lowercase tags |

`content_origin` describes who or what originated the actual wording:

- `human_direct`: a human directly authored the recorded content;
- `assist_a_generated`: AssistA on ChatGPT generated the content;
- `mixed`: human and GenAI wording cannot be cleanly separated.

These values describe the origin of the recorded wording, not the node's
epistemic authority or level of polish. A structured GenAI-written record may
remain a Raw Note when it captures a source conversation or a human's
developing thought. New retrospective interpretation across existing source
nodes belongs in a derived analysis node.

`created_by` and `imported_by` are identifiers, not claims of approval.
`review_status: reviewed` means a human reviewed transcription/provenance; it
does not mean the note's claims are true.

For a completed Raw Note, use the following review-status defaults:

- A note directly authored in the repository by its human author uses
  `reviewed`. This applies to `content_origin: human_direct` with
  `capture_mode: direct` or `assisted` and `imported_by: none`.
- A blank scaffold remains `unreviewed` until the human author fills and
  finalizes it.
- Imported, copied, or transcribed content remains `unreviewed` until a human
  confirms that the repository record matches their intent.
- `mixed` or `assist_a_generated` content remains `unreviewed` until explicit
  human review.
- A note with a correction history uses `corrected`, including after subsequent
  human review.

`sanitization_status` records only a publication-safety check. It does not
establish that the note's claims are true. If sanitization changes authored
wording, set `content_origin: mixed`. Never store removed sensitive values in
sanitization metadata.

## Derived node required fields

All derived nodes require:

- `id`, `type`, `title`, `created_at`, `created_by`;
- `content_language`: `ja`;
- `status`: `proposed`, `reviewed`, `rejected`, or `superseded`;
- `knowledge_basis`: a non-empty YAML list using the canonical values below;
- `confidence`: `low`, `medium`, `high`, or `not_assessed`;
- `relations`: a YAML list of typed relations.

Confidence is not probability and must not replace a description of evidence.
Derived analysis does not use `status: accepted`. Human intent review ends at
`reviewed`; adoption as current repository truth is recorded only in
`03_artifacts/`.

### Knowledge basis

`knowledge_basis` records how the knowledge or claim represented by a derived
node was formed. It does not record whether a human reviewed the wording,
whether a claim was validated, or whether it was adopted.

Allowed values are:

| Value | Meaning |
| --- | --- |
| `recorded_statement` | A repository source explicitly recorded the statement, plan, preference, or interpretation |
| `practitioner_experience` | A practitioner identifies accumulated professional experience or practice judgment as a basis |
| `case_recollection` | A bounded remembered episode is available without an inspectable primary record |
| `external_research` | An identifiable external source was actually inspected |
| `direct_observation` | Actual behavior, an event, or a condition was captured in a bounded record |
| `explicit_validation` | A purposeful test, interview, review, or other evidence-gathering activity was completed |
| `reasoned_synthesis` | The node combines or interprets sources to form a new inference |

Use every applicable value and no inferred value. Do not infer accumulated
experience from seniority, a framework vocabulary entry, polished prose, or a
single anecdote. Use `case_recollection` rather than `practitioner_experience`
when the only basis is one remembered episode without an inspectable record.
Use `explicit_validation` only when a validation activity actually occurred;
a planned method, human intent review, or GenAI review is not validation.

The following combination is valid and important:

```yaml
knowledge_basis:
  - practitioner_experience
```

with a Hypothesis Episode result of `not_tested`. It means that professional
practice grounds the claim while this repository contains no independent test
of it. It does not mean the claim has no basis, and it does not establish a
general law.

### Meaning of `reviewed`

For a derived node, `status: reviewed` means that a human explicitly reviewed
the node and confirmed that it faithfully represents the human's intended
meaning within the stated scope.

Every derived node with `status: reviewed` requires:

- `reviewed_at`: the ISO 8601 timestamp of the explicit human confirmation;
- `reviewed_by`: the `human:*` identifier of the reviewer;
- `review_scope`: `intent_alignment`.

It does not mean that:

- the claims are factually correct;
- the hypothesis was validated or supported;
- the content was adopted as current repository truth;
- the node is safe to publish; or
- an agent reviewed its own output.

An agent must not change a derived node from `proposed` to `reviewed` without
explicit human confirmation. Git authorship, an agent self-review, a repository
validation pass, and a publication-safety review are not substitutes for that
confirmation.

If a later edit materially changes the meaning of a reviewed node, return its
status to `proposed` until a human reviews the changed meaning. Metadata-only,
formatting-only, and publication-safety annotations that do not alter meaning
do not invalidate the existing intent review.

Hypothesis Episodes additionally require:

- `hypothesis_level`: `value`, `solution`, `feature`, or `not_assessed`.

The level identifies the hypothesis hierarchy used for retrospective
explanation. It is not a task state or delivery-progress field. Use
`not_assessed` when the sources do not support a reliable classification.

## Risk Decision required fields

A Risk Decision records an explicit human response to one residual risk. It is
not a derived analysis node and does not use `status`, `confidence`,
`knowledge_basis`, or a hypothesis `result`.

| Field | Type | Allowed values or rule |
| --- | --- | --- |
| `id` | string | `RSK-YYYYMMDD-HHMMSS-short-slug`; matches filename |
| `type` | string | `risk_decision` |
| `title` | string | Human-readable decision title |
| `content_language` | string | `ja` |
| `created_at` | string | ISO 8601 timestamp with timezone |
| `created_by` | string | Person or agent that recorded the node |
| `decision_status` | string | `current`, `superseded`, or `withdrawn` |
| `target_node` | string | Existing Hypothesis Episode ID |
| `target_component_id` | string | Stable component ID such as `U1` |
| `risk_response` | string | `investigate_more`, `mitigate`, `proceed_with_risk`, `avoid`, or `transfer` |
| `decision_sufficiency` | string | `insufficient`, `sufficient_for_next_step`, `sufficient_with_conditions`, or `sufficient_for_current_scope` |
| `decided_by` | string | Explicit `human:*` identifier |
| `decided_at` | string | ISO 8601 timestamp of the human decision |
| `relations` | YAML list | Typed relations including one matching `evaluates` edge |

There is no `undecided` Risk Decision. Absence of a node means no response has
been recorded. A later decision creates a new node with `supersedes`; it does
not overwrite the earlier decision history.

## Corrections

Do not erase an incorrect historical statement. Append:

```markdown
### CR-YYYYMMDD-HHMMSS

- corrected_at: 2026-07-29T12:00:00+09:00
- corrected_by: human:kijima
- target: a precise section or quoted fragment
- correction: the corrected statement
- reason: why the correction is necessary
```

Then set `review_status: corrected`. A correction has authority only over its
declared target.
