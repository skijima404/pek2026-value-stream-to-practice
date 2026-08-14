---
id: EXT-20260813-224201-safe-outcome-driven-product-development
type: external_input
title: "Scaled Agile Framework「Outcome-Driven Product Development in AI-Native SAFe」"
content_language: ja
created_at: 2026-08-13T22:42:01+09:00
created_by: agent:codex
source_type: user_provided_print_to_pdf_and_official_webpage
original_filename: "Outcome-Driven Product Development in AI-Native SAFe - Scaled Agile Framework.pdf"
source_url: https://framework.scaledagile.com/ain-safe-outcome-driven-product-development-in-ai-native-safe
retrieved_at: 2026-08-13T22:42:01+09:00
retrieval_method: user_provided_print_to_pdf_from_authenticated_official_webpage
provided_by: human:kijima
changeability: externally_managed
publication_date: 2026-06-30
source_last_updated: 2026-06-30
input_sha256: 8e1d550ad2f29bfe8c418a0f9219032822ea5aa631cb504ff01392978a547018
license: all_rights_reserved
asset_in_repository: false
asset_omission_reason: redistribution_not_authorized
relations:
  - type: references
    target: EXT-20260813-223151-safe-ai-innovation-pipeline
---

# Scaled Agile Framework「Outcome-Driven Product Development in AI-Native SAFe」

## 位置づけ

Scaled AgileがAI-Native SAFeの一部として公開する、Output中心のProduct Developmentから
Outcome中心のProduct Developmentへ移行する理由、Cycle、Outcome TreeおよびOKRの設計を
説明した公式記事である。

本ノードは記事の記載内容を後から参照できるようにするためのExternal Inputである。
ここに記録した内容はScaled AgileのGuidanceであり、このRepositoryの仮説が検証済み、
または登壇内容へ採用済みであることを意味しない。

## 書誌情報

- 発行元: Scaled Agile, Inc.
- 記事名: `Outcome-Driven Product Development in AI-Native SAFe`
- 公式URL:
  https://framework.scaledagile.com/ain-safe-outcome-driven-product-development-in-ai-native-safe
- 公開日および記事に表示された最終更新日: 2026年6月30日
- 提供されたPDF: 18ページ、Letter、432,883 bytes
- PDF作成日時: 2026年8月13日21時54分56秒（JST）
- PDF作成環境: FirefoxからmacOS Quartz PDFContextへの印刷保存
- 記事が参照する資料:
  Mik Kersten, `Output to Outcomes`, IT Revolution, 2026

## 提供されたPDFの由来

公式URLでは記事全文の閲覧にLoginが必要である。提供者がLogin済みの公式記事を
FirefoxからPDFとして保存し、この調査へ提供した。

PDFでは記事Title、Canonical URL、本文、Figure 1からFigure 2、Table 1からTable 5、
Reference、Key Takeaways、最終更新日およびScaled Agileの著作権表示を確認した。
提供ファイルの同一性確認にはfrontmatterの`input_sha256`を使用する。

## OutputからOutcomeへ移る理由

PDF 1ページから3ページでは、AIによってDigital Productを作るCostが大きく下がった環境では、
FeatureをReleaseすること自体は差別化要因ではなくOutputにすぎず、Validated Outcomeへ
焦点を移す必要があると説明している。

記事は、AIによるProduct Developmentの高速化によって、整合していないFeatureを大量に作り、
Customer Experience、Commercial PerformanceおよびResponsible AIへ悪影響を与えるRiskが
高まるとしている。Output-DrivenとOutcome-Drivenの違いをTable 1で次のように整理する。

| Aspect | Output-Driven | Outcome-Driven |
| --- | --- | --- |
| Focus | 事前に決めたFeatureをReleaseする | 特定のCustomerまたはBusiness Outcomeを達成する |
| Measurement | Flow Metric、Code Commit、Release Date | Customer Impact、Retention、Profit、Revenue |
| Roadmap | 何をいつ作るかを示すFeature中心 | なぜ作り、どのValueを届けるかを示すOutcome中心 |
| Completion | Featureが実装・Releaseされた | Impactが生まれ、Validated Learningが適用された |

記事は、この移行によって、利用されないFeatureを追加し続ける`build trap`を避け、Teamが
Customer Problemを解く方法を考え、TeamとARTをまたいだAlignmentとSystems Thinkingを
促進できるとしている。

