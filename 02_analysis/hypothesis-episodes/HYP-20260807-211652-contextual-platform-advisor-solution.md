---
id: HYP-20260807-211652-contextual-platform-advisor-solution
type: hypothesis_episode
title: "Contextを確認するPlatform Advisorは静的案内より選定負荷を減らしやすい"
content_language: ja
created_at: 2026-08-07T21:16:52+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-07T21:36:59+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260806-205437-platform-selection-solution-options
  - type: derived_from
    target: RN-20260807-140147-platform-advisor-story-solution-first-mobius
  - type: tests
    target: HYP-20260807-211651-platform-selection-preparation-value
---

# 仮説

利用者のContextを追加質問で確認し、候補、適用条件、判断材料、根拠および不足情報を
対話的に提示するPlatform Advisorは、静的なFAQ、Document拡充またはFlowchartだけを
提供する場合より、Platform選定に必要な情報探索と比較判断の負荷を減らしやすい。

## 知識の成立根拠

Raw Noteには、同じPlatform選定課題に対するSolution Optionとして、FAQ、選び方
Flowchart、比較資料Template、Document拡充およびPlatform Advisorが記録されている。
別のRaw Noteでは、Contextに応じて質問を返せることをAdvisorの差異として置いた。

物語内で行ったことにしたPrototype比較は架空であり、検証結果として使用しない。
このEpisodeは、記録されたOptionと想定Mechanismから形成した`reasoned_synthesis`である。

## Mobiusでの位置づけ

`practice` scopeの`solution`

Platform選定に関与する利用者が探索と判断準備の負荷を減らすというValue Hypothesisに
対し、複数のSolution OptionからContextualなAdvisorを選ぶ因果を確認する。

## このRepositoryでの扱い

このEpisodeは、Platform Advisorの架空Scenarioで検討したSolution Optionと因果を、
後から参照、比較またはScenario作成へ再利用できるHypothesis Modelとして保持する。
現在、このRepositoryでPrototype比較その他の検証を実施する予定はない。

`not_tested`は、Solutionが否定されたこと、検証待ちの作業であること、または登壇内容へ
採用されたことを意味しない。以下のValidation Componentと検証方法は、将来この仮説を
別Scopeで検討する場合に利用できる検証設計であり、現在の実施計画ではない。

## 期待する兆候

- 同じ選定Taskで、静的案内より少ない探索、追加質問または時間で適切な候補へ到達する
- 利用者が、候補だけでなく適用条件、制約、根拠および不足情報を説明できる
- Context不足、対象外または高RiskなCaseで、追加質問、保留、拒否またはEscalationを
  適切に選べる
- Advisorの構築・更新・Support Costを含めても、対象Jobに対して他Optionより妥当である

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | Contextualな対話が静的案内より探索と比較判断の負荷を減らす | critical | none | not_checked | unknown | unknown | 架空比較以外の実測Task、時間、追加質問および誤りを確認していない |
| U2 | Advisorが適用条件、制約、根拠、不足情報および非対応範囲を伝えられる | critical | none | not_checked | unknown | unknown | 流暢な回答と安全な判断支援を区別する評価を実施していない |
| U3 | Advisorの作成、Source更新、訂正、SupportおよびEscalation Costが妥当である | high | none | not_checked | unknown | unknown | 静的案内や人による相談との総Cost比較がない |
| U4 | Advisorが、選択を望む対象Segmentに適合する | critical | none | not_checked | unknown | unknown | 標準Pathを望む利用者へ選択作業を追加する可能性がある |

## 検証方法

以下は、将来この仮説を検証する場合の方法候補であり、このRepositoryでの実施予定ではない。

### 方法と対象範囲

- 方法:
  同じPlatform選定Scenarioを、現行手段、FAQまたはDocument、Flowchartおよび
  限定したAdvisor Prototypeで実施し、Task結果と後続説明を比較する
- 対象・資料:
  実在する選定Jobを一般化したScenarioと、公開可能または検証用に限定したSource
- 選定方法:
  Platform選定経験、Roleおよび選択意向が異なる対象を含める
- 実施規模:
  一つの対象Jobと少人数から開始し、Solution一般へ拡張しない

### GenAIの利用

- 利用内容:
  Prototype、Known-good、Known-bad、Context不足および対象外Scenarioの作成支援
- 実際に確認した資料・記録:
  relationで示したRaw Noteのみ。物語内の架空結果はEvidenceにしない

## 結果

`not_tested`

### 実際に観測したこと

複数のSolution Optionと比較観点は記録されているが、実在する利用者またはTaskを使った
比較結果はない。

## 解釈

Advisorは、AIであること自体ではなく、利用者Contextに応じて不足情報と適用条件を
確認できるというMechanismで比較する。静的Optionが同じOutcomeを小さいCostで
実現できる場合、Advisorを選ぶ理由は弱くなる。

## 限界

- 選定上の偏り: Scenario Designから形成され、実在する比較対象は未選定である
- 未確認の証拠: Task精度、利用者行動、総Cost、更新負荷および後続Outcome
- 一般化できない範囲: 何でも質問できるBot、別のPlatform Job、高Riskな意思決定
- 残存リスクと影響を受ける判断:
  U1からU4を確認するまで、Platform Advisorを他Optionより優先できない

## 公開安全性確認

- checked_at: 2026-08-07T21:36:59+09:00
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
