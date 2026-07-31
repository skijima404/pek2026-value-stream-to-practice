# 分析

Raw Noteや外部入力から作った派生ノードを置きます。

- `observations/`: 根拠の範囲を限定した観察
- `hypothesis-episodes/`: 小さな仮説と検証結果
- `patterns/`: 複数episodeを横断する再利用可能な解釈

本文は日本語で記述します。人間が内容と意図の一致を確認した分析は
`status: reviewed` とします。分析ノードでは `status: accepted` を使用しません。
現在の登壇成果物として採用する場合は、明示的な採用判断と根拠を
`03_artifacts/` に記録します。

## このIndexの扱い

このREADMEは、既存Nodeを見つけ、現在のReasoning Chainを追うための
再生成可能なNavigation Viewです。Evidence、派生Claim、採用判断、現在の
正本ではありません。

- 内容の正本は、リンク先のNodeとArtifactです。
- status、confidence、result、relationを、リンク先を越えて解釈しません。
- このIndexに載っていないことを、却下や不存在の証拠として扱いません。
- NodeやArtifactと矛盾する場合は、リンク先を優先してIndexを再生成します。

## 現在のReasoning Chain

```text
参加者の成功条件とJourney
  -> Observationとして整理
  -> 参加者Journey兼Value Streamとして採用済み

Audienceと価値課題の見立て
  + 採択済み方向性とDelivery範囲
  -> AI速度と価値選択・検証の必要性というValue Hypothesis
  -> 未検証

AIの局所高速化、ハンドオーバー、リレー、早期中止判断
  -> 構成要素と表現選択をObservationとして整理
  -> リレー中心のSession StoryというSolution Hypothesis
  -> 人間の意図Review済み、未検証、未採用

AI SlopによるCost外部化
  + Release前のValue Hypothesis検証と早期廃棄
  -> Lean Startupの選別をAdmission Controlとして使うSolution Hypothesis
  -> 人間の意図Review済み、未検証、未採用

PEのDevelopment Value Stream（DVS）
  + 利用者側Operational Value Stream（OVS）
  + 価値とSlop経験を分ける判断Flow
  -> 二つのValue Streamを接続したObservabilityというSolution Hypothesis
  -> 人間の意図Review済み、未検証、未採用

AI生成物またはPlatform ServiceのHandover
  + Contract、Accountability、Cost Transferの分離
  -> 共有前のService Contract明確化というSolution Hypothesis
  -> 人間の意図Review済み、未検証、未採用

BCGの10–20–70関連資料
  -> 説明対象の違いをObservationとして整理
  -> 登壇上の主張やArtifactには未採用
```

## MobiusによるHypothesis一覧

| Map | Level | Hypothesis Episode | Intent Review | Result |
| --- | --- | --- | --- | --- |
| Discovery | `value` | [AIによる作成速度向上は価値選択と検証の必要性を高める](./hypothesis-episodes/HYP-20260730-015718-ai-speed-requires-value-validation.md) | `proposed` | `not_tested` |
| Decision | `solution` | [リレーを中心にしたセッション構成ならAI SlopからVSMまでを一本道で伝えられる](./hypothesis-episodes/HYP-20260731-004119-relay-centered-session-story.md) | `reviewed` | `not_tested` |
| Decision | `solution` | [Lean Startupの選別と早期廃棄は未検証案のコスト外部化を抑える](./hypothesis-episodes/HYP-20260731-193520-lean-startup-as-admission-control.md) | `reviewed` | `not_tested` |
| Decision | `solution` | [PEのDVSと利用者側OVSを接続するとAI高速化のCost Transferを検知できる](./hypothesis-episodes/HYP-20260801-004822-coupled-observability-detects-cost-transfer.md) | `reviewed` | `not_tested` |
| Decision | `solution` | [共有前のService Contract明確化は下流への理解と判断Costの転移を抑える](./hypothesis-episodes/HYP-20260801-004823-service-contract-reduces-downstream-cost.md) | `reviewed` | `not_tested` |
| Delivery | `feature` | 該当するEpisodeなし | — | — |
| 未分類 | `not_assessed` | [開催側の採択を方向性継続の十分なシグナルとして扱う](./hypothesis-episodes/HYP-20260730-015717-organizer-selection-is-sufficient-signal.md) | `reviewed` | `supports` |

`supports` となっている採択シグナルは、Proposalの大方向を維持して制作を
進める判断に限定されます。Audience課題やValue Hypothesisの正しさを支持する
結果ではありません。

## Observation一覧

