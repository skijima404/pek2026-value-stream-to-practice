---
id: EXT-20260804-144101-betterup-workslop-recipient-experience
type: external_input
title: "BetterUp Workslop調査：受け手の負荷と信頼への影響"
content_language: ja
created_at: 2026-08-04T14:41:01+09:00
created_by: agent:codex
source_type: official_research_article
source_url: https://www.betterup.com/blog/hidden-costs-workslop
companion_url: https://www.betterup.com/workslop
retrieved_at: 2026-08-04T14:41:01+09:00
retrieval_method: official_webpage_inspection
provided_by: human:kijima
changeability: externally_managed
publication_date: 2025-09-29
license: all-rights-reserved
asset_in_repository: false
tracking_parameters_removed: true
---

# BetterUp Workslop調査：受け手の負荷と信頼への影響

## 位置づけ

BetterUpとStanford Social Media LabによるWorkslop調査を、AI生成物を受け取った
人の体験に焦点を当てた外部参照として保存する。

BetterUpはWorkslopを、完成しているように見える一方で、役に立たない、品質が低い、
または目的から外れたAI生成Contentとして説明している。調査ページは、生成物単体の
品質だけでなく、受け手に生じる修正、解釈、確認、関係性への影響を扱っている。

本ノードはBetterUpが公表した調査結果と説明の存在を記録するExternal Inputであり、
数値の一般化可能性、因果関係、Platform Engineeringへの適用可能性を保証しない。

## 公式ページで確認した調査結果

BetterUp Blog本文は、2025年9月に米国のFull-time Desk Workerを対象として実施した
調査について、次の結果を掲載している。

- 40%が、直近1か月にWorkslopを受け取ったと認識している
- 受け取る仕事の平均15.4%がAI Workslopであると回答者が推定している
- Managerでは54%、Individual Contributorでは38.5%がWorkslopを受け取ったと回答した
- 53%が、自分が送った仕事の少なくとも一部もWorkslopかもしれないと認めている
- 1件を処理するために平均1時間51分を要したと報告されている
- 受け手の感情として、Annoyed 54%、Frustrated 46%、Confused 38%、Offended 22%が
  掲載されている
- 受け手の約半数が、送信者を以前よりCreative、Capable、Reliableではないと評価し、
  42%がTrustworthyではないと評価したと説明されている

これらは回答者による認識、自己申告、推定を集計した結果である。AI生成物の品質を
第三者が判定した割合や、Workslopが負荷や信頼低下を引き起こした因果効果を直接測定
した値としては扱わない。

## 受け手の体験として読める範囲

公式Research Pageは、Workslopを受け取った同僚に実質的な思考と後処理が残ること、
個人には混乱や不満、Teamには重複作業と信頼低下、組織には時間損失と見かけ上の
生産性が生じると説明している。

したがって本Sourceは、AI Slopを生成物の外観や正誤だけでなく、受け手側に残された
仕事と関係性への影響から検討する材料になる。また公式ページ自身が、Contextと
Accountabilityを失ったAI WorkがWorkslopを広げるという説明を置いている。

## 標本数の不整合

2026年8月4日の確認時点で、同じBetterUpの公開ページ内に次の不整合がある。

- Blog本文: 1,004人
- Blog内Infographicの注記: 1,150人
- BetterUp Labsの専用Research Page: 1,150人

このため、1,004人を特定の4指標の標本数として引用する場合はBlog本文に依拠した
ことを明示する。調査全体の標本数を断定する場合は、原調査資料または著者による
訂正を追加確認する必要がある。

## 出典

- BetterUp Blog:
  The hidden cost of AI “workslop” — and how leaders can fix it
- Author:
  Marielle Leon
- Published:
  2025-09-29
- URL:
  https://www.betterup.com/blog/hidden-costs-workslop
- BetterUp Labs Research Page:
  Workslop is the new busywork. And it’s costing millions.
- URL:
  https://www.betterup.com/workslop
- Research partnership:
  BetterUp / Stanford Social Media Lab

## 限界

- 調査対象は米国のFull-time Desk Workerであり、Platform Engineering従事者や
  日本企業を対象とした調査ではない。
- Workslopの受領、割合、負荷、感情は回答者の自己申告または推定である。
- BetterUpは調査主体であると同時にCommercial Serviceの提供者でもある。
- 公開ページ内で標本数が一致していない。
- 「Workslopという名称は責任をAIから人間へ戻す意図で選ばれた」という解釈は、
  公式ページで確認した著者の明示的な命名理由ではない。
- 本Sourceだけでは、Platform Serviceにおける具体的な原因や対策の有効性を検証できない。
