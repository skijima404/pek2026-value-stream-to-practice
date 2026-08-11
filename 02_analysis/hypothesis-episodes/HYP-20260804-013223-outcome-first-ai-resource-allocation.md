---
id: HYP-20260804-013223-outcome-first-ai-resource-allocation
type: hypothesis_episode
title: "Value Streamの課題とOutcomeからAI Capabilityを配置すると局所最適を避けやすい"
content_language: ja
created_at: 2026-08-04T01:32:23+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: superseded
reviewed_at: 2026-08-11T12:03:41+09:00
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
    target: RN-20260730-111926-value-stream-ai-outcomes
  - type: derived_from
    target: RN-20260731-214443-ai-resource-management-in-value-stream
  - type: derived_from
    target: OBS-20260809-203133-dvs-quality-first-ai-outcome-selection
  - type: derived_from
    target: OBS-20260809-203134-downstream-load-frequency-induced-work
  - type: derived_from
    target: OBS-20260811-003710-platform-flow-step-quality-priorities
  - type: derived_from
    target: OBS-20260811-113031-outcome-first-changed-platform-decision
  - type: derived_from
    target: OBS-20260811-115141-standard-path-replaced-platform-selection
  - type: derived_from
    target: OBS-20260811-115142-lightweight-analysis-cost-judgment
  - type: tests
    target: HYP-20260804-183210-ai-slop-downstream-burden-value
  - type: superseded_by
    target: HYP-20260811-131148-consumer-governed-ai-capability
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

加えて、`OBS-20260811-003710-platform-flow-step-quality-priorities`には、
Platform選定から環境入手までのBounded Value Streamについて、実践者へのFocused
InterviewでStep別の優先品質とSpeedとのCounterfactualを確認した結果が記録されている。
この結果はU2だけを確認したもので、AI配置方法の実装比較またはU3の経済妥当性には
基づかない。

`OBS-20260811-113031-outcome-first-changed-platform-decision`には、一つのModernize
基盤選定Caseについて、AIまたはSpeedから開始する場合と、Business Outcome、Decision
QualityおよびRiskから開始する場合を比較したFocused Interviewの結果が記録されている。
この結果はU1だけを現在の範囲で確認したもので、二つの方法を実装した比較ではない。

`OBS-20260811-115141-standard-path-replaced-platform-selection`には、小規模Applicationの
対照Caseで、個別基盤選定を標準Path、Service ScopeおよびAdmission Controlへ置き換えた
判断が記録されている。`OBS-20260811-115142-lightweight-analysis-cost-judgment`には、
重い分析を軽量Hypothesis Statementと現場観察・Fact Checkへ簡略化し、実践者個人の
感覚値である約16時間を数か月の誤投資Riskと比較した結果が記録されている。

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
| U1 | Value Streamの課題と期待Outcomeから始めると、Toolまたは生成Use Caseから始める場合とは異なるAI Capability、責任境界、観測項目または棄却判断を選べる | critical | OBS-20260811-113031-outcome-first-changed-platform-decision, OBS-20260811-115141-standard-path-replaced-platform-selection | checked_for_current_scope | supports | direct | 同じ一人の実践者による重いOne Way Doorと小規模Applicationの二つのWalkthroughである。二つの開始方法を実装せず、当時の資料、他のActor、判断後のOutcome、Routing結果および比較Costは未確認である |
| U2 | 同じValue Streamの中でも、対象箇所とContextによって、Speed、Coverage、Decision Quality、Reproducibilityなどの優先品質は異なり、Speedが一貫して最優先になるとは限らない | critical | OBS-20260811-003710-platform-flow-step-quality-priorities | checked_for_current_scope | supports | direct | 一人の実践者によるBounded Walkthroughで8 Step中3 Stepを確認した。一次資料、他のActor、実施頻度、全Stepおよび自動化済みProcessへの観点の包含は未確認である |
| U3 | 対象箇所ごとに優先品質とAI Outcomeを分けて配置する方が、Speedを一律に優先する場合より、局所便益、発生頻度、対象Resource、誘発作業、Error Costおよび下流負荷を含む全体の経済妥当性を高める | critical | none | not_checked | unknown | unknown | 同一Caseで二つの配置を比較しておらず、便益とCostの範囲、単位、対象期間、重複計上および実際のOutcomeを確認していない |
| U4 | Value Stream、優先品質、Capability、責任境界および観測を整理するCostは、得られる経済的な判断改善または回避できる局所最適と下流負荷に対して妥当である | high | OBS-20260811-115142-lightweight-analysis-cost-judgment | partially_checked | supports | direct | 小規模Applicationでは一枚程度のStatementと実働約16時間という実践者個人の感覚値を得たが、実測Cost、組織合意、複数Case、回避効果、標準維持Costおよび高Risk利用の分析Costは未確認である |

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
- 対象・資料:
  - U1:
    一つのModernize基盤選定Case。AIまたはSpeed起点と、Business Outcome、Decision
    QualityおよびRisk起点を比較した実践者へのFocused Interviewと
    `OBS-20260811-113031-outcome-first-changed-platform-decision`
  - U2:
    Responsibilityと確認観点を明示するため、人手の申請・承認が残る組織で、開発Teamが
    Platformを選定し開発環境を入手するまでの8 Step。実践者へのFocused Interviewと
    `OBS-20260811-003710-platform-flow-step-quality-priorities`
  - U4:
    小規模Applicationの標準Path Case。軽量Hypothesis Statement、現場観察、Fact Check、
    実践者個人の所要時間感覚および数か月の誤投資とのCounterfactualを確認したInterviewと
    `OBS-20260811-115142-lightweight-analysis-cost-judgment`
