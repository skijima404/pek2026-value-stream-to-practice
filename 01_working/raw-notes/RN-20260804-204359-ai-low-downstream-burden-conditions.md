---
id: RN-20260804-204359-ai-low-downstream-burden-conditions
type: raw_note
title: "AI活用で下流負荷が生じにくい条件と段階的自動化"
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
tags: [ai-automation, contract-first, guardrails, handover, human-ai-collaboration, progressive-automation, workslop]
---

# メモ

2026年8月4日に、AIが下流負荷を生じやすい場合と生じにくい場合を比較した
Codex上の対話を記録する。以下は実務経験に基づく話と、対話中に生じた推測を
含んでおり、検証済みの一般則ではない。

## 比較的うまくいくと考えている条件

- 後続担当者へのHandoverがない。例えば、一つのPrompt内で完結するRole Playの
  Simulationなど
- 手順が確立されており、解釈の余地が小さい
- 目的が明確で、構造が単純である
- 多少の揺れを許容できる。揺れを許容できない部分は、AI以外の方法も使って
  仕組みとして固定されている
- 人間が必ずOutputを検証する。Personal Assistantのように人間との対話を
  基本とする場合、対話中に違和感を修正する工程を差し込めるため、大きな
  意思決定まで未修正のずれを持ち越しにくい

ここで「Slopになりにくい」とは、AIが不適切なOutputを生成しないという意味に
限定しない。判断する人間との対話内で違和感を発見し、未検証の完成品として
後続へ渡る前に修正できるという意味も含む。

## 段階的な自動化

自動化の仕組みを作る場合、通常はいきなりEnd-to-Endで自動化しない。

1. 人力などで作業を行い、手順を確立する
2. 確立した手順の各部分を個別に自動化する
3. 自動化した部分を最後に接続する

AI活用でも同じ順序が必要ではないかと考えている。手順、例外、判断基準、
責任境界が未確立なまま全体を接続すると、曖昧さまで高速化し、後続の人間へ
確認、修正または再構築を移す可能性がある。

## Contract First

市民開発向けAI開発PlatformのDemo環境と、別途実施している対話型Repositoryの
取り組みでは、いずれもAPIでいう`Contract First`を設計原則として使っている。
先に目的、制約、入出力、責任境界および許容しない揺れを定め、その後で個々の
自動化と接続を行う考えである。

## AIで問題が拡大し得る理由についての推測

対話中、自動化に関する知見が十分でない利用者でも、AIによって一気に自動化し、
局所的に「楽」をしようとできることが一因かもしれない、という推測が出た。

これは個人の能力不足を確認した記録ではない。また、効率化を求めること自体を
問題視するものでもない。AIによって自動化の実装障壁が下がる一方、手順の分解、
例外処理、検証、観測、停止およびRollbackといった設計上必要な摩擦まで省略される
可能性がある、という未検証の解釈である。

## 事例と確認可能な資料

市民開発向けAI開発PlatformのDemoでは、環境ProvisioningとDemo環境が比較的
うまく機能したという実務上の説明がある。関連Repositoryはローカルに存在し、
手順、Script、Check、GitOpsおよびRollback資産を別途確認できる。

実践者の記録では、このPlatformについて、環境の構築部分を3回、Demo部分を
約10回実施している。Test段階を含めると、関連する実行は20回以上になる。
開発部分には多少の揺れがあった一方、GitOpsを通じたDeploymentでは問題が
発生しなかったと説明している。

同じ設計思想で作成した別の類似環境についても、構築とDemoを10回以上実施し、
問題は発生しなかったと説明している。

ただし、このRaw Noteだけでは、AIの有無による比較、工数削減、成功率、現在の
実環境の正常性または一般化可能性を確認していない。回数と結果は実践者による
振り返りであり、全実行のLog、同一条件、失敗判定基準および独立した確認結果を
保存したものではない。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
