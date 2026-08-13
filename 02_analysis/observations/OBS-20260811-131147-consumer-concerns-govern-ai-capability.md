---
id: OBS-20260811-131147-consumer-concerns-govern-ai-capability
type: observation
title: "AI提供Topologyより消費側Value StreamのConcernを上位に置く境界原則が整理された"
content_language: ja
created_at: 2026-08-11T13:11:47+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-12T01:31:17+09:00
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
    target: RN-20260804-230526-platform-engineering-as-service-engineering
  - type: derived_from
    target: OBS-20260811-140549-ai-subsystem-team-terminology-fit
  - type: references
    target: OBS-20260801-004820-coupled-platform-value-streams
---

# 観察

## 知識の成立根拠

`RN-20260811-131146-ai-capability-consumer-value-stream-boundary`には、AIも通常の
Application開発として扱い、業務後のConcernを満たした上でSpeedを最適化するという
実践者の立場と、AIを消費側Value Streamから利用される提供側Capabilityとして位置づける
発言が記録されている。これらを`recorded_statement`として扱う。

`RN-20260804-230526-platform-engineering-as-service-engineering`には、Platform Engineeringを
Platform機能の製造ではなく、利用者が安全にOutcomeへ進むServiceの設計、運用および改善として
扱うFramingと、AI Service DesignではReasoningしてよい世界、約束できる範囲および不明時の
戻り先を設計するという整理が記録されている。このFramingを`recorded_statement`、現在の
消費側・提供側境界へ接続する部分を`reasoned_synthesis`として扱う。

Concernを受入条件へ変換する二段階、Capability Contract、およびComplicated Subsystem、
Platform Service、外部Serviceという提供Topologyを一つの境界原則へ接続する部分は
`reasoned_synthesis`である。

`OBS-20260801-004820-coupled-platform-value-streams`は、提供側と利用側のValue Streamを
接続して観測する既存の近接概念として参照する。今回の会話を検証したEvidenceまたは
Team Topologiesの定義根拠としては扱わない。

その後、`OBS-20260811-140549-ai-subsystem-team-terminology-fit`で、Team Topologiesの
公式ページを確認した`external_research`により、正式なTeam Typeが
`Complicated Subsystem team`であること、Stream-aligned teamがOutcomeとEnd-to-Endの
Sliceを所有すること、およびX-as-a-Serviceを含むInteraction Modeが確認された。この確認は
公式用語との整合を支えるが、AI Capabilityの分類条件または今回の境界原則の実務上の有効性を
検証したものではない。

## 根拠箇所

- `RN-20260811-131146-ai-capability-consumer-value-stream-boundary`の
  「通常のApplication開発として扱う」
- 同Raw Noteの「AIを提供側Capabilityとして位置づける」
- 同Raw Noteの「提供Topologyは成熟度によって変わる」
- 同Raw Noteの「既存Hypothesisへの含意」
- `RN-20260804-230526-platform-engineering-as-service-engineering`の
  「中心となったFraming」「AI Service Designとしての世界設計」
  「AI Slopとの接続」「既存Practice Solutionとの接続」
- `OBS-20260811-140549-ai-subsystem-team-terminology-fit`の
  「根拠から直接言えること」「今回の整理として導けること」
  「明示的な公式定義と今回の推論の境界」

## 根拠から直接言えること

実践者は、通常のApplication開発では一律にSpeedだけを優先するのではなく、業務後に
満たすべきConcernを前提として、その条件を満たす実現案の中でSpeed Upを図るという順序を
置いた。AIについても特別な導入論から始めず、通常のApplication開発と同じ順序で扱うという
立場を示した。

また、AIを専門的なSubsystemとして位置づけられる一方、そのCapabilityの所有者を公式用語の
`Complicated Subsystem team`として整理できることが確認された。AI CapabilityはValue
Streamから消費される提供側Capabilityであり、Subsystem側の論理が消費側のOutcome、Concern
または受入条件を上書きする理由にはならないと実践者は表明した。

