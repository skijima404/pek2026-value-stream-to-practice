---
id: RN-20260805-211320-ai-slop-design-layers
type: raw_note
title: "AI SlopをBuilding Block・Automation・Feature・Serviceの設計層で分ける"
content_language: ja
created_at: 2026-08-05T21:13:20+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-05T21:20:37+09:00
sanitization_checked_by: agent:codex
tags: [ai-slop, automation-design, building-block, feature-design, service-design, test-pyramid, validation]
---

# AI SlopをBuilding Block・Automation・Feature・Serviceの設計層で分ける

## このメモの位置づけ

AI Slopには、AI Solutionとしての当たり前の品質が不足している場合と、Featureまたは
Serviceの価値設計が不足している場合がある。この二つのどちらかだけを登壇で扱う
必要があるのか、構造を示したうえで両方の境界を説明できないか、という会話を記録する。

関連するRaw Noteとして、AI Building BlockからLoop、Graphへ進むAutomationの成熟順序を
整理した`RN-20260805-094034-ai-building-block-automation-maturity`がある。

以下は会話時点の設計整理であり、確立済みの参照ArchitectureやTest Strategyではない。
登壇への採用も決定していない。

## AI Slopの問題層

### Building Block品質

生成、探索、解釈、比較、評価など、個別のAI Building Blockが期待した結果を返せない。

例：

- 検索結果が関連していない
- 要約が重要な条件を落とす
- 分類が安定しない
- Reasoning Reviewが重要な欠落を検出できない
- Outputの根拠を追跡できない

### Automation Design品質

個々のBuilding Blockを接続したAI Solutionが、Automationとして成立していない。

例：

- Building Block間のContractが曖昧である
- 状態遷移、停止、再試行、収束条件がない
- Evaluatorがなく、何をもって次へ進むか判断できない
- Human in the Loopを入れる条件がない
- Contextが後段へ十分に渡らない
- Loopが暴走する、または誤りがGraph内へ伝播する
- 監視、例外処理、Rollbackが不足する

Building BlockとAutomationの問題は、AIを含むSystemの「当たり前品質」が不足している
問題として扱える。従来のSoftware Engineering、Automation Engineering、Workflow
Designの延長にある。

### Feature Design品質

Automationの結果を、利用者にどのような機能として提供するかが不足している。

例：

- 利用者が何を行えるFeatureなのか分からない
- Featureの入出力、操作、Feedback、例外時の振る舞いが分からない
- 内部のLoopやGraphは動くが、利用者の仕事を前へ進めない
- 必要な判断を支援せず、生成された情報だけを増やす

LoopやGraphはFeatureそのものではなく、Featureを実現するAutomation Layerの設計Pattern
として位置づける。

> AutomationはFeatureを実現する構成要素である。

### Service Design品質

Featureを、組織内で誰に、何のために、どの責任と運用条件で提供するかが不足している。

例：

- そもそも必要なServiceなのか確認されていない
- Value Streamのどの摩擦を改善するか分からない
- 誰が利用し、誰が運営し、誰が責任を持つか分からない
- Self-Service、Support、Guardrail、Cost、利用条件が設計されていない
- 何をOutcomeとして観測するか分からない
- Featureが動いても、組織に期待した価値が出ない

今回の登壇で主に扱ってきたのは、Feature DesignとService Designの側である。

## 二つに絞るのではなく、構造を示す

AI Slopを一つの原因で説明せず、次のLayerとして見る。

```text
Service Design
  ↓
Feature Design
  ↓
Automation Design
  ↓
AI Building Block
```

- AI Building Blockが悪い
- Automationが悪い
- Featureが悪い
- Serviceが悪い

のいずれでも、利用者にはAI SlopまたはWorkslopとして経験され得る。対策を考えるには、
SlopがどのLayerから生じたかを見分ける必要がある。

本編でAutomation Designの詳細をすべて説明する必要はない。AI Solutionとしての当たり前
品質が前提にあることを示したうえで、FeatureとServiceの価値設計へ焦点を移す方法がある。

```text
AI Slopには複数の原因Layerがある
  ↓
Building BlockとAutomationの当たり前品質を確認する
  ↓
それだけでは価値のあるFeature／Serviceにならない
  ↓
今回の中心であるFeature DesignとService Designへ進む
```

これにより、Automation品質を無視せず、登壇の中心を内部Architectureだけへ寄せない。

## 設計、実装、検証の向き

### 設計はMarket Inで上から下へ進む

```text
組織・利用者のNeed
  ↓
Service Design
  ↓
Feature Design
  ↓
Automation Design
  ↓
Building Blockの選定・実装
```

何を組織へ提供し、利用者にどの機能を提供するかを先に置き、その要求と制約から
AutomationとBuilding Blockを決める。

### Capabilityは下から上へ積み上がる

```text
AI Building Block
  ↓
Automation Capability
  ↓
Feature
  ↓
Service
```

Building BlockがAutomationを可能にし、AutomationがFeatureを可能にし、Featureが
Serviceを成立させる。上位Layerから要求と制約が流れ、下位LayerからCapabilityが
積み上がるという二つの向きを分けて考える。

## 検証方法もLayerで異なる

会話では、V字ModelとTest Pyramidは競合せず、異なる軸を示すものとして整理した。

- V字Model：設計Layerと対応する検証の関係を見る
- Test Pyramid：検証の量、Cost、粒度の構成を見る

Layer別の対応候補は次の通り。

| 設計Layer | 主な検証候補 | 検証上の性質 |
| --- | --- | --- |
| Building Block | Unit Test、Prompt評価、Benchmark、Evaluator | 比較的多数を機械的に確認しやすい |
| Automation | Integration Test、状態遷移、停止、再試行、Human Review | Block間の接続と制御を確認する |
| Feature | Scenario Test、User Test、UX評価 | 利用者が機能を使って仕事を進められるか確認する |
| Service | UAT、実運用、利用状況、Business／Process Outcome | 組織と業務を含むため最も検証しにくい |

Building Blockの品質が高く、Automationが正しく動いても、Featureが利用者の仕事に合うか、
Serviceが組織に価値を出すかは別途確認が必要である。

## 登壇Scopeの現時点の扱い

- AI Solutionの当たり前品質不足と、Feature／Service Design不足の両方がAI Slopの
  原因になり得ることは示す
- Building Block、Automation、Feature、Serviceという構造を見せる
- 本編の主役はFeature DesignとService Designに置く
- Human in the Loop、Evaluator、Loop、Graphの詳細は、前提説明またはAppendix候補とする
- 「Loopを作れば解決する」という反応に対しては、Loop以前にAutomationとして成立して
  いる必要があると説明できるようにする

これは現時点の構成候補であり、採用済みArtifactではない。

## 限界と未確認事項

- 4 Layerの分け方を既存の標準的なArchitecture Modelへ照合していない
- すべてのAI Slopがいずれか一つのLayerへ排他的に分類できるとは確認していない
- 一つの問題が複数Layerにまたがる可能性がある
- V字ModelとTest Pyramidへの対応は会話上の整理であり、外部Sourceによる検証をしていない
- Layer構造を示すことが参加者の理解を助けるかは未検証である

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
