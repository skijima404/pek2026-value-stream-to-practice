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
- status、knowledge_basis、confidence、result、hypothesis_scope、
  hypothesis_level、relationを、リンク先を越えて解釈しません。
- このIndexに載っていないことを、却下や不存在の証拠として扱いません。
- NodeやArtifactと矛盾する場合は、リンク先を優先してIndexを再生成します。

## Knowledge Basisの読み方

`knowledge_basis`は、内容がどの種類の知識に基づいて成立したかを示します。
正しさ、意図Review、検証結果、登壇への採用とは別の軸です。

- `recorded_statement`: Sourceに記録された発言、計画、選好、見立て
- `practitioner_experience`: 実務経験の蓄積から形成された判断または方法論
- `case_recollection`: 再確認できる一次記録がない、特定事例についての記憶
- `external_research`: 実際に確認し、Sourceとして保存した外部資料
- `direct_observation`: 範囲を限定して記録された実際の行動、出来事、状態
- `explicit_validation`: 実施済みのTest、Interview、Reviewなどの検証活動
- `reasoned_synthesis`: 複数Sourceの接続または解釈によって作った推論

複数のBasisを併記できます。`practitioner_experience`と`not_tested`の併記は、
実務経験に根拠を持つが、このRepositoryでは独立検証していない状態です。
経験知の価値を消さず、普遍的事実または検証済みEvidenceにも変換しません。

## 現在の全体像

Hypothesis Episodeは同じフォルダに置き、`hypothesis_scope`で二つの独立した
Value／Solution／Feature階層を表します。子から直上の親だけを`tests`で接続します。

### Session scope

```text
Value: AudienceがAI Slopを制御するActionを持ち帰る価値
  └─ tests ← Solution: 構造・Signal・仮説検証を一続きに説明する
       ├─ tests ← Feature: リレーを中心にした25分トーク
       └─ tests ← Feature: 一枚の補助説明とRepositoryへの導線
```

Session ValueはAI PoC InterviewのEvidence追加後に`reviewed`で、結果は
`inconclusive`です。Solutionと二つのFeatureはすべて`reviewed`で、3つの子Nodeは
いずれも`not_tested`です。
人間の意図Reviewまたは限定的な検証は、Session StoryやSlidesへの採用を意味しません。

### Practice scope

```text
Value: AI高速化による回避可能な下流負荷を特定・制御・削減できる状態
  ├─ tests ← Solution: 価値選択と検証
  │    └─ tests ← Feature: Value Hypothesis・期待Signal・停止条件によるAdmission Control
  ├─ tests ← Solution: DVSとOVSを接続した観測
  ├─ tests ← Solution: Service Contract
  ├─ tests ← Solution: Outcome-firstのAI Capability配置
  └─ tests ← Solution: 二段階Metric分析
```

Practice Valueと価値選択・検証Solutionは`reviewed`かつ`inconclusive`です。
他の4 Solutionは`reviewed`かつ`not_tested`です。Admission Control Featureは階層と
意味の変更後に再Reviewされ、`reviewed`かつ`not_tested`です。子の結果は親へ
自動的には推移しません。

Platform選定に関する別のPractice階層も、次の未検証候補として記録しています。

```text
Value: 選定へ関与する利用者の探索・判断準備負荷を軽減する
  └─ tests ← Solution: Contextを確認するPlatform Advisor
       └─ tests ← Feature: 選定作業を一つのChatへ統合する
```

3 Nodeはいずれも`reviewed`かつ`not_tested`です。架空Scenario内のPrototype結果、PT、
LTおよびGuardrailはEvidenceではありません。このValueは、選択を望む利用者Segmentに
限定し、安全な標準Pathを望む利用者のValue Hypothesisと競合または併存し得ます。
これらは参照、比較またはScenario作成へ再利用するHypothesis Modelであり、現在この
Repositoryで検証する予定はありません。記載した検証方法は現在の実施計画ではありません。

