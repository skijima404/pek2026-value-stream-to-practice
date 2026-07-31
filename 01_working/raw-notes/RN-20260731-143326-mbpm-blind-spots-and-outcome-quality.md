---
id: RN-20260731-143326-mbpm-blind-spots-and-outcome-quality
type: raw_note
title: "MBPMで観測できないAI SlopとOutcome Quality"
content_language: ja
created_at: 2026-07-31T14:33:26+09:00
content_origin: mixed
created_by: human:kijima
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-31T14:40:35+09:00
sanitization_checked_by: agent:codex
tags: [ai-slop, mbpm, outcome-quality, quality-assurance, service-contract, trust]
---

# メモ

## このメモの位置づけ

ChatGPTの会話「AI SlopとPE」から、2026年7月31日に行った
「MBPMで観測できないSlopは何か」という発散と、その後の
Outcome Oriented、Quality Assurance、Platform Service Contract、
Mobiusへの接続を抽出したRaw Note。

- source conversation:
  `chatgpt-conversation://6a41fa3c-4fac-83ee-8107-41096d4d5e3f`
- 人間とAssistAの発言を分離せず、思考が動いた経緯として再構成した
- 一般的なAI Slopの定義、検証済みのFramework、採用済みの登壇構成ではない

## 出発点: MBPMで観測できないSlopは何か

一本道が見えた後、その論理を壊す問いとして次を置いた。

> MBPMで観測できないSlopは何か。

きっかけは、一つのAI Slop的な登壇が、個別Sessionだけでなく、
Event全体、運営、他の登壇者、配信支援者の努力や信頼まで毀損し得るという
Event運営者の問題意識だった。

この例で起きているのは、単純なLead Time悪化、差し戻し、確認工数ではない。
個別成果物を超えて、場、Brand、Community、支援者、次回の参加意欲へ
影響が広がっている。

ここから、AI Slopによる影響を二つに分けた。

### 直接的に発生するSlopの現象

- 内容が薄い
- 根拠が弱い
- 利用者のContextに合っていない
- それらしいが判断に使えない
- 誤った自己解決を促す
- 利用されない
- 後工程で差し戻し、確認、再作業、例外対応を生む

### 二次被害

- PlatformまたはEvent全体の信頼が下がる
- 標準パス、次回利用、次回参加への意欲が下がる
- 他の提供者、登壇者、運営、支援者の努力まで毀損される
- 支援者が疲弊する
- 「このPlatformまたは場は信用できない」という印象が残る

この区別では、直接現象の一部はMBPM上の待ち、手戻り、確認負荷、
Lead Time、`% Complete & Accurate`などに現れ得る。

一方、二次被害は、特定Processの摩擦よりも、信頼資本、体験、
将来の選択に現れるため、MBPMだけでは見えにくい。

## 最終成果物の品質はMBPM上で見えにくい

MBPMは、Actor別のProcessとハンドオーバーを詳細化し、次のような
摩擦を観測することに向いている。

- 待ち時間
- Process TimeとLead Time
- 差し戻し
- 確認負荷
- 例外対応
- 手戻り
- ハンドオーバー後の修正、追加、確認

しかし、最終成果物がProcessを通過した後、受け手に初めて現れる次の品質は、
Process Map上では直接見えにくい。

- 読んだが薄い
- 聞いたが判断に使えない
- 公式Serviceらしいが信用できない
- 利用者の文脈に合っていない
- AIで作られた無難な内容に見え、誠実さを感じない
- 次も使いたい、参加したい、他者へ薦めたいと思えない

例として、資料作成、Review、登壇までのProcessが円滑でも、
参加者が「上滑りしている」「価値がない」と受け取る可能性がある。

同様に、Platform Serviceの企画、設計、実装、Releaseが円滑でも、
利用者が「判断に使えない」「また微妙なAI機能が増えた」と受け取る
可能性がある。

したがって、会話では次の境界を置いた。

```text
MBPM:
Process上の摩擦とハンドオーバーの品質を見る

Quality Assurance:
最終成果物が期待された品質を満たしたかを見る

Service QA:
利用者がServiceを信頼し、次の判断または行動へ使えるかを見る
```

## Quality Assuranceは期待された体験と価値の充足を見る

ここでいうQuality Assuranceは、単にBugを見つけるTestではない。

> 期待された体験、価値、信頼を、最終成果物が満たしているか。

会話では、次のQualityを分けた。

### Process Quality

- 作る過程で手戻りまたは確認負荷が増えていないか
- Actor間のハンドオーバーで情報が落ちていないか

