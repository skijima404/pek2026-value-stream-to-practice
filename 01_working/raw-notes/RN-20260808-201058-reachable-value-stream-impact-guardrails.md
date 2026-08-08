---
id: RN-20260808-201058-reachable-value-stream-impact-guardrails
type: raw_note
title: "手の届くValue Streamで効果と副作用を確認する"
content_language: ja
created_at: 2026-08-08T20:10:58+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-08T20:15:57+09:00
sanitization_checked_by: agent:codex
tags: [cost-transfer, guardrails, itsm, local-optimization, ovs, practitioner-experience, systems-thinking, value-stream]
---

# メモ

`RN-20260808-195818-problem-sufficiency-reachable-system-improvement`で整理した、
定義した問題への十分性と、手の届くEnd-to-End改善について、部分最適との違いを
追加で対話した。

このRaw Noteは、実践者の説明と過去のIT Service改善に関する記憶を保存する。
問い合わせData、報告資料、施策資料、利用者調査または当時のMetric定義は、
このRepositoryでは確認していない。

## 手の届くValue Streamの意味

実践者は、手の届く範囲で改善する場合でも、対象Value Streamに良い影響が出ているか、
または副作用が生じていないかを確認する必要があると説明した。

手の届く範囲とは、自分たちの局所Metricだけを見ることではない。介入は現在の権限、
能力、技術またはCostで変更可能な範囲に限定しても、価値判断は、介入の影響を受ける
利用者のValue Streamまで含めて行う。

例えば、問い合わせ件数が減った場合でも、次の状態は同じ意味ではない。

- 利用者の問題が減り、問い合わせの必要がなくなった
- 利用者が自力で問題を解決できるようになった
- 問い合わせ先またはChannelが変わった
- 利用者が解決を諦め、Serviceを使わなくなった
- 利用者へ確認、学習または回避作業を移した

局所的な問い合わせ件数だけでは、どの状態が起きたかを判定できない。定義したValueに
対する効果と、他のActorまたはProcessへのCost移転を確認して、介入の十分性を判断する。

## Password Reset問い合わせのValue Stream

約15年前のSupport Center事例では、Support Centerの関心事は、月曜日午前の
問い合わせPeakに合わせた人員配置と、平常時の余剰CapacityによるCostだった。

一方、問い合わせを行う利用者は、Passwordを使ってIT Serviceへログインする利用者だった。
Passwordの有効期限切れは、利用者にとって「必要な時にいつでもログインし、必要な情報を
確認できる」という状態を損なっていた。

連休前にPasswordの有効期限へ注意するよう促すCampaignは、Support CenterのPeak需要を
平準化するだけでなく、利用者が必要な時にログインできない状態を事前に避ける介入として
位置づけられた。実践者は、この施策を、利用者のValueを損なわず、現状より正方向へ
変化させる改善案として成立していたと評価している。

実践者の記憶では、Campaign後にPassword Reset問い合わせは従来の半分以下になった。
ただし、当時の利用者のログイン成功、業務開始Delay、事前変更作業、別Channelへの移動、
Securityへの影響または総Costを、このRepositoryで再確認できる資料はない。

## Service理解と選択を支援した事例

別の機会には、Serviceの使い方に関する問い合わせが非常に多かった。そこで、Serviceに
関心がある人へ説明会を実施し、WebでもServiceの使い方に関する情報を発信した。個別の
問い合わせへ繰り返し回答するだけでなく、より体系的に学べる機会を提供する介入だった。

実践者の記憶では、同様の問い合わせは数か月をかけて約半分になった。実践者は、この変化を、
利用者によるIT Serviceの理解と、利用の入口で生じる「どのIT Serviceを使えばよいか
分からない」という問題の改善として評価している。

この事例について、説明会の参加者数、Web情報の閲覧、問い合わせの分類方法、Serviceの
選択精度、利用開始、利用者Outcome、問い合わせChannel間の移動または施策以外の変化は、
このRepositoryでは確認していない。同様の問い合わせが減ったという記憶だけから、利用者が
Serviceを理解した因果効果または一般的なEnablement施策の有効性を確定しない。

## 部分最適との区別

手の届くValue Streamでの改善は、観測範囲を自Teamへ閉じる部分最適とは異なる。

- 定義した利用者Valueを明示する
- 介入によって期待する正方向の変化を置く
- 局所Metricと利用者側の変化を区別する
- 他のActor、ChannelまたはProcessへのCost移転を確認する
- 許容しない副作用またはGuardrailを置く
- 現在確認できない影響を残存不確実性として残す
- 効果が限定的であれば、次のCycleで観測または介入の境界を広げる

この整理では、観測と価値判断は介入範囲より広く取り得る。現在変更できない要因があっても、
その影響を見えなくしたり、局所改善をEnd-to-Endの価値改善として扱ったりしない。

## この記録の位置づけ

- 二つの事例は、元資料を現在確認できない`case_recollection`として扱う候補である。
- 複数の改善経験から形成された判断は、`practitioner_experience`として扱う候補である。
- Password Reset問い合わせとService理解の事例は、Platform ServiceのDVSとOVSを
  直接比較した検証ではない。
- 問い合わせ減少は局所Signalであり、利用者Valueの改善、Cost移転の不存在または因果を
  単独で証明しない。
- この内容は、手の届くValue StreamのOperational Definition候補であり、
  `HYP-20260807-232639-dvs-learning-sustains-ovs-quality`のEvidence Coverage、Finding、
  ApplicabilityまたはResidual uncertaintyを更新したものではない。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
