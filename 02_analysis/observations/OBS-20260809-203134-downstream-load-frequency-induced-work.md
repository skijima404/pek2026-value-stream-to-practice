---
id: OBS-20260809-203134-downstream-load-frequency-induced-work
type: observation
title: "下流負荷を単発Cost・発生回数・誘発作業に分ける評価候補が記録された"
content_language: ja
created_at: 2026-08-09T20:31:34+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-09T20:42:37+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: high
knowledge_basis:
  - recorded_statement
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260809-194608-dvs-phase-quality-ai-outcomes
  - type: derived_from
    target: RN-20260806-224717-vsm-mbpm-process-analysis-explanation
---

# 観察

## 知識の成立根拠

`RN-20260809-194608-dvs-phase-quality-ai-outcomes`には、AI生成物のReview負荷を
一回の確認時間だけで評価せず、一回あたりの確認・修正時間、発生頻度、対象Resource数、
品質不足が誘発する差し戻し、再生成、再確認および後続の待ち時間を合わせて見る案が
記録されている。

`RN-20260806-224717-vsm-mbpm-process-analysis-explanation`には、Process Time、
Lead Time、待ちおよび手戻りを可視化し、桁の違う箇所を改善候補として扱うこと、
PTと複数人の総工数を区別することが記録されている。

二つの記録を、単発Cost、発生回数、対象Resourceおよび誘発作業という評価単位へ
まとめる部分は`reasoned_synthesis`である。

## 根拠箇所

- `RN-20260809-194608-dvs-phase-quality-ai-outcomes`の
  「VSM・MBPMで時間を見る意味」および「頻度とError Costによる違い」
- `RN-20260806-224717-vsm-mbpm-process-analysis-explanation`の
  「なぜVSMやMBPMを使うのか」、「VSMやMBPMの効果が限定的と思われる点」および
  「解決策のアイデアを出したら」

## 根拠から直接言えること

記録では、下流負荷の大きさを検討する候補として、次の構成が示されている。

```text
下流負荷の候補
= 一回あたりの処理Cost × 発生回数
  + 品質不足から誘発された手戻り・待ち・再作業
```

一回のReviewが長くても頻度または対象Resourceが少なければ、Value Stream全体では
主要な制約でない可能性がある。反対に、一回は短くても高頻度または多数のResourceで
繰り返され、再確認や問い合わせ待ちを誘発する場合、累積負荷が大きくなる可能性がある。

この整理は、Process Timeを無視するものではない。単発の時間短縮だけから改善Priorityを
決めず、発生回数、Resource、手戻り、待ちおよび後続作業まで観測範囲を広げる候補である。

## 曖昧さと限界

- 記載した式は確立済みのCost Model、会計式または実測結果ではなく、観測項目を
  欠落させないための評価候補である。
- 各項目の単位、重複計上の防止、対象期間、Resource数の扱いおよび金額換算は
  定義されていない。
- 誘発作業とAI Output品質との因果、AI以外のProcess制約、および観測対象外のActorを
  区別する必要がある。
- 必要なReview、法令対応、安全確認または統制を、負荷があるという理由だけで
  削除可能なムダとは扱わない。
- このObservationは、測定方法、改善Priorityまたは登壇内容の採用を意味しない。

## 公開安全性確認

- checked_at: 2026-08-09T20:42:37+09:00
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
