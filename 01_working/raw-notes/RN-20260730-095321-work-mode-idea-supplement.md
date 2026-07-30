---
id: RN-20260730-095321-work-mode-idea-supplement
type: raw_note
title: "Workモード引き継ぎからのプレゼンテーション追加候補"
content_language: ja
created_at: 2026-07-30T09:53:21+09:00
content_origin: mixed
created_by: agent:codex
source_platform: other
capture_mode: import
imported_by: agent:codex
review_status: corrected
sanitization_status: sanitized
sanitization_checked_at: 2026-07-30T10:04:02+09:00
sanitization_checked_by: agent:codex
tags: [presentation-planning, delivery, ai-slop, service-quality, demand-pipeline, solution-strategy, value-stream]
---

# このメモの位置づけ

同じChatGPT会話をWorkモードが整理した引き継ぎ文書と、
`RN-20260730-093311-presentation-idea-inventory`を比較し、
既存の候補在庫に明示されていなかった追加候補だけを収集した。

引き継ぎ文書は元会話の要約とWorkモードによる展開を含む。
したがって、このメモの項目はユーザーが採用した内容ではなく、
今後比較できるように残した候補である。

# 追加候補

## Solution HypothesisをAIに固定しない比較

Platform Advisorを検討するとき、AI実装同士だけを比較しない。
同じTarget Frictionに対する選択肢として、次も並べる。

- Repositoryやドキュメントの情報設計を改善する
- 検索を改善する
- 判断基準をDecision Treeとして明示する
- Service Catalogを整理する
- Templateを提供する
- TrainingやEnablementを行う
- 人による相談、Office Hours、Triageを設ける
- Architecture ReviewやPlatform選定プロセス自体を改善する

この比較により、「AI Platform Advisorを作る」が価値仮説ではなく、
複数あるSolution Hypothesisの一つであることを示しやすくなる。

## サービス品質を四層で見る候補

既存の候補ネタ集では「基盤サービス品質」と「社内サービス品質」の二面を記録した。
Workモードの引き継ぎには、次の四層で扱う案が含まれている。

1. Internal Service
   - 利用者が何を得られ、なぜ価値があるか
2. Infrastructure Service
   - どのPlatform Capabilityがそれを提供するか
3. Development Support Service
   - 開発、Enablement、相談、支援を誰がどのように提供するか
4. Operational Service
   - 作られたApplicationやServiceを、その後どのように運用するか

二層モデルを四層へ広げるかは未決定である。
名称、境界、公開可能性、および既存の社内サービス設計との整合を確認してから採否を決める。

## Featureは価値ではなく検証手段

Deliveryで作るFeatureは、Value HypothesisやSolution Hypothesisを検証する手段として扱う。

候補フレーズ:

> Featureを完成させることが価値なのではなく、Featureを通じて価値仮説を検証する。

DiscoveryとDecisionを飛ばしてFeatureを高速生成することが、
AI Slopにつながるという説明を補強できる。

## Portfolioで使う動詞を増やす

既存の「選ぶ、捨てる、検証する」に加え、
Platform ServiceのPortfolio運営として次の判断を明示する案。

- Reject
- Revise
- Grow
- Standardize
- Continue
- Improve
- Retire

「捨てる」だけでは、実験から標準サービスへ育てる判断や、
一度Production化したServiceを継続評価して廃止する判断が見えにくい。
どの動詞を本編で使うかは、25分枠のStoryが決まってから選ぶ。

## Failure Demandとして観測する

AI導入後に増えた確認、訂正、差し戻し、例外対応、問い合わせを、
単なる追加作業ではなくFailure Demand候補として見る案。

確認する問い:

- AIが減らした作業とは別の場所で、後始末が増えていないか
- 人間の確認が、本来必要な高度判断か、誤りを補正する作業か
- Service利用が増えるほど、SupportやExceptionが不釣り合いに増えていないか

`Failure Demand`という用語を使用する場合は、定義と出典を確認する。

## Value Stream上の問いと測定点を対にする

仮説構築と検証の関係を、次の対句で見せる案。

> 仮説を作るときは、Value Stream上に問いを置く。

> 検証するときは、Value Stream上に測定点を置く。

Target Friction Checkと効果測定を同じMap上でつなげるための、
短い説明として利用できる可能性がある。

## Talk Contractを先に固定する

スライド構成を決める前に、短いTalk Contractを作る案。

- 誰に向けたセッションか
- 25分後に何を理解し、何を試したくなってほしいか
- 一つの中心命題は何か
- 中心命題を支えるために必須のEvidenceやExampleは何か
- 面白くても本編には入れないものは何か

候補となるCommunication Job:

> セッション終了時に、Platform Serviceを設計・運営する参加者が、
> AIで作れそうなIdeaをすぐFeatureにせず、
> Problem、Value、Solutionの仮説へ分けてValue Stream上で検証する
> 最初の一歩を選べるようになる。

これはStoryの採用案ではなく、今後の内容選別に使う判断基準候補である。

# ゲート設計に関する扱い

