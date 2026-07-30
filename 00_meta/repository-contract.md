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

Analysis nodes do not use `status: accepted`. A human may finish intent review
by setting an analysis node to `reviewed`, but only an explicitly adopted file
in `03_artifacts/` establishes current truth within its stated scope.

## Epistemic separation

Agents must label and keep separate:

- **source statement**: what the source says;
- **observation**: a bounded extraction with minimal interpretation;
- **hypothesis**: a falsifiable or assessable interpretation;
- **validation result**: what was actually checked;
- **decision**: what was adopted and why;
- **limitation**: what remains unknown or cannot be checked.

## Meaning of Raw Note

`Raw` describes a node's epistemic position, not its writing quality,
structure, length, or authorship.

A Raw Note may be:

- a short note written directly by a human;
- a conversation transcript or imported chat;
- a structured record written by GenAI at a human's request; or
- a record of thinking developed through human-GenAI dialogue.

It remains a Raw Note when its purpose is to preserve a source conversation or
developing thought without promoting that material into a new derived claim.
The provenance fields must make the origin, capture method, importer, and human
review state visible.

Do not promote a note merely because its prose is polished or highly
structured. Conversely, when GenAI retrospectively combines existing source
nodes to introduce a new observation, interpretation, or claim, store that
output in `02_analysis/` with typed relations instead of presenting it as a new
Raw Note.

## Source precedence

When statements conflict:

1. Do not merge them into a synthetic consensus.
2. Preserve both statements and their provenance.
3. Prefer a later explicit correction only for the corrected scope.
4. Record unresolved conflict as unresolved.
5. Never use file recency alone as evidence of correctness.

## Draft finalization exception

A Raw Note created as a blank scaffold may be finalized once after a human
writes its initial content:

- update provisional frontmatter;
- change `review_status` from `unreviewed` to `reviewed` when the completed
  content was directly authored by its human author and no correction history
  exists;
- replace an `untitled` slug with a safe topic-based slug;
- update the node ID to match that filename while preserving its timestamp.

This exception is allowed only before another node references the Raw Note.
Once referenced, its ID and filename are immutable. Filename slugs must never
contain customer, project, person, internal-system, or other identifying data.

## Confidentiality exception

Confidentiality takes precedence over source immutability. Before commit or
promotion, sanitize in place any customer, project, personal, commercial,
internal-system, credential, or re-identification information that should not
be published.

- Do not retain the removed value elsewhere in the repository.
- Do not quote it in a correction, commit message, filename, log, or summary.
- Use a category placeholder or safe generalization that retains only the
  analytical meaning needed by this repository.
- General context such as "a Red Hat Consulting Platform Engineering
  engagement" may remain when it does not identify a customer or engagement.
- If sensitive content exists in any Git commit, stop normal publication work.
  A working-tree edit does not remove Git history; report that repository
  history remediation is required without repeating the sensitive value.

## Placeholder rule

A file containing `status: placeholder` is navigation scaffolding only. Its
headings, filename, and prompts are not repository conclusions.

## Quality gate for generated output

Before saving generated content, an agent must verify:

- all factual claims cite source node IDs;
- interpretation is marked as interpretation;
- uncertainty and unavailable evidence are explicit;
- canonical enum values and relation types are used;
- no Raw Note was rewritten, moved, or removed outside the documented draft
  finalization or confidentiality exceptions;
- artifact adoption is supported by an explicit decision;
- repository validation passes.
