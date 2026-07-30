# Analysis Lenses

## Mobius retrospective lens

Use the Mobius Outcome Delivery map only to explain which levels of hypothesis
were considered in a selected retrospective scope.

Canonical visual reference:

- external input:
  `EXT-20260729-225555-mobius-outcome-delivery-map`
- asset:
  `10_external-inputs/frameworks/mobius/mobius-outcome-delivery-map.pdf`

### Hypothesis hierarchy

| Mobius map | `hypothesis_level` | Retrospective question |
| --- | --- | --- |
| Discovery | `value` | Whose problem and which customer or business outcome did we consider? |
| Decision | `solution` | Which solution options and causal assumptions did we consider? |
| Delivery | `feature` | Which smallest feature, change, or experiment did we consider to test the solution? |

The hierarchy is:

```text
Value Hypothesis
  -> Solution Hypothesis
    -> Feature Hypothesis
      -> explicit evidence and learning
```

This hierarchy is not transitive evidence. A successful Feature Hypothesis does
not automatically validate its parent Solution or Value Hypothesis.

### Retrospective output

When asked to explain what was considered, produce Japanese prose with these
sections:

1. `Discovery — Value Hypothesis`
2. `Decision — Solution Hypothesis`
3. `Delivery — Feature Hypothesis`
4. `横断的な学び`

For each section:

- cite the repository node IDs that support the explanation;
- explain only what was considered, tested, or learned in the requested scope;
- distinguish planned validation from completed validation;
- state that no relevant consideration was found when the sources do not
  support that section;
- leave ambiguity visible instead of forcing a classification.

Use `Measure & Learn` only to describe explicitly recorded evidence and
learning.

### Prohibited uses

Do not use the Mobius map:

- as a project plan, task board, delivery workflow, or progress report;
- to assign repository work to `To Do`, `Doing`, or `Done`;
- to infer completion from Git state, file presence, or artifact status;
- to require every retrospective to cover all three maps;
- to add structure to Raw Notes at capture time;
- as evidence that a hypothesis is correct.

`To Do`, `Doing`, and `Done` remain visual content in the external reference;
they are not canonical repository states.

## Speaker knowledge vocabulary

`01_working/context/speaker-knowledge.yaml` is a retrieval vocabulary. Use its
canonical names and aliases to expand searches and recognize terminology.

The presence of an entry:

- does not establish expertise level;
- does not adopt that framework for the current analysis;
- does not make the framework evidence;
- does not authorize forcing repository content into that framework.