Workモードの引き継ぎには、Gate 0からGate 5までの具体的な通過条件案が含まれている。
しかし、既存の候補ネタ集では次の状態が人間により確認されている。

- Horizon 3から2、2から1のどのゲートで何を確認するかは、まだマッピングしていない
- 25分枠の本筋と候補区分は、全体を入れ替える前提の叩き台である

したがって、Workモード案を確定済みのDemand Pipelineとして追加しない。
今後ゲートを設計するときに比較できる「問いの在庫」としてのみ残す。

候補となる問い:

- どのTarget Frictionを変えたいのか
- ProblemからOutcomeまでReasoning Chainが通っているか
- 複数のSolution Optionを比較したか
- Slop Risk、測定点、Stop Conditionがあるか
- Experimentから価値あるLearningを得たか
- 組織が長期依存してよいService品質と運用責任があるか
- 継続投資、改善、廃止のどれを選ぶか

# 重複または追加を見送った内容

以下は既存のRaw NoteまたはArtifactですでに扱っているため、この補足では展開しない。

- Audience、カテゴリ、タイトル、キーワード
- Problem / Value / Solution / Slop Risk Hypothesis
- Mobius Outcome Deliveryへの対応
- Platform Advisorの基本例
- Reasoning Chain強度チェック
- 仮説、事実、前提の仕分け
- VSMとMBPMによる測定
- ボトルネック移動の読み方
- Session Journey
- 冒頭アンケートと中盤の選択
- 登壇準備Repoをお土産にする案
- 10-20-70、DORA、PEK応募分析など、出典確認が必要な外部主張
- 25分の時間配分案

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->

### CR-20260730-095606

- corrected_at: 2026-07-30T09:56:06+09:00
- corrected_by: human:kijima
- target: 「サービス品質を四層で見る候補」
- correction: 四層モデルは、AI開発基盤を題材に、自組織であるRed Hatでも十分にできていないという自虐エピソードを通じて説明する。AI開発基盤を考えるとき、技術者の視点は2のInfrastructure Serviceと3のDevelopment Support Serviceに止まりやすい。しかし、利用者が何を得てなぜ価値があるかを定義する1のInternal Serviceと、作られたApplicationやServiceをその後どう運用するかを設計する4のOperational Serviceもそろわなければ、サービスとして成立しない。2と3だけに集中した状態は、技術基盤の前後でValue Streamが断絶している状態として説明する。
- reason: 四層モデルを紹介する目的と、AI開発基盤におけるValue Streamの断絶との関係を明確にするため。Red Hat内部の評価を含む具体的な公開表現は、登壇資料へ採用する前に公開可能性と事実関係を再確認する。

### CR-20260730-095701

- corrected_at: 2026-07-30T09:57:01+09:00
- corrected_by: human:kijima
- target: CR-20260730-095606の出典と検証可能性
- correction: このエピソードはDailyで交わされた会話について、登壇者自身が記憶から要約したものである。参照可能な議事録、社内文書、録音などの出典は存在しない。したがって、Red Hat全体の状態を示す検証済み事実やEvidenceとしては扱わず、登壇者の限定的な経験談・自己観察としてのみ扱う。
- reason: 出典が存在しない会話の記憶を、組織的な事実や再検証可能な観測結果として扱うことを避けるため。

### CR-20260730-095939

- corrected_at: 2026-07-30T09:59:39+09:00
- corrected_by: human:kijima
- target: 「Portfolioで使う動詞を増やす」
- correction: Portfolio判断の前提として、今後のアプローチには大きく二つの戦略がある。一つは、実装前に価値仮説とReasoning Chainを十分に叩き、価値があると判断したものだけを作る戦略である。もう一つは、作って検証する学習速度を優先し、仮説や利用状況に合わなければRetireする戦略である。どちらか一方を組織全体で固定的に採用する必要はない。作業の重さ、Solutionの重厚さ、利用者依存が発生する速さ、変更や撤退の難しさなどに応じて、案件またはService候補ごとに使い分けてもよい。重要なのは、実装を始める前にどちらの検証戦略を取るかを意識的に決めることである。
- reason: Reject、Grow、Standardize、Retireなどの個別判断を列挙する前に、事前検証と事後学習のどちらへ重心を置くかという上位の戦略選択を明示するため。

### CR-20260730-100143

- corrected_at: 2026-07-30T10:01:43+09:00
- corrected_by: human:kijima
- target: 「Failure Demandとして観測する」
- correction: 元の会話でユーザーが検討していたのは、Ideaから検証、育成、標準化、廃止までをDemand Pipelineとして見せることである。`Failure Demand`はWorkモードが引き継ぎ文書を整理する際に追加したキーワードであり、ユーザー由来の登壇ネタではない。確認負荷、訂正、差し戻し、例外対応などが増えていないかを観測する考え方は残せるが、現時点ではそれらを`Failure Demand`と呼ばない。
- reason: Demand Pipelineという元の着想と、Workモードによって追加された用語を区別し、出典のない概念をユーザーの採用済みアイデアとして扱うことを避けるため。
