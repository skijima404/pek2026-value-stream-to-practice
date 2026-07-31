---
id: RN-20260731-115056-managed-ai-slop-transformation
type: raw_note
title: "AI Slopを管理可能なTransformationの摩擦として捉える"
content_language: ja
created_at: 2026-07-31T11:50:56+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: copy_paste
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-31T12:04:07+09:00
sanitization_checked_by: agent:codex
tags: [ai-slop, enablement, handover, mbpm, non-functional-requirements, platform-service, transformation]
---

# AI Slopを管理可能なTransformationの摩擦として捉える

## このメモの位置づけ

2026年7月31日に、人間とAssistAが行った「AI Slopは悪か」という議論を
Codexへコピーし、その内容を後から参照できるように構造化したRaw Note。

次の既存メモから議論が続いている。

- `RN-20260731-105559-handover-decision-context-ai-enablement`
- `RN-20260731-113600-mbpm-session-emphasis`

このメモは、採用済みの登壇ストーリーでも、検証済みの定義でもない。
会話の中で形成された考え、判断候補、表現候補、会話中に訂正された内容を
保存する。

## 出発点: ズレは悪か

受け手と渡し手の間には、Role、知識、責任、技術成熟度、制約の違いがある。
極端には、受け手側がLegacyな仕事の仕方を持ち、渡し手側が先進的な
AutomationまたはPlatformを提示する場合でもズレは起きる。

議論では、ズレそのものをハンドオーバーの失敗とは捉えなかった。

> ズレはハンドオーバーの失敗ではなく、
> ハンドオーバーが必要になる前提条件である。

受け手に完全に合わせると、古い承認構造、手動作業、責任分担を固定し、
PlatformがLegacy Processの自動化装置になる可能性がある。

一方、渡し手が自分たちの方法を「先進的」として一方的に渡すと、
Skills、規制、監査、責任分界、移行期間、失敗時の戻し先を無視した
押しつけになる可能性がある。

問題はズレの存在ではなく、次にある。

> そのズレを誰が、どのように、どのコストで越えるのかが
> 設計されているか。

## 良いズレと悪いズレ

会話では、ズレの状態を次のように整理した。

| 状態 | 会話中の読み方 |
| --- | --- |
| 意図したズレ、移行支援あり | Transformation、Enablement |
| 意図したズレ、移行支援なし | 押しつけ、下流へのコスト転嫁 |
| 意図しないズレ、早期検知 | 学習、仮説の修正機会 |
| 意図しないズレ、未検知 | 手戻り、停滞、Slop化 |
| ズレがほぼない | Flowしやすいが、現状固定の可能性もある |

ズレがないことは、正しいOutcomeへ進んでいることを意味しない。

```text
ズレがない
  ≠
正しい

よく流れる
  ≠
価値がある
```

受け手側のLegacyな質問にも、規制、監査、過去の障害、Skills、責任条件、
組織固有のRiskが含まれている可能性がある。

ズレを見つけた時に、自動的にどちらかへ合わせるのではなく、次を確認する。

- 単なる認識違いか
- 受け手の制約か
- 意図したTransformationか
- 将来状態への移行Gapか
- Value Hypothesisへの反証か
- まだ不明か

## Transformationの本体は橋の設計

多くのTransformationは、現在とTarget Stateの間に意図的なズレを作る。
しかし、Target Architecture、標準Process、Golden Path、SaaS、
Operating Modelを作った後、受け手が現在地からどう移るかを
受け手の宿題にすることがある。

```text
提供側:
どこへ行くかを説明する

受け手:
ここからどう行くかを尋ねる
```

会話では、次の表現が作られた。

> Target StateはTransformationの目的地にすぎない。
> Transformationの本体は、現在地から目的地までの
> ハンドオーバーを設計することである。

> 将来状態の納品と、移行コストの外部化を、
> Transformationと呼ばない。

> 意図したズレはVision。移行支援がTransformation。

> Transformationとは、ズレを作ることではない。
> そのズレを越える責任を引き受けることである。

必要なものとして、次が挙げられた。

- Current Stateと制約を理解する
- 何を残し、何を変えるか合意する
- なぜ変えるのかを共有する
- 中間状態を設計する
- 新旧の共存条件を決める
- Skillsと責任の移行を支援する
- 小さく試し、Target State自体も修正する
- 移行できない理由を「抵抗」として片付けない

