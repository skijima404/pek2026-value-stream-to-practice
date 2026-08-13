---
id: HYP-20260812-010725-progressive-automation-contracts
type: hypothesis_episode
title: "Building Blockを個別検証してから接続すると未解決の誤りと曖昧さの伝播を抑えられる"
content_language: ja
created_at: 2026-08-12T01:07:25+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: feature
status: reviewed
reviewed_at: 2026-08-12T01:22:34+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - case_recollection
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260812-010724-contract-first-progressive-automation-practice
  - type: derived_from
    target: RN-20260805-094034-ai-building-block-automation-maturity
  - type: tests
    target: HYP-20260801-004823-service-contract-reduces-downstream-cost
  - type: references
    target: HYP-20260811-131148-consumer-governed-ai-capability
---

# 仮説

AI-enabled Solutionを最初からEnd-to-EndのWorkflow、LoopまたはGraphとして接続する代わりに、
まず人間が対象業務の手順、判断、状態遷移および完了条件を確認し、AI Building Blockごとに
Input、Output、失敗条件、Evaluator、Human Reviewおよび次工程へ渡すContractを検証してから、
安定した範囲だけを段階的に接続すれば、未解決の誤り、曖昧さおよび検証責任が後続Blockや
Actorへ伝播することを抑えられる。

## 知識の成立根拠

`OBS-20260812-010724-contract-first-progressive-automation-practice`には、Contract Firstと
段階的自動化を用いた環境構築およびDemoが複数回反復されたという
`recorded_statement`、`practitioner_experience`および`case_recollection`が記録されている。

`RN-20260805-094034-ai-building-block-automation-maturity`には、Manual Operation、Task
Automation、Workflow、Loop、Graphという成熟順序、Human in the Loopを失敗条件と
Evaluatorを発見する観測点として使う設計、およびBuilding Block OutcomeとSolution Outcomeを
分ける整理が記録されている。これは会話上の設計整理を含む`reasoned_synthesis`であり、
既存Frameworkによる保証または比較実験の結果ではない。

## Mobiusでの位置づけ

`practice` scopeの`feature`

`HYP-20260801-004823-service-contract-reduces-downstream-cost`が置く、共有前に対象、前提、
受入条件、保証範囲、責任境界および例外時の戻し先を明らかにするSolutionを、Automation内部の
Building Block間Contractと段階的接続によって試すFeature Hypothesisである。

`HYP-20260811-131148-consumer-governed-ai-capability`は、消費側Value StreamのConcernと
受入条件からAI利用条件を決める近接Solutionとして参照する。二つのSolutionを同時に親として
検証せず、`tests`の直接親はService Contract Solutionだけに限定する。

## 検証

- アプローチ: `experiment`
- 学習したい問い:
  同じ小さなAI-enabled Workflowについて、Building BlockとContractを個別確認してから
  接続する方法は、最初から接続した方法より、後続へ到達する不適合Output、差し戻し、
  再実行および人間の再構築作業を減らすか
- 前へ進むSignal:
  個別確認した方法で、次工程の受入条件を満たさないOutputの流入、差し戻し、再実行または
  人間の再構築時間の少なくとも一つが減り、追加した確認Costを含むEnd-to-Endの負荷が
  悪化しない
- 実施内容と範囲:
  未実施。可逆で小さく、同じInput群と受入条件を使える2〜3個のBuilding Blockからなる
  Workflowを選び、接続前後の結果を比較する
- 実際に確認した資料・人・記録:
  現時点ではrelationで示したObservationとRaw Noteのみ。過去のDemo実行Logまたは
  比較可能なWorkflow記録は確認していない
- GenAIの利用:
  Building Block候補、Contract、失敗条件、Evaluator、観測項目および反証条件の構造化に
  利用する。受入条件、許容Risk、合否および次工程へ渡す判断はGenAIだけで決定しない

## 結果

`not_tested`

## 学び

検証計画を形成した段階であり、比較結果はまだない。既存の反復実践は候補方法が運用された
ことを示すが、End-to-End先行との比較または下流負荷削減を示さない。

## 解釈

このFeatureは、Workflow、LoopまたはGraph自体を問題としない。Building Blockの正しさ、
受け渡し条件および評価方法が分からない段階で接続を先行すると、局所的な生成速度を
End-to-EndのOutcomeと誤認し、未解決の誤りを高速に伝播させる可能性を検証対象とする。

Human in the Loopは恒久的に全件承認することを目的にせず、失敗しやすいInput、判断基準、
停止条件およびRule化できる検査を発見し、安定した範囲をEvaluatorまたはAutomationへ
移す学習Phaseとして扱う。

## 限界と残存不確実性

- 選定上の偏り:
  小さく可逆なWorkflowでは段階的確認が有利でも、高頻度かつ既知の標準Processや既に成熟した
  Vendor Presetでは追加Costが便益を上回る可能性がある
- 未確認の証拠:
  同一Inputによる比較、失敗判定、差し戻し、再実行、人間の再構築時間、全体Lead Time、
  実装・維持Costおよび利用後Outcomeを確認していない
- 一般化できない範囲:
  過去のDemo反復から、複雑なAgent、Production Workflow、高Risk判断または他組織での
  因果効果を推定しない

## 次の判断

- 判断: `not_decided`
- 判断の対象範囲:
  小さなAI-enabled Workflowで、段階的接続をPractice Featureとして試すか
- 次に進めること:
  比較可能な2〜3 Building BlockのWorkflow、受入条件、失敗判定および観測可能な下流作業を
  一つ選ぶ

## 公開安全性確認

- checked_at: 2026-08-12T01:22:34+09:00
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
