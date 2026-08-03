---
id: OBS-20260804-004532-journey-before-vsm-mbpm
type: observation
title: "前回登壇で対象Journeyを特定し今回VSM・MBPMへ展開する前後関係が記録された"
content_language: ja
created_at: 2026-08-04T00:45:32+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-04T00:53:33+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: high
relations:
  - type: derived_from
    target: RN-20260803-000910-vsm-mbpm-timing-and-previous-talk-sequence
  - type: derived_from
    target: EXT-20260803-002840-previous-platform-engineering-talk
---

# 観察

## 根拠箇所

- `RN-20260803-000910-vsm-mbpm-timing-and-previous-talk-sequence` の
  「このメモの用途」「今回採用する作成順序」
- `EXT-20260803-002840-previous-platform-engineering-talk` の
  「資料内で確認できる構成」「前回と今回の境界」
  「VSM・MBPMの作成タイミングとの関係」

## 根拠から直接言えること

前回登壇の資料には、Platform TeamのVisionを作り、利用者のProblemと期待Valueを
明確にし、Platform ServiceのScopeと、価値を届ける対象Journeyを特定する内容が
記録されている。

提供された前回登壇PDFからは、そのJourneyをVSMまたはMBPMへ展開し、Actor間の
Process Time、Lead Time、手戻りを観測するところまでは明示的に確認されなかった。

作成者は今回のアプローチについて、前回登壇でTeamのVisionと対象Journeyを
特定した後、そのJourneyごとにVSMまたはMBPMを作成する順序を採ると記録している。
この順序では、JourneyのCurrent StateをActorとProcessへ分解し、Problem、
Value Hypothesis、施策対象、施策後の変化を観測可能にする。

作成者は、Journeyに特化せずMapを作る場合、Caseの違いが混在して課題を抽出しにくく、
Lead Time、Process Time、手戻り率が実態を反映しにくくなるため、IdeaのPriorityを
効果の大きさから判断しにくくなるという懸念も記録している。

## 曖昧さと限界

- 前回登壇で確認できた範囲は、提供されたPDFに記載された内容である。登壇時の
  口頭説明をすべて保存または否定するものではない。
- Journeyを先に特定する順序は、今回の登壇で採る前後関係として記録されたもので、
  VSMまたはMBPM一般に唯一の作成順序を定めない。
- Journeyに特化しないMapで課題抽出、Metric記録、Priority判断が難しくなるという
  記述は作成者の見立てであり、比較結果は保存されていない。
- このObservationはSession Story、Slide、Speaker Notesへの採用を意味しない。

## 公開安全性確認

- checked_at: 2026-08-04T00:53:33+09:00
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
