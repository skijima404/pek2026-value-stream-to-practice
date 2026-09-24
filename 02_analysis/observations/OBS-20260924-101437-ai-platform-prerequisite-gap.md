---
id: OBS-20260924-101437-ai-platform-prerequisite-gap
type: observation
title: "AI開発基盤の理解でAutomation・Platformとの接続が共有されていない経験が記録された"
content_language: ja
created_at: 2026-09-24T10:14:37+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-09-24T10:48:49+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - case_recollection
relations:
  - type: derived_from
    target: RN-20260805-211321-ai-platform-prerequisite-knowledge-gap
  - type: references
    target: OBS-20260827-010636-delegation-quality-assurance-scope
  - type: references
    target: HYP-20260812-010725-progressive-automation-contracts
---

# 観察

## 知識の成立根拠

`RN-20260805-211321-ai-platform-prerequisite-knowledge-gap`に保存された、複数の実務上の
会話についての実践者の説明に基づく。保存された説明を`recorded_statement`、反復する
実務上の判断を`practitioner_experience`、一次記録を確認できない会話の回想を
`case_recollection`として区別する。

## 根拠箇所

- 同Raw Noteの「驚いたこと」
- 同Raw Noteの「自分が暗黙に置いていたAI開発基盤のImage」
- 同Raw Noteの「生じた見立て」
- 同Raw Noteの「Enablementへの示唆候補」

## 根拠から直接言えること

実践者は、複数の会話で、手動で仕事を確認し、安定した部分を個別に自動化してから接続する
というAutomationの進め方が共有されず、実際の作業にも適用されていなかったと記録している。
同じ会話では、AI開発基盤が何を組み合わせたものかというImageも共有されていなかった。

実践者が暗黙に置いていたImageは、Git、CI/CD、GitOps、Identity、Observability、Workflow、
Test、ReviewおよびDeploymentなどのSoftware Delivery Platformへ、LLM、Prompt・Context、
Retrieval、Evaluator、Human in the LoopおよびAI Output Traceabilityを追加する構造である。

Sourceでは、Automation Engineering、Software Delivery・Platform Engineering、AI Platformの
接続が示されていないことが、AI Platform理解を難しくする原因候補として整理されている。
ただし、会話相手が知らなかったのか、知っていて適用しなかったのかは確認されていない。

## 既存Analysisとの関係

`OBS-20260827-010636-delegation-quality-assurance-scope`は、Automation成熟をDelegation範囲と
品質保証範囲の拡張として整理する。本Observationは、その構造が実務上の会話相手へ共有されて
いなかったという経験と、実践者が置いていた前提Imageを保存する。

`HYP-20260812-010725-progressive-automation-contracts`は段階的接続の効果を扱うが、本Observationは
相手の知識、説明方法または理解Outcomeを比較していないため、同Hypothesisの検証結果にはしない。

## 曖昧さと限界

- 会話記録、参加者のRole、事前知識、実際の設計成果物または理解度を確認していない。
- 対象者が概念を知らなかったことと、知っていて適用しなかったことを区別できない。
- AI Platform理解の原因をAutomationまたはPlatform知識の不足へ特定できない。
- 実践者の基盤Imageが唯一または標準的な構成であるとは確認していない。
- 接続を説明するEnablementが理解、設計品質またはOutcomeを改善する因果は未検証である。

## 公開安全性確認

- checked_at: 2026-09-24T10:48:49+09:00
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
