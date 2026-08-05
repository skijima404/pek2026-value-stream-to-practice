---
id: RN-20260805-211321-ai-platform-prerequisite-knowledge-gap
type: raw_note
title: "AI開発基盤の理解に必要なAutomation・Platform前提知識への気づき"
content_language: ja
created_at: 2026-08-05T21:13:21+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-05T21:20:37+09:00
sanitization_checked_by: agent:codex
tags: [ai-platform, audience-assumption, automation-engineering, enablement, knowledge-gap, platform-engineering, session-design]
---

# AI開発基盤の理解に必要なAutomation・Platform前提知識への気づき

## このメモの位置づけ

複数の顧客との会話で、自分がAutomationの基本だと考えていた進め方と、AI開発基盤を
構成する要素のImageが共有されていなかったことに驚いた。この体験と、そこから生じた
登壇AudienceおよびEnablementに関する見立てを記録する。

顧客、案件、参加者、会話時期を特定できる情報は保存しない。このメモは限定された
会話の記憶を起点としており、組織一般やPEK参加者全体の知識を示す調査結果ではない。

## 驚いたこと

自分がAutomationの基本として前提にしていたのは、次の順序である。

```text
まず手動で仕事を実行する
  ↓
手順、判断、状態遷移、完了条件を確認する
  ↓
安定した部分を個別に自動化する
  ↓
各部分の結果を確認する
  ↓
最後に接続し、Orchestrationする
```

しかし会話した相手には、この順序がAutomationの進め方として共有されておらず、
実際の作業でも適用されていなかった。

同じ会話では、「AI開発基盤」が具体的に何を組み合わせたものになるかというImageも
共有されていなかった。自分には既存のSoftware Delivery PlatformへAI特有のBuilding
Blockを追加する構造として見えていたが、この前提を他者も持っているとは限らなかった。

## 自分が暗黙に置いていたAI開発基盤のImage

### 既存のSoftware Delivery／Platform要素

- Git
- CI/CD
- GitOps
- Artifact管理
- Secrets
- Identity／Access Management
- Observability
- Workflow
- Test、Review、Deployment

### AI固有またはAIで重要性が増す要素

- LLM
- Prompt／Context
- Embedding
- Vector Search／Retrieval
- Evaluator
- Human in the Loop
- AI OutputのTraceability

この見方では、AI開発基盤は全体をゼロから作り直す特別な箱ではない。既存のSoftware
Delivery PlatformとEngineering Practiceを土台に、確率的にOutputを作るResourceと、
その評価・制御に必要なBuilding Blockを追加したものとして理解できる。

「AIは開発者の代わり」という説明も用いた。これは、AIが人間と同じ責任や判断権を
持つという意味ではない。AIがCodeや変更案を作る場合でも、Git、Review、Test、CI/CD、
GitOps、ObservabilityなどのDeliveryと運用の仕組みは引き続き必要である、という
連続性を示すための比喩である。

## 生じた見立て

当初は「Automationの基本を知らなかった」と受け止めて驚いた。一方、会話を通して、
個人の知識不足だけではなく、知識体系の接続が見えにくい可能性を考えた。

```text
Automation Engineering
  ↓
Software Delivery／Platform Engineering
  ↓
AI Platform
```

自分の中ではこの階段が一本につながっている。ところがAI、Agent、Loop、Graph、MCP、
Tool Callingなどの言葉から入ると、その手前にある手動Processの理解、状態遷移、
Building Block、Contract、Evaluatorが見えないことがあるかもしれない。

> AI Platformを理解しにくい原因は、AIの知識不足だけではなく、Automation EngineeringとPlatform Engineeringへの接続が示されていないことかもしれない。

これは現時点の仮説的な解釈である。限定された会話だけから、原因を特定したものではない。

## Enablementへの示唆候補

AI Platformを説明する時、完成形のAgentやGraphから始めず、次の順序を見せる方が理解を
助ける人がいる可能性がある。

1. 手動で仕事を実行し、判断と状態遷移を確認する
2. 従来の開発基盤を構成する要素を示す
3. AIによって追加・変更されるBuilding Blockを示す
4. 個々のBuilding BlockをHuman in the Loopで確認する
5. 安定した範囲をWorkflow、Loop、Graphへ発展させる
6. それらを利用者向けFeatureと組織向けServiceとして提供する

AIを完全に新しいPlatformとして説明するのではなく、既存知識のどこへ接続するかを
示すEnablementである。

```text
従来の開発基盤
Git / CI/CD / GitOps / Identity / Observability
  ＋
AI Building Block
LLM / Retrieval / Evaluator / Human in the Loop
  ↓
利用者向けAI Feature
  ↓
組織が運営するPlatform Service
```

ただし、GitOpsなどの既存Practice自体に馴染みがない人には、この説明も前提を要求する。
Automation、Software Delivery、Platform、AI Platformという教育順序を意識する必要がある。

## 登壇設計への影響候補

今回の体験は、話し手が暗黙に置いていた前提が、Audienceにとって一般的とは限らない
ことを示すSignalになった。

本編でFeature DesignとService Designを説明する前に、次の連続性を一枚程度で示す案がある。

```text
Automation
  ↓
Software Delivery／Platform Engineering
  ↓
AI Platform
```

この一枚には、次の役割を期待する。

- AI Platformを未知の巨大な箱に見せない
- 既存のAutomationとPlatformの知識へ接続する
- AI Solutionの当たり前品質が必要であることを前提化する
- そのうえでFeatureとServiceの価値設計へ話を進める

一方、この説明を本編で詳細化すると、25分の中心がAutomationへ移り、AI Slop、
Feature Design、Service Design、Lean Startup、MBPMの一本道がぼやける可能性がある。
現時点では本編の短い前提説明、Appendix、または別のAI Platform Enablement資料の候補
として保留する。

## 限界と未確認事項

- 限定された複数の会話の記憶であり、体系的なInterviewまたはAudience調査ではない
- 相手がAutomationの考え方を「知らなかった」のか、知っていて今回適用しなかったのかを
  このメモだけでは区別できない
- AI開発基盤をImageできなかった原因が、AutomationまたはPlatform知識の不足だとは
  確認していない
- 会話相手のRole、経験、組織条件を公開できないため、他のAudienceへの一般化はできない
- 一枚の補足説明がPEK参加者の理解を助けるかは未検証である
- 登壇本編への採用は決定していない

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
