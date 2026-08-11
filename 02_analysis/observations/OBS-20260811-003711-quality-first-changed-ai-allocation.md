---
id: OBS-20260811-003711-quality-first-changed-ai-allocation
type: observation
title: "申請Stepの品質起点検討はAI優先から決定的自動化と限定的AI補助へ割り当てを変えた"
content_language: ja
created_at: 2026-08-11T00:37:11+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-11T01:18:44+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - explicit_validation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260811-003709-platform-selection-step-quality-interview
---

# 観察

## 知識の成立根拠

Platform選定・環境入手FlowのStep 7について、一律のSpeed優先でAIを使う場合と、
Completeness、Traceability、ReproducibilityおよびRiskからCapabilityを選ぶ場合を、
実践者とのFocused Interviewで比較した。保存した回答を`recorded_statement`、実務上の
Capabilityと責任境界の判断を`practitioner_experience`、目的を持った比較を
`explicit_validation`として扱う。

AI、決定的自動化およびTicket Systemへの役割分担を比較した解釈には
`reasoned_synthesis`を含める。実装比較または稼働中のAIを観測したものではない。

## 根拠箇所

- `RN-20260811-003709-platform-selection-step-quality-interview`の
  「Step 7のCapabilityと責任境界」
- 同Raw Noteの「Step 7: 利用開始の手続きをする」

## 根拠から直接言えること

Step 7を速くする実行Capabilityとして、実践者はAIよりAnsibleまたはTerraformのような
決定的自動化を選んだ。AI候補は、分割された申請の不足Check、引き渡し前の構成要素Check、
Componentごとに混在する承認・Reject結果からの作業Scope確定、および確定したScopeに
対応するPlaybookの起動だった。

実践者はStep 7を、手順が固まったITSMのService Catalog Itemと位置づけ、非決定論的な
事象が発生すると問題になると説明した。この判断により、AIをDefaultの実行主体とせず、
決定的な手順の外側で不足Checkまたは条件整理へ限定する根拠が明確になった。

AIへ承認または実行判断を任せる条件として、承認基準が明確であること、重大な金銭判断など
高Riskな判断を含まないこと、必要な承認とCost確認がSystem上で完了していること、
Reproducibilityを制約するGuardrailがあることが挙げられた。高額Costが関係する、判断根拠が
乏しい、または別途承認が必要な場合はAIへ任せない。

実践者は、このStageでのAI利用に積極的ではなかった。Ticket Systemで申請と承認を統合
できるなら、その仕組みを優先する。統合機構がなく、複数承認の一部が欠けても技術的に
成立する場合に、不足検出とScope調整をPatch的に補う用途へAIを限定した。

## Hypothesisへの射程

`HYP-20260809-203135-quality-first-ai-allocation-workflow`のU2に対して、品質とRiskから
検討した結果、CapabilityはAIによる高速化から、Ticket Systemによる統合、決定的な
Infrastructure Automation、および限定されたAI Checkへ変わった。

責任境界も、明確で低Riskな承認・Scope確定・Playbook起動だけをAI候補とし、高Risk、
根拠不足または承認未完了の判断を人間と既存Governanceへ残した。さらに、統合機構が
作れる場合はAI利用自体を保留または棄却した。この限定されたWalkthroughでは、品質起点で
Capability、責任境界、Guardrailおよび棄却判断が変わるというU2を`supports`する。

## 代替説明

- 差を生んだのは品質起点の順序ではなく、実践者が以前から持つ自動化設計の選好である可能性
- Speed起点でも、通常のRisk Reviewによって同じCapabilityと責任境界へ到達する可能性
- 統合されていない人手の申請・承認という設定が、AIをPatchとして選びやすくした可能性
- AIのCapabilityが具体化されていないため、製品またはModelによって判断が変わる可能性

## 曖昧さと限界

- 一人の実践者によるWalkthroughであり、二つの開始方法を実装・運用して比較していない。
- AIの再現性を確認する試験、閾値、失敗率およびHuman Escalation手順は未定義である。
- Service Catalog Itemで許容できる実行差分と、AIを利用可能にする決定性の閾値は未定義である。
- 自動化後も維持すべきResponsibilityと確認観点は示されたが、自動化仕様への反映は
  確認していない。
- Ticket System統合、決定的自動化およびAI Patchの実装・運用Costを比較していない。
- U2の結果からFeatureのU3、U4または親SolutionのU1、U3、U4を支持しない。
- Featureの結果を親Solutionへ推移させず、主対象U2のEvidenceには使わない。

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
