# MobiusによるHypothesis一覧

[分析Indexへ戻る](../README.md)

このファイルは、Mobiusでの位置づけとCross-scope connectionを説明するために
Repository authorが保守する非同期な解説Viewです。Evidence、派生Claim、採用判断、
現在の正本ではなく、Source更新との同期も保証しません。現在のstatus、resultおよび
直接Parentは生成されたscope別Viewで候補を絞り、リンク先のNodeを直接確認します。
内容がリンク先と矛盾する場合はリンク先を優先します。

このViewはHypothesisの検討階層を説明するためにだけ使用します。Mobiusの
ボード列を作業状態の追跡には使用しません。

`hypothesis_scope`を先に選び、異なるValue Streamの階層を混ぜない。
子から直上の親への`tests` relationは階層を表すが、子の結果は親へ推移しない。

### Session scope

```text
AudienceがAI Slopを制御するActionを持ち帰る価値
  <- tests: 構造・Signal・仮説検証を一続きに説明するSolution
       <- tests: リレー中心の25分トークというFeature
       <- tests: 一枚の補助説明とRepositoryへの導線というFeature
```

| Map | Level | Hypothesis Episode | Knowledge Basis | Intent Review | Result |
| --- | --- | --- | --- | --- | --- |
| Discovery | `value` | [AudienceはAI Slopを制御するActionを持ち帰ることに価値を感じる](../hypothesis-episodes/HYP-20260804-183208-audience-actionable-ai-slop-value.md) | `recorded_statement`, `case_recollection`, `explicit_validation`, `reasoned_synthesis` | `reviewed` | `inconclusive` |
| Decision | `solution` | [AI Slopの構造・Signal・仮説検証を一続きに説明するとActionを選びやすい](../hypothesis-episodes/HYP-20260804-183209-ai-slop-learning-path-solution.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Delivery | `feature` | [リレーを中心にしたセッション構成ならAI SlopからVSMまでを一本道で伝えられる](../hypothesis-episodes/HYP-20260731-004119-relay-centered-session-story.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Delivery | `feature` | [Human-AI協業を一枚とRepositoryへの導線に限定すると本編を逸らさず深掘りを提供できる](../hypothesis-episodes/HYP-20260805-001809-repository-handoff-preserves-focus.md) | `recorded_statement`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| 未分類 | `not_assessed` | [開催側の採択を方向性継続の十分なシグナルとして扱う](../hypothesis-episodes/HYP-20260730-015717-organizer-selection-is-sufficient-signal.md) | `explicit_validation`, `external_research`, `reasoned_synthesis` | `reviewed` | `supports` |

### Practice scope

| Map | Level | Hypothesis Episode | Knowledge Basis | Intent Review | Result |
| --- | --- | --- | --- | --- | --- |
| Discovery | `value` | [AI高速化による下流負荷の制御はPlatform Teamの価値であり利用者の受入条件である](../hypothesis-episodes/HYP-20260804-183210-ai-slop-downstream-burden-value.md) | `recorded_statement`, `practitioner_experience`, `case_recollection`, `external_research`, `explicit_validation`, `reasoned_synthesis` | `reviewed` | `inconclusive` |
| Discovery | `value` | [Platform利用者の一部は選択肢より安全な標準Pathによる選択負荷軽減を重視する](../hypothesis-episodes/HYP-20260802-230425-platform-choice-burden-value.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Discovery | `value` | [Platform選定に関与する利用者は探索と判断準備の負荷軽減に価値を感じる](../hypothesis-episodes/HYP-20260807-211651-platform-selection-preparation-value.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [価値選択と検証はAI高速化による回避可能な下流Costを減らす](../hypothesis-episodes/HYP-20260730-015718-ai-speed-requires-value-validation.md) | `recorded_statement`, `practitioner_experience`, `case_recollection`, `explicit_validation`, `reasoned_synthesis` | `reviewed` | `inconclusive` |
| Delivery | `feature` | [Value Hypothesis・期待Signal・停止条件をAdmission Controlにすると依存形成前に廃棄できる](../hypothesis-episodes/HYP-20260731-193520-lean-startup-as-admission-control.md) | `external_research`, `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [PEのDVSと利用者側OVSを接続するとAI高速化のCost Transferを検知できる](../hypothesis-episodes/HYP-20260801-004822-coupled-observability-detects-cost-transfer.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [共有前のService Contract明確化は下流への理解と判断Costの転移を抑える](../hypothesis-episodes/HYP-20260801-004823-service-contract-reduces-downstream-cost.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [Solution-firstでもReasoning Chainを再構成すれば検証可能な仮説を作りやすい](../hypothesis-episodes/HYP-20260802-230423-solution-first-reconstruction-testability.md) | `recorded_statement`, `practitioner_experience`, `case_recollection`, `direct_observation`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [Value Streamの課題とOutcomeからAI Capabilityを配置すると局所最適を避けやすい](../hypothesis-episodes/HYP-20260804-013223-outcome-first-ai-resource-allocation.md) | `recorded_statement`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [異常検知と原因診断を分ける運用はMetric過剰取得を抑え改善Loopを両立する](../hypothesis-episodes/HYP-20260804-013226-two-stage-metrics-analysis.md) | `practitioner_experience`, `case_recollection`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [Contextを確認するPlatform Advisorは静的案内より選定負荷を減らしやすい](../hypothesis-episodes/HYP-20260807-211652-contextual-platform-advisor-solution.md) | `recorded_statement`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [組織が責任を持つ標準Pathと例外Routingは選択・説明・意思決定Riskを減らす](../hypothesis-episodes/HYP-20260807-223145-standard-path-exception-routing.md) | `recorded_statement`, `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Delivery | `feature` | [選定作業を一つのChatへ統合するとPT・LTを減らし下流負荷を増やさない](../hypothesis-episodes/HYP-20260807-211653-platform-advisor-chat-feature.md) | `recorded_statement`, `reasoned_synthesis` | `reviewed` | `not_tested` |

### Standalone Practice Solution

次のSolution Hypothesisは`practice` scopeだが、現時点では直上のValue Hypothesisへの
`tests`を持たない。MobiusのDecision Levelとして扱い、主階層へ暗黙に接続しない。

- [DVSの仮説検証と学習品質はOVS品質の継続的改善に必要である](../hypothesis-episodes/HYP-20260807-232639-dvs-learning-sustains-ovs-quality.md): `reviewed`、`inconclusive`
- [個人による学習機能の代行または好条件があれば制度化されたCapabilityなしでも一回の成功は起こり得る](../hypothesis-episodes/HYP-20260809-013741-individual-learning-substitution-one-shot-success.md): `reviewed`、`inconclusive`
- [Valueから意思決定・Data・利用・OutcomeへのTraceabilityはDVSの継続的学習を成立させる](../hypothesis-episodes/HYP-20260809-013742-value-traceability-enables-dvs-learning.md): `reviewed`、`inconclusive`

## Cross-scope connections

SessionとPracticeのHypothesisは、親子検証ではなくContextまたはSource共有として
接続します。HYPからHYPへのCross-scopeな`tests`はありません。

- [Session Feature](../hypothesis-episodes/HYP-20260731-004119-relay-centered-session-story.md)は、
  [価値選択と検証のPractice Solution](../hypothesis-episodes/HYP-20260730-015718-ai-speed-requires-value-validation.md)を
  `references`する。これは25分トークで扱う題材のContextであり、どちらかの検証結果を
  もう一方へ移すrelationではない。
- [Session Solution](../hypothesis-episodes/HYP-20260804-183209-ai-slop-learning-path-solution.md)と
  Practice階層は、次のObservationをSourceとして共有している。
  - [価値判断と受け手のSlop経験を分けるFlow](../observations/OBS-20260731-120412-value-and-slop-experience-decision-flow.md)
  - [提供側と利用側のValue Streamを接続して観測する考え](../observations/OBS-20260801-004820-coupled-platform-value-streams.md)
  - [仮説検証を不確実性の分解として扱う説明](../observations/OBS-20260804-004531-hypothesis-validation-uncertainty-decision.md)

Practiceにおける方法の成立と、SessionでAudienceへ伝わることは、それぞれのScopeで
別に検証します。

`session` scopeで`supports`となっている採択シグナルは、Proposalの大方向を維持して制作を
進める判断に限定されます。Audience課題やValue Hypothesisの正しさを支持する
結果ではありません。

`practitioner_experience`と`not_tested`は両立します。この組み合わせは、実務経験を
成立根拠に持つ一方、このRepositoryでは独立検証していないことを示します。
「根拠なし」または「検証済み」と読み替えません。
