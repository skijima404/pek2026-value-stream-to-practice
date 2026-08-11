---
id: HYP-20260804-183208-audience-actionable-ai-slop-value
type: hypothesis_episode
title: "AudienceはAI Slopを制御するActionを持ち帰ることに価値を感じる"
content_language: ja
created_at: 2026-08-04T18:32:08+09:00
created_by: agent:codex
hypothesis_scope: session
hypothesis_level: value
status: reviewed
reviewed_at: 2026-08-11T15:59:06+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - case_recollection
  - explicit_validation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260730-015714-session-goal-and-journey
  - type: derived_from
    target: OBS-20260730-015715-accepted-direction-and-delivery-scope
  - type: derived_from
    target: OBS-20260730-015716-audience-and-value-problem-statements
  - type: derived_from
    target: OBS-20260805-223704-audience-problems-and-ai-slop-interest
  - type: derived_from
    target: OBS-20260805-225027-function-evaluation-poc-business-use-gap
---

# 仮説

対象Audienceは、AIによって作る量または速度が増えても価値、利用、効果または
下流負荷を判断できないという問題に関心を持ち、AI Slopをゼロにする方法ではなく、
未検知・未制御のまま下流へ流さないための見方と最初のActionを持ち帰ることに
価値を感じる。

## 知識の成立根拠

作成者は、Audienceの課題候補として、作るべきものの判断、Platform Serviceの
価値説明、利用されない理由、AI導入後の効果測定およびIDP体験の悪化を記録している。
また、セッション成功条件として、参加者が試したいと思うこと、または一つでも
持ち帰って試すことを記録している。

その後、3人へのヒアリングで、価値・機能の選択、AI開発基盤の着手、精度の低い
受領物による仕事の増加および効果説明に関する問題が記録された。同じ3人は、
未検知・未制御のAI Slopを流さない方法を聞きたいと回答した。

このヒアリングは対象者全体の需要を示す調査ではなく、限定した3人への
`explicit_validation`として扱う。

## Mobiusでの位置づけ

`session` scopeの`value`

誰のどの問題を扱い、セッション後にどの変化が生じればAudience価値とみなすかを
確認するValue Hypothesisである。

## 期待する兆候

- 対象者が、AIによる作成速度以外に、選択、確認、手戻りまたは下流負荷の問題を挙げる
- 対象者が、AI Slopの発生箇所またはRiskを自身のValue Streamで一つ特定できる
- 対象者が、持ち帰って確認または試行する最初のActionを一つ選べる
- 「良い話だった」という感想だけでなく、実施意向または後日の試行が確認できる

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | 対象Audienceが、AI Slop、価値判断、効果測定または下流負荷に関係する問題を実際に持つ | critical | OBS-20260805-223704-audience-problems-and-ai-slop-interest, OBS-20260805-225027-function-evaluation-poc-business-use-gap | partially_checked | supports | contextual | 3人から関係する問題の回答を得たほか、別の一人への直接Interviewで機能評価型AI PoCをBusiness活用判断へ接続できない問題を確認した。一方、選定方法、想定Audienceとの一致、課題の保有率、頻度、影響および優先順位を確認していない |
| U2 | 対象Audienceが、AI Slopを未検知・未制御のまま流さない方法を知ることに価値を感じる | critical | OBS-20260805-223704-audience-problems-and-ai-slop-interest | partially_checked | supports | contextual | 同じ3人全員が聞きたいと回答したが、質問条件、他のテーマとの優先順位、理解またはActionへの移行および対象Audience全体の需要を確認していない |
| U3 | セッション後に、対象者が自身の現場で確認すべきRiskまたは箇所を特定できる | high | none | not_checked | unknown | unknown | 理解したという自己評価と、具体的な識別能力を区別して確認していない |
| U4 | 対象者が、持ち帰って試すActionを一つ選び、実施する意向を持つ | critical | none | not_checked | unknown | unknown | 満足度、実施意向および実際の行動の関係を確認していない |
| U5 | 一部の対象者が、セッション後に選んだActionを実際の組織で試す | medium | none | not_checked | unknown | unknown | 後日行動を追跡できる手段、期間および選択Biasを定義していない |

