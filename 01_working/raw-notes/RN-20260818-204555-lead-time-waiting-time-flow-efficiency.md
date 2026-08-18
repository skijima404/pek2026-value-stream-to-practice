---
id: RN-20260818-204555-lead-time-waiting-time-flow-efficiency
type: raw_note
title: "Process Time短縮より待ち時間へ着目するLead Time改善"
content_language: ja
created_at: 2026-08-18T20:45:55+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-18T21:40:50+09:00
sanitization_checked_by: agent:codex
tags: [lead-time, waiting-time, process-time, flow-efficiency, value-stream-mapping, mbpm, resource-efficiency, platform-engineering, ai, presentation-planning]
---

# メモ

## このメモの位置づけ

実務上の説明に用いた図について、画像そのものを保存せず、図中の例と
説明したかった要点をテキストとして記録したもの。

数値は、Process Timeの短縮より待ち時間の削減がLead Timeへ大きく効く場合を
説明するための仮の値であり、特定組織の実測値ではない。このメモ自体も、
改善効果を検証したEvidenceではない。

## 図に置いたプロセス

図では、次の6工程を左から右へ並べた。各工程のProcess Timeは1時間とした。

```text
リクエスト
  ↓
承認
  ↓
技術面でのアセスメント
  ↓
コーディングとテスト
  ↓
検証
  ↓
デプロイ
```

図中の矢印で表した待ち時間は、VSMやMBPMでの扱いに合わせて、矢印の先にある
次工程のLead Timeへ含める。各工程の1時間のProcess Timeも、その工程の
Lead Timeの内数として扱う。

| 工程 | Process Time | その工程のLead Timeに含める待ち時間 |
| --- | ---: | --- |
| リクエスト | 1時間 | この図では記載なし |
| 承認 | 1時間 | 管理者が着手するまで1週間 |
| 技術面でのアセスメント | 1時間 | 技術リーダーが着手するまで2週間 |
| コーディングとテスト | 1時間 | 開発者が割り当てられるまで2週間 |
| 検証 | 1時間 | 検証担当者が着手するまで1週間 |
| デプロイ | 1時間 | オペレーション担当者が着手するまで1週間 |

たとえば「承認」のLead Timeは、管理者が着手するまでの待ち時間と、実際に
承認判断を行うProcess Timeから構成される。

```text
承認のLead Time
= 承認への着手待ち + 承認のProcess Time
```

この仮定では、実際に手を動かしている時間は合計6時間である一方、工程間の
待ち時間だけで合計7週間になる。

```text
Process Time
= 1時間 × 6工程
= 6時間

Waiting Time
= 1週間 + 2週間 + 2週間 + 1週間 + 1週間
= 7週間
```

## この図で表現したかったこと

このようなプロセスでは、一つの工程を1時間から50分へ短縮することに意識を
向けても、全体のLead Timeに対する効果は小さい。7週間かかっている流れから
10分だけ削減しても、利用者が体験する速さはほとんど変わらない。

一方、全体時間の大部分は工程間の待ち時間である。承認、担当者の割り当て、
引き渡し、Queueなどによって発生している待ち時間を直接減らせれば、Lead Timeを
より大きく短縮できる可能性がある。

```text
各作業を少しずつ速くする
  ↓
Process Timeは減るが、7週間の待ち時間はほぼ残る

待ち時間の原因を見つけて減らす
  ↓
利用者が体験するLead Timeを直接短くできる
```

したがって、Lead Timeを短縮したい時は、最初から各工程の作業速度だけを
改善対象にせず、まずProcess TimeとWaiting Timeの比率を見て、仕事がどこで
留まっているかを確認する。

## フロー効率

この関係を考える手掛かりとして、フロー効率を次のように置く。

```text
フロー効率
= Value-adding Time または Process Time ÷ Lead Time × 100
```

図では説明を単純化し、6時間分のProcess Timeを約1日、7週間を49日として、
次のように表現していた。

