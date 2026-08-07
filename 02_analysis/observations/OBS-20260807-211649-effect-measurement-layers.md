---
id: OBS-20260807-211649-effect-measurement-layers
type: observation
title: "AI Featureの効果測定を直接効果・Guardrail・中間Signal・Business Outcomeへ分ける設計が記録された"
content_language: ja
created_at: 2026-08-07T21:16:49+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-07T21:29:32+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: high
knowledge_basis:
  - recorded_statement
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260807-123008-platform-advisor-effect-measurement-observation-rationale
  - type: derived_from
    target: RN-20260806-212832-platform-advisor-vsm-effect-hypothesis
  - type: derived_from
    target: RN-20260806-213822-platform-advisor-downstream-ai-slop-signals
---

# 観察

## 知識の成立根拠

三つのRaw Noteには、Platform Advisorという架空Scenarioについて、期待する局所効果と
下流への負荷移転を分け、さらにPlatform採用と最終Business Outcomeを別に観測する
測定設計が記録されている。四層を一つの測定構造として整理する部分は
`reasoned_synthesis`である。

これらは物語内の測定設計であり、実測値、実在する導入結果または
`explicit_validation`ではない。

## 根拠箇所

- `RN-20260807-123008-platform-advisor-effect-measurement-observation-rationale`の
  「観測観点とその理由」から「なぜ観測点を事前に決めるのか」まで
- `RN-20260806-212832-platform-advisor-vsm-effect-hypothesis`の「現行Scopeの効果仮説」、
  「VSM上の数値計算」および「現行Scopeに含めない工程」
- `RN-20260806-213822-platform-advisor-downstream-ai-slop-signals`の三つの観測ポイントと
  「読み方」

## 根拠から直接言えること

記録された測定設計は、少なくとも次の四つを分けている。

| 観測層 | Platform Advisor Scenarioで記録された対象 |
| --- | --- |
| 直接のProcess Outcome | 情報探索、問い合わせ、比較観点整理のPT、LTおよび手戻り |
| 下流Quality Guardrail | Project Owner Review、利用方法詳細調査、環境払い出し後の再確認、修正、追加作業および手戻り |
| 中間Signal | 対象ProjectにおけるPlatform採用率 |
| 最終Business Outcome | 標準化された運用の増加と既存システム運用費の削減 |

直接対象工程のPTまたはLTが短縮されても、下流のReviewまたは追加作業が増えれば、
局所効果とCost Transferが同時に起きた可能性があると整理されている。また、Platform
採用率が上がっても、運用標準化または運用費削減が実現したとは結論しない。

各観測層を分ける理由として、AI Featureが直接変更できる範囲と、複数要因の影響を受ける
中間・最終Outcomeを混同しないこと、および導入後に改善したMetricだけを選ぶことを
避けることが記録されている。

## 曖昧さと限界

- Platform Advisor、VSM、Baseline、Guardrailおよび数値は架空ScenarioのFixtureであり、
  実在する組織またはServiceのEvidenceではない。
- 四層の分け方が他のAI Featureでも十分か、どの期間と対象数で測るかは未確認である。
- 下流Metricが悪化しなくても、観測対象外のActor、定性的な負荷、さらに後続する工程へ
  Costが移る可能性は残る。
- このObservationは、測定方法またはPlatform Advisorの登壇への採用を意味しない。

## 公開安全性確認

- checked_at: 2026-08-07T21:29:32+09:00
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
