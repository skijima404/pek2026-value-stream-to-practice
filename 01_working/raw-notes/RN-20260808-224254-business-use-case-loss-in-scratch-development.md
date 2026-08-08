---
id: RN-20260808-224254-business-use-case-loss-in-scratch-development
type: raw_note
title: "Scratch開発でBusiness Use CaseがSystem Use Caseへ縮退する構造"
content_language: ja
created_at: 2026-08-08T22:42:54+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-08T22:48:22+09:00
sanitization_checked_by: agent:codex
tags: [business-use-case, ddd, dvs, enterprise-development, requirements, scratch-development, system-use-case, ux-responsibility]
---

# メモ

`RN-20260808-221549-individual-substitution-for-organizational-dvs-learning`で扱った
Package導入・設定型のContextとは別に、EnterpriseのScratch開発でBusiness Use Caseが
System Use Caseへ縮退する構造について、実践者の経験と解釈を記録する。

一般に「DX人材」と呼ばれる役割へ結びつける解釈は、今回のScopeには含めない。

## 要件・設計Reviewで見えるBusiness Use Caseの不在

実践者は、業務上の都合で要件定義の場へ参加し、設計書をReviewすることがある。その際、
Business Use Caseが会話や資料に存在せず、技術者が「業務」と呼ぶ内容が、すでに
Softwareの機能またはSystem Use Caseへ変換されている場合があると説明した。

例えば、要件定義で帳票を先に固める進め方がある。ここでいう帳票は、画面Layoutまたは
出力するReportである。帳票を決めた後、各属性をどのように計算するかを確認し、その内容を
実装する。

この進め方では、次のSystem側情報は具体化される。

- 画面またはReportのLayout
- 表示または出力する属性
- 属性の計算方法
- 入力、更新または連携の仕様
- 実装する機能

一方、その画面またはReportを利用するActorが、どの状況で、何を根拠に、何を判断し、
次にどのActionを取り、どのOutcomeを改善するのかは、Meetingで扱われず、資料にも
残っていない場合がある。Reviewで質問しても、そのBusiness Use Caseが出てこないことがある。

その結果、実装者は共有されたSystem Use Caseを正確に実装できても、完成したSoftwareが
利用者の業務判断とOVS Valueへ接続するかを検証できない。「要件がない」のではなく、
System Use Caseは存在するが、その根拠となるBusiness Use CaseとReasoning Chainが
失われている状態である。

## 失われた順序と復元すべき順序

実際に共有される順序は、次のようになり得る。

```text
帳票・画面
  -> 表示する属性
  -> 属性の計算方法
  -> 実装
```

一方、Business Use Caseから辿る場合は、次の順序になる。

```text
Actorが置かれた業務状況
  -> 必要な判断
  -> 判断後のAction
  -> 期待Outcome
  -> 判断に必要な情報
  -> Read Model・帳票・画面
  -> 属性と計算方法
  -> 実装
```

Package型Contextでは、期待ValueからDataの粒度、Mandatory Fieldおよび利用ルールへの
接続が欠ける。Scratch開発では、Business Use CaseからRequirement、Read Model、Data Model、
API、UIおよびAcceptance Criteriaへの接続が欠ける。いずれも、技術的な成果物は存在しても、
その根拠となる利用者Valueと意思決定が失われるという共通構造を持つ。

## UX Designの責務に生じる空白

実践者には、一部の古いEnterprise Contextで、UX Designの責務が利用者または業務側に
あるように見えることがある。一方、利用者または業務側は、UX DesignをIT側が行うものと
考えているように見える。

この責務認識が両側に存在する場合、次のEnd-to-Endの責任主体が空白になり得る。

- 利用者のProblemとContextを確認する
- Business Use Caseを構成する
- Actorの判断、ActionおよびOutcomeを定義する
- User Journeyと業務ProcessをSoftwareへ接続する
- Prototypeまたは設計を利用者と確認する
- 利用開始後の利用、非利用、回避行動およびOutcomeを観測する
- 観測結果を次のRequirementと設計へ戻す

IT側には帳票、画面、Fieldおよび計算式というSystem Use Caseだけが渡り、利用者側は
IT側がUXを設計すると期待する。両者とも責務を放棄した認識を持たないまま、Business Use Case
から利用後OutcomeまでをEnd-to-Endで所有するActorが存在しない状態になり得る。

これは両側の責務認識を直接確認した結果ではなく、要件定義と設計ReviewでBusiness Use Caseが
存在しないことから形成した実践者の見立てである。

