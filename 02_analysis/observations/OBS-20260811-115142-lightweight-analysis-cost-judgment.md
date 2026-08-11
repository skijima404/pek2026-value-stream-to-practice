---
id: OBS-20260811-115142-lightweight-analysis-cost-judgment
type: observation
title: "小規模Applicationでは約16時間の軽量分析が数か月の誤投資回避に妥当と判断された"
content_language: ja
created_at: 2026-08-11T11:51:42+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-11T12:02:05+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - explicit_validation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260811-115140-small-application-standard-path-walkthrough
---

# 観察

## 知識の成立根拠

小規模Applicationの標準Pathに対し、重いArchitecture分析を簡略化する条件、軽量な確認内容、
許容する分析Costおよび誤投資とのCounterfactualを実践者へ確認した。目的を持ったFocused
Interviewを`explicit_validation`、保存した回答を`recorded_statement`、分析の比例性と
Cost妥当性に関する実務判断を`practitioner_experience`として扱う。

約16時間と数か月の投資Riskを比較する部分は、組織の実測ではなく実践者個人の感覚値を
使った`reasoned_synthesis`である。

## 根拠箇所

- `RN-20260811-115140-small-application-standard-path-walkthrough`の「軽量な分析」
- 同Raw Noteの「この記録だけでは分からないこと」

## 根拠から直接言えること

一枚程度の小規模Applicationに対して、重いArchitecture Vision作成または詳細なRisk比較は
過剰と判断された。代わりに、対象課題、期待Outcome、部門Scope、Dataの重大性、標準構成への
適合、および受入・Scope外判断を一枚程度の軽量Hypothesis Statementで確認する候補が
示された。

これはSAFe上のEpic分類または規模を適用するものではない。`EPIC Hypothesis Statement`の
Formatだけを小規模Applicationへ流用し、価値仮説と得たいOutcomeを明確にできれば十分と
判断された。

実践者個人の感覚値では、現場観察とFact Checkを含む実働約16時間で十分とされた。これは
組織の実測値、合意値または標準ではない。

誤ったTeamまたは誤ったValue Hypothesisに基づいて数か月を投資するRiskを下げられるなら、
約16時間の分析Costは安く、妥当であると実践者は回答した。

## Hypothesisへの射程

`HYP-20260804-013223-outcome-first-ai-resource-allocation`のU4に対して、詳細なResource
AllocationをすべてのCaseへ適用せず、小規模Applicationでは一枚程度のStatementと約16時間の
現場観察・Fact Checkへ簡略化する条件が得られた。

数か月の誤ったTeam投資またはValue Hypothesisへの投資と比較したCounterfactualでは、
約16時間が妥当と判断された。このため、確認した小規模Applicationと実践者の感覚値の範囲では、
分析Costが回避可能な誤投資に対して妥当になり得るというU4を`supports`する直接Evidenceと
なる。ただし実Costまたは回避効果を確認していないため、Coverageは限定される。

## 代替説明

- 実際の現場観察、Fact Check、Statement作成およびReviewには16時間を超える可能性
- 標準Pathが明確なら16時間も不要で、さらに簡略化できる可能性
- 誤ったTeamまたはValue Hypothesisでも早期に気づき、数か月の損失にならない可能性
- 16時間の分析を行っても、正しいTeam、Valueまたは実装Scopeを選べない可能性

## 曖昧さと限界

- 約16時間は実践者個人の感覚値で、組織の実測、合意、標準または複数Caseの分布ではない。
- 軽量Hypothesis Statementを実際に作成・利用したCaseではなく、判断更新を観測していない。
- 流用するFormatの具体的な項目、必須入力または運用方法を確認していない。
- 誤投資の発生頻度、回避量、対象Resource、期間、金額またはOpportunity Costを確認していない。
- 標準構成の作成・維持Costと、Application単位の分析Costを同じ比較へ含めていない。
- この結果からU3の全体経済妥当性、Feature Hypothesisまたは親Value Hypothesisを支持しない。

## 公開安全性確認

- checked_at: 2026-08-11T12:02:05+09:00
- checked_by: agent:codex
- result: `sanitized`
- scope:
  この分析ノードの本文、frontmatter、relationの組み合わせを、
  人間の意図Reviewを確定する時点で再確認した
- finding:
  公開対象に不要な識別情報をCategory単位で削除または一般化し、削除値は
  Repository、訂正履歴、Filename、Logへ保存していない
- limitation:
  公開安全性の確認は、内容の正しさ、検証完了、採用を意味しない