「抵抗」は、設計されていないハンドオーバーが受け手側に現れた姿かも
しれないという見方も示された。

## Agile Transformationで起きたこと

会話では、Agile Transformationで起きた二つの失敗を例にした。

### 組織へ合わせすぎる

既存の承認、予算、組織構造とAgileがずれた時に、
「この組織には合わない」として従来の方法へ戻る。

この場合、年次予算、部門別KPI、遅い承認、Feedbackの欠如、
チームの意思決定権不足など、ズレが示したTransformationの機会を
失う可能性がある。

### Agileへの適応を一方的に強制する

「これが正しいAgileである」として、規制、責任、事業特性、
組織固有の制約を無視する。

一方はズレを理由にTransformationを止め、もう一方はズレを
受け手の責任にする。どちらもズレから学習していない。

## ズレは判定結果ではなく観測結果

```text
ズレが見つかった
  ≠
導入失敗

ズレが見つかった
  ≠
受け手が間違っている

ズレが見つかった
  ≠
提供側のSolutionが間違っている
```

ズレから直接言えるのは、Value Hypothesis、Solution、組織能力、
制約の間に、まだ説明できていない関係があるということだけである。

そのズレが次のどれなのかは、追加で調べる必要がある。

- 変えるべきLegacyな制約
- 守るべき規制または責任
- 不足しているEnablement
- 誤ったSolution Hypothesis
- 共有されていないValue Hypothesis
- 必要な中間状態
- 用語または認知の違い

> Fitを事前条件にするのではなく、Fitを学習によって作っていく。

## Resilientなハンドオーバー

良いハンドオーバーは、最初から誤解や質問が起きない設計ではない。

> ズレても、早く気づき、壊れる前に戻し、
> 意味と責任を再調整できるハンドオーバー。

必要な仕組み:

- 受け手が「次へ進めない」と表明できる
- 質問を抵抗や能力不足として扱わない
- どのLayerがずれているか確認できる
- 渡し手へContext付きで戻せる
- 誰が橋を作るか決められる
- 修正後の結果を再観測できる

オーバーラップ区間も、ズレを事前に消す場所ではなく、
実際に走りながら速度差を検知し、受け渡し位置を調整する区間として
捉え直された。

## ズレを学習可能にするLoop

```text
Value Hypothesisを置く
  ↓
小さく新しい方法を渡す
  ↓
実際の利用とハンドオーバーでズレが出る
  ↓
ズレを早く検知する
  ↓
ズレの意味を共同で解釈する
  ↓
何を変えるか判断する

- 受け手の能力または仕事
- 提供側のSolution
- ハンドオーバー条件
- 移行支援
- Target State
- Value Hypothesis

  ↓
小さく修正して再度試す
```

このLoopは、次の短い言葉へまとめられた。

> Transformationでは、ズレをなくすのではなく、
> ズレを学習可能にする。

## AI Slopは悪か

探索段階では、現在の理解とずれたOutputが価値を持つ場合がある。

- 思いつかなかった案
- 常識から外れた仮説
- 異なるLayerからの問い
- 既存方針への反例
- 捨てる前提のPrototype

この段階では、ズレが認知を広げる。

問題になるのは、探索物を、検証済み、利用可能、Production品質、
他者が依存してよいという約束とともに渡す場合である。

> ズレは悪ではない。合意も橋もないまま、
> そのズレを受け手の宿題にすることが問題である。

> どの状態のOutputを、どの約束を伴って、
> 誰へ渡したかを確認する。

## 受け手のAI Slop感と組織価値を分ける

受け手がAI Slopだと経験していることと、その変化が組織にとって
捨てるべきものであることは別である。

受け手に確認、修正、意味の再構築が増えたなら、その人のValue Streamには
実際にSlopが流れ込んでいる。

作成者自身も、AIで生成された提案書を受け取ると、自分で作成する場合より
長い時間をかけてReviewすることがあり、そのOutputをAI Slopだと感じている。

一方、最終的に、観点が広がる、見落としが減る、品質が上がる、
より多くの機会を扱えるなどの組織価値があるなら、
AI生成自体を捨てるべきとは限らない。

