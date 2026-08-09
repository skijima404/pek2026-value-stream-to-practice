# Sourceと派生Reasoning Chain

[分析Indexへ戻る](../README.md)

このファイルは、既存NodeとArtifactを横断して探すためにRepository authorが保守する
非同期な解説Viewです。Evidence、派生Claim、採用判断、現在の正本ではなく、Source更新との
同期も保証しません。現在のstatus、result、relationおよびCoverageは生成Viewで候補を絞り、
リンク先のNodeを直接確認します。内容がリンク先と矛盾する場合はリンク先を優先します。

以下はScope階層ではなく、Observation、Hypothesis、ArtifactがどのSource themeから
形成されたかを追うための詳細Viewです。

```text
参加者の成功条件とJourney
  -> Observationとして整理
  -> 参加者Journey兼Value Streamとして採用済み

Audienceと価値課題の見立て
  + 参加者が試したいと思うこと、または一つ持ち帰って試すという成功条件
  -> AI Slopを制御するActionを持ち帰ることのSession Value Hypothesis
  -> 構造・Signal・仮説検証を一続きに説明するSession Solution Hypothesis
  -> Session ValueのU1・U2を3人へのヒアリングで限定的に検証
  -> Session Solutionは未検証、いずれも未採用

3人へのAudienceヒアリング
  -> 機能・着手点、受領物による仕事の増加、効果説明に関する問題を記録
  -> 3人全員が未検知・未制御のAI Slopを流さない方法を聞きたいと回答
  -> Session ValueのU1・U2を`partially_checked / supports / contextual`として更新
  -> Risk特定、Action選択、実際の試行およびAudience全体への一般化は未確認

機能評価型AI PoCについての本人Interview
  -> 機能評価とReport作成を中心とする複数PoCがBusiness活用判断へ接続しなかった
     一事例をObservationとして整理
  -> Session ValueのU1に`contextual`な追加Evidence
  -> 価値選択と検証のPractice Solutionでは、機能評価側だけを確認した
     `inconclusive`なContrast Case
  -> Value Hypothesisを明示した比較、原因、下流Costおよび一般性は未確認

AIの局所高速化、ハンドオーバー、リレー、早期中止判断
  -> 構成要素と表現選択をObservationとして整理
  -> リレー中心の25分トーク構成というSession Feature Hypothesis
  -> 人間の意図Review済み、未検証、未採用

Human-AI協業モデルと登壇準備Repository
  -> 本編では一枚に限定し、Repositoryを登壇後の深掘りへ使う編集判断
  -> 一枚とRepositoryへの導線というSession Feature Hypothesis
  -> Focus維持、役割理解、閲覧、Action選択を分け、未検証、未採用

BetterUpのWorkslop調査
  -> 受け手が追加作業、感情および送信者への評価を自己申告した結果をObservation化
  -> Platform Engineeringへの適用と因果は未確認

判断Contextを渡すHandoverの事例記憶
  -> Outputだけでなく、問い、意味、根拠、Contextを渡すというObservation
  -> 一次資料を持つ比較ではなく、Case RecollectionとReasoned Synthesisとして保持

個別Enablementを反復する人力補完
  -> Persona、Contract、Service ScopeまたはCapacityの見直しSignalとしてObservation化
  -> 診断精度、因果および介入効果は未確認

AIによる候補流入と下流への確認、判断、手戻り、SupportのCost Transfer
  -> 回避可能な下流負荷を特定・制御・削減できるPractice Value Hypothesis
  -> 価値選択と検証、DVS/OVS観測、Service ContractなどのPractice Solution Hypothesis
  -> Value Hypothesis、期待Signal、停止条件をAdmission Controlとして運用する
     Practice Feature Hypothesis
  -> Session階層とは分離し、価値選択と検証のU1のみ限定的に確認、未採用

PresalesとProject Deliveryを通じた限定的な実務経験
  + Customerへ毎回、目的とDiscovery結果を質問した経験
  -> 確認時点で結果が定義されていないか、担当者が理解していないというObservation
  -> 調査による実施率ではなくpractitioner_experienceとして保持

Value Stream上の課題と期待Outcome
  + AI、Human、PlatformのCapabilityと責任境界
  -> OutcomeからAI Capabilityを配置するSolution Hypothesis
  -> 記録された考えと推論に基づき、未検証、未採用

AI SlopによるCost外部化
  + Release前のValue Hypothesis検証と早期廃棄
  -> 価値選択と検証Solutionを試すAdmission Control Feature Hypothesis
  -> Practice Featureへの意味変更後に人間の意図Review済み、未検証、未採用

PEのDevelopment Value Stream（DVS）
  + 利用者側Operational Value Stream（OVS）
  + 価値とSlop経験を分ける判断Flow
  -> 二つのValue Streamを接続したObservabilityというSolution Hypothesis
  -> 人間の意図Review済み、未検証、未採用

提供側DVSと利用者側OVSを接続する学習Loop
  + 仮説検証を外れ方からProblem・Value理解と判断へ戻す反復
  + Process上のFlowとOutcome Qualityの分離
  -> DVSの仮説検証と学習品質を、OVS品質の継続的改善に対する必要条件として仮説化
  -> 一回の偶発的成功、必要条件、非十分条件および循環論法Riskを分離
  -> DVSシステム学習と手の届くValue StreamのObservationを反映した意味変更について、
     人間の意図Reviewを再実施した
  -> 一回の良質なCycleと、複数Cycleをまたぐ組織的学習Capabilityを分離した
  -> 二つのObservationと既存HYPの判定条件を使った限定的なExpert Reviewを実施
  -> U1は`partially_checked / supports / contextual`、U3は
     `partially_checked / inconclusive / analogous`、U4は
     `partially_checked / inconclusive / contextual`
  -> 個人によるCapability代行とValueからData Contractへの接続を追加し、U2を
     `partially_checked / supports / contextual`へ更新した
  -> Scratch開発におけるBusiness Use Case喪失をU3へ追加した意味変更について、
     人間の意図Reviewを再実施した
  -> Episode全体は`inconclusive`で、未採用

一回限りの基盤移行と、改善Capabilityが未成熟な時期の初回成功に関するCase Recollection
  -> 組織的な学習改善の仕組みがなくても一回の成功は起こり得るというU2候補
  -> 個別Cycle品質、組織的仕組みの有無、成功条件の再利用および継続性は未確認
  -> Raw NoteはCase選定候補であり、Evidence CoverageとFindingには未使用

Valueから意思決定、Data Contract、利用ルールおよびOutcomeへの接続
  + 制度化された組織Capabilityを例外的な個人が局所代行するという実践説明
  -> 名目的なRule遵守とValueを生む利用を分けるObservation候補
  -> U2の個人代行Mechanismを限定的に支持し、U3の社会実装に関する判定内容を具体化
  -> 発生頻度、個人代行とOutcomeの因果、一次記録および継続性は未確認

EnterpriseのScratch開発における要件・設計Reviewの経験
  + [Legacy Systemで失われた要求を復元するDDD Workshopの公開自己資料](../../10_external-inputs/articles/EXT-20260808-224826-ddd-legacy-modernization-workshop-article.md)
  -> Business Use Caseが失われ、帳票・画面・属性・計算というSystem Use Caseだけが
     共有される場合があるというObservation候補
  -> Actorの判断とOutcomeからRequirement・設計・実装までのTraceabilityをU3へ追加
  -> 発生頻度、UX責務認識、利用・Outcomeへの因果および一般性は未確認

Review済みのITSM Case Recollectionとシステム思考の実践説明
  + 定義したProblem、Priority、Responsibility、Decision RightsおよびTime-to-value
  + 手の届くValue Streamにおける利用者Value、副作用、GuardrailおよびCost Transfer
  -> DVSのシステム学習と判断十分性をObservationとして整理
  -> 介入範囲と観測範囲を分け、局所Metricだけで改善を判定しないObservationとして整理
  -> 二つのObservationは人間の意図Review済みで、対象Hypothesisの検証設計Sourceとして接続

AI生成物またはPlatform ServiceのHandover
  + Contract、Accountability、Cost Transferの分離
  -> 共有前のService Contract明確化というSolution Hypothesis
  -> 人間の意図Review済み、未検証、未採用

Solution候補が先に出る実務上の思考順序
  + Challenge、Value、Solutionの役割分離
  + GenAIによるReasoning Chainの構造確認
  + Problem-firstの初期網羅性とSolution-firstの全体品質Trade-off
  -> Solution-firstから検証可能な仮説を再構成するSolution Hypothesis
  -> 構造品質、参加状態、VSM・MBPMによる欠落回収、後続の検証責任へ分解
  -> 人間の意図Review済み、未検証、未採用

Solution-first再構成の有無が異なるTraining記録
  -> Challenge表現、Idea数、所要時間、Facilitator負荷の違いをObservationとして整理
  -> 比較条件が揃っていないため、既存Solution Hypothesisの検証結果には使わない

実際に使用したSolution-first確認Prompt
  + 方法の用途と限界に関する記録
  -> Reasoning Chainの構造確認、VSM・MBPMに対する網羅性Review、実証的な仮説検証を
     別の確認としてObservation化
  -> Promptの使用経験は保持するが、有効性を独立検証した結果にはしない

案に含まれる複数の不確実性
  + Riskを引き受けられる状態まで確からしさを更新する意思決定
  -> 仮説検証を不確実性の分解と意思決定更新として扱う説明をObservationとして整理
  -> 説明の有効性と登壇への採用は未確認

前回登壇で特定したTeam Visionと対象Journey
  -> 今回、そのJourneyをVSM・MBPMへ展開する前後関係をObservationとして整理
  -> 今回の順序であり、VSM・MBPM一般の唯一の作成順序とはしない

Platform Advisorの隠れた前提
  + Platformを選びたい利用者と、選択を負担と感じる利用者
  -> 安全な標準Pathによる選択負荷軽減というValue Hypothesis
  -> 組織が責任を持つ標準Pathと例外RoutingというSolution Hypothesis
  -> 人間の意図Review済み、物語内のHypothesis Modelとして未検証、未採用

Platform Advisorの架空Scenarioと感想戦
  -> VSM・MBPMで観測した摩擦だけでは原因構造を一意に決められないというObservation
  -> 外れ方を観測し、Problem・Value理解と継続判断へ戻る反復というObservation
  -> 選定へ関与し比較したい利用者SegmentのValue Hypothesis
  -> ContextualなPlatform AdvisorのSolution Hypothesis
  -> 選定作業を一つのChatへ統合するFeature Hypothesis
  -> 直接効果、下流Guardrail、中間Signal、Business Outcomeを分ける測定設計
  -> 架空の結果はEvidenceにせず、全Nodeを未検証、未採用として保持

Project・Transformation関連資料の失敗率
  -> 対象、成功定義、Evidenceの性質が異なることをObservationとして整理
  -> Business Outcome未達率としては統合しない

MBPMで観測するProcess上のFlow
  + Output、Experience、Trust、Contract Quality
  -> 別の観測対象としてObservationに分離
  -> 測定方法と既存Observability Hypothesisへの接続は未決定

受け手がSlopとして経験する追加負荷
  + 品質、学習、Accountability、安全性のために残す摩擦
  -> 摩擦を除去するか目的を明示して残すかの境界をObservationとして整理
  -> 実際のServiceでの判定方法と効果は未確認

ITSMで約10年、約3件のProjectに再利用し、Project Portfolioにも持ち込んだ
メトリック分析運用
  -> Dashboardによる定期的な異常検知とBIによる原因診断をObservationとして整理
  -> practitioner_experienceとcase_recollectionを分離
  -> Metric過剰取得を抑えながら改善Loopの頻度と深さを両立するSolution Hypothesis
  -> DashboardとDataだけではなく分析Techniqueの習熟を成立条件とする
  -> 過去の一次資料は未確認、Platform Engineeringは導入初期、未採用

BCGの10–20–70関連資料
  -> 説明対象の違いをObservationとして整理
  -> 登壇上の主張やArtifactには未採用
```