- 選定方法:
  U1は、Business Outcomeと技術選定の接続、One Way DoorおよびBusiness Stakeholderの
  承認を確認できる過去Caseと、小規模Applicationの標準Pathという対照Caseを選んだ。
  U2は、前後のActorと期待Outcomeを限定でき、実践者が複数組織で利用を知る一般的なFlowから
  Step 1、Step 6、Step 7を選んだ。U4は、重い分析が過剰になり得る小規模Caseを選んだ
- 実施規模:
  同じ一人の実践者による三つのBounded Walkthrough。U1、U2およびU4の一部を現在の
  確認範囲とした

### GenAIの利用

- 利用内容:
  Value Stream上の課題、必要Capability、割り当てOption、暗黙の前提、反証候補を
  構造化する
- GenAIだけで実施しないこと:
  実際のOutcome、Capability、Accountability、採用または棄却を決定する
- 実際に確認した資料・記録:
  relationで示したRepository Nodeと、
  `RN-20260811-003709-platform-selection-step-quality-interview`に保存したFocused
  Interview、および
  `RN-20260811-113030-modernization-platform-decision-walkthrough`に保存したFocused
  Interview、および
  `RN-20260811-115140-small-application-standard-path-walkthrough`に保存したFocused
  Interview。Agentは質問の構造化、Counterfactualの提示および回答整理を行った

## 結果

`inconclusive`

### 実際に観測したこと

U1について、一つのModernize基盤選定Caseでは、将来拡張性と上位のBusiness課題が
語られた一方、Business Goal、Architecture Visionおよび基盤選定の因果は実践者には
見えなかった。実際の選定では運用能力、既存Skill、扱いきれること、および責任を
引き受けられることが重視され、仮想Machine基盤の選択がApplicationを粗い粒度へ制約した。

AIまたはSpeed起点ではTeamの不安に反応して選定を速める可能性があるが、Business Goalへの
適合性を解決しないと評価された。Outcome起点では、Business Outcome優先時の選定保留、
期限制約優先時の暫定基盤と再検討計画、推奨案と対抗案のRisk比較、技術Roleの確認・署名、
Business StakeholderのResidual Risk受入が判断Optionと責任境界へ入った。この結果はU1を
現在の範囲で支持する。

U1の対照となる小規模Application Caseでは、Application自体はTwo Way Doorだったが、
実装開始後のTeam持ち替えはOne Way Doorだった。部門標準が個別の基盤比較を不要にし、
標準で扱えない規模または重大なDataを扱うApplicationはService Scope外として断る
Admission Controlへ判断が変わった。現在はEnterprise情報のDigital化が制約されるため、
AIへ最終Routingを任せず、部門長が判断を保持した。この結果もU1を現在の範囲で支持する。

Platform選定から環境入手までの同じBounded Value Streamで、Step 1では主要候補の
Coverage、Step 6では将来の障害と運用を見越したDecision Quality、Step 7では
Tech Leadにとって利用開始に必要な一式のCompleteness、Platform Teamにとって管理・
監査のTraceabilityが優先された。Step 6は典型的なOne Way Door、Step 7は手順が
固まったITSMのService Catalog Itemとして区別された。

通常約1時間で得られる候補Listを10倍速くする代わりに主要候補を漏らす方法、Platformを
数日早く決める代わりに障害要因または運用設計を見落とす方法、承認を速くする代わりに
利用要素または管理記録を欠く方法は、いずれも採用しないと回答された。

Step 7について、実践者自身が参加した過去Caseでは、分割された申請の存在を知らず
再申請が連鎖し、実践者の作業開始が約2か月遅れた。ただし、当時の申請Ticketまたは
Project日程はRepositoryで確認していない。

この結果はU2を現在の範囲で支持する。

U4について、小規模Applicationでは重いArchitecture Visionまたは詳細Risk比較を過剰とし、
一枚程度の軽量Hypothesis Statement、現場観察およびFact Checkへ簡略化する候補が得られた。
実践者個人の感覚値では実働約16時間で、誤ったTeamまたはValue Hypothesisへ数か月投資する
Riskを下げられるなら妥当と判断された。実Costと回避効果は未確認のため、U4は
`partially_checked`とする。

