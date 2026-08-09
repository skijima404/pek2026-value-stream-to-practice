---
id: RN-20260809-194608-dvs-phase-quality-ai-outcomes
type: raw_note
title: "DVS各フェーズの品質からAI Outcomeを選ぶ"
content_language: ja
created_at: 2026-08-09T19:46:08+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-09T19:54:49+09:00
sanitization_checked_by: agent:codex
tags: [dvs, ai-outcome, process-quality, discovery, decision-quality, delivery, automation, ai-slop, presentation-planning]
---

# メモ

## このメモの位置づけ

AI活用の効果を速度へ集約することへの違和感から、Delivery Value Stream
（DVS）のどこへAIを置くかによって、先に定義すべき品質が異なるのではないか、
と議論した内容を記録する。

ここでのDiscover / Decide / Deliverは、DVS内の知的作業を振り返るための
補助的な区分として使っている。各区分の性質や対応する品質を確立済みの
一般モデルとして提示するものではなく、会話時点の整理である。

## 出発点となった違和感

AIやAutomationの効果は、工数削減、Lead Time短縮、コスト削減として
説明しやすく、測定もしやすい。そのため、AI活用の議論は速度へ集約されやすい。

しかし、DVS全体を対象にすると、速度は品質特性の一つにすぎない。
特にDiscoverやDecideでは、数分を短縮することよりも、誤った問題設定や
意思決定が後段へ与える影響を減らす方が重要な場合がある。

会話では、次の順序でAI活用を設計する案に整理した。

```text
DVSのどこへAIを使うのか
  ↓
その場所では何が「良い状態」なのか
  ↓
その品質を上げるために、AIへ何のOutcomeを期待するのか
  ↓
どのAI機能・Automationとして実装するのか
  ↓
何を観測するのか
```

AI機能やユースケースを先に置くのではなく、対象箇所と必要な品質を先に置く。

## VSM・MBPMで時間を見る意味

VSMやMBPMで時間を見る目的は、すべての作業を一律に速くすることではない。
時間、頻度、待ち、手戻り、担当者間の往復などを、システムの構造を知るための
観測値として使う。

Lead Time短縮を狙う場合は、他が時間単位である中に週単位の箇所があるなど、
プロセス全体の中で桁が違う場所を優先して見る。小さな作業時間だけを見て
改善対象を決めると、全体への効果がほとんどない場所を最適化する可能性がある。

AI生成物のレビューも同じである。1回の確認時間が長く見えても、それだけでは
改善効果が大きいとは言えない。少なくとも次を合わせて見る必要がある。

- 1回あたりの確認・修正時間
- 発生頻度と対象Resource数
- 品質不足に起因する差し戻し、再生成、再確認
- 問い合わせ回答待ちなど、後続で発生する待ち時間

```text
下流負荷の候補
= 1回あたりの処理コスト × 発生回数
  + 誘発された手戻り・待ち・再作業
```

この整理では、短いレビューそのものより、レビュー後に起きる往復や待ちが
支配的な可能性もある。反対に、1回は短くても高頻度で繰り返されるなら、
組織全体では大きな負荷になり得る。

## Discover / Decide / Deliverで異なる品質

会話では、各区分で改善したい品質と速度の位置づけを、次のように仮置きした。

| 区分 | 重要と考えた品質 | 速度の位置づけ | AI Outcomeとの接続候補 |
| --- | --- | --- | --- |
| Discover | Coverage、視点のDiversity、Problem Quality、Blind Spotの少なさ | 副次的になりやすい | 広く探す、分かるように解釈する、本当に筋が通るか疑う |
| Decide | 比較可能性、Reasoning、判断根拠の明示、Decision Quality | 副次的になりやすい | 選べるように整理する、本当に筋が通るか疑う |
| Deliver | Reproducibility、Efficiency、Transaction Cost、エラー率 | 主目的になりやすい | 速く作る、必要に応じて他のOutcomeも組み合わせる |

### Discover — 意図的に探索を広げる

Discoverでは、早く一つの答えへ収束することが常に良いとは限らない。
ある程度散らし、探索空間の広さと異質性を確保することが品質になり得る。

ここでいうDiversityは、議論時点では主に視点や職能の違いを指していた。
たとえば営業、経理、ITでは、同じ事象に対して顧客、市場、収益性、統制、
技術制約、運用など、異なる観点から違和感を見つける。

