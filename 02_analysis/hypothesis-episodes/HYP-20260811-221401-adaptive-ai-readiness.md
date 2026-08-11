---
id: HYP-20260811-221401-adaptive-ai-readiness
type: hypothesis_episode
title: "AI導入前にValue Streamを診断して観測網を置くと導入後の混乱へ早く対処しやすい"
content_language: ja
created_at: 2026-08-11T22:14:01+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-11T22:49:00+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - external_research
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260811-221400-ai-readiness-as-system-adaptation
  - type: derived_from
    target: OBS-20260811-224044-readiness-diagnosis-observation-net
  - type: tests
    target: HYP-20260804-183210-ai-slop-downstream-burden-value
  - type: references
    target: HYP-20260811-131148-consumer-governed-ai-capability
---

# 仮説

AI導入後の適応期間と混乱の大きさが導入前の組織状態によって変わるなら、対象Value Streamの
Actor、Process、Handover、Baseline、Verification Capacity、責任境界、Data and Knowledge
CurationおよびFeedback Loopを事前に診断し、負荷が現れそうな箇所へSignal、Trigger、Owner、
対処Optionという観測の「網」を置くことで、局所高速化が下流制約を露出させた時に、事後に
一から調査する場合より早く検知、判断および適応でき、混乱の期間と回避可能な下流負荷を
抑えやすい。

このEpisodeでいうReadinessは、組織の成熟度を測ること、すべての条件を導入前に完成させること、
または混乱をゼロにすることではない。問題が起きた時にどこを見て、誰が、どのOptionを判断するかを
準備することである。MBPMを、Actor間Handover、待ち、手戻りおよびProcess上の観測点を具体化する
方法として用いる。

## 知識の成立根拠

`OBS-20260811-221400-ai-readiness-as-system-adaptation`が抽出した、AIを既存の組織Systemの
増幅要因として捉える実践者の読み、End-to-End Verification Cost、Pipeline Adaptation、
Data and Knowledge Curation、Interaction進化およびSensingの整理から形成した。

`OBS-20260811-224044-readiness-diagnosis-observation-net`には、Readinessを測定自体ではなく、組織
状態によって長期化または拡大し得るAI導入後の混乱へ備える事前診断と観測網として扱い、その
具体化にMBPMを用いるという実践者の意図が記録されている。

この根拠は読書対話に記録された`recorded_statement`と、それを検証可能なReadinessへ構成した
`reasoned_synthesis`である。DataとKnowledge SystemのCuration、Domain-aligned API、Curated Data
EcosystemおよびData Meshに関する原文確認は
`EXT-20260811-223226-ai-data-knowledge-curation`として保存されているため、その範囲を
`external_research`として扱う。その他の外部主張は再確認しておらず、実際の組織診断、適応または
Outcome観測も行っていないため、`explicit_validation`として扱わない。

`HYP-20260811-131148-consumer-governed-ai-capability`は、消費側Value StreamのConcernから個々の
AI Capabilityの利用条件を決めるSolutionを扱う。本Episodeは、導入後の混乱を早期に検知して
対処するための事前診断と観測設計を扱う。同じ`practice` scopeの並行するSolutionであり、一方の
結果を他方へ推移させない。

## Mobiusでの位置づけ

`solution`

親となるPractice Value Hypothesis
`HYP-20260804-183210-ai-slop-downstream-burden-value`に対し、AI高速化による回避可能な下流負荷を
抑えるため、導入前のValue Stream診断と観測網によって、導入後に露出する制約への検知、判断、
適応を早めるSolution候補である。

## 期待する兆候

- AI導入前に、対象Outcome、Actor、Process、Handover、Process Time、Lead Time、待ち、手戻り、
  Verification Capacityおよび下流作業のBaselineが記録される
- MBPMまたは他の方法で、AIによってSpeedまたはVolumeが変わった時に負荷が現れそうなActor間
  Handoverと下流工程が特定される
- 観測箇所ごとに、Signal、対処を始めるTrigger、監視と判断のOwner、および利用範囲変更、Capacity
  追加、Pipeline変更、Guardrail、支援、保留または停止という対処Optionが事前に置かれる
- AI利用後にQueue、Waiting Time、Clarification、Correction、Backflow、`% Complete & Accurate`、
  End-to-End Verification CostまたはOutcome低下が早期に検知される