選択を負担と感じる利用者については、別の未検証階層を記録しています。

```text
Value: 安全な標準Pathによって選択負荷を軽減する
  └─ tests ← Solution: 組織が責任を持つ標準Pathと例外Routing
```

Valueと子Solutionは`reviewed`かつ`not_tested`です。選択の自由を求めるSegmentと
標準Pathを求めるSegmentを混同せず、競合または併存するSolutionとして比較します。
子Solutionは物語内の解説に使うHypothesis Modelであり、このRepositoryでは検証を
予定していません。標準Path側のFeature Hypothesisはまだ作成していません。

### Standaloneまたは未分類のHypothesis

- [DVSの仮説検証と学習品質はOVS品質の継続的改善に必要である](./hypothesis-episodes/HYP-20260807-232639-dvs-learning-sustains-ovs-quality.md)
  - `practice`、`solution`、`reviewed`、`inconclusive`
  - 今回の統合Expert Reviewを保持するEpisodeとして、今後は新しいEvidenceを継ぎ足さない
  - OVS品質の一時的な成功と、再現・適応・修正を含む継続性を分ける
  - 個別Cycle品質と複数Cycleをまたぐ組織的学習Capabilityを分ける
  - DVS品質をOVS品質から独立に判定するOperational Definition候補と、既存HYPに合わせた
    Component判定条件を追加した
  - 限定的なExpert ReviewによりU1〜U4を`partially_checked`とした
  - U2は個人によるCapability代行のMechanismだけを限定的に支持する
  - U3はPackage型のData Contract欠落とScratch型のBusiness Use Case欠落を分けて扱う
  - ITSMのCase Recollectionは学習Mechanismの類似経験であり、Platform Serviceへの直接Evidenceではない
  - 既存Practice Valueより広いOVS品質を扱うため、現時点では階層親への`tests`を置かない
- [個人による学習機能の代行または好条件があれば制度化されたCapabilityなしでも一回の成功は起こり得る](./hypothesis-episodes/HYP-20260809-013741-individual-learning-substitution-one-shot-success.md)
  - `practice`、`solution`、`reviewed`、`inconclusive`
  - 旧統合EpisodeのU2を、今後独立して検証するために分離した
  - 個人代行のMechanismだけが`partially_checked / supports / contextual`で、Bounded Caseと継続性は未確認
- [Valueから意思決定・Data・利用・OutcomeへのTraceabilityはDVSの継続的学習を成立させる](./hypothesis-episodes/HYP-20260809-013742-value-traceability-enables-dvs-learning.md)
  - `practice`、`solution`、`reviewed`、`inconclusive`
  - 旧統合EpisodeのU3を、Package型とScratch型を分けて検証するために分離した
  - Mechanismの構成要素は確認したが、判断更新またはOutcomeへの効果は未確認
- [Solution-firstから検証可能な仮説を再構成するPractice Solution](./hypothesis-episodes/HYP-20260802-230423-solution-first-reconstruction-testability.md)
  - `practice`、`solution`、`reviewed`、`not_tested`
  - 主階層への`tests`はなく、価値選択と検証のPractice Solutionを`references`する
- [開催側の採択を方向性継続のSignalとして扱うHypothesis](./hypothesis-episodes/HYP-20260730-015717-organizer-selection-is-sufficient-signal.md)
  - `session`、`not_assessed`、`reviewed`、`supports`
  - Value／Solution／Feature階層には分類されていない

## 再生成可能なView

詳細な横断表示は、役割ごとに次のViewへ分離しています。これらはEvidence、
派生Claim、採用判断、現在の正本ではありません。内容がNodeまたはArtifactと
矛盾する場合は、リンク先を優先してViewを再生成します。

- [Sourceと派生Reasoning Chain](./views/reasoning-chain.md):
  SourceからAnalysis、Artifactへ至る接続の詳細
