---
id: RN-20260804-235840-ai-proposal-stakeholder-concerns-handoff-contract
type: raw_note
title: "AI生成提案書におけるStakeholder ConcernとHand-off Contract"
content_language: ja
created_at: 2026-08-04T23:58:40+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-05T00:03:58+09:00
sanitization_checked_by: agent:codex
tags: [ai-slop, contract, handoff, proposal, service-design, stakeholder-concern]
---

# AI生成提案書におけるStakeholder ConcernとHand-off Contract

2026年8月4日にCodex上で行った対話を、公開可能な範囲へ一般化して記録する。
これは、別のRaw Noteに記録済みのConsulting提案書事例について、後続作業が必要に
なった背景をStakeholderごとのConcernから振り返ったものである。

## 作成担当者が重視したConcern

生成AIを利用して提案書を作成した担当者には、顧客価値が十分に高ければ顧客は
提案を購入する、という考えを重視する傾向があった。

生成された提案書は顧客価値を前面に出し、手作業で作る場合より見栄えが良かった。
その一方で、Project Scope、具体的な活動、作業分担、顧客が負う責務など、他の
Stakeholderが必要とする情報が不足した。

## 顧客側で必要になる情報

顧客は、提案の価値を理解するだけでなく、組織内で提案の必要性と実行条件を説明
する必要がある。振り返りでは、例えば次の情報が必要になるとされた。

- 既存の仕組みには何が不足しているか
- 対応しなければ、後でどのような問題が起こり得るか
- Projectへ参加するために、どの程度の工数が必要か
- どの資料を、誰と、どのようにやり取りするか
- 具体的にどのような活動を行うか
- 終了後に何が得られるか
- 得られる価値や成果を社内稟議でどのように説明するか
- 別のVendorや関係者と、どのように役割を分けるか

これらは提案の価値を補足する細部ではなく、顧客が購入判断、社内説明、参加準備
および関係者調整を行うために必要な情報である。

## Consulting側が重視したConcern

Consulting側では、提案内容が実行可能であり、将来の期待値の相違を生まないことが
重要になる。振り返りでは、例えば次の点を逐語的に確認する必要があるとされた。

- 合意できない作業がProject Scopeへ紛れ込んでいないか
- 顧客と提供側の役割および責務が区別されているか
- 「実際に行うこと」と、理解を助けるための「作業イメージ」が混同されていないか
- 他社事例が、今回も実施または提供される内容であるように読めないか
- 言葉の印象によって、実際の合意内容とは異なる期待を持たれないか
- 将来Projectが難しい状況になった時、解釈の違いによって紛争になり得る要素がないか

Consultingの契約形態として準委任を前提とする場合には、避けるべき表現や、使用を
慎重に判断すべきKeywordもある。一般的な提案書では自然に見える表現であっても、
完成責任、成果保証、引渡しまたは責任範囲について、意図しない印象を与える可能性が
ある。具体的な法的評価や使用可能な表現は、個別の契約条件と適切なReviewによる。

## 対話中に得られた暫定的な整理

この事例では、生成AIが事実と異なる内容を作ったことだけが問題だったわけではない。
生成物は、作成担当者が重視する「顧客価値」というConcernについてはよく表現した
一方、顧客とConsulting側が意思決定、実行および合意のために必要とするConcernを
十分に含まなかった。

AIが作成担当者のConcernの偏りを生んだかは確認できない。確認できる範囲では、
作成担当者が重視したConcernが、見栄えの良いPresentationとして高速に展開された。
一方、明示的に与えられなかった他のStakeholderのConcernは十分に補完されず、
生成後にReview、Cross-check、Scopeの再構築および追加資料の作成が必要になった。

この対話では、提案書を単なる説得資料ではなく、顧客の意思決定、社内説明、参加準備、
他者との役割分担、提供側の実行可能性および将来の期待値管理を接続する境界Artifact
またはContractとして見る整理が提示された。

また、次の表現が検討された。

> Hand-offで欠落したConcernは消えない。後続のReview、追加資料、調整、手戻り、
> または将来のトラブルとして再び現れる。

> AI Slopには、AIが間違えたものだけでなく、ある当事者には完成品に見える一方で、
> 他の当事者が意思決定または実行するための条件を欠いた成果物も含まれ得る。

これらは対話中の解釈であり、このRaw Note単独では一般的な因果関係または普遍的な
Patternを確立しない。

## この記録で確認できないこと

- 顧客本人または提案書作成担当者へ、各Concernの優先順位を改めて質問していない
- 生成時のPrompt、Context、Version履歴および指摘一覧をRepositoryで確認していない
- どのConcernが生成AIへ明示的に渡されていたかを確認していない
- 生成AIがConcernの偏りを作ったのか、既存の偏りを増幅または可視化したのかを判別できない
- 表現による契約上の効果を、法務または契約専門家が評価した記録ではない
- 一件の振り返りであり、他の提案、TeamまたはPlatform Serviceへ一般化できない

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
