---
id: OBS-20260807-211650-vsm-problem-causal-ambiguity
type: observation
title: "VSM・MBPMで観測した摩擦だけではProblemの原因構造を一意に決められないと整理された"
content_language: ja
created_at: 2026-08-07T21:16:50+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-07T21:29:32+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260807-194919-platform-advisor-retrospective-iterative-problem-learning
  - type: derived_from
    target: RN-20260806-194532-platform-advisor-selection-vsm-and-mbpm
  - type: derived_from
    target: RN-20260806-224717-vsm-mbpm-process-analysis-explanation
---

# 観察

## 知識の成立根拠

Platform Advisorの架空Scenarioでは、VSMとMBPMで情報探索、問い合わせ、比較資料作成、
合意形成および待ち時間を表現した。その後の感想戦で、同じ観測結果から複数のProblem
構造を解釈できると整理されている。

Scenarioの記述は`recorded_statement`であり、観測された摩擦と原因構造を分ける部分は
`reasoned_synthesis`である。実在する組織に対する因果分析または検証結果ではない。

## 根拠箇所

- `RN-20260807-194919-platform-advisor-retrospective-iterative-problem-learning`の
  「感想戦で見えた三つの前提」から「最初からすべてを当てようとしない」まで
- `RN-20260806-194532-platform-advisor-selection-vsm-and-mbpm`のVSM初期案、MBPMでの
  深掘りおよびInterview対象のSelection Bias候補
- `RN-20260806-224717-vsm-mbpm-process-analysis-explanation`のVSM・MBPMの利点と
  効果が限定的と思われる点

## 根拠から直接言えること

Scenarioでは、情報探索、問い合わせ、比較資料作成およびMeeting待ちという同じ摩擦に
対し、少なくとも次の原因候補が記録されている。

- 情報が不足または分散している
- 選択肢が多すぎる
- 利用者が判断に必要なSkillを持っていない
- 利用者に意思決定権限がない
- 選択結果のRiskと説明責任が利用者へ偏っている
- 組織が安全な標準Pathを提供していない
- 利用者と承認者が異なるValueまたは制約を持っている

VSMとMBPMは、工程、Actor、PT、LT、手戻りおよびHandoverを可視化できる。一方、
Process Metricだけでは、観測された摩擦をどの原因構造として解釈すべきか、利用者が
比較と選択を望んでいるか、または誰が意思決定Riskを引き受けるべきかは決まらないと
整理されている。

Interview対象をPlatform採用者に限定すると、選択へ関与しなかった人、採用しなかった人、
標準Pathを受動的に利用した人、および選択を負担と感じる人の視点が入りにくいという
Selection Bias候補も記録されている。

## 曖昧さと限界

- 原因候補は架空Scenarioの感想戦であり、各原因が実在することを確認したEvidenceではない。
- VSM・MBPM一般の能力または限界を体系的に調査した結果ではない。
- Process Metric、Interview、Decision Rights分析などを組み合わせた場合に、原因識別が
  どの程度改善するかは未確認である。
- このObservationは、特定のProblem Statement、Value HypothesisまたはSolutionの採用を
  意味しない。

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
