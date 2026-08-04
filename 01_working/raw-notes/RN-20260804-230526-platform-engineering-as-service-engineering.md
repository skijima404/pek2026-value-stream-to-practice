---
id: RN-20260804-230526-platform-engineering-as-service-engineering
type: raw_note
title: "AI時代のPlatform EngineeringをService Engineeringとして捉える"
content_language: ja
created_at: 2026-08-04T23:05:26+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-04T23:10:38+09:00
sanitization_checked_by: agent:codex
tags: [ai-slop, contract-first, platform-advisor, platform-engineering, service-contract, service-engineering, work-design]
---

# メモ

2026年8月4日に、AI Slop、Platform Advisor、Prompt TechniqueおよびBotの
Service DesignについてCodex上で対話した内容を記録する。

実践者は、Platform EngineeringをService Engineeringとして捉えるFramingに
非常に腹落ちすると述べた。一方、このFramingを今回のSessionでどこまで主張できるか、
またAudienceが説明についてこられるかは未確認である。

以下は実践者のPlatform Engineering経験、別のAI-native Repositoryを設計した経験、
および対話上のSynthesisに基づく発展中の考えである。Platform Engineeringの確立した
唯一の定義、他のPractitionerへのInterview結果またはAudience検証結果ではない。

## 中心となったFraming

対話では、次の表現を仮置きした。

> Platform Engineeringは、Platformを作る工学ではなく、Platformを通じて利用者が
> 安全にOutcomeへ進めるServiceを設計、運用、改善する工学である。

このFramingでは、Platform Teamが作るものを次のように分ける。

- Infrastructure、API、Portal、Golden PathおよびBotはFeature
- 利用者へ何を約束するかがService Contract
- 利用者が安全に次の判断または作業へ進めることがService Outcome
- 提供側と利用側を接続するものがValue Stream
- 約束を満たしているかを見るものがObservabilityとMetric
- 例外、支援、更新、訂正および廃止まで含むものがOperating Model

概念上の接続は次のとおりである。

```text
Platform Feature
API / Portal / Golden Path / Advisor
          ↓
Platform Service
誰に何を約束し、どこまで責任を持つか
          ↓
利用者の行動・体験
安全に次の開発・判断へ進める
          ↓
組織Outcome
速度、品質、学習、持続可能性
```

## Platform as a Productとの関係

対話では、Platform as a ProductとService Engineeringを競合する考えとして扱わず、
異なる問いへ答えるものとして整理した。

- Product Thinking:
  誰のどの問題を解き、どのOutcomeへ投資するかを決める
- Service Engineering:
  その価値をContract、Flow、運用、支援および検証を通じて継続的に成立させる
- Platform Engineering:
  技術Capabilityと組織的なService Deliveryを統合する

これは対話上の暫定整理であり、各用語の一般的な定義または境界を独立調査していない。

## BotとAdvisorの違い

実践者は、Dataの解説役となるNotebookLM的なBotは比較的作りやすいと考えている。
与えられたSourceについて、何が書かれているかを検索、要約および解説する範囲である。

一方、Advisorを名乗る場合は、利用者から与えられたContextとService側の世界を照合し、
少なくとも次を扱う必要があると考えた。

- 何が存在するか
- 何が存在しないか
- 何が適用できるか
- 何が適用できないか
- 判断に必要な情報のうち、何が不足しているか
- 不足時に追加質問、保留、拒否またはEscalationのどれを行うか
- 利用者が次にどのActionへ進めるか

特に「ない」には複数の意味がある。

- 利用者がまだ情報を提供していない
- Governing Sourceに記載がない
- 検索では見つけられなかった
- 現在のPlatformでは提供していない
- 対象Contextには適用できない
- 判断に必要なEvidenceが不足している

これらを区別せず、Source内で見つからないことを、現実に存在しないことへ変換すると、
Advisorは誤ったNegative Assuranceを与え得る。

## AI Service Designとしての世界設計

