---
id: HYP-20260731-004119-relay-centered-session-story
type: hypothesis_episode
title: "リレーを中心にしたセッション構成ならAI SlopからVSMまでを一本道で伝えられる"
content_language: ja
created_at: 2026-07-31T00:41:19+09:00
created_by: agent:codex
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-07-31T00:55:25+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: not_assessed
relations:
  - type: derived_from
    target: RN-20260730-212352-discard-hypotheses-before-production-commitment
  - type: derived_from
    target: RN-20260730-224731-ai-acceleration-to-contract-first
  - type: derived_from
    target: RN-20260730-225227-relay-baton-handover-metaphor
  - type: derived_from
    target: RN-20260730-230242-communicating-invisible-handover
  - type: derived_from
    target: RN-20260731-003419-drop-api-contract-framing
  - type: references
    target: RN-20260730-140133-ai-outcomes-and-mbpm
  - type: references
    target: HYP-20260730-015718-ai-speed-requires-value-validation
---

# 仮説

PEK2026の25分トークを、AIによる部分的な高速化からリレーの
バトンパスへ進み、User Story、Acceptance Criteria、早期の中止判断、
VSMへ戻る順序で構成すれば、AI Slop、価値仮説、効果測定の関係を、
新しい専門用語を増やさず一本道で伝えられる。

公式の30分枠は、25分のトークと5分のQAとして扱う。

この文書は、2026年7月31日時点の最有力案を比較可能な形で保存する
スナップショットである。採用済みの登壇ストーリーではない。

## Mobiusでの位置づけ

`solution`

Audienceへ価値仮説と効果測定を伝えるための、説明順序と比喩に関する
Solution Hypothesisとして扱う。スライドや個々の発話は、この構成を
試すためのFeature候補であり、まだ採用していない。

## 現時点の構成候補

```text
1. AIは生成・実装を高速化する
   ↓
2. しかし速くなるのはValue Streamの一部
   ↓
3. 後続工程とハンドオーバーが詰まる
   ↓
4. リレーでは、走者だけ速くしても全体は速くならない
   ↓
5. 次の走者が走り続けられる受け渡し条件を先に決める
   ↓
6. User Storyで利用者とOutcomeを定義する
   ↓
7. Acceptance Criteriaで受け渡し条件を定義する
   ↓
8. 小さく試し、Productionへ約束する前に価値の弱い案を捨てる
   ↓
9. VSMでリレー全体が本当に速くなったか検証する
```

この構成の由来:

- AIによる局所的な高速化と後続工程への負荷移動:
  `RN-20260730-224731-ai-acceleration-to-contract-first`
- リレーとオーバーラップ区間の比喩:
  `RN-20260730-225227-relay-baton-handover-metaphor`
- ハンドオーバー、User Story、Acceptance Criteria、VSMの接続:
  `RN-20260730-230242-communicating-invisible-handover`
- Productionという約束の前に価値の弱い仮説を捨てる判断:
  `RN-20260730-212352-discard-hypotheses-before-production-commitment`
- API Contract表現を本編から外す判断:
  `RN-20260731-003419-drop-api-contract-framing`

## 中心となる説明候補

> AI時代に設計すべきなのは、速い作業だけではない。
> 次の人が走り続けられるバトンパスである。

> ハンドオーバーの完了条件は、渡し手が作業を終えたことではありません。
> 受け手が次の作業を問題なく遂行できる状態になったことです。

> User Storyで利用者とOutcomeを定義し、Acceptance Criteriaで
> 受け渡し条件を定義し、VSMで本当に流れたかを確認します。

## 本編の外へ置く候補

現時点では、次の内容を中心経路から外す。

- API的なContract First:
  思考の背景としてRepositoryへ残すが、本編の中心用語にはしない
- AIモデル比較:
  個人的な観測としてRaw Noteへ残す
- 「変革の70%以上が失敗する」という数字:
  今回の価値仮説を直接支えないため使わない
- Horizon 1-2-3:
  中止判断の背景にはあるが、25分のトークでは補足候補とする
- Repositoryの構造とHuman-AI協業の詳細:
  最後のお土産への導線に留める

AIに期待するOutcomeの5分類
`RN-20260730-140133-ai-outcomes-and-mbpm` は、一本道を妨げず
「AIで速く作る以外の使い方もある」と示せる場合に限り、1枚程度の
補助スライド候補として残す。

