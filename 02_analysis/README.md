# 分析

Raw Noteや外部入力から作った派生ノードを置きます。

- `observations/`: 根拠の範囲を限定した観察
- `hypothesis-episodes/`: 小さな仮説と検証結果
- `patterns/`: 複数episodeを横断する再利用可能な解釈

本文は日本語で記述します。人間が内容と意図の一致を確認した分析は
`status: reviewed` とします。分析ノードでは `status: accepted` を使用しません。
現在の登壇成果物として採用する場合は、明示的な採用判断と根拠を
`03_artifacts/` に記録します。

## このIndexの扱い

このREADMEは、既存Nodeを見つけ、現在のReasoning Chainを追うための
再生成可能なNavigation Viewです。Evidence、派生Claim、採用判断、現在の
正本ではありません。

- 内容の正本は、リンク先のNodeとArtifactです。
- status、knowledge_basis、confidence、result、hypothesis_scope、
  hypothesis_level、relationを、リンク先を越えて解釈しません。
- このIndexに載っていないことを、却下や不存在の証拠として扱いません。
- NodeやArtifactと矛盾する場合は、リンク先を優先してIndexを再生成します。

## Knowledge Basisの読み方

`knowledge_basis`は、内容がどの種類の知識に基づいて成立したかを示します。
正しさ、意図Review、検証結果、登壇への採用とは別の軸です。

- `recorded_statement`: Sourceに記録された発言、計画、選好、見立て
- `practitioner_experience`: 実務経験の蓄積から形成された判断または方法論
- `case_recollection`: 再確認できる一次記録がない、特定事例についての記憶
- `external_research`: 実際に確認し、Sourceとして保存した外部資料
- `direct_observation`: 範囲を限定して記録された実際の行動、出来事、状態
- `explicit_validation`: 実施済みのTest、Interview、Reviewなどの検証活動
- `reasoned_synthesis`: 複数Sourceの接続または解釈によって作った推論

複数のBasisを併記できます。`practitioner_experience`と`not_tested`の併記は、
実務経験に根拠を持つが、このRepositoryでは独立検証していない状態です。
経験知の価値を消さず、普遍的事実または検証済みEvidenceにも変換しません。

## 現在の全体像

Hypothesis Episodeは同じフォルダに置き、`hypothesis_scope`で二つの独立した
Value／Solution／Feature階層を表します。子から直上の親だけを`tests`で接続します。

### Session scope

```text
Value: AudienceがAI Slopを制御するActionを持ち帰る価値
  └─ tests ← Solution: 構造・Signal・仮説検証を一続きに説明する
       ├─ tests ← Feature: リレーを中心にした25分トーク
       └─ tests ← Feature: 一枚の補助説明とRepositoryへの導線
```

一枚とRepositoryへの導線というFeatureは`reviewed`、他の3 Nodeは`proposed`で、
4 Nodeはいずれも`not_tested`です。人間の意図Reviewは検証またはSession Story、
Slidesへの採用を意味しません。

### Practice scope

```text
Value: AI高速化による回避可能な下流負荷を特定・制御・削減できる状態
  ├─ tests ← Solution: 価値選択と検証
  ├─ tests ← Solution: Lean Startupによる選別と早期廃棄
  ├─ tests ← Solution: DVSとOVSを接続した観測
  ├─ tests ← Solution: Service Contract
  ├─ tests ← Solution: Outcome-firstのAI Capability配置
  └─ tests ← Solution: 二段階Metric分析
```

この主階層の7 Nodeはいずれも`proposed`かつ`not_tested`です。個別Solutionの結果は、
親Valueの結果へ自動的には推移しません。

### Standaloneまたは未分類のHypothesis

- [Solution-firstから検証可能な仮説を再構成するPractice Solution](./hypothesis-episodes/HYP-20260802-230423-solution-first-reconstruction-testability.md)
  - `practice`、`solution`、`reviewed`、`not_tested`
  - 主階層への`tests`はなく、価値選択と検証のPractice Solutionを`references`する