## Experienceを形成しにくいEnterprise Project構造

Enterpriseで新しいSystemを立ち上げる機会は、同じTeamが短いCycleで何度も経験できる
日常的な活動ではない。実践者の経験では、新規System立ち上げの経験者が少ないことを、
関係者自身が大きな問題として認識しているContextがあった。

この条件から、次の構造が生じるという解釈候補がある。

```text
新規System立ち上げの機会が少ない
  -> Business Use CaseをSoftwareへ変換した経験者が育ちにくい
  -> 機能中心のRequirementと設計になる
  -> 利用後に期待Valueへ接続しない
  -> Project終了後に学習主体が残らない
  -> 次の立ち上げでも経験者が少ない
```

この因果Loopは現時点では解釈候補であり、Project間比較、Teamの継続期間、Experienceの分布、
利用後FeedbackのDelayまたは学びの再利用を調査した結果ではない。

## 継続的なWeb ServiceとのContrast

実践者の定性的な観察では、長期間Serviceを運営するWeb系の組織には、過去の反省をまとめ、
改善へ反映しているように見える例がある。

これはWeb系であること、またはAgileであること自体が十分条件だという主張ではない。
Contrastを説明し得る変数として、次の候補がある。

- Feedback機会の頻度
- FeedbackのDelay
- TeamとOwnerの継続性
- 利用後OutcomeへのAccess
- 学びの記録と再利用
- 次の変更へ反映するDecision Rights

同じServiceへ複数回Releaseし、利用を観測し、振り返りを次のReleaseへ反映できる構造は、
一回型ProjectよりDVS学習Capabilityを形成しやすい可能性がある。ただし、利用Dataを集めても、
Problem、Value、Solutionまたは実装のどこへ戻るかを判断しなければ、Release回数が多いだけで
システム学習にはならない。

## DDD Workshopによる要求の考古学

Business Use Caseと要求のReasoning Chainが失われている場合、DDDのWorkshopでは、
現在残っているSystem Use Case、帳票、画面、Process、Dataおよび実装上の制約から、
Business Use Caseを復元する「考古学」が必要になるという実践者の説明がある。

公開記事
[「レガシーモダナイゼーションのためのDDDワークショップ設計メモ」](https://note.com/skijima/n/n13533c4cdf48)
では、Legacy Systemで設計意図、Systemが支えるBusiness Architecture、および
Business ArchitectureからSystem設計へ至る要求仕様が失われる問題を記録している。

同記事では、System的な処理やEventを書いた後、その結果を人間がどのように認識し、
何を根拠に、どのような判断を行うかまで記述することをWorkshopの条件としている。
また、現在も有効なBusiness Architectureに根拠を持つ要求と、過去の技術に由来する
Legacy Constraintを区別し、要求からBoundary案までのReasoning Chainを検証する。

このWorkshopを提供した経験について、実践者には需要が大きかったという記憶がある。
ただし、提供件数、対象選定、利用者評価またはOutcomeを確認した記録ではない。

実践者は、Business Use CaseとSystem Use Caseの分離および両者を接続する必要性が、
DDDが生まれた背景にあるのではないかと解釈している。これはDDDの歴史的成立理由を
一次資料で調査した結果ではなく、実践経験から形成した個人的な解釈仮説である。

## この記録の位置づけ

- 要件定義と設計ReviewでBusiness Use Caseが見つからなかったことは、実践者の経験に
  基づく`practitioner_experience`として扱う候補である。
- 特定の要件定義または設計Reviewの詳細と一次記録は保存せず、発生件数も推定しない。
- Enterprise、Web系、技術者、利用者または業務側の全体へ一般化しない。
- UX Designの責務認識は、両側へ直接確認した事実ではなく、観察から形成した見立てである。
- Enterprise Project構造とExperience不足の因果Loopは未検証の解釈候補である。
- DDD Workshopの公開記事で確認できる内容と、Workshop需要に関するCase Recollectionを
  分けて扱う。
- DDDが生まれた理由についての説明は、歴史的事実ではなく個人的な解釈仮説である。
- このRaw Noteは、`HYP-20260807-232639-dvs-learning-sustains-ovs-quality`のEvidence Coverage、
  Finding、ApplicabilityまたはEpisode全体の結果を更新するEvidenceではない。
- Review後、U3のScratch開発Contextを具体化するObservation候補として検討できる。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
