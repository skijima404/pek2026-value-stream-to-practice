---
id: RN-20260811-113030-modernization-platform-decision-walkthrough
type: raw_note
title: "Modernize基盤選定におけるOutcome起点とSpeed起点の比較Interview"
content_language: ja
created_at: 2026-08-11T11:30:30+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-11T12:12:25+09:00
sanitization_checked_by: agent:codex
tags: [accountability, architecture-vision, case-recollection, decision-quality, focused-interview, modernization, platform-selection, practitioner-experience, residual-risk]
---

# Modernize基盤選定におけるOutcome起点とSpeed起点の比較Interview

## この記録の位置づけ

`HYP-20260804-013223-outcome-first-ai-resource-allocation`のU1を確認するため、
一つのModernize基盤選定Caseについて、AIまたはSpeedから開始する場合と、Business
Outcome、Decision QualityおよびRiskから開始する場合の判断差をFocused Interviewで
確認した対話を、Agentが構造化して保存する。

公開対象に不要な顧客、業種、時期、組織名、System名および製品固有の組み合わせは保存しない。
当時のArchitecture資料、会議記録、Hearing記録、Risk比較表または承認資料はRepositoryで
確認していない。

## Bounded Case

既存ApplicationをModernizeする際の実行基盤選定を対象とした。

- 判断者: Project Architect
- Input: Project MemberへのHearing
- 比較した基盤: 仮想Machine基盤とContainer Orchestration基盤
- 選択: 仮想Machine基盤
- 関連するApplication判断: 細かなMicroserviceではなく、Subdomain程度の粗い単位で分割

因果の順序は、Applicationの粒度を先に決めて基盤を選んだのではない。

```text
運用能力・既存Skill・責任を持てる範囲を評価
  -> 仮想Machine基盤を選択
  -> 扱える構成へ寄せる
  -> Applicationを粗い粒度で分割
```

## 表明されたOutcomeと接続の不足

将来拡張性が選定時のOutcomeとして説明されていた。上位のBusiness課題として、将来の
労働人口減少への対応が語られていたため、発端となるBusiness課題自体は存在した。

一方、何を実現すれば労働人口減少への対応になるのか、どの事業変化をApplicationおよび
基盤のどの能力で支えるのかという接続は、実践者には見えなかった。Architecture Visionと
その根拠となるBusiness Goalが、基盤選定に使える粒度で明示されていなかったと
実践者は振り返った。

## 実際の選定で重視された条件

主な判断材料は、運用能力と既存Skillだった。細かな粒度の構成を自分たちで扱いきれない
可能性を踏まえ、運用を想像でき、責任を引き受けられる基盤へ倒したと説明された。

外部Partnerを扱いきれるかという不安は、関係者から繰り返し表明されていた。一方、その
不安が基盤選定の根底にあったかは確認されておらず、実践者の解釈である。

実践者は、実装能力を外部Partnerへ依存し、複数のPartnerをSubdomain単位へ割り当て、
自組織が統括Architectureを担う初回の試みであったため、不確実性を増やしたくなかった
可能性を挙げた。この説明も、当時明示された判断根拠ではなく現在の推測である。

このContextでは、基盤選択は全体Risk管理の一項目であり、支配的な項目ではなかったと
実践者は解釈した。

## SpeedまたはAI Use Case起点のCounterfactual

「将来拡張性の高い基盤をAIで素早く選ぶ」ことから開始した場合、AIはTeamが扱いきれるか
という不安に反応し、意思決定自体を速めた可能性があると実践者は推測した。

ただし、選定速度が上がっても、その判断が労働人口減少への対応として適切かという疑問は
残る。AIが速くした可能性と、Business Goalへの適合性が改善したことを同一視しない。

## Outcome起点の判断分岐

実践者は、支配的なPriorityに応じて次のように判断すると回答した。

- Business Outcomeが優先される場合:
  Architecture VisionとBusiness Goalの接続を明確にするまで基盤選定を保留する
- 基盤RetirementなどのSchedule制約が優先される場合:
  仮想Machine基盤を暫定的に選んで前進し、後日さらに先の基盤またはArchitectureへ進む
  再検討計画を持つ

Outcome起点では、基盤推薦を速くするだけでなく、Architecture Visionの形成、選定の保留、
暫定Scopeの限定、および将来の再検討計画がCapabilityと判断Optionへ入る。

## GovernanceとDecision Package

最終承認はArchitecture Boardに相当するが、対象Caseでは経営会議のようなBusiness
Stakeholderの場だった。Business側は技術判断そのものを行うのではなく、その意思決定を
Businessとして支援できるかを承認する。

技術的な情報の非対称性があり、技術側が最もRiskを抑えられる案として提示すると、Business
側はその説明へ依存せざるを得ないと実践者は振り返った。

最低限必要なDecision Packageとして、次を挙げた。

- 推奨案の内容と根拠
- 推奨案によって発生するRiskと対策
- 対抗案の内容
- 対抗案によって発生するRiskと対策
- Riskの比較結果

実践者は経営会議資料の候補へ目を通した。ただし、上記のDecision PackageとResidual Risk
承認の構造は、当時の資料に明記されていた事実ではなく、現在の振り返りによる推測を含む。

## AIの責任境界

この承認は基幹系Systemに関するOne Way Doorであり、停止時にはReputation Riskが避けられない
ため、Decision Qualityを最優先とした。

AIがDecision Packageを下書きする場合でも、Project Architectまたは別の技術Roleによる
確認と署名が必要である。技術Roleは内容を読み、自組織のContextへ合わせて修正し、技術的な
Accountabilityを引き受ける。

Business Stakeholderは、技術側がRiskを管理・低減した後に残るResidual Riskを、Businessと
して引き受けられるか判断する。AIはPriorityとResidual Risk受入の最終判断を担わない。

## 成立根拠の区別

- `recorded_statement`候補:
  Interviewで保存したActor、選択肢、選択、運用能力、既存Skill、繰り返し表明された不安、
  Counterfactualおよび望ましい判断条件
- `case_recollection`候補:
  実践者が関与し、承認資料候補へ目を通した一つの過去Case
- `practitioner_experience`候補:
  One Way Door、Decision Package、AccountabilityおよびResidual Risk受入に関する実務判断
- `reasoned_synthesis`候補:
  Partnerへの不安と基盤選定の関係、初回Trialで不確実性を増やさなかった可能性、
  Governance構造および二つの開始方法から得られる判断差
- `explicit_validation`候補:
  U1を目的として、同一CaseのSpeed・AI起点とOutcome・品質起点を比較したFocused Interview

当時の資料をRepositoryで確認していないため、`direct_observation`または
`external_research`として扱わない。

## この記録だけでは分からないこと

- 当時のArchitecture Vision、Business Goal、選定基準、Risk比較および承認内容の原文
- Project Member、Project Architect、PartnerおよびBusiness Stakeholder本人の回答
- Partnerへの不安が基盤選定へ与えた実際の因果
- AIまたはSpeed起点の方法を実際に使った場合の推薦、所要時間、判断およびOutcome
- Outcome起点でArchitecture Visionを作った場合に、基盤またはApplication粒度が変わったか
- 暫定基盤から次へ進む再検討計画、Owner、期限、Exit条件および実行結果
- Decision Package作成、Reviewおよび比較に必要なCost
- 選定後の運用品質、Business Outcome、Reputation Riskおよび長期的な拡張性

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
