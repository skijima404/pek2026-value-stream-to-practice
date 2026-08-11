---
id: HYP-20260809-203135-quality-first-ai-allocation-workflow
type: hypothesis_episode
title: "対象箇所・必要品質・AI Outcome・Capability・観測の順で設計すると局所速度偏重を避けやすい"
content_language: ja
created_at: 2026-08-09T20:31:35+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: feature
status: reviewed
reviewed_at: 2026-08-11T01:18:44+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - case_recollection
  - explicit_validation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260809-203133-dvs-quality-first-ai-outcome-selection
  - type: derived_from
    target: OBS-20260809-203134-downstream-load-frequency-induced-work
  - type: derived_from
    target: OBS-20260811-003710-platform-flow-step-quality-priorities
  - type: derived_from
    target: OBS-20260811-003711-quality-first-changed-ai-allocation
  - type: tests
    target: HYP-20260804-013223-outcome-first-ai-resource-allocation
---

# 仮説

AIの生成Use CaseまたはToolを先に選ぶ代わりに、DVS上の対象箇所、その場所で
成立させたい品質、AIへ期待するOutcome、必要なCapabilityと責任境界、直接効果と
下流影響の観測方法の順で設計すれば、Process Timeの局所的な短縮だけに偏らず、
対象箇所に必要なAI活用とGuardrailを選びやすくなる。

## 知識の成立根拠

`OBS-20260809-203133-dvs-quality-first-ai-outcome-selection`には、DVS上の対象箇所と
必要品質からAI Outcome、機能、観測へ進む順序が、人間とGenAIの会話で形成した
設計案として記録されている。

`OBS-20260809-203134-downstream-load-frequency-induced-work`には、局所的な処理時間だけで
なく、発生回数、対象Resource、誘発された手戻り、待ちおよび再作業を観測する候補が
記録されている。

これらはFeatureとして利用できる設計順序を検討する根拠である。加えて、
`OBS-20260811-003710-platform-flow-step-quality-priorities`と
`OBS-20260811-003711-quality-first-changed-ai-allocation`には、Platform選定から
環境入手までのBounded FlowでStep別品質を定義し、Speed起点と品質起点のCapability、
責任境界、GuardrailおよびAI棄却判断をFocused Interviewで比較した結果が記録されている。
これは一人のWalkthroughであり、二つの順序を実装して比較したものではない。

## Mobiusでの位置づけ

`practice` scopeの`feature`

既存のPractice Solution Hypothesis
`HYP-20260804-013223-outcome-first-ai-resource-allocation`に対し、Value Stream上の課題と
OutcomeからAI Capabilityを配置するための具体的な作業順序を置くFeature Hypothesisである。

## 期待する兆候

- ToolまたはAI Use Caseを固定する前に、対象Actor、DVS上の対象箇所、期待Valueおよび
  成立させたい品質を説明できる
- 同じ改善候補でも、Use Case先行の場合とは異なる探索、解釈、比較、反証または生成の
  AI Outcomeが選択肢へ入る
- 必要Capabilityだけでなく、人間または組織が保持する判断、Accountabilityおよび
  Closure条件が明示される
- 局所的なPTまたはLTに加えて、前後の待ち、発生頻度、対象Resource、手戻り、品質および
  下流Guardrailが観測候補へ入る
- 期待Outcomeへ寄与しない、または下流負荷を増やすAI Use Caseを実装前に保留、修正または
  棄却できる

## 反証またはChallengeとなる兆候

- この順序を使っても、Use CaseまたはToolから始める場合と、候補、前提、責任境界、
  観測項目または判断が変わらない
- 対象箇所の品質を事前に定義できず、結局は選んだToolのMetricを後付けする
- 分析項目が増えるだけで、継続、修正、保留、棄却または追加確認の判断を更新できない
- 小さなAI利用に対する分析、記録および調整Costが、回避可能な負荷または学習価値を上回る
- 品質起点で選んだAI Outcomeでも、対象箇所の品質または下流負荷が改善しない

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | Tool選定前に、DVS上の対象箇所と成立させたい品質を、実務で判断可能な粒度に定義できる | high | OBS-20260811-003710-platform-flow-step-quality-priorities | checked_for_current_scope | supports | direct | 一人の実践者によるBounded Walkthroughで8 Step中3 Stepを確認した。全Step、他のActor、実測閾値および自動化仕様への観点の反映は未確認である |
| U2 | 品質からAI Outcomeを選ぶと、生成Use Case先行とは異なるCapability、責任境界または棄却判断が得られる | critical | OBS-20260811-003711-quality-first-changed-ai-allocation | checked_for_current_scope | supports | direct | 一人のWalkthroughで判断差を確認したが、二つの開始方法を実装・運用して比較せず、AIの再現性試験とCapability条件も未定義である |
| U3 | 観測方法を最後に接続すると、局所速度だけでなく頻度、誘発作業、品質および下流Guardrailを事前に選べる | critical | none | not_checked | unknown | unknown | 観測項目の選択差、実際のData取得可能性、重複計上および判断への利用を確認していない |
| U4 | この設計順序の分析、記録および調整Costは、回避可能な局所最適または下流負荷に対して妥当である | high | none | not_checked | unknown | unknown | 小規模利用と高Risk利用の適用境界、所要時間、必要Skillおよび簡略化条件を確認していない |

## 検証方法

### 方法と対象範囲

