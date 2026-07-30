---
id: RN-20260730-093311-presentation-idea-inventory
type: raw_note
title: "PEK2026プレゼンテーション候補ネタ集"
content_language: ja
created_at: 2026-07-30T09:33:11+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
review_status: corrected
sanitization_status: sanitized
sanitization_checked_at: 2026-07-30T09:44:30+09:00
sanitization_checked_by: agent:codex
tags: [presentation-planning, delivery, ai-slop, value-hypothesis, vsm, platform-advisor, reasoning-chain, demand-pipeline, outcome-delivery]
---

# このメモの位置づけ

参照されたChatGPT会話から、PEK2026登壇のDelivery候補を収集した。
このメモはストーリーやスライド順の採用決定ではなく、後から選別するための候補在庫である。

会話には、人間が直接述べた着想、AssistAが展開した案、未確認の外部主張が混在している。
以下では、それらを同じ確度の情報として扱わない。
公開時に組織や案件を推定できる可能性がある文脈は一般化した。

既存のAudience、価値仮説、Journeyに関するメモと重複する箇所は、Deliveryを考えるために必要な範囲だけ再掲する。

# ユーザーが明示または採用した核

## セッションで伝えたい中心的な緊張

- Platform Team自身もAIでサービス開発を高速化する。
- AIをPlatform Serviceにも組み込みたくなる。
- どちらの場合も、速く作れることと価値が出ることは同じではない。
- AIによって、それらしい機能やサービス候補を簡単に増やせるため、価値仮説が弱いままではゴミ山を作りやすい。
- AI Slop対策は、AIの生成品質だけでなく、Value Stream上の価値と副作用を検証することとして扱いたい。

## 人間とAIの役割

- 「AIを使うな」という話にはしない。
- この領域では、AIを「スピードを上げる」「人間の代わりに何かを作る」ためだけに使わない。
- 人間が作ったReasoning Chain、話の論理強度、ついて行きやすさを複数のAIで確認する。
- AIを人間のアウトプットの検証役に置くことで、人間の意思決定品質を上げる。
- AIはPersonaをシミュレーションできるが、そのPersonaが実在し、正しいかどうかは依然として仮説であり、現場で検証する必要がある。
- AIに「何がまだ仮説か」を判定させる使い方がある。

## Outcome Deliveryへの対応

- Discovery:
  - Problem Hypothesis
  - Value Hypothesis
- Decision:
  - Solution Hypothesis
- Delivery:
  - Feature / Experiment
  - Measure & Learn

価値仮説はDiscoveryのOutcome側に置く。
Decisionでは、その価値を実現するSolution Hypothesisを比較する。
DeliveryではFeatureを作り、Outcomeを検証する。

## 価値仮説構築の最初の型

参加者が思いついた「これをやったらいいかも」を、次の3点でReasoning Chainにする。

1. これをやったらいいかもと思うもの
2. それをやると、現状のどんな困りごとが改善するのか
3. その改善は、どんなビジネス価値やOutcomeにつながるのか

このとき、AIかどうかをいったん脇に置き、その案がMBPM上のどの付箋または付箋群を扱うのか指定できるかを確認する。
対象を指定できなければ、まだ価値仮説ではなく、便利そうな機能案に留まっている可能性がある。

## 仮説検証の実務例

過去のワークショップでは、Reasoning Chainの検討とAIによる論理強度の確認を用い、当初3回を想定していた内容を2回に圧縮した実績がある。
ただし、どの作業がどれだけ短縮に寄与したか、他の条件でも再現するかは別途確認が必要である。

紹介する手法について「AIを使うなら検証せよ」と主張する以上、どこまで実務で試され、どこからが未検証かを明示する。

# 本編で使える題材

## Platform Advisor

仮のお題:

> EA RepoをチャットBotのように操作できるPlatform Advisorを作ってはどうか。

想定する利用場面:

- Platform Serviceの選定
- 標準パスの確認
- 過去の判断や根拠の探索
- Architecture Review前の準備
- 例外時の相談先の確認

この題材が適している理由:

- 技術的には作れそうに見える。
- デモ映えしやすい。
- 「作れる」と「社内サービスとして価値がある」の差を示せる。
- 誤推奨、古い情報、過信、確認負荷、保守負債などのSlopリスクを扱える。
- 仮説構築から効果測定まで、一つの題材で追跡できる。

