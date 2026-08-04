---
id: HYP-20260804-013226-two-stage-metrics-analysis
type: hypothesis_episode
title: "異常検知と原因診断を分ける運用はMetric過剰取得を抑え改善Loopを両立する"
content_language: ja
created_at: 2026-08-04T01:32:26+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: proposed
confidence: medium
knowledge_basis:
  - practitioner_experience
  - case_recollection
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260804-013225-itsm-metrics-analysis-practice
  - type: references
    target: OBS-20260802-230427-process-flow-and-outcome-quality
  - type: tests
    target: HYP-20260804-183210-ai-slop-downstream-burden-value
---

# 仮説

入力と定型Report作成をできるだけ自動化し、必要最小限のDashboardを定期的な
異常検知に、BI ToolまたはCustom Reportを原因診断に使い分ければ、一つの
Dashboardへ分析柔軟性を集約する場合より、改善Loopを回す頻度と、必要時に
原因を深掘りする柔軟性を両立しやすく、目的が明らかでないMetricの取得と維持を
減らしやすい。

ただし、この運用はDashboardまたはDataを置くだけでは成立しない。違和感から問いを
立て、適切な比較対象、分布、Segment、期間を選び、観測できたFactと解釈を分ける
分析Techniqueを担当者が習熟していることを成立条件とする。

## 知識の成立根拠

この方法は、作成者が約10年間、約3件のITSM Projectで再利用し、Project Portfolio
領域にも持ち込んだ実務経験に基づく。週次・月次運用、約20%のMetric改善、Project
Portfolioで機能したという結果は、一次記録をこのRepositoryで確認できないCaseの
記憶として扱う。

経験範囲は仮説の実務上の根拠であるが、他の方法との比較、改善の因果効果、分野を
またぐ一般的な再現性を独立検証したものではない。Platform Engineeringでは最近
利用を始めたばかりで、結果はまだ確認されていない。

また、DashboardとDataだけでFactを取り出せるわけではなく、分析Techniqueの習熟が
必要だという作成者の実務判断を前提に含む。

## Mobiusでの位置づけ

`solution`

Value StreamまたはProcessの変化を継続的に観測し、違和感を改善対象の発見へ戻す
ための運用方法に関するSolution Hypothesisである。

## 期待する兆候

- 手入力、データ加工、定型Report作成に必要な工数が減り、週次または月次の確認が
  継続される
- DashboardのMetric数を限定しても、重要な変化を検知できる
- 違和感を検知した時だけ、分布、推移、Journey等の切り口で原因を深掘りできる
- 検知から追加分析、改善判断、次回観測までのLoopが途切れない
- Dashboardの作り込み自体が目的化せず、改善判断に使われる
- 実際の判断または原因分析に使われないMetricが、取得・維持対象へ増え続けない
- 分析者が、観測条件、Metric定義、比較方法、限界を示し、Dataから直接確認できる
  Factと追加解釈を分けて説明できる

## 反証またはChallengeとなる兆候

- 最小限のDashboardでは重要な異常を検知できない
- DashboardとBI Toolの分離により、Contextの引き継ぎやTool運用Costが増える
- 原因診断に必要なDataが取得されておらず、違和感を深掘りできない
- 定期確認は続いても、改善ActionまたはOutcomeへ接続されない
- Metric数を減らした結果、後の原因診断に必要なDataまで失われる
- DashboardとDataは存在するが、分析Techniqueが不足し、Noise、相関、定義差、
  欠損または偏りをFactとして扱ってしまう

## 検証方法

### 方法と対象範囲

- 方法:
  一つのProcessまたはPlatform Serviceについて、最小限のDashboardで定期検知し、
  違和感発生時のみ追加分析する小規模運用を行う。確認頻度、Report作成工数、
  検知した異常、原因特定までの時間、改善判断への利用を記録する。分析結果について、
  使用した定義、比較方法、観測Fact、解釈、限界を第三者が追跡できるかも確認する
- 対象・資料: 未選定
- 選定方法:
  継続取得できるMetricがあり、週次または月次で改善判断を行える対象を選ぶ
- 実施規模:
  一つのJourneyまたはProcessで数回の観測Cycleから始める

### GenAIの利用

- 利用内容:
  異常候補、追加分析の切り口、分布またはSegment比較、観測記録の整理を支援する
- GenAIだけで実施しないこと:
  異常の存在、原因、改善効果、業務上の判断を生成結果だけから確定する。GenAIが
  分析TechniqueまたはDomain理解の習熟を代替したとみなす
- 実際に確認した資料・記録:
  現時点ではrelationで示したRepository Nodeのみ。過去ITSM運用の一次資料は未確認

## 結果

`not_tested`

### 実際に観測したこと

作成者は、同種の運用をITSMで約10年間、約3件のProjectに再利用し、週次・月次の
報告を行った経験を持つ。1年間でSLAおよびその他のMetricが約20%改善したという
記憶もある。また、Project Portfolio領域へ持ち込み、機能することを確認した経験が
記録された。Platform Engineeringでは最近利用を始めたが、結果はまだ確認していない。

作成者は、DashboardとDataだけでは分析またはFact抽出は成立せず、分析Techniqueの
習熟が必要だと判断している。この成立条件に関する習熟度比較またはTraining結果は
保存されていない。

ただし、このEpisodeで定義した比較方法による検証は実施しておらず、一次資料も
Repository内で確認していない。ITSMとProject Portfolioの経験を実質的な成立根拠に
持つが、このEpisodeとしては独立した検証を行っていないため、`not_tested`を維持する。

## 解釈

蓄積したITSM実務経験とProject Portfolioでの適用経験は、この運用を分野横断で
検討する実質的な根拠になる。一方、Metric改善が運用方法だけで生じたこと、約20%が
再現可能な効果量であること、Platform Engineeringでも同じ結果になることは
主張しない。

## 限界

- ITSM、Project Portfolio、Platform EngineeringではActor、Journey、利用可能な
  Data、改善周期、Metricを使うDecisionが異なる。
- 比較対象、統一されたMetric定義、Project別の結果は確認できない。
- Project Portfolioでの適用範囲と結果を示す一次資料は確認できない。
- Platform Engineeringでの実践は開始直後で、結果を評価できない。
- 必要な分析Technique、習熟度、Training方法、習熟までの期間は定義されていない。
- 分析者の習熟と、Data品質、Domain知識、Tool操作能力の影響を分離していない。
- 改善には他のProcess変更、運用判断、Team活動が寄与した可能性がある。
- Dashboardで検知できることと、Outcome Qualityを判断できることは同じではない。
- この仮説は登壇内容または標準運用として採用されたものではない。

## 公開安全性確認

- checked_at: 2026-08-04T01:53:23+09:00
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
