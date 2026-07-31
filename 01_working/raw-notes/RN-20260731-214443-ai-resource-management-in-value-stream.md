---
id: RN-20260731-214443-ai-resource-management-in-value-stream
type: raw_note
title: "AIをValue Streamへ配置するResource Management"
content_language: ja
created_at: 2026-07-31T21:44:43+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-31T21:54:11+09:00
sanitization_checked_by: agent:codex
tags: [ai-capability, accountability, human-ai-collaboration, raci, resource-management, responsibility-boundary, value-stream, work-design]
---

# メモ

## このメモの位置づけ

2026年7月31日に「残すべき摩擦」を議論した後、責任境界、RACI、仕事の依頼、
AIをResource Managementへ組み込む考えへ発散した対話を抽出したRaw Note。

- 人間とAssistAの発言を分離せず、思考がDriftした経緯として再構成した
- AIを法的または人格的に人間と同一視する主張ではない
- Human Resourceという表現は、Capabilityを把握し、仕事を割り当て、Reviewし、
  責任境界を設計するWork Allocation Modelの比喩として使った
- PEK2026本編への採用は未決定であり、本筋から外れる可能性がある
- 会話上の観察と発散であり、検証済みの一般論ではない

## Driftの起点: 全部、責任境界ではないか

必要な摩擦を考える中で、人間とAI、Platform Teamと利用者、開発者とBusinessの
間にある問題は、責任境界の違いとして整理できるのではないかという話になった。

```text
AI
  ↓
人間
  ↓
Platform Team
  ↓
利用開発者
  ↓
Business Owner
```

各境界では、仕事または成果物だけでなく、次を決める必要がある。

- 誰が目的を決めるか
- 誰が作業するか
- 誰が採用または却下を判断するか
- 誰が何を保証するか
- 誰が失敗時に説明するか
- 誰がOutcomeを評価するか

対話上の短い整理:

> ハンドオーバーはEventであり、責任境界はDesignである。

## 人間とAIの協業モデル

会話では、AIと人間の候補的な分担を次のように置いた。

```text
AI
- 候補を生成する
- 探索する
- 比較する
- 反証候補を出す
- 情報を整理する

人間
- 目的を決める
- 前提と適用範囲を確認する
- 採用、却下、例外を判断する
- 結果を利用する責任を引き受ける
- 説明責任を持つ
```

これは、人間がAIの全出力を無差別に再実施または全文確認するという意味ではない。
人間がどの判断にAccountabilityを持ち、何を機械的に検証し、どこで専門家Reviewへ
戻すかを設計する、という意味である。

## Accountabilityの空白

AIは案を生成できるが、会話上はAI自身へ組織的なAccountabilityを置かないと
整理した。

```text
AI
案を生成した

人間
良さそうなので共有した

未整理
誰が採用を判断したのか
誰が利用者へ保証したのか
誰が失敗時に説明するのか
```

この空白があると、「AIが作ったから」という説明により、成果物を採用した人間
または組織の判断が見えなくなる。

成熟した候補では、AIは選択肢、理由、前提、Risk、追加Review条件を示し、人間は
確認した前提と採用理由を記録した上で判断する。

この点で、Reasoning Chainを確認する目的は、AIの回答精度を上げることだけでなく、
人間が判断を引き受けられる状態かを確認することにもある、という案が出た。

## RACIは組織図ではなく責任の流れを見る

会話では、そもそも仕事をRACIの粒度で整理していない組織があるのではないか、
という発散があった。

人間側の個人的な観察として、RACIを説明すると、`R`と`A`へ上司または役職者を
置き、結果として単なる組織図のようになるケースがあるという話が出た。この観察は
体系的に検証しておらず、特定の国または組織形態の一般的特性とは扱わない。

会話で意図したRACIの読み方:

```text
Responsible
誰が作業、品質確認、Maintenanceを実行するか

Accountable
誰が採用判断を引き受け、利用者へ説明できるか

Consulted
誰の専門知識または判断材料が必要か

Informed
誰が結果または影響を知る必要があるか
```

`A`は単に最も役職が高い人ではなく、その判断を引き受け、説明可能な人である。
詳細を知らない上司だけが`A`で、現場の`R`には判断権限がない場合、承認は必要だが
実質的な判断者がいない状態になりうる。

AIによって案を作れる人が増えるほど、「誰がその案を採用してよいと判断したか」
を分けて見る必要がある。

## Prompt Engineeringを仕事依頼の設計として見る

