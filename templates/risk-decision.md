---
id: RSK-YYYYMMDD-HHMMSS-short-slug
type: risk_decision
title: "残存リスクへの対応判断"
content_language: ja
created_at: YYYY-MM-DDTHH:MM:SS+09:00
created_by: agent:codex
decision_status: current
target_node: HYP-YYYYMMDD-HHMMSS-short-slug
target_component_id: U1
risk_response: proceed_with_risk
decision_sufficiency: sufficient_with_conditions
decided_by: human:kijima
decided_at: YYYY-MM-DDTHH:MM:SS+09:00
relations:
  - type: evaluates
    target: HYP-YYYYMMDD-HHMMSS-short-slug
  - type: informed_by
    target: OBS-YYYYMMDD-HHMMSS-evidence-slug
---

<!--
このTemplateは、Artifact採用または宣言済みの現在Actionに影響する重要な残存リスクを、
人間が明示的に判断した場合だけ使用する。通常の未検証事項や次の学習Stepには使用しない。
対象HYPには、人間Review済みのExtended Validation Componentが必要である。
-->

# 残存リスクへの対応判断

## 判断対象

- 対象となる不確実性:
- Evidence確認後も残るリスク:
- 影響を受ける判断:

## 判断範囲

この判断によって、どの次の行動まで進めるかを限定して書く。

## 理由

確認したEvidenceと、Evidenceでは解消できない不確実性を区別して書く。

## 条件・軽減策

- 条件:

## 再評価Trigger

- 再評価する条件:

## 境界

この判断は、仮説が真であること、独立検証されたこと、Analysisが採用されたこと、
またはArtifactへ採用されたことを意味しない。
