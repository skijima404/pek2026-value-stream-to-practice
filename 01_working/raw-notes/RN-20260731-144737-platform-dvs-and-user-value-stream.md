---
id: RN-20260731-144737-platform-dvs-and-user-value-stream
type: raw_note
title: "Platform ServiceのDVSと利用者Value Streamを接続して観測する"
content_language: ja
created_at: 2026-07-31T14:47:37+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-31T14:52:46+09:00
sanitization_checked_by: agent:codex
tags: [ai-adoption, development-value-stream, mbpm, platform-service, sdlc, value-stream]
---

# メモ

## 出発点

AI活用を考える時、Platform ServiceへAI機能を組み込むことだけでなく、
Platform Team自身がPlatform Serviceを企画、設計、実装、検証、運用する
Development Value Stream（DVS）で、AIをどのように使っているかも
確認する必要がある。

元のCfPには、次の二つのAI活用が含まれていた。

1. Platform Team自身がAIを使ってService開発を高速化する
2. AIをPlatform Serviceへ組み込み、利用者へ提供する

この二つは、同じ「AI活用」でも、異なるValue Streamへ作用する。

## AIを生成以外の目的で使えているか

DVS側のAI活用が、Code、Document、Test、Feature候補などを
「速く作る」ことだけに偏っていないかを確認したい。

```text
Discovery能力: 変わらない
Decision能力: 変わらない
生成能力: 爆発的に増える
検証能力: 変わらない
```

この状態では、選択能力と検証能力を超える量のSolutionまたはFeatureが
Deliveryへ流れ、AI Slopを生む条件になる。

Platform ServiceのSDLC全体を対象に、AIで何を作るかではなく、
どの認知、判断、品質保証能力を増強したいかを確認する方法が考えられる。

## SDLC全体に対するAI活用レビュー

先に「各工程へどのAIを置くか」を決めるのではなく、Process、判断点、
ハンドオーバー、品質Riskを見た後で、AIの適用可能性を確認する。

```text
Platform ServiceのSDLCを可視化する
  ↓
各工程の作業、判断、ハンドオーバー、品質Riskを見る
  ↓
AIで得たいOutcomeを選ぶ
  ↓
Value HypothesisとRisk Hypothesisを置く
  ↓
限定導入して測定する
```

各工程の確認項目候補:

| 観点 | 問い |
| --- | --- |
| Activity | ここでは何をしているか |
| Decision | 誰が何を判断しているか |
| Friction | 待ち、探索、認知負荷、手戻りは何か |
| Quality | 何を間違えると後工程へ影響するか |
| AI Outcome | 生成、探索、解釈、整理、反証のどれが必要か |
| Human Role | 最終判断と責任を誰が持つか |
| Handover | 次の人が何を受け取れば進めるか |
| Evidence | 品質またはOutcomeの改善を何で確認するか |
| Risk | AIによって新しく増える負荷は何か |
| Control | 停止、縮退、人間へのEscalationをどうするか |

これは、全工程にAIを置くためのChecklistではない。
AIを使わない工程、または人間の判断を維持する工程も選択肢に含める。

## Discoveryで考えられるAI活用

生成よりも、次のような認知、探索、反証への利用が考えられる。

- 利用者Feedbackの構造化
- 過去事例または類似課題の探索
- Problem Statementの曖昧さ検出
- Outcome Breakdownの抜け漏れ確認
- Value Hypothesisへの反例提示
- 事実、経験、仮説、解釈の分類

## Decisionで考えられるAI活用

- Solution Optionを広げる
- 判断軸、影響、Trade-off、Riskを整理する
- 未検証の前提を抽出する
- Reasoning Chainの強度を確認する
- 「作らない」「捨てる」というOptionを含める

## DeliveryとLearnで考えられるAI活用

- 実装、Test、Documentationを生成する
- Acceptance Criteriaとの不一致を検出する
- 変更影響を分析する
- 根拠、前提、人間の判断をTrace可能にする
- 利用状況とOutcomeの乖離を検出する
- Release後のFeedbackを分類し、仮説へ戻す
- Contract mismatchまたはDriftの兆候を探す

同じAIに生成と品質保証を任せるだけでは、同じ前提または盲点を
再生産する可能性がある。
生成、反証、根拠確認、人間のAcceptanceを意識的に分ける必要があるという
注意も置いた。

## Platform Serviceを作るDVS

Platform Team自身のDVSを、例えば次のように見る。

```text
Discovery
  ↓
Decision
  ↓
Design
  ↓
Implementation
  ↓
Review
  ↓
Release
  ↓
Learn
```

DVS側のVSMまたはMBPMで見たいもの:

- AIでどの工程が速くなったか
- 探索、判断、検証能力も上がったか
- Reviewまたは承認へ負荷を移していないか
- Feature候補、Output、Queue、WIPを増やしていないか
- AIから人間へのハンドオーバーが成立しているか
- 学習がValue HypothesisまたはSolution Hypothesisへ戻っているか

## Platform利用者側のValue Stream

利用者がPlatform Serviceを知り、選び、利用し、開発と運用を進める
Value Streamを別に見る。

```text
認知
  ↓
選定
  ↓
利用開始
  ↓
開発
  ↓
運用への移管
  ↓
継続利用
```

利用者側のVSMまたはMBPMで見たいもの:

- 利用者が次の判断または作業へ進めたか
- 探索、判断、待ち時間が減ったか
- 修正、追加、確認、誤判断、例外対応が増えていないか
- Platform、Application、Security、Operations間のハンドオーバーが
  成立しているか
- Service Contractと期待された体験を満たしたか
- 実際の利用者OutcomeまたはBusiness Outcomeが出たか

## 二つのValue Streamを接続する

DVSと利用者側Value Streamは、独立したMapとして閉じない。

```text
Platform ServiceのDVSで作る
  ↓
利用者側Value Streamで使われる
  ↓
Slop経験、Outcome、Trust、Contract充足を観測する
  ↓
DVSのDiscoveryとDecisionへ学習を戻す
```

AIでDVSだけを高速化しても、利用者側が詰まれば局所最適になる。

反対に、利用者向けAI機能が便利でも、その保守、Review、Enablement、
SupportによってPlatform TeamのDVSが破綻すれば持続しない。

MBPMは両側で使える。

- DVS側:
  企画、設計、生成、Review、Release、Learn間のハンドオーバー
- 利用者側:
  Platform、Application、Security、Operations間のハンドオーバー

両者を接続する境界では、Release、利用開始、Enablement、Support、
Feedback、改善判断を観測する必要がある。

## AIによる品質向上をどう見るか

AIによって生成量が増えたかではなく、次を確認する。

- 抜け漏れが減ったか
- 判断根拠が明確になったか
- 誤りまたはズレを早く発見できたか
- 次工程の`% Complete & Accurate`が上がったか
- 利用者Outcomeとの不一致を早く検知できたか
- 学習を次のValue HypothesisまたはSolution Hypothesisへ戻せたか

## 現時点の表現候補

> AIで何を作るかではなく、Platform ServiceのSDLC上で、
> どの認知、判断、品質保証能力を増強するかを網羅的に点検する。

> Platform Serviceを作るValue Streamと、
> Platform Serviceを使って価値を得るValue Streamを接続して観測する。

## 留保

- このメモは会話中に形成した検討案であり、採用済みの登壇構成ではない
- DVSと利用者側Value Streamの具体的な範囲、Actor、Metricは
  対象組織またはServiceごとに異なる
- AI活用を全工程へ広げること自体を目的としない
- VSMまたはMBPMだけでOutcome、Experience、Trustを完全に測定できるとは
  していない

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
