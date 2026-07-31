---
id: RN-20260731-201346-platform-service-rejection-authority-and-duty
type: raw_note
title: "Platform Service案を作らない・まだ出さないと判断する責任"
content_language: ja
created_at: 2026-07-31T20:13:46+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-31T20:15:53+09:00
sanitization_checked_by: agent:codex
tags: [accountability, decision-authority, governance, lean-startup, platform-product-management, platform-service]
---

# メモ

## このメモの位置づけ

`RN-20260731-200122-handover-contract-accountability-transfer`をReviewした後、
Platform ServiceをめぐるDecision RightsのScopeをさらに整理したメモ。

ここでは、次の二つを分ける。

1. 利用者または組織が、どのPlatform Serviceを使うか決める権限
2. Platform Teamが、どのService案を作る、試す、保留する、捨てるか決める権限

この整理は会話時点の考えであり、検証済みの一般論または登壇への採用決定ではない。

## Platform利用に関するDecision Rightsは組織ガバナンスに依存する

Platform Serviceの利用方針は、組織によって異なる。

```text
Mandatory
標準Platformの利用を原則必須とし、例外だけを審査する

Recommended
標準Platformを推奨するが、条件に応じて別の選択を認める

Optional
複数の選択肢の一つとして提供し、利用側が自由に決める
```

この違いは、組織のRisk、規制、標準化方針、Architecture Governance、
予算配分、Team間の責任分界などによって決まる。

したがって、今回のセッションでは「誰がPlatform利用を最終決定すべきか」または
「Mandatory、Recommended、Optionalのどれが正しいか」を一般論として決めない。

Platform Teamが行うべきこととして残るのは、少なくとも次を曖昧にしないことである。

- 利用は必須、推奨、任意のどれか
- 誰が採用または不採用を決めるのか
- 誰が例外を承認するのか
- Platform Teamの推奨は助言か、組織的な決定か
- 利用しない場合に誰が何を引き受けるのか

会話上の短い表現:

> Decision Rightsの配置は組織が決める。Platform Teamは、その配置を
> 曖昧にしたままServiceを提供しない。

## 「アイデアを捨てる権利」への違和感

一方、Platform Team内部のProduct Managementでは、PdMまたはPOがアイデアを
採用、保留、棄却する権限を持つことが多い。

当初は、これを「価値仮説の弱いPlatform Service案を共有資源へ流さない権利」と
表現した。しかし、「権利」だけでは弱く、未検証案を安易にReleaseしないことは
義務または責任とも言える、という違和感が出た。

そこで、次の三つに分ける。

```text
Decision Authority
=
アイデアを採用、保留、棄却できる権限

Duty
=
価値仮説の弱い案を、未検証のまま共有資源へ流さない義務

Accountability
=
なぜ進めた、止めた、捨てたのかを説明する責任
```

PdMまたはPOへ棄却権限が委譲されている場合には、Platform Teamは価値仮説に
基づいてアイデアを選別・棄却する権限を持ち、その権限を行使する義務も持つ、
という整理になる。

## Top-downでSolutionが指定される場合

組織によっては、経営層またはManagerの強い意向により、実施するSolutionまで
Platform Teamへ与えられる。この場合、PdM、POまたはPlatform Teamに完全な
棄却権限がない可能性がある。

この状況では「アイデアを捨てる権利」が重要になる。権限者の意向に対して、
Platform TeamがValue Hypothesisの弱さを理由に止められるかは、組織設計に
依存する。

ただし、完全な棄却権限がなくても、次の責任まで消えるわけではない。

- Value Hypothesisが未検証であると明示する
- 全面Releaseではなく、限定したExperimentへ落とす
- 継続条件と停止条件を置く
- 下流へ生じるCostとRiskを可視化する
- 検証結果と継続判断を、権限を持つ人へ返す

この場合、止める対象は必ずしも経営上のValue Hypothesisではない。
未検証のSolutionを無制限にProductionまたは共有資源へ流すことを止め、
安全に検証可能な単位へ変換する。

## Lean Startupとの接続

ここでいう「捨てる」は、気に入らないアイデアを恣意的に排除することではない。

- Value Hypothesisを置く
- 小さく検証する
- 継続条件と停止条件を決める
- Evidenceに基づいて継続、Pivot、保留、棄却を選ぶ

というLean Startupの選別機能を指す。

AIによって案、Prototype、文書、機能を短時間で作れるほど、この選別を行わない
Costは大きくなる。未検証案が共有資源へ入ると、利用者、Reviewer、Enablement、
Operationsなどへ理解、検証、Support、廃止の仕事が発生するためである。

特にMandatoryなPlatformでは、価値の弱いServiceを出した時の影響が、利用者の
選択によって避けられず、組織全体へ強制的に広がる可能性がある。このため、
Release前の選別と検証はより重要になる。

## 現時点の中心表現

会話で最も分かりやすいと判断した表現:

> AI時代のPlatform Teamは、作る責任だけでなく、作らない・まだ出さないと
> 判断する責任を持つ。

より厳密に表す場合:

> Platform Teamには、未検証のアイデアをそのままProductionへ流さないための
> Decision AuthorityとAccountabilityが必要である。

ただし、Authorityの範囲は組織によって異なる。したがって、この表現は
「Platform利用を利用者へ強制する権限」を意味しない。

## セッションScope候補

今回扱う候補:

- Platform TeamがService案を選別する
- Value Hypothesisの弱い案をRelease前に捨てる
- 捨てられない案を小さなExperimentへ変換する
- 「まだ出さない」と判断する
- その判断を説明可能にする

今回扱わない候補:

- Platform利用をMandatory、Recommended、Optionalのどれにすべきか
- 標準Platformの採用を誰が強制できるか
- 例外承認権限をどのRoleへ配置すべきか
- 組織ごとのArchitecture、Security、Risk Governanceの正解

このScope分離により、Platform利用の統治モデル一般へ話を広げず、AIで生成が
高速化した時代のPlatform Product ManagementとAdmission Controlへ集中できる。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