### Output Quality

- 回答、Template、Document、Featureが正確か
- 根拠、前提、適用範囲が明らかか

### Experience Quality

- 利用者が期待した体験を得られたか
- 利用者のContext、権限、判断責任に合っているか
- 次の判断または行動が分かったか

### Trust Quality

- 利用者が公式Serviceとして信頼できるか
- 次も使いたい、他者へ薦めたいと思えるか

### Contract Quality

- Serviceが利用者へ暗黙または明示に約束した価値を満たしたか
- 利用者が安全に次の判断または行動へ進めたか

観測候補として、アンケート、自由記述、再利用率、継続利用、推奨率、
再訪率、支援者または利用者の反応が挙げられた。

ただし、これらのMetricだけで信頼または価値を完全に測定できるとは
結論していない。

## Platform Service Contractという見方

Platform Serviceは機能を提供するだけでなく、利用者へ次のような
暗黙または明示の約束をしているという話になった。

> このServiceを使えば、利用者は特定の判断、作業、申請、設計を、
> 一定の品質で進められる。

AI Slopは、Outputが間違っている場合だけでなく、このContractを
満たしていない場合にも現れる。

例えばPlatform Advisorに対し、利用者は次を期待する可能性がある。

- 自分の状況に関係する標準またはADRを見つけられる
- その意味を理解できる
- 標準パスか例外かを判断する材料が得られる
- 次に何をすればよいか分かる
- 大きく誤った方向へ誘導されない

提供側が「参考情報を出すだけ」と考え、利用者が「設計判断に使える」と
考えているなら、機能が動いていてもContract mismatchが起きる。

Contract候補として挙げられたもの:

- 対象利用者
- 提供範囲
- 非提供範囲
- 利用条件
- 品質保証範囲
- 利用者責任
- Platform責任
- 非対応Case
- 例外時のEscalation
- 更新責任

## レゴブロックの比喩

Platform Engineeringを、開発者が従来すべて担っていた10×10の壁の一部を、
Platformが5×5として引き受ける構造に例えた。

「5×5を提供する」だけでは、利用者には次が分からない。

- 右上、右下、左上、左下のどこか
- 本当に5×5か
- 境界線はどこか
- 残りの責任を誰が持つか
- 他の部品と接続できるか
- 期待する強度を持つか

さらに、次のContract mismatchが挙げられた。

### レゴだと思ったらナノブロックだった

部品そのものは成立しているが、接続規格、粒度、用途が異なる。

### 構造ブロックの一つがミニフィグだった

単体として悪い部品ではないが、壁を作るというOutcomeに対して、
抽象度、粒度、責任境界が合わない。

この比喩が示すのは、「悪いものを作ったか」だけではない。

> 目的に対して、適切な抽象度、粒度、境界のものを提供できたか。

AIは便利そうな部品を短時間で大量に作れるため、OutcomeまたはContractに
適合しない部品までPlatform Serviceに混ぜる可能性がある。

## MBPM上でFlowが良くてもOutcomeは間違い得る

会話では、MBPMの限界を次のように表現した。

> MBPMはFlowの品質を見るが、価値の意味を保証しない。

極端には、要求受付から提供までが速く、問い合わせも差し戻しもなく、
Process上は円滑でも、利用者が欲しかった壁用ブロックではなく、
ミニフィグが届いている可能性がある。

```text
Process Quality
  - 速いか
  - 滞留していないか
  - 手戻りがないか
  - ハンドオーバーが成立しているか

Outcome Quality
  - 欲しかったものか
  - 期待した価値が出たか
  - 利用者の判断または行動が改善したか
  - Service Contractを満たしたか
```

ここから、MBPMだけでSlopを判定するのではなく、Outcome Orientedな仕組みが
必要だという話になった。

## Outcome Orientedへ戻った理由

Outcome Orientedな分解は、Solutionの機能一覧ではなく、
価値を成立させる能力または条件の抜け漏れを見る。

例:

```text
Outcome:
開発者が安全かつ早く設計判断できる

必要な価値要素:
  - 必要な情報を見つけられる
  - 情報の意味を理解できる
  - 自分のCaseへ適用できる
  - 判断してよい範囲が分かる
  - 判断結果を後から説明できる
```

Solutionから「EA RepositoryをChat化する」と置くと、検索と回答ができた時点で
完成と見なす可能性がある。

Outcomeから分解すると、検索だけでは、解釈、適用判断、責任境界、
Decision Traceを満たせないことが見える。

したがって、AI ChatbotはOutcomeを構成する一部の手段であり、
Outcomeそのものではない。

