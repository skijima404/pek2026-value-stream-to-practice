---
id: RN-20260805-094034-ai-building-block-automation-maturity
type: raw_note
title: "AI Building BlockからLoop・Graphへ進む段階的自動化"
content_language: ja
created_at: 2026-08-05T09:40:34+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-05T09:45:54+09:00
sanitization_checked_by: agent:codex
tags: [ai-automation, ai-outcome, building-block, evaluator, graph, human-in-the-loop, loop, orchestration, progressive-automation]
---

# AI Building BlockからLoop・Graphへ進む段階的自動化

## このメモの位置づけ

AIによる生成Taskを組み合わせてSolutionを作る時にも、従来のAutomationと同じ
成熟順序が必要ではないか、という会話を記録する。

関連する既存Raw Noteは次の通り。

- `RN-20260730-140133-ai-outcomes-and-mbpm`
  - AIに期待する局所的なOutcomeを「速く作る」「広く探す」「分かるように解釈する」
    「選べるように整理する」「本当に筋が通るか疑う」に分けた
- `RN-20260804-204359-ai-low-downstream-burden-conditions`
  - 手動で手順を確立し、各部分を自動化してから接続する段階的自動化と、
    Contract Firstの考え方を記録した

このメモでは、二つの議論をつなぎ、AI Building BlockとAI-enabled Solutionを
分ける。また、Human in the Loop、Evaluator、Workflow、Loop、Graphを、
Automationの成熟順序として整理する。

以下は会話時点の設計解釈であり、確立済みのAI Solution成熟Modelや、特定製品の
能力を評価した結果ではない。会話中の割合表現も実測値ではなく、汎用部品だけでは
組織固有の正しさを充足できないことを示す例示である。

## 出発点：AIでも仕事の設計は省略できない

従来のAutomationでは、通常は次の順序で進める。

1. まず人間が手動で作業し、手順、判断、状態遷移、完了条件を確認する
2. 安定した部分を個別に自動化する
3. 個々の入出力と失敗条件を確認する
4. 部品間のContractを定義する
5. 最後に接続し、全体をOrchestrationする

Generative AIは、曖昧な目的からもっともらしいOutputを作れる。このため、手動で
仕事を理解し、安定させる段階を飛ばしても、End-to-Endの仕組みが動いているように
見えやすい。

しかしAIによって省略できるのは、各処理を完全な決定論的Logicとして記述する作業の
一部である。次の設計が不要になるわけではない。

- 必要なInput
- 期待するOutput
- 状態遷移
- 完了条件
- 失敗条件
- 次工程へ渡す条件
- どの条件で人間へ戻すか
- 再実行時に保持するContext
- 例外処理、監視、停止、Rollback

> AIは手順の記述を省略できるが、仕事の設計を省略できるわけではない。

むしろ非決定的な部品を含むため、Outputの充足度、状態の観測、再試行の収束条件を、
従来のAutomation以上に明示する必要があるかもしれない。

## AI Building BlockとAI-enabled Solutionを分ける

### AI Building Block

一回のInputに対し、一つのまとまった処理結果を返す最小単位として考える。

例：

- 文書を生成する
- 関連資料を探索する
- 標準の意味と適用条件を説明する
- 選択肢と判断軸を整理する
- Reasoning ChainをReviewする
- 情報を分類する
- 要件を抽出する
- Testを実行し、結果を判定する

一つのBuilding Blockが、既存の5つのAI Outcomeのどれか一つに完全分類できるとは
限らない。「ADRを探し、現在の設計にどう適用できるか説明する」Blockは、探索と
解釈の両方へ寄与する。

したがって5分類はMECEなTask分類ではなく、そのBuilding Blockがどの局所的Outcomeへ
主に貢献するかを考える観点として扱う。

### AI-enabled Solution

複数のBuilding Blockを、Data Source、状態遷移、Evaluator、Human Review、例外処理
などと組み合わせ、業務上のOutcomeを実現する仕組みとして考える。

