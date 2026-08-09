---
id: HYP-20260804-013223-outcome-first-ai-resource-allocation
type: hypothesis_episode
title: "Value Streamの課題とOutcomeからAI Capabilityを配置すると局所最適を避けやすい"
content_language: ja
created_at: 2026-08-04T01:32:23+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-09T21:21:34+09:00
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
  - type: derived_from
    target: OBS-20260809-203133-dvs-quality-first-ai-outcome-selection
  - type: derived_from
    target: OBS-20260809-203134-downstream-load-frequency-induced-work
  - type: tests
    target: HYP-20260804-183210-ai-slop-downstream-burden-value
---

# 仮説

AIの生成Use CaseまたはTool選定から始める代わりに、Value Stream上の課題と
期待Outcomeを先に特定し、対象箇所によってSpeed、Coverage、Decision Quality、
Reproducibilityなどの優先品質が異なることを踏まえて、必要なCapability、Boundary、
Context、AccountabilityをHuman、AI、Platformへ割り当てれば、Process Timeだけを
一律に優先する場合より、Value Stream全体の経済妥当性、Flow、品質および判断責任に
適合したAI活用を選びやすい。

## 知識の成立根拠

`RN-20260730-111926-value-stream-ai-outcomes`に記録された、Process Time、Lead Time、
手戻りなどの課題から狙うOutcomeを考える発言と、
`RN-20260731-214443-ai-resource-management-in-value-stream`に整理された
Capabilityと責任境界の推論を組み合わせた。

`OBS-20260809-203133-dvs-quality-first-ai-outcome-selection`には、DVS上の対象箇所、
必要品質、AI Outcome、機能および観測という設計順序が記録されている。
`OBS-20260809-203134-downstream-load-frequency-induced-work`には、局所的な処理時間に
加えて、発生回数、対象Resourceおよび誘発作業から下流負荷を評価する候補が
記録されている。これらは仮説と検証方法を具体化する設計根拠であり、AI配置方法を
比較した検証Evidenceではない。

この仮説は記録された考えと推論に基づくが、AI配置方法を比較した実地検証には
基づかない。

## Mobiusでの位置づけ

`solution`

親となるValue Hypothesis
`HYP-20260804-183210-ai-slop-downstream-burden-value`に対して、何を作るかの選択と
価値検証を、Value Streamから必要Capabilityを割り当てる方法として具体化する。

## 期待する兆候

- AI導入目的が、生成量ではなく対象Stepの課題と期待Outcomeへ接続される
- 対象箇所ごとにSpeed、Coverage、Decision Quality、Reproducibilityなどの
  優先順位が異なることを説明できる
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
- 対象箇所ごとに優先品質を分けても、局所的なSpeedを一律に優先する場合より
  総便益、総Costまたは判断が改善しない

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | Value Streamの課題と期待Outcomeから始めると、Toolまたは生成Use Caseから始める場合とは異なるAI Capability、責任境界、観測項目または棄却判断を選べる | critical | none | not_checked | unknown | unknown | 同一の改善候補について、二つの開始方法から得られる選択と判断を比較していない |
| U2 | 同じValue Streamの中でも、対象箇所とContextによって、Speed、Coverage、Decision Quality、Reproducibilityなどの優先品質は異なり、Speedが一貫して最優先になるとは限らない | critical | none | not_checked | unknown | unknown | 優先品質の候補は会話から整理されたが、実在するValue Streamの複数箇所について、Actor、Error Cost、頻度、時間制約および期待Outcomeから優先順位を確認していない |
| U3 | 対象箇所ごとに優先品質とAI Outcomeを分けて配置する方が、Speedを一律に優先する場合より、局所便益、発生頻度、対象Resource、誘発作業、Error Costおよび下流負荷を含む全体の経済妥当性を高める | critical | none | not_checked | unknown | unknown | 同一Caseで二つの配置を比較しておらず、便益とCostの範囲、単位、対象期間、重複計上および実際のOutcomeを確認していない |
| U4 | Value Stream、優先品質、Capability、責任境界および観測を整理するCostは、得られる経済的な判断改善または回避できる局所最適と下流負荷に対して妥当である | high | none | not_checked | unknown | unknown | 小規模利用と高Risk利用の適用境界、所要時間、必要Skillおよび簡略化条件を確認していない |

## 検証方法

### 方法と対象範囲

- 方法:
  - 同じValue Streamの複数箇所について、Actor、期待Outcome、時間制約、頻度、
    Error Costおよび下流影響を確認し、Speed、Coverage、Decision Quality、
    Reproducibilityなどの優先順位が異なるかを整理する
  - 同一の小さな改善候補について、AI Use CaseまたはSpeedから開始する配置と、
    Value Stream上の対象箇所、期待Outcomeおよび優先品質から開始する配置を作る
  - 二つの配置から得られるCapability、責任境界、観測項目、棄却判断、局所便益、
    発生頻度、対象Resource、誘発された手戻り・待ち・再作業、Error Cost、
    下流Guardrailおよび分析Costを比較する
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
配置する整理に加え、対象箇所によってSpeed、Coverage、Decision Quality、
Reproducibilityなどの優先品質が異なり得るという設計案と、下流負荷の評価候補は
Repositoryに記録されている。これらは会話から形成した設計案の記録であり、実在する
Value Streamの複数箇所における優先順位、または二つの配置の経済妥当性を比較した
記録ではない。

## 解釈

このEpisodeが置く因果は、AIを利用するかではなく、Value Stream内で一律にSpeedを
優先せず、対象箇所の期待Outcomeと優先品質からCapabilityを配置することが、全体の
経済妥当性を高め、局所最適の回避に寄与するという点である。

ここでいう経済妥当性は金額換算だけを意味しない。局所的な時間短縮と品質・判断・
探索範囲の便益に対し、AI活用と分析のCost、発生頻度、対象Resource、誘発作業、
Error Costおよび下流負荷を、対象Caseで比較可能な範囲に限定して扱う。

## 限界

- 「局所最適を避けた」と判断する観測候補は、前後の品質、発生頻度、対象Resource、
  誘発作業および下流Guardrailとして具体化したが、単位、閾値、重複計上の防止および
  判断への利用方法は未定義である。
- AI以外のProcess変更、組織設計、利用者Skillの影響を分離する必要がある。
- 小規模なAI利用では、詳細なResource Allocationが過剰になる可能性がある。
- この仮説は登壇内容、組織標準またはArtifactとして採用されたものではない。

## 公開安全性確認

- checked_at: 2026-08-09T21:21:34+09:00
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
