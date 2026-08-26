---
id: RN-20260826-124353-outcome-driven-cognitive-step-decomposition
type: raw_note
title: "AI協働におけるOutcome起点のCognitive Step分解"
content_language: ja
created_at: 2026-08-26T12:43:53+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-26T12:58:27+09:00
sanitization_checked_by: agent:codex
tags: [ai-outcome, cognitive-step, user-story, delegation-design, accountability, review-boundary, presentation-planning]
---

# AI協働におけるOutcome起点のCognitive Step分解

## このメモの位置づけ

`RN-20260826-120311-ai-outcome-scope-control-reasoning-review` に記録した実例から、
AIとの作業分担を設計する際の考え方として対話で導いた整理を残す。

元のRaw Noteは、Reasoningの検査とNext Stepの提案が同じ成果物へ混ざった際に、
AI Outcome分類を使ってCognitive Stepを分けた事例である。このメモでは、その事例を
一般化できるかもしれない設計原則候補として扱う。

登壇で説明するかは未決定である。詳しく説明する候補ではなく、一言だけ触れる候補、
またはRepositoryにのみ残す背景思想として保持する。

## 作業名だけでは境界が曖昧になる

作業分担は、通常「何をするか」という動詞で記述されやすい。

たとえば「Intentをレビューする」という作業名には、次の異なる認知作業が
入り得る。

- 記述内容を理解する
- 前提、矛盾、Reasoning Chainの飛躍を検査する
- 不足情報を補う
- 選択肢を追加する
- Next Stepを提案する
- 最善案を選ぶ
- 本文を書き換える

どれも広い意味では「レビュー」に見える。しかし、各作業が目指すOutcome、
成果物、完了条件および人間が引き受ける責任は同じとは限らない。

そのため、「何をするか」だけで作業を定義すると、「何をどこまで行うか」に
解釈の余地が入り、複数のCognitive Stepが一つの作業へ混ざりやすい。

## User Storyの`so that`を見るイメージ

Cognitive Stepを分ける際は、AgileのUser Storyにある`so that`を確認する
イメージが使える。

```text
As a Repository owner,
I want Codex to inspect the Intent,
so that I can trust the Reasoning and take accountability for it.
```

```text
As a Repository owner,
I want Codex to propose possible Next Steps,
so that I can compare options for subsequent work.
```

表面上はどちらも「Intentをレビューする」という一つの作業に見える。しかし、
一つ目のOutcomeはReasoningを信頼して責任を引き受けられる状態であり、二つ目の
Outcomeは次の行動候補を比較できる状態である。

`I want to`だけを見ると一つに束ねやすいが、`so that`が表す状態変化を見ると、
別のOutcome、別のCognitive Step、別のClosure条件として分けやすくなる。

## AIではCognitive Stepを細かめに分ける必要があるかもしれない

人間同士の共同作業では、途中で作業の性質が変わると、対話、担当者または成果物の
変化として境界が見える場合がある。

一方、AIは一つの依頼から複数のCognitive Stepを流暢に連続実行できる。

```text
理解する
  ↓
前提を推測する
  ↓
不備を指摘する
  ↓
選択肢を補う
  ↓
推奨案を選ぶ
  ↓
本文を書き換える
  ↓
Next Stepを決める
```

各StepのOutputが高品質でも、その境界が見えなければ、AIがどの時点から人間の
委譲していない判断へ入ったか、どのOutputまでReviewすれば現在の作業を閉じられるかが
分かりにくくなる。

そのためAIとの作業では、人間同士の場合よりもCognitive Stepを細かめに分け、
少なくとも次をStepごとに明示する必要があるかもしれない。

- `so that`に相当するOutcome
- AIが観察、推論または提案してよい範囲
- AIが変更してよい成果物
- Outputの格納先
- 人間がReviewする単位
- 人間の確認なしに次のStepへ進んでよいか
- Stepを閉じられる条件
- 最終的にAccountabilityを持つ人

## 細分化の目的

Cognitive Stepを分ける目的は、AIの能力を削ったり、Option生成を禁止したりする
ことではない。

Reasoningの検査も、Option生成も、Next Stepの提案も利用できる。ただし、それぞれを
別のOutcome、成果物、格納先、Review条件およびClosureへ接続する。

```text
AIの能力を制限する

ではなく

AIの能力ごとにReviewとAccountabilityの境界を置く
```

元の事例では、IntentのReasoningを検査するStepと、Next Stepの候補を生成するStepを
分け、提案は別Folderへ格納した。これにより、提案を捨てずにIntentのReview範囲を
限定できた。

## 現時点の設計原則候補

> 作業を動詞だけで分けず、User Storyの`so that`に相当するOutcomeで分ける。

> AIは複数の認知作業を流暢につなげるため、異なるCognitive Stepを識別可能にし、
> 成果物、格納先、Review、ClosureおよびAccountabilityの境界を置く。

この対話では、実践者の設計観を次のように表現した。

> 設計とは、Cognitive Stepを分けて管理できるようにすることである。

## 登壇で触れる場合の最小表現候補

> AIに「何をしてほしいか」だけでなく、「何のためのStepか」を伝える。
> `so that`が変わるなら、成果物とReviewも分ける。

または、AI Outcome分類を示した直後に次だけ添える。

> 一つの依頼にOutcomeが二つ混ざっていないかを見ると、AIとの仕事を分けやすくなります。

## 限界

- 一つの実践事例と対話から形成した設計原則候補であり、他のAI利用、利用者または
  組織で有効かは確認していない。
- Cognitive Stepを細かく分けるほど、作業設計、状態管理および運用のCostが増える。
  どの粒度で分けるべきかは未検討である。
- User Storyの`so that`はOutcomeを見分ける補助線として借用している。User Storyの
  一般的な書き方やAgile Practice全体を、このメモで定義するものではない。
- AI Outcome分類は網羅的・排他的な分類ではない。複数Outcomeを組み合わせることでは
  なく、異なるOutcomeの境界を識別できないことを問題候補としている。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