## 価値仮説がなければ検証全体が成立しない

議論は最終的に、MBPMの観測限界より前に、Value Hypothesisの有無へ戻った。

```text
Value Hypothesisがない
  ↓
期待するOutcomeがない
  ↓
何を測れば成功か決まらない
  ↓
利用率または速度だけを成果として扱う
  ↓
Slopか価値ある変化かを見分けられない
```

MBPMは、Flowが速くなったか、下流負荷が増えたかを観測できる。
しかし、Value Streamが正しい価値へ向かっているかは、Value Hypothesisなしには
判定できない。

この時点で、次のGateが置かれた。

```text
Gate 0:
Value Hypothesisは存在するか
  ├─ No
  │    → Discoveryへ戻る
  └─ Yes
       → Outcomeを定義する
       → 検証方法を設計する
```

三つの状態:

- Value Hypothesisがない
  - 検証不能であり、何を作るか以前へ戻る
- Value Hypothesisはあるが支持されない
  - Lean Startupの考え方で案を捨てる
- Value Hypothesisが支持され、受け手にはSlopとして経験される
  - 価値ある変化を残し、ハンドオーバーへ橋を架ける

「上滑りする登壇資料」も、単に出来が悪いのではなく、
参加者に起こしたい変化が定義されていなければ、刺さったかどうかを
検証できない状態と整理できる。

## Mobiusへの暫定的な接続

会話では、混ざりやすいものを次のように分ける補助線として、
MobiusのDiscovery、Decision、Deliveryを使った。

```text
Discovery:
何の価値を実現したいのか
  - Problem Hypothesis
  - Value Hypothesis
  - Outcome Breakdown

Decision:
その価値をどう実現するのか
  - Solution Hypothesis
  - Option比較
  - Trade-off
  - Experiment判断

Delivery:
実際に価値になったのか
  - Feature
  - Experiment
  - 利用状況
  - Metrics
  - Learn
```

この会話中の対応は、登壇準備を振り返るための仮説階層の補助線であり、
MobiusのBoard列をTask実行管理として使う意図ではない。

典型的なAI Slopの流れとして、次が挙げられた。

```text
Discoveryが不足する
  ↓
Value Hypothesisがない
  ↓
DecisionでSolutionを先に固定する
  ↓
DeliveryでFeatureを高速生成する
  ↓
作ったが、価値が分からない
```

AI以前はDelivery Costが途中の抑制として働く場合があった。
AI時代には、作る能力が上がったため、DiscoveryまたはDecisionが不足したまま
Deliveryまで到達しやすいという見立てが置かれた。

## AI活用Outcomeとの接続

Outcomeを先に定義することで、AIへ期待する能力を選べる。

- 速く作る
- 広く探す
- 分かるように解釈する
- 選べるように整理する
- Reasoning Chainが本当に成立しているか疑う

重要な順序として、次が置かれた。

> AI能力選択の前に、Outcome選択がある。

AIはOutcomeそのものを決定するよりも、Outcome要素の洗い出し、
抜け漏れ確認、反例提示、Contract違反Caseの想定に使えるという
観察も記録された。

## 現時点の整理

```text
Value Hypothesis
  ↓
Outcome Definition / Outcome Breakdown
  ↓
Solution Hypothesis
  ↓
Feature / Experiment
  ↓
MBPMでProcessとハンドオーバーを観測
  +
QA / Service Quality / Contract Qualityで最終成果物を観測
  +
Journey / Trustで二次被害を観測
  ↓
学習をValue HypothesisとSolution Hypothesisへ戻す
```

会話から得た暫定的な結論:

> MBPMはAI Slop検知の一部であり、入口はValue Hypothesisである。

> MBPMはSlopのProcess負荷を見つけやすいが、最終成果物の体験品質、
> Contract充足、信頼毀損は別の観測を必要とする。

> AI時代に必要なのは、AIで何を作れるかを先に考えることではない。
> どのOutcomeを実現したいかを定義し、そのValue Hypothesisを
> 検証できる状態を作ることである。

## 留保

- このメモは対話から抽出した思考ログであり、一般的な能力論または
  検証済みの方法論ではない
- MBPMで「観測できない」と断定するより、MBPM単体では直接観測しにくい、
  または別の測定対象として明示する方が正確
- Trust、Experience、Contract Qualityの具体的な測定方法と閾値は未定義
- 利用率、再利用率、推奨率が高くても、Business Outcomeが出たとは限らない
- Mobiusとの対応は会話中の暫定整理であり、採用済みArtifactではない

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
