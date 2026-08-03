---
id: HYP-20260804-013223-outcome-first-ai-resource-allocation
type: hypothesis_episode
title: "Value Streamの課題とOutcomeからAI Capabilityを配置すると局所最適を避けやすい"
content_language: ja
created_at: 2026-08-04T01:32:23+09:00
created_by: agent:codex
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-04T01:53:22+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260730-111926-value-stream-ai-outcomes
  - type: derived_from
    target: RN-20260731-214443-ai-resource-management-in-value-stream
  - type: tests
    target: HYP-20260730-015718-ai-speed-requires-value-validation
---

# 仮説

AIの生成Use CaseまたはTool選定から始める代わりに、Value Stream上の課題と
期待Outcomeを先に特定し、必要なCapability、Boundary、Context、Accountabilityを
Human、AI、Platformへ割り当てれば、Process Timeだけを局所的に短縮する場合より、
Value Stream全体のFlow、品質、判断責任に適合したAI活用を選びやすい。

## 知識の成立根拠

`RN-20260730-111926-value-stream-ai-outcomes`に記録された、Process Time、Lead Time、
手戻りなどの課題から狙うOutcomeを考える発言と、
`RN-20260731-214443-ai-resource-management-in-value-stream`に整理された
Capabilityと責任境界の推論を組み合わせた。

この仮説は記録された考えと推論に基づくが、AI配置方法を比較した実地検証には
基づかない。

## Mobiusでの位置づけ

`solution`

親となるValue Hypothesis
`HYP-20260730-015718-ai-speed-requires-value-validation`に対して、何を作るかの選択と
価値検証を、Value Streamから必要Capabilityを割り当てる方法として具体化する。

## 期待する兆候

- AI導入目的が、生成量ではなく対象Stepの課題と期待Outcomeへ接続される
- AIが速くしたStepだけでなく、前後の待ち、手戻り、判断、品質への影響を
  事前に確認できる
- AIへ任せるTaskと、人間または組織が引き受ける判断責任が明確になる
- 生成以外の探索、比較、反証、評価基準作成も選択肢として比較される
- 期待Outcomeに寄与しないAI Use Caseを、実装または拡大前に保留・棄却できる

## 反証またはChallengeとなる兆候

- Value Streamから始めても、Toolまたは生成Use Caseから始めた場合より選択が
  改善しない
- 分析と責任設計のCostが大きく、小さなAI利用の価値を上回る
- CapabilityがModel、Context、運用条件で変動し、事前の割り当てが維持できない
- Outcomeを定義しても、AI配置と観測結果の因果を識別できない

## 検証方法

### 方法と対象範囲

- 方法:
  同程度の小さな改善候補について、AI Use Caseから開始する整理と、Value Streamの
  課題・Outcome・Capabilityから開始する整理を作り、候補、前提、責任境界、観測項目、
  棄却判断の違いを比較する
- 対象・資料: 未選定
- 選定方法:
  前後のActorと期待Outcomeを限定できる一つの業務またはPlatform Serviceを選ぶ
- 実施規模:
  一つの改善候補について小規模なWalkthroughまたはExpert Reviewから始める

### GenAIの利用

- 利用内容:
  Value Stream上の課題、必要Capability、割り当てOption、暗黙の前提、反証候補を
  構造化する
- GenAIだけで実施しないこと:
  実際のOutcome、Capability、Accountability、採用または棄却を決定する
- 実際に確認した資料・記録:
  現時点ではrelationで示したRepository Nodeのみ

## 結果

`not_tested`

### 実際に観測したこと

Value Streamの課題からAI Outcomeを考える発言と、AIをCapabilityと責任境界で
配置する整理はRepositoryに記録されている。二つの開始方法を同一条件で比較した
記録はない。

## 解釈

このEpisodeが置く因果は、AIを利用するかではなく、Value Stream上で必要な
OutcomeとCapabilityから配置を決めることが局所最適の回避に寄与するという点である。

## 限界

- 「局所最適を避けた」と判断するMetricは未定義である。
- AI以外のProcess変更、組織設計、利用者Skillの影響を分離する必要がある。
- 小規模なAI利用では、詳細なResource Allocationが過剰になる可能性がある。
- この仮説は登壇内容、組織標準またはArtifactとして採用されたものではない。

## 公開安全性確認

- checked_at: 2026-08-04T01:53:22+09:00
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
