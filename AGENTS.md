# Repository Agent Contract

This repository is an evidence-preserving workspace for the Platform Engineering
Kaigi 2026 session described in `README.md`.

## Language

- Write machine-only instructions and contracts in English. This includes this
  file, `00_meta/`, source code, schema descriptions, and validation messages.
- Write repository content in Japanese. This includes Raw Notes, Observations,
  Hypothesis Episodes, Patterns, adopted Artifacts, and their human-readable
  templates.
- Write participant- and contributor-facing repository guidance in Japanese.
- Keep identifiers, frontmatter keys, enum values, paths, and relation types in
  English. Every governed content node must declare `content_language: ja`.
- A verbatim quotation may preserve its source language, but its surrounding
  description and interpretation must be Japanese.
- Do not mix English prose into Japanese content merely because an upstream
  template or source uses English. Proper nouns and established technical terms
  are allowed.
- Do not translate canonical identifiers, keys, enum values, or paths.

## Required reading order

Before creating, interpreting, promoting, or editing repository content, read:

1. `00_meta/repository-contract.md`
2. `00_meta/provenance-schema.md`
3. `00_meta/promotion-policy.md`
4. `00_meta/relation-schema.md`
5. `00_meta/naming-conventions.md`

The files above define how truth is handled. They do not define the truth about
the session.

## Non-negotiable behavior

- Treat `01_working/raw-notes/` as immutable source material.
- Apply the draft-finalization and confidentiality exceptions defined in
  `00_meta/repository-contract.md` before applying Raw Note immutability.
- Never move or delete a Raw Note because a derived node was created.
- Preserve incorrect source statements and append a correction instead of
  silently rewriting history.
- Never preserve customer, project, personal, commercial, internal-system, or
  credential information merely for provenance. Sanitize it before commit and
  never repeat removed values in corrections, filenames, logs, or summaries.
- Do not turn a short note into a confident claim without recording the
  interpretation and its uncertainty.
- Every derived claim must cite one or more repository node IDs through typed
  relations.
- Keep observation, interpretation, hypothesis, decision, and current artifact
  distinct. Do not collapse them into one document.
- Do not infer that a placeholder, directory name, template, or planned
  artifact is an adopted conclusion.
- Do not invent missing provenance, validation results, participant behavior,
  metrics, or evidence. Use `unknown`, `unverified`, or an explicit limitation.
- Do not promote content into `03_artifacts/` unless an adoption decision is
  explicit and traceable.
- Run `python3 scripts/validate_repository.py` after changing governed Markdown.

## Scope rules

- Humans may write low-structure Raw Notes. Do not force hypothesis fields into
  capture-time notes.
- GenAI may propose derived nodes in `02_analysis/` when asked, but must retain
  traceability and epistemic status.
- `03_artifacts/` contains current adopted outputs, not every explored idea.
- `10_external-inputs/` contains immutable constraints and references. External
  input is not automatically evidence that a hypothesis is true.

When instructions conflict, stop and report the conflict rather than choosing a
convenient interpretation.
