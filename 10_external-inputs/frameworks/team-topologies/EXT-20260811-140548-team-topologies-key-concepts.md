---
id: EXT-20260811-140548-team-topologies-key-concepts
type: external_input
title: "Team Topologiesの主要概念とTeam間Interaction Mode"
content_language: ja
created_at: 2026-08-11T14:05:48+09:00
created_by: agent:codex
source_type: official_webpage
source_url: https://teamtopologies.com/key-concepts
retrieved_at: 2026-08-11T14:03:00+09:00
retrieval_method: official_webpage_inspection
provided_by: human:kijima
changeability: externally_managed
asset_in_repository: false
tracking_parameters_removed: false
---

# Team Topologiesの主要概念とTeam間Interaction Mode

## 位置づけ

Team Topologies公式サイトの`Key Concepts`ページを、Team TypeとTeam間Interaction Modeの
用語参照として保存する。

本ノードは、外部ページの説明を確認日時点で要約したExternal Inputである。AI Capabilityを
特定のTeam Typeへ分類する決定、今回の責任境界の妥当性、またはHypothesisの検証結果を
示すものではない。

## 外部ページが説明していること

同ページはTeam Topologiesを、価値のFlowを速めるためにTeam-of-Teamsの組織設計を考える
Approachとして説明している。

四つの基本Topologyは、TechnologyまたはComponentそのものではなく、次のTeam Typeとして
説明されている。

- Stream-aligned team:
  通常はBusiness Domainの一部分における仕事のFlowへAlignmentするTeam
- Enabling team:
  Stream-aligned teamが障害を越えることを支援し、不足Capabilityも検出するTeam
- Complicated Subsystem team:
  重要な数学、計算または技術的専門知識を必要とする領域を担うTeam
- Platform team:
  Stream-aligned teamのDeliveryを加速する内部Productを提供するTeam群

同ページは、Stream-aligned teamがBusiness Domainまたは他のFlowのSliceをEnd-to-Endで
所有し、Customerへ直接Valueを届け、Outcomeを所有するとも説明している。

Team間のInteraction Modeには、期間を区切った`Collaboration`、一方のTeamが提供し他方が
Serviceとして消費する`X-as-a-Service`、一方が他方を支援する`Facilitation`がある。

## 今回参照した範囲

- `Four fundamental topologies`
- `Three team interaction modes`
- `Words of caution`
- `Four fundamental topologies - with the flow of change`
- `The Six Patterns`内のTeam TypeとInteraction Modeの説明

## 限界

- 外部ページは外部管理されており、内容またはURLが変更される可能性がある。
- 本ノードは確認日時点の公式Webページを要約したものであり、書籍、Course、Case Studyまたは
  Team Topologiesの全Practiceを網羅しない。
- 公式ページはAI CapabilityをComplicated Subsystem teamが担うべきだとは説明していない。
- 公式ページは、提供側Teamの論理が消費側Value StreamのOutcomeを上書きしてはならないという
  今回の境界原則を、明示的なRuleとして記載していない。
- Team Typeだけを切り出して適用するのではなく、Flow、Cognitive Load、Interaction Modeなどを
  含むThinking Model全体で扱う必要があるという注意も同ページにある。
