---
id: RN-20260814-004140-rand-ai-failure-patterns-llm-reading
type: raw_note
title: "RANDのAI Project失敗PatternをLLM／Agent文脈で読む"
content_language: ja
created_at: 2026-08-14T00:41:40+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-14T00:47:57+09:00
sanitization_checked_by: agent:codex
tags: [ai-project, failure-pattern, genai, knowledge-context, llm, ml, platform-engineering, technology-first]
relations:
  - type: derived_from
    target: EXT-20260813-225740-rand-ai-project-failure-anti-patterns
---

# RANDのAI Project失敗PatternをLLM／Agent文脈で読む

## この記録の位置づけ

RAND Report `The Root Causes of Failure for Artificial Intelligence Projects and How They Can
Succeed: Avoiding the Anti-Patterns of AI`を読み、ChatGPTとの対話で残したReading Captureと
読後の感想戦を再構成したRaw Noteである。

Reportの書誌情報、調査方法、原文上のFindingおよびLimitは、External Input
`EXT-20260813-225740-rand-ai-project-failure-anti-patterns`を正本とする。このRaw Noteでは、
Reportの内容に対する読者としての反応と、2026年のLLM／Agent Projectへの読み替えを記録する。

以下の5分類をLLM／AgentへMappingする部分はRAND自身のClaimではなく、読後の解釈である。
このNoteだけを、LLM Projectに対する実証結果や一般化済みのFailure Modelとして扱わない。

## 読後の第一印象

最初の感想は「面白かったというより、まさにまさに」であった。Reportが挙げるFailureの多くは、
AI Modelの性能問題ではなく、Problem、Business Context、Success Metric、Data、Infrastructure、
Processおよび組織の判断に関する問題だった。

一方、Reportが扱うAI Projectはかなり明確にMachine Learning中心である。Supervised Learning、
Unsupervised Learning、Reinforcement LearningおよびLLMを含むが、Pretrained LLMをそのまま利用する
Prompt EngineeringだけのProjectは調査対象外である。

そのため、次の記述にはML固有の背景が強い。

- Training DataのQuality、UtilityおよびBalance
- Data Engineerの不足
- Model Training
- Test EnvironmentからProductionへのModel Deployment
- ML EngineerとMLOps Infrastructure

それでも、実装技術の一段上にあるFailureの構造は、現在のGenAI／Agent Projectにもかなり残って
いるように見えた。ML固有の要素と、AI Project一般に残る要素を分けて読む必要がある。

## Reading Capture

### 80%という数字

Reportは、推計によっては80%を超えるAI Projectが失敗すると紹介している。ただし、この数字は
RANDが65名へのInterviewから測定したFailure Rateではない。RANDがFortune記事を参照している
二次的なBackground Claimであり、今回の読後理解では中心に置かない。

RAND自身の調査で重要なのは、AI／MLを実際に作る側のPractitionerへ半構造化Interviewを行い、
彼らが経験したFailureのRoot Causeを抽出していることである。

### Failureの定義

Reportは、AI ProjectのFailureをOrganizationからFailureと認識されたProjectとして定義し、
Technical FailureとBusiness Failureの双方を含めている。

この定義は、Modelが技術的に動いたかだけではProjectのSuccessを決められないことを示す。
Technologyが動いても、期待したBusiness Outcomeへつながらない、日常業務へ統合できない、
またはOrganizationからValueがないと判断されればFailureになり得る。

### Industry側の5分類

Table 3で整理されたIndustry Interviewの主要なFailure Causeは次の5つである。

1. `Leadership-driven failures`
2. `Data-driven failures`
3. `Bottom-up-driven failures`
4. `Underinvestment in infrastructure`
5. `Immature technology`

84%のIndustry Intervieweeが、一つ以上のLeadership-driven Failureを主要なFailure Causeとして
挙げている。これはAI Project全体の84%がLeadershipによって失敗するというPopulation Statistic
ではなく、50名のIntervieweeが主要因として言及した割合である。

特に強く反応したのは、LeadershipがEngineering Teamへ、解くべきProblemと最適化すべきMetricを
伝えられないという説明だった。AIのTechnical Metricが良くても、実際のBusiness Successを表す
Metricとずれていれば、完成したModelを日常業務へ統合する段階でFailureが顕在化する。

### Project PurposeとDomain Context

Recommendationの`Ensure That Technical Staffs Understand Project Purpose and Domain Context`は、
特に納得した点である。

技術側へ渡す必要があるのは「何を作るか」だけではない。

- 何のために取り組むのか
- どのBusiness Contextで使われるのか
- Intended Userは誰か
- 何をSuccessとするのか
- どのMetricを最適化すべきか

