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
- Distinguish planned validation from completed validation.
- Record the actual method, result, and limitations.
- Use `not_tested` when no validation occurred.

### Proportional and lightweight validation

A Hypothesis Episode is one bounded learning attempt, not a requirement to
prove a claim conclusively. The effort and rigor of a validation method may be
proportional to the decision it informs and the maturity of the hypothesis.
This keeps early exploration feasible without overstating what weak evidence
can establish.

Acceptable lightweight methods include:

- desk research using identifiable sources;
- interviews with a small number of relevant participants;
- expert review;
- a small prototype or walkthrough;
- a session poll or other bounded participant response;
- a limited follow-up after the session.

There is no universal minimum sample size. Every completed episode must record:

- the expected signal;
- the actual method, scope, and participant or source selection;
- what was actually observed;
- the result as `supports`, `challenges`, or `inconclusive`;
- limitations, including selection bias and unavailable evidence.

Use `not_tested` only when no evidence-gathering activity occurred. A
lightweight result may justify the statement that the observed cases support
or challenge the hypothesis. It does not justify population-wide validity,
causality, or proof unless the method independently supports that stronger
claim. Confidence must reflect the accumulated evidence, not the amount of
effort spent.

### GenAI-assisted research

GenAI may help assess research feasibility, discover candidate sources, draft
an interview guide, organize supplied material, and summarize evidence.
GenAI output is process assistance, not evidence by itself.

- Claims from desk research must be checked against identifiable source
  material.
- Evidence used by a derived node must be preserved as a repository source
  node and cited through typed relations.
- Record what GenAI did and which sources a human or agent actually checked.
- Do not treat generated citations, unverified summaries, simulated
  participants, or predicted interview responses as validation.
- GenAI may analyze real interview notes or transcripts, but it must not imply
  that an interview occurred when it did not.

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