| 組織的な価値 | 受け手の負荷 | 判断候補 |
| --- | --- | --- |
| 低い | 高い | 止める、捨てる |
| 高い | 高い | 変化は維持し、壊れたハンドオーバーを修正する |
| 高い | 低い | 維持、拡大候補 |
| 低い | 低い | 害は小さいが、継続理由も弱い |

扱いが難しいのは、価値はあるが、受け手にはSlopとして現れている状態である。

「Slopだから止める」と、Transformationの機会を失う。
「組織に価値があるから我慢する」と、Transformation Costを
受け手へ外部化する。

> 価値ある変化は維持する。
> ただし、Slopとして現れている下流負荷を放置しない。

## AI Slopを判定ではなくシグナルとして扱う

> 「AI Slopだ」という言葉は、生成物の最終評価ではなく、
> 下流に未処理の仕事が来ているというAlarm。

受け手側で、Review時間の増加、全文の再確認、根拠の再探索、
AI生成箇所の不明、責任の不明、もっともらしい誤りの確認が起きているなら、
そのSlop感を観測結果として扱う。

> AI Slopは、捨てるべきものの名前ではない。
> 受け手側で、まだ価値へ変換されていないOutputの状態である。

## AI Slopは防げないが、事前のリスク管理は必要

ズレは学習機会になりうるが、無制限に発生させてよいわけではない。
受け手のCapacityを超え、業務を止めるほどのボトルネックが発生する場合は、
組織価値がある可能性を残していても、Outputの流入を止める必要がある。

次の二つを分ける。

```text
この変化に価値があるか
```

```text
この変化を、今の速度と規模で流して安全か
```

AI Slopになるかを事前に断定することは難しいが、Risk Hypothesisは置ける。

- どのLaneのOutputが増えるか
- 次に受け取るのは誰か
- 受け手の処理Capacityはどの程度か
- どんな修正、追加、確認が発生しうるか
- 責任または判断Contextが欠ける可能性はあるか
- `% Complete & Accurate`がどこまで下がりうるか
- 最悪の場合、どの業務が止まるか
- ズレが大きかった時に誰が支援するか
- どのMetricを超えたら止めるか
- 元の方法へ戻せるか

> AI Slopかどうかを予言するのではなく、
> Slopとして現れた時に被害を限定して回復できるかを設計する。

## Value Hypothesisを捨てずに流入を止める

```text
価値が低い
  → 捨てる

価値は高いが、現在の運用では処理不能
  → Outputの流入を止める
  → Value Hypothesisは保持する
  → ハンドオーバーを修正する
  → 小さく再開する
```

> 止めるのはOutputの流入であって、
> Value Hypothesisまで捨てるとは限らない。

## Safe-to-Failな展開

最初から全件または広範囲へ展開せず、次のように進める。

```text
限定した対象
  ↓
少量のOutput
  ↓
明確な受け手
  ↓
支援担当者あり
  ↓
MBPMで観測
  ↓
修正後に拡大
```

AIが無制限に生成できても、次のLaneへ流す量は、
人間のReview Capacityに合わせる。

> AIの生成能力ではなく、次のLaneの受入能力が
> 全体の流量を決める。

## Early Warning、停止、支援、回復

事前に設計する候補:

### Early Warning

- ReviewerのQueue長
- Review開始までの待ち時間
- 一件あたりの修正時間
- 根拠確認数
- 差し戻し回数
- `% Complete & Accurate`
- 通常業務への影響
- 重大な誤りの発生

### 停止条件

- Review Lead Timeが許容範囲を超える
- `% Complete & Accurate`が仮置きした水準を下回る
- 重大な誤りが発生する
- 通常業務のService Levelを維持できない
- 未ReviewのWIPが許容範囲を超える

具体的な数値は、この会話では測定していない。
Baseline取得後に仮置きし、更新する必要がある。

### 支援と回復

- 生成量を絞る
- 対象業務または利用者を限定する
- AI生成箇所を明示する
- 根拠、Source、前提を付ける
- ReviewerのCapacityを一時的に追加する
- 生成者とReviewerが同席する
- 問題の多いSectionを人間作成へ戻す
- Acceptance Criteriaを修正する
- AIへ求めるOutcomeを変更する
- 旧ProcessへRollbackする

## AI Slop対策は非機能要件設計

AI機能の機能要件だけなら、次で終わる。

- 提案書を生成できる
- Codeを生成できる
- 問い合わせへ回答できる
- Platform Serviceを推奨できる
- 設定例を生成できる

