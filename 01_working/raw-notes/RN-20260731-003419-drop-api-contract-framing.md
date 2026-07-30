---
id: RN-20260731-003419-drop-api-contract-framing
type: raw_note
title: "API Contract表現を本編から外す判断"
content_language: ja
created_at: 2026-07-31T00:34:19+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-31T00:36:19+09:00
sanitization_checked_by: agent:codex
tags: [presentation-planning, design-decision, idea-rejection, audience, contract-first, handover, metaphor]
---

# メモ

## 検討していた表現

Platform Serviceの利用者体験とハンドオーバーを説明するために、
API設計の `Contract` および `Contract First` の概念を使うことを
検討していた。

背景にあった考え:

- 利用者はPlatformの内部実装ではなく、Platform Teamとの接点を体験する
- 接点では入力、出力、前提条件、保証、責任、タイミング、意味、
  制約などが問題になる
- 基盤、開発支援、運用を個別に積み上げるのではなく、最初に利用者へ
  提供したいOutcomeと体験を定義し、そこから各Serviceを逆算したい
- 作業の中心ではなく、次の作業者へどう渡せるかをScopeの中心に置きたい

この構造は、APIの内部実装より先に利用者との接点を定義する
Contract Firstとよく似ている。

## 本編から外す判断

25分のセッション本編では、API的な `Contract` の概念を中心用語として
使わない。

理由:

- `Contract` はAPI設計、Interface仕様、Schema、Contract Testingなどの
  用語として受け取られやすい
- 聴衆がAPIの知識や経験を共有しているとは限らない
- Platform Engineering寄りの聴衆に、意図している広いハンドオーバーの
  意味が伝わらない可能性がある
- `Contract` の意味を説明するために、別の概念説明が必要になる
- API Contractとの共通点と相違点を説明すると、本題から外れる
- 25分の中では、価値仮説、AI Slop、VSMの実践へ時間を使いたい
- リレーのバトンパスの方が、前提知識なしで同じ構造を伝えやすい

これはContractという考え方自体を否定した判断ではない。

> 思考の背景としては残すが、Audienceへ届ける表現としては採用しない。

## 残す内容と捨てる表現

### 本編から捨てるもの

- `Contract First` を中心概念として説明する
- API Contractとの対応関係を詳しく説明する
- Platform ServiceをContractとして定義する
- Human-AI Contract Designを本編で展開する

### 本編に残すもの

- ハンドオーバーは成果物を渡す一点ではない
- 次の作業者が問題なく作業を開始・遂行できる状態を渡す
- 作業の完了条件は、受け手が次へ進めたかで決まる
- 利用者とOutcomeを実装より先に考える
- 受け渡し条件を先に定義する
- 基盤、開発支援、運用を利用者のOutcomeから逆算する
- VSMで実際に次へ進めたかを検証する

つまり、Contractという語を外しても、その語を使って考えていた設計原則は
残す。

## Audience向けの翻訳

API Contractを説明する代わりに、リレーのバトンパスを使う。

```text
AIで一人の走者が速くなる
  ↓
バトンパスで詰まる
  ↓
全体のタイムは縮まらない
  ↓
次の走者が走り続けられる条件を先に考える
  ↓
User Storyで誰の何を良くするかを決める
  ↓
Acceptance Criteriaで受け渡し条件を決める
  ↓
VSMで本当に流れたか確認する
```

用語の翻訳:

```text
Contract
  → 受け渡し条件

Contract First
  → 次の走者が走り続けられる条件を、走り方より先に決める

Interfaceの成立
  → 受け手が次の作業を開始・遂行できる

Contractの検証
  → VSMで実際の待ち時間、手戻り、次工程への移行を観測する
```

User StoryとAcceptance Criteriaを使うことで、APIの前提知識なしに、
利用者、Outcome、受け渡し条件、実装の順序を説明できる。

```text
User Story
  = 誰が、何を可能にし、なぜ必要なのか

Acceptance Criteria
  = 次の走者が走り続けられる受け渡し条件

Implementation
  = 条件を満たすための走り方

VSM
  = 個々の走者ではなく、リレー全体が速くなったかを見る
```

## 現時点のトーク候補

> AIで一人ひとりの作業を速くしても、バトンパスが変わらなければ、
> Value Stream全体は速くなりません。

> ハンドオーバーの完了条件は、渡し手が作業を終えたことではありません。
> 受け手が次の作業を問題なく遂行できる状態になったことです。

> 次の走者が走り続けられる条件を、走り方より先に決めます。

> User Storyで利用者とOutcomeを定義し、Acceptance Criteriaで
> 受け渡し条件を定義し、VSMで本当に流れたかを確認します。

## この判断のScope

この不採用判断は、PEK2026の25分セッション本編における表現の選択に限る。

Contractに関するRaw Noteは、思考の由来や詳細を確認できるRepository上の
背景資料として残す。別のAudience、長いセッション、API設計を扱う場では、
Contract Firstを再び中心概念として使う可能性がある。

今回捨てたのはアイデアそのものではなく、特定のAudienceと時間枠に対する
伝え方である。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