## 期待する兆候

- API Contractなどの追加概念を説明せずに、AI Slopがハンドオーバーと
  Value Stream全体の問題であることを説明できる
- リレーの比喩からUser Story、Acceptance Criteria、VSMへ自然に進める
- セッションタイトルに含まれる価値仮説と効果測定へ最後に戻れる
- Platform Engineerが、自分の業務における「次の走者」と
  「受け渡し条件」を一つ挙げられる
- 25分のトーク内で、具体例と持ち帰り可能な最初のActionを含められる
- 聴衆が中心メッセージを一文で再説明できる

## 検証方法

### 方法と対象範囲

- 方法:
  - 2026年8月14日頃まで構成を採用せずに置き、追加された代替案と比較する
  - 25分のトーク用Outlineまたは簡易Walkthroughを作り、所要時間と接続の
    飛躍を確認する
  - 可能であれば、Platform Engineeringの前提知識を持つ少人数へ
    Outlineを説明し、中心メッセージを再説明してもらう
- 対象・資料:
  - このHypothesis Episode
  - relationで参照したRaw Notes
  - 今後追加されるセッション構成候補
- 選定方法:
  - 採択済みProposalのタイトル、25分のトーク、想定Audienceとの整合を優先する
- 実施規模:
  - 自己レビュー1回以上
  - 実施可能な場合のみ少人数のWalkthrough

### GenAIの利用

- 利用内容:
  - Raw Notesから構成候補を再構成する
  - 接続の飛躍、概念数、時間超過、タイトルからのDriftをレビューする
  - 代替構成との比較表を作る
- 実際に確認した資料・記録:
  - relationで示したRaw Notes
  - `HYP-20260730-015718-ai-speed-requires-value-validation`

## 比較基準

約2週間後に、現案と代替案を次の基準で比較する。

1. タイトルの「価値仮説と効果測定」へ自然に戻れるか
2. AI Slopが起きる因果を説明できるか
3. Platform Engineerが週明けに試せるActionを持ち帰れるか
4. 新しい概念の説明コストが少ないか
5. 25分のトークに収まるか
6. 一本の話として記憶に残るか
7. VSMが最後に付け足された測定手法ではなく、因果の検証方法として
   必要になっているか

## 結果

`not_tested`

### 実際に観測したこと

複数のRaw Noteから、AI高速化、ハンドオーバー、リレー、User Story、
Acceptance Criteria、早期の中止判断、VSMを接続する構成候補が形成された。

現時点では、この構成を25分のトークとしてWalkthroughした結果、Audienceの理解、
代替構成との比較結果は記録されていない。

## 解釈

このスナップショットを残す目的は、現案を固定することではない。
約2週間後により筋の良い構成が現れた場合、当時の最有力案と比較し、
何を改善したのか説明できるようにすることである。

Codexによる検索で個々のRaw Noteを再発見することは可能だが、その時点で
自然に見えていた順序、不採用にした概念、比較基準まで同じ形で再構成される
とは限らない。そのため、現在の構成をSolution Hypothesisとして保存する。

## 限界

- 選定上の偏り:
  登壇者とGenAIの会話から形成された構成であり、Audienceへの直接確認を
  経ていない
- 未確認の証拠:
  25分のトーク用Walkthrough、第三者レビュー、参加者による再説明、当日の反応
- 一般化できない範囲:
  リレーの比喩がすべてのPlatform Engineeringのハンドオーバーに
  適用できるとは結論できない
- 現時点の制約:
  この文書は採用済みArtifactではなく、スライド制作開始の指示でもない

## 公開安全性確認

- checked_at: 2026-07-31T01:11:50+09:00
- checked_by: agent:codex
- result: `not_needed`
- scope:
  このHypothesis Episodeの本文、frontmatter、relationの組み合わせを、
  セッション枠の内訳（25分のトークと5分のQA）へ明確化した時点で再確認した
- finding:
  顧客、案件、非公開の個人、商用条件、内部System、認証情報、
  再識別につながる組み合わせは確認されず、本文の変更や削除は行っていない
- limitation:
  公開安全性の確認は、仮説の正しさ、検証完了、構成の採用を意味しない