会話では、良いPromptに含まれる要素を次のように挙げた。

- Role
- Objective
- Context
- Constraint
- Acceptance Criteria

これはRACIそのものではないが、相手に何を担当させ、どこまで期待し、何をもって
完了とするかを明確にする点で共通している。

対話上の見方:

```text
未成熟な見方
Prompt Engineering = AIへ命令する呪文

別の見方
Prompt Engineering = AI Resourceへ仕事を依頼するWork Design
```

AIに仕事を渡すことで、これまで人間同士では暗黙に済ませていた目的、責任範囲、
判断基準、完了条件を言語化せざるを得なくなる。この意味でAIは、組織が曖昧に
してきた責任境界を可視化する圧力になりうる、という解釈が出た。

## AIを「生成する道具」と見ることの影響

AIを「生成する道具」と捉えると、利用は自然に生成Taskへ集中する。

```text
- 文章を書く
- Codeを書く
- 資料を作る
- 要約する
- Imageを作る
```

一方、会話ではAIを生成前の仕事にも配置できると整理していた。

```text
- Problemを分解する
- 観点を増やす
- 前提を確認する
- 仮説を比較する
- 反証する
- 評価基準を作る
```

生成TaskではInputがある程度決まり、Outputを作る。DiscoveryまたはDecisionでは、
そもそも何をInputとし、何を決める必要があるかを整理する。

したがって、AIを単なる生成Toolとして見るか、共同作業するKnowledge Workerの
ように見るかで、配置するTaskと必要なContractが変わるという話になった。

## AI Resourceを管理する項目

AIをResourceとして扱う場合、会話では次の項目を候補として挙げた。

```text
Capability
何ができるか

Boundary
何ができないか、何を任せないか

Context
仕事に必要な何を知っているか、何を渡す必要があるか

Accountability
AIのOutputに関する判断責任を誰が持つか

Feedback
結果から何を更新するか
```

人間のTeam Memberについて、調査が得意、設計Reviewはできる、最終判断は任せない、
背景説明が必要、と考えるのと同様に、AIについてもCapabilityとBoundaryを見て
仕事を割り当てるという比喩である。

重要な留保:

- AIを法的または人格的なHuman Resourceと同一視しない
- AIに最終的なAccountabilityを置くという意味ではない
- AIが`Responsible`相当のTaskを実行しても、人間または組織が判断責任を持つ
- CapabilityはModel、Tool、Context、Task、運用条件によって変わる

## Value StreamへのResource配置

AIをResourceとして扱うと、議論の入口が「どのAI Use Caseを作るか」から変わる。

```text
Value Streamを観察する
  ↓
必要なCapabilityを特定する
  ↓
Human / AI / Platformの役割と責任を分ける
  ↓
適切なResourceを配置する
  ↓
全体のFlow、品質、Accountabilityを観測する
```

この観点では、AI導入はTool選定だけではなく、Work DesignとResource Allocationの
問題になる。

以前整理したAI Outcomeの候補とも接続する。

```text
1. 速く作る
2. 広く探す
3. 分かるように解釈する
4. 選べるように整理する
5. 本当に筋が通るか疑う
```

どのOutcomeが必要かを先に決め、そのCapabilityを持つAIをValue Streamのどこへ
配置するかを考える。AIの性能比較または生成Use Caseを先に置かない。

## 現時点の中心表現

対話上の暫定表現:

> AI時代の課題は、AIの使い方を覚えることだけではない。仕事を渡す相手が
> 人間であれAIであれ、Capabilityと責任境界を設計できる組織になることにある。

もう一つの表現:

> どのCapabilityを持つResourceを、どのValue Streamへ配置するか。

この二つは発散中の表現であり、PEK2026の中心メッセージとしては未採用。

## Sessionとの距離

この話は、AI Slopから責任境界を経て、組織設計とResource ManagementへDriftした。

PEK2026へ接続できる点:

- DeliveryだけでなくDiscoveryとDecisionへAIを配置する
- AIに期待するOutcomeを先に定義する
- AIから人間、Platformから利用者への責任境界を設計する
- VSMまたはMBPMで局所最適を避ける

本筋から外れる点:

- RACI一般の解説
- 国または組織文化に関する一般化
- AIをHuman Resourceとして扱う組織論
- Prompt Engineeringの再定義

したがって、現時点では本編の構成要素ではなく、背景となる個人の観察および
将来の検討候補として残す。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
