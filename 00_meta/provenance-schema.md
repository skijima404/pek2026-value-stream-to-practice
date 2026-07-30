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
- `status`: `proposed`, `reviewed`, `accepted`, `rejected`, or `superseded`;
- `confidence`: `low`, `medium`, `high`, or `not_assessed`;
- `relations`: a YAML list of typed relations.

Confidence is not probability and must not replace a description of evidence.

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
