---
id: OBS-20260808-224827-business-use-case-loss-in-scratch-development
type: observation
title: "Scratch開発ではBusiness Use Caseが失われSystem Use Caseだけが共有される場合がある"
content_language: ja
created_at: 2026-08-08T22:48:27+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-08T22:53:38+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - external_research
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260808-224254-business-use-case-loss-in-scratch-development
  - type: derived_from
    target: EXT-20260808-224826-ddd-legacy-modernization-workshop-article
---

# 観察

## 知識の成立根拠

実践者は、EnterpriseのScratch開発における要件定義または設計Reviewで、Business Use Caseが
会話や資料に存在せず、技術者が「業務」と呼ぶ内容が、すでにSoftwareの機能または
System Use Caseへ変換されている場合があると説明した。この説明は`recorded_statement`と
`practitioner_experience`として保持する。

本人が公開したDDD Workshop記事を実際に確認し、Legacy Systemで設計意図、Business
Architectureおよび要求仕様が失われるという問題設定と、人間の判断まで遡って要求と
System Boundaryを復元・検証する方法が記載されていることを`external_research`として保持する。

Package型のData Contract欠落とScratch型のBusiness Use Case欠落を、Value、判断、Data、
SoftwareおよびOutcomeのTraceabilityが失われる共通Mechanismとして接続する部分は
`reasoned_synthesis`である。

## 根拠箇所

- `RN-20260808-224254-business-use-case-loss-in-scratch-development`の
  「要件・設計Reviewで見えるBusiness Use Caseの不在」
- 同Raw Noteの「失われた順序と復元すべき順序」
- 同Raw Noteの「UX Designの責務に生じる空白」
- 同Raw Noteの「Experienceを形成しにくいEnterprise Project構造」
- 同Raw Noteの「継続的なWeb ServiceとのContrast」
- 同Raw Noteの「DDD Workshopによる要求の考古学」
- `EXT-20260808-224826-ddd-legacy-modernization-workshop-article`の
  「公開ページで確認した内容」と「今回の分析との関係」

## 根拠から直接言えること

実践者の説明では、要件定義で帳票、画面Layoutまたは出力Reportを先に固め、表示属性と
計算方法を確認して実装する場合がある。この時、System側のLayout、Field、計算式、連携および
機能は具体化される一方、画面を利用するActorが、どの状況で、何を根拠に、何を判断し、
次にどのActionを取り、どのOutcomeを改善するのかが会話と資料に存在しないことがある。

これはRequirementが完全に存在しない状態ではない。System Use Caseは共有されているが、
その根拠となるBusiness Use CaseとReasoning Chainが失われ、実装者が仕様どおり作っても、
Softwareが利用者の業務判断とOVS Valueへ接続するかを検証できない状態である。

失われたTraceabilityは、次の順序として整理できる。

```text
Actorと業務状況
  -> 判断とAction
  -> 期待Outcome
  -> 判断に必要な情報
  -> Read Model・帳票・画面
  -> 属性、計算方法、Data Model、APIおよび実装
```

実践者には、一部の古いEnterprise Contextで、UX Designを利用者・業務側とIT側の双方が
相手側の責務と見ているように見えるという見立てがある。この場合、利用者Contextの確認、
Business Use Case、User Journey、Prototype、導入後の利用観測およびFeedbackを
End-to-Endで所有する主体が空白になり得る。

公開記事では、Legacy SystemでBusiness ArchitectureからSystem設計へ至る要求仕様が
失われる問題を扱い、System上の処理またはEventの後に、人間が結果をどう認識し、何を根拠に、
どのような判断をするかまで記述するWorkshop条件を置いている。既存SystemとIT側のKnowledgeを
起点に業務を復元する場合は、Domain Expertによる確認が必要な箇所を分け、現在の仕様を
そのまま再生産しないために実装理由を問い直す。

## 解釈候補

Package型では、期待ValueからDataの粒度、Mandatory Fieldおよび利用ルールへの接続が欠ける。
Scratch型では、Business Use CaseからRequirement、Read Model、Data Model、API、UIおよび
Acceptance Criteriaへの接続が欠ける。両者は、技術的成果物が存在しても、Value、判断、Data、
利用およびOutcomeのReasoning Chainが失われる共通Mechanismとして比較できる。

新規System立ち上げの機会が少ない、利用後のFeedbackを受ける前にProjectが終了する、
または学習主体が次のProjectへ残らないことが、このCapabilityを形成しにくくする可能性がある。
一方、長期間継続するWeb Serviceでは、Feedback頻度、Team継続性、OutcomeへのAccessおよび
次のReleaseへ反映するDecision Rightsを持ちやすい可能性がある。

これらは因果を検証したFindingではなく、今後比較する変数の候補である。

## 曖昧さと限界

- 要件定義または設計Reviewの件数、選定方法、一次記録および発生率は確認していない。
- Business Use Caseが存在しなかったのか、参加者が説明できなかったのか、Reviewで参照できる
  資料に残っていなかっただけなのかを区別していない。
- UX Designの責務認識を利用者・業務側とIT側へ直接確認していない。
- Enterprise Project構造、Experience不足、Business Use Case喪失および利用後Outcomeの
  因果を比較Caseで検証していない。
- Web系の組織に関する説明は実践者の定性的なContrastであり、組織群の比較調査ではない。
- 公開記事はLegacy Modernization向けの自己資料であり、新規Scratch開発の直接Evidence、
  DDD Workshopの効果検証または独立した第三者研究ではない。
- Workshopの需要に関するCase Recollectionと、DDDが生まれた理由についての個人的な
  解釈仮説は、このObservationのFindingには含めていない。
- このObservationは、対象HypothesisのU3を具体化するSource候補であり、Platform Serviceで
  OVS品質への影響を独立検証したものではない。

## 公開安全性確認

- checked_at: 2026-08-08T22:53:38+09:00
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
