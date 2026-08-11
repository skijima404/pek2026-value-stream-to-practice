---
id: RN-20260811-115140-small-application-standard-path-walkthrough
type: raw_note
title: "小規模Applicationの標準Path・Scope判定・軽量分析Interview"
content_language: ja
created_at: 2026-08-11T11:51:40+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-11T12:02:00+09:00
sanitization_checked_by: agent:codex
tags: [admission-control, case-recollection, focused-interview, lightweight-analysis, platform-standard, practitioner-experience, service-scope, standard-path, two-way-door]
---

# 小規模Applicationの標準Path・Scope判定・軽量分析Interview

## この記録の位置づけ

`HYP-20260804-013223-outcome-first-ai-resource-allocation`のU1について、基幹系の
One Way Doorとは異なるContextを確認し、同HypothesisのU4について小規模利用での分析Costと
簡略化条件を確認するため、実践者へFocused Interviewを行った対話をAgentが構造化して
保存する。

具体的なApplication例は実践者の指示により保存しない。公開対象に不要な組織、部門、
Application、利用者、内部Systemまたは技術構成の識別情報は保存せず、分析に必要な
Application規模、Risk境界、Roleおよび標準Pathだけを残す。

## Bounded Case

小さな新規Applicationを、一つの部門が標準構成で短期間に提供するCaseを対象とした。

- Application自体は、作り直し可能なTwo Way Doorである
- 作り直しによるSchedule遅延はあり得るが、同じFramework内なら手戻りは比較的小さい
- 部門標準として技術構成があらかじめ決まっている
- 開発者は、違和感がなければ比較選定せず標準構成を採用する
- Applicationごとの選定理由は、実質的に「部門標準だから」で閉じる

標準構成を決める側は、顧客体験を改善する小規模Applicationを迅速に作るという部門Missionに
適合する構成として選定していた。

## Service ScopeとAdmission Control

標準構成で扱えない規模のApplicationは、例外構成として部門内で受け入れるのではなく、
部門のService Scope外として受けない。

- Decision Owner: 部門長
- 対象Scope:
  Serverless Functionと単純なData Store程度で構成できる、本当に小さなApplication
- Risk境界:
  重大なDataを扱わない
- Scope外の場合:
  より大規模なApplicationを扱う別部門へ相談するよう案内して断る

Scope外判断後のRoutingは実践者が他者から聞いた内容であり、実施記録または判断者本人の
回答を確認していない。

具体的に確認できた受付基準は、Application規模とDataの重大性の二つである。それ以外の
受付基準は確認していない。

## 可逆性と判断時点

Application自体はTwo Way Doorである一方、実装Teamへの割り振りは、実装開始後に別Teamへ
持ち替えることが難しいためOne Way Doorになると実践者は判断した。

したがって、作る技術の選択をApplication単位で比較するCostは小さいが、どのTeamまたは
Service Scopeで引き受けるかは実装開始前に確認する必要がある。

## 実際の受付対話

実際のやり取りは固定Formによる二条件Checkより流動的である。Business側などから判断者へ
実現可能性を相談し、判断者が次のいずれかを返す。

- 標準構成で実現できるため受け入れる
- 別の仕掛けが必要なため受け入れず、別部門へ相談するよう案内する

AI判定または単純なRule Checkを行うには、申込側が必要な実装を理解し、Architecture判断と
正しいTeamへの割り振りに必要な情報を入力できるという前提が必要になる。しかし、実際の
相談はBusiness要求から必要な仕掛けを解釈する対話であり、その前提を満たすとは限らない。

## AIの責任境界

Enterprise全体がAI Nativeで、部門Scope、利用可能なCapability、Riskおよび他部門の
受入条件がDigital化・接続されていれば、AI Routingが可能になる将来はあり得る。

現時点では、Enterprise情報のDigital化が制約され、AIが判断に必要なContextへアクセス
できないため、AIへ最終的な受入、拒否またはRoutingを任せない。AIを使う場合も、質問の
聞き返し、要求整理または判断材料の下書きに限定し、部門長が最終判断を保持する。

## 軽量な分析

一枚程度の小規模Applicationに対して、重いArchitecture Vision作成または詳細なRisk比較は
過剰である。軽量なHypothesis Statement程度で、次を確認する候補を置いた。

- 誰のどの課題を扱うか
- 期待するOutcome
- 小規模Application部門のScopeへ収まるか
- 重大なDataを扱わないか
- 標準構成で実現できるか
- 受入またはScope外の判断

実践者は、これをSAFe上のEpicとして扱うことを明確に否定した。このCaseの規模はEpicより
小さい。ここでは`EPIC Hypothesis Statement`の分類または規模を適用せず、Formatだけを
流用する。価値仮説と得たいOutcomeを明確にできれば十分とする。

実践者個人の感覚値では、現場観察とFact Checkを含め、実働約16時間で十分とした。これは
組織の実測値、合意値または標準ではない。

誤ったTeamまたは誤ったValue Hypothesisに基づいて数か月を投資するRiskを下げられるなら、
約16時間の分析Costは安く、妥当であると実践者は回答した。

## 成立根拠の区別

- `recorded_statement`候補:
  Interviewで保存した標準構成、Service Scope、可逆性、受付対話、AI責任境界、軽量分析案、
  約16時間の感覚値およびCounterfactual
- `practitioner_experience`候補:
  標準Path、Two Way DoorとOne Way Doorの区別、AIのContext制約、軽量分析およびCost妥当性に
  関する実務判断
- `case_recollection`候補:
  実践者が知る一つの部門の標準Pathと受付対話
- `reasoned_synthesis`候補:
  Applicationの可逆性とTeam割り振りの不可逆性、標準Pathによる選定不要化、AI Nativeな
  将来と現在の責任境界、および約16時間と数か月の投資Riskの比較
- `explicit_validation`候補:
  U1の対照ContextとU4の軽量化条件を目的として行ったFocused Interview

Routingの実施は伝聞であり、部門資料、受付記録、開発記録またはCost記録をRepositoryで
確認していないため、`direct_observation`または`external_research`として扱わない。

## この記録だけでは分からないこと

- 部門Mission、標準構成、Service Scope、受付基準またはRoutingの正本
- 部門長、開発者、Business側またはRouting先部門の回答
- Application件数、失敗率、作り直しCost、Team持ち替えCostまたは実際のLead Time
- AIまたはRule-based Checkを導入した場合の判断品質、所要時間またはRouting結果
- Enterprise情報のDigital化範囲と、AI Routingに必要なContextの具体的な充足条件
- 軽量Hypothesis Statementの実際の形式、作成時間、Review時間または判断への寄与
- 約16時間の感覚値が組織で再現され、数か月の誤投資を実際に回避するか
- 標準構成の作成・維持Cost、標準が顧客体験および開発速度へ与えたOutcome

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