コード変更Solutionの例：

```text
要求を解釈する
  ↓
関連CodeとADRを探す
  ↓
変更Optionを整理する
  ↓
Codeを生成する
  ↓
Testを実行する
  ↓
Reasoningと品質を検査する
  ↓
人間が承認する
```

このSolution全体は、5つのAI Outcomeのどれか一つではない。複数の局所的Outcomeを
組み合わせ、「安全に変更をDeliveryする」などの業務Outcomeを実現しようとする。

## Outcomeも二つのLevelに分ける

### Building Block Outcome

AIが人間の作業または認知へ与える局所的な効果。

- 速く作れる
- 広く探せる
- 分かるようになる
- 選べるようになる
- 筋が通っているか疑える

### Solution Outcome

業務またはValue Stream全体に期待する変化。

- 開発Lead Timeを短縮する
- 設計Reviewの手戻りを減らす
- 標準Pathの利用を増やす
- Incident調査を速くする
- 意思決定品質を上げる

両者を混ぜると、個々の生成や探索が速くなったことを、Solution全体の価値と誤認
しやすい。構造は次のように置ける。

```text
AI Capability
  ↓
AI Building Block
  ↓
Building Block Outcome
  ↓
組み合わせ・Orchestration
  ↓
AI-enabled Solution
  ↓
Business / Process Outcome
```

MBPMなどでValue Stream上の摩擦を見つけた後、その摩擦を解くSolutionと、Solutionを
構成するBuilding Blockに必要なAI Outcomeを考える。この順序であれば、AIのCapability
から利用箇所を探すのではなく、業務Outcomeから必要な部品へ戻れる。

## Human in the Loopは自動化を育てる観測点

Human in the Loopを、AIの隣で人間が承認Buttonを押す安全装置だけとして扱わない。
初期段階では、人間が各Building Blockの結果を確認し、次を発見する運用Phaseとして
機能する。

- どのInputで失敗するか
- 何を見れば妥当性を判断できるか
- どの中間Outputが次工程の前提を満たさないか
- どこで再生成、差し戻し、停止を選ぶか
- 何が次工程への受け渡し条件か
- どの判断をRuleまたはEvaluatorへ移せるか
- どの判断を文脈依存または高Riskとして人間に残すか

人間の役割も段階的に変わる。

```text
全件を人間が確認する
  ↓
失敗しやすい箇所を重点的に確認する
  ↓
Rule化できる検査をEvaluatorへ移す
  ↓
例外と高Risk判断だけを人間へ戻す
```

> Human in the Loopは未熟な設計の妥協ではなく、自動化可能なProcessを発見するための正規ルートである。

各部品を何で評価すればよいか分からない段階でLoopやGraphへ進むと、誤りを高速で
再生成し、その誤りを後続のBlockや分岐へ伝播させる可能性がある。

## Automation成熟順序としてのWorkflow、Loop、Graph

会話では、次の進化をAI固有の新しい魔法ではなく、Automationの自然な成熟として
整理した。

| 段階 | 主な対象 | 安定させる設計対象 |
| --- | --- | --- |
| Manual Operation | 人間の仕事 | 手順、判断、完了条件 |
| Task Automation | 単一のBuilding Block | Input、Output、失敗条件 |
| Workflow Automation | 複数のBuilding Block | 順序、状態遷移、Handover |
| Loop | Feedbackと再試行 | Evaluator、停止、収束条件 |
| Graph | 分岐、並列、複数経路 | Node間のContract、依存関係、Context伝播 |

Workflowは一方向の流れが安定した結果として作れる。LoopはOutputを評価し、再試行または
停止を選ぶ条件が安定した結果として作れる。Graphは各NodeのContract、依存関係、
分岐条件が安定した結果として作れる。

