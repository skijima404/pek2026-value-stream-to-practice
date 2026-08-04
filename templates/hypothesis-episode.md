---
id: HYP-YYYYMMDD-HHMMSS-short-slug
type: hypothesis_episode
title: "小さな仮説検証のタイトル"
content_language: ja
created_at: YYYY-MM-DDTHH:MM:SS+09:00
created_by: agent:codex
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

## 期待する兆候

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | 確認したい不確実性 | high | none | not_checked | unknown | unknown | 現時点で残っている不確実性 |

`Evidence refs`には、このリポジトリで実際に確認したEvidenceを表す`OBS-*`を
カンマ区切りで記載する。Raw NoteやExternal Inputを直接Evidenceとして使わず、
その内容・成立根拠・限界をObservationへ昇格してから参照する。

`Coverage state`は確認した範囲であり、正しさの割合ではない。
`not_checked`の場合は`Evidence refs: none`、`Finding: unknown`、
`Applicability: unknown`とする。Evidenceを確認したが判断できない場合は
`Finding: inconclusive`を使う。

## 検証方法

### 方法と対象範囲

- 方法:
- 対象・資料:
- 選定方法:
- 実施規模:

### GenAIの利用

- 利用内容: `none`
- 実際に確認した資料・記録:

## 結果

`not_tested`

実施後は `supports`、`challenges`、`inconclusive` のいずれかに置き換える。

### 実際に観測したこと

## 解釈

観測対象の範囲を越えて一般化しない。

## 限界

- 選定上の偏り:
- 未確認の証拠:
- 一般化できない範囲:
- 残存リスクと影響を受ける判断:
