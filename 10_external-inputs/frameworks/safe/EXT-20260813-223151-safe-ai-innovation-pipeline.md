---
id: EXT-20260813-223151-safe-ai-innovation-pipeline
type: external_input
title: "Scaled Agile Framework「AI Innovation Pipeline」"
content_language: ja
created_at: 2026-08-13T22:31:51+09:00
created_by: agent:codex
source_type: user_provided_print_to_pdf_and_official_webpage
original_filename: "AI Innovation Pipeline - Scaled Agile Framework.pdf"
source_url: https://framework.scaledagile.com/ain-safe-ai-innovation-pipeline
retrieved_at: 2026-08-13T22:31:51+09:00
retrieval_method: user_provided_print_to_pdf_from_authenticated_official_webpage
provided_by: human:kijima
changeability: externally_managed
source_last_updated: 2026-08-11
input_sha256: 4828ead8c7bf60ee14695442eefbd8a5b362309efb1ce8004eecbd6ee052d77d
license: all_rights_reserved
asset_in_repository: false
asset_omission_reason: redistribution_not_authorized
---

# Scaled Agile Framework「AI Innovation Pipeline」

## 位置づけ

Scaled AgileがAI-Native SAFeの一部として公開する、OutcomeからCustomerおよび
Business Valueへ至るProduct Lifecycleと、それを支える共通Capabilityを説明した
公式記事である。

本ノードは記事の記載内容を後から参照できるようにするためのExternal Inputである。
ここに記録した内容はScaled AgileのGuidanceであり、このRepositoryの仮説が検証済み、
または登壇内容へ採用済みであることを意味しない。

## 書誌情報

- 発行元: Scaled Agile, Inc.
- 記事名: `AI Innovation Pipeline`
- 公式URL:
  https://framework.scaledagile.com/ain-safe-ai-innovation-pipeline
- 記事に表示された最終更新日: 2026年8月11日
- 提供されたPDF: 6ページ、Letter、497,427 bytes
- PDF作成日時: 2026年8月13日21時53分50秒（JST）
- PDF作成環境: FirefoxからmacOS Quartz PDFContextへの印刷保存

## 提供されたPDFの由来

公式URLでは記事全文の閲覧にLoginが必要である。提供者がLogin済みの公式記事を
FirefoxからPDFとして保存し、この調査へ提供した。

PDFでは記事Title、Canonical URL、本文、Figure 1からFigure 7、Table 1、Reference、
Key Takeaways、最終更新日およびScaled Agileの著作権表示を確認した。提供ファイルの
同一性確認にはfrontmatterの`input_sha256`を使用する。

## AI Innovation Pipelineについて記事が述べていること

PDF 1ページでは、AI Innovation Pipelineを、意図したOutcomeをCustomerおよび
Business Valueへ変換するProduct Lifecycleとして説明している。Lifecycleは次の
5段階で構成される。

1. `Discover`: Problem、Intentおよび期待Outcomeを明確にし、Experiment、Prototype
   またはValueへ直接つながるFeatureのいずれを扱うかを決める
2. `Specify`: SpecificationとContextを明示し、人間とAI Agentが利用できる形にする
3. `Build`: Specificationに基づくOutputを作る
4. `Validate`: Outputを目的に照らして検証し、Featureなら有用性、適切性および
   Release可能性を確認する
5. `Release`: FeatureをProductionと利用者へ届け、実利用とTelemetryをLearningへ戻す

ExperimentとPrototypeは主にLearningを生み、FeatureとEnablerは主にCustomerおよび
Business Valueを生むものとして区別される。Learning-oriented Outputから十分な
Confidenceが得られた場合に、Value-oriented OutputへCommitするSet-basedな流れが
示されている。

## Pipelineを支える4つのComponent

PDF 2ページでは、Lifecycleを支える共通Capabilityを次の4つに分けている。

- `AI-Empowered Workflows`: 人とAgentがLifecycle上で協働するWorkflow
- `Embedded Policies`: Boundary、ApprovalおよびStopping RuleをWorkflowへ埋め込むPolicy
- `Insights and Evidence`: Decision、ActionおよびDataのAudit Trailと、それらから得るInsight
- `Shared Platforms`: Workflow、Policy、Insight、EvidenceおよびDataを接続・構成・拡張する基盤

記事は、4つを独立した部品ではなく、相互作用によって価値を持つものとして説明する。
WorkflowはIntent、Specification、ContextおよびCurated Dataを利用し、Policyの制約下で
実行され、Evidenceを生成し、Insightを次の判断へ返す。Shared Platformは、それらを
接続して再利用可能にする。

## AI-Empowered Workflowの品質

PDF 3ページでは、AI-Empowered Workflowに必要な品質を次の5つとしている。

- `Grounded`: Intent、Specification、Contextおよび関連するCurated Dataに基づく
- `Connected`: 他のAgent、Workflow、SystemおよびShared Platformと接続できる
- `Controlled`: 適用されるPolicyの範囲内で動く
- `Auditable`: AuditおよびReviewに必要なInsightとEvidenceを生成する
- `Owned`: 維持と進化に責任を持つOwnerが明確である

