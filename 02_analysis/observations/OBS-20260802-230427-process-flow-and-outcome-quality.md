---
id: OBS-20260802-230427-process-flow-and-outcome-quality
type: observation
title: "Process上のFlowと最終成果物のOutcome Qualityは別の観測対象として記録された"
content_language: ja
created_at: 2026-08-02T23:04:27+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-02T23:18:14+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: high
knowledge_basis:
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260731-143326-mbpm-blind-spots-and-outcome-quality
  - type: references
    target: EXT-20260731-113601-mbpm-open-practice-library
---

# 観察

## 根拠箇所

- `RN-20260731-143326-mbpm-blind-spots-and-outcome-quality` の
  「最終成果物の品質はMBPM上で見えにくい」「Quality Assuranceは期待された体験と
  価値の充足を見る」「MBPM上でFlowが良くてもOutcomeは間違い得る」
- MBPMの用語Contextとして
  `EXT-20260731-113601-mbpm-open-practice-library`を参照する

## 根拠から直接言えること

作成者は、MBPMがActorごとのProcess、Handover、Process Time、Lead Time、
`% Complete & Accurate`などを通じて、次の摩擦を観測することに向くと記録している。

- 待ち、滞留、手戻り
- 確認、修正、追加作業
- Handover後の再作業または例外対応

一方、Processを通過した最終成果物について、次の状態はProcess上のFlowだけでは
直接判定しにくいと記録している。

- 利用者が必要とした内容またはServiceか
- 利用者のContextで判断または行動に使えるか
- 期待した体験、価値、信頼を満たすか
- Serviceが暗黙または明示に約束した責任境界と品質を満たすか
- 次も使いたい、参加したい、他者へ薦めたいと思えるか

作成者はこの違いを、Process Quality、Output Quality、Experience Quality、Trust
Quality、Contract Qualityとして分ける候補を記録している。また、Value
Hypothesisと期待Outcomeがなければ、Flowが改善しても正しい価値へ向かったかを
判定できないとしている。

## 曖昧さと限界

- Quality分類は人間とGenAIの対話で形成された候補であり、確立されたFrameworkの
  定義として確認されていない。
- MBPMで全く観測できないという主張ではない。利用後の反応をProcess Stepとして
  組み込むなど、MapのScopeによって観測可能性は変わる。
- Trust、Experience、Contractの具体的なMetricと判定基準は未定義である。
- Process QualityとOutcome Qualityが独立しているとは限らず、相互に影響し得る。
- このObservationは、測定方法または登壇構成としての採用を意味しない。

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
