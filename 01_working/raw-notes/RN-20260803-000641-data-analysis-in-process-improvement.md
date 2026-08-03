---
id: RN-20260803-000641-data-analysis-in-process-improvement
type: raw_note
title: "プロセス改善におけるデータ分析"
content_language: ja
created_at: 2026-08-03T00:06:41+09:00
content_origin: human_direct
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-03T00:22:11+09:00
sanitization_checked_by: agent:codex
tags: [data-analysis, metrics, observability, dashboard, business-intelligence, process-improvement, anomaly-detection]
---

# メモ

メトリックの分析について。

メトリックの分析はなるべく頻度を確保できるよう
- 違和感の抽出がなるべく労力なく行えるように
  - 入力の手間の削減 (手入力は基本入れられなくなるものと思った方が良い)
  - データ加工から実際に違和感の検知ができるまでのレポート作成のための工数削減

分析ツールの活用は2段階で考える。
- ダッシュボード
  - 「なんかおかしい」という違和感が検知できる仕掛けとして活用
  - ここには分析の柔軟性を求めない
- BIツール等
  - ここは取得できるデータを使って違和感の正体を見つけるための工程
  - 柔軟にデータを組み合わせて分析できる必要がある

## ダッシュボード
- 最初から作り込みすぎない
  - ダッシュボード作り始めるとメトリックをひたすら取ってしまい、重要なポイントがわからなくなるので、必要最小限にする。
    - Bad Practiceを脱した事例: [カルビーの事例](https://www.getgamba.com/guide/archives/6152/)

## BIツール等
- 違和感を検知したら、なぜ違和感を感じたかを深掘りするため、カスタムレポート等を作って特定
- 具体的な方法論や深掘り方は一般的なデータ分析のやり方を参照。ここでは深掘りしない
  - というより具体例がないとやりづらい
  - Platform Advisorの例で分析ユースケースを紹介するかは後で判断

## 分析手法Tips
- 時間の長さ等は平均で見るよりは分布で見た方が違和感検知しやすい
- 平均を見たい時はないわけではない。平均の推移 (全体的に下がっている、など) を見たい時などが考えられる
- どんなJourneyも一律で見ようとすると焦点がぼやけて違和感を見つけづらい。あらかじめJourneyごとなどでフィルタリングできるようにすると良い


## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