公式説明が対象とする、重要な数学、計算または技術的専門知識を必要とする部分という条件から、
AI全体を一括してComplicated Subsystemと呼ぶより、特にAI Modelの設計、学習、評価など、
高度な専門性をValue Stream側から隔離して提供する部分をSubsystem候補とする方が対応を
明確にできる。この対応は公式ページがAI Modelを例示した事実ではなく、公式の分類Signalと
今回のAI Capabilityを接続した`reasoned_synthesis`である。

この分解では、Complicated Subsystem teamがModelと専門的な技術制約を所有しても、AIを
利用するApplication、業務ProcessおよびEnd-to-End Outcomeまで所有することにはならない。
消費側Value Streamは、自らのConcernと受入条件を満たすためにModel Capabilityを利用する。

対話では、AI CapabilityがComplicated Subsystem、社内Platform Service、Commodity化された
外部Serviceまたは通常の開発Toolとして提供されても、次の責任境界は維持する候補として
整理された。

- 消費側Value Stream:
  Business Outcome、業務後のConcern、受入条件、利用判断およびAccountabilityを持つ
- 提供側AI Capability:
  実現可能性、技術的制約、内部実装、GuardrailおよびCapabilityの限界を示す
- 両者の境界:
  Capability Contractによって必要条件と提供条件を接続する

この整理では、Speedは無条件の最優先品質ではなく、Concernを満たすという制約の下で
最適化する対象となる。提供側の生成速度、Model精度、採用率または内部実装の都合だけから、
消費側の成功条件を置き換えない。

先行するService EngineeringのFramingでは、Platform Teamが作るFeatureだけでなく、利用者が
Outcomeへ進むための約束、利用条件、責任、運用およびValue Stream全体を設計対象としていた。
また、AI Service DesignはPrompt Techniqueではなく、Reasoningしてよい範囲、約束してよい
範囲、検証および不明時の戻り先を設計するものとして整理されていた。これは、消費側Concernと
提供側CapabilityをCapability Contractで接続する現在の境界原則に至る先行Framingとして
位置づけられる。

## 後継Hypothesis候補への射程

このObservationは、AI Capabilityの提供Topologyではなく、消費側Value Streamが定義する
Outcome、Concern、受入条件およびAccountabilityから利用、限定、Guardrailまたは棄却を
決めるという後継Solution Hypothesis候補の設計根拠になる。

ただし、会話上の立場とAgentによる構造化を記録したものであり、Capability Contractの
実用性、判断変更、Speed Up、End-to-End Flowまたは経済妥当性を確認したEvidenceではない。

## 曖昧さと限界

- Team Topologies公式ページでTeam Type、Stream-aligned teamのOutcome所有および
  Interaction Modeを確認したが、書籍、Courseまたは実組織での適用結果は確認していない。
- 公式ページはAI Capability自体を分類していない。重要な数学、計算または技術的専門知識を
  必要とすることを最初の分類Signal候補にできるが、どの程度の専門性でComplicated
  Subsystem teamを分離し、Platform Service、外部Serviceまたは通常Toolへ移すかの閾値は
  未確認である。
- 提供側の論理が消費側Outcomeを上書きしないという境界原則は、公式ページに明記されたRule
  ではなく、確認した公式概念と実践者の立場を接続した`reasoned_synthesis`である。
- 一つの対話で表明された立場であり、組織、Team、ApplicationまたはAI ServiceのCaseを
  観測していない。
- `practitioner_experience`の範囲、Case数または再現性を推定しない。
- Capability Contractの項目、Decision Owner、例外、Residual Risk受入および維持Costは
  未定義である。
- Commodity化の判定基準と、提供Topologyを変更すべきSignalを確認していない。
- このObservationから旧HypothesisのFindingを後継Hypothesisへ推移させない。
- このObservationは登壇内容、Team設計またはAI Toolの採用を意味しない。
- Service EngineeringおよびAI Service Designの表現は会話上のFramingであり、標準、外部
  Frameworkまたは実組織での有効性を確認したものではない。

## 公開安全性確認

- checked_at: 2026-08-12T01:31:17+09:00
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
