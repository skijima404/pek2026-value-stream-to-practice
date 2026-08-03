---
id: OBS-20260804-013225-itsm-metrics-analysis-practice
type: observation
title: "Dashboardと分析を分ける運用がITSMとProject Portfolioで用いられた"
content_language: ja
created_at: 2026-08-04T01:32:25+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-04T01:53:23+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - practitioner_experience
  - case_recollection
relations:
  - type: derived_from
    target: RN-20260803-000641-data-analysis-in-process-improvement
  - type: derived_from
    target: RN-20260804-013224-itsm-metrics-analysis-practice
  - type: derived_from
    target: RN-20260804-014715-cross-domain-metrics-analysis-practice
  - type: derived_from
    target: RN-20260804-015137-analysis-skill-required-for-metrics
---

# 観察

## 知識の成立根拠

異常検知と原因診断を分けるDashboard・分析運用は、作成者が約10年間実施し、
約3件のITSM Projectで再利用した後、Project Portfolioでも利用した
`practitioner_experience`として明示された。

週次・月次の報告運用と、1年間でSLAおよびその他のメトリックが約20%改善した
という結果と、Project Portfolioで機能したという説明は、Repository内で一次記録を
確認できない適用事例の記憶であるため、`case_recollection`として分けて扱う。

## 根拠箇所

- `RN-20260803-000641-data-analysis-in-process-improvement`の
  「分析ツールの活用は2段階で考える」「Dashboard」「BIツール等」
- `RN-20260804-013224-itsm-metrics-analysis-practice`に記録された、実施期間、
  再利用範囲、対象領域、報告頻度、改善結果についての追加説明
- `RN-20260804-014715-cross-domain-metrics-analysis-practice`に記録された、Project
  Portfolioでの適用経験、Platform Engineeringでの導入状況、Metric過剰取得を
  減らす目的についての追加説明
- `RN-20260804-015137-analysis-skill-required-for-metrics`に記録された、Dashboardと
  DataだけではFactを取り出せず、分析Techniqueの習熟が必要だという追加説明

## 根拠から直接言えること

作成者はITSM領域で、次の役割を分けたメトリック運用を約10年間実施し、約3件の
Projectでほぼ同じ方法を再利用したと説明している。

- Dashboardは、定期的に「何かおかしい」という違和感を検知する
- BI ToolやCustom Reportは、検知した違和感の原因を柔軟に掘り下げる
- 入力とReport作成の手間を減らし、週次・月次で確認できる頻度を維持する
- 時間は平均だけでなく分布や推移を見て、必要に応じてJourney等で絞り込む

作成者の記憶では、この運用を行った範囲で、1年間にSLAおよびその他のMetricが
約20%改善した。ただし、どのMetricをどの計算方法で統合した値か、約3件の
Projectすべてに共通する結果かは、このRepositoryから確認できない。

作成者は、同じ考え方をProject Portfolio領域へ持ち込み、機能することを確認した
経験も持つ。必要性が明らかでないMetricを過剰に取得、維持する無駄を減らす方法
として、分野をまたいで使えると評価している。

Platform Engineeringでは最近この運用を始めたばかりであり、現時点で結果は
確認されていない。

作成者は、この運用を成立させるには分析Technique自体が必要であり、Dashboardと
Dataを用意しただけで分析またはFactの抽出が可能になると考えるべきではないと
説明している。違和感から問いを立て、比較対象と切り口を選び、Dataから直接確認
できる範囲と解釈を分けるには習熟が必要だという実務判断である。

## 曖昧さと限界

- 長期的な経験と改善結果は主にITSMに基づく。Project Portfolioでの対象数、期間、
  Metric、削減量、評価方法は保存されていない。
- Platform Engineeringでは導入初期であり、有効性を支持または反証する結果はない。
- 元のDashboard、週次・月次Report、Metric定義、Baseline、比較期間は保存されて
  いない。
- 約20%は記憶に基づく値であり、独立して再計算していない。
- 同期間に行われた他のProcess改善を分離できず、この分析運用だけの因果効果とは
  言えない。
- ITSMとProject Portfolioでの利用経験は分野をまたいだ適用可能性を考える根拠に
  なるが、一般的な再現性または普遍的なBest Practiceを意味しない。
- 必要な分析Technique、習熟度の判定方法、Training方法、必要期間は未定義である。
- 追加説明を保存したSource Raw Notesは作成者によりReviewされている。

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