## Supporting Node索引

各themeの正本と状態は、次のリンク先で確認します。この表は上のReasoning Chainを
新しいEvidenceへ変換するものではありません。

| Theme | Supporting nodes |
| --- | --- |
| 参加者の成功条件とJourney | [OBS-20260730-015714](../observations/OBS-20260730-015714-session-goal-and-journey.md)、[参加者Journey兼Value Stream](../../03_artifacts/attendee-journey.md) |
| Audienceと価値課題 | [OBS-20260730-015716](../observations/OBS-20260730-015716-audience-and-value-problem-statements.md)、[Session Value](../hypothesis-episodes/HYP-20260804-183208-audience-actionable-ai-slop-value.md)、[Session Solution](../hypothesis-episodes/HYP-20260804-183209-ai-slop-learning-path-solution.md) |
| Audienceヒアリング | [OBS-20260805-223704](../observations/OBS-20260805-223704-audience-problems-and-ai-slop-interest.md)、[Session Value](../hypothesis-episodes/HYP-20260804-183208-audience-actionable-ai-slop-value.md) |
| 機能評価型AI PoC | [OBS-20260805-225027](../observations/OBS-20260805-225027-function-evaluation-poc-business-use-gap.md)、[Session Value](../hypothesis-episodes/HYP-20260804-183208-audience-actionable-ai-slop-value.md)、[Practice Solution](../hypothesis-episodes/HYP-20260730-015718-ai-speed-requires-value-validation.md) |
| リレー中心のSession | [OBS-20260731-021631](../observations/OBS-20260731-021631-relay-story-source-elements.md)、[Session Feature](../hypothesis-episodes/HYP-20260731-004119-relay-centered-session-story.md) |
| Human-AI協業とRepository | [Raw Note](../../01_working/raw-notes/RN-20260730-102859-ai-outcomes-and-collaboration-model.md)、[Session Feature](../hypothesis-episodes/HYP-20260805-001809-repository-handoff-preserves-focus.md) |
| BetterUp Workslop | [External Input](../../10_external-inputs/research/betterup/EXT-20260804-144101-betterup-workslop-recipient-experience.md)、[OBS-20260805-001807](../observations/OBS-20260805-001807-workslop-recipient-burden.md) |
| 判断ContextのHandover | [OBS-20260805-001808](../observations/OBS-20260805-001808-decision-context-handover.md) |
| 個別Enablementの反復 | [OBS-20260805-001810](../observations/OBS-20260805-001810-repeated-enablement-dependency-signal.md) |
| 下流へのCost Transfer | [OBS-20260804-195508](../observations/OBS-20260804-195508-ai-proposal-generation-shifted-review-burden.md)、[Practice Value](../hypothesis-episodes/HYP-20260804-183210-ai-slop-downstream-burden-value.md)、[Admission Control Feature](../hypothesis-episodes/HYP-20260731-193520-lean-startup-as-admission-control.md) |
| Discovery結果の未定義 | [OBS-20260804-013221](../observations/OBS-20260804-013221-discovery-practice-gap.md) |
| Outcome-first AI配置 | [Practice Solution](../hypothesis-episodes/HYP-20260804-013223-outcome-first-ai-resource-allocation.md) |
| DVSとOVSの接続 | [OBS-20260801-004820](../observations/OBS-20260801-004820-coupled-platform-value-streams.md)、[Practice Solution](../hypothesis-episodes/HYP-20260801-004822-coupled-observability-detects-cost-transfer.md) |
| DVS学習とOVS品質の継続性 | [Practice Solution](../hypothesis-episodes/HYP-20260807-232639-dvs-learning-sustains-ovs-quality.md)、[OBS-20260808-204750](../observations/OBS-20260808-204750-dvs-system-learning-decision-sufficiency.md)、[OBS-20260808-204751](../observations/OBS-20260808-204751-reachable-value-stream-impact-guardrails.md) |
| 一回の成功候補 | [Raw Note](../../01_working/raw-notes/RN-20260808-213258-one-shot-success-without-organizational-dvs-learning.md)、[旧統合HYP](../hypothesis-episodes/HYP-20260807-232639-dvs-learning-sustains-ovs-quality.md)、[個人代行HYP](../hypothesis-episodes/HYP-20260809-013741-individual-learning-substitution-one-shot-success.md) |
| 個人代行とData Contract | [OBS-20260808-222203](../observations/OBS-20260808-222203-individual-substitution-and-value-data-contract.md)、[個人代行HYP](../hypothesis-episodes/HYP-20260809-013741-individual-learning-substitution-one-shot-success.md)、[Traceability HYP](../hypothesis-episodes/HYP-20260809-013742-value-traceability-enables-dvs-learning.md) |
| Scratch開発とBusiness Use Case | [OBS-20260808-224827](../observations/OBS-20260808-224827-business-use-case-loss-in-scratch-development.md)、[External Input](../../10_external-inputs/articles/EXT-20260808-224826-ddd-legacy-modernization-workshop-article.md)、[Traceability HYP](../hypothesis-episodes/HYP-20260809-013742-value-traceability-enables-dvs-learning.md) |
| Service Contract | [OBS-20260801-004821](../observations/OBS-20260801-004821-contract-accountability-cost-transfer.md)、[Practice Solution](../hypothesis-episodes/HYP-20260801-004823-service-contract-reduces-downstream-cost.md) |
| Solution-first再構成 | [OBS-20260802-230422](../observations/OBS-20260802-230422-solution-first-hypothesis-reconstruction.md)、[Practice Solution](../hypothesis-episodes/HYP-20260802-230423-solution-first-reconstruction-testability.md) |
| Training記録 | [OBS-20260804-004530](../observations/OBS-20260804-004530-solution-first-training-behavior.md) |
| Solution-first確認Prompt | [OBS-20260807-211648](../observations/OBS-20260807-211648-structural-coverage-empirical-checks.md) |
| 不確実性分解と判断更新 | [OBS-20260804-004531](../observations/OBS-20260804-004531-hypothesis-validation-uncertainty-decision.md) |
| 前回登壇のJourney | [OBS-20260804-004532](../observations/OBS-20260804-004532-journey-before-vsm-mbpm.md) |
| Platform Advisorの隠れた前提 | [OBS-20260802-230424](../observations/OBS-20260802-230424-platform-choice-hidden-assumption.md)、[Practice Value](../hypothesis-episodes/HYP-20260802-230425-platform-choice-burden-value.md)、[Practice Solution](../hypothesis-episodes/HYP-20260807-223145-standard-path-exception-routing.md) |
| Platform Advisor Scenario | [OBS-20260807-211650](../observations/OBS-20260807-211650-vsm-problem-causal-ambiguity.md)、[OBS-20260807-223144](../observations/OBS-20260807-223144-iterative-problem-understanding.md)、[Value](../hypothesis-episodes/HYP-20260807-211651-platform-selection-preparation-value.md)、[Solution](../hypothesis-episodes/HYP-20260807-211652-contextual-platform-advisor-solution.md)、[Feature](../hypothesis-episodes/HYP-20260807-211653-platform-advisor-chat-feature.md) |
| 効果測定の層 | [OBS-20260807-211649](../observations/OBS-20260807-211649-effect-measurement-layers.md) |
| Project・Transformation失敗率 | [OBS-20260802-230426](../observations/OBS-20260802-230426-failure-rate-definition-mismatch.md) |
| Process FlowとOutcome Quality | [OBS-20260802-230427](../observations/OBS-20260802-230427-process-flow-and-outcome-quality.md) |
| 必要な摩擦 | [OBS-20260804-013222](../observations/OBS-20260804-013222-necessary-friction-boundary.md) |
| 二段階Metric分析 | [OBS-20260804-013225](../observations/OBS-20260804-013225-itsm-metrics-analysis-practice.md)、[Practice Solution](../hypothesis-episodes/HYP-20260804-013226-two-stage-metrics-analysis.md) |
| BCG 10–20–70 | [OBS-20260730-210822](../observations/OBS-20260730-210822-bcg-10-20-70-claim-variation.md) |
