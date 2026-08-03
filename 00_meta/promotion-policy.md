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

### Confidentiality at every promotion boundary

Run a fresh publication-safety review whenever content is promoted or its
epistemic status is advanced. A source node that was previously sanitized does
not make a newly composed node safe by inheritance.

- Inspect the complete promoted node, including the combination of excerpts,
  derived prose, metadata, and relations.
- Check whether individually ordinary details become identifying when combined.
- Sanitize before changing an analysis node to `reviewed`, adopting content
  into an accepted Artifact, or committing a newly promoted node.
- Record the check result, timestamp, checker, scope, and whether content was
  changed in the promoted node or in schema-supported sanitization metadata.
- Repeat the check at each later promotion boundary. Do not rely solely on a
  check performed on an earlier source or layer.
- If sensitive content is found in a committed revision, stop normal
  publication work and report that Git history remediation is required without
  repeating the sensitive value.

A publication-safety review does not validate a claim, increase confidence, or
adopt an artifact. Keep epistemic status and sanitization status separate.

### Knowledge basis at every promotion boundary

Assign `knowledge_basis` from what the cited sources and completed activities
actually support. Preserve multiple bases when a node combines practitioner
experience, external research, direct observation, or reasoned synthesis.

- Do not treat `not_tested` as meaning that a node has no knowledge basis.
- Do not treat `practitioner_experience` as independent validation, a measured
  result, population-wide evidence, or a universal rule.
- Do not invent engagement counts, years of experience, success rates, or case
  details to make practitioner experience appear more rigorous.
- Use `case_recollection` for one remembered episode that lacks an inspectable
  primary record. Do not silently expand it into accumulated experience.
- Use `external_research` only for identifiable material that was actually
  checked and preserved as a repository source.
- Use `direct_observation` only for a bounded record of actual behavior, an
  event, or a condition. Record selection and comparability limitations.
- Use `explicit_validation` only after an evidence-gathering activity was
  completed and its actual result was recorded.
- Sanitization or confidentiality-driven generalization does not erase the
  knowledge basis, but it may limit reproducibility and generalization. State
  that limitation without retaining identifying details.

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
- Practitioner experience does not waive the Episode and counterexample rules.
  Do not fabricate cases or Episodes to make an experienced practice look like
  a repository-validated Pattern.

### Analysis to Artifact

- Require an explicit adoption decision in the artifact.
- Cite the supporting analysis with `adopted_from`.
- State scope, unresolved uncertainty, and replacement/supersession behavior.
- Never interpret a requested filename or placeholder as an adoption decision.
- A human may explicitly adopt an independently untested practitioner practice
  as current session guidance. Preserve `practitioner_experience`, disclose
  that the repository did not independently test it, state its application
  scope and limitations, and do not present it as a universal or measured fact.

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
