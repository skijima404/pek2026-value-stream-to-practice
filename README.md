# pek2026-value-stream-to-practice

Platform Engineering Kaigi 2026 セッション「AI Slopを生まないPlatform
Service設計：価値仮説と効果測定ってどうやるの？」
の準備過程と、仮説検証の生ログを公開するためのリポジトリです。

このリポジトリは、完成した方法論だけでなく、短い気づきがどのように観察、
仮説、パターン、登壇成果物へ昇格したかを追跡可能にします。

## Raw Noteの位置づけ

`01_working/raw-notes/` には、検討時点の発言、対話、調査メモなどの原資料を
保存します。

Raw Noteの `Raw` は、文章の粗さや人間による直接執筆を意味しません。人間と
GenAIの対話を整理した文書も、後から追加した解釈ではなく検討時点の記録で
あればRaw Noteとして扱います。

Raw Noteの記述は、検証済みの事実や現在採用されている結論ではありません。
Observation、Hypothesis Episode、Pattern、Artifactへの派生関係と、それぞれの
状態を確認してください。

Raw Noteから派生ノードが作られても、原資料は移動・削除しません。誤りが
判明した場合も原文を消去せず、Correctionによって訂正範囲を記録します。

Raw Note、派生した分析、採用成果物の本文は日本語で記述します。frontmatter
のkey、enum、ID、relation typeは英語で固定します。原資料からの直接引用は
原文を維持できます。

## GenAIでこのRepositoryを読む場合

このRepositoryは単一文書の要約ではなく、複数ノード間のprovenance、typed
relation、`session` と `practice` のscope、Hypothesis階層、Evidence Coverage、
残存リスク、Human Risk Decisionを横断して解釈することを前提としています。

Repository全体のSynthesis、Hypothesis構造の解釈、Pattern抽出、または設計意図の
説明には、複数ファイル間の関係を追跡できる推論モデルと、十分なコンテキスト
および推論設定を使用することを強く推奨します。最新世代のモデルであること
自体は必須ではありません。

高速・軽量・推論量を抑えたモデルでは、もっともらしい文章を生成できても、
次の誤りが生じる可能性があります。

- `session` と `practice` のHypothesis階層を混同する
- 子Hypothesisの結果を親Hypothesisへ推移させる
- 経験知を「根拠なし」または独立検証済みとして扱う
- Evidence Coverageを仮説の正しさの割合として扱う
- Human Risk Decisionを仮説の支持またはArtifact採用として扱う
- ファイルをまたぐrelationやCorrectionを取り落とす

使用するモデルがRepository全体のSource graphを安定して追跡できない場合は、
解釈対象を単一ノードとその直接relationへ限定してください。

モデルの性能にかかわらず、GenAIによる説明はEvidence、人間による意図確認、
公開安全性確認、またはRepository上の採用判断を代替しません。

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
