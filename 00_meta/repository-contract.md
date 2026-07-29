# Repository Contract

## Purpose

Preserve a traceable path from low-friction human capture to adopted session
artifacts without converting interpretation into false certainty.

## Language boundary

- Machine-only contracts and instructions are written in English.
- Raw Notes, derived analysis nodes, and adopted artifact prose are written in
  Japanese and declare `content_language: ja`.
- Frontmatter keys, enum values, IDs, paths, and relation types remain English.
- Verbatim source quotations may retain their original language. Surrounding
  descriptions and interpretations remain Japanese.
- Proper nouns and established technical terms do not count as language drift.

## Authority by layer

| Layer | Meaning | May establish current truth? |
| --- | --- | --- |
| `10_external-inputs/` | Immutable external constraints or references | Only about the external input itself |
| `01_working/raw-notes/` | What a source recorded at a point in time | No |
| `02_analysis/observations/` | Bounded descriptions extracted from sources | No |
| `02_analysis/hypothesis-episodes/` | A claim and its attempted validation | No |
| `02_analysis/patterns/` | A reusable interpretation across episodes | No |
| `03_artifacts/` | Explicitly adopted, current outputs | Yes, within stated scope |
| `00_meta/` | Rules for handling all layers | Never |

Directory position alone does not prove validity. Frontmatter status, typed
relations, and content must agree.

## Epistemic separation

Agents must label and keep separate:

- **source statement**: what the source says;
- **observation**: a bounded extraction with minimal interpretation;
- **hypothesis**: a falsifiable or assessable interpretation;
- **validation result**: what was actually checked;
- **decision**: what was adopted and why;
- **limitation**: what remains unknown or cannot be checked.

## Source precedence

When statements conflict:

1. Do not merge them into a synthetic consensus.
2. Preserve both statements and their provenance.
3. Prefer a later explicit correction only for the corrected scope.
4. Record unresolved conflict as unresolved.
5. Never use file recency alone as evidence of correctness.

## Placeholder rule

A file containing `status: placeholder` is navigation scaffolding only. Its
headings, filename, and prompts are not repository conclusions.

## Quality gate for generated output

Before saving generated content, an agent must verify:

- all factual claims cite source node IDs;
- interpretation is marked as interpretation;
- uncertainty and unavailable evidence are explicit;
- canonical enum values and relation types are used;
- no Raw Note was rewritten, moved, or removed;
- artifact adoption is supported by an explicit decision;
- repository validation passes.
