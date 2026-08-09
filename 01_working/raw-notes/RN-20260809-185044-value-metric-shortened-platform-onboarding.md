---
id: RN-20260809-185044-value-metric-shortened-platform-onboarding
type: raw_note
title: "価値Metricの修正が共通PlatformのOnboarding作業を減らした事例"
content_language: ja
created_at: 2026-08-09T18:50:44+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-09T18:55:42+09:00
sanitization_checked_by: agent:codex
tags: [case-recollection, expected-signal, itsm, metrics, onboarding, platform-service, value-hypothesis]
---

# 価値Metricの修正が共通PlatformのOnboarding作業を減らした事例

## この記録の位置づけ

過去に社内向けの共通業務Platformを設計・提供した一事例について、当時の判断Ownerで
あった実践者が対話で振り返った内容を記録する。公開されている別の事例情報との組み合わせで
組織、Service、顧客または関係者を再識別できないよう、固有名、企業形態、顧客属性および
正確な件数は保存しない。当時の設計資料、Interview記録、入力資料、Onboarding記録または
提案資料は、この対話では確認していない。

## 当初のValueとOnboarding案

実践者は、共通業務Platformによる分析と効率化の効果を最大化することにValueを置いていた。
当初のOnboarding案は、多数回のMeetingと、利用組織が記入する複数の入力資料を必要とする
重いProcessだった。

利用候補組織の担当者へ当初案を示し、入力資料を実際に埋められるか確認したところ、担当者は
実行できるか分からないと回答した。実践者は説明時の様子も理解が難しい兆候と受け取ったが、
表情に基づく解釈と、明示的な回答は分けて扱う。

## Stakeholder確認とMetricの修正

実践者は複数の関係者へ、共通業務Platformに期待するValueを確認した。その結果、分析・
効率化の効果を最初から最大化することよりも、Onboardingを短くし、早く利用開始できることが
重視されると判断した。

実践者は最終判断Ownerとして、重視するMetricを分析・効率化中心からOnboardingの時間と
利用者負荷へ修正し、Onboarding Serviceを再設計した。多数回のMeetingを、入力方法の説明と
動作確認・Demonstrationを行う少数回のMeetingへ減らし、複数の入力資料を単一の入力へ
まとめた。

## 再設計後の実施

再設計後の方式は、少数の実Onboarding Caseで使用した。これらのCaseでは、入力方法の説明と
動作確認・Demonstrationという設計した少数回のMeeting内でOnboardingが完了した。

当初案は実運用していない。実践者は当時の作業分解から、当初案ではMeetingだけでも
再設計後の倍を超え、利用組織の担当者とその先の利用者が行う作業はさらに大きくなると
見積もっている。入力資料ごとに、その背景、得られることおよび記入方法を説明し、利用側でも
説明された事象を検討する必要があったためである。この差は実測比較ではなく反実仮想の
見積もりである。

## 後から得たContext

実践者は後に、Onboardingに必要な工数が、利用組織への提案時に見える導入負荷へ反映され、
Serviceの競争力にも関係することを知った。これは事前に設定した期待Signalではなく、
後から得たContextとして扱う。

## この記録だけでは分からないこと

- 当初案を実運用した場合の実際のMeeting、入力、説明、検討および手戻りのCost
- 再設計後の各Caseにおける参加人数、Process Time、Lead Timeおよび利用者評価
- Stakeholderの選定方法、回答範囲および異なる意見
- Metric修正、Stakeholder Interview、入力統合または説明方法のどれが結果へ寄与したか
- 分析・効率化の効果を最大化するという当初Valueを、再設計によってどの程度失ったか
- AIによる候補生成の高速化がある場合にも、同じMechanismと効果が成立するか
- 提案時の競争力に関する後から得た説明を確認できる一次資料

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