- [安全な標準Pathによる選択負荷軽減のPractice Value](./hypothesis-episodes/HYP-20260802-230425-platform-choice-burden-value.md)
  - `practice`、`value`、`reviewed`、`not_tested`
  - 現在は独立したValue Hypothesisであり、子Solutionは記録されていない
- [開催側の採択を方向性継続のSignalとして扱うHypothesis](./hypothesis-episodes/HYP-20260730-015717-organizer-selection-is-sufficient-signal.md)
  - `session`、`not_assessed`、`reviewed`、`supports`
  - Value／Solution／Feature階層には分類されていない

## Sourceと派生Reasoning Chain

以下はScope階層ではなく、Observation、Hypothesis、ArtifactがどのSource themeから
形成されたかを追うための詳細Viewです。

```text
参加者の成功条件とJourney
  -> Observationとして整理
  -> 参加者Journey兼Value Streamとして採用済み

Audienceと価値課題の見立て
  + 参加者が試したいと思うこと、または一つ持ち帰って試すという成功条件
  -> AI Slopを制御するActionを持ち帰ることのSession Value Hypothesis
  -> 構造・Signal・仮説検証を一続きに説明するSession Solution Hypothesis
  -> いずれも未検証、未採用

AIの局所高速化、ハンドオーバー、リレー、早期中止判断
  -> 構成要素と表現選択をObservationとして整理
  -> リレー中心の25分トーク構成というSession Feature Hypothesis
  -> 階層変更により再Review待ち、未検証、未採用

Human-AI協業モデルと登壇準備Repository
  -> 本編では一枚に限定し、Repositoryを登壇後の深掘りへ使う編集判断
  -> 一枚とRepositoryへの導線というSession Feature Hypothesis
  -> Focus維持、役割理解、閲覧、Action選択を分け、未検証、未採用

BetterUpのWorkslop調査
  -> 受け手が追加作業、感情および送信者への評価を自己申告した結果をObservation化
  -> Platform Engineeringへの適用と因果は未確認

判断Contextを渡すHandoverの事例記憶
  -> Outputだけでなく、問い、意味、根拠、Contextを渡すというObservation
  -> 一次資料を持つ比較ではなく、Case RecollectionとReasoned Synthesisとして保持

個別Enablementを反復する人力補完
  -> Persona、Contract、Service ScopeまたはCapacityの見直しSignalとしてObservation化
  -> 診断精度、因果および介入効果は未確認

AIによる候補流入と下流への確認、判断、手戻り、SupportのCost Transfer
  -> 回避可能な下流負荷を特定・制御・削減できるPractice Value Hypothesis
  -> 価値選択と検証、Lean Startup、DVS/OVS観測、Service Contractなどの
     Practice Solution Hypothesis
  -> Session階層とは分離し、未検証、未採用

PresalesとProject Deliveryを通じた限定的な実務経験
  + Customerへ毎回、目的とDiscovery結果を質問した経験
  -> 確認時点で結果が定義されていないか、担当者が理解していないというObservation
  -> 調査による実施率ではなくpractitioner_experienceとして保持

Value Stream上の課題と期待Outcome
  + AI、Human、PlatformのCapabilityと責任境界
  -> OutcomeからAI Capabilityを配置するSolution Hypothesis
  -> 記録された考えと推論に基づき、未検証、未採用

AI SlopによるCost外部化
  + Release前のValue Hypothesis検証と早期廃棄
  -> Lean Startupの選別をAdmission Controlとして使うSolution Hypothesis
  -> 親Value変更により再Review待ち、未検証、未採用

PEのDevelopment Value Stream（DVS）
  + 利用者側Operational Value Stream（OVS）
  + 価値とSlop経験を分ける判断Flow
  -> 二つのValue Streamを接続したObservabilityというSolution Hypothesis
  -> 親Value変更により再Review待ち、未検証、未採用

AI生成物またはPlatform ServiceのHandover
  + Contract、Accountability、Cost Transferの分離
  -> 共有前のService Contract明確化というSolution Hypothesis
  -> 親Value変更により再Review待ち、未検証、未採用

Solution候補が先に出る実務上の思考順序
  + Challenge、Value、Solutionの役割分離
  + GenAIによるReasoning Chainの構造確認
  -> Solution-firstから検証可能な仮説を再構成するSolution Hypothesis
  -> 人間の意図Review済み、未検証、未採用

Solution-first再構成の有無が異なるTraining記録
  -> Challenge表現、Idea数、所要時間、Facilitator負荷の違いをObservationとして整理
  -> 比較条件が揃っていないため、既存Solution Hypothesisの検証結果には使わない

案に含まれる複数の不確実性
  + Riskを引き受けられる状態まで確からしさを更新する意思決定
  -> 仮説検証を不確実性の分解と意思決定更新として扱う説明をObservationとして整理
  -> 説明の有効性と登壇への採用は未確認

前回登壇で特定したTeam Visionと対象Journey
  -> 今回、そのJourneyをVSM・MBPMへ展開する前後関係をObservationとして整理
  -> 今回の順序であり、VSM・MBPM一般の唯一の作成順序とはしない

Platform Advisorの隠れた前提
  + Platformを選びたい利用者と、選択を負担と感じる利用者
  -> 安全な標準Pathによる選択負荷軽減というValue Hypothesis
  -> 人間の意図Review済み、未検証、未採用

Project・Transformation関連資料の失敗率
  -> 対象、成功定義、Evidenceの性質が異なることをObservationとして整理
  -> Business Outcome未達率としては統合しない

MBPMで観測するProcess上のFlow
  + Output、Experience、Trust、Contract Quality
  -> 別の観測対象としてObservationに分離
  -> 測定方法と既存Observability Hypothesisへの接続は未決定

受け手がSlopとして経験する追加負荷
  + 品質、学習、Accountability、安全性のために残す摩擦
  -> 摩擦を除去するか目的を明示して残すかの境界をObservationとして整理
  -> 実際のServiceでの判定方法と効果は未確認

ITSMで約10年、約3件のProjectに再利用し、Project Portfolioにも持ち込んだ
メトリック分析運用
  -> Dashboardによる定期的な異常検知とBIによる原因診断をObservationとして整理
  -> practitioner_experienceとcase_recollectionを分離
  -> Metric過剰取得を抑えながら改善Loopの頻度と深さを両立するSolution Hypothesis
  -> DashboardとDataだけではなく分析Techniqueの習熟を成立条件とする
  -> 過去の一次資料は未確認、Platform Engineeringは導入初期、未採用

BCGの10–20–70関連資料
  -> 説明対象の違いをObservationとして整理
  -> 登壇上の主張やArtifactには未採用
```

