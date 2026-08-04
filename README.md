# pek2026-value-stream-to-practice

Platform Engineering Kaigi 2026 セッション「AI Slopを生まないPlatform
Service設計：価値仮説と効果測定ってどうやるの？」
の準備過程と、仮説検証の生ログを公開するためのリポジトリです。

このリポジトリは、完成した方法論だけでなく、短い気づきがどのように観察、
仮説、パターン、登壇成果物へ昇格したかを追跡可能にします。

## Raw Noteを追加する

Codexで「ファイルくださいな」「Raw Noteをください」と依頼すると、ID・時刻・
provenanceを入力済みの空ファイルを作成します。

手動で追加する場合:

1. `templates/raw-note.md` を
   `01_working/raw-notes/RN-YYYYMMDD-HHMMSS-short-slug.md` としてコピーします。
2. frontmatterを埋めます。本文は箇条書きや短文のままで構いません。
3. `python3 scripts/validate_repository.py` を実行します。

人間が本文を追記した後に「このRaw Noteを仕上げて」と依頼すると、frontmatter
と安全なファイル名を内容に合わせ、顧客・案件・個人・内部システムなどの
公開できない情報を除去します。

Raw Noteに最初から仮説や検証計画を書く必要はありません。後日、GenAIまたは
人間がRaw Noteを根拠として `02_analysis/` に派生ノードを作成します。元の
Raw Noteは移動・削除しません。

Raw Note、派生した分析、採用成果物の本文は日本語で記述します。frontmatter
のkey、enum、ID、relation typeは英語で固定します。原資料からの直接引用は
原文を維持できます。

## 人間とAIの協業モデル

このリポジトリでは、AIが記録と構造化を支援し、人間が意味と採用判断を
保持します。

```text
人間とAIの対話
  -> Raw Noteとして由来を保存
  -> AIがAnalysisを作成（created_by: agent:codex）
  -> 人間が意図との一致を確認（status: reviewed）
  -> 仮説検証は別に記録
  -> 残存リスクへの対応を人間が判断（Risk Decision）
  -> 人間が現在の成果物として採用（adopted_by: human:kijima）
```

`status: reviewed` は、人間がAnalysisの内容を確認し、自分の意図を正しく
表していると判断したことを示します。事実確認、仮説の検証、公開安全性確認、
成果物への採用を意味しません。

複合仮説はHypothesis Episode内で小さな検証対象に分解できます。各対象について、
確認範囲、Evidenceが示す結果、対象条件への適用可能性、残存リスクを区別します。
残存リスクに対して先へ進む、追加調査する、軽減するなどの判断は
`04_decisions/risk-decisions/` に履歴として残します。この判断は仮説が真であることや、
成果物へ採用されたことを意味しません。

## ディレクトリ

- `00_meta/`: 情報をどう扱うかを定める契約とschema
- `01_working/raw-notes/`: 低負荷で記録する原資料
- `02_analysis/`: observations、hypothesis episodes、patterns
- `03_artifacts/`: 採用された現在の成果物
- `04_decisions/`: 残存リスクに対する人間の意思決定
- `10_external-inputs/`: CfPや登壇枠などの外部入力
- `templates/`: 新しいノードのテンプレート

重要な原則:

> Meta defines how truth is promoted; it does not define the truth itself.

セッション情報: [Platform Engineering Kaigi 2026 CfP](https://www.cnia.io/pek2026/sessions/c8d1236b-8a03-454c-80e3-063f57d858ba/)