記事は、ControlとAuditabilityをResponsible AIの前提とし、GroundingとConnectionの
品質および範囲がWorkflowのPotential Benefitを左右すると述べている。

## Processを明文化する理由

PDF 4ページでは、組織には文書化されたProcessと、実際に仕事が行われるProcessが
存在すると説明している。人間はTacit KnowledgeとSituational Judgmentによって両者の
Gapを補えるが、AI Agentは、不完全なProcessを与えられると不足部分を推測で補い、
不整合、安全でない近道または誤りを生む可能性がある。

そのため、記事はAIを利用するProcessを明文化、採用、進化させ、完了後に何を行うかまで
定義する必要があるとしている。この記述は、明文化だけでProcess品質やOutcomeが改善する
という実証結果ではなく、AI-Native Workflow設計上のGuidanceである。

## Embedded Policiesについて記事が述べていること

PDF 4ページでは、Policyを次の3分類で示している。

1. PerformanceやSecurityなど、SolutionまたはWorkflowが持つべきSystem Quality
2. Encryption ProtocolやRegulatory Obligationなど、満たすべきStandard
3. Definition of DoneやApproval Gateなど、満たすべきCheck

PolicyをMachine-readableにしてWorkflowへ適用し、Authorityの上限に達した場合は
より高いAuthorityを持つ人間へEscalateする。Human-in-the-loopとHuman-on-the-loopを
使い分け、AgentのAccessおよびAuthorityは狭い範囲から開始し、信頼できる実績に応じて
拡張し、Failureによって縮小または撤回する考え方を示している。

## InsightsとEvidenceについて記事が述べていること

PDF 4ページでは、EvidenceをWorkflow内の人間とAgentが行ったAction、Decisionおよび
利用したDataのAudit Trailとして扱う。Model、Prompt、Tool、Data Version、AI Eval、
Automated Check、Experiment、Prototype、Feature利用などがEvidenceのSourceになり得る。

記事は、Evidenceを起きたことの記録、InsightをEvidenceの分析から得る価値として区別する。
Insightの例として、Root Causeの特定、Hypothesisの確認または反証、Flowを妨げる
Bottleneckの発見を挙げる。得られたInsightは次のOutputを定義するIntentとContextへ戻される。

## Shared Platformについて記事が述べていること

PDF 4ページから5ページでは、Shared PlatformをAI Innovation Pipelineの`control plane`
として説明している。主な機能は次のとおりである。

- Team、ART、Portfolio LeadershipおよびAgentをWorkflowへ接続する
- WorkflowへEmbedded Policyを適用する
- 一つのWorkflowから次のWorkflowへ作業をRoutingする
- 適切なInsightを提供する
- 実行されたStepとDecisionをEvidenceとして蓄積する

PlatformはWorkflow、AgentおよびPolicyの共通Baselineを提供しつつ、Localな適応を共有側へ
戻せる構造を取る。共通ServiceやData Connectivityを再利用可能にし、Team固有のWorkflowと
Agentも同じFoundation上で接続する。

Workflow間で仕事を渡す際には、Intent、Current Version、DecisionおよびEvidenceを含む
Contextも運ぶ必要があるとされる。人間同士ではTacit Knowledgeとして補える情報でも、
Agentには明示的に提供する必要がある。Platformは過去のSignalとPatternをInsightとして示し、
実施内容、Decision、参照DataおよびActorをEvidenceとして後から利用可能にする。

## この資料が支え得る範囲

このExternal Inputは、Scaled AgileがAI-Native Product Developmentについて次の構造を
公式Guidanceとして提示していることのReferenceになり得る。

- AIによるOutput生成と、LearningまたはValueの実現を分ける
- Workflow、Policy、Evidence、InsightおよびShared Platformを一体で設計する
- Evidence収集を目的化せず、Root Cause、HypothesisおよびBottleneckに関するInsightへ接続する
- AgentへのHand-overでIntent、DecisionおよびEvidenceを明示的に運ぶ
- Shared Platformを個別Toolの集合ではなく、共通CapabilityとControl Planeとして扱う

一方、この資料だけでは、これらの構造が特定のPlatform Teamで有効であること、下流Costを
削減すること、Audienceが登壇内容として価値を感じること、または他の設計より優れることを
検証できない。

## 限界

- 発行元によるFramework Guidanceであり、記載された構造の有効性を比較検証したResearchではない。
- 記事内のWorkflow、Planning AgentおよびCustomer Win-backの例は説明例であり、調査設計、
  Sample、比較条件または測定結果を示すCase Studyではない。
- `Grounded`、`Connected`、`Controlled`、`Auditable`、`Owned`の5品質が、すべての
  AI Workflowに対して十分または必要であることを実証していない。
- 公式ページは発行元により変更される可能性があり、Login条件も変わり得る。
- PDFはWebpageの印刷Snapshotであり、公式に配布された静的PDFではない。

## PDF本体をRepositoryへ格納しない理由

PDFにはScaled Agile, Inc.の著作権表示があり、画像または本文の複製には明示的な許諾が
必要であると記載されている。再配布許諾を確認できないため、提供されたPDF本体は
Repositoryへ複製せず、Canonical URL、取得経路、書誌情報およびSHA-256を保存する。