## 検証

- アプローチ: `interview`

### 方法と対象範囲

- 方法:
  - セッション前の少人数Interviewまたは既存の対象者記録から`U1`と`U2`を確認する
  - Walkthroughまたは当日の短い応答から`U3`と`U4`を確認する
  - 任意のFollow-upから`U5`を確認する
- 対象・資料: 未選定
- 選定方法: Platform Serviceの企画、提供または利用に関与する想定Audienceを優先する
- 実施規模: 意思決定に必要な範囲で小さく開始し、母集団全体へ一般化しない

### 実施した限定的なヒアリング

- 方法:
  3人へ、価値判断、効果測定、確認作業または下流負荷に関係する問題を確認し、
  未検知・未制御のAI Slopを流さない方法を知りたいかを質問した
- 対象・資料:
  `RN-20260805-223703-audience-ai-slop-interviews`に保存した回答要約
- 選定方法:
  この記録では確認できない
- 実施規模:
  3人。母集団への一般化を目的としない

### 実施したAI PoC事例の本人Interview

- 方法:
  開発関連AIのPoCについて、その状況を説明した本人へ、PoCの内容、得られた結果、
  社内およびBusiness活用への接続を確認した
- 対象・資料:
  `RN-20260805-225026-ai-poc-business-use-interview`に保存した回答要約。
  PoCの一次資料は未確認
- 選定方法:
  この記録では確認できない
- 実施規模:
  一人へのInterview、一組織についての事例記憶

### GenAIの利用

- 利用内容: Interview質問、回答分類、自由記述の整理および反証候補の抽出
- 実際に確認した資料・記録: relationで示したRepository Nodeと、保存したヒアリング回答

## 結果

`inconclusive`

### 実際に観測したこと

3人へのヒアリングでは、Platform Engineeringで最初に作る機能、AI開発基盤の着手点、
精度の低い受領物による仕事の増加、および経営報告での効果説明に関する問題が
回答に含まれた。

同じ3人は、未検知・未制御のAI Slopを流さない方法を聞きたいと回答した。これにより、
U1とU2は限定した3人の範囲で`partially_checked / supports / contextual`となった。
自身の現場でRiskを特定するU3、Actionを選ぶU4および実際に試すU5は確認していない。

別の一人への直接Interviewでは、開発関連AIのPoCで機能評価とReport作成を行っても、
社内またはBusinessでの活用判断へ接続できなかった事例が回答された。これはU1の
問題に関係する追加Evidenceだが、本人が今回のSession内容を聞きたいと回答した
記録ではないため、U2のEvidenceにはしない。

## 解釈

限定した3人の回答は、問題の存在と対処方法への関心を分けて確認する最初のSignalに
なる。一方、「聞きたい」という回答を、説明方法の有効性、Actionの選択または実際の
行動へ拡張しない。

このValue Hypothesisは、採択済みProposalの正しさ、セッション構成の有効性、
またはAudience全体の需要を示すものではない。Session SolutionおよびFeatureを
比較する時の親となる価値仮説として扱う。

## 限界

- 想定Audienceは作成者の見立てであり、実際の参加者構成と一致するとは限らない
- 3人の選定方法、Role、想定Audienceとの一致および質問条件を確認できない
- AI PoC事例は一人の回答に基づき、一次資料、他の関係者および原因を確認していない
- 課題の頻度、影響、優先順位および他のテーマとの比較を確認していない
- 関心を示すこと、Actionを選ぶこと、実際に試すことは別のSignalである
- 当日の反応だけでは、組織での適用またはOutcomeを確認できない
- この仮説は登壇内容または評価方法の採用決定ではない

## 次の判断

- 判断: `validate_further`
- 判断の対象範囲: U3のRisk特定とU4の最初のAction選択
- 次に進めること:
  Walkthrough、当日の短い応答、または登壇後アンケートのいずれかで、対象者が
  Riskを一つ特定し、Actionを一つ選べるかを確認する。U5の実行追跡は現段階の
  必須条件にしない

## 公開安全性確認

- checked_at: 2026-08-11T15:59:06+09:00
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
