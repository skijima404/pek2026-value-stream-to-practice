---
id: EXT-20260813-224814-safe-ai-value-architect
type: external_input
title: "Scaled Agile Framework「AI Value Architect」"
content_language: ja
created_at: 2026-08-13T22:48:14+09:00
created_by: agent:codex
source_type: user_provided_print_to_pdf_and_official_webpage
original_filename: "AI Value Architect - Scaled Agile Framework.pdf"
source_url: https://framework.scaledagile.com/ain-safe-ai-value-architect
retrieved_at: 2026-08-13T22:48:14+09:00
retrieval_method: user_provided_print_to_pdf_from_authenticated_official_webpage
provided_by: human:kijima
changeability: externally_managed
publication_date: 2026-07-14
source_last_updated: 2026-07-14
input_sha256: 35fb87735d33353a0458cbef61c79f3fe06fe12c25bcce6b9eeeaeae60906443
license: all_rights_reserved
asset_in_repository: false
asset_omission_reason: redistribution_not_authorized
relations:
  - type: references
    target: EXT-20260813-223151-safe-ai-innovation-pipeline
  - type: references
    target: EXT-20260813-224201-safe-outcome-driven-product-development
---

# Scaled Agile Framework「AI Value Architect」

## 位置づけ

Scaled AgileがAI-Native SAFeの一部として公開する、AI SolutionをPrototypeから継続利用と
Business Outcomeへ接続するための`AI Value Architect`という役割を説明した公式記事である。

本ノードは記事の記載内容を後から参照できるようにするためのExternal Inputである。
ここに記録した内容はScaled AgileのGuidanceであり、このRepositoryの仮説が検証済み、
または登壇内容へ採用済みであることを意味しない。

## 書誌情報

- 発行元: Scaled Agile, Inc.
- 記事名: `AI Value Architect`
- 公式URL: https://framework.scaledagile.com/ain-safe-ai-value-architect
- 公開日および記事に表示された最終更新日: 2026年7月14日
- 提供されたPDF: 14ページ、Letter、921,031 bytes
- PDF作成日時: 2026年8月13日21時54分16秒（JST）
- PDF作成環境: FirefoxからmacOS Quartz PDFContextへの印刷保存
- 記事のReference欄に記載された資料:
  Kweilin Ellingrud, `A New Year's Resolution for Leaders: Redesign Work for
  People and AI`, McKinsey & Company, 2026年1月8日

## 提供されたPDFの由来

公式URLでは記事全文の閲覧にLoginが必要である。提供者がLogin済みの公式記事を
FirefoxからPDFとして保存し、この調査へ提供した。

PDFでは記事Title、Canonical URL、本文、Figure 1からFigure 4、責務、候補Role、Reference、
Key Takeaways、最終更新日およびScaled Agileの著作権表示を確認した。提供ファイルの
同一性確認にはfrontmatterの`input_sha256`を使用する。

## 記事が定義する課題と役割

PDF 2ページでは、AI InitiativeがPrototypeからProductionへ進む道筋、Data、Operation、Risk、
AdoptionおよびValue Measurementを一体として扱う主体が不明確なため、技術的に有望な
DemonstrationがScaleまたは継続利用へ至らない状態を`POC Graveyard`と表現している。

記事は、既存責務の横でTeamごとにAIを導入すると、局所的な最適化と断片的なApproachに
なりやすく、AI Solution DevelopmentにはSystems Viewが必要だとする。AI Value Architectを
ART上の専任Roleとして置き、Team、複数Team、特定SolutionまたはART全体を支援する構成を示す。

記事によると、このRoleはBusiness Owner、AI DeveloperまたはFacilitatorのいずれか一つではない。
Businessを理解し、AIについて専門家と対話でき、Business、Engineering、DataおよびRiskの間を
Facilitateする役割として、次の5領域を担う。

1. `Coaching AI Adoption`
2. `Unlocking Value from AI Workflows and Tools`
3. `Bridging Business and Technology`
4. `Facilitating AI Solution Development`
5. `Optimizing Outcomes`

## Coaching AI Adoption

PDF 4ページから5ページでは、ToolへのAccessや一回限りのTrainingだけでは利用定着に
つながらないとしている。AI Value Architect自身がModel、Agent、Retrieval、Prompt、Evaluation、
RiskおよびConstraintについて、専門家に適切な質問をし、Assumptionを見つけられる水準の
AI Fluencyを持つことを求める。