- [MobiusによるHypothesis一覧](./views/mobius-hypothesis-map.md):
  `session`と`practice`を分離したHypothesis階層とCross-scope connection
- [Evidence Coverageと残存リスク](./views/evidence-status.md):
  現在の検証状況と、Nodeに明記された未解決事項

## Observation一覧

| Observation | Knowledge Basis | Status | Confidence | 現在の接続先 |
| --- | --- | --- | --- | --- |
| [セッション成功条件と参加者Journeyの原案](./observations/OBS-20260730-015714-session-goal-and-journey.md) | `recorded_statement` | `reviewed` | `high` | 採用済みJourney／Value Stream |
| [採択済み方向性とDeliveryの検討範囲](./observations/OBS-20260730-015715-accepted-direction-and-delivery-scope.md) | `external_research`, `recorded_statement` | `reviewed` | `high` | 採択シグナルHypothesis、Value Hypothesis、採用済みJourney |
| [Audienceと価値課題について記録された見立て](./observations/OBS-20260730-015716-audience-and-value-problem-statements.md) | `recorded_statement` | `reviewed` | `high` | 採択シグナルHypothesis、Value Hypothesis |
| [BCG資料内で10–20–70の説明対象が変化している](./observations/OBS-20260730-210822-bcg-10-20-70-claim-variation.md) | `external_research` | `reviewed` | `high` | 現時点ではHypothesis／Artifactへのrelationなし |
| [リレー中心の構成候補を形成した要素と表現選択](./observations/OBS-20260731-021631-relay-story-source-elements.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `high` | リレー中心のSession Story Hypothesis |
| [価値判断と受け手のSlop経験を分ける判断Flowが記録された](./observations/OBS-20260731-120412-value-and-slop-experience-decision-flow.md) | `practitioner_experience` | `reviewed` | `high` | 作成者の現場実践として確認済み、Slide構成には未採用 |
| [Platform Serviceの提供側と利用側を接続して観測する考えが記録された](./observations/OBS-20260801-004820-coupled-platform-value-streams.md) | `reasoned_synthesis` | `reviewed` | `high` | DVSとOVSを接続したObservability Hypothesis |
| [ハンドオーバーとContractとCost Transferを分ける考えが記録された](./observations/OBS-20260801-004821-contract-accountability-cost-transfer.md) | `external_research`, `reasoned_synthesis` | `reviewed` | `high` | Service Contract Hypothesis |
| [Solution候補からChallengeとValue Hypothesisを再構成する技法が記録された](./observations/OBS-20260802-230422-solution-first-hypothesis-reconstruction.md) | `case_recollection` | `reviewed` | `high` | Solution-first再構成Hypothesis |
| [Platform Advisorには利用者がPlatformを選びたいという隠れた前提が記録された](./observations/OBS-20260802-230424-platform-choice-hidden-assumption.md) | `practitioner_experience` | `reviewed` | `high` | Platform選択負荷のValue Hypothesis |
| [プロジェクトと変革の失敗率は対象と成功定義が異なり統合できない](./observations/OBS-20260802-230426-failure-rate-definition-mismatch.md) | `external_research` | `reviewed` | `high` | 登壇での利用判断とは分離 |
| [Process上のFlowと最終成果物のOutcome Qualityは別の観測対象として記録された](./observations/OBS-20260802-230427-process-flow-and-outcome-quality.md) | `reasoned_synthesis` | `reviewed` | `high` | 測定方法と接続先は未決定 |
| [Solution-first再構成の有無でTraining中の記述とIdea数に異なる様子が記録された](./observations/OBS-20260804-004530-solution-first-training-behavior.md) | `case_recollection`, `direct_observation` | `reviewed` | `medium` | 既存Solution HypothesisのContext、Validation Resultには不使用 |
| [仮説検証を不確実性の分解と意思決定更新として扱う説明が記録された](./observations/OBS-20260804-004531-hypothesis-validation-uncertainty-decision.md) | `reasoned_synthesis` | `reviewed` | `high` | Lean Startup HypothesisのContext |
| [前回登壇で対象Journeyを特定し今回VSM・MBPMへ展開する前後関係が記録された](./observations/OBS-20260804-004532-journey-before-vsm-mbpm.md) | `external_research`, `recorded_statement` | `reviewed` | `high` | 前回登壇と今回の検討範囲の接続 |
| [Customerへの確認ではDiscovery結果が未定義または担当者に理解されていなかった](./observations/OBS-20260804-013221-discovery-practice-gap.md) | `practitioner_experience` | `reviewed` | `medium` | Solution-firstが起こる背景となる限定的な経験知 |
| [Slopとして経験される摩擦にも残す目的があり得ると整理された](./observations/OBS-20260804-013222-necessary-friction-boundary.md) | `reasoned_synthesis` | `reviewed` | `medium` | 価値とSlop経験を分ける判断Flowの境界条件 |
| [Dashboardと分析を分ける運用がITSMとProject Portfolioで用いられた](./observations/OBS-20260804-013225-itsm-metrics-analysis-practice.md) | `practitioner_experience`, `case_recollection` | `reviewed` | `medium` | 二段階メトリック分析Hypothesis |
| [今回のProblem Spaceは2026年4月公開記事に記録され、後続準備で実践方法が追加された](./observations/OBS-20260804-014228-prior-article-session-continuity.md) | `external_research`, `recorded_statement`, `reasoned_synthesis` | `reviewed` | `high` | 先行する自己資料と今回の実践方法の連続性 |
| [Workslopの受け手は追加作業と信頼低下を自己申告している](./observations/OBS-20260805-001807-workslop-recipient-burden.md) | `external_research` | `reviewed` | `high` | Practice Value U6への`analogous`な限定Evidence、U1への適用候補 |
| [良いハンドオーバーには受け手の判断に必要なContextが含まれると整理された](./observations/OBS-20260805-001808-decision-context-handover.md) | `case_recollection`, `reasoned_synthesis` | `reviewed` | `medium` | Service Contract Hypothesisを補助するContext |
| [個別Enablementの反復はService設計の人力補完を示す兆候として整理された](./observations/OBS-20260805-001810-repeated-enablement-dependency-signal.md) | `reasoned_synthesis` | `reviewed` | `medium` | Service Contract、Persona、Service Scopeの未検証Signal |
| [提案書の生成短縮後に別担当者へ検証・再構築・意味変換の作業が移り生成停止が判断された](./observations/OBS-20260804-195508-ai-proposal-generation-shifted-review-burden.md) | `case_recollection`, `explicit_validation` | `reviewed` | `medium` | Practice ValueのU1・U2・U3・U4・U7に対する`analogous`な限定Evidence |
| [下流負荷制御の優先度はServiceの目的とOutputの可逆性に依存すると整理された](./observations/OBS-20260805-005540-downstream-control-priority-reversibility.md) | `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `medium` | Practice ValueのU5・U6に対する`contextual`な境界条件 |
| [3人へのヒアリングで着手・価値説明・下流負荷の問題とAI Slop対処への関心が記録された](./observations/OBS-20260805-223704-audience-problems-and-ai-slop-interest.md) | `recorded_statement`, `explicit_validation` | `reviewed` | `medium` | Session ValueのU1・U2に対する`contextual`な限定Evidence |
| [本人Interviewで機能評価型AI PoCがBusiness活用判断へ接続しなかった事例が記録された](./observations/OBS-20260805-225027-function-evaluation-poc-business-use-gap.md) | `recorded_statement`, `case_recollection`, `explicit_validation` | `reviewed` | `medium` | Session Value U1への`contextual`なEvidence、価値選択と検証Solution U1への`inconclusive`なContrast Case |
| [Reasoning Chainの構造確認・網羅性Review・実証的検証は別の確認として記録された](./observations/OBS-20260807-211648-structural-coverage-empirical-checks.md) | `recorded_statement`, `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `high` | Solution-first再構成Hypothesisの検証対象分解 |
| [AI Featureの効果測定を直接効果・Guardrail・中間Signal・Business Outcomeへ分ける設計が記録された](./observations/OBS-20260807-211649-effect-measurement-layers.md) | `recorded_statement`, `reasoned_synthesis` | `reviewed` | `high` | Platform Advisor Feature Hypothesisの測定設計 |
| [VSM・MBPMで観測した摩擦だけではProblemの原因構造を一意に決められないと整理された](./observations/OBS-20260807-211650-vsm-problem-causal-ambiguity.md) | `recorded_statement`, `reasoned_synthesis` | `reviewed` | `medium` | Platform選定Value Hypothesisの原因候補とSelection Bias |
| [仮説検証は外れ方を観測しProblem・Value理解と継続判断を更新する反復として整理された](./observations/OBS-20260807-223144-iterative-problem-understanding.md) | `recorded_statement`, `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `high` | 価値選択と検証Solutionの学習Loopと廃棄判断 |
| [DVSのシステム学習は定義したProblemへの判断十分性まで含むと整理された](./observations/OBS-20260808-204750-dvs-system-learning-decision-sufficiency.md) | `recorded_statement`, `practitioner_experience`, `case_recollection`, `reasoned_synthesis` | `reviewed` | `medium` | DVS学習継続性Hypothesisへ`derived_from`で接続 |
| [手の届くValue Streamでは利用者Value・副作用・Cost移転を分けて確認すると整理された](./observations/OBS-20260808-204751-reachable-value-stream-impact-guardrails.md) | `recorded_statement`, `practitioner_experience`, `case_recollection`, `reasoned_synthesis` | `reviewed` | `medium` | DVS学習継続性Hypothesisへ`derived_from`で接続 |
| [組織的DVS学習機能の個人代行とValueからData Contractへの接続が整理された](./observations/OBS-20260808-222203-individual-substitution-and-value-data-contract.md) | `recorded_statement`, `practitioner_experience`, `reasoned_synthesis` | `reviewed` | `medium` | 旧統合HYPのU2・U3と、個人代行およびValue Traceabilityの新規HYPへ接続 |
| [Scratch開発ではBusiness Use Caseが失われSystem Use Caseだけが共有される場合がある](./observations/OBS-20260808-224827-business-use-case-loss-in-scratch-development.md) | `recorded_statement`, `practitioner_experience`, `external_research`, `reasoned_synthesis` | `reviewed` | `medium` | 旧統合HYPのU3とValue Traceabilityの新規HYPを具体化 |

`knowledge_basis`は成立根拠の種類、`confidence`は確率ではなく確信度、
`result`は実施した検証の結果です。互いに置き換えず、根拠と詳細な限界は
リンク先を確認します。

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
- [リレー比喩でシステム思考を説明する設計判断](../01_working/raw-notes/RN-20260802-215509-relay-metaphor-as-systems-thinking-translation.md)

## Patternの状態

現在、Patternは0件です。

21件のHypothesis Episodeは異なる範囲を扱っており、複数Episodeを横断して
繰り返し検証された関係はまだ記録されていません。Indexを埋める目的でPatternを
作らず、複数の検証結果と反例確認が揃ったときに提案します。

## 更新するタイミング

次の場合に、NodeとArtifactを再読してこのREADMEと関連Viewを再生成します。

- Observation、Hypothesis Episode、Patternを追加または実質変更したとき
- status、knowledge_basis、confidence、result、hypothesis_scope、
  hypothesis_level、relation、Validation Componentが変わったとき
- Risk Decisionを追加、置換、撤回したとき
- Artifactを採用、更新、置換したとき
- 人間が現在の全体像、Reasoning Chain、Mobius ViewまたはEvidence Statusの整理を依頼したとき
