---
id: OBS-20260811-140549-ai-subsystem-team-terminology-fit
type: observation
title: "AI Capabilityを担うComplicated Subsystem teamという整理は公式用語と両立する"
content_language: ja
created_at: 2026-08-11T14:05:49+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-11T14:12:53+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - external_research
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260811-131146-ai-capability-consumer-value-stream-boundary
  - type: derived_from
    target: EXT-20260811-140548-team-topologies-key-concepts
  - type: references
    target: OBS-20260811-131147-consumer-concerns-govern-ai-capability
---

# 観察

## 知識の成立根拠

`RN-20260811-131146-ai-capability-consumer-value-stream-boundary`には、実践者がAIを
`Complicated Subsystem`として捉え、消費側Value Streamから利用される提供側Capabilityに
位置づけた発言が記録されている。この発言を`recorded_statement`として扱う。

`EXT-20260811-140548-team-topologies-key-concepts`は、Team Topologies公式ページで確認した
Team Type、Stream-aligned teamのOutcome所有、およびTeam間Interaction Modeを
`external_research`として保存している。

AI Capabilityを専門的なSubsystem、そのCapabilityを所有するTeamをComplicated Subsystem
team、利用側をStream-aligned teamとして対応づけ、今回の責任境界との整合を判断する部分は
`reasoned_synthesis`である。

## 根拠箇所

- `RN-20260811-131146-ai-capability-consumer-value-stream-boundary`の
  「AIを提供側Capabilityとして位置づける」
- 同Raw Noteの「提供Topologyは成熟度によって変わる」
- `EXT-20260811-140548-team-topologies-key-concepts`の
  「外部ページが説明していること」
- 同External Inputの「限界」

## 根拠から直接言えること

Team Topologies公式ページが定義するのは四つの基本的なTeam Typeであり、正式な用語は
`Complicated Subsystem team`である。このTeamは、重要な数学、計算または技術的専門知識を
必要とする領域を担う。

同ページでは、Stream-aligned teamがValue Streamに沿って直接Valueを届け、Outcomeと
End-to-EndのSliceを所有する。Team間には、一方が提供し他方がServiceとして消費する
`X-as-a-Service`を含むInteraction Modeがある。

## 今回の整理として導けること

高い専門知識を必要とするAI Capabilityが存在する場合、そのCapabilityを複雑なSubsystem、
所有TeamをComplicated Subsystem teamとして整理し、Stream-aligned teamが利用する構図は、
公式ページのTeam TypeとInteraction Modeに矛盾しない。

この対応では、会話上の「AIはComplicated Subsystem」という短縮表現を、Repositoryでは
次のように分解できる。

- 対象:
  専門知識を要するAI Capabilityまたは複雑なSubsystem
- 所有者:
  Complicated Subsystem team
- 利用者:
  Value StreamにAlignmentするStream-aligned team
- Interaction:
  Contextに応じたX-as-a-ServiceまたはCollaboration

Stream-aligned teamがOutcomeとEnd-to-EndのSliceを所有し、Complicated Subsystem teamが
専門性を担うという公式説明から、提供側の局所指標または内部都合だけで消費側Value Streamの
Outcomeを置き換えないという今回の境界原則は、Team Topologiesの意図に沿う解釈といえる。

## 明示的な公式定義と今回の推論の境界

公式ページは、AI TechnologyまたはAI Capability自体をTeam Topologyとして分類していない。
また、提供側Teamの論理が利用側のOutcomeを上書きしてはならないというRuleを、その文言で
明示していない。

したがって、AI CapabilityをComplicated Subsystemとして扱える条件と、消費側Value Streamの
Outcomeを上位に置く責任境界は、公式用語を利用した今回の設計上の推論である。公式ページとの
整合は、この推論の実務上の有効性、組織への適用結果またはHypothesisの検証を意味しない。

## 曖昧さと限界

- AI Capabilityのどの複雑性、専門性またはCognitive Loadを分類Signalとするか確認していない。
- Complicated Subsystem team、Platform teamまたは外部Serviceの境界をCaseで比較していない。
- X-as-a-Serviceが常に適切とは限らず、未知のCapabilityを共同で発見する期間には
  Collaborationが必要となる可能性がある。
- ConsumerとProviderの条件が衝突した場合のDecision Owner、例外、Residual Risk受入および
  Accountabilityを確認していない。
- 公式ページ一つの確認であり、Team Topologiesの書籍、Courseまたは実組織での適用結果を
  調査していない。
- このObservationはTeam設計、AI Capabilityまたは登壇内容の採用を意味しない。

## 公開安全性確認

- checked_at: 2026-08-11T14:12:53+09:00
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
