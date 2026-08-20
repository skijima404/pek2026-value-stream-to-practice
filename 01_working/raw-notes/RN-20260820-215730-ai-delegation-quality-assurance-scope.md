---
id: RN-20260820-215730-ai-delegation-quality-assurance-scope
type: raw_note
title: "AI AgentをDelegationとして捉える品質保証範囲の拡張"
content_language: ja
created_at: 2026-08-20T21:57:30+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-20T22:08:05+09:00
sanitization_checked_by: agent:codex
tags: [ai, delegation, automation, quality-assurance, evaluator, human-in-the-loop, workflow, loop, graph, itsm, ai-slop, maturity-model]
---

# メモ

## このメモの位置づけ

AI Automationの成熟Modelについて行った対話から、既存Repositoryにまだ明示的に
記録されていない可能性がある整理を抽出したもの。

既存の`RN-20260805-094034-ai-building-block-automation-maturity`には、Manual Operation、
Task Automation、Workflow、Loop、Graphという段階的Automation、Human in the Loopを
Evaluator発見の観測点として扱う考え、および完成形ではなく成熟過程を真似る必要性が
記録されている。

このメモでは成熟段階そのものを繰り返さず、次の更新された理解を記録する。

1. 上位概念をAutomationではなくDelegationとして捉える
2. 成熟の梯子を、実装順序ではなくDelegation範囲と品質保証範囲の拡張として捉える
3. LLMは、従来なら実装不能によって露呈した仕事の設計不足を隠せる可能性がある

以下は対話時点の設計解釈であり、確立済みFramework、検証済み因果関係または
ITSMの公式定義ではない。

## AutomationではなくDelegationを上位概念にする

AI Agentを新しいAutomationとしてだけ扱うと、Agent、Loop、Graphなどがすべて
新しい設計問題に見えやすい。一方、「別の実行主体へ仕事を渡すDelegation」として
考えると、人間同士の業務移管、従来のAutomation、AI Agentを同じ問いで扱える。

```text
仕事
  ↓
Delegation
  ├─ Human → Human
  │    Expert → Operatorなど
  │
  ├─ Human → Deterministic System
  │    従来のAutomation
  │
  └─ Human → Non-deterministic System
       AI / Agent
```

共通する中心質問は次のように置ける。

> この仕事を、この実行主体へ、どの条件なら安全に渡せるか。

委譲先が人間であっても従来SystemであってもAIであっても、仕事を渡すためには
少なくとも次を扱う必要がある。

- Inputと期待するOutput
- 手順または実行可能な仕事の構造
- 判断条件と完了条件
- 例外と失敗条件
- EscalationとHuman Fallback
- 次のActorへ渡す条件
- 実行結果の観測と改善

したがって、AutomationはDelegationの一つの形として捉えられる。AI固有の新規性を
考える前に、Delegationとして既知の問題と、AI固有の差分を分ける。

## AI固有の差分としての非決定性

従来の決定論的AutomationとAI Agentの差分候補として、同じInputに対してOutputが
常に同一とは限らない非決定性がある。

この差分により、従来のDelegation設計へ次の要素を追加する必要がある。

```text
従来のDelegation設計
  +
非決定性への対応
  ├─ Evaluator
  ├─ Quality Threshold
  ├─ Retry条件
  ├─ 停止・収束条件
  └─ Human Fallback
```

「AIは従来とすべて同じ」でも「AIではすべてを新しく考える」でもなく、
Delegationとして共通する設計問題と、非決定性によって追加される設計問題を
分離する。

## 成熟の梯子は品質保証範囲の拡張である

既存の成熟順序を、必ず順番に実装しなければならない工程表としてではなく、
Delegationする範囲と、その範囲について保証しなければならない品質の拡張として
読み替える。

| 段階 | Delegationする範囲 | 保証しなければならない主な対象 |
| --- | --- | --- |
| Manual Operation | 人間が仕事全体を実行する | 手順、判断、完了条件 |
| Task Automation | 単一Taskを委譲する | Input、Output、失敗条件 |
| Workflow | 複数Taskとその接続を委譲する | 順序、状態遷移、Handover |
| Loop | 評価と再試行を含めて委譲する | Evaluator、Retry、停止、収束条件 |
| Graph | 分岐、並列、複数経路を委譲する | Node間Contract、依存関係、Context伝播 |

この見方では、LoopやGraphを技術的に構築できることは、その段階へ進んでよい
十分条件ではない。委譲範囲全体について品質を定義し、検証できることが必要になる。

> Delegationの範囲を広げるほど、その範囲について品質を保証できなければならない。

> Loopを作れるからLoopにするのではない。Loop全体の品質を担保できるようになった
> からLoopへ進める。

## 梯子は飛ばせても品質保証は飛ばせない

Manual Operationから必ず時間をかけて一段ずつ進むことを絶対則にはしない。
業務設計、モデリングおよびAI EngineeringのCapabilityによって、後段で必要になる
構造と検査方法を事前に用意できる場合がある。

モデリングでは、暗黙の仕事を次のような要素へ外在化する。

- StateとTransition
- InputとOutput
- Decision
- Exception
- Dependency
- Contract
- Success ConditionとFailure Condition

