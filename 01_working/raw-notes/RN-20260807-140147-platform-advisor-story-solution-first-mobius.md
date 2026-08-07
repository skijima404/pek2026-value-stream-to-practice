---
id: RN-20260807-140147-platform-advisor-story-solution-first-mobius
type: raw_note
title: "Platform Advisor物語内のSolution-first再構成とMobius 3区分"
content_language: ja
created_at: 2026-08-07T14:01:47+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-07T14:55:30+09:00
sanitization_checked_by: agent:codex
tags: [platform-advisor, solution-first, mobius, problem-hypothesis, value-hypothesis, solution-hypothesis, feature-hypothesis, fictional-scenario]
---

# メモ

以下はPlatform Advisorの通し事例で使用する物語内の出来事であり、実在する組織の分析、検証またはEvidenceではない。

Platform TeamはVSMとMBPMを作成した後、すでに思いついていたSolution候補からProblemとValueを遡るSolution-firstのアプローチで仮説を整理した。

## Discovery

### Problem Hypothesis

> 利用者は、設計初期やPlatform選定時の情報探索と解釈に時間を使っている。

システム構想時にインフラを選定する担当者は、必要な情報が分散しているため、情報探索、Platform Teamへの問い合わせ、比較観点の整理に時間を要している。対象工程にはPT 17h、LT 59hのAddressable Costがあり、情報収集と問い合わせでは40%および50%の手戻りが発生している。

Platform Teamは、VSMで情報探索と問い合わせの摩擦を確認できたため、Problem Hypothesisについて追加検証は不要と判断した。

### Value Hypothesis

> 探索と判断準備の負荷を下げると、判断待ちや差し戻しを減らせる。

Platform Teamは、情報探索と判断準備の負荷を減らせれば、利用者が自分のContextに適したPlatformを短時間で選び、判断根拠を説明して、安全に次の作業へ進めると考えた。

このValue Hypothesisについて独立した検証は行わず、Platform TeamはSolution Optionの比較へ進んだ。

## Decision

### Solution Option

Platform Teamは、同じProblemとValueに対するSolution Optionとして次を挙げた。

- FAQの作成
- Platformの選び方Flowchart
- 比較検討資料Template
- 質問の多い内容を中心としたDocument拡充
- Platform Advisor

### Solution Hypothesis

> 利用者のContextに応じて対話的に候補、適用条件、判断材料を提示するPlatform Advisorは、静的なFAQやFlowchartより、情報探索と比較判断の負荷を減らせる。

Platform Teamは、過去にPlatformを採用したTeamを対象に、同じPlatform選択Scenarioを使ってFAQまたはDocument拡充、選び方Flowchart、およびPlatform Advisorの会話Prototypeを比較した。

比較では次のSignalを確認した。

- 標準Pathへ正しく到達できたか
- 判断に必要な時間
- 判断根拠を説明できたか
- Platform Teamへの追加質問数
- 利用者が次の作業へ進めると感じたか

Platform Advisorは、利用者のContextに応じた質問を返せるため、FAQやFlowchartより短時間で候補の標準Pathへ到達し、参加者からも最も高い評価を得た。Platform Teamはこの結果を受け、Platform Advisorの開発を選択した。

## Delivery

### Feature Hypothesis

> 情報探索、不明点への回答、比較観点整理を一つのChatで提供すれば、対象工程のPTとLTを短縮でき、Project Owner Review、利用方法詳細調査、環境払い出し後の手戻りや追加負荷を増やさない。

最初のFeatureでは、Platform選択VSMの次の範囲をChatで提供する。

- 利用可能なインフラの情報探索
- 不明点への回答
- Platform候補と適用条件の提示
- 比較観点の整理

Project Ownerとの合意形成、利用方法詳細調査、環境払い出しおよび利用開始後の作業は、最初のFeatureの代替対象に含めない。

Platform Teamは、導入後に対象工程のPTとLTをBaselineと比較する計画を置いた。また、上流で短縮したCostが下流へ移っていないことを確認するため、Project Owner Review、利用方法詳細調査、および環境払い出し後の手戻りや追加負荷をQuality Guardrailとして観測する計画を置いた。

効果仮説と下流の観測設計は、次のRaw Noteに記録されている。

- `RN-20260806-212832-platform-advisor-vsm-effect-hypothesis`
- `RN-20260806-213822-platform-advisor-downstream-ai-slop-signals`


## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