Platform Serviceとしては、次の非機能要件が必要になる。

- 受け手が処理可能な流量である
- 下流のLead Timeを悪化させない
- 根拠とSourceを追跡できる
- AI生成部分を識別できる
- 人間へ戻す条件が明確である
- 誤りを検知できる
- 停止条件が定義されている
- 段階的に縮退できる
- 旧ProcessへRollbackできる
- 問題発生時の支援担当が明確である
- 修正結果を次の生成へ反映できる
- 受け手が次の作業を開始できる

| 非機能特性 | AIとハンドオーバーで見る候補 |
| --- | --- |
| Performance | 生成時間ではなく、最終判断までのLead Time |
| Capacity | 下流のReview、承認、運用が処理できる量 |
| Reliability | 修正、追加、確認なしで利用できる割合 |
| Observability | Queue、差し戻し、確認往復、ズレを検知できる |
| Resilience | Slopが増えても業務全体を停止させない |
| Controllability | 生成量、対象、権限、展開範囲を制御できる |
| Recoverability | 停止、縮退、Rollback、再開ができる |
| Traceability | 根拠、前提、AI生成箇所、人間の判断を追跡できる |
| Safety | 誤った約束や危険な判断を承認前に流さない |
| Operability | 問題時の相談先、責任者、Support手順がある |
| Usability | 受け手が意味を理解し、次の行動へ進める |
| Maintainability | 発見したズレをServiceへ反映できる |

AI機能が正常に応答していても、ReviewerのQueue、Review時間、
確認往復、通常業務への影響が悪化しているなら、
トータルサービスとしては障害になっている可能性がある。

> AI Slopは、機能の失敗ではなく、
> 下流とのハンドオーバーに現れる非機能障害である。

> AI Slop対策は、AI機能の品質管理ではない。
> AIを含むトータルサービスの非機能要件設計である。

## MBPMとMobiusの混同、および訂正

会話の途中で、次の誤った説明が行われた。

> VSMは、ズレがどこで痛みになっているかを見る。
> MBPMは、どの仮説レイヤーでズレているかを考える。

この説明では、MBPMとMobius Outcome Delivery Lensを混同していた。
会話中に次のように訂正された。

- MBPM:
  Metrics Based Process Mapping。
  特定のValue Stream Segmentを、担当Actor別のProcess StepとMetricへ
  詳細化するPractice
- Mobius Outcome Delivery Lens:
  Value、Solution、FeatureのHypothesis Levelを振り返るLens

MBPMの外部参照:

- `EXT-20260731-113601-mbpm-open-practice-library`

このメモでは、以降のMBPMを、訂正後の意味で使用する。

## 今回MBPMを前面に出す理由

今回の話では、VSMをValue Stream全体を見る背景として残し、
実際に「どこを観測するか」を決める道具としてMBPMを前面に出す。

```text
VSM:
Value Stream全体と、詰まっているSegmentを見る

MBPM:
特定SegmentをActor別のProcessとMetricへ分解し、
怪しいハンドオーバーまでZoomする

レイヤーずれレビュー:
なぜそのハンドオーバーで、
相手の判断へ答えられていないのかを診断する
```

MBPMでは、Actor間の境界ごとに次を確認できる。

| 観測項目 | 確認すること |
| --- | --- |
| 渡し手 | 誰が作業を完了したか |
| 受け手 | 誰が次の作業を開始するか |
| Incoming Work | 何が渡されたか |
| Next Action | 受け手が何を判断、実行するはずか |
| Process Time | 各Stepの作業時間 |
| Lead Time | 渡されてから次のStepが完了するまでの時間 |
| Waiting Time | 受け手が開始できず待った時間 |
| Correction | 受け手が修正したもの |
| Addition | 受け手が追加したもの |
| Clarification | 確認の往復 |
| `% Complete & Accurate` | 追加、修正、確認なしで進めた割合 |
| Backflow | 前のLaneへ戻った理由 |

特に`% Complete & Accurate`は、下流の利用者が受け取った仕事を
訂正、追加、確認せずに実行できる割合であり、今回のハンドオーバーの
議論と直接つながる。

> ハンドオーバーの成否は、渡した側ではなく、
> 受け取った側が次へ進めたかで決まる。

## AI SlopをMBPMで観測する

AI導入後に、あるLaneのProcess Timeだけが短くなる可能性がある。

