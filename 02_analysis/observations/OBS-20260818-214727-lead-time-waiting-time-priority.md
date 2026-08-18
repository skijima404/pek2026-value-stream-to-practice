---
id: OBS-20260818-214727-lead-time-waiting-time-priority
type: observation
title: "Lead Timeの支配項が待ち時間ならProcess Time短縮の全体効果は限定されると整理された"
content_language: ja
created_at: 2026-08-18T21:47:27+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-18T21:55:39+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: high
knowledge_basis:
  - recorded_statement
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260818-204555-lead-time-waiting-time-flow-efficiency
  - type: references
    target: EXT-20260731-113601-mbpm-open-practice-library
  - type: references
    target: OBS-20260804-013222-necessary-friction-boundary
  - type: references
    target: HYP-20260809-203135-quality-first-ai-allocation-workflow
---

# 観察

## 知識の成立根拠

`RN-20260818-204555-lead-time-waiting-time-flow-efficiency`に記録された、
Process TimeとWaiting Timeを分けてLead Time改善を考える説明用モデルを
`recorded_statement`として抽出した。

仮定上の時間を比較し、Lead Timeの大部分を占める要素によって改善Priorityが
変わるという関係へ整理する部分は`reasoned_synthesis`である。特定組織の実測、
改善前後の比較または因果効果を確認した記録ではない。

## 根拠箇所

- `RN-20260818-204555-lead-time-waiting-time-flow-efficiency`の
  「図に置いたプロセス」「この図で表現したかったこと」
- 同Raw Noteの「フロー効率」「VSMとMBPM上での扱い」
- 同Raw Noteの「AIとPlatform Engineeringへの接続」

## 根拠から直接言えること

記録された説明用モデルでは、六つの工程に各1時間のProcess Timeを置き、工程間の
着手待ちを合計7週間としている。この仮定では、実作業の合計6時間に対し、利用者が
経験するLead Timeの大部分をWaiting Timeが占める。

このような構造では、一つの工程を1時間から50分へ短縮しても、7週間の着手待ちは
残るため、Value Stream全体のLead Timeに対する効果は小さいと説明されている。
改善対象を決める前に、Process TimeとWaiting Timeを分け、仕事がどこで留まって
いるかを確認する考えが記録された。

また、必要なRisk評価、意思決定または安全確認を実行している時間はProcess Time、
担当者が着手するまでの滞留はWaiting TimeまたはQueueとして区別されている。
したがって、待ち時間の削減は必要な判断を省略することではなく、Queue、優先順位、
Batch、役割分担またはHandover条件を調べる入口として位置づけられている。

AIまたはPlatform Serviceについても、個別作業を高速化できることだけで配置を決めず、
その作業がLead Timeのどの程度を占めるか、Waiting Timeの原因を変えられるかを確認する
必要があるという説明が記録された。

## 既存Analysisとの関係

`OBS-20260804-013222-necessary-friction-boundary`は、品質、学習、Accountabilityまたは
安全性のために残す摩擦と、削減対象となる負荷を分ける境界を扱う。本Observationは、
必要な判断の実行時間と、その判断が始まるまでのQueueを時間構造として分ける。

`HYP-20260809-203135-quality-first-ai-allocation-workflow`のU3が扱う、局所速度以外の
観測項目を選ぶための説明候補にはなる。ただし、仮定値を用いた概念モデルであり、
U3の検証結果またはEvidence Coverageを更新するEvidenceにはしない。

## 曖昧さと限界

- 6時間、7週間および約2%という値は説明用の仮定で、特定Processの実測値ではない。
- すべてのProcessでWaiting Timeが支配的とは限らず、Process Time短縮が主要な改善に
  なるContextもある。
- Process TimeのすべてがValue-adding Timeとは限らず、厳密なFlow Efficiencyでは
  分子と分母の定義が必要である。
- 必要な統制と不要なQueueの境界、Waiting Timeの原因および変更可能性は、対象
  Value Streamで確認する必要がある。
- このObservationは、改善方法、AI配置または登壇説明の採用を意味しない。

## 公開安全性確認

- checked_at: 2026-08-18T21:55:39+09:00
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
