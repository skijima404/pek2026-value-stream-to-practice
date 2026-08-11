---
id: OBS-20260811-003710-platform-flow-step-quality-priorities
type: observation
title: "Platform選定・環境入手FlowではStepごとに優先品質とError Costが異なった"
content_language: ja
created_at: 2026-08-11T00:37:10+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-11T01:18:44+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - case_recollection
  - explicit_validation
relations:
  - type: derived_from
    target: RN-20260811-003709-platform-selection-step-quality-interview
---

# 観察

## 知識の成立根拠

複数組織で利用される一般的なPlatform選定・環境入手Flowを知る実践者へ、同じFlowの
複数Stepについて、Actor、Outcome、優先品質、時間制約、Error Cost、下流影響および
SpeedとのCounterfactualを一問ずつ確認した。目的を持ったFocused Interviewを
`explicit_validation`、保存した回答を`recorded_statement`、複数組織での実務判断を
`practitioner_experience`として扱う。

Step 7の遅延は、実践者自身がProject Memberとして経験した一つの過去事例である。
当時の申請TicketまたはProject日程をRepositoryで確認していないため、
`case_recollection`として扱い、`direct_observation`にはしない。

## 根拠箇所

- `RN-20260811-003709-platform-selection-step-quality-interview`の
  「Step 1: Platformの種類を調べる」
- 同Raw Noteの「Step 6: 決める」
- 同Raw Noteの「Step 7: 利用開始の手続きをする」

## 根拠から直接言えること

人手の申請・承認が残るBounded Caseで、開発TeamがPlatformを選定して開発環境を
入手するまでの8 Stepを整理し、3 Stepを詳しく確認した。未自動化Processを選んだのは、
申請者、承認者およびPlatform TeamのResponsibilityと確認観点を明示するためだった。
AutomationされてもResponsibilityは消えず、自動化されたProcessが同じ観点を包含する
必要があるという条件が示された。

Step 1では、Tech Leadが利用可能なPlatformのListを持つため、主要候補に漏れがない
Coverageが最優先だった。通常は約1時間でListを入手できるため、主要候補が漏れる可能性と
引き換えに10倍速くする便益は小さかった。漏れはArchitecture Reviewまたは運用段階での
説明と再検討を誘発する。

Step 6では、Tech LeadとArchitecture Boardが、可用性実績、運用可能性、自動化、保守性、
監視設計を考慮してPlatformを決めるDecision Qualityが最優先だった。実践者はこの決定を
典型的なOne Way Doorと位置づけた。数日早く決める代わりに将来の障害要因または運用設計の
見落としが増える方法は、業務上の信頼性とReputation Riskのため採用しないと回答した。

Step 7では、Tech Leadにとって、承認の局所速度より、認証情報、接続経路および関連申請を
含む利用開始に必要な一式のCompletenessが優先された。実践者が参加した一つの過去Caseでは、
分割された申請の存在を知らず再申請が連鎖し、実践者の作業開始が約2か月遅れた。

同じStep 7でも、Platform Teamにとっては、申請、作業、責任者、必要な監査情報および
管理台帳を追跡できるTraceabilityが必須だった。記録を省略して承認を速くする方法は、
Incident対応と棚卸しで問題を起こすため採用しないと回答した。

実践者はStep 7を、手順が固まったITSMのService Catalog Itemと位置づけた。非決定論的な
事象が発生すると問題になるため、CompletenessとTraceabilityに加えて、決定的で再現可能な
実行が必要だと説明した。

## Hypothesisへの射程

`HYP-20260804-013223-outcome-first-ai-resource-allocation`のU2に対して、同じBounded
Value Stream内でも、Step 1はCoverage、Step 6はDecision Quality、Step 7はActorに応じて
CompletenessまたはTraceabilityが優先され、Speedが一貫した最優先ではなかった。

優先順位は品質Labelだけでなく、Actor、Outcome、通常所要時間、将来の障害、業務上の
信頼性、Reputation Risk、再申請、Incident対応および棚卸しという下流影響で説明された。
Counterfactualでも、Speed改善と引き換えに最優先品質を下げる方法は採用されなかった。
このため、確認したCaseと3 Stepの範囲ではU2を`supports`する直接Evidenceとなる。

`HYP-20260809-203135-quality-first-ai-allocation-workflow`のU1に対しても、StepとActorを
限定すると、候補List、運用品質に基づく決定、利用可能な構成一式、追跡可能な管理記録という
判断可能な完了状態へ品質を具体化できた。この限定範囲でU1を`supports`する。

## 代替説明

- 品質差はStep固有ではなく、質問時に選んだLabelまたは説明の粒度から生じた可能性
- Step 1のCoverageとStep 7のCompletenessは、同じ網羅性を異なる名前で表した可能性
- AIを含まない通常のArchitecture Reviewまたは申請改善でも同じ優先順位が得られる可能性
- 約2か月の遅延には、申請分割以外の待ち、CapacityまたはProject事情が寄与した可能性

## 曖昧さと限界

- 一人の実践者による一般化されたFlowと一つの過去事例に基づき、一次資料または他のActorの
  回答を確認していない。
- 8 Stepのうち3 Stepだけを詳しく確認し、頻度は定量化していない。
- Speedを最優先とするStepがないことを、すべてのStepまたは組織へ一般化できない。
- 品質優先による実際の障害削減、Reputation Risk低減または総Lead Time短縮を測定していない。
- Step 6をOne Way Doorとする具体的な可逆性基準と、Step 7で許容できる実行差分は未定義である。
- 自動化済みProcessが同じResponsibilityと確認観点を実際に包含するかは確認していない。
- U2の結果から、親Solutionの他Component、特にU3の経済妥当性を支持しない。

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
