# Evidence Coverageと残存リスク

[分析Indexへ戻る](../README.md)

このファイルは、既存NodeとArtifactを横断して探すための再生成可能な
Navigation Viewです。Evidence、派生Claim、採用判断、現在の正本ではありません。
内容がリンク先と矛盾する場合は、リンク先を優先してこのViewを再生成します。

複数の不確実性を含むHypothesis Episodeは、`検証対象の分解`で`U1`、`U2`のような
小さな検証対象に分けます。

- `Coverage state`: どの範囲を確認したか
- `Finding`: 現在のEvidenceが何を示すか
- `Applicability`: Evidenceを対象条件へどの程度適用できるか
- `Residual uncertainty`: 確認後も残る不確実性

Coverageは仮説が正しい割合ではありません。検証対象で参照するEvidenceは原則として
Observationとし、経験知、外部Research、直接観察などの性質はObservation側の
`knowledge_basis`を確認します。

残存リスクへの人間の対応判断は`04_decisions/risk-decisions/`に分離します。
`proceed_with_risk`は限定した範囲で先へ進む判断であり、Hypothesisの`supports`、
Analysisの採用、Artifactへの採用を意味しません。

### 現在の検証状況

| Hypothesis Episode | Scope | Components | Coverage | Current Risk Decision |
| --- | --- | ---: | --- | --- |
| [AudienceがActionを持ち帰るSession Value](../hypothesis-episodes/HYP-20260804-183208-audience-actionable-ai-slop-value.md) | `session` | 5 | U1・U2は`partially_checked`、U3・U4・U5は`not_checked` | なし |
| [一続きの説明によるSession Solution](../hypothesis-episodes/HYP-20260804-183209-ai-slop-learning-path-solution.md) | `session` | 5 | すべて`not_checked` | なし |
| [一枚とRepositoryへの導線によるSession Feature](../hypothesis-episodes/HYP-20260805-001809-repository-handoff-preserves-focus.md) | `session` | 4 | すべて`not_checked` | なし |
| [下流負荷の制御を提供側の価値と利用者の受入条件として扱うPractice Value](../hypothesis-episodes/HYP-20260804-183210-ai-slop-downstream-burden-value.md) | `practice` | 7 | U1・U2・U4・U5・U6は`partially_checked`、U3・U7は`checked_for_current_scope` | なし |
| [価値選択と検証のPractice Solution](../hypothesis-episodes/HYP-20260730-015718-ai-speed-requires-value-validation.md) | `practice` | 3 | U1は`partially_checked`、U2・U3は`not_checked` | なし |
| [Admission ControlによるPractice Feature](../hypothesis-episodes/HYP-20260731-193520-lean-startup-as-admission-control.md) | `practice` | 4 | すべて`not_checked` | なし |
| [Solution-first再構成のPractice Solution](../hypothesis-episodes/HYP-20260802-230423-solution-first-reconstruction-testability.md) | `practice` | 4 | すべて`not_checked` | なし |
| [DVS学習継続性のPractice Solution](../hypothesis-episodes/HYP-20260807-232639-dvs-learning-sustains-ovs-quality.md) | `practice` | 4 | U1〜U4は`partially_checked` | なし |
| [個人代行または好条件による一回の成功](../hypothesis-episodes/HYP-20260809-013741-individual-learning-substitution-one-shot-success.md) | `practice` | 3 | U1は`partially_checked`、U2・U3は`not_checked` | なし |
| [Valueから利用・OutcomeまでのTraceability](../hypothesis-episodes/HYP-20260809-013742-value-traceability-enables-dvs-learning.md) | `practice` | 4 | U1〜U3は`partially_checked`、U4は`not_checked` | なし |
| [選定へ関与する利用者のPractice Value](../hypothesis-episodes/HYP-20260807-211651-platform-selection-preparation-value.md) | `practice` | 4 | すべて`not_checked` | なし |
| [Contextual Platform AdvisorのPractice Solution](../hypothesis-episodes/HYP-20260807-211652-contextual-platform-advisor-solution.md) | `practice` | 4 | すべて`not_checked` | なし |
| [標準Pathと例外RoutingのPractice Solution](../hypothesis-episodes/HYP-20260807-223145-standard-path-exception-routing.md) | `practice` | 4 | すべて`not_checked` | なし |
| [選定作業をChatへ統合するPractice Feature](../hypothesis-episodes/HYP-20260807-211653-platform-advisor-chat-feature.md) | `practice` | 4 | すべて`not_checked` | なし |

