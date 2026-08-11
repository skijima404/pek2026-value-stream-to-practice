---
id: OBS-20260811-220557-ai-resource-software-component-decomposition
type: observation
title: "AI ResourceはSoftware Systemとして責任単位へ分解して扱う"
content_language: ja
created_at: 2026-08-11T22:05:57+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-11T22:12:34+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - external_research
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260811-204844-ai-flow-team-topologies-reading-dialogue
  - type: derived_from
    target: EXT-20260811-140548-team-topologies-key-concepts
  - type: references
    target: OBS-20260811-140549-ai-subsystem-team-terminology-fit
---

# 観察

## 知識の成立根拠

`RN-20260811-204844-ai-flow-team-topologies-reading-dialogue`には、実践者がAIをWorkloadまたは
Business Capability上では仕事を割り当てるResourceとして扱う一方、そのResourceを成立させる
実体は開発、Test、運用および改善の対象となるSoftware Systemであると整理した対話が記録されて
いる。この立場と、「AIも通常のSoftware開発として扱う」という判断を`recorded_statement`と
して扱う。

同Raw Noteには、実践者が2019年英語Kindle版`Team Topologies`のChapter 5、
`Complicated-Subsystem Teams`と、Chapter 8、Figure 8.8を確認した記録がある。
`EXT-20260811-140548-team-topologies-key-concepts`には、現在のTeam Topologies公式ページが、
Team TypeをTechnologyまたはComponentそのものではなくTeamとして定義し、重要な数学、計算または
技術的専門知識を必要とする領域をComplicated Subsystem teamが担うと説明していることが保存
されている。これらを`external_research`として扱う。

AIをResourceとして利用するViewと、その実体をSoftware Systemとして構成・所有するViewを分け、
Feature、Model、Inference、Evaluation、Guardrailなどへ責任を分解する部分は
`reasoned_synthesis`である。

## 根拠箇所

- `RN-20260811-204844-ai-flow-team-topologies-reading-dialogue`の
  「AIを一つの箱として分類しない」
- 同Raw Noteの「AIにはWorkloadとSoftware Systemの二つの見方がある」
- 同Raw Noteの「専門性には専門性の置き場所がある」および
  「`significant mathematics`の確認範囲」
- `EXT-20260811-140548-team-topologies-key-concepts`の
  「外部ページが説明していること」および「限界」

## 根拠から直接言えること

実践者は、Workload上のAIをHuman、Automationまたは外部Providerと並ぶResourceとして扱えるが、
その背後にはModel、Inference、Evaluation、Guardrailおよび運用を含むSoftware Systemと、それを
保守するTeamが存在すると整理した。また、AI Productを一つの箱として一つのTopologyへ当てはめず、
利用者が触れるFeatureと高度な専門性を持つComponentを分ける必要があると述べた。

Team Topologies公式ページが定義しているのは`Complicated Subsystem team`というTeam Typeであり、
TechnologyまたはAI全体をTeam Typeとして分類していない。重要な数学、計算または技術的専門性を
必要とする領域を、そのTeamが担うと説明している。

## 今回の整理として導けること

AIの利用判断では、次の二つを同時に扱う必要がある。

1. Workload View:
   Value Stream上のTaskまたは判断を、Human、AI、決定的Automationまたは外部Serviceのどこへ
   割り当てるか
2. Software System View:
   AI Resourceを成立させるFeature、Model、Inference、Evaluation、Guardrail、Context処理および
   運用機能を、どのSoftware Componentと責任へ分解するか

高度な数学、評価または推論の専門性を持つSoftware Componentを`Complicated Subsystem`、それを
所有するTeamを`Complicated Subsystem team`として区別する整理は、Team Topologies公式用語と
両立する。利用者に接するFeature、共通Platform Interfaceまたは外部Serviceまでを、一律に
Complicated Subsystemと呼ぶ必要はない。

この分解の目的はOrganization Readinessを評価することではない。AIを通常のSoftware Systemとして
扱い、各ComponentへOwnership、Boundary、Version、TestまたはEvaluation、変更、Release、運用、
観測および障害時責任を置けるようにすることである。その上で、消費側Value StreamのOutcome、
受入条件および最終利用判断と、提供側Software Systemの実現責任を接続する。

## 明示的な外部説明と今回の推論の境界

Team Topologies公式ページは、AI ProductをFeature、Model、Inference、EvaluationまたはGuardrailへ
分解する方法を説明していない。また、すべてのAI ModelをComplicated Subsystemとして扱うべき
だとも説明していない。

通常のSoftware Engineeringに必要な責任をAI Componentへ適用すること、ならびにWorkload Viewと
Software System Viewを接続することは、実践者の立場と公式用語を組み合わせた設計上の推論である。
このObservationは、その分解方法が実際のAI利用判断、品質、FlowまたはAccountabilityを改善した
という検証結果ではない。

## 曖昧さと限界

- どの粒度までSoftware Componentを分解すれば判断に十分か確認していない。
- Model、Prompt、Context、Evaluation DataまたはGuardrailのうち、何を独立した変更・Release単位と
  するか確認していない。
- 外部AI Serviceでは内部Componentを直接管理できず、ProviderとのContract、Version、Telemetry
  およびExit条件へ責任を写像する必要がある可能性がある。
- 通常のTestとAI固有のEvaluation、決定的Automationと非決定的AIの境界をCaseで確認していない。
- Complicated Subsystem team、Platform team、Stream-aligned teamまたは外部Providerの配置を
  実Caseで比較していない。
- Organization Readiness、Knowledge CurationまたはInteraction成熟度は、このObservationの
  対象外である。
- このObservationはTeam設計、Software Architecture、AI Toolまたは登壇内容の採用を意味しない。

## 公開安全性確認

- checked_at: 2026-08-11T22:12:34+09:00
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
