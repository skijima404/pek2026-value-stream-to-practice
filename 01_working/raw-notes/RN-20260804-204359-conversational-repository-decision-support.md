---
id: RN-20260804-204359-conversational-repository-decision-support
type: raw_note
title: "対話型RepositoryによるEnterprise Architecture意思決定支援"
content_language: ja
created_at: 2026-08-04T20:43:59+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-04T20:54:05+09:00
sanitization_checked_by: agent:codex
tags: [contract-first, decision-support, enterprise-architecture, human-ai-collaboration, personal-assistant, practitioner-case]
---

# メモ

2026年8月4日に、対話型RepositoryをPersonal Assistantとして利用する
Enterprise Architectureの取り組みについて説明したCodex上の対話を記録する。
公開時の再識別Riskを避けるため、顧客、案件、組織、日付および内部Systemを
特定できる情報は保存していない。

## 取り組み

Enterprise Architectureの実務において、複数の支援先で類似したRepositoryを
作成し、運営している。Repositoryには、目的、制約、技術的な検討、判断材料、
未確定事項などを蓄積し、人間とAIの対話を通じて更新する。

AI Outputは、そのまま別の担当者へ完成品として渡すことを基本としない。判断する
人間が対話に参加し、違和感、前提のずれまたは不足を意思決定前に修正する。

## 計画変更時の事例

ある支援先で大きなSchedule変更が発生した際、蓄積したContextを使い、半日で
Schedule上の制約と技術的制約からFeasibilityを確認した。その上で3案の妥当性を
検討し、進め方の提案を作成した。

このRepositoryがなかった場合のOutput品質と所要時間は算出できない。ただし、
実践者本人は、同じ検討と提案を半日で行うことは困難だったと評価している。
この評価は比較実験または工数記録によって確認したものではない。

提案後の意思決定Outcome、各案の予測精度、後続作業量および長期的な効果は、
この対話では確認していない。

## Contract First

この取り組みでは、API設計における`Contract First`を設計原則として使っている。
大きな判断をAIへ一括して委ねるのではなく、目的、制約、前提、比較軸、
Accountabilityおよび確認方法を先に定め、そのContractの中で探索、比較、反証、
Feasibility確認および提案作成を行う。

実践者本人は、この経験が、本Repositoryの議論でContractの考え方を持ち出した
背景なのかもしれないと振り返っている。これは概念の由来を履歴資料で確認した
事実ではなく、本人による可能性の説明である。

## 位置づけ上の注意

- 複数の実務で使っているという説明はPractitionerの経験であり、成功率を示さない
- 半日の事例は、一次資料をこのRepositoryで確認していないCase recollectionである
- AIなしの比較対象がないため、短縮量や因果を定量化できない
- 人間が検証することは未検証Outputの下流流出を抑え得るが、Review Cost自体が
  小さいことを保証しない

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