- 観測網がない場合と比べて、Time to Detect、Time to DecideまたはTime to Adaptが短くなる
- 早期対処によって、混乱が続く期間、手戻り、待ち、検証Costまたは下流負荷が小さくなる
- DataまたはKnowledge Systemが制約になるCaseでは、Serviceを管理するTeam、Domain-aligned API、
  Curated Data Ecosystem、Governanceおよび更新責任が観測と対処へ接続される
- 一つの制約への対処後に次の制約が露出した場合、同じ観測網を更新して次の判断へ接続する

## 反証またはChallengeとなる兆候

- 事前診断を行っても、導入後に負荷が現れる箇所または有効なSignalを特定できない
- 観測網を置いてもTime to Detect、Time to DecideまたはTime to Adaptが短くならない
- 早く検知しても実行可能な対処Option、CapacityまたはDecision Ownerがなく、混乱の期間と下流
  負荷が変わらない
- MBPM上の時間またはHandoverだけを見て、Business Outcome、最終成果物の品質、Data、Knowledge、
  Architecture Riskまたは人間の違和感を見落とす
- 事前診断と観測維持のCostが、混乱の早期対処による回避効果を上回る
- 組織状態が異なっても適応期間または混乱の大きさに差がなく、中心となる因果前提が成立しない

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | AI導入前の組織状態によって、導入後の適応期間または混乱の大きさが異なる | critical | none | not_checked | unknown | unknown | 組織状態、混乱、適応期間の操作的定義、比較可能なCaseおよびAI以外の影響を確認していない |
| U2 | 事前診断によって、AIによるSpeedまたはVolume変化で負荷が現れそうな箇所を特定し、Signal、Trigger、Ownerおよび対処Optionからなる観測網を置ける | critical | none | not_checked | unknown | unknown | 予測可能な制約の範囲、診断入力、観測粒度、TriggerおよびOwnerを確認していない |
| U3 | 事前に観測網があると、ない場合よりTime to Detect、Time to DecideまたはTime to Adaptが短くなり、混乱の期間または回避可能な下流負荷を減らせる | critical | none | not_checked | unknown | unknown | 比較可能なBaseline、導入記録、実際の対処、時間、総CostおよびOutcomeを確認していない |
| U4 | MBPMはActor、Process、Handover、PT、LT、待ち、手戻り、確認負荷および`% Complete & Accurate`を、観測網の設計と更新に使える粒度で表現できる | high | none | not_checked | unknown | unknown | 実Caseでの作成時間、Signal選定、更新可能性、およびMBPM外で補うべきOutcome、品質、Data、Knowledge、Architecture Riskを確認していない |
| U5 | 事前診断と観測網の作成・維持Costは、対象の規模、可逆性、Error Costおよび反復量に対して比例的であり、早期対処による回避効果を下回る | high | none | not_checked | unknown | unknown | 小さく可逆な利用と高Riskまたは大量反復する利用を比較しておらず、診断Cost、観測維持Costおよび回避効果を確認していない |

## 検証方法

### 方法と対象範囲

- 方法:
  - 一つのBoundedなAI利用候補についてCurrent State MBPMを作り、対象Outcome、Actor、Process、
    Handover、PT、LT、待ち、手戻り、確認負荷、反復量および下流作業をBaselineとして記録する
  - AIによってSpeedまたはVolumeが変わる箇所と、その直後のHandoverまたは下流工程を選び、Signal、
    Trigger、Ownerおよび実行可能な対処Optionを事前に置く
  - 利用後に実際に露出した制約、Time to Detect、Time to Decide、Time to Adapt、対処内容、待ち、
    手戻り、Verification Cost、`% Complete & Accurate`およびOutcomeを記録する
  - 可能であれば、観測網を事前に置いたCaseと、事後に調査を始めた類似Caseを比較する。比較が
    できない場合は、Counterfactualを事実とせず、単一Caseの検知・判断経路だけを記録する
  - MBPMで観測しにくいBusiness Outcome、最終成果物品質、Data and Knowledge Curation、
    Architecture Riskまたは人間の違和感に、別のSignalが必要か確認する
- 対象・資料:
  未選定。導入前Baselineと、導入後に露出した制約、検知、判断および対処を同じ変更として追跡
  できるCaseを優先する