## MobiusによるHypothesis一覧

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
| Discovery | `value` | [AudienceはAI Slopを制御するActionを持ち帰ることに価値を感じる](./hypothesis-episodes/HYP-20260804-183208-audience-actionable-ai-slop-value.md) | `recorded_statement`, `reasoned_synthesis` | `proposed` | `not_tested` |
| Decision | `solution` | [AI Slopの構造・Signal・仮説検証を一続きに説明するとActionを選びやすい](./hypothesis-episodes/HYP-20260804-183209-ai-slop-learning-path-solution.md) | `practitioner_experience`, `reasoned_synthesis` | `proposed` | `not_tested` |
| Delivery | `feature` | [リレーを中心にしたセッション構成ならAI SlopからVSMまでを一本道で伝えられる](./hypothesis-episodes/HYP-20260731-004119-relay-centered-session-story.md) | `practitioner_experience`, `reasoned_synthesis` | `proposed` | `not_tested` |
| Delivery | `feature` | [Human-AI協業を一枚とRepositoryへの導線に限定すると本編を逸らさず深掘りを提供できる](./hypothesis-episodes/HYP-20260805-001809-repository-handoff-preserves-focus.md) | `recorded_statement`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| 未分類 | `not_assessed` | [開催側の採択を方向性継続の十分なシグナルとして扱う](./hypothesis-episodes/HYP-20260730-015717-organizer-selection-is-sufficient-signal.md) | `explicit_validation`, `external_research`, `reasoned_synthesis` | `reviewed` | `supports` |

