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
- `confidence`: `low`, `medium`, `high`, or `not_assessed`;
- `relations`: a YAML list of typed relations.

Confidence is not probability and must not replace a description of evidence.
Derived analysis does not use `status: accepted`. Human intent review ends at
`reviewed`; adoption as current repository truth is recorded only in
`03_artifacts/`.

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
