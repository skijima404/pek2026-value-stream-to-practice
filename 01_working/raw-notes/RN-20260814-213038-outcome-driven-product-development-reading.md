---
id: RN-20260814-213038-outcome-driven-product-development-reading
type: raw_note
title: "Outcome-Driven Product Developmentを検証可能なPlatformとして読む"
content_language: ja
created_at: 2026-08-14T21:30:38+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-14T21:35:10+09:00
sanitization_checked_by: agent:codex
tags: [ai-native-safe, feedback-loop, metrics, outcome-tree, outcome-validation, platform-engineering, product-management, value-realization]
relations:
  - type: derived_from
    target: EXT-20260813-224201-safe-outcome-driven-product-development
---

# Outcome-Driven Product Developmentを検証可能なPlatformとして読む

## この記録の位置づけ

Scaled Agile Frameworkの記事`Outcome-Driven Product Development in AI-Native SAFe`を読み、
Work Modeで残したReading CaptureとPost-reading Reflectionを再構成したRaw Noteである。

記事の書誌情報、本文上の定義、Figure、TableおよびLimitは、External Input
`EXT-20260813-224201-safe-outcome-driven-product-development`を正本とする。このRaw Noteでは、
記事への読者としての反応、Platform EngineeringとProduct Managementの責任境界、および説明への
利用候補を記録する。

添付Captureに含まれていた特定の資料名は、公開用Repositoryへ保存する必要がないため除外した。
その資料との対応関係は、このRaw Noteでは未確認として扱う。

以下のPlatform Engineering Boundary、Metric Ownership、Outcome Treeの実装Schemaおよび説明Sequenceは、
記事自身のClaimではなく読後の解釈と候補である。

## 読後の中心的な理解

AIによってDigital Productを速く作れること自体は、差別化になりにくくなる。多くのOrganizationが
高速にOutputを生成できるなら、競争力の源泉は、OutputをOutcomeへ変換する割合を高めることへ移る。

```text
Outputを速く作る
  -> 速いことは前提になる
  -> Outcomeへ変換できるOutputを選ぶ
  -> 実際のImpactを測る
  -> Learningを次のDecisionへ戻す
```

記事だけを読んだ時点では、どの程度すでに速度がCommodity化しているかの実感や測定値までは分からない。
それでも、「速く作る」から「正しいOutcomeを生む確率を上げる」へFocusを移す必要があるという
Problem Framingには納得感があった。

Outcome、Prioritization、Output、MeasurementおよびValueをつなぎ、各段階からFeedbackを返す必要がある。
Outcomeへつながらない大量のOutputは、Build TrapやAI Slopとして経験され得る。

## OutputからOutcomeへ

記事のOutput-drivenとOutcome-drivenの比較は保存しておきたい。

| Aspect | Output-driven | Outcome-driven |
| --- | --- | --- |
| Focus | 事前に決めたFeatureをReleaseする | 特定のCustomerまたはBusiness Outcomeを達成する |
| Measurement | Flow Metric、Commit、Release Date | Customer Impact、Retention、Profit、Revenue |
| Roadmap | 何をいつ作るかを示す | なぜ作り、どのValueを届けるかを示す |
| Completion | Featureが実装・Releaseされた | Impactが生まれ、Validated Learningが適用された |

この比較から、FeatureのCompletionとOutcomeの実現を同一視しないことが重要だと読んだ。Productまたは
Solutionも、Outcomeを生成するまではOutputである。

大量のFeatureを作っても、Customer ExperienceとCommercial Performanceを悪化させる可能性がある。
AIによってPoorly alignedなFeatureが大量に作られた状態は、受け手側から見たAI Slopの一形態として
理解できそうである。ただし、`AI Slop`というLabelは記事自身の定義ではない。

## Outcome-Driven Product Development Cycle

記事のCycleは次の関係を示す。

```text
Outcomes
  -> Priorities
  -> Outputs
  -> Measurements
  -> Value
  -> Feedback
```

読書時に保持したかった短い表現は次のとおりである。

- Outcomes articulate strategic intent.
- Prioritization commits investment.
- Products and solutions are outputs until they generate outcomes.
- Metrics measure how outputs are performing.
- Customer and business value make ROI concrete.

