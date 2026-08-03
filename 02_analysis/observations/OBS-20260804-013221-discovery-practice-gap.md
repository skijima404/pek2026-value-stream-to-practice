---
id: OBS-20260804-013221-discovery-practice-gap
type: observation
title: "Customerへの確認ではDiscovery結果が未定義または担当者に理解されていなかった"
content_language: ja
created_at: 2026-08-04T01:32:21+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-04T01:41:32+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - practitioner_experience
relations:
  - type: derived_from
    target: RN-20260730-101222-discovery-gap-and-talk-continuity
  - type: derived_from
    target: RN-20260804-013822-discovery-result-customer-inquiry
---

# 観察

## 知識の成立根拠

作成者が、PresalesとProject Deliveryを通じてCustomerへ目的とDiscovery結果を
質問してきた蓄積経験を、母集団調査ではなく実務上の判断として明示した記録に
基づく。

## 根拠箇所

- `RN-20260730-101222-discovery-gap-and-talk-continuity`の
  「Discover / Decide / Deliveryに関する感覚値」
- 同Raw Noteの「参加者へ伝える知見候補」
- `RN-20260804-013822-discovery-result-customer-inquiry`に記録された、Customerへ
  毎回目的とDiscovery結果を質問していたという追加説明

## 根拠から直接言えること

作成者はCustomerと接する際、毎回「なぜこれを行うのか」と、Mobiusでいう
Discoveryの結果に相当する内容を質問していた。その回答を確認した上で、
Discoveryの結果が定義されていないか、対応した担当者がその結果を理解していない
状態のいずれかだと判断してきた。

したがって、この経験は、作成者がDiscoveryらしい活動を受動的に見かけなかった
ことだけに基づくものではない。目的とDiscovery結果をCustomerへ明示的に確認した
時点で、それを提示または説明できる状態ではなかったという実務経験である。

一方、Solutionを選ぶDecisionとDeliveryに関する議論には接してきた。ただし、
そのDecisionがDiscoveryで形成したProblemやValueを受けたものか、複数の
Solution Hypothesisを比較したものか、検証方法まで定めたものかは、必ずしも
明確ではなかったという経験が記録されている。

Raw Noteには「3年に一度程度」という感覚値もあるが、これは母数、観測期間、
判定基準を伴う集計値ではない。Discoveryの実施率ではなく、作成者が経験した
希少さの表現としてのみ扱う。

## 曖昧さと限界

- PresalesとProject Deliveryで質問した対象の選定、件数、期間、質問と回答の
  一次記録は保存されていない。
- 組織としてDiscovery結果が存在しなかった状態と、回答した担当者が結果を理解、
  参照または説明できなかった状態は区別できない。
- 回答した担当者以外が結果を保持していた可能性や、別の文書または名称で結果が
  存在した可能性は残る。
- 「Discovery結果が定義されている」と判断する統一的な判定基準は保存されていない。
- Platform Engineering、特定地域、特定業界またはProject全体の一般的な頻度へ
  外挿できない。
- `practitioner_experience`はこのObservationの実務上の成立根拠だが、独立した
  調査または検証結果ではない。

## 公開安全性確認

- checked_at: 2026-08-04T01:41:32+09:00
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
