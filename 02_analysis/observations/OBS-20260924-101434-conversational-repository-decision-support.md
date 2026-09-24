---
id: OBS-20260924-101434-conversational-repository-decision-support
type: observation
title: "Contract-firstな対話型Repositoryを複数の意思決定支援で運用した経験が記録された"
content_language: ja
created_at: 2026-09-24T10:14:34+09:00
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
    target: RN-20260804-204359-conversational-repository-decision-support
  - type: references
    target: OBS-20260827-010635-ai-outcome-review-boundary
  - type: references
    target: HYP-20260801-004823-service-contract-reduces-downstream-cost
  - type: references
    target: HYP-20260809-013742-value-traceability-enables-dvs-learning
---

# 観察

## 知識の成立根拠

`RN-20260804-204359-conversational-repository-decision-support`には、一人の実践者が
Enterprise Architectureの複数の実務で類似Repositoryを作成・運用しているという説明と、
そのうち一件で計画変更へ対応した回想が保存されている。

反復する実務上の方法を`practitioner_experience`、保存された説明を`recorded_statement`、
一次記録を確認できない個別Episodeを`case_recollection`として区別する。

## 根拠箇所

- 同Raw Noteの「取り組み」
- 同Raw Noteの「計画変更時の事例」
- 同Raw Noteの「Contract First」
- 同Raw Noteの「位置づけ上の注意」

## 根拠から直接言えること

実践者は、複数の支援先で、目的、制約、技術検討、判断材料および未確定事項を蓄積し、
人間とAIの対話で更新する類似Repositoryを運用していると説明している。AI Outputをそのまま
完成品として他者へ渡すことを基本とせず、判断する人間が対話へ参加し、違和感、前提のずれ
または不足を意思決定前に修正する運用が記録されている。

一件の回想では、大きなSchedule変更時に蓄積Contextを用い、半日でSchedule上と技術上の
制約からFeasibilityを確認し、三案を検討して進め方を提案した。実践者本人はRepositoryが
なければ同じ時間で行うことは困難だったと評価しているが、比較実験または工数記録はない。

この運用では、目的、制約、前提、比較軸、Accountabilityおよび確認方法を先に置き、
そのContract内で探索、比較、反証、Feasibility確認および提案作成を行うと記録されている。

## 既存Analysisとの関係

`OBS-20260827-010635-ai-outcome-review-boundary`は、Traceabilityを担うIntentへ異なるOutcomeを
混ぜず、Cognitive StepとReview範囲を分けた一件を扱う。本Observationは、それより広い
意思決定支援Repositoryの反復Practiceと一件の利用回想を保存する。

Service ContractまたはValue Traceabilityが意思決定品質、速度またはOutcomeを改善する因果は、
本記録から検証できないため、関連Hypothesisの結果を変更しない。

## 曖昧さと限界

- Repository、変更履歴、判断資料、時間記録または後続Outcomeを確認していない。
- 複数の実務で利用したことは成功率または一貫した効果を示さない。
- 半日という所要時間に比較対象がなく、Repositoryの因果効果を定量化できない。
- 人間ReviewのCost、誤りの見落とし、案の予測精度および長期効果は未確認である。
- Enterprise Architecture以外へ同じ運用が適用可能とは結論できない。

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
