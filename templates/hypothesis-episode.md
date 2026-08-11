---
id: HYP-YYYYMMDD-HHMMSS-short-slug
type: hypothesis_episode
title: "小さな仮説検証のタイトル"
content_language: ja
created_at: YYYY-MM-DDTHH:MM:SS+09:00
created_by: agent:codex
hypothesis_scope: not_assessed
hypothesis_level: not_assessed
status: proposed
# `status: reviewed` の場合は reviewed_at、reviewed_by、
# review_scope: intent_alignment を追加する。
confidence: not_assessed
knowledge_basis:
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-YYYYMMDD-HHMMSS-source-slug
---

# 仮説

## 知識の成立根拠

この仮説が、経験知、外部Research、直接観察、明示的検証、または推論の
どれに基づくかを書く。`practitioner_experience`と`not_tested`は両立する。

## Mobiusでの位置づけ

Value、Solution、Feature Hypothesisのどれとして検討したかを説明する。
タスクの進行状況は記述しない。

## 検証

- アプローチ: `not_selected`
- 学習したい問い:
- 前へ進むSignal:
- 実施内容と範囲:
- 実際に確認した資料・人・記録:
- GenAIの利用: `none`

`research`の場合だけ、次も記録する。

- 資料を選んだ理由:
- 資料が支えられる主張・資料文脈・今回への適用範囲:
- 反証・代替資料を確認した範囲:

アプローチは`experiment`、`research`、`interview`から一つ選ぶ。
まだ選んでいない場合だけ`not_selected`を使う。

複数の重要な不確実性を別々に追跡する場合、または正式なRisk Decisionの
安定した対象が必要な場合だけ、`00_meta/promotion-policy.md`に従って
`## 検証対象の分解`を追加する。

## 結果

`not_tested`

実施後は `supports`、`challenges`、`inconclusive` のいずれかに置き換える。

## 学び

## 解釈

観測対象の範囲を越えて一般化しない。

## 限界と残存不確実性

- 選定上の偏り:
- 未確認の証拠:
- 一般化できない範囲:

## 次の判断

- 判断: `not_decided`
- 判断の対象範囲:
- 次に進めること:

判断は`proceed`、`revise`、`validate_further`、`stop_for_current_scope`から
一つ選ぶ。まだ決めていない場合だけ`not_decided`を使う。`inconclusive`でも
現在Scopeで追加検証しないなら`stop_for_current_scope`としてEpisodeを閉じられる。
