---
id: RN-20260729-220353-audience-and-value-hypothesis
type: raw_note
title: "Audienceと価値仮説の検討"
content_language: ja
created_at: 2026-07-29T22:03:53+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: unreviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-30T00:44:17+09:00
sanitization_checked_by: agent:codex
tags: [audience, value-hypothesis, platform-engineering, ai-slop]
---

# メモ

全体的にPowered by AssistA

Audienceについて思いついたこと

- 大きく2種類
  - 当日参加
    - リモート
    - オンサイト
  - 後でキャッチアップ
    - 資料その他

リモートはキャパシティなさそうなので、「他がいっぱいだったから」みたいな参加者は多分オンサイトのみ。
と考えると、リモート、および後でキャッチアップ勢は興味があってみるものと思われる。

## あらかじめ興味があるAudienceにとって課題は何か

これがこのセッションの価値の仮説につながるユーザーのChallenge。
(当日なんとなくで入った人たちを引き込むことはセッション冒頭でやる。なのでここでの価値仮説は、課題感のある人をターゲットにする。)

- 作ることはできる。でも、作るべきものか判断できない
- Platform Serviceの価値を説明できない
- プラットフォーム (サービス) が使われない
  - 利用されない理由がわからない
- 価値を生んでいるか不安
  - 価値を生んでいるか把握できていない
  - 正しい (効果の出る) やり方がわからない
- AI Slopを起こしていないか不安
  - Slopを問題にするのは多分利用者側、つまりSlopの被害を受けた側。
  - ツールを作った側は大体気にしない。
- AI導入後の効果測定方法がわからない
- AIを活用した何かを作りたいが、いまいちしっくりこない
- 作るものが増えすぎる
  - IDPの体験がかえって悪くなる

## 価値仮説

AIによってPlatform Serviceや支援機能を作る速度が上がるほど、Platform Teamには「作る能力」だけでなく、以下の能力が必要になる。

- 何を作るべきかを選ぶ能力
- 価値が弱いものを捨てる能力
- 作ったものが本当に価値を生んだか検証する能力

これらの能力を持つことで、Platform TeamはAIによって増えるアイデアや機能候補を、局所最適なAI Slopとして増殖させるのではなく、価値あるPlatform Serviceとして育てることができる。

## 検証

この価値仮説をこのセッション単体で精緻に検証することはできないため、まずはResearchとして扱う。

現時点では、以下の観測結果と整合している。

- 過去の調査結果や、典型的なPlatform Engineeringの失敗パターンと一致している
- 現場観察結果とも一致している
- 弊社公式ブログEditorialの見解とも一致している

したがって、この価値仮説は「証明済み」ではないが、複数の観測結果から支持されている有力なProblem / Value Hypothesisとして扱う。

## 仮説: PEKのAudienceにこの課題を持っている人がいるか

前回クラウドネイティブ会議の時の登壇の「続き」にあたるもの。
半分から2/3程度埋まったからそれなりに興味を持つ人はいると思われる。
(これもこれ以上精緻な検証は不可能。よってこれでよしとしましょう。)


## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
