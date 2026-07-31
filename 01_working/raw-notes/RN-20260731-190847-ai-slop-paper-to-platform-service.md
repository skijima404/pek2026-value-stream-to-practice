---
id: RN-20260731-190847-ai-slop-paper-to-platform-service
type: raw_note
title: "AI Slop論文からPlatform Service設計へ読み替えた対話"
content_language: ja
created_at: 2026-07-31T19:08:47+09:00
content_origin: mixed
created_by: human:kijima
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-07-31T19:22:23+09:00
sanitization_checked_by: agent:codex
tags: [accountability, ai-slop, platform-service, queue, wip, workslop]
---

# メモ

## このメモの位置づけ

2026年7月31日に、読書メモを材料として人間とAssistAが行った対話から、
論文の位置づけ、Platform Engineeringへの読み替え、Accountabilityを
抽出したRaw Note。

- 人間とAssistAの発言を分離せず、思考が動いた経緯として再構成した
- 論文の内容そのものは、別Raw Note
  `RN-20260731-190846-endless-stream-ai-slop-reading-notes`に保存した
- ここにある読み替えは、論文のClaimではなく、登壇へ接続するための
  人間とAssistAの解釈を含む

## 論文の位置づけ

“An Endless Stream of AI Slop”は、AI Slopの客観的な発生率または因果を
証明する研究ではなく、開発者がAI Slopをどのように認知し、語っているかを
構造化した探索研究として読む。

したがって、Review Friction、Quality Degradation、Forces and Consequencesは、
AI Slopの「体験された症状」の分類として扱う。

## 論文と今回の登壇で扱うLayerの違い

会話では、論文と登壇の整理を次のように分けた。

```text
論文:
AI Slopが開発者、Reviewer、Maintainerに
どのように体験され、語られたか

今回の登壇:
Platform Service設計において、
その症状がなぜ生じるか、どこへ介入できるか
```

Platform Service設計側のCause Lens候補:

- Outcomeが不明確
- Service Contractが不明確
- WIPまたはQueueが過多
- Human AttentionまたはReview Capacityが制約
- Feedbackが不足
- Incentiveが不一致
- Accountabilityが不明確
- Deliveryだけが高速化され、Discovery、Decision、Validationが追いつかない

この対応は確立された分類ではなく、論文の症状分類をPEの設計問題へ
読み替えるための検討案である。

## AI Slopをコスト外部化として読む

対話で中心になったのは、AI Slopを単なるlow-qualityな生成物としてではなく、
生成側の生産性向上が、受け手側の検証税、判断負荷、将来Riskへ変換される
構造として読むことだった。

Slop性を高める条件候補:

- 表面的には有能で、無視せず確認する必要がある
- 生成より検証の方が高コスト
- 大量に作れる
- 検証コストが他者または共有資源へ移る
- 作った人が理解、説明、責任を引き受けない

```text
生成者の時間削減
  ↓
Reviewerまたは利用者の確認負荷
  ↓
Human AttentionのQueue
  ↓
技術的負債、判断Risk、信頼低下
```

## 生成の自由と共有資源への投入責任

ローカルでAIを使って多数の案を生成し、探索すること自体は問題としない。

問題になる境界は、選別、理解、検証していない探索物を、Review、PR、
Platform Portal、Document、Template、Advisor回答などの共有資源へ投入し、
他者の仕事へ変えた時である。

> 自分の探索成果を、いつ他人の仕事へ変えたのか。

表現候補:

```text
Generate freely.
Share responsibly.
```

日本語での表現候補:

> 生成は自由でよい。ただし、共有資源へ流す前に責任を引き受ける。

## Accountability

読書メモで残った言葉:

> “It’s not AI’s code, it’s my code.”

Platform Serviceへ読み替えた表現候補:

> “It’s not AI’s service, it’s our Platform Service.”

AIが作ったかどうかではなく、提供者が次を引き受けられるかを問う。

- 内容を理解しているか
- 検証したか
- 根拠と前提を説明できるか
- 責任境界を定義したか
- 利用者へ渡してよい品質か
- 誤った時に修正または停止できるか

AI生成物を共有した瞬間に、それはAIの成果物ではなく、提供者の成果物または
Serviceになるという整理である。

## Platform Engineeringで影響が直接利用者へ届く

通常のProduct Developmentでは、AI SlopはDVS内の不良WIPとして発生し、
その先でOVSへ品質劣化または障害として影響するという見方ができる。

Platform Engineeringでは、次のもの自体が利用開発者への価値提供になる。

- Golden Path
- Template
- Documentation
- API
- Guardrail
- Platform Advisor
- Self-Service Experience

そのため、PEのDVSで作られたものが、利用開発者のOVSへ直接入る。

```text
PEチームがAIで生成を高速化する
  ↓
粗いTemplate、Document、Guardrail、Advisor回答を共有する
  ↓
利用開発者が確認、回避、再検証、問い合わせを行う
  ↓
PEチームの局所的な生産性向上が、
Product Teamのworkslopになる
```

これは、別Raw Note
`RN-20260731-144737-platform-dvs-and-user-value-stream`で検討した、
Platform Serviceを作るDVSと、利用者側Value Streamを接続して観測する考えへ
つながる。

## WIP、Queue、Human Attention

正しい種類の試行またはTransformation上必要なズレであっても、組織が
Reviewと学習へ変換できる量を超えるとworkslopになり得る。

```text
AIで生成を並列化する
  ↓
試行、Review待ち、判断待ちが増える
  ↓
人間のAttentionと判断Queueへ集中する
  ↓
Context Switchと滞留によって文脈が劣化する
  ↓
Feedbackの密度が下がる
  ↓
学習に変換できないOutputが増える
```

したがって、Transformationは正しい方向の試行を増やすだけでは進まず、
試行をReviewし、学習へ変換する能力と釣り合った速度を必要とする。

## 検証能力ではなく、物差しの不足かもしれない

AIには「これを作って」と対象を指定する一方、「これが正しいか確認して」では、
何に照らすかを渡していないことがある。

検証に必要な物差し候補:

- 期待する状態
- Value HypothesisとOutcome
- Acceptance Criteria
- 変えてはいけないこと
- 比較方法
- Risk許容度
- 完了の定義
- Service Contract

物差しを与えずにAIへ実装と検証を依頼すると、AIが要求を推測し、同じ推測に
沿って実装とTestを作り、両方が同時に間違いながらgreenになる可能性がある。

したがって、「生成は強いが検証は弱い」とAI能力だけを比較する前に、
生成へ与えた「これ」と同じ密度で、検証にも「これに照らして」を
渡しているかを確認する。

## 留保

- このメモは論文そのものではなく、人間とAssistAによる読み替えを含む
- 論文の症状分類と、Platform Service設計のCause Lensを混同しない
- DVSとOVSの接続およびCause Lensは、検証済みの一般理論ではない
- 個別Modelの能力比較は本編の対象外とする

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
