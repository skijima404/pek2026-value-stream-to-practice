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
| `tests` | For Hypothesis Episode to Hypothesis Episode, source tests its immediate hierarchy parent within the same scope |
| `supports` | Evidence in this node supports target |
| `challenges` | Evidence in this node challenges target |
| `adopted_from` | This artifact adopts content from target analysis |
| `corrects` | This node explicitly corrects a scoped part of target |
| `supersedes` | This node replaces target as current within stated scope |
| `rejected_by` | Target records the decision rejecting this node |
| `superseded_by` | Target is the node that superseded this node |
| `references` | Non-evidentiary contextual link |
| `evaluates` | This Risk Decision responds to residual risk in target Hypothesis Episode; `target_component_id` provides the local scope |
| `informed_by` | This Risk Decision actually considered target evidence when making the response |

Rules:

- `target` is a repository node ID, not a path or free-form title.
- Use `references` only when no evidentiary implication is intended.
- `supports` and `challenges` require an explanation in the body.
- Every Hypothesis Episode to Hypothesis Episode `tests` relation is reserved
  for the immediate Value/Solution/Feature hierarchy parent. Source and target
  use the same `hypothesis_scope`, and the target is exactly one level above
  the source.
- Use `references` or `derived_from` for cross-scope context or same-level
  hypotheses. If a future workflow needs a non-hierarchical HYP-to-HYP test,
  define a separate relation type instead of overloading `tests`.
- Relations do not inherit transitively. A Pattern citing an Episode does not
  automatically cite every Raw Note behind the Episode.
- Circular `derived_from`, `adopted_from`, or `supersedes` chains are invalid.
- A Risk Decision has exactly one `evaluates` relation matching `target_node`.
  The component is identified only by the dedicated `target_component_id`
  field because component IDs are local to a Hypothesis Episode.
- `informed_by` does not change the evidence's finding or knowledge basis.