### Practice scope

| Map | Level | Hypothesis Episode | Knowledge Basis | Intent Review | Result |
| --- | --- | --- | --- | --- | --- |
| Discovery | `value` | [AI高速化による下流負荷の制御はPlatform Teamの価値であり利用者の受入条件である](./hypothesis-episodes/HYP-20260804-183210-ai-slop-downstream-burden-value.md) | `recorded_statement`, `practitioner_experience`, `case_recollection`, `external_research`, `explicit_validation`, `reasoned_synthesis` | `reviewed` | `inconclusive` |
| Discovery | `value` | [Platform利用者の一部は選択肢より安全な標準Pathによる選択負荷軽減を重視する](./hypothesis-episodes/HYP-20260802-230425-platform-choice-burden-value.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [価値選択と検証はAI高速化による回避可能な下流Costを減らす](./hypothesis-episodes/HYP-20260730-015718-ai-speed-requires-value-validation.md) | `practitioner_experience`, `reasoned_synthesis` | `proposed` | `not_tested` |
| Decision | `solution` | [Lean Startupの選別と早期廃棄は未検証案のコスト外部化を抑える](./hypothesis-episodes/HYP-20260731-193520-lean-startup-as-admission-control.md) | `external_research`, `practitioner_experience`, `reasoned_synthesis` | `proposed` | `not_tested` |
| Decision | `solution` | [PEのDVSと利用者側OVSを接続するとAI高速化のCost Transferを検知できる](./hypothesis-episodes/HYP-20260801-004822-coupled-observability-detects-cost-transfer.md) | `practitioner_experience`, `reasoned_synthesis` | `proposed` | `not_tested` |
| Decision | `solution` | [共有前のService Contract明確化は下流への理解と判断Costの転移を抑える](./hypothesis-episodes/HYP-20260801-004823-service-contract-reduces-downstream-cost.md) | `practitioner_experience`, `reasoned_synthesis` | `proposed` | `not_tested` |
| Decision | `solution` | [Solution-firstでもReasoning Chainを再構成すれば検証可能な仮説を作りやすい](./hypothesis-episodes/HYP-20260802-230423-solution-first-reconstruction-testability.md) | `case_recollection`, `reasoned_synthesis` | `reviewed` | `not_tested` |
| Decision | `solution` | [Value Streamの課題とOutcomeからAI Capabilityを配置すると局所最適を避けやすい](./hypothesis-episodes/HYP-20260804-013223-outcome-first-ai-resource-allocation.md) | `recorded_statement`, `reasoned_synthesis` | `proposed` | `not_tested` |
| Decision | `solution` | [異常検知と原因診断を分ける運用はMetric過剰取得を抑え改善Loopを両立する](./hypothesis-episodes/HYP-20260804-013226-two-stage-metrics-analysis.md) | `practitioner_experience`, `case_recollection`, `reasoned_synthesis` | `proposed` | `not_tested` |

## Cross-scope connections

SessionとPracticeのHypothesisは、親子検証ではなくContextまたはSource共有として
接続します。HYPからHYPへのCross-scopeな`tests`はありません。

- [Session Feature](./hypothesis-episodes/HYP-20260731-004119-relay-centered-session-story.md)は、
  [価値選択と検証のPractice Solution](./hypothesis-episodes/HYP-20260730-015718-ai-speed-requires-value-validation.md)を
  `references`する。これは25分トークで扱う題材のContextであり、どちらかの検証結果を
  もう一方へ移すrelationではない。
- [Session Solution](./hypothesis-episodes/HYP-20260804-183209-ai-slop-learning-path-solution.md)と
  Practice階層は、次のObservationをSourceとして共有している。
  - [価値判断と受け手のSlop経験を分けるFlow](./observations/OBS-20260731-120412-value-and-slop-experience-decision-flow.md)
  - [提供側と利用側のValue Streamを接続して観測する考え](./observations/OBS-20260801-004820-coupled-platform-value-streams.md)
  - [仮説検証を不確実性の分解として扱う説明](./observations/OBS-20260804-004531-hypothesis-validation-uncertainty-decision.md)

Practiceにおける方法の成立と、SessionでAudienceへ伝わることは、それぞれのScopeで
別に検証します。

`session` scopeで`supports`となっている採択シグナルは、Proposalの大方向を維持して制作を
進める判断に限定されます。Audience課題やValue Hypothesisの正しさを支持する
結果ではありません。

`practitioner_experience`と`not_tested`は両立します。この組み合わせは、実務経験を
成立根拠に持つ一方、このRepositoryでは独立検証していないことを示します。
「根拠なし」または「検証済み」と読み替えません。

## Evidence Coverageと残存リスク

複数の不確実性を含むHypothesis Episodeは、`検証対象の分解`で`U1`、`U2`のような
小さな検証対象に分けます。

- `Coverage state`: どの範囲を確認したか
- `Finding`: 現在のEvidenceが何を示すか
- `Applicability`: Evidenceを対象条件へどの程度適用できるか
- `Residual uncertainty`: 確認後も残る不確実性

Coverageは仮説が正しい割合ではありません。検証対象で参照するEvidenceは原則として
Observationとし、経験知、外部Research、直接観察などの性質はObservation側の
`knowledge_basis`を確認します。

残存リスクへの人間の対応判断は`04_decisions/risk-decisions/`に分離します。
`proceed_with_risk`は限定した範囲で先へ進む判断であり、Hypothesisの`supports`、
Analysisの採用、Artifactへの採用を意味しません。

### 現在の検証状況

| Hypothesis Episode | Scope | Components | Coverage | Current Risk Decision |
| --- | --- | ---: | --- | --- |
| [AudienceがActionを持ち帰るSession Value](./hypothesis-episodes/HYP-20260804-183208-audience-actionable-ai-slop-value.md) | `session` | 5 | すべて`not_checked` | なし |
| [一続きの説明によるSession Solution](./hypothesis-episodes/HYP-20260804-183209-ai-slop-learning-path-solution.md) | `session` | 5 | すべて`not_checked` | なし |
| [一枚とRepositoryへの導線によるSession Feature](./hypothesis-episodes/HYP-20260805-001809-repository-handoff-preserves-focus.md) | `session` | 4 | すべて`not_checked` | なし |
| [下流負荷の制御を提供側の価値と利用者の受入条件として扱うPractice Value](./hypothesis-episodes/HYP-20260804-183210-ai-slop-downstream-burden-value.md) | `practice` | 7 | U1・U2・U4・U5・U6は`partially_checked`、U3・U7は`checked_for_current_scope` | なし |
| [価値選択と検証のPractice Solution](./hypothesis-episodes/HYP-20260730-015718-ai-speed-requires-value-validation.md) | `practice` | 3 | すべて`not_checked` | なし |

他のHypothesis Episodeには、現在Validation Component表がありません。Risk Decision
Nodeはまだ作成されていません。これはRiskが存在しないことではなく、人間による
対応判断がまだ記録されていないことを示します。

## Observation一覧

| Observation | Knowledge Basis | Status | Confidence | 現在の接続先 |
| --- | --- | --- | --- | --- |
| [セッション成功条件と参加者Journeyの原案](./observations/OBS-20260730-015714-session-goal-and-journey.md) | `recorded_statement` | `reviewed` | `high` | 採用済みJourney／Value Stream |
| [採択済み方向性とDeliveryの検討範囲](./observations/OBS-20260730-015715-accepted-direction-and-delivery-scope.md) | `external_research`, `recorded_statement` | `reviewed` | `high` | 採択シグナルHypothesis、Value Hypothesis、採用済みJourney |
| [Audienceと価値課題について記録された見立て](./observations/OBS-20260730-015716-audience-and-value-problem-statements.md) | `recorded_statement` | `reviewed` | `high` | 採択シグナルHypothesis、Value Hypothesis |
| [BCG資料内で10–20–70の説明対象が変化している](./observations/OBS-20260730-210822-bcg-10-20-70-claim-variation.md) | `external_research` | `reviewed` | `high` | 現時点ではHypothesis／Artifactへのrelationなし |
| [リレー中心の構成候補を形成した要素と表現選択](./observations/OBS-20260731-021631-relay-story-source-elements.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `high` | リレー中心のSession Story Hypothesis |
| [価値判断と受け手のSlop経験を分ける判断Flowが記録された](./observations/OBS-20260731-120412-value-and-slop-experience-decision-flow.md) | `practitioner_experience` | `reviewed` | `high` | 作成者の現場実践として確認済み、Slide構成には未採用 |
| [Platform Serviceの提供側と利用側を接続して観測する考えが記録された](./observations/OBS-20260801-004820-coupled-platform-value-streams.md) | `reasoned_synthesis` | `reviewed` | `high` | DVSとOVSを接続したObservability Hypothesis |
| [ハンドオーバーとContractとCost Transferを分ける考えが記録された](./observations/OBS-20260801-004821-contract-accountability-cost-transfer.md) | `external_research`, `reasoned_synthesis` | `reviewed` | `high` | Service Contract Hypothesis |
| [Solution候補からChallengeとValue Hypothesisを再構成する技法が記録された](./observations/OBS-20260802-230422-solution-first-hypothesis-reconstruction.md) | `case_recollection` | `reviewed` | `high` | Solution-first再構成Hypothesis |
| [Platform Advisorには利用者がPlatformを選びたいという隠れた前提が記録された](./observations/OBS-20260802-230424-platform-choice-hidden-assumption.md) | `practitioner_experience` | `reviewed` | `high` | Platform選択負荷のValue Hypothesis |
| [プロジェクトと変革の失敗率は対象と成功定義が異なり統合できない](./observations/OBS-20260802-230426-failure-rate-definition-mismatch.md) | `external_research` | `reviewed` | `high` | 登壇での利用判断とは分離 |
| [Process上のFlowと最終成果物のOutcome Qualityは別の観測対象として記録された](./observations/OBS-20260802-230427-process-flow-and-outcome-quality.md) | `reasoned_synthesis` | `reviewed` | `high` | 測定方法と接続先は未決定 |
| [Solution-first再構成の有無でTraining中の記述とIdea数に異なる様子が記録された](./observations/OBS-20260804-004530-solution-first-training-behavior.md) | `case_recollection`, `direct_observation` | `reviewed` | `medium` | 既存Solution HypothesisのContext、Validation Resultには不使用 |
| [仮説検証を不確実性の分解と意思決定更新として扱う説明が記録された](./observations/OBS-20260804-004531-hypothesis-validation-uncertainty-decision.md) | `reasoned_synthesis` | `reviewed` | `high` | Lean Startup HypothesisのContext |
| [前回登壇で対象Journeyを特定し今回VSM・MBPMへ展開する前後関係が記録された](./observations/OBS-20260804-004532-journey-before-vsm-mbpm.md) | `external_research`, `recorded_statement` | `reviewed` | `high` | 前回登壇と今回の検討範囲の接続 |
| [Customerへの確認ではDiscovery結果が未定義または担当者に理解されていなかった](./observations/OBS-20260804-013221-discovery-practice-gap.md) | `practitioner_experience` | `reviewed` | `medium` | Solution-firstが起こる背景となる限定的な経験知 |
| [Slopとして経験される摩擦にも残す目的があり得ると整理された](./observations/OBS-20260804-013222-necessary-friction-boundary.md) | `reasoned_synthesis` | `reviewed` | `medium` | 価値とSlop経験を分ける判断Flowの境界条件 |
| [Dashboardと分析を分ける運用がITSMとProject Portfolioで用いられた](./observations/OBS-20260804-013225-itsm-metrics-analysis-practice.md) | `practitioner_experience`, `case_recollection` | `reviewed` | `medium` | 二段階メトリック分析Hypothesis |
| [今回のProblem Spaceは2026年4月公開記事に記録され、後続準備で実践方法が追加された](./observations/OBS-20260804-014228-prior-article-session-continuity.md) | `external_research`, `recorded_statement`, `reasoned_synthesis` | `proposed` | `high` | 先行する自己資料と今回の実践方法の連続性 |
| [Workslopの受け手は追加作業と信頼低下を自己申告している](./observations/OBS-20260805-001807-workslop-recipient-burden.md) | `external_research` | `reviewed` | `high` | Practice Value U6への`analogous`な限定Evidence、U1への適用候補 |
| [良いハンドオーバーには受け手の判断に必要なContextが含まれると整理された](./observations/OBS-20260805-001808-decision-context-handover.md) | `case_recollection`, `reasoned_synthesis` | `reviewed` | `medium` | Service Contract Hypothesisを補助するContext |
| [個別Enablementの反復はService設計の人力補完を示す兆候として整理された](./observations/OBS-20260805-001810-repeated-enablement-dependency-signal.md) | `reasoned_synthesis` | `reviewed` | `medium` | Service Contract、Persona、Service Scopeの未検証Signal |
| [提案書の生成短縮後に別担当者へ検証・再構築・意味変換の作業が移り生成停止が判断された](./observations/OBS-20260804-195508-ai-proposal-generation-shifted-review-burden.md) | `case_recollection`, `explicit_validation` | `reviewed` | `medium` | Practice ValueのU1・U2・U3・U4・U7に対する`analogous`な限定Evidence |
| [下流負荷制御の優先度はServiceの目的とOutputの可逆性に依存すると整理された](./observations/OBS-20260805-005540-downstream-control-priority-reversibility.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `medium` | Practice ValueのU5・U6に対する`contextual`な境界条件 |

`knowledge_basis`は成立根拠の種類、`confidence`は確率ではなく確信度、
`result`は実施した検証の結果です。互いに置き換えず、根拠と詳細な限界は
リンク先を確認します。

## 採用済みArtifact

- [参加者Journey兼Value Stream](../03_artifacts/attendee-journey.md)
  - `adopted_by: human:kijima`
  - 発見・選択、参加、復習、現場適用までを対象とする現在の正本
- [Value Stream](../03_artifacts/value-stream.md)
  - 参加者Journeyを正本として参照する短いCanonical Entry

現在のSession Story、Slides、Speaker Notes、Participant Takeawayは未採用です。

## まだRaw Noteにだけ存在する主要テーマ

次のRaw Noteには、現在のAnalysisまたはArtifactから直接のtyped relationが
ありません。これは却下を意味せず、未昇格または別経路で扱っている状態です。

- [PEK2026プレゼンテーション候補ネタ集](../01_working/raw-notes/RN-20260730-093311-presentation-idea-inventory.md)
- [Workモード引き継ぎからのプレゼンテーション追加候補](../01_working/raw-notes/RN-20260730-095321-work-mode-idea-supplement.md)
- [リレー比喩でシステム思考を説明する設計判断](../01_working/raw-notes/RN-20260802-215509-relay-metaphor-as-systems-thinking-translation.md)

## Patternの状態

現在、Patternは0件です。

14件のHypothesis Episodeは異なる範囲を扱っており、複数Episodeを横断して
繰り返し検証された関係はまだ記録されていません。Indexを埋める目的でPatternを
作らず、複数の検証結果と反例確認が揃ったときに提案します。

## 未解決事項

- AudienceがAI Slopを制御するActionを持ち帰ることに価値を感じるかは
  `not_tested`です。
- 構造、Signal、仮説検証を一続きに説明するSession Solutionが、Audienceの
  理解とAction選択を改善するかは`not_tested`です。
- AI高速化による下流負荷を特定・制御・削減できる状態のPractice Valueは、
  Consulting提案書の一件によりU1・U2・U4が`partially_checked`、U3・U7が
  `checked_for_current_scope`になりました。Workslop受け手負荷の外部Researchにより、
  U6も`partially_checked`です。実践者の条件整理によりU5も`partially_checked`となり、
  U6にはOutputの検知可能性、可逆性、回復Costおよび反復量の境界を追加しました。
  実際のPlatform TeamによるCapacity配分、採用率との関係、Platform利用者の行動および
  Platform Serviceへの直接適用は未確認です。
- 価値選択と検証によって回避可能な下流Costが減るというPractice Solutionは、
  3 Componentsすべてが`not_checked`です。
- Lean Startupの選別と早期廃棄をAdmission Controlとして使うSolution
  Hypothesisは `not_tested` のままです。
- PEのDVSと利用者側OVSを接続した観測が、局所指標より早くCost Transferを検知
  できるかは `not_tested` です。
- 共有前のService Contract明確化が、受け手の理解、検証、判断Costを減らすかは
  `not_tested` です。
- Solution-firstからの再構成が、教科書的順序または人間だけのReviewより検証可能な
  仮説を作りやすいかは `not_tested` です。
- Solution-first再構成の有無が異なるTraining記録は、条件が揃っておらず、手法の
  効果検証には使えません。
- 仮説検証を不確実性の分解として説明することが、参加者の理解や意思決定を
  改善するかは未確認です。
- Journey特定後にVSM・MBPMへ展開する今回の順序が、課題抽出やPriority判断を
  改善するかは比較されていません。
- Customerへ目的とDiscovery結果を質問した経験はありますが、質問件数と一次記録を
  備えた調査ではなく、組織で未定義なのか担当者が理解していないのかは区別できません。
- Value Streamの課題とOutcomeからAI Capabilityを配置する方法が、AI Use Caseから
  始める方法より局所最適を避けやすいかは `not_tested` です。
- Slopとして経験される摩擦のうち、何を残すべきかを判定する方法と効果は
  未確認です。
- 異常検知と原因診断を分ける運用はITSMとProject Portfolioの経験に基づきますが、
  過去の一次資料は未確認で、Platform Engineeringでの実践は導入初期です。
- DashboardとDataからFactを取り出すために必要な分析Technique、習熟度、Training
  方法は未定義です。
- Platform利用者のどのSegmentが選択肢より標準Pathと選択負荷軽減を重視するかは
  `not_tested` です。
- Outcome、Experience、Trust、Contract Qualityの具体的なMetricと、MBPMへ
  組み込むScopeは未定義です。
- Session Featureであるリレー中心の25分トークは、Walkthrough、代替案比較、
  第三者Reviewが未実施です。Practice scopeのFeature Hypothesisはまだありません。
- Human-AI協業を一枚とRepositoryへの導線に限定するSession Featureは、Focus維持、
  Repositoryの役割理解、登壇後の閲覧およびAction選択の4 Componentsが未確認です。
- BetterUpのWorkslop調査は受け手の自己申告を扱いますが、Platform Engineeringへの
  適用、AI利用との因果および対策の効果は確認していません。
- 判断Contextを渡すHandoverと、個別Enablementの反復を人力補完のSignalとして扱う
  整理は、事例記憶またはReasoned Synthesisであり、比較Caseで検証されていません。
- 想定Audienceの課題と参加者Journeyは、参加者への直接確認を経ていません。
- 現場適用、Live Document、Takeawayの有効性は未検証です。

## 更新するタイミング

次の場合に、NodeとArtifactを再読してこのIndexを再生成します。

- Observation、Hypothesis Episode、Patternを追加または実質変更したとき
- status、knowledge_basis、confidence、result、hypothesis_scope、
  hypothesis_level、relation、Validation Componentが変わったとき
- Risk Decisionを追加、置換、撤回したとき
- Artifactを採用、更新、置換したとき
- 人間が現在の全体像やReasoning Chainの整理を依頼したとき
