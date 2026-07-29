# pek2026-value-stream-to-practice

Platform Engineering Kaigi 2026 セッション「AI Slopを生まないPlatform
Service設計：価値仮説と効果測定ってどうやるの？」
の準備過程と、仮説検証の生ログを公開するためのリポジトリです。

このリポジトリは、完成した方法論だけでなく、短い気づきがどのように観察、
仮説、パターン、登壇成果物へ昇格したかを追跡可能にします。

## Raw Noteを追加する

1. `templates/raw-note.md` を
   `01_working/raw-notes/RN-YYYYMMDD-HHMMSS-short-slug.md` としてコピーします。
2. frontmatterを埋めます。本文は箇条書きや短文のままで構いません。
3. `python3 scripts/validate_repository.py` を実行します。

Raw Noteに最初から仮説や検証計画を書く必要はありません。後日、GenAIまたは
人間がRaw Noteを根拠として `02_analysis/` に派生ノードを作成します。元の
Raw Noteは移動・削除しません。

Raw Note、派生した分析、採用成果物の本文は日本語で記述します。frontmatter
のkey、enum、ID、relation typeは英語で固定します。原資料からの直接引用は
原文を維持できます。

## ディレクトリ

- `00_meta/`: 情報をどう扱うかを定める契約とschema
- `01_working/raw-notes/`: 低負荷で記録する原資料
- `02_analysis/`: observations、hypothesis episodes、patterns
- `03_artifacts/`: 採用された現在の成果物
- `10_external-inputs/`: CfPや登壇枠などの外部入力
- `templates/`: 新しいノードのテンプレート

重要な原則:

> Meta defines how truth is promoted; it does not define the truth itself.

セッション情報: [Platform Engineering Kaigi 2026 CfP](https://www.cnia.io/pek2026/sessions/c8d1236b-8a03-454c-80e3-063f57d858ba/)
