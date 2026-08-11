---
id: HYP-20260811-131148-consumer-governed-ai-capability
type: hypothesis_episode
title: "消費側Value StreamのConcernからAI Capabilityの利用条件を決めると局所最適を避けやすい"
content_language: ja
created_at: 2026-08-11T13:11:48+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-11T22:12:34+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - external_research
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260811-131147-consumer-concerns-govern-ai-capability
  - type: derived_from
    target: OBS-20260811-140549-ai-subsystem-team-terminology-fit
  - type: derived_from
    target: OBS-20260811-220557-ai-resource-software-component-decomposition
  - type: tests
    target: HYP-20260804-183210-ai-slop-downstream-burden-value
  - type: supersedes
    target: HYP-20260804-013223-outcome-first-ai-resource-allocation
---

# 仮説

AIを特別な導入対象としてCapabilityまたはToolから検討する代わりに、通常のApplication
Engineeringと同様に、消費側Value StreamがBusiness Outcome、業務後に満たすべきConcern、
受入条件およびAccountabilityを先に定義し、提供側AI Capabilityがその条件を満たす形で
実現可能性、制約およびGuardrailを提示すれば、提供側の局所指標または内部都合から設計する
場合より、AIの利用、限定、代替、保留または棄却をValue Stream全体へ適合させやすい。

AI CapabilityをComplicated Subsystem teamまたは社内Platform teamが提供する場合でも、
外部Serviceまたは通常の開発Toolとして利用する場合でも、消費側のOutcomeと受入条件を
提供側の論理で上書きしない。必要なConcernを満たす実現案の中で、Speed、CostおよびFlowを
最適化する。

AIをWorkload上のResourceとして扱う場合でも、その実体を一つの箱として特別扱いせず、
Feature、Model、Inference、Evaluation、GuardrailなどのSoftware Componentと責任へ分解する。
高度な専門性を持つComponentをComplicated Subsystem、その所有TeamをComplicated Subsystem
teamとして区別し、各Componentを通常のSoftware Engineeringに必要なOwnership、Boundary、
Version、TestまたはEvaluation、変更、Release、運用、観測および障害時責任の対象とする。

## 知識の成立根拠

`OBS-20260811-131147-consumer-concerns-govern-ai-capability`に整理された、AIも通常の
Application開発として扱う立場、Concernを受入条件として先に満たす順序、および提供Topologyに
かかわらず消費側Value StreamのOutcomeを上位に置く境界原則から形成した。

この根拠は、実践者の`recorded_statement`、Team Topologies公式ページを確認した
`external_research`、およびAgentによる`reasoned_synthesis`である。
`OBS-20260811-140549-ai-subsystem-team-terminology-fit`によって、正式なTopologyが
Complicated SubsystemそのものではなくComplicated Subsystem teamであること、Stream-aligned
teamがOutcomeを所有すること、Team間にX-as-a-Serviceの提供・利用関係があることを確認した。

`OBS-20260811-220557-ai-resource-software-component-decomposition`には、AIをWorkload上の
Resourceとして利用するViewと、その実体をSoftware Systemとして構成・所有するViewを分け、
AI全体ではなく責任単位のSoftware Componentへ分解する整理が記録されている。この分解を
Organization Readinessではなく、通常のSoftware Engineeringの責任を適用するための設計境界と
して扱う。

ただし、公式ページはAI Capabilityの分類や今回の責任境界を明示していない。公式用語との
整合を確認しただけであり、Capability Contractの適用、実際の判断変更またはOutcome観測を
行っていないため、現時点ではHypothesisの検証Evidenceとして扱わない。

`HYP-20260804-013223-outcome-first-ai-resource-allocation`は、この候補に至る前の学習Episode
として残す。このEpisodeは今後検証するPractice Solutionの中心表現と比較対象を置き換えるが、
旧EpisodeのU1、U2およびU4のFinding、Evidenceまたは結果を、このEpisodeへ自動的に転用しない。