```text
上流:
Process Timeが短縮
Output到着量が増加

下流:
Waiting Timeが増加
Clarificationが増加
Correctionが増加
% Complete & Accurateが低下
```

この場合、上流の高速化が、下流へ確認、修正、待ち時間を移した可能性がある。

> AI Slopとは、上流のProcess Timeを短縮しながら、
> 下流の`% Complete & Accurate`を下げるOutputである。

これは完全な定義ではなく、「下流へ宿題を移しただけではないか」を
確認するSignal候補である。

MBPMは異常を観測し、レイヤーずれレビューは原因仮説を作る。

```text
% Complete & Accurateが低い
Clarificationが多い
次のStep開始まで長く待つ
  ↓
なぜ受け取れなかったか
  ↓
質問と回答のLayerがずれていないか
判断Contextが欠けていないか
責任またはAcceptance Criteriaが不明ではないか
```

## Current StateとFuture State

```text
Current State MBPM
  ↓
AIまたは新しいPlatform Serviceを小さく導入
  ↓
Future State候補のMBPM
  ↓
変化したハンドオーバーを比較
```

比較候補:

- Process Timeは短くなったか
- Lead Timeは短くなったか
- `% Complete & Accurate`は上がったか
- 新しい確認または修正が増えていないか
- 誰かのLaneへ仕事を移しただけではないか
- Transformationのズレから学習できたか

MBPMはズレを事前に消す道具ではない。

> Transformationによって生まれたズレが、
> どのActor間で、どのような下流作業になったかを
> 可視化する手掛かり。

## 登壇での役割分担候補

- VSM:
  局所的な高速化ではなく、Value Stream全体を見るという原則
- MBPM:
  Actor間のハンドオーバーを観測する方法
- `% Complete & Accurate`:
  受け手が宿題なしで次へ進めたかを見るMetric
- レイヤーずれレビュー:
  問題が見つかった後の原因仮説
- AI Outcome分類:
  その原因に対して、AIを何のために使うか選ぶ

持ち帰りAction候補:

> AIで速くなったStepの直後にあるハンドオーバーを、
> MBPMで一つだけ見に行く。

確認する問い:

> 受け手は、修正、追加、確認なしで次へ進めているか。

## EnablementとMarketingは最前線

EnablementまたはInternal Product Marketingは、完成したPlatformを
後から説明する補助部隊ではない。

> Platform Serviceと利用組織のズレを最初に観測し、
> そのズレを修正する最前線。

### Marketing

- 誰にどのValue Hypothesisがあるか
- 利用者が何を判断しようとしているか
- どの言葉またはLayerなら価値が伝わるか
- なぜ使われないか
- どの懸念が導入を止めているか
- Target Stateへ移る理由が共有されているか

### Enablement

- 最初の利用を一緒に試す
- Current StateとTarget Stateをつなぐ
- SkillsとContextを補う
- 関係部門との会話へ同席する
- Acceptance Criteriaを共同で作る
- 例外をPlatform Teamへ戻す
- 繰り返される問題をService改善へ変える

あるPlatform Engineeringの現場では、チームCapacityの相当部分が、
利用者との接点にある活動へ継続的に割り当てられていた。
この配分は、説明要員ではなく、Platform Serviceの非機能要件を
成立させるCapacityとして理解できるという話になった。

再識別を避けるため、企業、案件、具体的な配分は記録しない。

EnablementとMarketingの比喩:

> Platform Serviceの組織境界に置かれた
> ObservabilityとControl Plane。

ただし、Enablementが永続的な人力通訳工場になってはいけない。
個別支援で観測した内容を、次へ戻す必要がある。

- Contractの更新
- Platform機能の改善
- Documentationの改善
- 標準と例外の明確化
- Migration Pathの再設計
- 次回のハンドオーバー改善
- 再利用可能な学習

評価候補:

- ズレを検知するまでの時間
- 解消するまでの時間
- 同じ質問の再発
- `% Complete & Accurate`
- 利用者が次へ進めたか
- 個別支援がService改善へ変換されたか

## Release前の価値選別とRelease後の橋渡し

ここまでの議論を、Release前後の判断Flowとして整理する案が出た。

Release前には、Lean Startupの考え方でValue Hypothesisを安価に検証し、
価値の弱い案をProductionへ約束する前に捨てる。