上表以外のHypothesis Episodeには、現在Validation Component表がありません。Risk Decision
Nodeはまだ作成されていません。これはRiskが存在しないことではなく、人間による
対応判断がまだ記録されていないことを示します。

## 未解決事項

- AudienceがAI Slopを制御するActionを持ち帰るSession Valueは、3人への
  ヒアリングによりU1・U2が`partially_checked / supports / contextual`になりました。
  別の一人へのAI PoC InterviewもU1を`contextual`に支持します。対象者の選定方法、
  Audience全体への適用、課題の頻度・優先順位、Risk特定、Action選択および実際の
  試行は未確認で、Episode全体は`inconclusive`です。
- 構造、Signal、仮説検証を一続きに説明するSession Solutionが、Audienceの
  理解とAction選択を改善するかは`not_tested`です。
- AI高速化による下流負荷を特定・制御・削減できる状態のPractice Valueは、
  Consulting提案書の一件によりU1・U2・U4が`partially_checked`、U3・U7が
  `checked_for_current_scope`になりました。Workslop受け手負荷の外部Researchにより、
  U6も`partially_checked`です。実践者の条件整理によりU5も`partially_checked`となり、
  U6にはOutputの検知可能性、可逆性、回復Costおよび反復量の境界を追加しました。
  実際のPlatform TeamによるCapacity配分、採用率との関係、Platform利用者の行動および
  Platform Serviceへの直接適用は未確認です。
- 価値選択と検証によって回避可能な下流Costが減るというPractice Solutionは、
  機能評価型AI PoCの一事例によりU1が`partially_checked / inconclusive / contextual`です。
  Value Hypothesisを明示した比較、原因、判断品質および下流Costを確認しておらず、
  U2・U3は`not_checked`です。
- DVSの仮説検証と学習品質をOVS品質の継続性に対する必要条件とするPractice Solutionは、
  限定的なExpert Reviewにより、U1とU2が`partially_checked / supports / contextual`、U3が
  `partially_checked / inconclusive / analogous`、U4が
  `partially_checked / inconclusive / contextual`です。U1の支持はOperational Definitionの
  構成可能性、U2の支持は個人によるCapability代行のMechanismだけに限定されます。
  ValueからData Contract、利用Levelおよび社会実装への接続をU3へ追加しましたが、
  U3のFindingは変更していません。Scratch開発についても、Business Use CaseからActorの
  判断、帳票・画面、Dataおよび実装へのTraceabilityを追加しました。同一Platform Serviceの
  複数Cycle、個人代行とOutcomeの因果、他の非公式な学習経路、Business Use Caseの有無と
  利用・Outcomeの差、成功条件の再利用、反例および一次記録は未確認で、Episode全体は
  `inconclusive`です。意味変更後の人間の意図Reviewは完了しています。
- 個人代行または好条件による一回の成功を扱う新規Practice Solutionは`proposed`です。
  個人代行Mechanismは`partially_checked / supports / contextual`ですが、一次記録を持つ
  Bounded Case、組織的Capabilityの不在、因果、成功条件の継承および複数Cycleは未確認です。
- Valueから意思決定・Data・利用・OutcomeへのTraceabilityを扱う新規Practice Solutionは
  `proposed`です。Package型とScratch型のMechanismは区別して記録しましたが、Traceabilityの
  有無による判断更新、追加作業、利用またはOutcomeの差は未確認です。
- Value Hypothesis、期待Signal、停止条件および判断OwnerをAdmission Controlとして
  運用するPractice Featureは、4 Componentsがすべて`not_checked`です。Featureへの
  意味変更後の人間の意図Reviewは完了していますが、検証と採用判断は未実施です。