## Platform Advisorで扱う仮説候補

- Problem Hypothesis:
  - 利用者は、設計初期やPlatform選定時の情報探索と解釈に時間を使っている。
- Persona Hypothesis:
  - 主な利用者は、開発チーム、Tech Lead、Architectなどである。
- Target Friction Hypothesis:
  - 摩擦は、設計初期、Platform選定、Architecture Review前の付箋群に存在する。
- Value Hypothesis:
  - 探索と判断準備の負荷を下げると、判断待ちや差し戻しを減らせる。
- Solution Hypothesis:
  - EA Repoを参照するPlatform Advisorが、その摩擦を減らす選択肢になる。
- Slop Risk Hypothesis:
  - 誤推奨、古い根拠、利用者の過信、確認負荷、例外対応、保守負債が増える可能性がある。

## 社内サービスとして確認すること

- 誰のためのサービスか。
- どの判断を支援するのか。
- 何を提供するのか。
- 何を提供しないのか。
- 根拠と責任境界をどう示すか。
- 例外をどこで人に渡すか。
- 情報更新の責任を誰が持つか。
- 成功と廃止を何で判断するか。

# 説明を支えるモデル候補

## AI Slopの定義候補

AI Slopを、AIが誤った文章やコードを生成することだけに限定しない。

候補となる説明:

> 価値仮説が曖昧なまま、もっともらしい成果物や便利そうな機能が増え、Value Stream上の待ち時間、手戻り、確認負荷、例外対応が減っていない状態。

別の説明候補:

> DiscoveryとDecisionを十分に扱わず、DeliveryだけをAIで高速化した結果。

## 二種類のサービス品質

Platform Serviceを次の二面から見る案。

- 基盤サービス品質:
  - 安定性
  - セキュリティ
  - 性能
  - 運用性
- 社内サービス品質:
  - 対象利用者
  - 解決する問題
  - 期待するOutcome
  - 提供範囲と責任境界
  - 支援と情報更新
  - 成功指標
  - 改善および廃止判断

基盤サービス品質を満たしていても、社内サービス品質を満たさなければ、利用されない、価値を説明できない、維持対象だけが増える可能性がある。

## Demand PipelineとHorizon 1-2-3

AIによってIdeaと試作品が高速に増えるため、IdeaをそのままProduction Platform Serviceに流さない。

候補となる流れ:

```text
Idea
  -> Problem / Value Hypothesis
  -> Experiment
  -> Growth Decision
  -> Production Service
```

Horizonの対応候補:

- Horizon 3:
  - 探索と仮説検証
  - 捨てられる範囲で試す
- Horizon 2:
  - 利用、効果、運用負荷を観測して育成判断する
- Horizon 1:
  - 依存を受け入れ、標準サービスとして運営する

重要な論点:

- 「作ってから捨てる」ではなく、「捨てられる場所で作ってから判断する」。
- Production Portalに載せ、利用者の設計や見積の前提になると廃止は難しくなる。
- AI Slopは、Horizon 3のIdeaを検証なしにHorizon 1として扱うことで増えやすい。
- 各昇格ゲートでReasoning Chain、Value Hypothesis、Slop Risk、観測結果、サービス品質を確認する。

# 効果測定のネタ

## 最初に確認するもの

- 実際に使われたか。
- 継続利用されたか。
- 想定したPersonaが使ったか。
- 対象とした付箋または付箋群に変化があったか。

## Value Stream上で確認するもの

- 情報探索時間
- Platform選定のLead Time
- Architecture Reviewの差し戻し
- 標準パス利用
- 問い合わせ件数
- AI回答の確認工数
- 例外対応
- 誤選定や手戻り
- Platform TeamまたはEA Teamの運用負荷

## ボトルネック移動の読み方

ボトルネックが移動したこと自体を失敗としない。

- 望ましい移動:
  - 単純な探索や標準判断が減り、人間が例外判断や高度な相談に集中する。
- 望ましくない移動:
  - AI回答の確認、誤推奨の修正、差し戻し、古い情報の後始末が増える。

「どこへ移動したか」だけでなく、「移動先が意図した価値ある活動か」を確認する。

