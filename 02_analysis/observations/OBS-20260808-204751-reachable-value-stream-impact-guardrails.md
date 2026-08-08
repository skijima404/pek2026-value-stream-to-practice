---
id: OBS-20260808-204751-reachable-value-stream-impact-guardrails
type: observation
title: "手の届くValue Streamでは利用者Value・副作用・Cost移転を分けて確認すると整理された"
content_language: ja
created_at: 2026-08-08T20:47:51+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-08T20:56:36+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - case_recollection
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260808-195818-problem-sufficiency-reachable-system-improvement
  - type: derived_from
    target: RN-20260808-201058-reachable-value-stream-impact-guardrails
  - type: derived_from
    target: RN-20260808-202752-responsibility-bounded-problem-scope
---

# 観察

## 知識の成立根拠

作成者は、手の届く範囲で改善する場合でも、対象Value Streamに良い影響が出たか、
許容しない副作用がないか、および他のActorやProcessへCostを移していないかを確認する
必要があると説明した。この判断は、`recorded_statement`および
`practitioner_experience`として保持する。

Password Reset問い合わせとService理解を支援した介入は、元資料を現在確認できない
個別事例の記憶であるため、`case_recollection`として扱う。

三つのRaw Noteを接続し、介入範囲、観測範囲、利用者Value、局所Metric、Guardrail、
Cost移転および判断十分性を分ける部分は`reasoned_synthesis`である。これは
Platform ServiceまたはWorkslop対策の効果を独立検証した結果ではない。

## 根拠箇所

- `RN-20260808-195818-problem-sufficiency-reachable-system-improvement`の
  「連休明けのPassword Reset問い合わせ」、
  「手の届く限りのEnd-to-End」
- `RN-20260808-201058-reachable-value-stream-impact-guardrails`の
  「手の届くValue Streamの意味」、
  「Password Reset問い合わせのValue Stream」、
  「Service理解と選択を支援した事例」、
  「部分最適との区別」
- `RN-20260808-202752-responsibility-bounded-problem-scope`の
  「手の届くValue Streamで先に価値を出す」、
  「部分最適との区別」

## 根拠から直接言えること

記録では、「手の届く範囲」を自Teamの局所Metricだけを見ることとは区別している。
介入は現在の権限、能力、技術またはCostで変更可能な範囲に限定しても、観測と価値判断は、
介入の影響を受ける利用者のValue Streamまで広げる。

問い合わせ件数が減った場合でも、次の状態は同じ意味ではないと整理している。

- 利用者の問題が減り、問い合わせの必要がなくなった
- 利用者が自力で解決できるようになった
- 問い合わせ先またはChannelが変わった
- 利用者が解決またはService利用を諦めた
- 確認、学習または回避作業を利用者へ移した

そのため、局所Metricだけで改善を判定せず、次を分けて確認する。

- 定義した利用者Valueと期待する正方向の変化
- 局所Processまたは提供側のSignal
- 利用者側で実際に起きた変化
- 許容しない副作用とGuardrail
- 他のActor、ChannelまたはProcessへのCost移転
- 現在確認できない影響と残存不確実性
- 定義したProblemへの十分性と、次に境界を広げる条件

Password Resetの事例では、Support Center側の目的を、連休明け月曜午前の問い合わせPeakを
平準化し、Peak基準の人員配置による余剰Costを抑えることとして説明している。一方、
利用者側のValueを、必要な時にログインして必要な情報を確認できる状態としている。
連休前の注意喚起は、当時手の届く範囲で両方を正方向へ変える介入として評価された。

Service理解を支援した事例では、説明会とWeb情報を、利用者がServiceを体系的に理解し、
利用の入口で「どのIT Serviceを使えばよいか分からない」という問題を改善する介入として
説明している。実践者の記憶では、同様の問い合わせは数か月かけて約半分になった。

これらの事例では、問い合わせ減少そのものではなく、定義した利用者Valueとの接続を
判断根拠としている。利用者が諦めた、別Channelへ移動した、または負担を引き取った結果で
あれば、問い合わせ減少だけをValue Stream改善として扱わない。

## 曖昧さと限界

- Password ResetとService理解の事例について、元のData、報告資料、問い合わせ分類、
  対象期間、比較条件および施策以外の変化を現在確認できない。
- Password Reset問い合わせの減少が、時間帯間の移動、総件数の減少、別Channelへの移動、
  利用者の事前作業または実際の人員Costのどれに対応したかは未確認である。
- Service理解に関する問い合わせ減少が、理解、選択精度、利用開始または利用者Outcomeの
  改善によって生じた因果効果かは確認していない。
- 副作用またはCost移転がなかったことを示す一次記録は確認していない。
- ITSMのCaseは、Platform ServiceのDVSとOVSまたはWorkslop対策へ直接適用できない。
- どこまでを観測範囲とし、どの副作用をGuardrailにし、何をもって定義したProblemへ
  十分と判断するかは、対象Value Streamごとに定義する必要がある。
- このObservationは、`HYP-20260807-232639-dvs-learning-sustains-ovs-quality`のU1または
  U3に対するEvidence CoverageやFindingを更新するものではない。

## 公開安全性確認

- checked_at: 2026-08-08T20:56:36+09:00
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
