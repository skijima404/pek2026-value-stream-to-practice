---
id: HYP-20260802-230425-platform-choice-burden-value
type: hypothesis_episode
title: "Platform利用者の一部は選択肢より安全な標準Pathによる選択負荷軽減を重視する"
content_language: ja
created_at: 2026-08-02T23:04:25+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: value
status: reviewed
reviewed_at: 2026-08-02T23:18:14+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - practitioner_experience
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260802-230424-platform-choice-hidden-assumption
---

# 仮説

Platform利用者は一様にPlatformを選びたいわけではない。利用者の一部は、選択肢を
増やすことより、自分のContextで安全に利用できる標準Pathが示され、選択と説明の
負荷が減ることを価値とする。

## Mobiusでの位置づけ

`value`

誰がどのような選択負荷を持ち、どの変化を価値とするかに関するValue Hypothesis
である。Platform Advisorは、このValue Hypothesisを実現できるかを検討する複数の
Solution候補の一つであり、本Episodeでは採用しない。

## 期待する兆候

- Platform選定を避けたい、または負担と感じる利用者が存在する
- 利用者が求めるものとして、選択肢一覧より推奨Path、適用条件、例外時の相談先が
  挙げられる
- Platform選択へ関心が低い利用者でも、適切な標準Pathが示されると次の判断または
  作業へ進みやすくなる
- Platform Advisorを採用しなかった人へのInterviewから、選択支援の前提が外れた
  理由を確認できる

## 反証またはChallengeとなる兆候

- 対象利用者の大半がPlatformを自分で比較し、選べることを価値としている
- 選択を避ける理由が、認知負荷ではなく、Platformの品質、信頼、適用可能性の不足で
  ある
- 標準Pathを示しても、利用者の意思決定または行動に変化がない
- MandatoryなPlatform利用により、選択行動から価値認識を観測できない

## 検証方法

### 方法と対象範囲

- 方法:
  Platformを採用した人、比較後に採用しなかった人、選定へ関与しなかった人を含む
  少人数Interviewと、実際の選定または利用開始行動の記録を組み合わせる。
- 対象・資料:
  未選定。特定のPlatform Advisor実装を前提にせず、Platform選定Jobを扱う。
- 選定方法:
  選択へ関心が高い人だけに偏らず、非採用者または標準Pathを受動的に利用した人を
  含める。
- 実施規模:
  初期段階では異なる選択行動を持つ少人数に限定する。

### GenAIの利用

- 利用内容:
  Interview Guide、回答の分類、代替解釈、見落としている利用者Segmentの候補を
  整理する。
- GenAIだけで実施しないこと:
  架空Personaの回答を利用者Evidenceまたは検証結果として扱う。
- 実際に確認した資料・記録:
  現時点ではrelationで示したRepository Nodeのみ。

## 結果

`not_tested`

### 実際に観測したこと

作成者は、Platformを選びたい自身の経験と、選択を負担と感じる開発者へ過去に
接した経験を記録している。対象者の選定、Interview記録、利用行動、人数を確認
できるEvidenceは保存されていない。

## 解釈

このEpisodeは、Platform Advisorの価値を前提とせず、利用者が本当に行いたいJobが
「Platformを選ぶこと」なのか、「安全なPathで次へ進むこと」なのかをDiscoveryへ
戻して確認するための対抗的なValue Hypothesisである。

PEK2026の題材では、物語内のProject TeamがこのHypothesisに気づいていない状態から
始める。これは仮説発見を説明するScenario上の設定であり、検証結果ではない。

## 限界

- 作成者の個人的経験から形成されたHypothesisである
- 「選択負荷」と、その原因となる知識、権限、責任、信頼をまだ分離できていない
- 組織が利用をMandatoryにしている場合、選択したという行動を価値Signalにできない
- Platform AdvisorのSolution Hypothesis、Feature、Scenario詳細は本Episodeの対象外

## 公開安全性確認

- checked_at: 2026-08-02T23:18:14+09:00
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
