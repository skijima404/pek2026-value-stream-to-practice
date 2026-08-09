# 生成View

このディレクトリには、Repositoryの正本Markdownから決定論的に生成した、
GenAIおよびTool向けの機械可読Viewを置きます。

`repository-graph.json`は検索とrelation追跡を補助するProjectionであり、
Evidence、解釈、採用判断または現在の正本ではありません。Nodeの本文と正式な
状態は、JSON内の`path`が指すMarkdownを直接確認してください。

手作業で編集せず、次のCommandで再生成します。

```text
python3 scripts/generate_analysis_views.py
```