ただし、Release前の検証だけでProductionにおける価値や、受け手が
AI Slopとして経験する可能性を完全に予測できるわけではない。
そこで、Release後は少なくとも次を分けて観測する。

- 利用率または利用継続
- 想定したBusiness Outcomeまたは利用者Outcome
- 受け手側の待ち、修正、追加、確認、Queue
- MBPMのProcess Time、Lead Time、`% Complete & Accurate`
- 通常業務または下流Capacityへの影響

利用率だけでは価値を証明できず、利用されていることと、
受け手がSlopとして経験していないことも同義ではない。

全体Flowの候補:

```text
Idea / Value Hypothesis
  ↓
Lean StartupでRelease前に安価に検証する
  ↓
価値仮説は支持されるか
  ├─ No
  │    → Productionへ約束せず、案を捨てる
  │
  └─ Yes
       → Risk Hypothesis、停止条件、支援策を置く
       → 限定的にReleaseする
            ↓
       利用率、Outcome、MBPMを観測する
            ↓
       価値は実際に出ているか
       ├─ No
       │    → 止める、捨てる、またはValue Hypothesisを見直す
       │
       └─ Yes
            ↓
       受け手はSlopとして経験しているか
       ├─ No
       │    → 維持し、段階的な拡大を検討する
       │
       └─ Yes
            → 価値ある変化は残す
            → Enablement、Context、ハンドオーバー、
              非機能要件によって橋を架ける
            → MBPMで再測定する
```

このFlowでは、「価値があるか」と「受け手にSlopとして経験されるか」を
別の判断軸にする。

- 価値がないなら、受け手の負荷が小さくても続ける理由は弱い
- 価値があり、Slopとして経験されていないなら、維持または段階拡大の候補
- 価値があり、Slopとして経験されているなら、変化そのものを捨てる前に、
  受け手が次へ進める橋を設計する
- 負荷が業務を止める水準なら、価値の有無にかかわらず流入を一時停止し、
  支援と回復を優先する

これは採用済みのスライド構成ではなく、ここまでの議論を一つのFlowへ
まとめるための候補である。

## タイトルへの回答

会話では、最終的に「AI Slopを生まない」というタイトルの前提を
次のように反転させた。

> AI Slopは防げない。

受け手とのズレには、実際にOutputを渡して初めて分かるものがある。
そのズレは、価値のないゴミかもしれず、必要なTransformationの摩擦かも
しれない。

そのため、設計対象はSlopゼロではない。

- 事前に下流Riskを想定する
- 小さく流す
- MBPMでハンドオーバーを観測する
- 受け手のSlop感をSignalとして拾う
- 業務を守るために流量を制御し、必要なら停止する
- 価値がないOutputを捨てる
- 価値ある変化なら、Enablementによってハンドオーバーを修正する
- 修正して再開する

> AI Slopを生まないPlatform Serviceとは、
> Slopを一切生成しないServiceではない。
> Slopを未検知、未制御のまま下流へ流し続けないServiceである。

短い表現候補:

> AI Slopは防げない。だから、Platform Serviceとして備える。

```text
Observe
Control
Stop
Learn
Enable
Recover
```

最終定義候補:

> AI Slopを生まないPlatform Service設計とは、
> Slopの発生をゼロにすることではない。
> 受け手側に現れたズレを早く観測し、業務への影響を制御し、
> 価値のないOutputを捨て、価値ある変化ならEnablementによって
> ハンドオーバーを修復できるようにすることである。

## 現時点の留保

- このメモは、人間とAssistAの対話をCodexが構造化した混合由来のRaw Note
- ここにある定義、分類、Metric、非機能要件は、登壇への採用決定ではない
- AI Slopの善悪に関する一般的な定義を確立したものではない
- Agile Transformationに関する記述は、体系的な調査結果ではなく、
  議論中の一般化である
- MBPMとVSMの関係はExternal Inputを参照したが、
  今回の適用方法が有効であることは未検証
- `% Complete & Accurate`は強いSignal候補だが、
  AI Slopを単独で判定するMetricではない
- Risk Thresholdや停止条件の具体値は未測定であり、
  会話中の数値例をRepositoryの基準として採用していない
- EnablementまたはMarketingの役割とCapacity配分は、
  すべてのPlatform Teamへ一般化できない
- 顧客または案件を再識別できる情報は記録していない

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