- PEのDVSと利用者側OVSを接続した観測が、局所指標より早くCost Transferを検知
  できるかは `not_tested` です。
- 共有前のService Contract明確化が、受け手の理解、検証、判断Costを減らすかは
  `not_tested` です。
- Solution-firstからの再構成は、構造品質、参加状態とFacilitator負荷、VSM・MBPMに
  よる欠落回収、および後続の検証責任という4 Componentsがすべて`not_checked`です。
  人間の意図Reviewは完了していますが、手法の効果検証と採用判断は別です。
- Solution-first再構成の有無が異なるTraining記録は、条件が揃っておらず、手法の
  効果検証には使えません。
- 仮説検証を不確実性の分解として説明することが、参加者の理解や意思決定を
  改善するかは未確認です。
- 外れ方の観測からProblem・Value理解と継続判断へ戻る学習Loopは、実務上の説明と
  Reasoned Synthesisであり、判断品質、廃棄時点またはOutcomeの比較は未実施です。
- Journey特定後にVSM・MBPMへ展開する今回の順序が、課題抽出やPriority判断を
  改善するかは比較されていません。
- Customerへ目的とDiscovery結果を質問した経験はありますが、質問件数と一次記録を
  備えた調査ではなく、組織で未定義なのか担当者が理解していないのかは区別できません。
- Value Streamの課題とOutcomeからAI Capabilityを配置する方法が、AI Use Caseから
  始める方法より局所最適を避けやすいかは `not_tested` です。
- Slopとして経験される摩擦のうち、何を残すべきかを判定する方法と効果は
  未確認です。
- 異常検知と原因診断を分ける運用はITSMとProject Portfolioの経験に基づきますが、
  過去の一次資料は未確認で、Platform Engineeringでの実践は導入初期です。
- DashboardとDataからFactを取り出すために必要な分析Technique、習熟度、Training
  方法は未定義です。
- Platform利用者のどのSegmentが選択肢より標準Pathと選択負荷軽減を重視するかは
  `not_tested` です。
- 組織が責任を持つ標準Pathと例外Routingが、比較、説明、意思決定Riskおよび下流負荷を
  減らすかは、4 Componentsがすべて`not_checked`です。物語内のHypothesis Modelとして
  保持し、このRepositoryでは検証を予定していません。標準Path側のFeatureは未作成です。
- Platform選定へ関与し比較したい利用者SegmentのValue、Contextual Advisorという
  Solution、および選定作業を一つのChatへ統合するFeatureは、各4 Componentsが
  `not_checked`です。架空Scenario内の結果はEvidenceではなく、選択意向、権限、
  責任、代替Solution比較、下流Guardrailおよび運用Costを実在Episodeで確認していません。
  現在このRepositoryで検証する予定はなく、検証方法は将来別Scopeで検討する場合の
  再利用可能な設計として保持しています。
- Outcome、Experience、Trust、Contract Qualityの具体的なMetricと、MBPMへ
  組み込むScopeは未定義です。
- Session Featureであるリレー中心の25分トークは、Walkthrough、代替案比較、
  第三者Reviewが未実施です。Practice scopeのAdmission Control Featureも未検証です。
- Human-AI協業を一枚とRepositoryへの導線に限定するSession Featureは、Focus維持、
  Repositoryの役割理解、登壇後の閲覧およびAction選択の4 Componentsが未確認です。
- BetterUpのWorkslop調査は受け手の自己申告を扱いますが、Platform Engineeringへの
  適用、AI利用との因果および対策の効果は確認していません。
- 判断Contextを渡すHandoverと、個別Enablementの反復を人力補完のSignalとして扱う
  整理は、事例記憶またはReasoned Synthesisであり、比較Caseで検証されていません。
- 想定Audienceの課題候補は3人へ限定的に確認しましたが、参加者Journey、実際の
  参加者構成およびAudience全体の需要は確認していません。
- 現場適用、Live Document、Takeawayの有効性は未検証です。