Table 1はMeasurementの重点を比較したものであり、記事がFlow Metricを不要としているとは
記載されていない。後述のCycleでは、Outcomeへの寄与、因果と相関の区別、Feasibility、Risk、
LearningおよびCounter-effectを確認するGranular Metricも扱っている。

## Outcome-Driven Product Development Cycle

PDF 3ページから5ページでは、Mik KerstenのOutcome Loopを発展させたCycleを示している。

```text
Outcomes
  -> Priorities
  -> Outputs
  -> Measurements
  -> Value
  -> Feedback
```

Cycleの各要素は次の役割を持つ。

- `Outcomes`: Strategyが目指すDestinationとStrategic Intentを明示する
- `Priorities`: FundingまたはCapacityをどのOutcomeへCommitするかを決める
- `Outputs`: Product、Solution、Feature、Prototype、EnablerまたはExperimentを作る
- `Measurements`: Outputが期待Outcomeを動かしたかを観測し、継続または停止を判断する
- `Value`: Customer Outcomeと、それが生むBusiness ResultおよびROIを具体化する

記事は、ProductとSolutionもOutcomeを生むまではOutputであり、購入されないProductまたは
利用されないFeatureは、まだOutcomeにつながっていないとする。また、Outputを作る前に、
それが動かすべきMetricを理解する必要があると述べる。MetricはOutcome Measureへの直接Mapping、
または因果と相関を区別するためのより細かなMeasureになり得る。

## Outcome Treeと時間軸

PDF 5ページから7ページでは、AIがOutputを高速に生成するほど、間違ったProductを作るRiskが
高まるため、日々の仕事をStrategyへ接続するOutcome Treeが必要だと説明している。

Outcome Treeは次のLevelとTime Horizonを接続する。

| Level | Scope | Time Horizon | Created by | Approved by |
| --- | --- | --- | --- | --- |
| Portfolio Outcomes | Portfolioが組織Strategyへ行う貢献 | Strategic Investment Cycle、通常は年単位 | Portfolio Leadership | Organizational Executives |
| ART Outcomes | ARTがPortfolio Outcomeへ行う貢献 | Strategic Investment Cycle | ART Leadership、Business Owners | Portfolio Leadership |
| PI Outcomes | 次のPIでART Outcomeを最も進めるFocus | PI Cycle | ART Leadership、特にProduct Management | Business Owners |
| Team Outcomes | TeamがARTのPI Outcomeへ行う貢献 | PI Cycle | AI-Native Teams | Business Owners |

上位から下位へPurposeを伝え、下位から上位へCommitmentを伝える構造によって、異なる
時間軸のOutcomeを接続する。記事は、OutcomeとEvidenceの変化に応じて、この接続を
形成・維持する必要があるとしている。

## OKRによるOutcomeの表現

PDF 7ページ以降では、Objectiveを達成したいOutcomeと`What and Why`、Key Resultを
達成をどう確認するかとして説明する。一つのObjectiveに通常2から5のKey Resultを置き、
Evidenceが得られたらGoalを見直せる速いCadenceを重視する。

記事は、Key ResultをOutputではなく作るValueに基づいて定義し、途中でも程度を測定できる
Measurableなものにするよう求める。Destination到達時にしか読めないMeasureでは、途中で
Steeringできないためである。

## Value Creationの4分類

PDF 8ページから9ページでは、AI-Native Organizationが追求するValue Creationを次の4分類で
示している。

1. `Building Products and Services`: Customerへ提供するProductとServiceを改善する
2. `Scaling Growth`: Customer、MarketおよびRevenueへのReachを広げる
3. `Driving Operational Efficiencies`: Cost、Effortおよび日常業務のWasteを減らす
4. `Improving Quality / Mitigating Risk`: Quality、ComplianceおよびRisk Exposureを改善する

記事は、すべてを同じ比率で追求するのではなく、VisionとOutcome Tree上の関係に応じて
どの分類をどの組み合わせで選ぶかを明示的に決めるとしている。

## AmbitionとRiskの明示

PDF 9ページから10ページでは、ObjectiveのAmbitionとRiskを次の二つで表す。

- `Roofshot`: Lower-riskで、実現可能性が高い具体的な結果を目指す
- `Moonshot`: High-riskだが不可能ではないInnovationまたはStep Changeを目指す