## Mobiusでの位置づけ

`solution`

親となるPractice Value Hypothesis
`HYP-20260804-183210-ai-slop-downstream-burden-value`に対し、回避可能な下流負荷を生まない
AI Capabilityの選定と責任境界を、消費側Value Streamが定義するConcernと受入条件から
設計するSolutionとして具体化する。

## 置換関係

- decided_at: 2026-08-11T13:57:54+09:00
- decided_by: human:kijima
- supersedes:
  `HYP-20260804-013223-outcome-first-ai-resource-allocation`
- scope:
  今後検証するPractice Solution Hypothesisの中心表現と比較対象
- reason:
  Speedと品質を無条件に競合させず、業務後のConcernを受入条件として先に満たし、その条件を
  満たす実現案の中でSpeed、CostおよびFlowを最適化する。また、AIの提供Topologyではなく、
  消費側Value StreamのOutcomeとConcernが利用条件を規定する境界を検証対象とする
- evidence_boundary:
  置換はEvidence継承を意味しない。このEpisodeは`result: not_tested`、全Componentを
  `not_checked`のまま維持する。旧Episodeを親とするFeature Hypothesisの`tests`関係も
  過去の検証履歴として付け替えない

## 期待する兆候

- AI ToolまたはUse Caseを選ぶ前に、消費側Actor、Business Outcome、業務後のConcern、
  受入条件、Error CostおよびAccountabilityが記録される
- 提供側は生成速度またはModel指標だけでなく、Capabilityの限界、必要Context、技術的Risk、
  Guardrailおよび実現Costを提示する
- Capability Contractによって、AIの利用範囲、人間の判断、決定的Automation、非AIの
  代替案、保留または棄却が比較される
- Complicated Subsystem team、Platform teamまたは外部Serviceへ提供主体または提供形態が
  変わっても、消費側のOutcome、受入条件および最終利用判断が維持される
- AIが一つのResource名だけで記録されず、利用者向けFeature、Model、Inference、Evaluation、
  GuardrailなどのSoftware ComponentとOwnerへ、判断に必要な粒度で分解される
- AIを構成するSoftware Componentに、通常のSoftware Engineeringと同様のVersion、Testまたは
  Evaluation、変更、Release、運用、観測および障害時責任が置かれる
- 必要なConcernを満たす実現案同士で、AIによるEnd-to-EndのLead Time、手戻り、待ち、
  Error Cost、下流負荷または総Costの改善を確認できる

## 反証またはChallengeとなる兆候

- 消費側が提供側の専門知識なしにConcernまたは受入条件を定義できず、境界を分けることで
  判断品質が下がる
- 提供側の技術的制約によってBusiness Outcomeまたは業務Processの再定義が必要となり、
  消費側の条件を常に上位に置けない
- Capability Contractを置いても、AIの利用、限定、代替、保留、棄却またはGuardrailが
  変わらない
- 同じConcernを満たす非AI案と比較して、AIがEnd-to-EndのFlowまたはCostを改善しない
- 小規模またはCommodity化されたTool利用では、境界とContractを明示するCostが得られる
  便益を上回る
