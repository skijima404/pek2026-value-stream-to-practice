---
id: RN-20260801-001118-pe-investment-purpose-and-sustainable-value-observation
type: raw_note
title: "PE投資目的と提供側の持続可能性を含む価値観測"
content_language: ja
created_at: 2026-08-01T00:11:18+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-01T00:17:14+09:00
sanitization_checked_by: agent:codex
tags: [platform-engineering, value-hypothesis, observability, adoption, retention, sustainability, mbpm]
---

# メモ

## このメモの位置づけ

2026年7月31日から8月1日にかけて行った、Platform Engineering（PE）の価値を
何によって観測するかについての対話を再構成したRaw Note。

- 人間とCodexの発言を分離せず、議論の流れとして記録した
- 特定のMetricを一般解として採用するものではない
- 記載した例は個人の経験と観察に基づき、一般化可能性は検証していない
- ある組織の事例は、分析上必要な構造だけが残るよう一般化した
- PEK2026本編で個別Metricの各論まで扱うことは、現時点では意図していない

## 出発点：価値と下流負荷の二軸

AI Slopを、組織にとっての価値と、受け手が経験する負荷の二軸で整理すると、
少なくとも次の四つに分けられる。

| 組織的な価値 | 受け手の負荷 | 暫定的な扱い |
| --- | --- | --- |
| 高い | 低い | 維持または拡大する候補 |
| 高い | 高い | 価値を残し、Service、Contract、Enablementを修正する候補 |
| 低い | 低い | 継続理由を見直し、選別または棄却する候補 |
| 低い | 高い | 流入を止め、棄却する候補 |

この分類を置いた瞬間に、少なくとも次の二つを観測する方法が必要になる。

1. Value Hypothesisに対して、実際に価値が出たか
2. その価値を成立させるために、下流の誰へどの程度の追加作業が移ったか

特に防ぎたい状態として、対話では次の二つを挙げた。

- 価値の低いOutputを共有資源へ流すこと
- ズレを補完する人力作業が溢れ、提供または利用を持続できなくなること

## 採用はValue Hypothesisの重要な観測点

対象プロジェクトを分母としたPlatform Serviceの採用率は、Value Hypothesisを
観測する一つの手掛かりになる。

```text
適用可能な対象プロジェクト
  ↓
Serviceを検討した
  ↓
採用した
  ↓
実際に利用できた
  ↓
期待したOutcomeへ到達した
  ↓
次回も選んだ
```

採用は、利用者が期待価値を認識し、行動によって選んだことを示す。ただし、採用
だけで期待した価値が実現したとは言えない。採用後のOutcomeと継続も別に観測する
必要がある。

また、組織がPlatform Serviceの利用をMandatoryとしている場合、採用率は価値を
選択した結果にならない。この場合は、例外、回避、離脱、Outcome到達、個別支援量
など、別の観測点が必要になる。

## Metricは投資理由から導く

PEの価値を観測するには、組織がなぜPEへ投資したのかまで戻る必要がある。

```text
組織がPEへ投資した理由
  ↓
Value Hypothesis
  ↓
期待するOutcome
  ↓
その変化を知るための観測
```

例として、対話では次の対応を挙げた。

- Lead Time短縮が目的なら、Lead Time上の変化を見る
- コスト削減が目的なら、工数や投入Resourceの変化を見る
- ガバナンスが目的なら、必要な統制を満たしつつFlowを損なっていないかを見る

このため、すべてのPlatform Teamへ共通のMetricを置くだけでは、投資目的に対する
成否を十分に説明できない可能性がある。

## ガバナンスとFlowを対で見る

セキュリティなどのガバナンスは、事故が起きなかったことをPE単独の効果として
説明しにくい。また、統制の数または実施件数だけを増やすと、すべてを止める方向へ
局所最適する可能性がある。

対話では、ガバナンスに関するPEの期待結果を次のように表現した。

> より多くの対象プロジェクトが安全な標準Pathを利用しても、Lead Timeと人力負荷が
> 悪化していないこと。

概念上は、次の変化を対で観測する。

```text
採用または適用範囲     増加
ガバナンス充足         維持または向上
Lead Time              維持または短縮
個別対応・補完工数     維持または削減
```

ただし、これは固定KPI案ではなく、「ガバナンスを満たした結果、Flowまたは人力負荷が
どう変わったかも同時に見る」という観測上の考え方である。

## KPIではなくObservability

今回の本編で個別Metricを詳しく扱うことには違和感がある。対話では、その理由を
次のように整理した。

- 共通Metricの採用そのものが主題になると、PEの効果測定一般の話へ広がる
- 4 Keysのような最終結果に近いMetricは、異常が見えても修正箇所を診断しにくい
- Waterfallを含む組織では、Delivery modelとMetricの前提が噛み合わない場合がある
- Metricを改善目標にすると、数値自体の局所最適を招く可能性がある
- Platform Serviceの採用、境界での待ち、追加作業、責任移行を直接表すとは限らない

