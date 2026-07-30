# Promotion Policy

Promotion creates a new node. It never relocates or replaces its sources.

## Allowed flow

```text
Raw Note / External Input
  -> Observation
  -> Hypothesis Episode
  -> Pattern
  -> Adopted Artifact
```

Steps may be skipped only when the derived node still cites adequate source
nodes and explains why the intermediate layer adds no value.

## Promotion requirements

### Raw Note to Observation

- Quote or precisely locate the source statement.
- Describe only what is supported by the source.
- Add at least one `derived_from` relation.
- Record ambiguity instead of resolving it silently.

### Observation to Hypothesis Episode

- State the hypothesis and expected signal.
- Classify `hypothesis_level` as `value`, `solution`, or `feature` only when the
  source supports that classification; otherwise use `not_assessed`.
- Distinguish planned validation from completed validation.
- Record the actual method, result, and limitations.
- Use `not_tested` when no validation occurred.
- A Solution Hypothesis may test a Value Hypothesis, and a Feature Hypothesis
  may test a Solution Hypothesis. Record those parent relations explicitly.
- Do not treat a child result as transitive validation of its parent.

### Episodes to Pattern

- Cite at least two distinct episodes by default.
- If only one episode exists, keep `status: proposed` and state that the pattern
  is a single-case interpretation.
- Record known counterexamples or the absence of a counterexample search.

### Analysis to Artifact

- Require an explicit adoption decision in the artifact.
- Cite the supporting analysis with `adopted_from`.
- State scope, unresolved uncertainty, and replacement/supersession behavior.
- Never interpret a requested filename or placeholder as an adoption decision.

## Rejection and supersession

Do not delete rejected or superseded analysis. Change its status and add:

- a `rejected_by` or `superseded_by` relation;
- a concise reason;
- the date and decision-maker when known.

## Prohibited shortcuts

- Promoting conversational plausibility as evidence.
- Inventing a validation result from a proposed test.
- Treating participant access, attendance, or positive feedback as field
  application without direct evidence.
- Adding precise KPIs solely because a template contains a metric field.
- Using Mobius `To Do`, `Doing`, or `Done` as repository task states.
- Filling every Mobius retrospective section without supporting source nodes.
