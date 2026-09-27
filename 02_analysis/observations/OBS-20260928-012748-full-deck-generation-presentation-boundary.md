---
id: OBS-20260928-012748-full-deck-generation-presentation-boundary
type: observation
title: "完成Storylineからの一括生成比較で視線誘導とトーク・スライド境界の差が認識された"
content_language: ja
created_at: 2026-09-28T01:27:48+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-09-28T01:31:16+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - direct_observation
  - explicit_validation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260928-011537-slide-authoring-genai-retrospective
  - type: references
    target: OBS-20260924-223229-rehearsal-exposed-delivery-constraints
  - type: references
    target: OBS-20260924-223230-human-ai-slide-authoring-role-boundary
---

# 観察

## 知識の成立根拠

登壇後、公開済み37枚版に準拠する採用済みStorylineから、Codexが31枚のPDF、HTML、
発表者Noteを生成し、制作者が手作りの登壇資料との違いを確認した記録に基づく。実施内容と
本人の評価を`recorded_statement`、対話中に比較用生成を実行したことを`direct_observation`
として扱う。

完成資料を入力側に含む限定的な比較に対して、制作者が自分の制作判断との差を識別したことを
`explicit_validation`とする。視線誘導とトーク・スライド境界という差分へ整理した部分は
`reasoned_synthesis`である。Audienceへの効果、一括生成の優劣、初期段階から構成を発見する
能力を検証したものではない。

## 根拠箇所

`RN-20260928-011537-slide-authoring-genai-retrospective`の
「一括生成の比較実験をきっかけに見えたこと」、
「スライドとトークは、作りながら同時に変わる」および
「今回まだ分からないこと」。

## 根拠から直接言えること

- 比較用生成物は登壇後に作られ、実際の登壇には使われていない。
- 入力したStorylineは完成スライドから再構成されており、初期メモから構成を発見する試験ではない。
- 制作者は生成物を「綺麗」と評価した一方、手作りの資料では、どこを見てもらうかを考えて
  視線を誘導していたことに気づいたと述べた。
- 制作者は資料制作中、話してみてスライドを変え、表現を変えて話し方を変えていた。
  スライドから情報を外すことは、その内容を口頭で担うことや伝え方の変更につながると説明した。
- 本番では会場の空気、前方の参加者、直前のKeynoteを見て話し方を変えるため、選択余地を
  残す目的で、あえて曖昧なスライドにする場合があった。

この一件では、完成Storylineから整ったDeckを生成できることと、制作者が本番で使う
視線誘導や口頭説明との分担を決められることは、同じ完了条件ではなかった。

## 既存Analysisとの関係

`OBS-20260924-223229-rehearsal-exposed-delivery-constraints`は、通し説明により時間制約や
口頭で補う箇所が見えた事例を扱う。本Observationは、スライドの表現と口頭説明の境界が
制作中と本番まで動き、その境界が一括生成物との差として認識された事例を追加する。

`OBS-20260924-223230-human-ai-slide-authoring-role-boundary`は、実際の資料制作でAIと人間が
担った作業を扱う。本Observationの一括生成は登壇後の比較であり、実際に採用された制作支援と
区別する。

## 曖昧さと限界

- 生成物はRepo外へ移動されており、本Observationから成果物を再検査できない。
- 完成資料から再構成したStorylineを入力したため、完成資料の設計判断が入力へ循環している。
- Audience、独立Review者、理解度、記憶、行動、所要時間および比較条件を収集していない。
- 「綺麗」、視線誘導の差および境界の説明は制作者本人の定性的評価である。
- 早い段階の一括生成をRehearsalへ使う次回案は未実施で、この一件から有効性を判断できない。

## 公開安全性確認

- checked_at: 2026-09-28T01:31:16+09:00
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