Teamに対しては、日常業務のどこでAIを使うか、使わないか、Outputをどう評価するか、Dataを
どう保護するか、AI利用をどう開示するか、Workflowをどう反復するかをCoachする。記事は、
この活動を次の`AI-Native Success Factors`へ接続する。

1. `Anchor AI to Business Value`
2. `Upskill Relentlessly`
3. `Start Smart, Include AI Early`
4. `Move Fast, Learn Fast`
5. `Provide Context for AI`
6. `Embed AI into the Everyday`
7. `Innovate Boldly, Govern Wisely`

## AI Workflowと既存ToolからValueを引き出す

PDF 5ページから6ページでは、組織がすでに承認または導入したAI Platform、Copilot、組込み機能、
利用状況およびWorkaroundを把握し、未利用または低利用のCapabilityを見つけるとしている。
Model Release、Feature UpdateおよびPolicy Changeを追跡し、古くなったGuidanceを廃止し、
Teamで観測したFeedbackをPlatform Ownerへ返す。AI Value Architectを、ARTにおける共通AI
PlatformのLocal Championとして位置づけている。

また、既定設定のCopilotまたはAgentをそのまま適用するのではなく、Team固有のDomainと
Outcomeに合わせてPrompt、Workflow、Data ConnectionおよびEvaluation Practiceを調整する。
そのLocal Adaptationは、組織のGovernance、SecurityおよびCostのBoundary内に保つとしている。

## BusinessとTechnologyを接続する

PDF 6ページから7ページでは、AI Initiativeを開始する前に、Business Stakeholderとともに
Outcome、Intent、ContextおよびSuccess Measureを定義し、追加ResourceをCommitする前に必要な
FeedbackとValidationを明確にするとしている。

同時に、Cost、LatencyおよびAccuracyに関するConstraintを明示し、期待と技術的Capabilityを
整合させる。System Architect、Product ManagerおよびTeamが、AgentのAutonomy、Human Approvalの
Threshold、BiasとFairnessおよびAudit Evidenceを含むAI固有のGovernanceを扱えるよう支援し、
要件をSolutionへ組み込むGuardrailと実務上の行動へ翻訳する。

## AI Solution DevelopmentをFacilitateする

PDF 7ページから8ページでは、Non-deterministicなOutput、Evaluation Gap、Data Dependency、
Agentic BehaviorおよびIntegration Complexityが、従来のProduct Developmentとは異なる判断を
必要にすると説明している。AI Value ArchitectはProduct ManagementとSystem Architectureが行う
重要Decisionを支援し、Prototypeを作りながらHypothesisを試すExperimentの設計にも関与する。

Data AvailabilityとPermission、PrivacyとRegulation、Human OversightおよびEthical Trade-offを
Discovery段階で明らかにし、必要に応じてData Engineering、LegalまたはComplianceの専門家を
設計対話へ接続する。Productionで得たInsightを今後のARTのApproachへ戻し、複数のAI Solutionを
Lifecycle全体で接続するSystems Viewを維持する。

## Outcomeを継続的に最適化する

PDF 8ページから9ページでは、AI利用そのものではなくBusinessとCustomerのOutcomeを最終目的と
し、Product PerformanceとDelivery Capabilityの両方を測定するとしている。

- Product側ではCost、Revenue、Risk ExposureおよびCustomer Experienceを観測する
- ART側ではFlow Time、ThroughputおよびError Rateを観測する
- Production Usage、Model Performance、Customer FeedbackおよびCostを継続的なSignalとして扱う
- Signalに応じてAI Configurationの調整、Workflow再設計、Value Propositionの改訂またはPivotを選ぶ
- InnovationとExecutionへのCapacity Allocationを比較し、Continue、Pivot、PauseまたはCancelを判断する

記事は、AI SolutionのOutcomeと、ARTがAI Solutionを作るCapabilityの双方で改善が確認できる
ことを、継続投資の根拠としている。

## Role Candidate

PDF 9ページから11ページでは、新規採用だけを前提とせず、Business Acumen、十分なAI Fluency、
Facilitation能力、複雑さを早期に単純化しない姿勢およびMeasurementを最後まで追う規律を持つ
既存人材を候補としている。一人が全責務を持つ必要はなく、ART内の複数人でSkillを補完できる。

候補として次の既存Roleを挙げる。

- Scrum MasterおよびTeam Coach
- SAFe Practice Consultant
- Release Train Engineer
- System Architect
- Product Management