さらに、飛ばした先の段階で何を品質とするかを定義し、それをRule、Test、Evaluator、
Human Reviewまたは実運用Metricによって検証できれば、実装Phaseを短縮できる可能性が
ある。

```text
標準Route
Manual → Task → Workflow → Loop → Graph
実際に回しながら、必要な知識、失敗条件、評価方法を発見する

Expert Shortcut
業務設計 + モデリング + AI Engineering
飛ばす段階で得るはずの知識と品質保証方法を先に構築する
```

ただし、Shortcutは各段階で必要なKnowledgeを不要にするものではない。

> SkipできるのはPhaseであって、Knowledgeではない。

> 梯子はスキップできる。品質保証はスキップできない。

業務設計、モデリング、AI EngineeringのCapabilityが同じTeamに揃うとは限らない。
したがってExpert Shortcutを一般的な標準Routeとして勧めず、段階的な学習をDefaultに
置く方が安全である、という判断も対話中に置かれた。

## LLMが消した「設計不足を早期に発見する摩擦」

従来のAutomationでは、曖昧な仕事、未定義の状態遷移、欠けた完了条件は、実装できない
ことによって早期に露呈しやすかった。

```text
従来のAutomation

曖昧な仕事
  ↓
実装できない、接続できない
  ↓
仕事の設計不足が入口で露呈する
```

LLMは、曖昧な依頼からももっともらしいOutputを生成できる。そのため、従来は実装不能に
よって機能していた設計上の関門を通らなくても、動いたように見える場合がある。

```text
LLMを含むSolution

曖昧な仕事
  ↓
もっともらしいOutputが返る
  ↓
動いたように見える
  ↓
未解決の前提、判断、例外、検証責任が後続へ渡る
  ↓
設計不足が下流負荷またはAI Slopとして露呈する
```

この整理から、AI Slopの原因候補をModelの精度不足だけに限定せず、次のようにも
捉えられる。

> AIが未設計の仕事までそれらしく実行できるため、本来入口にあった設計上の
> Quality Gateを通過し、設計不足が下流へ移る。

これは現時点では因果を検証した結論ではなく、AI-enabled Solutionを設計する際に
調べるべき仮説である。

## ITSMとの接続候補

対話では、ExpertからOperatorへの運用移管において蓄積された次の考え方を、AIへの
Delegationにも再利用できる可能性があると整理した。

- RunbookとOperating Procedure
- Entry CriteriaとExit Criteria
- 判断条件と例外条件
- Escalation
- Control PointとQuality Gate
- 監視、Metricおよび継続改善

AI Agentを作る議論はAgent、Tool Use、Loop、Graphなど開発側の語彙で進みやすい。
一方、実際に仕事を任せる段階では、例外、停止、移管、運用、責任境界など、運用側が
扱ってきた問いが前面に出る。

ただし、ITSMまたはITILがこのDelegation成熟Modelを公式に定義しているとは、この
メモでは確認していない。既存のITSM原則からAI時代のDelegation問題を解釈した
接続候補として扱う。

## 既存Repositoryとの関係

このメモは、次の既存整理を置き換えない。

- `RN-20260805-094034-ai-building-block-automation-maturity`
  - Building Block、Human in the Loop、Evaluator、Workflow、Loop、Graphの成熟順序
- `HYP-20260812-010725-progressive-automation-contracts`
  - Building Blockを個別検証し、安定した範囲を段階的に接続するFeature Hypothesis
- `OBS-20260812-010722-ai-output-closure-boundary`
  - AI Outputの下流負荷を、媒体より委譲範囲、検証可能性、ClosureおよびHand-offで
    捉えたObservation

今回の追加点は、次のように整理できる。

```text
既存整理
Automationを段階的に育てる
  ↓
今回の追加
段階的に拡張しているものはDelegation範囲と品質保証範囲である
  ↓
留保
必要なKnowledgeと品質保証方法を先取りできるならPhaseは短縮できる
```

## 登壇への適用可能性

本編へ入れる場合、詳細な成熟Modelをすべて説明するより、次の因果へ限定する案がある。

```text
LLMは曖昧な仕事でもOutputを返せる
  ↓
仕事の設計不足が入口で止まらない
  ↓
未解決の検証責任が下流へ移る
  ↓
AI Slopとして体験される
  ↓
AIへのDelegation範囲に応じて品質保証範囲を設計する
```

Automation成熟Model、Expert ShortcutおよびITSMとの技術史的な接続は、25分の
本編には詳細すぎる可能性があり、Appendix、BlogまたはRepositoryを訪れた人向けの
補足候補とする。

## 限界と未確認事項

- Delegationを上位概念とする整理は、対話で形成した設計解釈であり、既存Frameworkとの
  対応を検証していない。
- Manual、Task、Workflow、Loop、Graphの段階を、品質保証範囲として比較した実験は
  行っていない。
- Expert Shortcutに必要なCapability、その再現可能性および失敗条件を確認していない。
- LLMが設計不足の早期検知を弱め、下流負荷を増やすという因果は検証していない。
- ITSM、従来Automation、AI Agentは完全に同型ではない。法的責任、学習、権限、
  可逆性、実行速度および失敗規模などの差を別途扱う必要がある。
- 世代構成または特定世代の不在を知識継承断絶の原因とする仮説は、根拠を確認して
  いないため記録対象から外した。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
