---
id: OBS-20260802-230426-failure-rate-definition-mismatch
type: observation
title: "プロジェクトと変革の失敗率は対象と成功定義が異なり統合できない"
content_language: ja
created_at: 2026-08-02T23:04:26+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-02T23:18:14+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: high
knowledge_basis:
  - external_research
relations:
  - type: derived_from
    target: RN-20260802-195858-open-organization-change-project-evidence-review
  - type: derived_from
    target: RN-20260730-224354-seventy-percent-failure-source-check
  - type: references
    target: RN-20260802-201449-project-change-failure-rate-not-used
---

# 観察

## 根拠箇所

- `RN-20260802-195858-open-organization-change-project-evidence-review` の各資料の
  「調査対象」「確認できたデータ」「制約」「調査結果の横断比較」
- `RN-20260730-224354-seventy-percent-failure-source-check` の「確認した候補」
  「今回の判断」「この探索から残った注意点」
- `RN-20260802-201449-project-change-failure-rate-not-used` の登壇上の不採用判断は、
  EvidenceではなくContextとして参照する

## 根拠から直接言えること

根拠ノードには、近い失敗率または成功率を示す資料であっても、少なくとも次が
異なると記録されている。

- 対象:
  Project、IT Change、組織変革、Transformation、大規模改善施策
- 成功または失敗の基準:
  期限、予算、Scope、品質、Feature、Project Objective、Business Case上の期待価値、
  中止、完全な不使用
- Evidenceの性質:
  自己申告、実務家Survey、少数施策の分析、複合指標、外部資料の要約

PwC、McKinsey、IBM、Standish、SAFeの数字は、同じ母集団または同じOutcomeを
測定していないと記録されている。特に、Delivery Constraintを満たした割合、
Business Case上の期待値を達成した割合、Transformationが失敗した割合を、単一の
「Business Outcome未達率」として扱うことはできない。

また、期待値未達、マイナスROI、Project Failure、誰にも利用されなかった状態は
同義ではないと記録されている。

## 曖昧さと限界

- このObservationが直接示すのは、Reviewed Raw Noteに保存されたSource Reviewの
  結果であり、各外部資料をこのObservation作成時に独立再調査した結果ではない。
- 調査資料の多くは2000年代から2011年までのもので、現在のProduct Developmentへ
  一般化できない。
- Sourceごとの母集団、設問、統計処理、定義には公開情報だけで監査できない部分が
  ある。
- 複数資料で似た論点が現れることは、因果的な成功法則のEvidenceではない。
- 「登壇で数字を使わない」という判断は別Raw NoteのDelivery判断であり、この
  Observation自体による採用決定ではない。

## 公開安全性確認

- checked_at: 2026-08-02T23:18:14+09:00
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