LLM／Agentへ仕事を渡す場合にも、単なるInstructionだけでは足りない。人間のTechnical Staffと
同様に、Project Purpose、Domain Knowledge、判断基準および利用Contextが必要になる。

### Problem First

Recommendationの`Focus on the Problem, not the Technology`も、そのまま受け入れられる内容だった。

RANDはTop-downのTechnology-firstだけでなく、Data Scientist自身が新しいModelやFrameworkを
使うことを優先するBottom-up-driven Failureも扱っている。

LLM／Agent文脈でも、次のような形で同じ問題が起こり得る。

- 最新Modelを使うことから始める
- Agentを作ることを目的にする
- 新しいAgent Frameworkを採用することを成果にする
- Intended UserのProblemよりTechnology CapabilityのDemonstrationを優先する

重要なのはAIを使うことではなく、解くべきProblemと期待するOutcomeである。

### AIのCapabilityとLimitations

Recommendationの`Understand Artificial Intelligence's Limitations`も非常に重要である。

AIに何をさせるかを選ぶ側が、次を理解していなければならない。

- AIが何を得意とするか
- 何を苦手とするか
- 現在の技術水準でどこまで実現可能か
- 必要なQuality、Reliability、LatencyおよびCostを満たせるか
- Human Judgmentを残すべきBoundaryはどこか

何でもAIへ渡すのではなく、ProblemまたはTaskがAIに適しているかを判断すること自体が、
AI Project Designの一部である。Technologyを理解する目的はAIを使うことではなく、Problemと
Capabilityの適切なMatchingを判断することにある。

### RigidなAgile Processとの不整合

Industry Interviewee 50名のうち10名が、Rigidに運用されたAgile Software Development Processは
AI Projectへ適合しにくいと述べている。

Data Explorationは、どのDataをどう加工すれば必要な情報になるかを発見するまで所要時間を
見積もりにくい。探索結果が得られた瞬間には必要なContextが頭の中に揃っているため、そこで
実装まで進めた方が効率的な場合もある。Sprintへ合わせて探索を無理に分割すると、Work Itemを
Reopenしたり、意味の薄い単位へ分けたりする可能性がある。

これはAgile Principleの否定ではない。固定ProcedureへAI Projectを合わせるのではなく、
不確実な探索とLearningに合わせてProcessを適応させ、Business Stakeholderへ途中の発見を
頻繁に共有する必要があるという読みである。

### IndustryとAcademiaで異なるFailureの意味

IndustryとAcademiaでFailureの意味が異なる点も面白かった。

Industryでは、Business OutcomeやOrganizationによる評価を基準にSuccessとFailureを比較的
定義しやすい。一方、Academiaでは、不確実な領域を探索すること自体に意味があり、Technicalな
Problemの発見が新しいResearchへつながる場合もある。

それでもPublicationにつながらなければ、ProjectがFailureとして認識される場合がある。Successと
FailureはTechnical Achievementだけで決まらず、活動を取り巻くOrganizationのPurpose、Evaluation
SystemおよびIncentiveによって変わる。

## MLのFailure PatternをLLM／Agentへ読み替える

### 1. Leadership-driven failure

ML文脈では、LeadershipがProblem、Intent、Business ContextおよびMetricを適切に設定・伝達できず、
Priorityも頻繁に変えるFailureである。

LLM／Agent文脈でも、次のFailureとしてほぼそのまま残る。

- 解くProblemが曖昧または誤っている
- OutcomeとOutputを区別していない
- Success Metricが定義されていない
- AIへ渡すIntentとDecision Boundaryが不明確である
- PrototypeのTechnical PerformanceをBusiness Valueと取り違える

### 2. Data-driven failure

最初はTraining DataのQualityというML固有の話として受け止め、あまり反応しなかった。しかし、
LLM／Agentへ置き換えるなら、Training Dataの問題はKnowledge／Context Dataの問題として残る。

RANDは、Dataが大量に存在することと、そのDataが新しいPurposeへ使えることを区別する。また、
分析には単なる`what happened`だけでなく、`why things happened`というContextが必要になる場合が
あると説明する。

GenAIでも、Organization内にDocument、Code、TicketおよびLogが大量に存在することと、次の条件が
満たされることは別である。

- AIが仕事を遂行するために必要なKnowledgeが存在する
- Knowledgeの意味、信頼性、鮮度および重要度を判断できる
- 必要なDomain ContextへAccessできる
- Decisionの理由と適用Boundaryが残っている
- Intended Taskに合う粒度とStructureで提供される

したがって、次のように読み替えられる。

```text
Training Data
  -> Knowledge / Context Data
```

