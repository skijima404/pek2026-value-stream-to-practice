---
id: EXT-20260813-225740-rand-ai-project-failure-anti-patterns
type: external_input
title: "RAND「The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed」"
content_language: ja
created_at: 2026-08-13T22:57:40+09:00
created_by: agent:codex
source_type: official_research_report
source_url: https://www.rand.org/pubs/research_reports/RRA2680-1.html
source_pdf_url: https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2600/RRA2680-1/RAND_RRA2680-1.pdf
retrieved_at: 2026-08-13T22:57:40+09:00
retrieval_method: official_publication_page_and_pdf_inspection
provided_by: agent:codex
changeability: externally_managed
publication_date: 2024-08-13
license: all_rights_reserved
asset_in_repository: false
asset_omission_reason: redistribution_not_authorized
relations:
  - type: references
    target: EXT-20260813-224814-safe-ai-value-architect
---

# RAND「The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed」

## 位置づけ

RAND Corporationが2024年に公開した、AI ProjectのFailureに関するExploratory Research
Reportである。IndustryとAcademiaのAI Practitionerへの半構造化Interviewから、繰り返し
報告されたFailureのAnti-patternと、IndustryおよびAcademia向けのRecommendationを整理する。

本ノードはReportの書誌情報、調査方法、Source StatementおよびLimitを後から参照できるように
保存するExternal Inputである。ここに記録した内容は、このRepositoryのHypothesisが検証済み、
Population全体のFailure Rateが確立済み、または登壇内容へ採用済みであることを意味しない。

## 書誌情報

- Title: `The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed`
- Subtitle: `Avoiding the Anti-Patterns of AI`
- Authors: James Ryseff、Brandon F. De Bruhl、Sydne J. Newberry
- Publisher: RAND Corporation
- Report Number: `RR-A2680-1`
- Publication Date: 2024年8月13日
- Research Completion: 2024年4月
- Official Publication Page:
  https://www.rand.org/pubs/research_reports/RRA2680-1.html
- Official PDF:
  https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2600/RRA2680-1/RAND_RRA2680-1.pdf
- PDF: 20ページ

ReportはRAND National Security Research DivisionのAcquisition and Technology Policy Programで
実施された。RAND National Defense Research InstituteのExploratory Research Fundingを使用し、
SponsorおよびDefense Office of Prepublication and Security ReviewによるSecurity Reviewを経て
公開されたと記載されている。

## 調査目的と方法

Reportは、AI ProjectのFailure Rateを測定するPrevalence Studyではなく、経験者が認識した
FailureのRoot Causeを探索するInterview Studyである。

- Interview期間: 2023年8月から12月
- 全参加者数: 65名
- Industry: 50名、50を超えるOrganizationを代表
- Academia: 15名
- 方法: Open-ended Questionを用いた半構造化Interview
- Failureの定義: OrganizationからFailureと認識されたAI Project
- Failureの範囲: Technical FailureとBusiness Failureの双方
- 分析対象: 参加者がFrequentまたはImpactfulと認識したFailureと、そのRoot Cause

Industry Participantは、AIまたはMLのIndustry Experienceが5年以上あり、Data Scienceまたは
ML EngineeringのIndividual ContributorまたはManagerである人をLinkedIn RecruiterとInMailで
募集した。379名へ連絡し、50名が参加、14名が辞退した。参加者はStart-up、Medium-sized Company、
Large Company、およびTechnology、Health Care、Finance、Retail、Consultingなど複数Industryから
選ばれ、45分のInterviewに100米ドルのHonorariumが提供された。

Academia Participantは、ConferenceおよびResearch Teamの既知のNetworkから得たConvenience
Sampleである。Engineering ProgramとBusiness School、Tenure-track、Non-tenure-track、Graduate、
UndergraduateおよびResearch Assistantなどを含む。IndustryとAcademiaの双方で匿名性を約束し、
Interview GuideはAppendix AおよびAppendix Bに掲載されている。

## 調査対象となるAIの範囲

ReportはMachine Learningを中心とし、Supervised Learning、Unsupervised Learning、
Reinforcement LearningおよびLarge Language Modelを含む。ただし、Pretrained LLMを使用するだけで、
ModelのTrainingまたはCustomizationを行わないProject、本文でPrompt Engineeringと呼ばれる利用は
調査対象外である。

したがって、このReportのFindingは、現在のGeneral-purpose Copilot、Prompt中心のLLM利用、
または既成AgentをWorkflowへ導入するCaseへ直接一般化できない。一方、Domain Context、Data、
Metric、InfrastructureおよびProduction Integrationに関するFindingは、比較対象または
Applicabilityを検討するReferenceになり得る。

## Industry Interviewで抽出された5つのRoot Cause

