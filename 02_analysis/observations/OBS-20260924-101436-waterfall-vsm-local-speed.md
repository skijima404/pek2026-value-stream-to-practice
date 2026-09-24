---
id: OBS-20260924-101436-waterfall-vsm-local-speed
type: observation
title: "Waterfall組織のVSMで開発工程の高速化と全体効果を分けて問うた一事例が記録された"
content_language: ja
created_at: 2026-09-24T10:14:36+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-09-24T10:48:49+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - case_recollection
relations:
  - type: derived_from
    target: RN-20260914-204312-waterfall-vsm-lead-time-and-cost
  - type: references
    target: OBS-20260818-214727-lead-time-waiting-time-priority
  - type: references
    target: HYP-20260809-203135-quality-first-ai-allocation-workflow
---

# 観察

## 知識の成立根拠

`RN-20260914-204312-waterfall-vsm-lead-time-and-cost`に保存された、一人の実践者が
Waterfallを主に用いる組織でVSMを作成した一件の回想に基づく。説明を
`recorded_statement`、元の計測資料を確認できないEpisodeを`case_recollection`として扱う。

Sourceのfrontmatterは`review_status: reviewed`だが、本文末には整理済みノートの人間による
意図確認が未実施と記載されている。このProvenance上の不整合を解消せず、Confidenceを
`low`として保持する。

## 根拠箇所

- 同Raw Noteの「VSMを作成した際の経験」
- 同Raw Noteの「提示されたスライドとの関係」
- 同Raw Noteの「今回の登壇での使い方の候補」
- 同Raw Noteの「公開範囲と未確認事項」

## 根拠から直接言えること

実践者は、Waterfall中心のある組織でVSMを作成した際、要件定義とテストがProjectの
大きな部分を占め、開発工程は相対的に小さかったと振り返っている。その組織が開発の
高速化を検討していたため、開発を速くしても全体に対する効果は小さいのではないかと
問いかけたと記録されている。

実践者が普段説明に使用するスライドの工程棒は、当時の数値を見ながら相対的な長さを
調整したものだと説明されている。一方、元の数値、分母、工程重複、期間と工数の区別、
作図方法または施策後の結果は、このRepositoryで確認していない。

このSourceでは、局所工程の高速化がValue Stream全体のLead Timeへ与える効果と、工数または
コスト削減を分けて考える必要があると記録されている。開発工程が相対的に小さいことだけから、
コスト効果も小さい、または施策に価値がないとは結論していない。

## 既存Analysisとの関係

`OBS-20260818-214727-lead-time-waiting-time-priority`は、仮定値を用いて、Lead Timeの
支配項が待ち時間ならProcess Time短縮の全体効果が限定されると整理している。本Observationは、
数値を再現できない一件の実務回想として、局所速度と全体効果を分けて問うたContextを追加する。

## 曖昧さと限界

- 元のVSM、計測資料、スライド画像および施策後の結果を確認していない。
- 回想内の割合は分母、重複、期間、工数またはコストの区別が確定していない。
- 一件からWaterfall一般の工程配分、Agileの効果または高速化施策の価値を一般化できない。
- 局所工程の比率が小さくても、品質、Risk、Capacityまたは戦略上の効果が大きい場合がある。
- SourceのReview metadataと本文が不一致であり、Sourceの意図整合性が完全には確認できない。

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
