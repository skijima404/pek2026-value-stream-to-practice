---
id: RN-20260811-003709-platform-selection-step-quality-interview
type: raw_note
title: "Platform選定・環境入手FlowのStep別品質Interview"
content_language: ja
created_at: 2026-08-11T00:37:09+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-11T01:14:31+09:00
sanitization_checked_by: agent:codex
tags: [ai-allocation, case-recollection, focused-interview, one-way-door, platform-selection, practitioner-experience, quality-priority, service-catalog, value-stream]
---

# Platform選定・環境入手FlowのStep別品質Interview

## この記録の位置づけ

`HYP-20260804-013223-outcome-first-ai-resource-allocation`のU2と、
`HYP-20260809-203135-quality-first-ai-allocation-workflow`のU1およびU2を確認するため、
実践者へ一問ずつFocused Interviewを行った対話を、Agentが構造化して保存する。

対象Flowは複数組織で使われている一般的なFlowを実践者が整理したものであり、単一組織の
一次記録ではない。Bounded Caseは、人手の申請・承認が残る組織で、開発Teamが開発着手に
あたりPlatformを選定し、開発環境を入手するまでとした。

自動化されていないProcessを選んだ理由は、申請者、承認者およびPlatform Teamが担う
Responsibilityと確認観点を明示して比較するためである。AutomationされてもResponsibilityが
消えるわけではなく、自動化されたProcessは、手作業で確認していたCompleteness、
Traceability、Risk GateおよびAccountabilityを包含する必要がある。今回のCase選択は、
未自動化を望ましい状態またはPlatform Engineering成熟度の判定として扱うものではない。

公開対象に不要な固有名、作品名、推定金額および利用基盤の組み合わせは保存していない。
当時の申請Ticket、Project日程、Architecture Review、台帳または自動化設定は確認していない。

## 対象Flow

実践者は次の8 Stepを示した。

1. Platformの種類を調べる
2. それぞれの特徴を調べる
3. 自分が使えそうなものをList upする
4. 比較観点を整理する
5. 観点に従って情報収集する
6. 決める
7. 利用開始の手続きをする
8. 環境を入手する

組織によってStep 7は自動化されている場合があるが、今回のCaseではResponsibilityと
確認観点を可視化するため、人手の申請・承認が残る条件に固定した。自動化済みの場合も、
同じResponsibilityと観点が自動化の仕様、Controlおよび記録へ含まれる必要がある。

## Step 1: Platformの種類を調べる

- Actor: Tech Lead。別ContextではArchitectが担う場合もある
- 完了Outcome: 利用可能なPlatformのListを持っている
- Scope外: 各Platformの詳細調査はStep 2で行う
- 最優先品質: 主要候補に漏れがないCoverage
- 下流影響: Architecture Reviewまたは運用段階で未検討候補を指摘されると、説明と
  再検討が発生する
- 時間制約: 通常はPortal Siteなどを辿れば入手でき、迷っても約1時間である。
  一方、完全性のために1か月から2か月を要することは許容しにくい
- Counterfactual: 10倍速くなる代わりに主要候補が一つ漏れる方法は、Speed改善の便益が
  小さく、漏れのCostが大きいため望ましくない

## Step 6: 決める

- Actor: Tech LeadとArchitecture Board
- 判断特性: 典型的なOne Way Doorとして扱う
- 選定条件: Applicationが必要とする可用性と、それを上回るPlatformの実績を確認する
- 選定条件: 必要な運用を具体的に想像・実行できるか、自動化できるかを確認する
- 選定条件: 保守性と監視設計を確認する
- 最優先品質: 将来の障害と運用を見越し、考慮漏れなく妥当な選択を行うDecision Quality
- Error Cost: 将来の障害、業務上の信頼性低下、Reputation Risk
- Counterfactual: 数日早く決められても、障害要因や必要な運用設計の見落としが明確に
  増える方法は採用しない