```text
手動で試す
  ↓
Building Blockごとに品質を確認する
  ↓
Input / Output / Contractを固める
  ↓
人間がBlock間をつなぐ
  ↓
失敗条件と判断基準を集める
  ↓
Evaluatorを作る
  ↓
部分的にWorkflow・Loop化する
  ↓
Contractと分岐が安定した範囲をGraph化する
```

LoopやGraphは否定すべきものではなく、妥当な進化になり得る。ただし、名称や完成図を
出発点として導入するのではなく、前提となるBuilding Blockと評価条件が安定した結果
として選ぶ。

> AI Solution設計は、非決定的な部品を含むAutomation Engineeringである。

## Vendor Presetは完成品ではなく初期仮説

Solution Vendorは、次のような汎用的な骨格をPresetとして提供できる可能性がある。

- よくある工程分割
- 標準的な入出力形式
- 一般的なEvaluator
- 再試行回数と停止条件
- Human Approvalの挿入点
- 典型的な状態遷移
- Log、監査、Rollbackの仕組み

しかし次の正しさは、組織、業務、System、Riskによって変わり得る。

- 何が正しいOutputか
- どの誤りを許容できないか
- どのInput条件で品質が崩れるか
- 誰が何を見て承認するか
- 次工程へ渡してよい最低条件は何か
- 可読性、性能、Security、保守性などの何を優先するか

したがってPresetは完成した業務Solutionではなく、「この分解、評価基準、状態遷移なら
一定品質で回るかもしれない」という初期仮説として扱う。

会話では「汎用Presetで組織にとっての6〜7割程度まで立ち上げる」という例示を用いた。
これは実測値でも一般則でもない。重要なのは、残りが単なる設定差分ではなく、
組織またはSystem固有の正しさの定義であり得ることである。

Human in the Loopで実際の結果と失敗を観測し、Evaluator、遷移条件、Human Reviewの
範囲を補正する。成熟後も完全自動化を目的化せず、文脈依存性やAccountabilityの重さ
から意図的に人間へ残す判断を識別する。

> VendorはLoopの骨格を提供できても、何をもって収束したとみなすかは利用組織が定義する。

## 知識の非対称性

自分でAI Solutionを組み立ててきた人は、実装上の失敗を通じて次を学び、Automationの
原則へ戻りやすい。

- 単発Taskが安定しないと接続できない
- 入出力が曖昧だと後段が壊れる
- 評価基準がないとLoopにできない
- 状態遷移が曖昧だと再試行が暴走する
- 最後は例外処理と監視が支配的になる

一方、後から完成した情報発信を見る人には、Agent、Loop、Graph、Multi-Agentなどの
完成形だけが見え、その手前にある手動確認、失敗収集、Evaluator形成が省略されて
見える可能性がある。

先行者が意図的に隠しているとは限らない。本人にとって自動化の前提が当然となり、
説明から省略されている可能性がある。

後追いする時に真似るべきものは完成形の図だけではない。

> どのBuilding Blockをどの順序で検証し、何を確認して次の自動化段階へ進んだかという成熟順序を真似る。

## 今回の登壇での扱い

この議論は、AI Slop、Handover、Evaluator、Platform Service設計を支える設計思想に
なり得る。一方、25分の本編全体に対しては詳細度が高く、現時点では本編へ入れるかを
決定しない。

本編へ直接入れなくても、AI Platform Design、Agentic Workflow、AI Governance、
Human in the Loop、Evaluator Designについて今後検討する際に再利用できる。

## 限界と未確認事項

- Automationの成熟順序としての整理は、この会話で形成した解釈であり、特定の
  既存Frameworkに照合していない
- Loop Engineering、Graph Engineeringという名称の定義や一般的な用法を外部Sourceで
  検証していない
- Presetが提供できる範囲や、組織固有の補正割合を測定していない
- Human in the Loopから自動Evaluatorへ移行した実例や失敗例を、このメモでは検証していない
- この設計順序がすべてのAI-enabled Solutionに適用できるとは確認していない

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
