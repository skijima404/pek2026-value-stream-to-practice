---
id: RN-20260806-014446-platform-advisor-business-goal-and-blind-spot
type: raw_note
title: "Platform Advisor物語のビジネスゴールとBlind Spot"
content_language: ja
created_at: 2026-08-06T01:44:46+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-06T02:10:06+09:00
sanitization_checked_by: agent:codex
tags: [platform-advisor, worked-example, business-goal, platform-engineering, kubernetes, value-hypothesis, blind-spot]
---

# メモ

以下はPlatform Advisorの通し事例で使用する物語世界の初期設定であり、実在組織の分析結果ではない。

## Platform Advisorが前提とするビジネスゴール

基準時点でIT投資総額の50%を占めている既存システム運用費を半減し、削減によって生まれた投資余力を新規ビジネスや価値創出へ振り向ける。IT投資総額が一定の場合、既存システム運用費の構成比は50%から25%へ低下する。

## 背景にある問題

IT投資を分析したところ、基準時点でIT投資総額の50%が、新規ビジネスや価値創出のための開発ではなく、既存システムの運用に使われていることがわかった。
(注釈: Three Horizon Model でいうところの、Horizon 1)

これではビジネスがスケールするための投資ができない。
そのため、既存システム運用費を半減し、投資総額が一定の場合に構成比を50%から25%へ下げることを目標とする。

コスト削減のため、Kubernetes基盤を導入し、運用を標準化することで人件費を削減する。

### 補足

この人件費削減は、リストラを意味しない。
Opsは手作業の多さや属人的作業の多さから運用品質の担保に苦しんでいる。
今まではこれを人の手でカバーしていた。
しかしAI時代は開発のスピードが上がり、より多くのアプリケーションがリリースされる可能性がある。
これを考えると、人の手をより戦略的な、運用高度化の取り組みに集中し、運用品質の担保も同時に狙うことを考えている。

## Platform Engineering発足の経緯

Kubernetes基盤を整備したが、期待したほど利用されなかった。基盤を作るだけでは、運用の標準化と既存システム運用費の削減にはつながらない。

そこで、利用者の課題を理解し、標準Pathの利用を支援し、利用状況から継続的に学習・改善するためにPlatform EngineeringのTeamを発足させた。Platform Teamの目的はKubernetesを使わせること自体ではなく、Platformの活用を通じて既存システム運用費の削減と運用品質の向上を実現することである。

## Platform Teamが置く初期仮説

Platform Teamは、Kubernetes基盤が使われないのは、利用者が「どのような場合に使えばよいか」を判断できないからに違いない、と考える。

利用者のContextに応じて、利用すべきPlatformや標準Pathを案内すれば、利用者は適切にPlatformを選び、安全に次の作業へ進めると想定する。この想定から、Platform AdvisorというSolution案が生まれる。

## 作者だけが知るBlind Spot

物語内のPlatform Teamは気づいていないが、「利用者は自分でPlatformを選びたい」という前提そのものが、重要な未検証の仮説である。利用者の中には、Platformを比較して選びたいのではなく、自分のContextで安全に使える標準Pathを示され、選択と説明の負荷を減らしたい人がいる。

作者はこのBlind Spotを知っているが、物語内のPlatform Teamには当初気づかせない。この仮説を見落としたままPlatform Advisorを作るため、物語ではAdvisorがあまり使われない、または利用されてもProjectの意思決定に影響する使われ方をしない結果になる予定である。

この設定は、当面は登壇ですべて説明せず、このRepositoryで読める背景情報として保存する。登壇時間に余裕があれば、「実はこのAdvisorはあまり使われない結果になる。彼らが気づいていない重要な仮説があった」とだけ示し、詳細はRepositoryへ誘導する案を候補とする。


## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