## Lead Time計測の注意候補

- 営業時間または営業日ベースで扱う。
- 休日や営業時間外をどう扱うかを明示する。
- 平均値だけでなく中央値、分位点、分布を見る。
- 作業時間と待ち時間を分ける。
- AI導入箇所だけでなく、後工程の手戻りや確認負荷まで見る。

これらはスライドで断定する前に、用語定義と出典を確認する。

# AI活用の具体例候補

## Reasoning Chain強度チェック

AIに解決策を出させるのではなく、次を確認させる。

- 1から2はつながっているか。
- 2から3はOutcomeにつながっているか。
- ProblemがSolutionの言い換えになっていないか。
- 主語、問題領域、目的、成果が途中ですり替わっていないか。
- ビジネス価値が中間能力で止まっていないか。
- 暗黙の前提や反例が残っていないか。

会話中には、`OK / あと一歩！ / 要ブラッシュアップ`で判定する長文プロンプト原案がある。
これは公開用Takeaway候補だが、現在のワークショップ固有の運用と例を含むため、別資産として整備する場合は再レビューする。

## 仮説の仕分け

Platform Service案に含まれる記述を、AIに次のように分類させる。

- 確認済みの事実
- 未検証の仮説
- 暗黙の前提
- 検証が必要なリスク
- 実装判断前に確認すべきこと

AIは仮説を事実に変えない。
AIの役割は、未検証部分を見えやすくし、検証順序を考える材料を増やすことである。

## Personaシミュレーション

AIにできること:

- 仮のPersonaならどこで迷いそうかを列挙する。
- 説明不足や利用時の失敗候補を探す。
- 異なる関心を持つ利用者の反応候補を比較する。

AIにできないこと:

- Personaの実在を証明する。
- Problemの深刻さを確認する。
- 実際の利用行動を保証する。

# 参加型Deliveryの候補

## 冒頭

候補フレーズ:

> ようこそ、地味なセッションへ。

価値を下げる自虐にはせず、派手な実装紹介ではなく「なぜ作るか」「何を価値とするか」を扱う期待値調整として使う。

候補となる挙手:

- AIを日常的に使っている人。
- AI Slopに遭遇した、または被害を受けたと感じた人。

## 中盤

後半の比重を参加者に選んでもらう案:

- A: 価値仮説の構築
- B: 効果測定と検証

固定した主張と結論は変えず、補足例や説明時間の配分だけを変える。

## 判断問題

候補シナリオ:

> Platform Advisor導入後、一次問い合わせは減ったが、レビュー差し戻しが増えた。成功か、失敗か。

想定する学び:

- 局所指標だけでは判断できない。
- Value Stream全体と、移動したボトルネックの質を見る必要がある。

# 冒頭と締めの素材

## プレゼンテーション作成におけるAI利用

冒頭の自己開示候補:

- スライド本文や主張の生成にはAIをほとんど使わない。
- 聴衆のKnowledge Gapに何をどの順番で刺すかは、人間が設計する。
- 論理強度、話の流れのついて行きやすさ、飛躍の有無は複数のAIで確認する。
- この使い分け自体が、セッションで紹介するAI活用の実例である。

「AIは無難にまとめる」と断定するのではなく、自分の制作上の観察と使い分けとして話す。

## 締めの主張候補

- AIで作れるものが増えたからこそ、価値あるものを見極める速度を上げる。
- AI時代に必要なのは、作る能力だけでなく、選ぶ能力、捨てる能力、検証する能力である。
- AIに作らせる前に、AIに疑わせる。
- AIは仮説を強くできるが、仮説を検証済みにはしない。
- 正しい答えを一発で出す能力ではなく、見落としを見落としのまま放置しない能力が必要である。

# お土産候補

## このセッション自体の思考ログ

このリポジトリを、完成資料だけでは見えない次の情報をたどれるLive Documentとして提供する案。

- 初期Idea
- Problem / Value / Solution Hypothesis
- 採択前後に変わった前提
- Delivery候補と選択理由
- 見落とし
- AIに確認させた箇所
- 未検証のまま残ったこと
- 当日および事後の学び

紹介表現の候補:

> 私は息をするようにValue Streamと仮説検証を組み合わせるので、この登壇準備でもログを残しました。

または:

