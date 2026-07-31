---
id: RN-20260731-214443-necessary-friction-experienced-as-slop
type: raw_note
title: "Slopと感じても残すべき摩擦"
content_language: ja
created_at: 2026-07-31T21:44:43+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-31T21:52:12+09:00
sanitization_checked_by: agent:codex
tags: [ai-slop, accountability, enablement, friction, governance, learning, platform-service, responsibility-boundary]
---

# メモ

## このメモの位置づけ

2026年7月31日の対話から、「利用者がSlopと感じても、あえて解消しない方がよい
摩擦はあるか」という問いを抽出したRaw Note。

- 人間とAssistAの発言を分離せず、議論の流れとして再構成した
- 利用者のSlop経験を否定するのではなく、摩擦を除去すべきか判断するための
  境界条件として整理した
- 会話上の発散であり、検証済みの一般論または採用済みArtifactではない
- この論点はEnablementとPlatform Teamの組織設計へ広がるため、PEK2026本編では
  中心テーマにしないという判断も含む

## 最初の問い

AIによって追加の確認、判断、学習、Reviewが発生すると、受け手はそれをSlopと
感じうる。しかし、受け手が負荷を感じたという理由だけで、すべての摩擦を
Platform TeamまたはAIが除去することが妥当とは限らない。

対話では、摩擦を次のように分ける案が出た。

```text
解消すべき摩擦
=
本来なくても価値提供、品質、責任分担が成立する摩擦

残す必要がある摩擦
=
品質、学習、判断、責任分担、安全性のために必要な摩擦
```

「必要な摩擦」という分類は、受け手の負荷を軽視するためではない。摩擦をなくす
代わりに、判断責任またはRiskを別の場所へ隠していないかを確認するためのもの。

## 1. PlatformのScope外にある能力を肩代わりする摩擦

利用者側に必要なAI Literacy、Architecture Literacy、業務知識などが不足している
場合、Platform TeamによるEnablementが必要になることはある。

しかし、利用者固有のArchitectureを毎回Platform Teamが設計すると、次の状態に
なりうる。

```text
利用者
必要な設計能力を獲得しない

Platform Team
個別案件の設計Teamになる

Platform Service
標準化、改善、Scaleが進まない
```

会話では、次の境界を候補とした。

- 教育、標準Pattern、Sampleを提供する
- 判断材料を提供する
- ReviewとFeedbackを提供する
- ただし、利用者が持つべき能力または個別案件の設計責任を恒久的に代替しない

これは、利用者の能力不足を一律に自己責任とする主張ではない。想定Personaの
知見と実際の利用者像が合わない場合には、Platform Service側のPersona、Contract、
Value Hypothesisを見直す必要がある。

## 2. 判断責任を引き受けるための摩擦

AI AdvisorまたはPlatform Serviceが、選択肢と判断材料を提供することはできる。
一方で、個別SystemまたはProductの最終判断を、常にAIまたはPlatform Teamが
肩代わりすることは適切とは限らない。

例:

```text
AIまたはPlatform
候補、根拠、前提、Risk、Review条件を示す

System Owner、Product責任者、Architect
自分の責任範囲で採用、却下、例外を判断する
```

この時に人間へ残る確認または判断は、単なる無駄なSlopではなく、Accountabilityを
引き受けるための摩擦である可能性がある。

ただし、最終判断権限の配置は組織ガバナンスによって異なるため、今回の会話では
一般的な正解を決めていない。

## 3. 学習のための摩擦

利用者がAIまたはPlatformに答えを求めるだけで作業を完了できる場合、短期的な
Process Timeは短くなる。

一方で、次を考える機会が失われる可能性がある。

- なぜその設計になるのか
- どこに責任境界があるのか
- 何が標準で何が例外か
- どの前提が変わると判断も変わるのか

Platformを操作できる人を増やすことと、Platformを正しく適用できる人を育てる
ことは同じではない。必要な学習まで自動化によって隠すと、例外時または障害時に
判断できる人が育たない可能性がある。

ただし、どの摩擦が本当に学習へ寄与したかは、この対話では検証していない。
単に不便な作業を「成長のため」と正当化しないよう注意が必要である。

## 4. Governanceと安全性を成立させる摩擦

Review、承認、根拠確認には、単純な品質検査以外の役割がある場合がある。

- 誰が判断したかを明確にする
- 意思決定を関係者間で共有する
- 専門知識を伝播する
- Riskを引き受けられるか確認する
- 例外を組織として認識する

AIがReviewできることを理由に人間の関与をすべて削ると、責任所在または組織的な
合意まで失う可能性がある。

一方、すべての承認または会議が必要な摩擦とは限らない。摩擦の目的が明示できず、
Outcome、品質、学習、Accountabilityのどれにも寄与しないなら、削減対象になりうる。

## Platformが提供するものと、代替しないもの

会話では、概念的に次のような境界を置いた。

```text
Platformが提供する候補

- 知識へのAccess
- 標準Path
- 判断材料
- 自動化
- 良い例
- Feedback

Platformが恒久的に代替しない候補

- 個別案件の最終判断
- 基礎能力不足の完全な肩代わり
- 利用者固有の業務責任
- 価値判断そのもの
```

この境界は固定された一般解ではない。Mandatory、Recommended、Optionalなど、
Platformの位置づけと組織ガバナンスによって変わる。

## 「どの橋を誰が架けるか」という問い

対話の暫定的な言い換え:

> Enablementで橋を架けるべきでないケースというより、その橋はPlatformが
> 架ける橋なのか、利用者自身が渡れるようになるべき橋なのかを判断する。

摩擦を観測した時には、少なくとも次を分ける必要がある。

- ServiceまたはContractの不足なのでPlatform側で除去する
- 初期学習または移行なので一時的にEnablementする
- 利用者の責任または能力なので、判断材料と学習機会を提供して残す
- Governanceまたは安全性のために意図的に残す
- 価値に寄与しないため削除する

## AI Slopとの関係

利用者が追加の確認または判断を求められれば、Slopとして経験する可能性がある。
その経験は、下流へ仕事が来ているという観測として扱う必要がある。

ただし、その後の判断は別である。

```text
受け手がSlopと感じた
  ↓
どの仕事が追加されたか観測する
  ↓
その摩擦は価値、品質、学習、責任、安全性に必要か確認する
  ├─ 不要
  │    → 削減する
  └─ 必要
       → なぜ必要か明示する
       → 実行可能な負荷にする
       → 必要なSkill、権限、支援を整える
```

したがって、Slop経験を否定せず、かつ「利用者が嫌がる摩擦はすべてなくす」とも
しない。必要な摩擦であっても、受け手のCapacityを超えるなら流量制御、段階導入、
Training、支援または役割再設計が必要になる。

## Session Scope

この論点はPlatform Teamの責任境界、Enablement、組織ガバナンスへ広がるため、
PEK2026本編では詳細を扱わない候補とした。

残す場合も、次の境界条件として短く触れる程度とする。

> Slopとして経験された摩擦をすべて除去するとは限りません。必要な判断、学習、
> 責任または安全性の摩擦なら、目的を明示し、受け手が引き受けられる形へ
> 設計し直します。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