- Software Componentへ分解してもOwnership、Test、変更または障害時判断が明確にならず、
  AIを一つの外部Resourceとして扱う場合より判断Costだけが増える

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | 消費側Value Streamが、AIの提供Topologyを決める前に、Business Outcome、業務後のConcern、受入条件、Error CostおよびAccountabilityを実務で判断可能な粒度に定義できる | critical | none | not_checked | unknown | unknown | 定義に必要なActor、入力、粒度、時間、Decision Ownerおよび提供側の関与範囲を確認していない |
| U2 | 消費側のConcernと受入条件から始めると、提供側のCapabilityまたは局所指標から始める場合とは異なるAI利用範囲、責任境界、Guardrail、代替、保留または棄却判断を選べる | critical | none | not_checked | unknown | unknown | 同一Caseで二つの開始方法を比較しておらず、旧EpisodeのFindingを転用していない |
| U3 | 同じConcernと受入条件を満たす実現案の中でAIを利用すると、非AI案または他のCapability配置より、手戻り、待ち、Error Costおよび下流負荷を含むEnd-to-EndのFlowまたは総Costを改善できる | critical | none | not_checked | unknown | unknown | 比較可能なCase、単位、対象期間、Baseline、発生頻度、対象Resourceおよび実Outcomeを確認していない |
| U4 | AI CapabilityをComplicated Subsystem teamまたはPlatform teamが提供する場合でも、外部Serviceまたは通常の開発Toolとして利用する場合でも、消費側のOutcome、受入条件および最終利用判断を維持できる | high | none | not_checked | unknown | unknown | Team Topologies公式ページによる用語とInteraction Modeは確認したが、AI Capabilityの分類、複数の提供主体・提供形態のCase、Capability Contractおよび例外時のDecision Ownerは確認していない |
| U5 | Concern、受入条件、Capability Contractおよび責任境界を整理・維持するCostは、対象の規模、可逆性およびRiskに対して比例的である | high | none | not_checked | unknown | unknown | 小規模Tool利用と高Riskな内部Subsystemを比較しておらず、作成・Review・更新Costおよび回避効果を確認していない |
| U6 | AIをWorkload上のResourceとして扱う場合でも、その実体をFeature、Model、Inference、Evaluation、GuardrailなどのSoftware Componentと責任へ分解し、高度な専門部分をComplicated Subsystem、その所有者をComplicated Subsystem teamとして区別して、通常のSoftware Engineeringに必要なOwnership、Boundary、Version、TestまたはEvaluation、変更、Release、運用、観測および障害時責任を置ける | high | none | not_checked | unknown | unknown | 分解に必要な粒度、AI固有Evaluationと通常Testの境界、内部Componentを直接管理できない外部Serviceへの責任の写像、および分解による判断・運用効果を確認していない |

## 検証方法

### 方法と対象範囲

- 方法:
  - 一つのBoundedなAI利用候補について、消費側Actorと提供側Actorを分け、Business Outcome、
    業務後のConcern、受入条件、Error Cost、Accountabilityおよび提供側制約を記録する
  - 提供側Capabilityまたは局所指標から始めた案と、消費側のConcernと受入条件から始めた案を
    同じCaseで比較し、利用範囲、責任境界、Guardrail、代替、保留または棄却が変わるか確認する
  - 条件を満たす実現案について、局所的な生成時間だけでなく、Lead Time、Review、手戻り、
    待ち、Error Cost、下流負荷、対象Resource、発生頻度および分析Costを同じ期間で比較する
  - 専門性の高い内部AI Capabilityと、Commodity化されたAI Coding Toolなどの外部Serviceを
    一つずつ選び、Workload上のResource配置とSoftware System上のComponent・Ownerを分けて
    記録する。提供主体または提供形態が変わっても、通常のSoftware Engineeringに必要な責任と
    消費側のOutcome、受入条件および最終利用判断を維持できるか確認する
- 対象・資料:
  未選定。実際の利用判断、受入条件、作業記録および利用後Outcomeを追跡できるCaseを優先する
- 選定方法:
  消費側と提供側のActorを区別でき、AIを使わない選択肢を含めて比較できる小さなCaseから
  始める。高Risk Caseへ一般化する前に、可逆なCaseでContract作成Costも記録する
- 実施規模:
  最初は二つの異なる提供主体または提供形態を持つ少数Caseとし、一般化より境界と反証条件の
  具体化を優先する

### GenAIの利用

- 利用内容:
  Concern、受入条件、Capability、Boundary、Guardrail、比較案および観測項目の構造化
- GenAIだけで実施しないこと:
  Business Outcome、受入条件、Residual Risk受入、AIの採用または棄却の最終判断
