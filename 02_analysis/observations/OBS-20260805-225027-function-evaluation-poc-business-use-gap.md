---
id: OBS-20260805-225027-function-evaluation-poc-business-use-gap
type: observation
title: "本人Interviewで機能評価型AI PoCがBusiness活用判断へ接続しなかった事例が記録された"
content_language: ja
created_at: 2026-08-05T22:50:27+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-05T22:55:41+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - case_recollection
  - explicit_validation
relations:
  - type: derived_from
    target: RN-20260805-225026-ai-poc-business-use-interview
---

# 観察

## 知識の成立根拠

ある組織で実施された開発関連AIのPoCについて、その状況を説明した本人への直接
Interviewに基づく。目的を持って本人へ確認した活動を`explicit_validation`、保存した
回答を`recorded_statement`として扱う。

PoCのReport、計画、評価記録、意思決定記録または利用状況をRepositoryで確認して
いないため、過去の事例についての回答は`case_recollection`として扱う。Interviewを
直接行ったことを、PoC自体の`direct_observation`には変換しない。

## 根拠箇所

- `RN-20260805-225026-ai-poc-business-use-interview`の「Interviewで得た回答」
- 同Raw Noteの「この記録だけでは分からないこと」

## 根拠から直接言えること

Interview回答者は、ある組織で開発に関係するAIのPoCを複数実施し、AI Toolの
機能評価と機能Reportの作成を中心とするPoCが複数あったと説明した。

回答者によれば、それらのPoCから、社内でどのように利用するかという結論または
Businessでの活用方法を取り出せなかった。この状態を避けるAI活用方法およびPoCの
使い方が課題として残っていた。

## 既存Hypothesisへの射程

- Session ValueのU1に対しては、「AIで何を作り、どのようにBusinessへ活かすかを
  判断できない」という問題が一人への直接Interviewで確認されたため、
  `contextual`な`supports`となる。
- 価値選択と検証のPractice SolutionのU1に対しては、機能評価を実施した側では
  Business活用の判断更新へ接続できなかった一例になる。ただし、価値仮説と期待Signalを
  明示した比較Caseがないため、Solutionの効果については`inconclusive`となる。
- 下流のReview、手戻り、Supportまたは総Costを確認していないため、Practice Valueの
  Cost TransferまたはPractice SolutionのU2に対するEvidenceにはしない。
- Value Hypothesisを置く時間、Skill、調整または判断Costを確認していないため、
  Practice SolutionのU3に対するEvidenceにはしない。
- 本人が今回のSessionまたはAI Slopを流さない方法を聞きたいと回答した記録ではないため、
  Session ValueのU2には接続しない。

## 曖昧さと限界

- 一人への直接Interviewであり、PoCの一次資料または他の関係者の回答を確認していない。
- PoCの正確な件数、期間、対象、比較条件、Costおよび意思決定過程は分からない。
- 技術学習、Risk低減またはCapability確認としての別の価値を評価していない。
- Business活用判断へ接続できなかった原因を、機能評価型PoCだけへ帰属できない。
- Value HypothesisまたはOutcome-firstの方法を適用すれば改善したとは確認していない。
- 類似する話が多いという作成者の認識を、発生率または一般性のEvidenceへ使わない。

## 公開安全性確認

- checked_at: 2026-08-05T22:55:41+09:00
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
