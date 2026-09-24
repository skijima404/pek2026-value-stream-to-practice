---
id: OBS-20260924-101435-ai-slop-design-layers
type: observation
title: "AI Slopの原因候補をBuilding Block・Automation・Feature・Serviceへ分ける設計整理が記録された"
content_language: ja
created_at: 2026-09-24T10:14:35+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-09-24T10:48:49+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260805-211320-ai-slop-design-layers
  - type: references
    target: OBS-20260827-010636-delegation-quality-assurance-scope
  - type: references
    target: HYP-20260812-010725-progressive-automation-contracts
  - type: references
    target: OBS-20260802-230427-process-flow-and-outcome-quality
---

# 観察

## 知識の成立根拠

`RN-20260805-211320-ai-slop-design-layers`に保存された、人間とGenAIの対話で形成した
設計整理を`recorded_statement`として抽出した。AI Slopの原因候補、設計の向きおよび
検証粒度を四つのLayerへ接続する部分は`reasoned_synthesis`である。

確立済みArchitecture、標準Test Strategy、実在Systemの障害分類または比較結果ではない。

## 根拠箇所

- 同Raw Noteの「AI Slopの問題層」
- 同Raw Noteの「二つに絞るのではなく、構造を示す」
- 同Raw Noteの「設計、実装、検証の向き」
- 同Raw Noteの「検証方法もLayerで異なる」

## 根拠から直接言えること

記録では、AI Slopとして経験される状態の原因候補を、少なくとも次の四層へ分けている。

| Layer | 記録された主な不足候補 |
| --- | --- |
| AI Building Block | 生成、探索、解釈、分類、評価または根拠追跡の品質 |
| Automation Design | Contract、状態遷移、停止、再試行、Evaluator、Human FallbackまたはContext伝播 |
| Feature Design | 利用者が行えること、操作、Feedback、例外時の挙動および仕事を前へ進める能力 |
| Service Design | 対象者、Value Stream、運営責任、利用条件、Support、CostおよびOutcome |

設計は利用者・組織のNeedからService、Feature、Automation、Building Blockへ下り、
実装CapabilityはBuilding Blockから上位へ積み上がるという二つの向きが記録されている。
また、Building BlockとAutomationが技術的に成立しても、Featureが利用者の仕事に合い、
Serviceが組織Outcomeへ寄与するかは別に確認する必要があると整理されている。

検証候補も、Building Blockの評価、Automationの接続・制御確認、FeatureのScenario・User Test、
Serviceの実運用・Outcome確認という異なる粒度へ対応づけられている。

## 既存Analysisとの関係

`OBS-20260827-010636-delegation-quality-assurance-scope`は、Task、Workflow、Loop、Graphへ
Delegation範囲が広がる時の品質保証範囲を扱う。本Observationは、同じ成熟段階ではなく、
AIを含むServiceを構成する設計Layerの違いを扱う。

`OBS-20260802-230427-process-flow-and-outcome-quality`が分けるFlowとOutcome Qualityに対し、
本Observationは品質不足が生じ得る設計対象を四層へ分解する候補である。

## 曖昧さと限界

- 四層構造を外部の標準Architectureまたは実証研究へ照合していない。
- 問題が一つのLayerへ排他的に属するとは確認しておらず、複数Layerにまたがり得る。
- Layer別の検証候補が十分または最適とは確認していない。
- Layerを分けることで診断、設計またはOutcomeが改善する因果は未検証である。
- このObservationはArchitecture、Test Strategyまたは登壇内容の採用を意味しない。

## 公開安全性確認

- checked_at: 2026-09-24T10:48:49+09:00
- checked_by: agent:codex
- result: `not_needed`
- scope:
  この分析ノードの本文、frontmatter、relationの組み合わせを、
  人間の意図Reviewを確定する時点で再確認した
- finding:
  顧客、案件、非公開の個人、商用条件、内部System、認証情報、再識別に
  つながる組み合わせは確認されず、本文の変更や削除は行っていない
- limitation:
  公開安全性の確認は、内容の正しさ、検証完了、採用を意味しない
