---
id: OBS-20260815-000410-ai-project-system-failure-structure
type: observation
title: "AI Projectの失敗はModel単体ではなく目的・Context・Data・基盤を接続できない構造として報告された"
content_language: ja
created_at: 2026-08-15T00:04:10+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-15T00:20:04+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - external_research
  - reasoned_synthesis
relations:
  - type: derived_from
    target: EXT-20260813-225740-rand-ai-project-failure-anti-patterns
  - type: derived_from
    target: RN-20260814-004140-rand-ai-failure-patterns-llm-reading
  - type: references
    target: OBS-20260811-221400-ai-readiness-as-system-adaptation
---

# 観察

## 知識の成立根拠

RANDのExploratory Research Reportは、AIまたはMLを作るIndustry Practitioner 50名と
Academiaの参加者15名への半構造化Interviewを行い、OrganizationがFailureと認識した
ProjectについてRoot Causeを整理している。

`EXT-20260813-225740-rand-ai-project-failure-anti-patterns`は調査方法、対象範囲、5分類、
RecommendationおよびLimitを保存している。`RN-20260814-004140-rand-ai-failure-patterns-llm-reading`
は、そのFindingをLLM／Agent文脈へ読み替えた読書記録である。ReportのFindingを
`external_research`、読書記録を`recorded_statement`、複数要素をSystem-levelの接続問題として
まとめる部分を`reasoned_synthesis`として扱う。

## 根拠箇所

- `EXT-20260813-225740-rand-ai-project-failure-anti-patterns`の「調査目的と方法」、
  「調査対象となるAIの範囲」、「Industry Interviewで抽出された5つのRoot Cause」、
  「この資料が支え得る範囲」および「限界」
- `RN-20260814-004140-rand-ai-failure-patterns-llm-reading`の「Industry側の5分類」、
  「MLのFailure PatternをLLM／Agentへ読み替える」、「全体所感」および
  「この記録だけでは分からないこと」

## 根拠から直接言えること

RANDのIndustry Interviewでは、AI Projectの主要なFailure Causeとして次の5分類が
繰り返し報告された。

1. LeadershipがProblem、Intent、Business ContextまたはMetricを設定・伝達できない
2. Modelに必要なDataの量、品質、Balance、意味またはDomain Contextが不足する
3. Intended UserのProblemよりModel、FrameworkまたはTechnologyの利用を優先する
4. Data Governance、Pipeline、Monitoring、MaintenanceおよびDeployment基盤へ投資しない
5. 現在のAI Capabilityに適さないProblemまたはHuman Judgmentを自動化しようとする

ReportはModelのTechnical Performanceだけでなく、Business Workflowへの統合とProductionでの
継続運用をFailure認識に含めている。したがって、調査対象となったAI／ML Projectでは、
Model単体の性能ではなく、Project Purpose、Domain Context、Success Metric、Data、Workflow、
InfrastructureおよびTechnical Capabilityの接続に関するFailureが報告されたと言える。

読書記録では、Data-driven FailureをKnowledge／Context Data、Bottom-up-driven Failureを
Model・Agent・Frameworkの目的化、Infrastructure不足をEvaluation、Observability、Fallback、
Human EscalationおよびKnowledge Curationを含む運用能力へ読み替えている。この対応は
Report自身のFindingではなく、LLM／Agent Projectへ適用するための解釈である。

## 既存Analysisとの関係

`OBS-20260811-221400-ai-readiness-as-system-adaptation`は、AI ReadinessをOutcome、Value Flow、
Verification、Platform、Data／Knowledge CurationおよびSensingへ分けるRepository側の整理である。
本Observationは、その軸の有効性を検証するものではないが、AI／ML Practitionerが類似する
System-levelのFailure Causeを報告した外部Researchとして比較可能なContextを提供する。

## 曖昧さと限界

- ReportはFailure Rateを推定する調査ではなく、Control GroupまたはProject Outcomeの追跡もない。
- 84%は50名のIndustry IntervieweeがLeadership-driven Causeへ言及した割合であり、AI Project
  母集団のFailure Rateまたは因果効果ではない。
- Prompt EngineeringだけでPretrained LLMを利用するProjectは調査対象外である。
- Industry参加者はEngineering側が中心で、Leadership Failureを過大に抽出した可能性がある。
- LLM／Agentへの読み替え、6軸のAI Readinessとの対応、およびPlatform Engineeringによる
  予防効果は未検証である。
- このObservationは、RANDのRecommendation、RepositoryのReadiness Modelまたは登壇上の主張の
  採用を意味しない。

## 公開安全性確認

- checked_at: 2026-08-15T00:20:04+09:00
- checked_by: agent:codex
- result: `not_needed`
- scope:
  この分析ノードの本文、frontmatter、relationの組み合わせを、
  人間の意図Reviewを確定する時点で再確認した
- finding:
  顧客、案件、非公開の個人、商用条件、内部System、認証情報、再識別に
  つながる組み合わせは確認されず、本文の変更や削除は行っていない
- limitation:
  公開安全性の確認は、内容の正しさ、検証完了、採用を意味しない
