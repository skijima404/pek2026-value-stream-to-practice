---
id: RN-20260806-210946-platform-advisor-fictional-validation
type: raw_note
title: "Platform Advisorを選ぶ物語内検証の設定"
content_language: ja
created_at: 2026-08-06T21:09:46+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-06T21:14:29+09:00
sanitization_checked_by: agent:codex
tags: [platform-advisor, worked-example, fictional-scenario, hypothesis-validation, prototype-testing, user-research, selection-bias, value-hypothesis]
---

# メモ

## このメモの位置づけ

これはPlatform Advisorの通し事例のために、物語内で実施したことにする検証を記録した設定である。実在する検証の実施記録またはEvidenceではない。この詳細はPresentationに出さない可能性がある。

関連するRaw Note：

- `RN-20260806-194532-platform-advisor-selection-vsm-and-mbpm`
- `RN-20260806-205437-platform-selection-solution-options`

## 物語内の検証

Platform Teamは、そのPlatformを採用した3〜5 Team程度へInterviewし、直近のPlatform選択過程を確認する。

Interviewでは、次のようなVSM上の問題が確認されたことにする。

- 必要な情報が複数の場所に分散している
- Platform Teamへ問い合わせた後の回答待ちがある
- 利用者自身が比較資料を作る必要がある
- どのPlatformをどのような場合に使うべきかの判断が難しい

次に、同じPlatform選択Scenarioを使って、少なくとも次のSolution Optionを簡易Prototypeで比較する。

- FAQまたはドキュメント拡充
- Platformの選び方Flowchart
- Platform Advisorの会話Prototype

## 比較するSignal

- 標準Pathへ正しく到達できたか
- 判断に必要な時間
- 判断根拠を説明できたか
- Platform Teamへの追加質問数
- 利用者が次の作業へ進めると感じたか

## 物語内の結果と判断

Platform Advisorは利用者のContextに応じた質問を返せるため、FAQやFlowchartよりも短時間で候補の標準Pathへ到達し、参加者からも高く評価されたことにする。Platform Teamはこの結果を受け、Platform Advisorの開発を選択する。

## 確認できた範囲

この検証で確認できたことにするのは、次の限定的な範囲である。

> Platformを比較して選ぼうとしている利用者に対し、Platform Advisorが選択作業を支援できる可能性がある。

これはPlatform Advisorが実際のProjectの意思決定で継続的に使われること、既存システム運用費を削減すること、または利用者全体に価値があることを確認する結果ではない。

## 未確認のBlind Spot

InterviewとPrototype比較の対象は、過去にPlatformを採用したTeamに偏っている。次の対象は含まれていない。

- Platformを採用しなかったTeam
- Platformの比較を始めなかったTeam
- 標準Pathを受動的に利用したTeam
- Platformを自分で選びたいと思っていない利用者

そのため、「利用者はPlatformを自分で選びたい」というValue Hypothesisそのものは検証されていない。Platform TeamはInterviewとPrototype比較を実施したが、対象選定の偏りによってこのBlind Spotを見落としたことにする。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
