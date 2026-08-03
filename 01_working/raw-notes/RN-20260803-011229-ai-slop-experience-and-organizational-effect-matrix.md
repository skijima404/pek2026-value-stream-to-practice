---
id: RN-20260803-011229-ai-slop-experience-and-organizational-effect-matrix
type: raw_note
title: "AI Slop経験と組織効果を分ける2×2の見せ方"
content_language: ja
created_at: 2026-08-03T01:12:29+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-03T01:16:19+09:00
sanitization_checked_by: agent:codex
tags: [presentation-design, ai-slop, organizational-outcome, downstream-load, value-hypothesis, lean-startup, mbpm, decision-matrix]
---

# メモ

## このメモの目的

AI利用による組織Outcomeへの寄与と、Outputを受け取る側に発生する負荷を
混同しないため、2×2で説明する見せ方の候補を記録する。

これは採用済みのスライドではなく、参加者へ判断構造を伝えるための
Presentation Design候補である。

## 2つの独立した軸

- 縦軸: 組織Outcomeへの寄与
  - AI活用を始めた目的に対して、実際にどの程度効果が出たか
  - Lead Time、コスト、リスク、採用、Retentionなど、施策ごとの
    Value Hypothesisに対応して確認する
- 横軸: 受け手に発生した追加負荷
  - 確認、修正、根拠探索、再説明、判断、手戻りなどがどの程度増えたか
  - 上流の生成時間だけでなく、次のActorへ移った仕事を観測する

組織Outcomeへの寄与が高いことと、受け手の負荷が低いことは同じではない。
また、受け手がAI Slopだと感じたことだけでは、そのAI活用を組織として
捨てるべきかまでは決まらない。

## 2×2

| | 受け手の追加負荷が低い | 受け手の追加負荷が高い |
| --- | --- | --- |
| 組織Outcomeへの寄与が高い | 維持・拡大する | 価値は残し、流量制御、ハンドオーバー、Enablementを修復する |
| 組織Outcomeへの寄与が低い | 作らない、または撤退する | 流入を止め、棄却する。橋を架けて延命しない |

## スライド上の囲い方

### 右側の2象限

「受け手の追加負荷が高い」右側の2象限を一つの枠で囲い、
`AI Slopとして経験される領域` と示す。

ここでのAI Slopは、生成物に対する組織としての最終判定ではない。
受け手側に、まだ処理されていない確認、修正、判断などの仕事が届いている
というSignalである。

### 下側の2象限

「組織Outcomeへの寄与が低い」下側の2象限を別の枠で囲い、
`作らない・止める・捨てる領域` と示す。

Release前であればValue Hypothesisの弱い案を作らない。
Release後に価値が支持されなければ、停止またはRetireを検討する。
受け手の負荷が低くても、価値がなければ保守、認知、選択肢、Portfolioの
複雑性を増やすため、残し続ける理由にはならない。

### 右上

右上は今回、明示的な説明が必要な象限である。

- 受け手にはAI Slopとして経験されている
- しかし、組織として残したい価値も出ている

この場合は、Slop経験を否定してはならない。同時に、Slopと呼ばれたことだけを
理由に価値あるTransformationを捨ててもならない。

価値ある変化は残し、受け手へ押し出された仕事を観測して、流量制御、
Service設計、ハンドオーバー、Enablementなどを修正する。

ただし、受け手のCapacityを超えて業務継続が困難になる場合は、価値があっても
流入を一時停止し、修正後に小さく再開する。

### 右下

負荷が高く、組織Outcomeへの寄与も低い。ここではEnablementによって
Solutionを延命せず、流入を止めて棄却する。

## 視覚表現の候補

- 右列をオレンジ色で囲う:
  `AI Slopとして経験される`
- 下段を赤色で囲う:
  `作らない・止める・捨てる`
- 右上へ矢印を付ける:
  `価値を残して橋を架ける`
- 右下へ停止記号を付ける:
  `橋を架けず止める`

`AI Slop` と `捨てるべきもの` を同じ色や同じ囲いにしない。
受け手の経験と、組織としてのPortfolio判断を別の軸として見せる。

## 説明の順序

2×2を最初から抽象的に提示せず、同じOutputを作る側と受け取る側から
見せてから導入する。

例:

```text
作成者:
AIで提案書作成が8時間から2時間になった

Reviewer:
確認が4時間から8時間になった
```

参加者へ次のように問う。

> これは成功でしょうか。AI Slopでしょうか。

この情報だけではまだ判断できない。最終的な組織Outcomeと、受け手に移った
追加負荷を別々に確認する必要がある。その説明後に2×2を提示する。

## Lean StartupとMBPMの役割

- 組織Outcomeへの寄与を判断する:
  - Value Hypothesisを置く
  - Lean StartupでRelease前に選別する
  - Release後は実際に期待したOutcomeが出たか確認する
- 受け手の追加負荷を観測する:
  - MBPMでActor間の境界を見る
  - Process Time、Lead Time、確認、修正、手戻り、受入可能性などを見る

## 中心メッセージ候補

> AI Slopとして経験されるものを、すべて消すわけではない。
> 消すべきなのは、組織Outcomeへ寄与しないものである。

> 「AI Slopだ」という受け手の経験は、下流負荷が増えたという重要なSignalである。
> しかし、それだけでは、そのAI活用を組織として捨てるべきかまでは決まらない。

> 価値のないものは作らない。価値があるのに受け取れないものには橋を架ける。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
