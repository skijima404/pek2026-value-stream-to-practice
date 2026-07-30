---
id: RN-20260730-101222-discovery-gap-and-talk-continuity
type: raw_note
title: "Discoverの欠落感と前回登壇からの接続"
content_language: ja
created_at: 2026-07-30T10:12:22+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-30T10:15:12+09:00
sanitization_checked_by: agent:codex
tags: [presentation-planning, discovery, decision, delivery, reasoning-chain, session-continuity, field-observation, outcome-delivery]
---

# このメモの位置づけ

PEK2026登壇の新しいネタとして、登壇者の現場感覚、
Reasoning Chain強度チェックへの導入、
前回のクラウドネイティブ会議登壇との接続案を記録する。

現場感覚は調査結果ではない。
PresalesとProject Deliveryを通じて接した範囲に限られる、
登壇者個人の経験と印象である。

# Discover / Decide / Deliveryに関する感覚値

## Discover

Presalesで出会う顧客およびProject Deliveryで出会う顧客の中で、
Discoverをきちんと実施しているProjectに出会うのは、
登壇者の感覚値では3年に一度程度である。

この数字には、母数、観測期間、判定基準を伴う調査はない。
頻度の一般化や統計的主張には使わず、
Discoverが想像以上に希少であるという個人的な現場感覚として扱う。

## Decide

Decideに相当する意思決定は、すべてのProjectで行われている。

ただし、次の点は不明確である。

- Discoveryで形成したProblem HypothesisやValue Hypothesisを受けたDecisionか
- 複数のSolution Hypothesisを比較したか
- 何を検証すれば選択が妥当だったと判断できるかを定義したか
- 単に実装するSolutionを選んだことをDecideと呼んでいないか

したがって、Decideしていることと、
仮説検証としてDecideできていることは分けて扱う。

## Delivery

Deliveryに関する議論は豊富である。

- 何を実装するか
- どの技術を使うか
- どのように設計、開発、テスト、リリースするか
- どう自動化し、どのように速く作るか

AIは、この既に議論の豊富なDeliveryをさらに高速化する。

# 参加者へ伝える知見候補

候補となる強い言い方:

> 皆さんも、まずは「自分たちはDiscoverをやっている」と思わない方がいいです。
> やっていない前提で、一度確かめてみてください。

この言い方の目的は、参加者を否定することではない。
次の違いを自己点検してもらうことである。

- DiscoveryらしいMeetingやWorkshopを実施した
- Problem HypothesisとValue Hypothesisを形成した

また、Decideについても次の違いを示す。

- Solutionを選択した
- Solution Hypothesisを比較し、検証方法を定めた

「3年に一度」は、参加者がDiscoverの希少さを感覚的につかむための経験談として使う。
調査結果であるかのような見せ方はしない。

# Reasoning Chain強度チェックへの導入

この現場感覚から、Reasoning Chain強度チェックの必要性を導入する。

候補となる流れ:

1. Deliveryの議論は豊富である
2. Decideもしているように見える
3. しかし、そのDecisionがDiscoveryで見つけたProblemやOutcomeにつながっているかは怪しい
4. 当事者はつながっているつもりでいるため、欠落に気づきにくい
5. AIは、その確認を待たずにDeliveryを高速化する
6. そこで、実装前にReasoning Chainの論理強度を確認する

Reasoning Chain強度チェックの役割:

> Discover、Decide、Deliveryが、本当に一本の因果でつながっているかを可視化する。

候補となる説明:

> Discoverをやったつもり、Decideをしたつもりでも、
> Deliveryまでの理屈が本当につながっているとは限りません。
> しかもAIは、その確認を待たずにDeliveryを猛烈に速くします。
> そこで、人間が作った価値仮説とSolution HypothesisのReasoning Chainを、
> 実装前にAIにも叩かせます。

重要な制約:

> Reasoning Chainが通ったから仮説が正しいわけではありません。
> ただし、筋が通っていない仮説を、検証せず高速に実装することは防ぎやすくなります。

# 前回登壇との接続

前回のクラウドネイティブ会議では、
Kotter Step 1の「危機意識を高める」を手がかりに、
「なぜやるのか」を明確にし、Platform Serviceの価値とScopeを定義する話をした。

公開資料:

- https://speakerdeck.com/skijima404/platform-engineeringhanazesukerusinainoka
- https://note.com/skijima/n/n9bf27a8cb0ae

今回の登壇は、そのさらに上流を扱うという位置づけ候補である。

- 前回:
  - なぜやるのかを明確にする
  - 誰のどんな問題を扱うかを定義する
  - 価値に合わせてScopeを決める
- 今回:
  - そのProblemや価値を、どのようにDiscoverしたのか
  - Value Hypothesisをどのように形成したのか
  - Solutionを仮説としてDecideできているか
  - Delivery後に何を観測して検証するか

候補となる接続:

> 前回は、「なぜやるのかを明確にし、
> 価値に合わせてPlatform ServiceのScopeを決めましょう」という話をしました。
> 今回は、そのさらに上流です。
> そもそも、そのProblemや価値はどうDiscoverしたのでしょうか。
> 選んだSolutionは、価値につながる仮説としてDecideできているでしょうか。

Reasoning Chainへの接続候補:

> 前回は「なぜやるのかを書きましょう」とお話ししました。
> しかし、そのWhyがProblemからOutcomeまで本当につながっているかは、
> 別途確認しなければなりません。
> そのために今回はReasoning Chainをチェックします。

# 前回登壇を紹介する場合の条件

- 前回参加者には続編だと分かる
- 初見の参加者にも、今回単独で問題設定が理解できる
- `Kotter Step 1`という固有名だけで接続しない
- まず「なぜやるのかを明確にする話」と日本語で説明する
- 前回の内容を長く再説明しない
- 接続は30秒程度の短い位置づけに留める

今回のEventは、前回のクラウドネイティブ会議と参加者層に一定の連続性がある可能性がある。
ただし実際の重複参加率は不明であり、前回登壇の視聴を前提にしない。

# 未決事項

- 「Discoverをきちんと実施している」の判定条件を、どこまで明文化するか
- 「3年に一度」という感覚値を本編で使うか
- 強い言い方を、参加者への否定ではなく自己点検として成立させる表現
- 前回登壇との接続を本編に入れるか
- 前回登壇のSlideや図を再利用するか、口頭だけで接続するか
- Reasoning Chain強度チェックを、今回の最初の実践例として扱うか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
