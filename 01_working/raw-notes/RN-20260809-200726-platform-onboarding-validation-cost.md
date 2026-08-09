---
id: RN-20260809-200726-platform-onboarding-validation-cost
type: raw_note
title: "共通PlatformのMetric検証とOnboarding再設計Cost"
content_language: ja
created_at: 2026-08-09T20:07:26+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-09T20:10:26+09:00
sanitization_checked_by: agent:codex
tags: [case-recollection, cost-benefit, expected-signal, itsm, metrics, onboarding, platform-service, validation-cost]
---

# 共通PlatformのMetric検証とOnboarding再設計Cost

## この記録の位置づけ

`RN-20260809-185044-value-metric-shortened-platform-onboarding`に記録した過去Caseについて、
価値選択と検証のCost、再設計・実装Cost、Lead Time、再利用および見送った開発Scopeを
追加確認した対話を保存する。

公開されている別の事例情報との組み合わせで組織、Service、顧客または関係者を再識別
できないよう、固有名、企業形態、顧客属性および正確なCase件数は保存しない。当時の
作業記録、Calendar、設計資料、Source Code、Interview記録、Onboarding記録または
Feedback原文は、この対話では確認していない。

## 価値選択と検証に使ったCost

- 新しいMetricの作成:
  実践者一人で約2時間
- Stakeholder Interview:
  現場に近い役割とPlatform側の役割を含む複数名へ、既存Meetingの一部を一人あたり
  約5分使って確認した。Concept確認とは別に行った
- 新しいMetricに適したOnboarding Conceptの確認:
  実践者と取りまとめ役の二人で約30分
- 進捗共有:
  実践者が取りまとめ役へ、必要に応じて約5分の口頭報告を行った
- 現場へ当てるまでのLead Time:
  週次Meetingの機会を待つため、約1週間の待ちが発生した。これは実作業ではない

## 再設計・実装に使ったCost

Onboarding Flowと体験の設計、実際の資材作成およびData Import Toolの開発に、実践者
一人で約2週間の実作業を使った。これは価値選択と検証そのものではなく、確認結果を受けて
選んだOnboarding Serviceを実装する介入Costである。

実践者の当時の見積もりでは、当初案の方が追加ScriptとMetric実装を多く必要とした。
再設計後のTool実装は、当初案で想定した開発Scopeの一部に収まった。ただし、当初案は
実装していないため、この差は実測比較ではない。

## 実装Scopeの限定

当初案で予定していた追加ScriptとMetricの一部を見送った。再設計後は、処理開始から
完了までの経過時間と、Service Levelの目標を満たしたかを確認できる最小限のMetricへ
Scopeを絞った。

それ以上のMetricまたは機能が必要であれば、Onboarding後にNeedを確認して追加実装する方針を
利用者へ伝えた。観測した複数Caseでは追加Needが表明されず、追加ScriptまたはMetricを
実装しなかった。Needが表明されなかったことだけから、潜在的なNeedが存在しなかったとは
断定しない。

## 再利用とFeedback

再設計したFlow、資材およびImport Toolは、複数のOnboarding Caseで追加修正または
個別開発なしに共通利用した。一部の利用者からは、分かりやすさと簡便さについて肯定的な
Feedbackがあった。

このFeedbackは限定された利用者の自己申告であり、全利用者の評価、作業時間、Data品質、
分析効果または長期的なValueを示すものではない。

## この記録だけでは分からないこと

- Stakeholderの選定方法、全回答、異なる意見および発言原文
- Metric作成、Interview、Concept確認、進捗共有および再設計の正確なProcess Time
- 当初案を実装・利用した場合の開発、Onboarding、入力、説明、検討および手戻りの実Cost
- 再設計によって見送った分析CapabilityのValue
- 追加Needが表明されなかった理由と、Feedback経路の十分性
- 再設計したFlow、資材およびToolの長期的な維持Cost
- AIによる候補生成の高速化がある場合にも、同じCost妥当性が成立するか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
