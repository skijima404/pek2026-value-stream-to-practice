---
id: RN-20260804-015137-analysis-skill-required-for-metrics
type: raw_note
title: "MetricからFactを取り出すには分析Techniqueの習熟が必要"
content_language: ja
created_at: 2026-08-04T01:51:37+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-04T01:53:12+09:00
sanitization_checked_by: agent:codex
tags: [metrics, data-analysis, analytical-skill, practitioner-experience, dashboard]
---

# メモ

二段階メトリック分析を説明する場合の重要な前提として、作成者から次の実務判断が
共有された。

- 分析Technique自体が必要である
- DashboardとDataが存在するだけで、分析できるようになるわけではない
- DashboardとDataからFactを取り出せるようになるには、分析の習熟が必要である

Dashboardは違和感を検知する入口になり、BI ToolやDataは深掘りする材料になる。
しかし、問いを立て、適切な比較対象と切り口を選び、Noise、相関、因果、欠損、
定義差を区別して、観測できた範囲を説明する能力はToolやDataだけでは得られない、
という作成者の実務上の判断である。

ここでいう`Fact`は、Dataから自動的に唯一の意味が生成されることではない。
観測条件、定義、比較方法、限界を示した上で、Dataから直接確認できる範囲を
取り出すことを指す。

必要な習熟内容、習熟度の判定方法、Training方法、必要期間は、この記録では
定義していない。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
