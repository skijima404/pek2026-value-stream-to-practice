---
id: EXT-20260731-113601-mbpm-open-practice-library
type: external_input
title: "Open Practice Library「Metrics Based Process Mapping」"
content_language: ja
created_at: 2026-07-31T11:36:01+09:00
created_by: agent:codex
source_type: official_webpage
source_url: https://openpracticelibrary.com/practice/metrics-based-process-mapping/
retrieved_at: 2026-07-31T11:36:01+09:00
retrieval_method: official_webpage_inspection
provided_by: human:kijima
changeability: externally_managed
publication_date: 2020-08-03
license: CC-BY-4.0
asset_in_repository: false
tracking_parameters_removed: false
---

# Open Practice Library「Metrics Based Process Mapping」

## 位置づけ

Open Practice Libraryが公開するMetrics Based Process Mapping（MBPM）の
説明ページを、用語と手法の外部参照として保存する。

本ノードは、外部ページに書かれている内容を後から確認できるようにするための
External Inputである。MBPMを今回のセッションで採用する決定や、MBPMによって
特定の仮説が検証済みであることを示すものではない。

## 外部ページが説明していること

同ページはMBPMを、具体的なProcess Step、担当Actor、主要な時間および
品質Metricを記録する、詳細なProcess MappingのPracticeとして説明している。

各Process Stepには、必要に応じて次のMetricを記録する。

- Resources:
  Stepの完了に必要な人数などのResource量
- Process Time:
  実際に作業を行う時間
- Lead Time:
  作業が利用可能になってから完了し、次のStepへ渡されるまでの経過時間
- `% Complete & Accurate`:
  下流の利用者が、受け取った仕事を訂正、追加、確認せずに実行できる割合

Process Stepを担当Actorへ対応づけるため、実務上はActorまたはRoleごとの
Swimlaneを持つ詳細Process Mapとして表現できる。

## Value Stream Mappingとの関係

同ページは、MBPMをValue Stream Mappingと組み合わせて使用できるとしている。
その場合、MBPMは、Strategy LevelのValue Stream Mapに含まれる一つのSegmentを、
Implementation Levelで詳細化する。一つ以上のMBPMが、上位のValue Streamの
各Segmentへ対応する場合もある。

そのため、次の表現は登壇時の短い説明候補としては利用できる。

> MBPMは、VSMの一部分を担当RoleのSwimlaneとMetricまで詳細化したもの。

ただし、「VSMをSwimlaneへ分解したもの」は理解のための短縮表現であり、
外部ページに記載されたMBPMの定義そのものではない。

## Current StateとFuture State

同ページでは、MBPMによってCurrent State Mapを作成した後、
実装対象となるFuture State Mapを設計するとしている。

Processを共同で可視化し、Baselineとなる時間、Resource、品質を記録することで、
AutomationまたはProcess改善の前後を比較し、改善によって得られたValueを
測定できるとしている。

## 出典と帰属

- Practice名: Metrics Based Process Mapping (MBPM)
- Contributor: Matt Takane、Blake Douglas
- 公開日: 2020年8月3日
- 発行元: Open Practice Library
- 公式ページ:
  https://openpracticelibrary.com/practice/metrics-based-process-mapping/
- License:
  Creative Commons Attribution 4.0 International

## 限界

- Open Practice Libraryは外部管理されており、ページ内容は変更される可能性がある。
- 本ノードは2026年7月31日に確認できた説明を要約したものであり、
  MBPMに関するすべての流派や文献を網羅しない。
- MBPMの有効性、今回のセッションとの適合、測定値の信頼性は、
  この外部ページの存在だけでは検証されない。
