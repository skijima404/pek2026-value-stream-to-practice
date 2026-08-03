---
id: EXT-20260803-002840-previous-platform-engineering-talk
type: external_input
title: "前回登壇『Platform Engineeringはなぜスケールしないのか』"
content_language: ja
created_at: 2026-08-03T00:28:40+09:00
created_by: agent:codex
source_type: user_provided_file
original_filename: "Platform_Engineeringはなぜスケールしないのか.pdf"
asset: platform-engineering-why-it-does-not-scale.pdf
source_url: https://speakerdeck.com/skijima404/platform-engineeringhanazesukerusinainoka
provided_by: human:kijima
retrieved_at: 2026-08-03T00:28:40+09:00
retrieval_method: human_provided_file
changeability: externally_managed
license: unknown
input_sha256: 986cb79922f5d69efbdb6038cf37b8bb633bfffd94b5fdd678003660f9aa04a2
asset_sha256: 986cb79922f5d69efbdb6038cf37b8bb633bfffd94b5fdd678003660f9aa04a2
---

# 前回登壇『Platform Engineeringはなぜスケールしないのか』

## 位置づけ

今回のセッションに先行する公開登壇資料を、前回実際に説明した範囲を
確認するための一次資料として保存する。

このExternal Inputは、前回登壇内容と今回のセッション案の重複、連続性、
追加点を確認するために使う。前回の主張が正しいことや、今回も同じ内容を
採用することを自動的に確立するものではない。

添付PDFは29ページであり、利用者から公開SpeakerDeckと同じ前回登壇資料として
提供された。Repo格納時にPDF本文とレイアウトは変更していない。

## 資料内で確認できる構成

- 1〜7ページ:
  Platform Engineeringを組織変革として捉え、Kotterを使って失敗要因を整理する
- 8〜12ページ:
  「なぜやるのか」と負の連鎖を明確にし、利用者、Platform Team、経営の問題を
  接続する
- 13〜20ページ:
  Platform as a ProductとしてPersona、Value、Scope、提供資産を定義し、
  対象Journeyを選別して仮説文へ落とす
- 21〜25ページ:
  Quick Win、Enablement、Adoption、相手の視点へ接続する説明を扱う
- 26〜28ページ:
  全体のまとめと失敗パターンRepositoryを紹介する

## 前回と今回の境界

前回登壇の中心は、Platform TeamのVisionを作り、価値を届ける対象Journeyを
特定するところまでである。

- Solutionから始めず、利用者の問題と期待する価値を明確にする
- Valueに合わせてPlatform ServiceのScopeを決める
- 繰り返し使う提供資産を選別し、案を無制限に増やさない
- Personaを開発者に固定せず、実際のJourneyと意思決定者を見る
- TeamのVisionと対象Journeyを特定する

今回のセッションは、そのJourneyを特定した後を扱う。対象Journeyの流れと
Actor間の境界を観測し、どこへAIを配置するか、局所的な高速化が全体のOutcomeへ
つながったか、新しい確認負荷や手戻りを生んでいないかを検証する。

したがって前回の内容は今回の前提であり、今回のセッション内で詳しく再説明する
対象ではない。初見の参加者が今回の開始地点を理解するために必要な範囲だけを
短く示す。

## 前回資料内では明示的に確認できなかった範囲

PDFの記載内容からは、次の論点は明示的には確認できなかった。

- VSMまたはMBPMを使ったActor間のProcess Time、Lead Time、手戻りの観測
- AIによる生成高速化と、下流へ移る確認・修正負荷
- GenAIによるReasoning Chain強度チェック
- AI Slopを受け手側の経験またはコスト外部化として扱う整理
- Release前の価値選別と、Release後のハンドオーバー観測を組み合わせる判断フロー

ここで確認できなかったことは、登壇時に口頭で一切触れなかったことを意味しない。
このExternal Inputが保存しているのは、提供されたPDFで確認可能な範囲である。

## VSM・MBPMの作成タイミングとの関係

前回資料では、利用者の問題、Value、Scope、提供資産を定義し、TeamのVisionと
対象Journeyを特定するところまでを扱っている。一方、そのJourneyをVSM・MBPMへ
展開し、Current Stateと施策後の変化を比較するところまでは明示されていない。

今回のVSM・MBPMは、前回の「なぜやるのか」「誰のどのJourneyを対象とするか」が
決まった後に作成する。そのJourneyのCurrent StateをActorとProcessへ分解し、
ProblemやValue Hypothesisを観測可能にして、施策の対象と効果を確認するための
追加的な実践として位置づける。

## 出典

- 公開資料:
  https://speakerdeck.com/skijima404/platform-engineeringhanazesukerusinainoka
- Repo内PDF:
  `platform-engineering-why-it-does-not-scale.pdf`