記事は特にScrum MasterとTeam Coachについて、Team Dynamics、Focus保護およびFeedback Loopを
閉じる既存能力に、AI Fluency、Evaluation PracticeおよびValue Measurementを加える自然な
発展先として詳述している。

## 記事中の80% Claimの扱い

PDF 2ページは、業界調査ではAI ProjectのFailure Rateが80%を超えると一般的に述べ、
`POC Graveyard`へ接続する。PDF 6ページは、RAND CorporationのStudyが「AI Solutionの80%が
期待Valueを下回る」と報告したと述べる。ただし、`Project Failure`と`Expected Value未達`は
同一のOutcome定義ではない。

提供PDFのReference欄にはMcKinseyの記事1件のみがあり、RANDのReport名、URL、調査年、Sample、
FailureまたはValue未達の判定基準は記載されていない。PDFからRANDへのLink Annotationも
確認できなかった。

本文の表現に対応し得るRAND公式資料として、2024年の
`The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed`を
確認した。このReportは65名のData ScientistおよびEngineerへのInterviewからFailureの
Root Causeを分析する一方、80%超というRate自体はReportの調査結果ではなく、同Reportが引用する
既存推計として記載している。提供記事がこのReportを意図したかは、PDFだけでは確定できない。

- RAND公式PDF:
  https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2600/RRA2680-1/RAND_RRA2680-1.pdf

したがって、このExternal Inputは`POC Graveyard`というProblem FramingとRole設計のReferenceには
使用できるが、80%を独立に確立された単一のFailure Rateとして扱うには、元調査、母集団および
Failure定義を追加確認する必要がある。

## この資料が支え得る範囲

このExternal Inputは、Scaled AgileがAI-Native Organizationについて次の構造を公式Guidanceとして
提示していることのReferenceになり得る。

- AIへのAccessとPrototypeの成功を、Scale、継続利用およびValue Realizationから分ける
- AI AdoptionをTool導入ではなく日常Workflowの変更、EvaluationおよびFeedback Loopとして扱う
- Business Outcome、Technical Constraint、Data、Operation、RiskおよびGovernanceを接続する
- 共通AI PlatformをTeam固有Workflowへ適応し、Local FeedbackをPlatform Ownerへ戻す
- Prototype、Experiment、Production Signalおよび投資判断を一つのLifecycleで接続する
- Output量ではなくOutcome、Evidenceおよび継続的なValue Measurementを判断基準にする

一方、この資料だけでは、AI Value Architectを独立Roleとして置くことが他のRole Designより
有効であること、特定のPlatform TeamでValue Realizationを改善すること、記事のFailure Rateが
対象Contextにも当てはまること、またはAudienceが登壇内容として価値を感じることを検証できない。

## PEKおよびRepositoryとの接続に関する境界

記事は、AI Tool、Workflow、Outcome、Evidence、Governanceおよび実際の仕事を接続するRoleを
明示している。このため、Platform EngineeringにおけるEnablementまたはValue Realizationの
仮説を検討するReferenceになり得る。

ただし、`AI Value ArchitectはPlatform EnablementのRoleである`、またはこのRepositoryが
`AI-Native WorkflowのControl Planeである`という対応は記事自体のClaimではない。それらは
Repository側で別途、Observation、Hypothesis EpisodeまたはPatternとして解釈と適用可能性を
検討すべき内容である。

## 限界

- 発行元によるFramework GuidanceおよびTrainingへ接続するRole説明であり、Role導入効果を
  比較検証したResearchではない。
- `POC Graveyard`の規模、AI ProjectのFailure Rateおよび期待Value未達の基準を本文中で
  一貫したOperational Definitionとして示していない。
- RANDへの本文中の帰属とReference欄の間にTraceability Gapがある。
- 責務の多くは既存のProduct Management、Architecture、Coaching、Change Management、
  GovernanceまたはPlatform Enablementと重なるが、責任境界やAccountabilityの競合を扱っていない。
- 一人では全責務を担わず複数人で補完できるとする一方、RoleのStaffing Model、Capacity、
  評価基準または導入条件を定量化していない。
- 公式ページは発行元により変更される可能性があり、Login条件も変わり得る。
- PDFはWebpageの印刷Snapshotであり、公式に配布された静的PDFではない。

## PDF本体をRepositoryへ格納しない理由

PDFにはScaled Agile, Inc.の著作権表示があり、画像または本文の複製には明示的な許諾が
必要であると記載されている。再配布許諾を確認できないため、提供されたPDF本体は
Repositoryへ複製せず、Canonical URL、取得経路、書誌情報およびSHA-256を保存する。