- 選定方法:
  最初は可逆な一つのAI利用候補を選び、高Risk Caseまたは全社Readinessへ一般化する前に、観測網が
  実際の検知と対処を早めるか確認する
- 実施規模:
  一つから二つのBounded Case。成熟度Modelの完成ではなく、検知・判断・適応時間とMBPMの実用性を
  優先する

### GenAIの利用

- 利用内容:
  Current State MBPM、Signal、Trigger、Owner、対処Option、比較案および観測項目の構造化
- GenAIだけで実施しないこと:
  Business Outcome、Residual Risk、Trigger発火後の対処、AIの採用・保留・棄却および組織変更の
  最終判断
- 実際に確認した資料・記録:
  `OBS-20260811-221400-ai-readiness-as-system-adaptation`と、そのSourceである
  `RN-20260811-204844-ai-flow-team-topologies-reading-dialogue`、および原文確認を保存した
  `EXT-20260811-223226-ai-data-knowledge-curation`、意図の具体化を保存した
  `OBS-20260811-224044-readiness-diagnosis-observation-net`を確認した。他の外部資料の原典は、
  このEpisodeの作成時には再確認していない

## 結果

`not_tested`

### 実際に観測したこと

実践者の読書対話から診断候補軸を構成し、Readinessの中心を事前診断と観測網へ具体化したが、
実際の組織またはValue StreamについてCurrent State MBPM、Baseline、Signal、Trigger、Owner、
対処Option、Time to Detect、Time to Decide、Time to Adaptまたは利用後Outcomeを観測していない。

## 解釈

このEpisodeが扱うReadinessは、AI導入へ許可を与えるための全社成熟度ではない。組織状態に
よって避けられない適応期間が長引く、または混乱が拡大する可能性に対し、個々のValue Streamで
先にCurrent Stateと観測点を具体化し、問題発生後の探索と調整を短くできるかを扱う。

事前診断は、すべての問題を予測して除去するためではない。AIによる局所高速化がどの下流制約を
露出させるかは利用後まで分からない場合がある。そのため、Baseline、Signal、Trigger、Ownerおよび
対処Optionを「網」として置き、未知の制約を早く発見して対処することに価値を置く。

MBPMは、Actor間Handover、Process Time、Lead Time、待ち、手戻り、Clarification、Correction、
Backflowおよび`% Complete & Accurate`を置く有力な方法候補である。ただし、Business Outcome、
最終成果物の品質、原因構造、Data and Knowledge CurationまたはArchitecture RiskまでMBPMだけで
判断せず、別のSignalとDecisionを接続する。

AI Capability自体のModel、Evaluation、GuardrailまたはSoftware Component責任は、
`HYP-20260811-131148-consumer-governed-ai-capability`と
`OBS-20260811-220557-ai-resource-software-component-decomposition`が扱う。このEpisodeは、それらを
曖昧な組織Readinessへ吸収せず、Capabilityを利用する周辺Systemの適応能力に範囲を限定する。

## 限界

- 組織状態がAI導入後の適応期間または混乱の大きさへ影響する中心前提を独立して検証していない。
- 「混乱」「適応期間」「効率的な対処」を表す操作的定義、開始点、終了点および比較単位を
  確定していない。
- 事前診断と観測網によって、Time to Detect、Time to Decide、Time to Adapt、混乱の期間または
  下流負荷が改善するか確認していない。
- DataとKnowledge SystemのCurationに関する三つの原文抜粋は確認したが、Report全文、その他の
  外部資料の正確な主張、定義、対象範囲および相互整合を確認していない。
- Data Meshの定義、実装方法、効果およびAI Readinessとの因果関係を独立して確認していない。
- 観測網のSignal、Trigger、Owner、Decision Right、対処Optionおよび更新頻度を定義していない。
- 組織Systemの制約とAI利用後のOutcome、FlowまたはCostの因果関係を確認していない。
- 事前診断と観測網が通常の継続的改善、Platform Product Management、Architecture Governanceまたは
  Software Delivery Performanceの境界を確認していない。
- MBPMが観測網の設計に十分な粒度を持つか、作成・維持Costが比例的か確認していない。
- 同じPractice Value Hypothesisを親とする他のSolutionまたはFeatureの結果を継承しない。
- このHypothesisは組織標準、成熟度Model、AI導入判断または登壇内容として採用されていない。

## 公開安全性確認

- checked_at: 2026-08-11T22:49:00+09:00
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