```text
1日 ÷ 49日 × 100
≒ 2%
```

ここでは、必要な活動と、その活動が始まるまでの待ちを分けて扱う。

- リスク評価や意思決定を実際に行っている時間は、Waiting Timeではなく
  Process Timeとして計上する。
- リスク評価や意思決定を担当する人が着手するまでの滞留は、Waiting Timeとして
  計上する。
- 担当者が他作業を処理しているために生じる順番待ちは、対象のValue Streamに
  価値を加えないQueueとして扱う。

特に最後の順番待ちは、人や設備を常に稼働させるリソース効率を優先した結果、
仕事が空くのを待つ状態になった可能性がある。個々のResourceが高い稼働率を
維持していても、対象の仕事は前へ進まず、フロー効率は悪化する。

したがって、約2%という値を見た時には、残りを一括して「必要な待ち」または
「無価値」と判定するのではなく、待ち時間の正体を深掘りする。必要な仕事は
Process Timeとして可視化し、その仕事が始まるまでに発生しているQueueを疑う。

フロー効率は、必要な統制や判断を削るための指標ではない。Lead Timeの大部分を
占める滞留について、どこで、なぜ仕事が止まり、どのQueueを短縮できるかを
調べる入口として使う。

## VSMとMBPM上での扱い

VSMやMBPMでこのプロセスを扱う場合、工程名だけを並べるのではなく、実際に
仕事を行っている時間と、次の仕事を開始できずに待っている時間を分けて記録する。

```text
必要な判断を行う
  → Process Time

判断担当者が着手するまで待つ
  → Waiting Time / Queue

判断結果を受け取った後、次工程の担当者が空くまで待つ
  → Waiting Time / Queue
```

MBPMではActor別のスイムレーンとProcess Stepへ分解することで、どのActor間の
ハンドオーバー後にQueueが生じているかを観測できる。Process Timeだけを
短縮する前に、Lead Timeの大部分がどのWaiting Timeによって構成されているかを
確認する。

この区別がないまま「承認に2週間かかる」とだけ記録すると、2週間すべてを
必要な判断時間だと誤認する可能性がある。実際の判断が1時間で、残りが着手待ち
なら、改善対象は判断の品質を落とすことではなく、Queue、優先順位、Batch、
役割分担、ハンドオーバー条件などにある。

## AIとPlatform Engineeringへの接続

AIによって「コーディングとテスト」の1時間を短縮しても、工程間に7週間の
待ち時間が残るなら、Value Stream全体のLead Time改善は限定的になる。

```text
AIで一つの作業を高速化する
  ≠
Value Stream全体が同じ割合で高速化する
```

Platform Engineeringでも、個々の作業を自動化するだけでなく、承認待ち、
担当者探索、環境待ち、レビュー待ち、運用への引き渡しなどを観測する必要がある。
Self-Serviceや標準パスは、作業時間の短縮に加え、不要なQueueやハンドオーバーを
減らせる場合にLead Timeへ大きく効く。

このため、AIやPlatform Serviceを配置する場所は、「どの作業を速くできるか」
だけでなく、「Lead Timeのどこを占めているか」「待ち時間の原因を変えられるか」
を見て決める。

## 再利用時の留意点

- 図の6時間を1日へ丸めているため、2%は概念説明用の概算である。
- 7週間を49暦日としている。営業日で計算する場合は値が変わる。
- Process TimeのすべてがValue-adding Timeとは限らない。厳密なフロー効率を
  求める場合は、分子に何を含めるかを明示する必要がある。
- 待ち時間を減らすこと自体が目的ではない。必要な統制や安全確認を失わずに、
  不要なQueue、Batch、引き渡し、再確認を見つける必要がある。
- この例は直列プロセスとして単純化しており、並行作業、手戻り、WIP、
  Calendar上の稼働時間は表現していない。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