- 実際に確認した資料・記録:
  `OBS-20260811-131147-consumer-concerns-govern-ai-capability`、
  `OBS-20260811-140549-ai-subsystem-team-terminology-fit`、
  `OBS-20260811-220557-ai-resource-software-component-decomposition`、および各Sourceを確認した。
  Team Topologies公式ページは用語とInteraction Modeの参照に限り、Case、Capability Contract
  または実装結果は確認していない

## 結果

`not_tested`

### 実際に観測したこと

後継Hypothesisを形成する対話と、AIをWorkload上のResourceおよびSoftware Systemの二つのViewで
扱う整理は記録したが、Case選定、Software Component分解、Capability Contract作成、比較判断、
実装または利用後Outcomeの観測は行っていない。

## 解釈

このEpisodeは、AIを利用するかというTool選定を先に置かず、通常のApplication Engineeringと
同じく、消費側Value StreamのOutcomeとConcernから必要条件を定義するというSolution候補を
扱う。Speedを軽視するのではなく、必要なConcernを満たす実現案の中で最適化する。

提供側AI Capabilityは専門知識と内部実装を所有し、技術的制約を示す。しかし、その専門性
だけを根拠に消費側のBusiness Outcomeまたは成功条件を定義しない。境界で条件が衝突する
場合は、暗黙に上書きせず、代替案、Scope変更、保留、棄却またはResidual Risk受入を明示的に
判断する必要がある。

AIをResourceとして配置する判断は、その実体となるSoftware Systemの設計責任を消さない。
利用者向けFeatureと、高度な数学、推論または評価を担うComponentを分け、Software Componentと
所有Teamを区別することで、AIを特別な例外ではなく、通常のArchitecture、Test、変更、運用、
観測および障害対応の対象として扱う。この分解はOrganization Readinessの評価ではなく、
消費側と提供側の責任境界を実装可能な粒度へ下ろすために行う。

## 限界

- Team Topologies公式ページでComplicated Subsystem team、Stream-aligned teamのOutcome所有、
  およびInteraction Modeを確認したが、AI CapabilityをどのTeam Typeで提供すべきかは
  同ページから決まらない。
- 提供側の論理が消費側Value StreamのOutcomeを上書きしないという境界原則は、公式ページに
  明記されたRuleではなく、公式のTeam Type、Outcome所有およびInteraction Modeと、実践者の
  立場を接続した推論である。
- 今回の会話は、実践者の立場とAgentによる構造化であり、独立した検証ではない。
- 消費側と提供側の境界は、同一組織内、外部Vendor利用、組込み機能または個人Tool利用で
  異なる可能性がある。
- Business Outcomeと技術的実現可能性が相互に更新される場合に、どちらを上位と呼ぶかは
  単純化できない可能性がある。
- Capability ContractのSchema、Decision Owner、例外、Residual Risk受入、更新Triggerおよび
  廃止条件を定義していない。
- AI Software Systemをどの粒度でComponentへ分解するか、通常のTestとAI固有Evaluationをどう
  分けるか、外部Serviceの内部Componentを管理できない場合に責任をContractへどう写像するかを
  定義していない。
- Software Component分解が、実際のOwnership、変更判断、品質、Flowまたは障害対応を改善するか
  確認していない。
- Knowledge Curation、Interaction成熟度または組織全体のAI Readinessは、このEpisodeの
  検証対象に含めない。
- Commodity化、Application規模、可逆性またはRiskに応じた最小限のGovernanceを
  定義していない。
- 旧Solution Hypothesisを置き換えたが、旧EpisodeのEvidence、Findingまたは結果を継承せず、
  このEpisodeの検証を別に行う必要がある。
- このHypothesisは登壇内容、組織標準、Team設計、AI ToolまたはArtifactとして採用されて
  いない。

## 公開安全性確認

- checked_at: 2026-08-11T22:12:34+09:00
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