このCycleでは、Output、MeasurementおよびValueからFeedbackが返る点がよい。直線的にFeatureを作って
終わるのではなく、各段階で得られたSignalによってPriority、Outputおよび次のInvestmentを変えられる。

## Outputを作る前にMetricを決める

記事の`No output should be produced without an understanding of the metrics it should move`という
考え方に強く反応した。

MetricはRelease後に成果を報告するためだけのものではない。Outputを作り始める前に、次を明らかにする
ためのDesign Toolでもある。

- そのOutputは何を変えるつもりか
- どのActorのBehaviorまたは状態を変えるのか
- 期待した変化をどのSignalで確認するか
- OutputとOutcomeの間にどの因果仮説を置くか
- どのSignalが出なければ停止または変更するか

Metricを先に考えることで、誰のどのProblemを解くのか、作ろうとしているFeatureのScopeが適切かを
実装前に問い直せる。

## Build TrapとAI Slop

OutcomeへつながらないFeatureを作り続ける状態はBuild Trapである。AIはこのTrapを解消するとは限らず、
Output生成Costを下げることで、むしろ間違ったFeatureを大量に作れるようにする。

```text
Output生成が速くなる
  -> 作れるFeature数が増える
  -> 選択と停止が弱いと不要なOutputも増える
  -> Customer Experienceと下流の仕事を悪化させる
```

したがって、AI時代に必要なのはOutputを最大化する仕組みではなく、OutcomeへつながらないOutputを
早く見抜き、Learningへ変換し、停止または修正できる仕組みである。

## Platform EngineeringはOutcomeを定義しない

Outcomeと、それを検証するProduct固有のMetricはDomain Contextへ依存する。そのため、Platform
Engineeringが各ProductのOutcomeを定義するのは適切ではない。

読後の責任境界は次のように整理した。

### Product Management／Domain Teamが担うこと

- 目指すOutcomeを定義する
- Outcomeを検証するMetricを定義する
- OutputとOutcomeの間にある因果仮説を置く
- Resultを解釈し、継続、変更または停止を判断する
- 複数Productに共通する意味的なMeasurement Patternを発見する

### Platform Engineeringが担えること

- Measurement、StorageおよびVisualizationの共通基盤を提供する
- Feature Flag、段階的Release、A/B TestなどのValidation手段を提供する
- Hypothesis、Change、対象および実測ResultをTrace可能にする
- Guardrail、停止およびRollbackを実装可能にする
- 共通性が確認されたMeasurement Patternを再利用可能なPlatform Capabilityへ昇格させる

この境界を短く表すWorking Statementは次のとおりである。

> PdMが意味の共通性を発見し、PEが実装の共通性を引き取る。

これは記事から直接導かれるRole Definitionではなく、記事をPlatform Engineeringへ適用した読者側の
解釈である。

## PlatformはOutcomeを保証せず、検証Costを下げる

Platform EngineeringはOutcomeを直接生み出すPlatformを提供するのではなく、OutputがOutcomeへ
つながったかを検証できるPlatformを提供する。

成功確率を直接保証するのではない。間違ったOutputを早く見抜き、Learningを得て次のDecisionへ進む
ためのCostとTimeを下げる。

```text
Platform Capability
  -> Small Release／Experimentを容易にする
  -> MeasurementとEvidenceを取得する
  -> Outcomeへの寄与を解釈できる
  -> Continue／Change／Stopを早く判断する
```

この見方では、PlatformのValueはFeature Deliveryの速度だけでなく、Validation Loopを安全かつ低Costで
回せることにもある。

## Metric Ownership

Metricを一種類として扱わず、少なくとも次の二つへ分けると責任境界が見えやすい。

| Metric class | Primary owner | Examples |
| --- | --- | --- |
| Platform Standard Metric | Platform Engineering／Operations | Availability、Latency、Change Failure Rate、Deployment Frequency、Cost |
| Outcome Validation Metric | Product Management／Domain Team | Customer Behavior、Task Completion、Retention、Conversion、Business Time Reduction |

Platform Teamは、Outcome Validation Metricの意味をProduct Teamの代わりに決めない。一方、Product Teamが
毎回独自にMeasurement Infrastructureを作らなくても済むよう、収集、Storage、Visualization、Experiment
およびTraceabilityのCapabilityを提供できる。

## Measurement PatternのPromotion Flow

共通Metricを最初からPlatform Standardとして決めるのではなく、個別Productで意味を確認してから
昇格させる流れを考えた。

