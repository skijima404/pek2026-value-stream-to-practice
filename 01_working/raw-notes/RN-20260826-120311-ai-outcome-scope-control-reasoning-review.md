---
id: RN-20260826-120311-ai-outcome-scope-control-reasoning-review
type: raw_note
title: "AI Outcome分類を用いたAI委譲範囲の調整事例"
content_language: ja
created_at: 2026-08-26T12:03:11+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: corrected
sanitization_status: not_needed
sanitization_checked_at: 2026-08-26T12:33:27+09:00
sanitization_checked_by: agent:codex
tags: [ai-outcome, delegation-scope, cognitive-step, reasoning-chain, review-cost, accountability, practitioner-experience]
---

# AI Outcome分類を用いたAI委譲範囲の調整事例

## このメモの位置づけ

既存のAI Outcome分類が、AIに依頼する作業の境界を説明するために実際に
役立った一事例を記録する。

分類そのものは
`RN-20260730-140133-ai-outcomes-and-mbpm` で次のように整理されている。

1. 速く作る
2. 広く探す
3. 分かるように解釈する
4. 選べるように整理する
5. 本当に筋が通るか疑う

この事例は分類の一般的な有効性を検証したものではなく、一人の実践者が
別RepositoryでCodexと共同作業した際の観察である。別Repositoryの固有情報や
記述内容は、このメモには保存しない。

## 起きたこと

Knowledge Graph開発用の別Repositoryで、RepositoryのルールとIntentを整備していた。
その際、CodexがIntentの記述から推論したNext Stepを提案し、Intentの記述へ
混ぜ込んだ。

Codexの提案内容自体は非常に良かった。一方で、提案の量が多く、その状態を
レビュー完了にするには、作成者が内容をかなり整理する必要があった。
永続化されたIntentへ含める以上、レビューせずに作成者が責任を持つことは
できないため、良い提案であっても追加のReview負荷になった。

## AI Outcome分類によって分かったずれ

この時に作成者がAIへ求めていたOutcomeは、主として次だった。

> 5. 本当に筋が通るか疑う

つまり、自分が記述したIntentについて、前提の不足、Reasoning Chainの飛躍、
矛盾または弱い接続がないかを確認してほしかった。

しかし、実際の応答には次のOutcomeも混ざっていた。

> 4. 選べるように整理する

Codexは、記述済みのReasoningを検査するだけでなく、推論したNext Stepや
追加の選択肢を並べた。これは有用な提案ではあったが、その時点で依頼していた
Outcomeとは異なっていた。

この分類を思い出したことで、問題を単に「出力が多い」「勝手に提案された」
と表現するのではなく、次のように切り分けられた。

```text
求めていたOutcome
= 本当に筋が通るか疑う

混ざったOutcome
= 選べるように整理する
```

## ルール説明に使えたこと

Outcomeの違いを認識すると、Codexに対して、二つの作業を同時に一つの成果物へ
混ぜるのではなく、別のCognitive Stepとして扱うよう説明しやすくなった。

この事例から作れる指示例は次のようになる。ただし、これは会話を整理するために
作成した例であり、別Repositoryで使用した文面の転載ではない。

> まず、記述済みReasoningについて、前提の不足、矛盾、論理の飛躍および
> 弱い接続を検査する。Next Step、追加Optionまたは実装案も提案してよいが、
> Reasoningの検査結果とは混ぜず、別の提案用Folderへ格納する。

実際の事例でも、Codexの意見やNext Stepが不要だったわけではない。提案は欲しかった
ため、Intent本文へ混ぜるのではなく、別Folderへ提案として格納する運用にした。
これにより、IntentのReasoningをReviewするStepと、提案を評価して選ぶStepを分けた。

## 現時点の解釈

この事例では、AI Outcome分類はAI機能の分類表というより、AIとの共同作業を
異なるCognitive Stepへ分け、成果物、格納先およびReview単位を調整する共通言語として
機能した。

特に、次を区別するのに役立った。

- 提案内容の品質が高いか
- 今回扱っているCognitive StepのOutcomeに合っているか
- 永続化する内容として人間がReview可能な量か
- 誰がその内容を確認し、責任を引き受けるか
- 異なるOutcomeのOutputをどこへ格納し、いつReviewするか

提案内容が良いことと、現在Reviewしている成果物へ混ぜてよいことは別である。
複数OutcomeのOutputが一つの成果物へ混ざると、人間が責任を引き受けるための
整理とReviewを増やす場合がある。一方、別のCognitive Stepと格納先へ分離すれば、
有用な提案を捨てずに、現在のReview範囲を限定できる。

したがって、AI利用時には「この作業でAIに何をしてほしいか」だけでなく、
「今回のCognitive Stepで扱うOutcomeはどれか」「別OutcomeのOutputをどこへ分けるか」
まで明示すると、委譲範囲とReview範囲を合わせやすい可能性がある。

この事例からは、設計を次のように捉える実践者の考え方も記録できる。

> 設計とは、異なるCognitive Stepを分けて管理できるようにすることである。

ここでいう分離は、AIに一種類の作業しかさせないことではない。Reasoningの検査、
Option生成、選択および採用判断を識別可能にし、それぞれを適切な成果物、格納先、
Review条件および責任へ接続できるようにすることである。

## 限界

- 一人の実践者による一回の事例であり、他の利用者や作業でも同様に機能するかは
  確認していない。
- Outcomeを明示した場合と明示しなかった場合のReview時間やOutput量を比較測定
  していない。
- Codexの提案が有用だったことと、Intentへ混ぜるべきだったことは別であるが、
  この事例では提案内容自体の品質を独立に評価していない。
- 五つのOutcomeは網羅的・排他的な分類ではないため、一連の共同作業に複数Outcomeを
  組み合わせること自体を否定しない。問題にしたのは、異なるCognitive StepのOutputが
  同じ成果物とReview単位へ混ざっていたことである。

## 訂正履歴

### CR-20260826-123051

- corrected_at: 2026-08-26T12:30:51+09:00
- corrected_by: human:kijima
- target: `ルール説明に使えたこと`の「Next Step、追加Optionまたは実装案は、明示的に依頼されるまで生成しない」という初期解釈、およびその解釈に基づく委譲範囲の説明
- correction: Codexの意見とNext Stepも必要だったため生成を禁止したのではなく、Reasoningの検査とは別のCognitive Stepとして扱い、別Folderへ提案として格納した。IntentのReviewと提案の評価を別の成果物およびReview単位へ分けた
- reason: 保存後、実践者から、求めていたのはOption生成の除外ではなくCognitive Stepの分離だったと明示されたため
