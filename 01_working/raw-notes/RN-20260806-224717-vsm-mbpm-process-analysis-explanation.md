---
id: RN-20260806-224717-vsm-mbpm-process-analysis-explanation
type: raw_note
title: "VSM・MBPMによるプロセス分析の登壇用解説"
content_language: ja
created_at: 2026-08-06T22:47:17+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-06T23:54:39+09:00
sanitization_checked_by: agent:codex
tags: [vsm, mbpm, process-analysis, process-improvement, presentation-planning, platform-advisor]
---

# メモ

## プロセス分析部分

状況把握のため、対象JourneyのOverviewをVSMで表し、改善候補となる一部をMBPMで掘り下げる。
MBPMはActorごとのProcessとActor間のハンドオーバーを表現できるため、特に担当者間のやり取りがある題材に適している。

### なぜVSMやMBPMを使うのか

Platform Engineeringには、利用者へ価値を届けるプロセス全体を改善する側面がある。
Leanでは、待ち、滞留、手戻りなど、Flowを阻害する箇所を改善対象として扱う。
この考え方をもとに、まずはタスクごとの時間とプロセス全体にかかる時間を可視化し、そのうちの想定外に長い場所や手戻りの多い場所に着目して改善機会（「ムダ」）を発見する考え方が、シンプルで実施しやすい。

この方法には、次の利点もある。

- 付加価値のある作業と、付加価値が限定的な作業が見分けやすい
- 思いついたソリューションの効果仮説を簡単に算出できる
- 実施した施策の効果や副作用の観測ポイントを特定しやすい
- 効果測定時、効果のプロセス全体への影響がわかりやすい

### VSMやMBPMの効果が限定的と思われる点

- 長い間利用されているプロセスは個人の努力に支えられ、表面上は上手くできているように見えても、実施担当者が違和感を覚えている場合がある。このような違和感は時間や手戻りのMetricだけでは見えにくい
  - 別途付箋の周りにそういった「工夫しているポイント」や「モヤモヤを感じるポイント」を貼り、実施担当者の所感と合わせて分析することもできる
- 特に高度に属人化している箇所は見分けにくく、Metricだけではリスクの高い箇所を特定しきれない
  - これも別途表現すると良い
- 工数を扱う場合は、Resource数と各Resourceの稼働時間を別途記録する。PTは実作業時間を表すが、複数人で実施した場合の総工数とは同義ではない。LTも工数を表すものではない

### ムダの分析

- 一般的な「7つのムダ」を参照し、観測した待ち、手戻り、移動などを分類する
- ムダを分類した後、特定のタスクをなくす、他のタスクと統合する、または短くするといった改善方法を検討する
- 特に付加価値が限定的な作業に着目する。ただし、法令対応、安全確認、統制など、付加価値を直接生まなくても残す必要がある作業とは区別する

### 解決策のアイデアを出したら

- VSMやMBPMに記録されたタスクの時間をもとに、解決策のアイデアがうまくいった場合のPT/LT/手戻り率を記録しておくと、後でアイデアの比較をする際に効果の大きさを比較しやすい

### Platform Advisorのシナリオでの利用上の注意点

- Platform Advisorのゴールは「IT投資総額の50%を占めている既存システム運用費を半減」であり、プロセスの短縮がビジネスアウトカムの実現を必ずしも意味しない。
  - ここでは「時間や手間がかかる作業は避けたいと思っているに違いない」という前提で、所要時間を認知負荷の対応にかかる時間の長さとして扱っている

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
