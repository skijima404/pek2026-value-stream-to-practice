---
id: OBS-20260804-004530-solution-first-training-behavior
type: observation
title: "Solution-first再構成の有無でTraining中の記述とIdea数に異なる様子が記録された"
content_language: ja
created_at: 2026-08-04T00:45:30+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-04T00:53:33+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
relations:
  - type: derived_from
    target: RN-20260802-232517-solution-first-training-observations
  - type: references
    target: HYP-20260802-230423-solution-first-reconstruction-testability
---

# 観察

## 根拠箇所

- `RN-20260802-232517-solution-first-training-observations` の
  「手法がなかった時」「手法があった時」「件数と所要時間以外に観測した差」

## 根拠から直接言えること

作成者は、Solution-first再構成手法を用いなかったOutcome Delivery Trainingと、
用いたTrainingで、次の異なる様子を観測したと記録している。

手法を用いなかった側は、5人3 TeamのTrainingを3回程度実施した記録である。

- Teamによる違いはあるが、Challengeの3分の1程度が「何かがないこと」または
  「できていないこと」と表現された
- その表現によって、欠けているとされたものが実質的にSolutionとして固定された
- Challengeは1 Teamあたり10から15個で、その中に作成者が質の悪いHypothesisと
  評価した記述も含まれた
- 所要時間は25分程度だった

手法を用いた側は、10人程度の1 Teamで実施した記録である。

- 参加者は当初、それぞれ1回「何かがないこと」という形式で記述した
- GenAIの指摘を受けて、その記述を修正した
- 40個弱のIdeaが、設定されたTest Caseを通過した
- 所要時間は15分だった

作成者は、件数と時間以外にも、ファシリテーター負荷と、その後の仮説検証の
質に差があったと認識している。

## 曖昧さと限界

- 手法なしは複数回、手法ありは1回であり、人数、Team構成、題材、参加者経験、
  Facilitation条件を揃えた比較ではない。
- 件数と所要時間は概数であり、Training記録や第三者評価との照合結果は保存されて
  いない。
- Test Case通過は構造上の条件を満たしたことを示すだけで、Challengeの実在、
  仮説の価値、検証可能性、後続Outcomeを保証しない。
- ファシリテーター負荷は作業時間、介入回数、修正回数で測定されていない。
- 後続する仮説検証の質には、評価基準、第三者評価、比較可能な結果がない。
- このObservationは、Solution-first再構成手法の因果的効果を検証した結果ではなく、
  `HYP-20260802-230423-solution-first-reconstruction-testability`を支持またはChallenge
  するValidation Resultとして扱わない。

## 公開安全性確認

- checked_at: 2026-08-04T00:53:33+09:00
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
