---
id: HYP-20260802-230423-solution-first-reconstruction-testability
type: hypothesis_episode
title: "Solution-firstでもReasoning Chainを再構成すれば検証可能な仮説を作りやすい"
content_language: ja
created_at: 2026-08-02T23:04:23+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-07T21:38:30+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - case_recollection
  - direct_observation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260802-230422-solution-first-hypothesis-reconstruction
  - type: derived_from
    target: OBS-20260804-004530-solution-first-training-behavior
  - type: derived_from
    target: OBS-20260807-211648-structural-coverage-empirical-checks
  - type: derived_from
    target: RN-20260807-191024-problem-first-solution-first-quality-tradeoff
  - type: references
    target: HYP-20260730-015718-ai-speed-requires-value-validation
---

# 仮説

参加者がSolution候補から考え始める場合でも、そのSolutionが解決するChallengeと、
Challengeを解消した時のValue Hypothesisを明示的に遡って再構成し、GenAIによる
Reasoning Chainの構造確認、VSM・MBPMに対する網羅性Review、実証的な仮説検証を
別の確認として扱えば、教科書的な順序をそのまま実行させる場合より、参加者の表現と
主体性を保ちながら、反証条件と検証対象を説明できる仮説を作りやすい。

## 知識の成立根拠

作成者は、Solution-firstからReasoning Chainを再構成する方法をTrainingで用いた
`practitioner_experience`を持つ。異なるTrainingで観測したChallenge表現、Idea数、
所要時間およびFacilitator負荷は、条件を揃えた比較ではないため、
`case_recollection`と`direct_observation`を含むContextとして扱う。

実際に使ったPromptを公開可能な形へクレンジングした記録と、方法の狙いおよび限界を
説明した記録を`recorded_statement`として追加した。構造確認、網羅性Review、実証的な
検証を分け、方法全体の不確実性を四つへ整理する部分は`reasoned_synthesis`である。

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
- 参加者がIdeaの提案と修正を続け、特定の正解を当てる作業にならない
- VSM・MBPMへの再照合により、未検討のActor、工程、摩擦またはOptionが見つかる
- 構造確認後も、Challengeの実在、Valueの重要性およびSolutionの有効性を別途検証する

## 反証またはChallengeとなる兆候

- 論理的に整った文章は増えるが、実在するChallengeを確認できない
- GenAIがもっともらしいChallengeを補い、Solutionの正当化を強化する
- 教科書的順序または人間だけのReviewと比べて、検証可能性に差がない
- Reasoning Chainの確認が形式的なGateとなり、未知のOptionを狭める
- GenAIへの委譲によって、参加者または後続Ownerが仮説の意味と検証責任を失う
- VSM・MBPMの既知の範囲だけを再確認し、Source側の欠落を見落とす

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | Solution-first再構成とGenAIによる構造確認が、教科書的順序または人間だけのReviewよりReasoning Chainの構造品質を高める | critical | none | not_checked | unknown | unknown | 同一題材、同一参加条件および第三者評価による比較がない |
| U2 | 方法を使っても参加者のIdea貢献、表現および主体性が保たれ、Facilitator負荷が許容範囲になる | high | none | not_checked | unknown | unknown | Training間の観測差はあるが、人数、Team構成、題材および進行条件が揃っていない |
| U3 | VSM・MBPMに対する網羅性Reviewが、見落としたActor、工程、摩擦またはOptionの回収に役立つ | high | none | not_checked | unknown | unknown | Review前後の差分と、Source自体にある欠落を区別した記録がない |
| U4 | 構造確認後も参加者または後続Ownerが仮説の意味と検証責任を保持し、実証的な検証へ接続できる | critical | none | not_checked | unknown | unknown | 構造確認後に生成した仮説のOwner、検証計画、実施結果および意思決定を追跡していない |

## 検証方法

### 方法と対象範囲

- 方法:
  小規模なWorkshopまたは既存Idea群を用い、教科書的順序、Solution-firstからの
  再構成、人間だけのReview、GenAI併用Reviewを限定比較する。作成時間、Solutionが
  混入したChallenge、独立したOption数、参加者の修正と貢献、Facilitator介入、
  第三者が説明できた反証条件を記録する。構造確認後にVSM・MBPMへ再照合し、回収した
  欠落を記録する。その後の検証計画、Ownerおよび実施結果は別に追跡する。
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
構造上の確認を通過したIdeaを数十件作成したと記録している。実際に使用したPromptの
公開可能な記録もあり、構造確認、網羅性Review、実証的な検証を分ける意図が明記された。

教科書的順序または別のReview方法との比較、第三者による検証可能性評価、
VSM・MBPM再照合による欠落回収、および生成した仮説を実際に検証した結果は
保存されていない。Training間の観測差は、条件が揃っていないため検証結果に使用しない。

## 解釈

このEpisodeが置く新しい因果は、思考の開始順序ではなく、Challenge、Value、
Solutionの役割を分離し、後からSourceと反証条件へ接続できるかが仮説品質を
左右するという点である。

GenAIの役割は仮説を正しくすることではなく、構造上の欠落と未検証部分を
見つけやすくすることに限定する。構造確認の通過、既知のVSM・MBPMへの再照合、
Challengeの実在およびSolutionの有効性は、それぞれ別の確認結果として記録する。

## 限界

- 一人の作成者が記録したWorkshop経験を出発点としている
- 仮説の論理的一貫性は、Challengeの実在または価値を保証しない
- Workshop参加者、題材、Promptによって結果が変わり得る
- VSM・MBPMまたはDomain Knowledge自体に欠落がある場合、網羅性Reviewでも回収できない
- GenAIが修正を主導すると、参加者の理解または検証責任が弱まる可能性がある
- このEpisodeは、登壇内容、Workshop手法、Prompt配布の採用決定ではない

## 公開安全性確認

- checked_at: 2026-08-07T21:38:30+09:00
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