> 私のセカンドブレインに近い思考ログを、公開可能な形で共有します。

完全な生ログを無加工で公開するのではなく、機密性、読みやすさ、出典境界を保った公開用ログとする。

## Unknown Unknownと二重の検証

- OVS側:
  - Platform Serviceが利用者のValue Streamを改善したか。
- DVS側:
  - Platform Team自身の仮説構築、判断、Delivery、検証プロセスが有効だったか。

どれだけ事前に仮説とSlopリスクを洗い出しても、Unknown Unknownは残る。
したがって、Serviceの効果だけでなく、自分たちの仮説検証で何を見落としたかを次の判断へ戻す。

# 25分枠に向けた選別候補

## 本筋候補

1. AIはPlatform Serviceを速く作れるが、価値の弱いものも速く増やせる。
2. DiscoveryでProblem / Value Hypothesisを作る。
3. DecisionでSolution HypothesisとしてPlatform Advisorを扱う。
4. AIでReasoning Chainと未検証前提を確認する。
5. DeliveryでFeatureを試し、Value Stream全体を測る。
6. 価値がなければ捨て、価値があれば育てる。ただしProduction化前に判断する。

## 時間があれば入れる候補

- 基盤サービス品質と社内サービス品質
- Horizon 1-2-3とDemand Pipeline
- Personaシミュレーション
- ボトルネック移動の良し悪し
- Lead Timeの測定注意
- DVS / OVS
- Miro上の情報設計と、継続更新を支える作業環境

## 本編から外し、お土産に回せる候補

- Reasoning Chainチェック用長文プロンプト全文
- このセッションの思考ログ詳細
- 参考文献と関連Frameworkの解説
- Journey MapおよびMBPMの全体図
- Horizonゲート条件の詳細

# 外部確認が必要なもの

以下は会話中に言及されたが、このRaw Noteでは出典確認していない。
スライドに使用する場合は、公式資料または一次資料をExternal Inputとして保存し、主張の範囲を確認する。

- 10-20-70の法則
- DORAの調査結果
- Mobius Outcome Deliveryの定義と図
- DVS / OVSの定義
- Horizon 1-2-3
- Epic Hypothesis Statement
- Metric Based Process Mapping
- Lead Time計測の実務上の定義
- PEK2026プロポーザル分析の応募数とカテゴリ別件数
- 過去のPlatform Engineering失敗パターン
- 組織内EditorialまたはOffering設計に関する見解

# 未決事項

- 25分枠で、Platform Advisorの一例をどこまで深く追うか。
- Discovery / Decision / Deliveryの全体像と、実演の時間配分。
- Horizon 1-2-3を本編に入れるか、Takeawayへ回すか。
- VSMとMBPMの用語をどの程度説明するか。
- 参加型の投票を実施する場合、固定部分と可変部分をどう分けるか。
- お土産の公開範囲と、Raw Noteをどこまで読みやすく整えるか。
- 当日および事後に何を観測し、どのHypothesis Episodeへつなげるか。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->

### CR-20260730-094152

- corrected_at: 2026-07-30T09:41:52+09:00
- corrected_by: human:kijima
- target: 「Demand PipelineとHorizon 1-2-3」の「各昇格ゲートでReasoning Chain、Value Hypothesis、Slop Risk、観測結果、サービス品質を確認する。」
- correction: この記述はゲートで確認し得る観点の候補を列挙したものであり、Horizon 3から2、Horizon 2から1など、どの昇格ゲートでどの観点を確認するかの具体的なマッピングはまだ行っていない。
- reason: ゲートごとの通過条件が設計済みであるかのような誤解を避け、現時点の検討状態を明示するため。

### CR-20260730-094319

- corrected_at: 2026-07-30T09:43:19+09:00
- corrected_by: human:kijima
- target: 「25分枠に向けた選別候補」の「本筋候補」および同セクション全体
- correction: 「本筋候補」は現時点の暫定的な叩き台である。項目の採否、粒度、順序だけでなく、「時間があれば入れる候補」「本編から外し、お土産に回せる候補」との区分を含む全体構成も、今後入れ替えることを想定している。
- reason: 25分枠のストーリーと内容選定が確定済みであるかのような誤解を避け、現在は候補を比較する段階であることを明示するため。
