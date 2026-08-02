---
id: RN-20260802-211319-textbook-hypothesis-flow-and-solution-first-reconstruction
type: raw_note
title: "教科書的な仮説構築とSolution候補からの逆算"
content_language: ja
created_at: 2026-08-02T21:13:19+09:00
content_origin: human_direct
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-02T21:51:39+09:00
sanitization_checked_by: agent:codex
tags: [hypothesis-construction, value-hypothesis, solution-hypothesis, challenge, reasoning-chain, vsm, mbpm, facilitation-technique, quantitative-outcome]
---

# メモ

RN-20260802-204018-derive-value-hypothesis-from-decide-backlog  
に書いた、「教科書的なやり方」

- VSM / MBPM を作成
  - 個人の努力で保たれているプロセスの可能性があるので、一緒に「工夫しているポイント」「こんなことにモヤモヤしている」なども付箋で周囲に貼っておく
- 7つのムダを手掛かりにムダを洗い出す
  - 必ずしも7つのムダだけに頼らなくても良いが、7つのムダを観点として使えると品質が上がる
- なぜそのムダがダメなのかを言語化する (Challenge)
- Challengeを解消すると、誰にどんないいことがあるかを言語化する (Value Hypothesis)
- ムダを改善するための施策を考える (Solution Hypothesis)
  - ここは明確にIdeationの形式をとっても良い

ただこれ、自分自身がプロセス改善のそれなりの経験がないと「7つのムダ」のコンセプトにキャッチアップするのにいっぱいで、どれがムダに分類されるべきものかもよくわからない。  
また、Challengeで「これこれ (Solution) がないこと」と言いがち。  

この形の中で崩してはいけないものもあって、
- VSM / MBPM をスタート地点とする
  - 共通言語の作成
  - 効果は原則として定量的に表現する
    - まず、すべての効果について定量的な説明を求める
    - 定性的にしか表現できない場合は、なぜ数値化できないのかを説明する
  - 小さすぎるOutcome, 大きすぎるOutcomeを目指すことを防ぐ
    - 数字が見えていないと、目指すべきOutcomeのサイズが安定しない
- 個人の努力でどうにかなっている領域や、個人がプロセスに対して思っている違和感も一緒に扱う
  - 個人の努力でどうにかなっている領域は属人化していることがある。VSM / MBPMだけだと見えにくい。
  - 違和感がムダ発見の手掛かりになる

これをスタート地点にしないと声の大きい人が勝つ状況になりやすい。

重要なのは、Challenge - Value Hypothesis - Solution Hypothesis のつながりに論理的強度があること。
およびこのつながりがどの程度確かかを検証できること。(これが仮説検証のキモ。)

従来のやり方でできる人であっても、状況を見て「こういう時はこのSolution」と直感的に発見し、「なぜそう思ったのか」とその直感の妥当性を後から検証する思考を辿る人もいる。というか私がそれ。
であれば、このやり方を使って仮説の質を上げられるなら、検証対象とする仮説がそれなりの品質でできるのであれば、順番はどうでもいい。

ただしこの後きちんと仮説を検証する。検証しないまま実装にはなだれ込まない。


## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