- 方法:
  前後のActorと期待Outcomeを限定できる一つの小さな改善候補について、AI Use Caseまたは
  Toolから開始する整理と、対象箇所、必要品質、AI Outcome、Capability、観測から開始する
  整理を作る。候補、前提、責任境界、観測項目、保留・棄却判断および分析Costの違いを
  WalkthroughまたはExpert Reviewで比較する。
- 対象・資料:
  Responsibilityと確認観点を明示するため、人手の申請・承認が残る組織で、開発Teamが
  Platformを選定し開発環境を入手するまでの8 Step。実践者へのFocused Interview、
  `OBS-20260811-003710-platform-flow-step-quality-priorities`および
  `OBS-20260811-003711-quality-first-changed-ai-allocation`
- 選定方法:
  生成速度だけでは十分性を判定できず、前後のActorまたは下流Quality Guardrailを
  一つ以上確認できる候補として、Step 1、Step 6、Step 7を選んだ。
- 実施規模:
  一人の実践者による一つのBounded Walkthrough。U1とU2だけを今回の確認範囲とした。

### GenAIの利用

- 利用内容:
  二つの開始方法の整理、暗黙の前提、AI Outcome候補、責任境界、観測項目、反証条件および
  分析Costの比較を支援する。
- GenAIだけで実施しないこと:
  実際の対象品質、Capability、Accountability、Outcome、Costまたは採用・棄却判断を
  Sourceなしに補完する。
- 実際に確認した資料・記録:
  relationで示したObservation、既存Practice Solution Hypothesis、および
  `RN-20260811-003709-platform-selection-step-quality-interview`に保存したFocused
  Interview。Agentは質問の構造化、Counterfactualの提示および回答整理を行った。

## 結果

`inconclusive`

### 実際に観測したこと

Platform選定から環境入手までのBounded Flowで、Step 1はCoverage、Step 6はDecision
Quality、Step 7はCompletenessとTraceabilityとして、Actorと下流影響から実務上の
完了状態を定義できた。この結果はU1を現在の範囲で支持する。

Step 7を一律に速くするCapabilityとして、実践者はAIよりAnsibleまたはTerraformのような
決定的自動化を選んだ。品質起点では、Ticket Systemによる申請・承認の統合を優先し、AIを
不足Check、混在する承認結果からのScope確定、および条件付きPlaybook起動へ限定した。
Step 7は手順が固まったITSMのService Catalog Itemであり、非決定論的な事象が問題になる
ため、AIをDefaultの実行主体としない判断が示された。
高Risk、根拠不足、必要な承認またはCost確認が未完了の場合はAIへ任せず、統合機構が作れる
場合はAI利用自体を保留または棄却した。この結果はU2を現在の範囲で支持する。

U3の観測方法とU4の分析Costは今回確認していない。U1とU2を支持する一方、Feature全体の
因果は未解決のため、Episode全体の結果を`inconclusive`とする。

## 解釈

このEpisodeで新しく置いたのは、Outcome-first AI配置というSolutionを、対象箇所、
必要品質、AI Outcome、Capability、観測という作業順序で実行するFeatureと、その順序が
局所速度偏重の回避に寄与するという因果である。

Discover、Decide、Deliverと特定品質の対応、五つのAI Outcome分類、および下流負荷式を
確立済みの一般モデルとして扱わない。検証では、実Caseで定義できた項目と判断差だけを
限定的に確認する。

今回確認した判断差は、AI利用を増やすことではなく、品質とRiskからAIより適切なCapabilityを
選び、AIを使う場合も責任境界とGateを狭め、条件によってAI案を棄却することだった。
このFeatureの結果を親Solutionへ推移させず、親SolutionのU2は別Evidenceで判定する。

## 限界

- 選定上の偏り:
  人間とGenAIの会話から形成された設計案と、作成者が整理したAI Outcome候補を起点とする。
- 未確認の証拠:
  同一Caseでの開始方法比較、第三者による適用、実際の判断更新、下流負荷、Outcomeおよび
  分析Cost。
- 一般化できない範囲:
  すべてのDVS、AI Use Case、Risk水準または小規模な個人利用へ同じ手順が妥当とは
  結論できない。
- 残存リスクと影響を受ける判断:
  U1とU2は現在の範囲で確認したが、U3とU4、AI再現性の試験、実装比較および他のActorを
  確認するまで、このFeatureを標準Practice、登壇で推奨する手順、またはAI配置の十分条件と
  して扱えない。
- このEpisodeは、登壇内容、組織標準またはArtifactへの採用決定ではない。
- 今回の結果は一人の実践者によるWalkthroughであり、Ticket System統合、決定的自動化、
  AI Patchの実装・運用Costまたは実Outcomeを比較していない。
- AutomationによってResponsibilityが消えるとは扱わず、自動化されたProcessが同じ確認観点を
  包含する必要がある。ただし、その仕様または運用は今回確認していない。
- Service Catalog Itemで許容される実行差分と、AIを利用可能にする決定性の閾値は
  定義していない。

## 公開安全性確認

- checked_at: 2026-08-11T01:18:44+09:00
- checked_by: agent:codex
- result: `sanitized`
- scope:
  この分析ノードの本文、frontmatter、relationの組み合わせを、
  人間の意図Reviewを確定する時点で再確認した
- finding:
  公開対象に不要な識別情報をCategory単位で削除または一般化し、削除値は
  Repository、訂正履歴、Filename、Logへ保存していない
- limitation:
  公開安全性の確認は、内容の正しさ、検証完了、採用を意味しない
