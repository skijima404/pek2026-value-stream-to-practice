---
id: RN-20260804-195507-ai-proposal-review-burden-case
type: raw_note
title: "生成AIによる提案書生成で検証・再構築作業が増え停止判断に至った事例"
content_language: ja
created_at: 2026-08-04T19:55:07+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: corrected
sanitization_status: sanitized
sanitization_checked_at: 2026-08-04T20:00:58+09:00
sanitization_checked_by: agent:codex
tags: [ai-slop, case-recollection, cost-transfer, proposal, review, workslop]
---

# 生成AIによる提案書生成で検証・再構築作業が増え停止判断に至った事例

2026年8月4日にCodex上で行った、作成者への振り返り質問と回答を、公開可能な
範囲へ一般化して記録する。顧客、案件、組織、個人および内部資料を識別できる
情報は保存しない。

## 対象となった作業

Consulting提案書の作成に生成AIを利用した一件を振り返った。

従来、同種の提案書を手作業で作る場合は複数人で4〜5時間程度を要し、作成者本人の
作業は1〜2時間程度だった。今回の提案書と従来の提案書は同一内容ではなく、品質、
範囲および完成条件を揃えた比較ではない。

生成AIを利用した作業では、類似する提案資料と、それまでの対話記録を組み合わせて
Presentationを生成した。初稿生成は1時間未満だった。

## 生成後に発生した作業

作成者は、生成された提案書を逐語的に3時間Reviewした。指摘事項を伝えて修正を
依頼した後、生成物全体の見栄えが大きく変化したことから、部分修正ではなく全体が
再生成されたと認識した。再生成後も逐語的なReviewを3時間行った。

生成された提案書は手作業で作る場合より見栄えが良かった。一方、顧客価値を前面に
出す構成でありながら、この提案と具体的な顧客価値の接続、Project Scope、具体的な
活動および作業分担が十分に分からない状態だった。

作成者は、不足したScopeと作業分担を別途3時間かけて作成した。すでに提供済みの
資料と矛盾しないよう、多くのCross-checkが必要だった。この3時間は、二回の逐語的
Reviewに含まれない。

さらに別の担当者が、顧客が提案の必要性と具体的な活動を理解できるようにするため、
通常は作成しないSummary資料を3時間かけて追加した。

確認できた人間作業は、二回のReview 6時間、Scopeと作業分担の再構築3時間、
Summary作成3時間の合計12時間である。初稿生成の操作時間と、指摘を反映させるための
操作時間はこの12時間に含まれない。

## ContextとGuardrail

作成者は、再生成に備えてCriticalな内容をMarkdownのContextとして用意した。
そこには、提案書で避ける用語と使用する用語などのGuardrailも含まれていた。

再生成された提案書は、そのContextに記録された用語上のGuardrailに従わなかった。
生成時にContextが渡されなかったのか、渡されたが生成時に重視されなかったのかは
確認できない。

## 行った判断

作成者は、この結果を受けて提案書の生成AIによるPresentation生成を停止した。

再生成を試しても、顧客に届く具体的な書き方になるか不明瞭であり、具体的な活動、
Scopeおよび顧客が負う責務が生成物へ安定して含まれなかったことを理由としている。

この作業のOutcomeは顧客へ提案することであり、再利用可能なPresentation生成
Pipelineを構築することではない。そのため、Pipeline改善を継続するより、人間が
提案書作成と責任ある確認を引き受ける判断をした。

## この記録で確認できないこと

- 従来版と生成AI版で、同じ提案内容、品質、範囲および完成条件を比較していない
- Version履歴、作業時間記録、指摘一覧または生成時のPromptをRepositoryで確認していない
- Contextが実際に生成AIへ渡されたかを確認していない
- 顧客本人へ、理解度、価値、負担または優先順位を質問していない
- 生成を停止した後の提案作成時間または品質を、同一条件で比較していない
- 一件の記憶であり、他の提案、TeamまたはPlatform Serviceへ一般化できない

## 訂正履歴

### CR-20260804-200014

- corrected_at: 2026-08-04T20:00:14+09:00
- corrected_by: human:kijima
- target: 「対象となった作業」から「行った判断」までの生成担当者と後続担当者の関係
- correction: Presentationの生成と再生成はInterview回答者とは別の担当者が実施した。Interview回答者は生成物を受け取る後続担当者として、逐語的Reviewと不足したScope・作業分担の再構築を実施した。Summary資料はさらに別の担当者が作成した。
- reason: 元の記述では、Presentation生成と後続作業を同じ担当者が実施したように読めたため