U1とU2を現在の範囲で支持し、U4を部分的に確認した一方、U3とU4の実測は未解決のため、
Episode全体の結果を`inconclusive`とする。

## 解釈

このEpisodeが置く因果は、AIを利用するかではなく、Value Stream内で一律にSpeedを
優先せず、対象箇所の期待Outcomeと優先品質からCapabilityを配置することが、全体の
経済妥当性を高め、局所最適の回避に寄与するという点である。

ここでいう経済妥当性は金額換算だけを意味しない。局所的な時間短縮と品質・判断・
探索範囲の便益に対し、AI活用と分析のCost、発生頻度、対象Resource、誘発作業、
Error Costおよび下流負荷を、対象Caseで比較可能な範囲に限定して扱う。

今回の結果から直接言えるのは、確認した3 Stepで優先品質をActor、Outcome、時間制約、
Error Costおよび下流作業から区別でき、SpeedとのCounterfactualでも優先順位が維持された
ことまでである。Feature Hypothesisで確認したCapability選択またはAI棄却の結果を、
このSolutionのU1、U3またはU4へ推移させない。

U1で確認した判断差は、AI利用を増やすことではなく、上位Outcomeとの接続が不足する場合に
Architecture Vision形成、OptionとRiskの比較、選定保留または暫定化、およびResidual Risk
受入の責任境界を選ぶことだった。Counterfactual Walkthroughの結果であり、実装効果または
経済妥当性を示さない。

小規模Applicationの対照Caseでは、Outcome起点が個別選定を増やすのではなく、標準Pathへ
選定を前倒しし、Application単位ではService ScopeとAdmission Controlだけを軽量に確認する
形になった。分析の深さはApplicationの可逆性だけでなく、Team割り振りの可逆性、標準の
存在およびRisk境界に応じて変える必要がある。

## 置換

- decided_at: 2026-08-11T13:57:54+09:00
- decided_by: human:kijima
- replacement:
  `HYP-20260811-131148-consumer-governed-ai-capability`
- scope:
  今後検証するPractice Solution Hypothesisの中心表現と比較対象
- reason:
  通常のApplication開発を表す比較対象として「Speedを一律に優先する場合」は不自然であり、
  業務後のConcernを受入条件として満たした実現案の中でSpeed、CostおよびFlowを最適化する
  形へ中心仮説を改めた。さらに、AIを消費側Value Streamから利用される提供側Capabilityと
  位置づけ、提供側の論理が消費側のOutcomeを上書きしない境界を新Episodeで検証する
- preservation:
  このEpisodeのU1、U2およびU4のCoverage、Finding、Applicability、Evidence、
  `result: inconclusive`、知識の成立根拠およびFeature Hypothesisとの関係は、過去の
  学習履歴として維持する。新EpisodeへEvidenceまたはFindingを転用しない

## 限界

- 「局所最適を避けた」と判断する観測候補は、前後の品質、発生頻度、対象Resource、
  誘発作業および下流Guardrailとして具体化したが、単位、閾値、重複計上の防止および
  判断への利用方法は未定義である。
- AI以外のProcess変更、組織設計、利用者Skillの影響を分離する必要がある。
- 小規模なAI利用では、詳細なResource Allocationが過剰になる可能性がある。
- この仮説は登壇内容、組織標準またはArtifactとして採用されたものではない。
- 今回のU2確認は一人の実践者による一般化されたFlowと一つの過去事例に基づき、一次資料、
  他のActor、8 Stepすべて、および自動化されたProcessが同じResponsibilityと確認観点を
  包含するかを確認していない。
- 品質優先による実際の障害削減、総Lead Time、総便益または総Costを測定していないため、
  U3の経済妥当性を支持しない。
- One Way Doorの具体的な可逆性基準と、Service Catalog Itemで許容される実行差分は
  定義していない。
- U1は一人の実践者による一つの過去CaseとCounterfactualに基づき、当時のArchitecture、
  Risk比較、承認資料、他の関係者、実装比較または判断後のOutcomeを確認していない。
- Partnerへの不安と基盤選定の因果、および当時のGovernance構造には実践者の推測を含む。
- 小規模Application CaseのRoutingは伝聞で、部門資料、関係者本人、受付結果、標準Pathの
  成功率または実Outcomeを確認していない。
- 約16時間は実践者個人の感覚値で、組織の実測、合意、標準または複数Caseの分布ではない。
- 標準構成の作成・維持CostをApplication単位の分析Costへ含めていない。

## 公開安全性確認

- checked_at: 2026-08-11T13:57:54+09:00
- checked_by: agent:codex
- result: `sanitized`
- scope:
  この分析ノードの本文、frontmatter、relationの組み合わせを、
  後継Solution Hypothesisとの置換関係を記録する時点で再確認した
- finding:
  公開対象に不要な識別情報をCategory単位で削除または一般化し、削除値は
  Repository、訂正履歴、Filename、Logへ保存していない
- limitation:
  公開安全性の確認は、内容の正しさ、検証完了、採用を意味しない
