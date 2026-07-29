# Naming Conventions

## Node IDs and files

Use local time with a numeric timezone in frontmatter and UTC-independent,
sortable local timestamps in IDs.

| Type | ID and filename stem |
| --- | --- |
| Raw Note | `RN-YYYYMMDD-HHMMSS-short-slug` |
| Observation | `OBS-YYYYMMDD-HHMMSS-short-slug` |
| Hypothesis Episode | `HYP-YYYYMMDD-HHMMSS-short-slug` |
| Pattern | `PAT-YYYYMMDD-HHMMSS-short-slug` |
| External Input | `EXT-YYYYMMDD-HHMMSS-short-slug` |

The filename is `<id>.md`. Use lowercase ASCII kebab-case for `short-slug`.
IDs are immutable even when titles change.

## Tags

Tags are lowercase kebab-case. Prefer existing tags. Tags aid discovery but do
not establish relations or evidence.

## Stable author identifiers

Use a namespaced identifier where practical:

- `human:kijima`
- `agent:codex`
- `agent:assista`

Do not infer a human identity from a Git author or platform account.