ReportはIndustry Interviewから、次の5つを主要なRoot Causeとして整理する。

1. `Leadership-driven failures`
   Business Stakeholderが解くべきProblem、Intentまたは最適化すべきMetricを誤解、または
   Engineering Teamへ適切に伝達できない。Priorityを短期間で変え、十分な結果が出る前に
   Projectを中断する場合も含む。
2. `Data-driven failures`
   EffectiveなModelをTrainingするためのDataの量、品質、Balance、意味またはDomain Contextが
   足りない。Data Engineeringの不足とKnowledge Lossも含む。
3. `Bottom-up-driven failures`
   Intended UserのProblemより、Engineerが新しいModel、FrameworkまたはTechnologyを試すことを
   優先する。
4. `Failures due to underinvestment in infrastructure`
   Data Governance、Data Pipeline、Monitoring、Model MaintenanceおよびProduction Deploymentを
   支えるInfrastructureへ投資しない。
5. `Failures due to immature technology`
   現在のAI Capabilityに適していないProblem、特にSubjectiveなHuman Judgmentを要するProcessを
   自動化しようとする。

Reportは、OrganizationとEngineering Teamの間でProject Purpose、Business ContextおよびMetricが
一致しないことを最も大きなProblemとして扱う。完成したModelを日常のBusiness Operationへ
統合する段階で、Model Metricと実際のBusiness Success Metricの不一致が初めて明らかになる
Caseを説明している。

## Interview内で報告された主な数値

次の数値は、Project母集団に対する発生率ではなく、50名のIndustry Intervieweeのうち、各要因を
主要なFailure CauseまたはDifficultyとして挙げた人の割合または人数である。

- 84%が、一つ以上のLeadership-driven Root CauseをAI Project Failureの主要因として挙げた
- 30名が、Data Qualityに関する継続的な問題を述べた
- 16名が、Data Scientist側から生じるBottom-up-driven Failure Patternを述べた
- 14名が、Leadershipによる必要時間の過小評価を述べた
- 10名が、Domain Understandingの不足がFailureにつながると述べた
- 10名が、Rigidに解釈されたAgile Software Development ProcessはAI Projectに適合しにくいと述べた

Report自身も、Intervieweeの多数がNon-managerial Engineerであるため、Leadership Failureを
過大に抽出している可能性をLimitとして明示する。上記の数値をOrganization全体のFailure発生率、
因果効果または一般Populationの分布として扱うことはできない。

## Data、ContextおよびInfrastructureに関する記述

Reportは、保存済みDataが大量に存在することと、新しいAI Use Caseに適したTraining Dataが
存在することを区別する。ComplianceやLoggingのために保存されたDataは、何が起きたかを示しても、
なぜ起きたか、どのOptionが提示されていたか、どのContextでDecisionされたかを持たない場合がある。

Data ScientistはDomain Expertではないため、Fieldの意味、ReliabilityおよびImportanceを理解する
支援が必要である。Domain ExpertがAIによるJob Replacementを懸念し、協力に消極的になる可能性も
Interviewで報告されている。

Infrastructureについては、Prototypeを連続して作るだけでは、Deployment後のData Format Change、
Data Arrival FailureおよびModel Maintenance Needを観測できないとする。Data EngineerとML Engineer、
自動化されたData Pipeline、MonitoringおよびProduction Deployment Capabilityへの投資が、
Modelを実際のEnd Userへ届ける前提として説明されている。

## Agile Software Developmentに関する記述

Industry Interviewee 50名のうち10名は、Rigidに運用されたAgile ProcessがAI Projectへ適合しにくい
と述べた。Data ExplorationとExperimentは所要時間を事前に予測しにくく、一週間または二週間の
Sprintへ合わせるため、Work Itemを繰り返しReopenするか、意味の薄い単位へ分割するCaseが報告された。

ReportはAgileのPrinciple自体を否定せず、UniformなProcedureを強制するのではなく、TeamがWorkloadへ
Processを適応させ、Business StakeholderとProject StatusおよびInterim Discoveryを頻繁に共有する
ことを推奨する。このFindingは10名のIntervieweeが述べた経験であり、Agileと他のProcessを比較した
Outcome Studyではない。

## Industry向けRecommendation

ReportはIndustry Leader向けに次の5点を推奨する。

1. Technical StaffがProject PurposeとDomain Contextを理解できるようにする
2. 少なくとも一年間取り組む価値がある、持続的なProblemを選ぶ
3. Technologyではなく、解くべきProblemへFocusする
4. Data Governance、Data Pipeline、MonitoringおよびDeployment Infrastructureへ投資する
5. AIのTechnical Limitationを理解し、Technical ExpertとともにFeasibilityを評価する

一年という期間は、Interviewから導かれたReportのRecommendationであり、すべてのAI Projectに
必要なMinimum Durationを比較試験で確立したものではない。

