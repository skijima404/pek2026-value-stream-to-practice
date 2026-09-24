---
id: OBS-20260924-223230-human-ai-slide-authoring-role-boundary
type: observation
title: "登壇資料制作でAIを探索・壁打ち・Review・記録へ使い、人間が選択と発話検証を担った一事例が記録された"
content_language: ja
created_at: 2026-09-24T22:32:30+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-09-24T22:35:46+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - direct_observation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260924-213546-ai-assisted-slide-authoring-interim-retrospective
  - type: derived_from
    target: RN-20260924-213546-closing-scope-enablement-and-repository-disclosure
  - type: derived_from
    target: RN-20260924-220725-personal-retrospective-slide-authoring-and-generation
  - type: references
    target: OBS-20260827-010635-ai-outcome-review-boundary
  - type: references
    target: HYP-20260805-001809-repository-handoff-preserves-focus
---

# 観察

## 知識の成立根拠

PEK2026の登壇資料制作における人間とAIの対話、Repositoryへの記録、PDF Review、画像候補の
検討、通し説明および作成者本人の総括に基づく。実施内容と本人の説明を`recorded_statement`、
このRepositoryと会話に保存された制作上の往復を`direct_observation`として扱う。

個々の往復を、AIが支援したOutcomeと人間が保持した判断へ整理する部分は
`reasoned_synthesis`である。この役割分担が最適である、またはAIによって制作が効率化した
という因果は置かない。

## 根拠箇所

- `RN-20260924-213546-ai-assisted-slide-authoring-interim-retrospective`の
  「AIを何に使ったか」、「具体的な往復」および
  「確認できた変化と、まだ測っていない効果」。
- `RN-20260924-213546-closing-scope-enablement-and-repository-disclosure`の
  「Repo紹介とAI利用の説明」。
- `RN-20260924-220725-personal-retrospective-slide-authoring-and-generation`の
  「Repoに徹底的に蓄積してみたかった理由」、
  「生成で難しいと感じること」および「それでも、面白いから試してみたい」。

## 根拠から直接言えること

今回の制作では、AIが少なくとも次の用途に使われたと記録されている。

- 過去のRaw Note、Observation、外部Sourceおよび説明候補の検索・再発見。
- 構成、因果、比喩、文言および代替案についての壁打ち。
- PDFまたは画像を対象とした、誤読、飛躍、測定対象のずれおよび配置のReview。
- 会話のRaw Note化、relation、Review状態、公開安全性およびRepository構造の確認。
- 別の画像生成対話を含む、バトンパス等の画像候補の作成支援。

人間は、持ち帰ってもらう核、組織目的、説明したい比喩、残す案と外す案、実際のスライド編集、
最終表現および通し説明を担った。AIの提案は全件採用されず、検索結果、構造検証または画像生成の
完了を、内容の正しさやAudienceへの効果とは扱っていない。

作成者は、固定したい表現と変更指示が蓄積すると、どの指示が現在も有効かを人間でも追いにくく、
AI側の精度も落ちると感じたと述べた。一方で、今回の過程を外部から眺め、将来のスライド生成に
つなげることへ関心を示している。これは使用感と今後の関心であり、精度低下または改善方法を
比較した結果ではない。

## 既存Analysisとの関係

`OBS-20260827-010635-ai-outcome-review-boundary`は、機能要件のTraceabilityを担うIntentへ
異なるAI Outcomeを混ぜず、Review境界を分けた一件を扱う。本Observationは、実際の登壇資料
制作でAIを複数のOutcomeへ使い、人間の選択と発話検証を残した一件を追加する。

`HYP-20260805-001809-repository-handoff-preserves-focus`は、Human-AI協業の説明を限定し、
Repositoryへの導線で深掘りを提供できるかを扱う。本ObservationはRepositoryを制作に使った
事実を示すが、Audienceが導線を理解または利用した結果ではないため、同Hypothesisの結果を
変更しない。

## 曖昧さと限界

- 全Prompt、AI Output、編集操作、採否理由および画像生成の試行回数を収集していない。
- 制作時間、AI利用時間、Review Cost、比較対象、費用および品質差を測定していない。
- 人間の着想とAI提案が相互に影響した箇所を、すべて独立に帰属できない。
- 作成者本人と制作を支援したAIによる記録で、第三者によるProcess監査ではない。
- この一件から、同じ役割分担が他の作成者、資料またはAI Systemでも有効とは一般化できない。

## 公開安全性確認

- checked_at: 2026-09-24T22:35:46+09:00
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
