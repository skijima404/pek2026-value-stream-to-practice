---
id: RN-20260730-212352-discard-hypotheses-before-production-commitment
type: raw_note
title: "Productionへの約束前に仮説を捨てる"
content_language: ja
created_at: 2026-07-30T21:23:52+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-30T21:27:20+09:00
sanitization_checked_by: agent:codex
tags: [presentation-planning, value-hypothesis, lean-startup, platform-service, value-stream, ai-slop]
---

# メモ

## 議論の出発点

次の価値仮説をどのように検証するかを検討した。

> AIによって作成速度が上がるほど、Platform Teamには「選ぶ・捨てる・検証する能力」が必要になる。

上流の意思決定が重要であることは一般的にも言われており、外部Researchで
周辺の考え方を確認できる。一方で、この仮説そのものを精緻に組み立てることと、
Value Streamの詰まり方をシミュレーションすることのどちらが有効かを考えた。

## 検証方法についての整理

仮説の精緻化とシミュレーションは二者択一ではなく、順番に実施できる。

まず、観測可能な因果へ分解する。

> AIによってPlatform Service候補の生成速度が上がっても、選定、価値検証、
> 中止判断の処理能力が変わらなければ、未検証候補の滞留や、価値が確認されない
> 候補への投資が増える。

その後、Value Stream上で次のような流れを置き、ボトルネックの移動を
シミュレーションする案がある。

```text
Idea発生
  ↓
Problem Validation
  ↓
Value Validation
  ↓
Prototype
  ↓
User Test
  ↓
Experiment
  ↓
Production候補
```

観測候補:

- IdeaおよびFeature候補の到着率
- 各検証段階の処理能力とWIP
- 検証待ち時間
- 一案あたりの検証コスト
- 各Gateでの中止率
- Production候補へ到達するまでの総投資
- 価値が未確認のまま次段階へ進んだ候補数

比較候補:

1. AI導入前
2. IdeaとPrototypeの生成速度だけが上がる
3. 生成速度と検証能力がともに上がる
4. 検証能力は同じだが、WIP制限と中止Gateを設ける
5. 検証基準が曖昧なまま候補が次工程へ流れ続ける

シミュレーションで確認できるのは、置いた前提のもとで因果が成立するかという
論理的妥当性であり、実際のPlatform Teamでも同じことが起きるという実証ではない。
外部Research、現場観察、過去のPlatform Engineeringの失敗パターンとの照合が
別途必要になる。

## 「捨てる」の意味

ここでいう「捨てる能力」は、一度Productionへ提供したPlatform Serviceを
廃止する能力ではない。

Lean Startupにおける、価値が確認できない案への投資を早期に止める能力を指す。

- Idea段階で捨てる
- Problem Validationで捨てる
- Value Validationで捨てる
- Prototype段階で捨てる
- User Test段階で捨てる
- Experimentの結果を受けて捨てる

三つの能力は次のようにつながる。

- 選ぶ: どの仮説に検証コストを使うかを決める
- 検証する: 継続、修正、中止を判断するための証拠を得る
- 捨てる: 証拠が弱い案への追加投資を止める

捨てることは失敗後の後始末ではなく、学習による正常な投資判断である。

## Platform ServiceではProduction前に捨てたい理由

Platform Serviceは、一度リリースすると、実際の利用開始前でも利用者の計画に
依存を生む。

- 利用者がその機能を使える前提で設計する
- 導入工数や開発費を見積もる
- Roadmapや予算に組み込む
- 関係者へその前提で説明する

この状態で廃止すると、Platform Teamの廃止作業だけでなく、利用者側の計画、
見積もり、設計、説明にも手戻りが発生する。

したがって、Platform ServiceにおけるProduction公開は、単なる提供開始ではなく、
利用者に対する「将来も使える」という約束として扱う必要がある。

今回のセッションでは、Production後のService廃止ではなく、Productionという
約束をする前に、Idea、Problem Validation、User Testなどの段階で価値の弱い
案を捨てる話に絞る。

## 現時点の表現候補

価値仮説:

> AIによってIdeaと実装候補を速く大量に生成できるほど、Platform Teamには、
> 価値ある候補を選び、仮説を検証し、価値が確認できない案への投資を早期に
> 止める能力が必要になる。

短いメッセージ:

> 作るコストが下がったからこそ、約束する前に捨てる。

想定する因果:

```text
AIでIdeaとPrototypeが増える
  ↓
検証能力が追いつかない
  ↓
「とりあえずリリース」が増える
  ↓
利用者がそれを前提に設計・見積もりする
  ↓
Platform側に継続責任が生まれる
  ↓
捨てられないAI Slopになる
```

## 未検証の点

- AI導入によってIdeaとPrototypeの到着率が実際にどの程度上がるか
- 選定、検証、中止判断のどこが先にボトルネックになるか
- WIP制限や中止Gateが、未検証候補への投資をどの程度抑えるか
- Platform Serviceの公開前から、利用者の見積もりや設計に依存が生じる条件
- この因果を説明するために、Value StreamシミュレーションがAudienceにとって
  分かりやすいか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