AIがAccessできるKnowledgeが存在することと、AIが仕事を遂行できるDomain Contextが揃っている
ことは同じではない。

### 3. Bottom-up-driven failure

ML文脈では、Data ScientistがBusiness Problemより新しいModelまたはFrameworkの利用を優先する。

LLM／Agent文脈では、最新Model、Agent、ToolまたはFrameworkを使うこと自体の目的化として残る。
Technology Explorationを行う場合も、それがLearning目的であることを明示し、Business Outcomeを
狙うDeliveryと区別する必要がある。

### 4. Underinvestment in infrastructure

RAND本文のInfrastructureは、典型的なAI Platform／MLOps Infrastructureの話である。

- Data Pipeline
- Data Monitoring
- Model Deployment
- Production Environment
- Model Maintenance
- Data EngineeringおよびML Engineering

つまり、Modelを作るだけで終わらせず、Productionで継続運用するための基盤を指す。

LLM／Agent時代にも、これらのOperational Capabilityは消えない。その上で、次のResourceと
ConstraintもInfrastructureの一部として重要になるように見える。

- 利用可能なModelとModel Access
- Token BudgetとContext Window
- RuntimeとOrchestration
- Rate Limit、LatencyおよびCost
- EvaluationとObservability
- Retry、FallbackおよびHuman Escalation
- Knowledgeを収集、整形、供給し、鮮度と変更を観測する仕組み

ただし、`Infrastructure = ModelとToken`だけに縮約するのは適切ではない。RANDの原文が扱う
Production OperationとMLOpsを土台として残し、GenAI固有のResourceおよびConstraintが追加される
という理解が妥当である。

### 5. Immature technology

ML文脈では、現在のState of the Artを超えるBusiness ProblemへAIを適用するFailureである。

LLM／Agent文脈では、現在のModelがTaskに必要なQualityやReliabilityを満たせない、またはHumanの
Subjective Judgmentを安定して代替できないにもかかわらず、自動化を前提にするFailureとして残る。

これは単なるModel Performanceの問題ではない。必要なQuality Threshold、許容Risk、Human Review、
FallbackおよびStopping Ruleを含むSolution Designの問題でもある。

## 5分類の読み替え

| RANDのIndustry分類 | LLM／Agent文脈での仮の読み替え |
| --- | --- |
| Leadership-driven failures | Problem、Outcome、Success Metric、IntentおよびBusiness Contextの設定・伝達の失敗 |
| Data-driven failures | Knowledge／Context Dataの不足、品質、鮮度、意味および用途不適合 |
| Bottom-up-driven failures | 最新Model、AgentまたはFrameworkを使うことの目的化 |
| Underinvestment in infrastructure | AI Platform／MLOpsに加え、Model Access、Token、Runtime、OrchestrationおよびObservabilityの不足 |
| Immature technology | 現在のAI CapabilityとProblem／Task、Quality ThresholdおよびRiskの不一致 |

## 全体所感

「ML時代のAI Project失敗論」で終わるかと思ったが、実際には現在のGenAI／Agentにもかなり
接続できる内容だった。

実装技術はMLからGenAIへ大きく変化した。それでも、次の基本構造は驚くほど変わっていない
ように見える。

- 何のProblemを解くのか
- 期待するOutcomeは何か
- SuccessをどのMetricで確認するのか
- 必要なKnowledgeとDomain Contextはあるか
- AIをProductionで継続利用するInfrastructureはあるか
- AIのCapabilityとLimitationsを理解しているか
- Technologyと実際のWorkflowを接続できるか

このReportから直接言えるのは、ML Projectを経験したPractitionerがこれらのFailure Causeを
繰り返し報告したことまでである。LLM／Agentにも同じ構造が存在するという見立ては、原文から
自然に伸ばせるものの、別途確認すべきHypothesisである。

読後の中心的な見立ては次のとおりである。

> AI Projectの失敗は、Modelの性能問題だけではない。Problem、Context、Metric、Workflow、
> InfrastructureおよびCapability Boundaryを接続できないSystem-level Failureとして現れる。

## この記録だけでは分からないこと

- RANDの5分類がPrompt中心のLLM／Agent Projectでも同じ頻度とImpactを持つか
- Training DataからKnowledge／Context Dataへの読み替えが、どのUse Caseまで適用できるか
- Model Access、Token Budget、RuntimeおよびOrchestrationをInfrastructureとして扱う分類が十分か
- AI PlatformまたはPlatform Engineeringが各Failureをどの程度予防または軽減できるか
- AI Value ArchitectのようなRoleを置くことが、Roleを置かない場合よりValue Realizationを改善するか
- PEKのAudienceがこの5分類と読み替えに価値を感じるか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
