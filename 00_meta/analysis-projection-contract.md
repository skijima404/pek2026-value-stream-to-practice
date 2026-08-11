# Analysis Projection Contract

## Authority boundary

- Repository Markdown nodes and adopted Artifacts remain authoritative.
- `02_analysis/README.md`, generated files under `02_analysis/views/`, and
  `views/repository-graph.json` are disposable navigation projections.
- Generated projections must not introduce interpretations, infer missing
  relations, aggregate hypothesis results, or imply that an absent Risk
  Decision is overdue.
- The JSON graph's `projection.authority` must remain `none`.
- A source digest identifies the exact Markdown inputs used for the projection.

## Projection content

The deterministic projection may contain only declared metadata, typed
relations, an explicitly recorded lightweight validation approach and
disposition, explicitly recorded hypothesis results, validation components,
current Risk Decision references, source paths, and deterministic counts.

Source bodies are not copied into the JSON graph. A consumer uses the graph to
identify candidate nodes and direct relations, then reads the authoritative
Markdown before interpreting or citing repository content.

A file under `01_working/raw-notes/` is treated as a Raw Note regardless of its
declared `type`. It enters a projection only when `type: raw_note` is valid and
all canonical Raw Note schema checks pass, including required fields, enums,
timestamps, ID and filename agreement, Japanese content, and completed
sanitization checker metadata. Its `sanitization_status` must then be
`not_needed` or `sanitized`. A Raw Note with missing or invalid metadata is
excluded fail-closed: its ID, title, path, tags, and body are not projected.
The projection may report only aggregate excluded counts. Exclusion does not
delete, reject, or change the epistemic state of the Raw Note.

An edge enters the graph only when both its source and target are projected
nodes. Relations to excluded or otherwise non-projected nodes are omitted so
their IDs are not copied into the graph. The projection may report only the
aggregate omitted-edge count. Repository validation remains responsible for
reporting invalid or missing relation targets from the authoritative Markdown.

## Generation

Run:

```text
python3 scripts/generate_analysis_views.py
python3 scripts/generate_analysis_views.py --check
```

`scripts/validate_repository.py` runs the freshness check. Any source change
that affects the projection requires regeneration before repository
validation can pass.

The generator uses only Python's standard library and the repository's
canonical Markdown parsers. Generation is deterministic: it does not call a
model, the network, or a database, and it does not add a wall-clock timestamp.

## Publication safety

The projection omits source bodies but combines titles and metadata from many
nodes. It does not inherit publication safety from individual sources. Review
the complete generated projection for re-identification risk before
publication when the source set or projection schema materially changes.

## Decision history

The reason for selecting this architecture and the conditions for revisiting
it are recorded in
`docs/architecture/decisions/ADR-0001-markdown-source-with-generated-graph-projection.md`.
The ADR explains the decision but does not replace this current contract.
