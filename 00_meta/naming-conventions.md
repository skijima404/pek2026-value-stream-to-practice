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
| Risk Decision | `RSK-YYYYMMDD-HHMMSS-short-slug` |
| External Input | `EXT-YYYYMMDD-HHMMSS-short-slug` |

Validation Component IDs are local to one Hypothesis Episode and use `U1`,
`U2`, and so on. They are immutable once referenced by a Risk Decision. A full
component reference is the pair `(target_node, target_component_id)`.

The filename is `<id>.md`. Use lowercase ASCII kebab-case for `short-slug`.
IDs are immutable even when titles change, except for the one-time,
pre-reference draft finalization defined in `repository-contract.md`.

Use a safe topic-based slug. Never include a customer, engagement, project,
person, account, hostname, internal system, or other identifying value.

## Tags

Tags are lowercase kebab-case. Prefer existing tags. Tags aid discovery but do
not establish relations or evidence.

## Stable author identifiers

Use a namespaced identifier where practical:

- `human:kijima`
- `agent:codex`
- `agent:assista`

Do not infer a human identity from a Git author or platform account.