実践者は、Bot的なものを作る時に相当量の「教師データ」を作ると述べた。別の
Practitionerへ作り方を聞いた際には、同程度の準備をしていないように感じたが、
対象人数、作成方法および比較尺度は記録していない。

実践者が教師データと呼んだものは、ModelのFine-tuning Dataだけを意味しない。
質問と期待回答、Scenario、Role、Contract、成功・失敗条件およびKnown-badな挙動を
用意し、AIへ世界観を一式渡す設計を含む。

対話では、AI Service Designを次のように整理した。

```text
世界に何が存在するか
誰が登場するか
誰が何を知っているか
何を判断してよいか
何を約束できるか
何が不足・例外・失敗か
どこで人へ戻すか
何を成功として観測するか
```

AIへ世界を渡さない場合、AIは利用者の一つのPromptから世界全体を推測する。
その結果、存在しない前提の補完、Roleや責任の取り違え、一般論への退避、別の
Ontologyの利用および対応範囲外へのもっともらしい回答が起き得る。

実践者が設計した別のAI-native Repositoryでは、世界を次のAssetへ分解していた。

- DomainまたはFailure Model
- PersonaおよびRole Contract
- 固定Context
- Expected Output
- Known-goodおよびKnown-bad Fixture
- Observability
- Regression Validation

この事例は、個々のPromptへ毎回世界を記述するのではなく、必要なPrompt Techniqueを
Durable Assetへ外在化する考えと整合する。ただし、異なるPrompt習熟度の利用者で
同じOutcomeが得られるかを比較したものではない。

## OpenなBot InterfaceとSlop

最初の検討では、AIに期待する5つのOutcomeのうち、1「速く作る」と2「広く探す」が
特にSlopを起こしやすい可能性を考えた。

```text
1. 速く作る
2. 広く探す
3. 分かるように解釈する
4. 選べるように整理する
5. 本当に筋が通るか疑う
```

対話を進めると、Outcome分類だけでSlop Riskの大小は決まらないと考えるようになった。

- 速く作ると、未検証Outputの流量が増え得る
- 広く探すと、見落としまたは古い情報を検知しにくい
- 解釈すると、利用者Contextを取り違え得る
- 整理すると、重要な選択肢または判断軸を落とし得る
- 疑うと、問題がないという偽の安心を与え得る

Botで特に問題になるのは、Blank Chatが「何を聞いてもよい」「何についても
答えられる」という広いDemand Surfaceを利用者へ見せる一方、実際のKnowledge、
判断能力および責任範囲は有限であることである。

```text
利用者から見えるDemand Surface
「何でも聞ける」
          ↓ mismatch
実際のService Coverage
「このSource、このJob、この条件だけ」
```

対話では、BotをService化するとは、自由入力を完全になくすことではなく、受け取った
要求を少なくとも次へ分類できるようにすることだと考えた。

- 対応可能
- 情報不足のため追加質問が必要
- 対応範囲外
- Source Coverageが不明
- Riskが高く、人へのEscalationが必要

良いAdvisorは何でも答えるBotではなく、何を答えられるか、何が不足しているか、
何を答えてはいけないかを判定できるServiceである、という表現まで整理した。

## Prompt Technique依存

「AIの挙動を理解して使いこなす」という表現だけでは、問題を個人のAI Literacyまたは
Prompt Techniqueへ戻してしまう。

Platform Advisorが良いPromptを書ける人にだけ良い助言を返すなら、Platform選択の
負荷をPrompt作成の負荷へ置き換えただけになる可能性がある。

Service側が、利用目的、必須Context、Source、適用条件、非対応範囲、追加質問、
保留およびEscalationを持つことで、利用者が毎回Prompt内で世界を説明する必要を
減らせる。

対話では、次の表現を候補とした。

> AIを使いこなすのではなく、AIを含む仕事を設計する。

> AIの揺れを個人の技量で吸収せず、仕事の境界、検証およびHand-offへ織り込む。

> AI Service Designとは、AIへ回答方法を教えることではなく、Reasoningしてよい
> 世界、約束してよい範囲、分からない時の戻り先を設計することである。

## AI Slopとの接続