記事は、従来の`committed`と`aspirational`というObjective分類を置き換えるものとしている。
CommitmentはObjectiveの属性ではなくPlanning後に行う行為であり、AmbitiousなObjectiveを
`aspirational`と呼ぶとCredibilityが低いように見える可能性があるためとしている。

## Balanced Key Results

PDF 10ページから13ページでは、一つのMetricだけを動かすと、その追求が別の害を生む可能性が
あるため、Counter-effectを監視するMeasureと組み合わせる必要があると説明する。

AI-Native SAFeは、Key Resultを次の3 Perspectiveで検討する。

- `Customer and Business`: CustomerとBusinessへValueが届くか
- `Feasibility and Risk`: Outcomeを達成可能か、追求すべきか、途中で何が失敗し得るか
- `Learning and Growth`: Outcomeを追求することで何を学び、組織がどのCapabilityを得るか

Feasibility and RiskおよびLearning and Growthでは、Outcomeが確定する前に行動できるLeading
Indicatorを重視する。Annual OutcomeではLeadingとLagging Indicatorを組み合わせ、PIとTeamの
Outcomeでは早期にSteering可能なLeading Indicatorを多くする傾向があるとしている。

記事の説明例には、Customer Outcomeだけでなく、Failed Handoff、Human Escalation、Safety
Incident、Service Level、Experimentで除外したOptionおよび次に安全に自動化できるDecisionを
Key Resultとして扱うものが含まれる。これらはFrameworkを説明する架空例であり、実測Caseではない。

## Strategic AlignmentとTeamの役割

PDF 13ページから15ページでは、Outcome TreeをOrganization内の`living strategic intent`を
運ぶ主要な仕組みとしている。Portfolio、ART、PIおよびTeamのObjectiveとKey Resultを接続し、
日常業務をCustomerおよびBusiness OutcomeへTrace可能にすることで、High-alignmentかつ
High-autonomyな状態を目指す。

記事は、技術的OutputがCommodity化する環境では、TeamはTop-downのTaskを実行する
`feature factory`を越え、日々の活動がBusinessとCustomer Valueへどう接続するかを理解する
Outcome-focused Partnerになる必要があるとする。ただし、すべてのEngineerがProduct Strategistに
なる必要があるとはしていない。

## この資料が支え得る範囲

このExternal Inputは、Scaled AgileがAI-Native Product Developmentについて次の構造を
公式Guidanceとして提示していることのReferenceになり得る。

- AIでOutput生成Costが下がるほど、Output量ではなくValidated Outcomeを管理する
- Outputを作る前に、それが動かすMetricを明確にする
- Release、利用、Impact、LearningおよびValueを別の状態として扱う
- Outcome、Investment Priority、Output、MeasurementおよびValueをFeedback Loopで接続する
- CustomerおよびBusiness Metricだけでなく、Feasibility、Risk、LearningおよびCounter-effectを観測する
- Teamの日常的なDecisionを上位OutcomeへTrace可能にする

一方、この資料だけでは、Outcome-Driven Product Developmentが特定のPlatform Teamで有効で
あること、下流Costを削減すること、記載されたOKR構造が他の方法より優れること、またはAudienceが
登壇内容として価値を感じることを検証できない。

## 限界

- 発行元によるFramework Guidanceであり、記載された構造の有効性を比較検証したResearchではない。
- 記事が示すOutcome Tree、Objective、Key Resultおよび自動配送の数値例は説明用であり、実際の
  Organization、調査設計、Sample、比較条件または測定結果を示すCase Studyではない。
- Outcome、Output、ValueおよびROIの境界は、具体的なContextで追加定義が必要になる。
- Outcome TreeとOKRによってAlignment、AutonomyまたはDecision Qualityが改善する因果を
  本文中で実証していない。
- 記事はOutcomeからPriorityへ至るDiscovery、Option比較およびDecision Processを独立した
  Stageとして詳述していない。
- 公式ページは発行元により変更される可能性があり、Login条件も変わり得る。
- PDFはWebpageの印刷Snapshotであり、公式に配布された静的PDFではない。

## PDF本体をRepositoryへ格納しない理由

PDFにはScaled Agile, Inc.の著作権表示があり、画像または本文の複製には明示的な許諾が
必要であると記載されている。再配布許諾を確認できないため、提供されたPDF本体は
Repositoryへ複製せず、Canonical URL、取得経路、書誌情報およびSHA-256を保存する。
