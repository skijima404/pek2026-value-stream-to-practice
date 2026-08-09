---
id: HYP-20260801-004822-coupled-observability-detects-cost-transfer
type: hypothesis_episode
title: "PEのDVSと利用者側OVSを接続するとAI高速化のCost Transferを検知できる"
content_language: ja
created_at: 2026-08-01T00:48:22+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-09T21:16:50+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260801-004820-coupled-platform-value-streams
  - type: derived_from
    target: OBS-20260731-120412-value-and-slop-experience-decision-flow
  - type: derived_from
    target: OBS-20260809-203134-downstream-load-frequency-induced-work
  - type: tests
    target: HYP-20260804-183210-ai-slop-downstream-burden-value
---

# 仮説

Platform Serviceを作るPEのDevelopment Value Stream（DVS）と、Serviceを使う
利用者側のOperational Value Stream（OVS）を、Release、利用開始、Enablement、
Support、Feedbackの境界で接続して観測すれば、AIで一工程を高速化した結果が、
別Teamの確認、修正、判断、個別支援、保守へCostとして移った状態を、局所的な
速度指標だけを見る場合より早く検知できる。

## 知識の成立根拠

`OBS-20260801-004820-coupled-platform-value-streams`に記録された、PEのDVSと利用者側OVSを
接続して扱う実践者の整理と、`OBS-20260731-120412-value-and-slop-experience-decision-flow`の
価値とSlop経験を分ける判断Flowを組み合わせた。

`OBS-20260809-203134-downstream-load-frequency-induced-work`には、下流負荷を一回あたりの
処理Cost、発生回数、対象Resourceおよび誘発された手戻り・待ち・再作業から評価する候補が
記録されている。これはCost Transferの規模を観測する設計候補であり、DVSとOVSを接続した
観測が実際にCost Transferを早く検知した検証Evidenceではない。

## Mobiusでの位置づけ

`solution`

親となるValue Hypothesis
`HYP-20260804-183210-ai-slop-downstream-burden-value`に対して、作成速度とは別に
価値と副作用を検証するための観測方法を置くSolution Hypothesisである。

## 期待する兆候

- 提供側で短縮したProcess Timeと同時に、利用側で増えた確認、修正、問い合わせを
  同じ変更の影響として発見できる
- 利用者側で減った作業と、Platform Team側へ増えたSupport、例外対応、知識更新を
  対にして確認できる
- 採用率または利用率だけでなく、期待Outcome、継続利用、下流負荷、提供側の
  持続可能性を分けて判断できる
- 観測結果が、提供側のDiscovery、Decision、Service改善または停止判断へ戻る

## 反証またはChallengeとなる兆候

- 二つのValue Streamを接続しても、Costの移動元と移動先を対応づけられない
- 観測項目が増えるだけで、既存の局所指標より早い検知または良い判断につながらない
- 測定と関連づけのCostが、発見できる副作用に対して過大になる
- 組織の投資目的または施策のValue Hypothesisが不明なため、変化を評価できない

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | DVSとOVSのSignalを接続すると、局所指標だけでは見えない追加作業の発生箇所、移動元および移動先を同じ変更の影響として特定できる | critical | none | not_checked | unknown | unknown | 実在するPlatform Serviceについて、二つのValue Streamと同一変更を対応づけていない |
| U2 | 一回あたりの処理Cost、発生回数、対象Resourceおよび誘発作業を確認すると、Cost Transferの規模と改善Priorityを判断可能な粒度で評価できる | high | none | not_checked | unknown | unknown | 評価候補は記録されたが、単位、対象期間、重複計上、因果および共通単位への換算を確認していない |
| U3 | 接続した観測は、局所指標だけの場合より早くCost Transferを検知し、Discovery、改善、支援、継続または停止の判断を更新できる | critical | none | not_checked | unknown | unknown | 検知時点の比較、判断者、更新された判断および介入後の変化を確認していない |
| U4 | 二つのValue Streamを接続し、下流負荷を測定・関連づけるCostは、発見できる副作用と更新できる判断に対して妥当である | high | none | not_checked | unknown | unknown | Data取得、分析、調整に必要な時間とSkill、および簡略化できる条件を確認していない |

## 検証方法

### 方法と対象範囲

- 方法:
  一つのPlatform ServiceまたはAI導入施策を選び、変更前後について提供側と
  利用側の簡易Value Streamを作る。高速化したStep、Release境界、利用開始後の
  追加作業、Support、Outcomeを対応づけ、従来の局所指標だけでは見えなかった
  影響が見つかるかを確認する。一回あたりの処理Cost、発生回数、対象Resource、
  誘発された手戻り・待ち・再作業、および観測と分析に要したCostを記録し、
  検知時点と更新された判断を局所指標だけの場合と比較する。
- 対象・資料: 未選定
- 選定方法:
  提供側の変更と利用側の反応を同じ期間またはServiceで追える小さな事例を優先する
- 実施規模:
  最初は一つのServiceまたは一つの変更に限定する

### GenAIの利用

- 利用内容:
  記録からActor、Step、Handover、追加作業候補を抽出し、二つのMapの対応候補を
  整理する
- GenAIだけで実施しないこと:
  Costの発生、利用者Outcome、因果関係を生成結果から推定する
- 実際に確認した資料・記録:
  現時点ではrelationで示したRepository Nodeのみ

## 結果

`not_tested`

### 実際に観測したこと

PEのDVSと利用者側OVSを接続する考えと、価値とSlop経験を分ける判断Flowは
Repositoryに記録されている。下流負荷を一回あたりの処理Cost、発生回数、対象Resource
および誘発作業から評価する候補も記録された。これは観測設計の具体化であり、実際の
Serviceについて、接続した観測が局所指標より早くCost Transferを発見した事例は、
まだ保存されていない。

## 解釈

このEpisodeが置く新しい因果は、二つのValue Streamを接続する観測方法が、
AI高速化による局所最適とCost Transferの検知に有効だという点である。

これは共通KPIの採用ではなく、Value Hypothesisに対応する変化と、前後のActorへ
移った作業を追える状態を作る提案である。

## 限界

- Value Stream間のCostを共通単位へ換算できるとは限らない
- 同時期の組織変更、需要変化、Service成熟などを分離する必要がある
- Trust、学習、疲弊などの変化は短期間のMapだけでは捉えにくい
- このEpisodeは、登壇上の主張または測定方法として採用されたものではない

## 公開安全性確認

- checked_at: 2026-08-09T21:16:50+09:00
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