AIはPlatform Featureの候補または実装を速く作れる。Service Designを行わずに
Featureだけを利用者へ渡すと、未定義の意味、責任、検証および例外対応を利用者または
後続Actorが引き受ける可能性がある。

```text
AIでFeatureを速く作れる
  ↓
Service Designを飛ばしやすくなる
  ↓
未定義の責任・検証・例外が利用者へ移る
  ↓
下流負荷としてSlopが体験される
```

この見方では、AIが全く新しい問題を作ったというより、以前から存在したPlatform
FeatureとPlatform Serviceの混同を、高速化によって顕在化させた可能性がある。

対話では、次の中心表現を候補とした。

> AI時代にPlatform Engineeringへ必要なのは、より速くPlatform機能を作ることだけ
> ではない。利用者への約束と、そこへ至るValue Stream全体をServiceとして設計する
> ことである。

短い対比としては、次を置いた。

> AIが速くするのはFeature開発。利用者へ価値を届けるのはService Engineering。

## 既存Practice Solutionとの接続

このFramingを用いると、現在別々に置いているPractice Solutionを、Service
Engineeringの構成要素として説明できる可能性がある。

- Lean Startup admission:
  どのFeature候補をServiceとして育てるかを選別する
- DVS/OVS observability:
  提供側のDeliveryと利用側の体験・追加作業を接続する
- Service Contract:
  対象利用者、Outcome、提供範囲、責任境界および例外を定義する
- Outcome-first AI配置:
  AI Capabilityを期待OutcomeとValue Stream上の課題から配置する
- 二段階Metric分析:
  Flow上の変化と最終的なOutcome Qualityを分けて確認する

この接続は対話上のReasoned Synthesisである。各Solutionの既存Hypothesis Resultを
変更せず、Service Engineeringという上位概念が実務上またはAudience理解上有効かを
検証したものでもない。

## Keywordは別途検証する

実践者は、基礎となる考えと、それを`Service Engineering`と呼ぶことを分けると
明示した。

- 基礎となる考え:
  AIで作ったFeatureをそのまま渡さず、利用者、Outcome、約束、責任境界、例外、
  運用および改善を含む社内サービスとして設計する
- 未検証のKeyword:
  この考えを`Service Engineering`と呼び、Platform Engineeringの上位または中心の
  Framingとして説明する

実践者本人が`Service Engineering`という表現に腹落ちすることは、Audienceにも
理解しやすいこと、一般的な用語法として適切であること、またはSessionで採用すべき
ことを意味しない。

別途確認する必要がある不確実性として、次を挙げた。

- Keywordだけで、社内サービスとして設計・運営する意味が伝わるか
- 別の既存概念、職種または方法論として解釈されないか
- Product Thinking、Platform EngineeringおよびService Engineeringの関係を
  追加説明なしで理解できるか
- 「社内サービスとして設計する」という表現より説明Costが下がるか、上がるか
- AI Slopと下流負荷の中心説明を強めるか、抽象概念を増やして妨げるか

検証方法、対象者、比較表現および採用基準は、このRaw Noteでは決めていない。
KeywordはSession Artifactへ採用せず、別のValidation対象として保留する。

## 現時点の位置づけ

実践者本人には、このFramingは非常に腹落ちしている。一方、次は未確認である。

- Platform EngineeringをService Engineeringとして捉える表現が、Audienceに通じるか
- Product Thinking、Service EngineeringおよびPlatform Engineeringの関係を、
  追加説明なしで理解できるか
- 25分のSessionで新しい抽象概念を増やす価値があるか
- Platform PractitionerがこのFramingを自分の業務へ適用できるか
- このFramingが既存のPlatform Engineering定義または議論とどう関係するか
- AI Slopの中心説明として採用するか、背景のSynthesisに留めるか

したがって、このRaw Noteは、実践者が強く納得する考えと、その成立理由を保存する。
`Service Engineering`というKeywordは別途検証するまで保留し、Session Artifactへの
採用、Analysis NodeへのPromotionまたはRisk Decisionはこの記録では行わない。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
