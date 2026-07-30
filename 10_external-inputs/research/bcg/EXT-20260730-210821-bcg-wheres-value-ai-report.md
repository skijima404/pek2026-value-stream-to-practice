---
id: EXT-20260730-210821-bcg-wheres-value-ai-report
type: external_input
title: "BCG Report「Where’s the Value in AI?」"
content_language: ja
created_at: 2026-07-30T21:08:21+09:00
created_by: agent:codex
source_type: official_report
source_url: https://www.bcg.com/publications/2024/wheres-value-in-ai
source_pdf_url: https://web-assets.bcg.com/a5/37/be4ddf26420e95aa7107a35aae8d/bcg-wheres-the-value-in-ai.pdf
retrieved_at: 2026-07-30T21:08:21+09:00
retrieval_method: official_webpage_and_linked_report
provided_by: agent:codex
changeability: externally_managed
publication_date: 2024-10-24
license: all_rights_reserved
asset_in_repository: false
asset_omission_reason: redistribution_not_authorized
---

# BCG Report「Where’s the Value in AI?」

## 位置づけ

Boston Consulting Groupが2024年10月24日に公開した、AIから価値を得ている
企業の特徴、価値の発生領域、必要な能力を扱うReport。

「The Leader’s Guide to Transforming with AI」が参照する調査Reportであり、
10–20–70の背景にある調査方法と能力の相対的重要度を確認できる。

本ノードはReportの記載内容を保存するExternal Inputである。調査結果の
妥当性をこのRepoが独立に確認したものではない。

## 調査方法として記載されていること

Report 19ページのAppendixには、次の方法が記載されている。

- 1,000人のCxOおよびSenior Executiveを対象としたSelf-report Survey
- 対象地域はAsia、Europe、North Americaの59か国
- 10のIndustryを対象
- 30のEnterprise Foundational CapabilityについてAI Maturityを評価
- Sector別の10のOutcome Dimensionを評価
- 各Capabilityが、回答者の報告したAI Value Generationへどの程度寄与するかを
  統計的手法で重み付け

## 10–20–70に直接関係する記載

Report 5ページでは、AI LeaderはResourceをAlgorithmへ10%、
TechnologyとDataへ20%、PeopleとProcessへ70%配分するRuleに従うと
説明している。

Report 16ページのExhibit 6では、30のCapabilityについて、AIとGenAIの
Value Creatorである確率に対する相対的重要度を示している。

- Algorithmに分類されたCapabilityの合計: 8%
- Technologyに分類されたCapabilityの合計: 22%
- PeopleとProcessに分類されたCapabilityの合計: 70%

Exhibit上では、この実測値と並べてBCGの10–20–70 Modelを表示している。
10%と20%は、相対的重要度の8%と22%を丸めたModelとして読める。

同Exhibitの脚注では、AIとGenAIのValue Creatorを、AI施策から期待される
Cost SavingとRevenue Upliftの平均が5%以上である状態として定義し、
その確率に対してRegressionを行ったとしている。

## PeopleとProcessに含まれるCapability

Exhibit 6でPeopleとProcessに分類される項目には、次のものが含まれる。

- Change Management
- Product Development PipelineとCycle
- Emerging TechnologyのAdoption
- RoleとResponsibility
- Process Reimagination
- AI Talent
- Responsible AI Governance
- Risk-informed Culture
- AI ModelおよびImplementationのGuardrail
- Innovative Culture
- Data Governance
- Product/Platform Orientation
- AI Strategy

この分類では、単なる利用者教育だけでなく、Product Development、
Governance、Strategy、Process再設計まで70%側へ含まれている。

## Report内で表現が変わる点

Exhibit 6の統計的な記載は、AI Value Creatorである確率に対する
`Relative importance of capabilities`である。

一方、Report 5ページの説明では、同じ10–20–70をLeaderの
`resources`配分として表現している。

したがって、このReportから直接確認できるものには、少なくとも次の二つの
異なる表現がある。

1. Capabilityの相対的重要度を集計した8%・22%・70%
2. Resource配分のRuleとして丸めた10%・20%・70%

両者はReport内で関連づけられているが、相対的重要度がそのままBudget、
工数、人員の最適配分を意味することは、調査方法からは直接確認できない。

## 限界

- CapabilityとOutcomeは回答者によるSelf-reportを含む。
- Regressionが扱うValue Creatorの定義には、実現済みの価値だけでなく
  回答者が期待するCost SavingとRevenue Upliftが使われている。
- 相対的重要度はCapabilityとValue Creatorである確率の関連を表すものであり、
  因果関係や厳密な最適Resource配分を直接証明するものではない。
- Industry、企業規模、地域ごとの配分差は10–20–70へ反映されていない。
- PDFは再配布許諾を確認できないため、Repoには格納しない。
