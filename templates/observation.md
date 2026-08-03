---
id: OBS-YYYYMMDD-HHMMSS-short-slug
type: observation
title: "観察の短いタイトル"
content_language: ja
created_at: YYYY-MM-DDTHH:MM:SS+09:00
created_by: agent:codex
status: proposed
# `status: reviewed` の場合は reviewed_at、reviewed_by、
# review_scope: intent_alignment を追加する。
confidence: not_assessed
knowledge_basis:
  - recorded_statement
relations:
  - type: derived_from
    target: RN-YYYYMMDD-HHMMSS-source-slug
---

# 観察

## 知識の成立根拠

`knowledge_basis`の各値が、どのSourceまたは記録に対応するかを書く。
経験知は検証結果に置き換えず、適用範囲と再現できない点を明示する。

## 根拠箇所

根拠ノードの該当箇所を引用または正確に指定する。

## 根拠から直接言えること

根拠から直接言える範囲だけを書く。

## 曖昧さと限界

解釈が必要な点、分からない点を書く。
