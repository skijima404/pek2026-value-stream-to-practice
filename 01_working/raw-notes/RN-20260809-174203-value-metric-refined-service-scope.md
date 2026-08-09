---
id: RN-20260809-174203-value-metric-refined-service-scope
type: raw_note
title: "価値指標の設計が標準Pathの対象Scopeを修正した事例"
content_language: ja
created_at: 2026-08-09T17:42:03+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-09T18:55:42+09:00
sanitization_checked_by: agent:codex
tags: [adoption, case-recollection, expected-signal, feature-scope, metrics, platform-service, value-hypothesis]
---

# 価値指標の設計が標準Pathの対象Scopeを修正した事例

## この記録の位置づけ

Platform ServiceのConcept段階で起きた最近の一事例について、実践者が対話で
振り返った内容を記録する。技術、組織、案件および個人を特定できる情報は保存せず、
対象技術は「特定の実行基盤」と一般化する。当時の企画資料、Metric定義、Persona、
Journeyまたは意思決定記録は、この対話では確認していない。

## 当初のFeature案

当初は、特定の実行基盤を汎用的に利用できる標準PathをFeature案として検討していた。
Concept段階でAdoption Metricを設計しようとしたところ、Marketingの観点から
「誰が採用するのか」という疑問が提示された。

実行基盤を利用するActorと利用文脈によって、必要なMarketingおよびEnablementの
活動が変わる。それに伴い、必要な標準PathのPatternも変わるため、汎用的な利用を
前提にしたままではMetricの意味とFeatureの詳細を十分に定められなかった。

## 分析と判断更新

Persona分析とJourney分析を改めて行った結果、汎用的に利用できるようにするという
対象設定は粗すぎて、作るものを絞り込めないと判断した。

最終判断OwnerはPOであり、PdM相当の役割を担うTeam LeaderがPOの当初想定へ反証を
提示した。判断は実装、Releaseまたは利用者による依存形成より前のConcept段階で行われ、
Feature案を小規模Application向けの標準Pathへ修正した。

Metricは実測されていない。Metricを設計して測定対象を明示しようとする活動が、
不足していた利用者視点を発見し、Actor、利用文脈およびFeature Scopeを再検討する
契機として働いた。

## 実践者のより広い認識

実践者が観察するTeamでは、Metricを置く活動が、不足していた視点から対象を見直す
Lensとして現れることが多い。一方、Release後は既に形成された依存や投資のため、
廃棄判断まで進みにくいと実践者は認識しており、国内ではその傾向を特に感じている。

これは実践者の経験範囲についての説明である。比較資料、発生件数、他地域との差または
一般化可能性を確認していないため、今回の一事例のFindingや地域一般の事実として
扱わない。

## この記録だけでは分からないこと

- 当時設計したAdoption Metricの詳細と、Metricを置かなかった場合の判断
- Persona分析およびJourney分析で確認した一次Data
- Metric設計、Marketing Review、Persona分析およびJourney分析のどれが判断更新に
  どの程度寄与したか
- 技術、Capacity、Portfolioまたは通常のScope Reviewだけでも同じ修正が起きたか
- 修正後のFeatureが実際に利用され、期待した顧客価値またはAdoptionを生んだか
- Release後の廃棄困難性が他のTeam、組織または地域へ一般化できるか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
