# Relation Schema

Relations are directed edges stored in frontmatter:

```yaml
relations:
  - type: derived_from
    target: RN-20260729-120000-example
```

Allowed relation types:

| Relation | Source -> target meaning |
| --- | --- |
| `derived_from` | This node was extracted or interpreted from target |
| `tests` | This episode tests the target hypothesis or claim |
| `supports` | Evidence in this node supports target |
| `challenges` | Evidence in this node challenges target |
| `adopted_from` | This artifact adopts content from target analysis |
| `corrects` | This node explicitly corrects a scoped part of target |
| `supersedes` | This node replaces target as current within stated scope |
| `rejected_by` | Target records the decision rejecting this node |
| `superseded_by` | Target is the node that superseded this node |
| `references` | Non-evidentiary contextual link |

Rules:

- `target` is a repository node ID, not a path or free-form title.
- Use `references` only when no evidentiary implication is intended.
- `supports` and `challenges` require an explanation in the body.
- Relations do not inherit transitively. A Pattern citing an Episode does not
  automatically cite every Raw Note behind the Episode.
- Circular `derived_from`, `adopted_from`, or `supersedes` chains are invalid.
