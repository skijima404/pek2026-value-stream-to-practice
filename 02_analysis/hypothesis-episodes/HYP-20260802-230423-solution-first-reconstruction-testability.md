---
id: HYP-20260802-230423-solution-first-reconstruction-testability
type: hypothesis_episode
title: "Solution-firstでもReasoning Chainを再構成すれば検証可能な仮説を作りやすい"
content_language: ja
created_at: 2026-08-02T23:04:23+09:00
created_by: agent:codex
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-02T23:18:14+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
relations:
  - type: derived_from
    target: OBS-20260802-230422-solution-first-hypothesis-reconstruction
  - type: references
    target: HYP-20260730-015718-ai-speed-requires-value-validation
---

# 仮説

参加者がSolution候補から考え始める場合でも、そのSolutionが解決するChallengeと、
Challengeを解消した時のValue Hypothesisを明示的に遡って再構成し、GenAIで
Reasoning Chainの欠落とSolutionの混入を確認すれば、教科書的な順序をそのまま
実行させる場合より、反証条件と検証対象を説明できる仮説を作りやすい。

## Mobiusでの位置づけ

`solution`

Discoveryで必要なValue Hypothesisを、Solution候補から安全に再構成するための
Facilitation Methodに関するSolution Hypothesisである。生成した個々のPromptや
Worksheetは、この方法を試すFeature候補であり、まだ採用していない。

## 期待する兆候

- Challengeが「特定Solutionがないこと」ではなく、観測可能な現在の問題として
  表現される
- Value Hypothesisに対象Actor、期待する変化、観測方法が含まれる
- 同じChallengeに対する複数のSolution Optionを挙げられる
- 第三者が、どのSourceを確認し、何が起きれば仮説をChallengeできるか説明できる
- GenAIが提案した前提と、人間またはSourceが確認した事実を区別できる

## 反証またはChallengeとなる兆候

- 論理的に整った文章は増えるが、実在するChallengeを確認できない
- GenAIがもっともらしいChallengeを補い、Solutionの正当化を強化する
- 教科書的順序または人間だけのReviewと比べて、検証可能性に差がない
- Reasoning Chainの確認が形式的なGateとなり、未知のOptionを狭める

## 検証方法

### 方法と対象範囲

- 方法:
  小規模なWorkshopまたは既存Idea群を用い、教科書的順序、Solution-firstからの
  再構成、人間だけのReview、GenAI併用Reviewを限定比較する。作成時間、Solutionが
  混入したChallenge、独立したOption数、第三者が説明できた反証条件を記録する。
- 対象・資料:
  未選定。機密情報を含まないPlatform Service候補を使う。
- 選定方法:
  参加者がSolutionを先に思いつきやすく、対象ActorとCurrent Stateを確認できる
  題材を優先する。
- 実施規模:
  最初は少数のIdeaまたは一回のWorkshopに限定する。

### GenAIの利用

- 利用内容:
  Solutionが混入したChallenge、Reasoning Chainの飛躍、暗黙の前提、代替Optionの
  候補を指摘する。
- GenAIだけで実施しないこと:
  Challengeの実在、利用者価値、検証結果を生成内容から判断する。
- 実際に確認した資料・記録:
  現時点ではrelationで示したRepository Nodeのみ。

## 結果

`not_tested`

### 実際に観測したこと

作成者は、Solution-firstからReasoning Chainを再構成するWorkshopを実施し、
構造上の確認を通過したIdeaを数十件作成したと記録している。

教科書的順序または別のReview方法との比較、第三者による検証可能性評価、
生成した仮説を実際に検証した結果は保存されていない。

## 解釈

このEpisodeが置く新しい因果は、思考の開始順序ではなく、Challenge、Value、
Solutionの役割を分離し、後からSourceと反証条件へ接続できるかが仮説品質を
左右するという点である。

GenAIの役割は仮説を正しくすることではなく、構造上の欠落と未検証部分を
見つけやすくすることに限定する。

## 限界

- 一人の作成者が記録したWorkshop経験を出発点としている
- 仮説の論理的一貫性は、Challengeの実在または価値を保証しない
- Workshop参加者、題材、Promptによって結果が変わり得る
- このEpisodeは、登壇内容、Workshop手法、Prompt配布の採用決定ではない

## 公開安全性確認

- checked_at: 2026-08-02T23:18:14+09:00
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
