---
id: OBS-20260811-115141-standard-path-replaced-platform-selection
type: observation
title: "小規模Applicationでは標準PathとAdmission Controlが個別基盤選定を置き換えた"
content_language: ja
created_at: 2026-08-11T11:51:41+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-11T12:03:41+09:00
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
    target: RN-20260811-115140-small-application-standard-path-walkthrough
---

# 観察

## 知識の成立根拠

小規模Applicationを標準構成で提供する一つの部門について、標準Path、Service Scope、
受付判断、可逆性およびAIの責任境界を実践者へ確認した。目的を持ったFocused Interviewを
`explicit_validation`、保存した回答を`recorded_statement`、標準Pathと可逆性に関する
実務判断を`practitioner_experience`として扱う。

一つの部門に関する説明は`case_recollection`として扱う。Applicationの可逆性とTeam割り振りの
不可逆性、標準Pathによる選定不要化、およびAI Nativeな将来と現在の責任境界の比較には
`reasoned_synthesis`を含める。Routingは伝聞で、部門資料または受付記録を確認していないため
`direct_observation`にはしない。

## 根拠箇所

- `RN-20260811-115140-small-application-standard-path-walkthrough`の「Bounded Case」
- 同Raw Noteの「Service ScopeとAdmission Control」
- 同Raw Noteの「可逆性と判断時点」
- 同Raw Noteの「実際の受付対話」および「AIの責任境界」

## 根拠から直接言えること

小さな新規Applicationは作り直し可能なTwo Way Doorで、同じFramework内なら手戻りは
比較的小さい。部門標準の技術構成が事前に決められ、開発者は違和感がなければ個別比較を
行わず標準構成を採用した。標準を決める側は、顧客体験を改善する小規模Applicationを
迅速に作るという部門Missionへ適合する構成として選んでいた。

標準構成で扱えない規模または重大なDataを扱うApplicationは、例外構成で受けるのではなく
Service Scope外とした。部門長が判断し、より大規模なApplicationを扱う別部門への相談を
案内して断るというRoutingは伝聞である。

Application自体はTwo Way Doorでも、実装開始後のTeam持ち替えが難しいため、実装Teamへの
割り振りはOne Way Doorとされた。受付は固定Formの二条件Checkだけでなく、Business要求から
必要な仕掛けを解釈して受入またはScope外を判断する流動的な対話だった。

現在はEnterprise情報のDigital化が制約され、AIが部門Scope、Capability、Riskおよび他部門の
受入条件を判断するContextを持たないため、AIへ最終的な受入、拒否またはRoutingを任せない。
AI Nativeな将来には可能性があるが、現在は要求整理または判断材料の下書きへ限定し、部門長が
最終判断を保持する。

## Hypothesisへの射程

`HYP-20260804-013223-outcome-first-ai-resource-allocation`のU1に対し、重いOne Way Door Caseとは
異なる小規模ApplicationのContextでも、Outcome起点はAIによる個別基盤選定の高速化ではなく、
部門Missionに適合する標準Path、Service Scope、Admission Control、Scope外Routingおよび
現在のAI Contextに応じた責任境界を選んだ。

個々の開発者に選定Capabilityを与える代わりに、標準を設計・維持するCapabilityと、
実装開始前に受入またはScope外を判断するCapabilityを上流へ置いた。この対照Caseは、
Value Streamの課題とOutcomeから始めると、AIまたはTool起点とは異なるCapability、責任境界
および棄却・Routing判断を選べるというU1を、現在の範囲で`supports`する直接Evidenceとなる。

## 代替説明

- 判断差はOutcome起点の効果ではなく、既存の部門標準と組織分業から生じた可能性
- AIまたはTool起点でも、既存標準を参照すれば同じ標準PathとRoutingへ到達する可能性
- 標準構成が既に存在するため個別選定が不要なだけで、新しいDomainでは同じ結果にならない
- Application規模またはDataの重大性以外にも、確認されていない受付条件がある可能性

## 曖昧さと限界

- 一人の実践者による一つのCase説明で、部門資料、受付記録または関係者本人の回答を
  確認していない。
- Scope外判断後のRoutingは伝聞であり、実際のRouting先または結果を確認していない。
- Application件数、標準Pathの成功率、作り直しCost、Team持ち替えCostまたは実Outcomeを
  確認していない。
- AI Routingは現在も将来も実装比較しておらず、必要なEnterprise Contextを定義していない。
- U1の結果からU3、U4、Feature Hypothesisまたは親Value Hypothesisを支持しない。

## 公開安全性確認

- checked_at: 2026-08-11T12:03:41+09:00
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