1. PdMがOutcomeとValidation Metricを定義する
2. 最初は個別Product内でMetricを実装して検証する
3. PEがMeasurement、Storage、VisualizationおよびExperimentの共通基盤を提供する
4. Product側で複数Productに共通する意味的Patternを見つける
5. 共通性が確認されたPatternをPEが標準Capabilityへ昇格させる

このFlowにより、Domain固有のMeaningを早期にInfrastructureへ固定することを避けつつ、実際に再利用できる
PatternをPlatformへ取り込める。

## Outcome Treeの読み

Outcome Treeは、Portfolio Outcome、ART Outcome、PI OutcomeおよびTeam Outcomeの親子関係、より正確には
Contribution Relationshipを表すGraphとして読める。

WBSのように作業を分解するのではない。下位Outcomeがどの上位OutcomeへContributionするかを表し、
Scope、Time Horizon、Created byおよびApproved byを接続する。

この違いは重要である。

```text
WBS
  -> 上位の作業を下位Taskへ分解する

Outcome Tree
  -> 下位Outcomeが上位Outcomeへどう貢献するかを示す
```

## Outcome TreeをTableで扱う候補

Outcome TreeをTableまたはRepository Nodeとして表す場合の候補Schemaを考えた。

| Field | Purpose |
| --- | --- |
| `outcome_id` | Stable Identifier |
| `parent_outcome_id` | 上位OutcomeへのContribution Relationship |
| `level` | Portfolio、ART、PIまたはTeam |
| `outcome_statement` | Intended Result |
| `metric` | Outcome Validation Metric |
| `owner` | Responsible RoleまたはTeam |
| `approver` | Approval Authority |
| `time_horizon` | Strategic Investment CycleまたはPI Cycle |
| `status` | Candidate State |
| `linked_outputs` | Outcomeを動かす予定のOutputまたはExperiment |

これはPossible Implementation Schemaであり、SAFe公式Schemaでも、このRepositoryへ採用したSchemaでもない。
特に`status`のEnum、OwnerとApproverの責任境界、および一つのOutcomeが複数の上位OutcomeへContributionする
場合の扱いは未検討である。

## Outcome Treeを説明に使う候補

短い説明Sequenceとして、次を考えた。

1. AI時代はOutputの生成速度だけでは差別化しにくい
2. AI-Native SAFe Outcome Treeを示す
3. PortfolioからART、PI、Teamへの接続を説明する
4. 同じ関係をTableで示し、Owner、Time HorizonおよびApproverを明確にする
5. 次の問いを提示する

> 自分たちの作業が何に貢献するかではなく、自分たちのOutcomeがどの上位Outcomeに貢献するか説明できますか？

Outcome Treeを新しいProcessとして追加するのではなく、PI ObjectiveとStrategic Intentの接続を説明する
補助線として扱う。

## RoofshotとMoonshot

記事のRoofshotとMoonshotの区別には既視感があった。

- Roofshot: Lower-riskで、実現可能性の高いTangibleなResultを狙う。Optimizationに適する
- Moonshot: High-riskだが不可能ではないStep Changeを狙い、現在のProblemの解き方を問い直す

この区別は、OutcomeのAmbitionとRiskを明示するために利用できる。ただし、どの比率で両者を持つべきか、
またはMoonshotが実際にInnovationを増やすかは、この記事だけでは分からない。

## 今後読みたいもの

- Mik Kerstenの`Output to Outcomes`
- AI-Native Portfolioの詳細
- Outcome Treeと既存のPI Objective、Strategic ThemeおよびPortfolio Managementとの関係
- Balanced Key ResultとCounter-effect Metricの具体的な設計

## この記録だけでは分からないこと

- AIによってFeature Delivery Speedがどの範囲でCommodity化しているか
- OutputをOutcomeへ変換する「割合」をどの単位と分母で測るべきか
- Platform CapabilityがOutcome ValidationのCostまたはLead Timeを実際に下げるか
- PdMとPEの責任境界が異なるOrganizationでも機能するか
- Measurement Patternを個別実装からPlatform Standardへ昇格させる判断条件
- Outcome TreeがAlignment、AutonomyまたはInvestment Decisionを改善するか
- 説明Sequenceが想定Audienceにとって理解しやすいか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