## Academia Interviewで抽出されたRoot Cause

Academiaでは、Industryと異なるSuccessおよびFailureの認識が報告された。Reportは次の3点を
主要なRoot Causeとして整理する。

- `Activity prestige`: ImpactよりPeerからPrestigiousと認識されるTopicが優先される
- `Improper data structures`: AI利用を前提に収集されていないData、量または品質の不足
- `Publication incentives`: 新しいProblemの発見や将来のResearch Agendaにつながっても、
  Publication、Conference ProceedingまたはCommunication ItemにならなければFailureと認識される

Reportは、Academic AI ProjectのFailureについてConsensusが得られず、Technical Barrierより
IncentiveのMisalignmentが支配的だったとまとめている。この結果は15名のConvenience Sampleに
基づく。

## 「80%を超えるAI Projectが失敗する」という記述の出典階層

ReportはBackgroundで、`By some estimates, more than 80 percent of AI projects fail`と述べる。
ただし、この80%は65名へのInterviewから計算したFailure Rateではない。

ReportのFootnote 13は、Jeremy Kahnによる2022年7月26日のFortune記事
`Want Your Company's A.I. Project to Succeed? Don't Hand It to the Data Scientists, Says This CEO`
を参照している。したがって、出典階層は次のようになる。

```text
Scaled Agileの記事
  -> RAND Reportの記述
    -> Fortune記事
      -> Fortune記事内で用いられた推計または発言
```

このReportが独立に提供する数値は、Interviewee数、Candidate Response、各Root Causeを述べた
Intervieweeの割合または人数である。80%をRANDが測定したFailure Rateとして引用することはできない。

## この資料が支え得る範囲

このExternal Inputは、次の限定されたClaimのReferenceになり得る。

- ExperiencedなAI PractitionerへのInterviewで、AI Project FailureのRoot Causeとして、
  ProblemとMetricのMisalignment、DataとDomain Contextの不足、Technology-firstの選択、
  Infrastructure不足およびTechnical Capabilityとの不一致が繰り返し報告された
- ModelのTechnical Performanceだけでなく、Business Workflowへの適合とProduction Operationが
  Failure認識に関係していた
- AI ProjectはTechnology PlatformとProjectを置くOrganization Structureの双方を含むという
  Systems-orientedなProblem FramingがResearch Reportに存在する
- PrototypeからProductionへ進むには、Data Engineering、ML Engineering、Monitoringおよび
  Deployment Infrastructureへの投資が必要だというPractitioner-based Recommendationが存在する
- AI Projectでは、予測困難なData ExplorationとExperimentに合わせてProcessを適応させる必要が
  あるというInterview Findingが存在する

一方、この資料だけでは、AI Projectの80%以上が失敗すること、5つのRoot CauseがPopulation全体で
同じ比率で発生すること、各RecommendationがFailureを減らす因果効果、Prompt中心のGenAI導入への
直接適用、またはPlatform Engineeringが唯一の解決手段であることを検証できない。

## 限界

- Exploratoryな半構造化Interview Studyであり、Project Outcomeの追跡、Control Groupまたは
  Failure Rateの推定を目的としていない。
- FailureはOrganizationがFailureと認識した状態であり、共通の定量Thresholdではない。
- Industry Candidate 379名中50名が参加しており、NonresponseおよびSelf-selection Biasがあり得る。
- Industry参加者はEngineering側が中心であり、Leadership Failureを過大に抽出した可能性がある。
- Academiaの15名はConvenience Sampleであり、一般化可能性が限られる。
- Report Summaryは参加者をAI/ML Model構築経験5年以上と説明するが、MethodsではAcademia Sampleに
  Graduate、UndergraduateおよびResearch Assistantも含むため、経験年数の適用範囲を本文だけでは
  完全に再構成できない。
- Prompt Engineeringだけを行うPretrained LLM ProjectはScope外である。
- DoDを含むLeader向けに構成されているが、Industry Sampleは複数Sectorを含む。特定のOrganization、
  Platform TeamまたはPEK AudienceへのApplicabilityは別途確認が必要である。
- Official Sourceは発行元により更新または移動される可能性がある。

## PDF本体をRepositoryへ格納しない理由

RANDはDirect Linkを推奨する一方、PublicationのUnauthorized Postingを禁止し、別形式でのReuseには
Permissionが必要と記載している。再配布許諾を確認できないため、PDF本体はRepositoryへ複製せず、
Official Publication Page、Official PDF URL、書誌情報、調査方法および確認したSource Statementを
保存する。

Official Serverがこの作業環境からの直接Downloadを拒否したため、Local FileのSHA-256は記録して
いない。本文はRAND公式Publication Pageと公式PDFの全20ページを確認した。
