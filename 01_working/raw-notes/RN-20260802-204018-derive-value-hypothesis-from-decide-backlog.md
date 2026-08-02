---
id: RN-20260802-204018-derive-value-hypothesis-from-decide-backlog
type: raw_note
title: "Decideのバックログ候補からValue Hypothesisを逆算する技法"
content_language: ja
created_at: 2026-08-02T20:40:18+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-02T20:56:11+09:00
sanitization_checked_by: agent:codex
tags: [facilitation-technique, value-hypothesis, solution-hypothesis, challenge, reasoning-chain, generative-ai, workshop]
---

# メモ

本来なら、Value Hypothesisも

1. Value Stream上に観測されたボトルネック
1. ボトルネックが発生する原因 (Challenge)
1. Challenge を言語化する
1. Challengeを解決するためのValue Hypothesisを言語化する
1. Value Hypothesisを実現するためのSolution Hypothesis

という順番実施するのが本来のやり方だが、これはうまくいかない。
ほとんどのケースで先にSolution Hypothesisが出てきて、「これこれがないこと」をChallengeとして定義してしまう。

ただしこれは「これこれ」というSolutionを正当化するための文言になっており、ChallengeからのReasoning Chainのつながりを保証しない。というか多くの場合切れており、検証不可能になってしまっている。  
仮説検証を実施する上で、検証不可能なのは致命的。

Challengeからおろしてくるやり方は正しいのだが、正しく実施できないなら全く意味がない。
そのため、以前のワークショップでは以下のようにやった。

1. Solution Hypothesisとして思いついた「やったらいいかもと思うもの」をあげる
1. それに対して「これがどんな課題を解決するか (Challenge)」を書く
1. これが解決すると「どんないいことがあると思うか (Value Hypothesis)」を書く
1. 1-3のReasoning Chainの強度をGenAIで判定する。

この時のプロンプトでは以下のようにした。
- 「これこれがないこと」を禁じ手として修正対象とする
- 想定されるChallengeとValue HypothesisをGenAI側から提案する

これで少なくともChallenge - Value Hypothesis - Solution Hypothesis までは筋が通ったものができる。  
あとは
- 本当にこのChallengeは存在するかから検証
- このChallengeがある場合、特定されたValue Hypothesis以外に足りないものがないか
- Solution Hypothesisも足りないものがないか
を上から埋めていく。

この方法は紹介しても良い。
あと、これは盛り上がったのでプロンプトサンプルをお土産として共有しても良い。これは真似しやすいので。

## この方法で出した実績

- 短時間で、このGenAIの「テストケース」を通ったアイデアを数十件作成した



## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