AIを使う場合も、最初から「最適解」を求めるより、営業、Security、運用、
反対者など異なる視点を仮置きし、見えていない論点を増やす使い方が
Discoverの品質に合う可能性がある。

### Decide — 散らしたものを比較可能にして収束する

Decideでは、Discoverで広げた選択肢や観点を比較可能にし、判断根拠を
明らかにして絞り込む品質が重要になる。

AIには、選択肢、判断軸、Trade-off、リスクを整理させるだけでなく、
Reasoning Chainの飛躍、前提の弱さ、Evidence不足、反例を確認させる使い方が
考えられる。目的はAIへ決定を委ねることではなく、人間が判断できる状態を
強化することにある。

### Deliver — 反復される実行の再現性と経済性を上げる

Deliverは同種の作業を反復する場面が多いため、1回あたりのTransaction Costを
下げる効果が累積しやすく、Automationの経済性が説明しやすい。

決めたものを低コスト、低ばらつきで繰り返せるようにする場面では、
「速く作る」が直接的に効きやすい。ただし、Deliverであっても必要な品質を
満たさず生成量だけを増やせば、下流の確認や修正を増やす可能性がある。

## 頻度とError Costによる違い

会話では、経済性の違いを次のようにも表現した。

```text
Deliver
  高頻度で反復されやすい
  → Transaction Cost削減の累積効果が大きい

Discover / Decide
  反復頻度が比較的低い場合がある
  → 単純な時間短縮より、Error Costを下げる価値が大きい
```

Discoverで誤った問題を選び、Decideで弱い根拠のSolutionを選べば、Deliverが
その誤りを高い再現性で増幅する可能性がある。そのためDiscover / Decideでは、
一回の所要時間よりも、判断が後段へ与えるレバレッジを見る。

ただし、Discover / Decideが常に低頻度で、速度が副次的だと一般化はしない。
運用上頻繁に繰り返す判断や、時間制約そのものが価値を左右する状況もある。
実際の頻度、Error Cost、判断の影響範囲を観測して決める必要がある。

## 5つのAI Outcome分類との接続

既存メモで整理した5つのAI Outcomeは、AI機能をMECEに分類するためというより、
対象箇所で必要な品質に対し、AIへ何を期待するかを選ぶ問いとして理解できる。

```text
AIで何をしたいのか？

1. 速く作る
2. 広く探す
3. 分かるように解釈する
4. 選べるように整理する
5. 本当に筋が通るか疑う
```

この接続により、「広く探す」は単なる検索ではなくDiscoverのCoverageや
視点のDiversityを補強する使い方になり、「選べるように整理する」と
「本当に筋が通るか疑う」はDecideの比較・Reasoning品質を補強する使い方になる。
「速く作る」はDeliverの再現性と経済性を改善する用途へ置きやすい。

一つのOutcomeを一つの区分へ固定するものではない。実際の作業と必要品質に
応じて、複数のOutcomeを組み合わせる。

## AI Slopとの接続

この議論では、AI Slopを速度だけの問題として捉えない。

```text
Discoverで視野が狭い
Decideで根拠が弱い
Deliverで再現性や受入品質がない
```

このように、その場所で必要な品質を満たしていないOutputが下流へ渡ることも、
Slopとして経験される可能性がある。

したがって、一律に生成速度を最適化するのではなく、各場所で何が良い状態かを
先に定義し、その品質に対応するAI Outcomeと観測方法を選ぶ。

> 速くすることが価値なのではない。その場所で重要な品質を改善した結果として、
> 速くなることもある。

## 現時点の制約

- この内容は人間とGenAIの会話を整理したもので、独立した検証結果ではない。
- Discover / Decide / Deliverと品質特性の対応は、会話時点の作業仮説である。
- 視点のDiversityを増やすことが常にDiscovery品質を上げるとは確認していない。
- 各区分の頻度、Error Cost、Transaction Costは対象Value Streamによって異なる。
- 5つのAI Outcomeは網羅的・排他的な能力分類ではない。

## 関連する既存Raw Note

- `RN-20260730-140133-ai-outcomes-and-mbpm`
- `RN-20260806-224717-vsm-mbpm-process-analysis-explanation`

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
