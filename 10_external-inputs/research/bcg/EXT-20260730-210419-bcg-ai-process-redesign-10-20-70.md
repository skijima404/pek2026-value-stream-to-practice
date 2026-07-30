---
id: EXT-20260730-210419-bcg-ai-process-redesign-10-20-70
type: external_input
title: "BCG「Scaling AI Requires New Processes, Not Just New Tools」"
content_language: ja
created_at: 2026-07-30T21:04:19+09:00
created_by: agent:codex
source_type: user_provided_generated_pdf_and_official_webpage
original_filename: scaling-ai-requires-new-processes-not-just-new-tools.pdf
source_url: https://www.bcg.com/publications/2026/scaling-ai-requires-new-processes-not-just-new-tools
source_pdf_url: https://web-assets.bcg.com/pdf-src/prod-live/scaling-ai-requires-new-processes-not-just-new-tools.pdf
generation_source_url: https://www.bcg.com/publications/2026/scaling-ai-requires-new-processes-not-just-new-tools
retrieved_at: 2026-07-30T21:04:19+09:00
retrieval_method: user_generated_pdf_from_official_webpage_and_official_webpage
provided_by: human:kijima
changeability: externally_managed
publication_date: 2026-01-20
input_sha256: 1bbcef59a85daf32dfad2f2b80bd1f4a9cf9d2063520dc630e535dbb44a34b2a
tracking_parameters_removed: true
license: all_rights_reserved
asset_in_repository: false
asset_omission_reason: redistribution_not_authorized
relations:
  - type: references
    target: EXT-20260730-210820-bcg-leaders-guide-ai-transformation
  - type: references
    target: EXT-20260730-210821-bcg-wheres-value-ai-report
---

# BCG「Scaling AI Requires New Processes, Not Just New Tools」

## 位置づけ

Boston Consulting Groupが2026年1月20日に公開した、AI Agentを大規模に
導入する際のプロセス再設計、組織変革、PlatformとProductの役割分担を扱う
外部資料。

本ノードは、この資料が述べている内容を後から参照できるようにするための
External Inputである。ここに記録した主張はBCGの見解であり、このRepoの
結論や、セッション内の仮説が実証済みであることを意味しない。

## 書誌情報

- 著者: Eric Jesse、Zeeshan Shah、Rajeev Singh
- 発行元: Boston Consulting Group
- 公開日: 2026年1月20日
- 提供されたPDF: 8ページ、A4、2,856,668 bytes
- 提供されたPDFの生成元: 公式記事ページのReport生成機能
- 公式記事:
  https://www.bcg.com/publications/2026/scaling-ai-requires-new-processes-not-just-new-tools
- 公式PDF:
  https://web-assets.bcg.com/pdf-src/prod-live/scaling-ai-requires-new-processes-not-just-new-tools.pdf

## 提供されたPDFの由来

提供者によると、PDFは公式記事ページからReportを生成する機能を使って
取得したものである。

提供されたURLには広告CampaignおよびClick計測用のQuery Parameterが
含まれていたため、本ノードでは同一記事のCanonical URLだけを保存する。

提供されたPDFと公式記事は、Title、著者、公開日、本文、ページ内の
著作権表示が対応している。公式サイトが公開する静的PDF URLと、提供された
生成済みPDFのバイト同一性は確認していない。提供ファイルの同一性確認には、
本ノードの`input_sha256`を使用する。

## 10/20/70について資料が述べていること

PDF 6ページの「How to Meet the Change Management Challenge」で、
BCGは複数業界のAI Transformationを通じて確立したリソース配分の指針として
10/20/70を提示している。

- 10%: Algorithmに関する取り組み
- 20%: TechnologyとDataに関する取り組み
- 70%: 変化を定着させるためのPeopleとProcessに関する取り組み

同じ節では、個別工程の自動化に留まらず、価値を生む工程全体を対象に
End-to-End Processを再設計すること、確認や反復的なReviewを減らすこと、
組織構造、管理範囲、必要Skillも変化することが述べられている。

## Platform Engineeringとの接点として資料に書かれていること

PDF 4ページでは、共通のMemory、Orchestration、Tool Registry、Governanceを
提供するAgentic Platformと、特定の能力やOutcomeを提供するAI Agent Productを
分けて説明している。

PDF 7ページでは、Platform Teamは共通のModular Infrastructureを所有し、
Product Teamは特定領域のProblemを解決するAI Agentを設計・改善するとしている。
Product Teamには、FeatureだけでなくOutcomeを定義できるBusiness Process
Ownerを含めるべきだとも述べている。

これらは、この資料がPlatform TeamとProduct Teamについて述べている内容の
記録であり、その役割分担をこのRepoで採用したことを示すものではない。

## 混同しないもの

PDF 3ページには、ある企業がRFQを次の割合で処理することを目標にした事例が
ある。

- 約70%: 人間の介入なし
- 約20%: AI Agentと人間が協働
- 約10%: AI Agentの支援を受けながら人間が集中的に対応

これは特定事例におけるRFQ処理の配分であり、PDF 6ページの
10/20/70リソース配分原則とは別の記述である。

## 限界

- この資料はBCGの論考であり、10/20/70の導出に使った調査設計、対象数、
  分析方法は本文中に示されていない。
- 10/20/70は厳密な普遍法則としてではなく、BCGが提示するGuiding Principle
  として扱う。
- 資料内の企業事例について、企業名、測定方法、比較条件、第三者による検証は
  本文から確認できない。
- 公式ページとPDFは発行元により変更または公開終了される可能性がある。

## PDF本体をRepoへ格納しない理由

PDF 8ページにはBoston Consulting Groupの著作権表示と
`All rights reserved`の記載があり、転載には許諾が必要とされている。
再配布許諾を確認できなかったため、提供されたPDF本体はRepoへ複製せず、
公式URLと提供ファイルのSHA-256を記録する。
