---
id: OBS-20260804-195508-ai-proposal-generation-shifted-review-burden
type: observation
title: "提案書の生成短縮後に別担当者へ検証・再構築・意味変換の作業が移り生成停止が判断された"
content_language: ja
created_at: 2026-08-04T19:55:08+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-12T01:26:17+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - case_recollection
  - explicit_validation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260804-195507-ai-proposal-review-burden-case
  - type: derived_from
    target: RN-20260804-235840-ai-proposal-stakeholder-concerns-handoff-contract
  - type: references
    target: RN-20260805-002030-ai-output-reviewer-feedback-withdrawal-case
---

# 観察

## 知識の成立根拠

一件のConsulting提案書作成について、生成物を受け取って後続作業を担当した
Practitionerへ、生成時間、Review、追加作業、再生成、Guardrailおよび後続判断を
順に質問した振り返りInterviewに基づく。
目的を持ってEvidenceを確認した活動は`explicit_validation`として扱う。

一方、Version履歴、作業時間記録、指摘一覧または生成時のPromptはRepositoryで
確認していない。記録された出来事と時間は、一件の記憶に基づくため
`case_recollection`として扱う。

`RN-20260804-235840-ai-proposal-stakeholder-concerns-handoff-contract`には、
同じ提案書Caseについて、作成担当者、顧客およびConsulting側が必要とするConcernの違いを
振り返った対話が記録されている。Concernの欠落を後続作業へ接続する部分は
`reasoned_synthesis`であり、顧客本人または作成担当者への追加Interviewではない。

`RN-20260805-002030-ai-output-reviewer-feedback-withdrawal-case`は、未成熟なAI生成資料を
受けた別ContextのReviewerがFeedback簡略化を検討した一件として参照する。提案書Caseの
出来事または因果を裏付けるEvidenceとしては扱わない。

## 根拠箇所

- `RN-20260804-195507-ai-proposal-review-burden-case`の「対象となった作業」
- 同Raw Noteの「生成後に発生した作業」「ContextとGuardrail」「行った判断」
- `RN-20260804-235840-ai-proposal-stakeholder-concerns-handoff-contract`の
  「作成担当者が重視したConcern」「顧客側で必要になる情報」
  「Consulting側が重視したConcern」「対話中に得られた暫定的な整理」

## 根拠から直接言えること

従来は複数人で4〜5時間程度だった同種の提案書作成に対し、生成AIを利用した一件では、
初稿生成が1時間未満だったと記録された。ただし、同一内容、品質および範囲を揃えた
比較ではない。

Presentationの生成と再生成は、Interview回答者とは別の担当者が実施した。
生成後には、後続担当者である回答者による二回の逐語的Review 6時間、不足した
Scopeと作業分担の再構築3時間、さらに別の担当者による、通常は作成しない顧客理解用
Summary 3時間が発生した。確認できた後続の人間作業は合計12時間であり、初稿生成と
修正操作の時間を含まない。

生成物は手作業の場合より見栄えが良かった。一方、提案と具体的な顧客価値の接続、
Project Scope、具体的活動、作業分担および顧客が負う責務が、提案として利用できる
程度に含まれなかったと記録された。

指摘後には生成担当者によってPresentation全体が再生成され、見栄えが大きく変化した
ため、後続担当者は全体を再Reviewした。再生成に備えてMarkdownで保持した用語上の
Guardrailも、
再生成された資料では守られなかった。Contextが渡されなかったのか、渡されたが
重視されなかったのかは確認できない。

後続担当者は、生成時間だけでなく、Review回数と時間、不足情報の再構築、追加資料の
作成を合わせて確認し、生成AIによる提案書生成を停止した。顧客提案が目的であり、
再利用可能なPresentation生成Pipelineの構築は目的ではないため、Pipeline改善を
継続しないと判断した。

同じCaseをStakeholder Concernから振り返ると、生成物は作成担当者が重視した顧客価値を
前面に出した一方、顧客が購入判断、社内説明、参加準備および役割調整を行うための条件と、
Consulting側が実行可能性、Scope、責務および将来の期待値相違を管理するための条件を
十分に含まなかったと整理された。AIがConcernの偏りを作ったかは確認されておらず、
明示されなかったConcernが後続のReview、再構築および追加資料作成として現れたという
Mechanism候補までを記録する。

別Contextでは、未成熟と認識されたAI生成資料をReviewしたExecutiveが、今後も丁寧な
Feedbackを続ける代わりに短い否定だけで終えることを検討していた。ただし、実際にFeedbackが
簡略化されたか、作成者の学習、次回品質または協働関係が変化したかは確認していない。
この一件は、下流負荷が継続するとReviewerの関与意欲または信頼へ影響し得る論点を示す
Contextであり、主Caseの観測結果へ統合しない。

## Validation Componentへの射程

- U1に対しては、生成時間の短縮と同時に、検証、再構築および意味変換の作業が
  生成担当者とは別の後続担当者へ現れた一件として、`analogous`なEvidenceになる。
  見栄えの改善もあったため、便益と負荷を分けずに一方だけを結論にできない。
- U2に対しては、生成時間だけでなく、Review時間、Review回数、不足情報の再構築、
  追加資料を接続して見ることで、負荷が現れた箇所を振り返りで特定できた。
  顧客側の直接Signalは取得していない。
- U3に対しては、観測した負荷と提案作成のOutcomeを用いて、生成の継続ではなく
  停止へ判断を更新した一件になる。
- U4に対しては、生成停止という制御は行われたが、停止後の負荷減少を同一条件で
  測定していないため、削減効果は判断できない。
- U7に対しては、提案の整合性、具体的活動、責務および顧客に届く意味の確認を
  必要な摩擦として残し、全体再生成に伴う再ReviewとPipeline改善の継続を目的に
  寄与しない負荷として止める判断に使った一件になる。

## 曖昧さと限界

- Consulting提案書の一件であり、Platform Serviceに対する直接Evidenceではない。
- 従来版と生成AI版の作業範囲、品質および完成条件は一致しない。
- 記録された時間は一次記録から再計算していない。
- Summaryが必要になった原因を、生成AI、入力Context、人間側のConcernの偏り、
  Facilitationまたは提案Processへ分離できない。
- 全体再生成は見栄えの大きな変化から後続担当者が判断したもので、生成Systemの内部記録を
  確認していない。
- 顧客価値と具体的な作業の接続が不足したという判断は提案側によるもので、顧客本人の
  Interviewまたは利用行動では確認していない。
- Stakeholder Concernの優先順位は、顧客本人または作成担当者へ追加確認していない。
- 別ContextのReviewerがFeedback簡略化を検討した一件は、実際の行動変更と後続Outcomeを
  確認しておらず、主Caseと同一のMechanismであるとは判断できない。
- 生成を停止した後に負荷が減ったか、手動作成がより良い結果になったかは未確認である。

## 公開安全性確認

- checked_at: 2026-08-12T01:26:17+09:00
- checked_by: agent:codex
- result: `sanitized`
- scope:
  この分析ノードの本文、frontmatter、relationの組み合わせを、
  人間の意図Reviewを確定する時点で再確認した
- finding:
  公開対象に不要な識別情報をCategory単位で削除または一般化し、削除値は
  Repository、訂正履歴、Filename、Logへ保存していない
- limitation:
  公開安全性の確認は、内容の正しさ、検証完了、採用を意味しない
