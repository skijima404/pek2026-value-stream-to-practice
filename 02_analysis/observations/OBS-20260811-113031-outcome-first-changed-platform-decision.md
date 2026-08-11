---
id: OBS-20260811-113031-outcome-first-changed-platform-decision
type: observation
title: "Outcome起点の検討はModernize基盤選定へ保留・暫定化・Risk承認を追加した"
content_language: ja
created_at: 2026-08-11T11:30:31+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-11T12:12:25+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - case_recollection
  - explicit_validation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260811-113030-modernization-platform-decision-walkthrough
---

# 観察

## 知識の成立根拠

一つのModernize基盤選定Caseへ関与し、承認資料候補へ目を通した実践者に、AIまたはSpeedから
開始する場合と、Business Outcome、Decision QualityおよびRiskから開始する場合の判断差を
一問ずつ確認した。目的を持ったFocused Interviewを`explicit_validation`、保存した回答を
`recorded_statement`、One Way Door、AccountabilityおよびResidual Riskに関する実務判断を
`practitioner_experience`として扱う。

過去Caseの経緯は`case_recollection`として扱う。Partnerへの不安と基盤選定の因果、
Governance構造およびCounterfactualの比較には`reasoned_synthesis`を含める。当時の資料を
Repositoryで確認していないため、`direct_observation`にはしない。

## 根拠箇所

- `RN-20260811-113030-modernization-platform-decision-walkthrough`の「Bounded Case」
- 同Raw Noteの「表明されたOutcomeと接続の不足」
- 同Raw Noteの「実際の選定で重視された条件」
- 同Raw Noteの「SpeedまたはAI Use Case起点のCounterfactual」
- 同Raw Noteの「Outcome起点の判断分岐」
- 同Raw Noteの「GovernanceとDecision Package」および「AIの責任境界」

## 根拠から直接言えること

一つのModernize Caseでは、Project ArchitectがProject MemberへのHearingを経て、Container
Orchestration基盤ではなく仮想Machine基盤を選んだ。選定が先にあり、運用可能な構成へ
寄せた結果、Applicationは細かなMicroserviceではなくSubdomain程度の粗い粒度で分割された。

選定では将来拡張性と、上位のBusiness課題である労働人口減少への対応が語られたが、
Business課題、Architecture Visionおよび基盤選定をつなぐ因果は、実践者には見えなかった。
実際に重視された主な条件は、運用能力、既存Skill、扱いきれること、および責任を引き受け
られることだった。

外部Partnerを扱いきれるかという不安は繰り返し表明されていた。ただし、その不安が基盤
選定の根底にあったかは実践者の推測であり、因果は確認されていない。

SpeedまたはAI Use Case起点では、Teamが扱いきれるかという不安へ反応し、意思決定を速める
可能性がある一方、Business Goalへの適合性は解決しないと実践者は評価した。

Outcome起点では、Business Outcomeが優先される場合にArchitecture Visionとの接続が
できるまで基盤選定を保留する。基盤Retirementなどの期限制約が優先される場合は、仮想
Machine基盤で暫定的に前進し、後日の再検討計画を持つという分岐が得られた。

また、AIによる推薦だけでなく、推奨案と対抗案の内容、根拠、Risk、対策および比較結果を
含むDecision Package、技術Roleによる確認・修正・署名、Business Stakeholderによる
Residual Risk受入が必要とされた。AIはDecision Packageの下書きを支援できるが、Priority、
技術的AccountabilityおよびResidual Risk受入の最終判断を担わない。

## Hypothesisへの射程

`HYP-20260804-013223-outcome-first-ai-resource-allocation`のU1に対して、同一の基盤選定候補を
AIまたはSpeedから始める場合と、Business Outcome、Decision QualityおよびRiskから始める
場合を比較した。

Outcome起点では、Capabilityが基盤推薦の高速化だけでなく、Architecture Vision形成、
OptionとRiskの比較、およびDecision Package作成へ広がった。責任境界は、AIの下書き、
技術Roleの確認・署名、Business StakeholderのPriority判断とResidual Risk受入に分かれた。
さらに、Business Outcomeを優先する場合の保留と、期限制約を優先する場合の暫定選定・
再検討計画が判断Optionへ入った。

このため、一人の実践者による一つのBounded Walkthroughの範囲では、Value Streamの課題と
期待Outcomeから始めると、AIまたはSpeedから始める場合とは異なるCapability、責任境界、
確認項目および保留判断を選べるというU1を`supports`する直接Evidenceとなる。

## 代替説明

- 判断差はOutcome起点の効果ではなく、質問によって通常のArchitecture Governanceを
  思い出したために生じた可能性
- SpeedまたはAI Use Case起点でも、通常のReviewによって同じDecision Package、責任境界、
  保留判断へ到達する可能性
- 実際の選定が運用能力と既存Skillに適合しており、Architecture Visionを明示しても同じ
  基盤とApplication粒度を選んだ可能性
- Business Outcomeではなく、基盤Retirement、実装CapacityまたはPartner管理Riskが実際の
  支配的な制約だった可能性

## 曖昧さと限界

- 一人の実践者による一つの過去CaseとCounterfactual Walkthroughであり、二つの開始方法を
  実装して比較していない。
- 当時のArchitecture資料、Risk比較、承認資料、会議記録または他の関係者の回答を確認して
  いない。
- Partnerへの不安と基盤選定の因果、および当時のGovernance構造には推測を含む。
- Architecture Vision形成、Decision Package作成、Reviewおよび再検討計画のCostを確認して
  いない。
- 選定後の運用品質、Business Outcome、Reputation Risk、再検討または長期的な拡張性を
  確認していない。
- U1の結果からU3の経済妥当性、U4の分析Cost、Feature Hypothesisまたは親Value Hypothesisを
  支持しない。

## 公開安全性確認

- checked_at: 2026-08-11T12:12:25+09:00
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
