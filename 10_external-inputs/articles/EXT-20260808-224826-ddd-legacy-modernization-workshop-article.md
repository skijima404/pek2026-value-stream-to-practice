---
id: EXT-20260808-224826-ddd-legacy-modernization-workshop-article
type: external_input
title: "レガシーモダナイゼーションのためのDDDワークショップ設計メモ"
content_language: ja
created_at: 2026-08-08T22:48:26+09:00
created_by: agent:codex
source_type: public_self_authored_article
source_url: https://note.com/skijima/n/n13533c4cdf48
retrieved_at: 2026-08-08T22:48:26+09:00
retrieval_method: public_webpage_inspection
provided_by: human:kijima
changeability: author_managed
publication_date: 2026-07-24
license: all-rights-reserved
asset_in_repository: false
tracking_parameters_removed: true
---

# レガシーモダナイゼーションのためのDDDワークショップ設計メモ

## 位置づけ

登壇者本人が2026年7月24日にnoteで公開した記事を、Legacy Systemで失われた要求、
Business Architecture、設計意図およびSystem BoundaryをDDD Workshopで復元・検証する方法が、
公開資料にどのように記録されているか確認するためのExternal Inputとして保存する。

## 公開ページで確認した内容

記事には、主に次の内容が記録されている。

- Legacy Systemでは、内部構造だけでなく、設計意図、Systemが支えるBusiness Architecture、
  およびBusiness ArchitectureからSystem設計へ至る要求仕様が失われ得るという問題設定
- Event Stormingを中心とするDDD Practiceを、要求仕様の復元・確認とDomain Modelingへ
  使用するWorkshop設計
- 現在も有効なBusiness Architectureに根拠を持つ要求と、過去の技術に由来する
  Legacy Constraintを区別する考え方
- System的な処理やEventを書いた後、その結果を人間がどう認識し、何を根拠に、
  どのような判断を行うかまで記述する条件
- Domain Expertが参加しない場合、既存SystemとIT側のKnowledgeから業務を復元し、
  Domain Expertによる確認が必要な箇所を分ける進め方
- System内部を知る参加者が現在の仕様を再生産する傾向へ対処するため、Systemを知らず、
  実装理由を問い直せる参加者またはFacilitatorを置く考え方
- 要求仕様からMicroservice Boundary案までのReasoning Chainを説明し、事実、仮説、
  不明点、Riskおよび後続の検証事項を分けるEnd State

本ノードは記事に記載された内容と公開時点を保存するものであり、記事の主張が一般に正しい、
Workshopが有効である、または対象Hypothesisが支持されたことを示さない。

## 今回の分析との関係

記事は、Business Use Case、Business Architectureまたは要求の根拠が失われ、現在のSystem
仕様と実装だけが残る場合に、人間の判断まで遡ってReasoning Chainを復元する方法の
自己資料として参照できる。

一方、Enterpriseの新規Scratch開発でBusiness Use Caseが失われる発生頻度、UX Designの
責務認識、Project構造との因果、Workshopの需要またはOutcomeは記事から確認していない。

## 出典

- Author: Sachiko Kijima
- Published: 2026-07-24
- Platform: note
- URL: https://note.com/skijima/n/n13533c4cdf48

## 限界

- 本人が公開した記事であり、独立した第三者研究ではない。
- 記事はLegacy Modernization向けWorkshopを扱い、新規Scratch開発全体の調査ではない。
- 公開記事に同じ方向の方法があることは確認できるが、Business Use Case喪失の原因、
  発生率、Workshopの効果または一般性を検証しない。
- 公開ページはAuthorによって更新される可能性がある。本ノードは2026年8月8日の
  確認範囲を要約したものである。