したがって今回扱いたいMetricは、目標管理または評価のためのKPIというより、
Value Streamの状態を知るためのObservabilityである。

```text
KPI
「この数字を良くする」

Observability
「今、どこで何が起きているかを知る」
```

MBPMのProcess Time、Lead Time、Resources、`% Complete & Accurate`なども、固定された
達成目標としてではなく、AIで速くなったStepの後に、待ち、修正、追加、確認、
人力補完が移っていないかを発見する計器として扱う。

対話上の短い表現は次のとおり。

> KPIを置くのではなく、Value Streamに計器を置く。

## 個々の施策にも固有の目的がある

組織全体がPEへ投資した理由だけでなく、個々の施策が何のために行われたかも
観測する必要がある。

Platform Teamの立ち上げ初期には、Platform Serviceを作る以前に、メンバーがPEの
仕事をできる状態を作るため、本来のPEとは異なる定型作業の自動化などを行う場合が
ある。

```text
施策
Platform Teamが抱える定型作業を自動化する

直接Outcome
定型作業の工数や割り込みを減らす

意図した次のOutcome
空いたCapacityをDiscoveryやPlatform Service開発へ再配分する

PE投資としてのOutcome
価値のあるPlatform Serviceを選別・提供できる能力を作る
```

この場合、作業時間を減らしただけでは意図したOutcomeへ到達したとは限らない。
空いたCapacityが別の非PE作業に吸収されたなら、施策の直接効果は出ていても、次の
価値へ接続していない。

したがって観測には、少なくとも次の二つの階層がある。

1. その施策自体を何のために置いたか
2. その変化が、組織がPEへ期待した価値へ接続したか

## PEチーム自身のRetentionを目的とした事例

個人が観測したある組織では、PEへ投資した最初の理由が、Platform利用者の生産性
ではなく、Platform Teamへ配属する技術人材のRetentionだった。

その組織では技術人材の退職が課題となっており、新しく挑戦的な領域としてPEを
立ち上げ、組織に残ってほしいメンバーをアサインした。

この事例を仮説の形で表すと、次の構造になる。

```text
Problem Hypothesis
重要な技術人材が、既存の仕事で十分な挑戦、裁量、成長機会を得られず退職する

Solution Hypothesis
新しく挑戦的なPE領域を立ち上げ、対象メンバーへ役割を提供する

期待Outcome
対象メンバーが組織に残り、PE Capabilityが組織内に蓄積される
```

この場合、利用者の認知負荷が減り、開発生産性が向上しても、残ってほしかった
Platform Teamのメンバーが退職すれば、当初の投資目的には失敗している。

一方で、Retentionだけを実現し、利用者へ価値の弱いPlatform Serviceを作り続ける
ことも正当化できない。そのため、この事例では少なくとも二つのValue Hypothesisを
分けて考える必要がある。

```text
組織内部への価値
重要な技術人材を定着させ、Capabilityを蓄積する

Platform利用者への価値
利用者の仕事を実際に改善するPlatform Serviceを提供する
```

## 利用者価値と提供側の持続可能性

利用者の認知負荷または手作業を減らしても、その複雑性をPlatform Teamが無制限に
引き受けているなら、トータルサービスとしては持続できない。

```text
利用者
認知負荷が下がる
開発生産性が上がる

Platform Team
問い合わせ、例外対応、個別支援、知識更新が集中する
面白い開発より後処理が増える
疲弊または退職が起きる

結果
Platform Serviceを維持できない
```

これは、利用者側の負荷を解消したのではなく、見えにくい提供側のLaneへ移した状態
と解釈できる。

対話上の暫定的な結論は次のとおり。

> PEの価値は、利用者が価値を得られることと、その価値をPlatform Teamが
> 持続可能な形で提供できることの両方で成立する。

また、MetricまたはOutcomeを考える前に必要な問いは次のように整理できる。

> 誰のOutcomeを見ているのか。組織は何を期待してPEへ投資したのか。この施策は
> そのReasoning Chainのどこへ作用するのか。

## PEK2026本編への接続候補

本編では具体的なMetric一覧を提示せず、次の考え方までを扱う候補とする。

```text
組織がPEへ投資した理由を確認する
  ↓
個々の施策の目的を確認する
  ↓
Value Hypothesisに対応する変化を観測する
  ↓
AIで変化したStepの前後をMBPMで観測する
  ↓
利用者だけでなく、下流と提供側へ移った人力負荷を見る
```

持ち帰り候補となる短い表現:

> 大事なのは共通Metricを採用することではない。組織がPEへ期待したOutcomeと、
> AIによってValue Streamのどこへ負荷が移ったかを観測できることである。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
