---
id: RN-20260811-131146-ai-capability-consumer-value-stream-boundary
type: raw_note
title: "AI Capabilityと消費側Value Streamの境界に関する対話"
content_language: ja
created_at: 2026-08-11T13:11:46+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-11T13:41:33+09:00
sanitization_checked_by: agent:codex
tags: [acceptance-criteria, ai-capability, capability-contract, complicated-subsystem, platform-capability, responsibility-boundary, team-topologies, value-stream]
---

# AI Capabilityと消費側Value Streamの境界に関する対話

## この記録の位置づけ

`HYP-20260804-013223-outcome-first-ai-resource-allocation`のU3に置いた
「Speedを一律に優先する場合」との比較が、通常のApplication開発を表す対抗案として
不自然ではないかを起点に、実践者とAgentが中心仮説を再整理した対話を保存する。

この対話は、Team Topologiesの正本、組織事例、AI Coding Toolの利用記録または実測結果を
確認したResearchではない。実践者の立場と、その立場を検証可能な形へ分解するための
Agentによる整理を区別して残す。

## 通常のApplication開発として扱う

実践者は、通常のApplication開発では全工程でSpeedだけを一律に優先することは想定しにくい
と指摘した。まず業務後に満たすべきConcernがあり、そのConcernを満たすことを前提として、
その後にSpeed Upを検討するという順序を置いた。

対話では、次の二段階として整理した。

```text
業務後に成立していなければならないConcernを受入条件として定義する
  -> 条件を満たす実現案を残す
  -> 残った実現案の中でSpeed、CostまたはFlowを最適化する
```

したがって、Speedは品質と無条件に順位を競う項目ではなく、必要なConcernを満たすという
制約の下で最適化する対象となる。実践者は、もともとの中心仮説を文章で説明すると
「AIも普通のApplication開発として扱う」と表現できるとした。

## AIを提供側Capabilityとして位置づける

実践者は、AIをTeam Topologiesでいう`Complicated Subsystem`として捉えられると述べた。
同時に、それはValue Streamから消費される提供側Capabilityであり、Complicated Subsystem側の
論理によって消費側Value StreamのOutcome、Concernまたは受入条件を上書きしてよい理由には
ならない、という立場を明示した。

対話では、この境界を次のように整理した。

```text
消費側Value Stream
  Business Outcome、業務後のConcern、受入条件、Accountabilityを定義する
        ↓
Capability Contract
        ↓
提供側AI Capability
  実現可能性、技術的制約、内部Architecture、Guardrailを提示する
```

提供側は、Capabilityの限界、技術的Risk、必要なContextまたは実現Costを示し、契約条件の
調整を要求できる。しかし、生成速度、Model精度、採用率または内部実装の都合を、それだけで
消費側のBusiness Outcomeへ置き換えることはできない。

## 提供Topologyは成熟度によって変わる

対話では、AI Capabilityの提供形態は一つに固定されないと整理した。

- 高い専門性を内部で保有する場合の`Complicated Subsystem`
- 共通Capabilityとして社内で提供するPlatform Service
- 市場でCommodity化された外部ServiceまたはTool
- 個別Teamが通常の開発Toolとして使う形態

実践者は、AI Codingを目的に利用するCursorを、Commodity化された外部ServiceまたはToolに
近い例として挙げた。この例でも、Toolの生成速度または生成量がApplicationの成功条件を
上書きせず、Test、Security、Architecture、保守性、説明可能性および運用上のConcernを
満たした後に開発速度への寄与を判断するという原則は変わらないと対話で整理した。

## 既存Hypothesisへの含意

対話では、現在の`HYP-20260804-013223-outcome-first-ai-resource-allocation`をそのまま
意味変更するのではなく、既存Episodeを学習履歴として残し、次の中心命題を持つ後継Solution
Hypothesis候補を別Episodeとして作る案を置いた。

> AI Capabilityの提供Topologyにかかわらず、消費側Value Streamが定義するOutcome、
> 業務後のConcern、受入条件およびAccountabilityが利用判断を規定する。

旧Episodeとの`supersedes`または他の関係は、後継候補の保存内容を人間がReviewした後に
確定する。旧Episodeで確認したU1、U2またはU4のFindingは、新しい中心命題へ自動的に
転用しない。

## 知識の成立根拠候補

- `recorded_statement`候補:
  実践者が表明した通常のApplication開発として扱う立場、Concernを満たした後にSpeedを
  最適化する順序、および提供側の論理が消費側Value Streamを上書きしないという立場
- `reasoned_synthesis`候補:
  Concernを受入条件とする二段階、Capability Contract、提供Topologyの分類、および
  後継Hypothesisの検証対象への分解

この対話は、目的を定めてCaseまたは実装結果を確認したものではないため、現時点では
`explicit_validation`、`direct_observation`または`external_research`として扱わない。
実践者はこの立場を経験知として明示的に位置づけていないため、この記録だけから
`practitioner_experience`を推定しない。

## この記録だけでは分からないこと

- Team Topologiesにおける`Complicated Subsystem`の正本上の定義と、この整理との一致
- AI Capabilityをどの条件でComplicated Subsystem、Platform Serviceまたは外部Serviceと
  分類するか
- 消費側Value StreamがConcernと受入条件を実務で定義できる粒度
- 提供側と消費側の意見が衝突した場合のDecision Owner、例外およびResidual Risk受入
- Capability Contractの具体的な項目、更新頻度および維持Cost
- Contractを先に置くことでAIの利用、限定、棄却またはGuardrailが実際に変わるか
- 同じ受入条件を満たす実現案の中で、AIがEnd-to-EndのFlowまたはCostを改善するか
- Cursorを含むAI Coding Toolの実利用結果、組織PolicyまたはApplication Outcome

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
