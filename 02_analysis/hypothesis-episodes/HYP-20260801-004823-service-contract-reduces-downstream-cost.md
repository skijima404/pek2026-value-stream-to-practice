---
id: HYP-20260801-004823-service-contract-reduces-downstream-cost
type: hypothesis_episode
title: "共有前のService Contract明確化は下流への理解と判断Costの転移を抑える"
content_language: ja
created_at: 2026-08-01T00:48:23+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-12T01:33:00+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - case_recollection
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260801-004821-contract-accountability-cost-transfer
  - type: derived_from
    target: OBS-20260812-010722-ai-output-closure-boundary
  - type: references
    target: OBS-20260812-010724-contract-first-progressive-automation-practice
  - type: tests
    target: HYP-20260804-183210-ai-slop-downstream-burden-value
---

# 仮説

AI生成物またはPlatform Serviceを共有資源へ流す前に、対象利用者、期待Outcome、
前提、受入条件、保証範囲、非対象、Decision Rights、例外時の戻し先をService
Contractとして明らかにし、提供者が理解、検証、採否判断を引き受ければ、
受け手へ移る前提調査、再検証、補完、判断、説明のCostを抑えられる。

## 知識の成立根拠

`OBS-20260801-004821-contract-accountability-cost-transfer`に整理された、Hand-off、
Service Contract、AccountabilityおよびCost Transferを分ける
`practitioner_experience`と`reasoned_synthesis`から形成した。

`OBS-20260812-010722-ai-output-closure-boundary`には、一人の実践者による複数Contextの
反証的Interviewを通じ、対象、保証範囲、採否主体およびHand-off前のClosureが異なるCaseで
下流負荷の現れ方も異なったことが、`recorded_statement`、`practitioner_experience`、
`case_recollection`、`explicit_validation`および`reasoned_synthesis`として記録されている。
ただし、Contract明示の有無を同一条件で比較したものではなく、このEpisodeのValidationを
完了したEvidenceとしては扱わない。そのため、Source Observationの
`explicit_validation`を、この`not_tested` Episode自身の`knowledge_basis`には転記しない。

`OBS-20260812-010724-contract-first-progressive-automation-practice`は、Contract Firstと
段階的自動化が複数回反復された実務Contextとして参照する。下流Cost削減または因果効果を
示さないため、非EvidenceのContextに限定する。

## Mobiusでの位置づけ

`solution`

親となるValue Hypothesis
`HYP-20260804-183210-ai-slop-downstream-burden-value`に対して、選択・検証能力を
共有境界で実装するSolution Hypothesisである。

## 期待する兆候

- 受け手が、適用対象、前提、保証範囲、次のActionを再構築する作業が減る
- 適用外Caseまたは例外が、利用後の手戻りより前に識別される
- 提供者が、共有前に採用、保留、棄却または限定Experimentを判断できる
- 問題発生時に、誰が修正、停止、例外判断を行うかが分かる
- Contract作成が形式的な文書追加ではなく、実際の選別と受入判断に使われる

## 反証またはChallengeとなる兆候

- Contractを明確にしても、受け手の確認、補完、判断Costが変わらない
- Contractの作成と維持が、回避した下流Costを継続的に上回る
- 実際の利用Contextを事前に記述できず、例外または問い合わせが減らない
- Contractが責任回避の免責文書になり、利用者が安全に次へ進めない
- 提供者に採否または停止のDecision Authorityがなく、未検証案の流入を止められない

## 検証方法

### 方法と対象範囲

- 方法:
  類似する小さなPlatform ServiceまたはTemplateを対象に、Contract項目を明示した
  Caseと明示しなかった過去Caseを比較する。または一つの限定Releaseで、共有前後の
  質問、追加確認、差し戻し、例外、Supportを記録する。
- 対象・資料: 未選定
- 選定方法:
  対象利用者と利用条件を限定でき、受け手側の追加作業を追えるCaseを優先する
- 実施規模:
  一つのService、Templateまたは限定Releaseから始める

### GenAIの利用

- 利用内容:
  Sourceから前提、非対象、受入条件、責任境界の候補を抽出し、欠落と矛盾を
  レビューする
- GenAIだけで実施しないこと:
  提供者のAccountability、利用可否、組織上のDecision Rightsを決定する
- 実際に確認した資料・記録:
  現時点ではrelationで示したRepository Nodeのみ

## 結果

`not_tested`

### 実際に観測したこと

Contract、Handover、Accountability、Cost Transferを分ける考えはRepositoryに
記録されている。複数ContextでClosure条件が異なるCase Seriesと、Contract Firstを
反復利用した実務Contextは追加された。一方、Contractを明確にしたCaseとしなかったCaseの
同一条件比較、または下流Costが減った実地記録は、まだ保存されていない。

## 解釈

このEpisodeが置く新しい因果は、Handoverの有無ではなく、共有前のContractと
提供者側のAcceptanceが、下流へのCost Transferを左右するという点である。

Contractは文書量を増やすことではなく、共有してよい候補を選別し、受け手が
安全に次へ進める条件を明らかにする仕組みとして扱う。

## 限界

- Contractの項目と必要な厳密さは、ServiceのRiskと組織ガバナンスによって異なる
- 暗黙知、未知の利用Context、Productionで初めて分かるRiskは残る
- Contractがあっても、内容が誤っている、古い、利用者に理解できない可能性がある
- このEpisodeは、Contractを登壇の中心概念として採用する判断ではない
- Closure Case Seriesは同一Practitionerの経験に相関し、Platform Serviceへ直接一般化できない
- 段階的自動化の反復回数は実践者の記憶で、Contractの因果効果または成功率を示さない

## 公開安全性確認

- checked_at: 2026-08-12T01:33:00+09:00
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