## Step 7: 利用開始の手続きをする

- Context: 人手による申請・承認が残る
- Actor: Tech Leadが申請し、Platform Teamが承認する
- 判断特性: ITSMのService Catalog Itemとして手順が固まっており、非決定論的な事象が
  発生すると問題になる

### Tech LeadのOutcome

- 短時間で承認される
- 実際に必要な環境を入手できる
- 認証情報、接続経路および関連する申請を含め、利用開始に必要なものに漏れがない

実践者がProject Memberとして参加した過去Caseでは、Database Serverの払い出し、特権
Accountの作成、管理経路からServerへのAccess許可が別々の申請だった。必要な申請の存在を
知らず、一つずつ申請を出し直したため、実践者の作業開始が約2か月遅れた。

実践者は、個々の申請が速いことより、利用開始に必要なものが一式揃うことを優先した。
抜け漏れを防ぐ方が、Value Stream全体の遅延を抑えられると説明した。

### Platform TeamのOutcome

- 申請内容、作業内容および必要に応じた監査情報を確認できる
- 誰の責任で何を作ったかを追跡できる
- 作成した環境が管理対象として台帳へ記録されている

承認時間を短縮する代わりに、作業記録、責任者、監査情報または台帳登録を省略する方法は
採用しない。省略すると、Incident対応または棚卸しで問題が起きるため、必要な記録の完了は
必須とした。

## Step 7のCapabilityと責任境界

一律に処理を速くするなら、環境構築はAIではなくAnsibleまたはTerraformのような決定的な
自動化を使うと実践者は回答した。

Step 7はITSMのService Catalog Itemに相当し、既知の手順を再現可能に実行する対象である。
そのため、非決定論的な振る舞いを持ち込むAIはDefaultの実行主体に適さず、使う場合も
決定的な手順の外側で不足Checkまたは条件整理へ限定する必要があると実践者は判断した。

AIを使う候補として、次を挙げた。

- 申請が複数に分かれていることを申請者が知らない場合を含む、申請の抜け漏れCheck
- 引き渡し前に、必要な構成要素が揃っているかのCheck
- Componentごとに承認とRejectが混在する場合に、承認結果から実際の作業Scopeを確定する
- 確定したScopeに対応するPlaybookの実行を起動する

承認基準が明確で、重大な金銭判断などCriticalな判断を含まない場合は、AIへ承認を任せる
余地がある。一方、高額Costが関係する、判断根拠が乏しい、または別途承認が必要な場合は
任せない。必要な承認とCost確認がSystem上で完了し、自動作成時のCostを確認でき、AIの
Reproducibilityを制約するGuardrailがあることを条件とした。

実践者は、このStageでのAI利用に積極的ではない。人間がTicket Systemの仕組みを使って
申請・承認を統合できるなら、その方法を優先する。統合の仕組みがなく、複数承認の一部が
欠けても技術的に成立するCaseで、暫定的またはPatch的に不足検出とScope調整を行う場合に、
AI利用の余地があるとした。

## この記録だけでは分からないこと

- 8 Stepのうち、Step 1、Step 6、Step 7以外の優先品質
- 複数組織でFlowが使われた件数、選定方法、例外および失敗率
- 約2か月の遅延を示すProject日程、申請Ticketまたは他の関係者の記録
- 各Stepの実測Process Time、発生頻度、金額換算したError Costおよび総便益
- Speed起点と品質起点の設計を、同一Caseで実装して比較した結果
- AIの再現性を判定する具体的な試験、閾値、Model、Contextおよび運用条件
- One Way Doorと判断する具体的な可逆性基準および例外条件
- Ticket Systemによる統合とAIによるPatchの実装・運用Cost
- 自動化済みProcessが、手作業で確認したResponsibilityと観点を実際に包含しているか
- この結果がPlatform選定以外のValue Streamへ一般化できるか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