| Observation | Status | Confidence | 現在の接続先 |
| --- | --- | --- | --- |
| [セッション成功条件と参加者Journeyの原案](./observations/OBS-20260730-015714-session-goal-and-journey.md) | `reviewed` | `high` | 採用済みJourney／Value Stream |
| [採択済み方向性とDeliveryの検討範囲](./observations/OBS-20260730-015715-accepted-direction-and-delivery-scope.md) | `reviewed` | `high` | 採択シグナルHypothesis、Value Hypothesis、採用済みJourney |
| [Audienceと価値課題について記録された見立て](./observations/OBS-20260730-015716-audience-and-value-problem-statements.md) | `reviewed` | `high` | 採択シグナルHypothesis、Value Hypothesis |
| [BCG資料内で10–20–70の説明対象が変化している](./observations/OBS-20260730-210822-bcg-10-20-70-claim-variation.md) | `reviewed` | `high` | 現時点ではHypothesis／Artifactへのrelationなし |
| [リレー中心の構成候補を形成した要素と表現選択](./observations/OBS-20260731-021631-relay-story-source-elements.md) | `reviewed` | `high` | リレー中心のSession Story Hypothesis |
| [価値判断と受け手のSlop経験を分ける判断Flowが記録された](./observations/OBS-20260731-120412-value-and-slop-experience-decision-flow.md) | `reviewed` | `high` | 作成者の現場実践として確認済み、Slide構成には未採用 |
| [Platform Serviceの提供側と利用側を接続して観測する考えが記録された](./observations/OBS-20260801-004820-coupled-platform-value-streams.md) | `reviewed` | `high` | DVSとOVSを接続したObservability Hypothesis |
| [ハンドオーバーとContractとCost Transferを分ける考えが記録された](./observations/OBS-20260801-004821-contract-accountability-cost-transfer.md) | `reviewed` | `high` | Service Contract Hypothesis |

`confidence` は確率ではなく、Evidenceや限界の記述を置き換えるものでも
ありません。根拠と詳細な限界はリンク先を確認します。

## 採用済みArtifact

- [参加者Journey兼Value Stream](../03_artifacts/attendee-journey.md)
  - `adopted_by: human:kijima`
  - 発見・選択、参加、復習、現場適用までを対象とする現在の正本
- [Value Stream](../03_artifacts/value-stream.md)
  - 参加者Journeyを正本として参照する短いCanonical Entry

現在のSession Story、Slides、Speaker Notes、Participant Takeawayは未採用です。

## まだRaw Noteにだけ存在する主要テーマ

次のRaw Noteには、現在のAnalysisまたはArtifactから直接のtyped relationが
ありません。これは却下を意味せず、未昇格または別経路で扱っている状態です。

- [PEK2026プレゼンテーション候補ネタ集](../01_working/raw-notes/RN-20260730-093311-presentation-idea-inventory.md)
- [Workモード引き継ぎからのプレゼンテーション追加候補](../01_working/raw-notes/RN-20260730-095321-work-mode-idea-supplement.md)
- [Discoverの欠落感と前回登壇からの接続](../01_working/raw-notes/RN-20260730-101222-discovery-gap-and-talk-continuity.md)
- [AI活用で狙うOutcomeと人間・AI協業モデル](../01_working/raw-notes/RN-20260730-102859-ai-outcomes-and-collaboration-model.md)
- [本編とRepositoryへの導線の役割分担](../01_working/raw-notes/RN-20260730-103954-session-repo-role.md)
- [Value Streamの課題からAIで狙う効果を考える](../01_working/raw-notes/RN-20260730-111926-value-stream-ai-outcomes.md)
- [70%失敗説の出典探索と不採用判断](../01_working/raw-notes/RN-20260730-224354-seventy-percent-failure-source-check.md)
- [MBPMで観測できないAI SlopとOutcome Quality](../01_working/raw-notes/RN-20260731-143326-mbpm-blind-spots-and-outcome-quality.md)
- [Enablementで橋を架け続けるべきでない境界](../01_working/raw-notes/RN-20260731-204459-enablement-bridge-boundaries.md)
- [AIをValue Streamへ配置するResource Management](../01_working/raw-notes/RN-20260731-214443-ai-resource-management-in-value-stream.md)
- [Slopと感じても残すべき摩擦](../01_working/raw-notes/RN-20260731-214443-necessary-friction-experienced-as-slop.md)

## Patternの状態

現在、Patternは0件です。

6件のHypothesis Episodeは異なる範囲を扱っており、複数Episodeを横断して
繰り返し検証された関係はまだ記録されていません。Indexを埋める目的でPatternを
作らず、複数の検証結果と反例確認が揃ったときに提案します。

## 未解決事項

- AI速度と価値選択・検証のValue Hypothesisは `not_tested` のままです。
- Lean Startupの選別と早期廃棄をAdmission Controlとして使うSolution
  Hypothesisは `not_tested` のままです。
- PEのDVSと利用者側OVSを接続した観測が、局所指標より早くCost Transferを検知
  できるかは `not_tested` です。
- 共有前のService Contract明確化が、受け手の理解、検証、判断Costを減らすかは
  `not_tested` です。
- リレー中心のSession Storyは、25分Walkthrough、代替案比較、第三者Reviewが
  未実施です。
- MobiusのFeature Hypothesisに該当するEpisodeはまだありません。
- 想定Audienceの課題と参加者Journeyは、参加者への直接確認を経ていません。
- 現場適用、Live Document、Takeawayの有効性は未検証です。

## 更新するタイミング

次の場合に、NodeとArtifactを再読してこのIndexを再生成します。

- Observation、Hypothesis Episode、Patternを追加または実質変更したとき
- status、confidence、result、relationが変わったとき
- Artifactを採用、更新、置換したとき
- 人間が現在の全体像やReasoning Chainの整理を依頼したとき
