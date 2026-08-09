---
id: ADR-0001
status: accepted
date: 2026-08-09
decision_scope: repository-architecture
---

# Markdownを正本としてGraph Projectionを生成する

## Context

Raw Note、Observation、Hypothesis Episode、Pattern、Risk DecisionおよびArtifactが
増えるにつれて、単一のAnalysis READMEへReasoning Chain、Hypothesis階層、
Evidence CoverageおよびNode一覧を集約する方法は肥大化しやすくなった。

このRepositoryはGenAIによる横断的な検索とrelation追跡を重視する。一方で、
主目的は高頻度のTransaction処理や任意のGraph Queryではなく、Markdownに保存した
原資料、解釈、検証および採用判断のTraceabilityを維持することである。

GraphDBを導入するとGraph検索を直接表現できるが、MarkdownとGraphDBのどちらを正本と
するか、同期失敗をどう扱うか、Schema Migration、運用Dependencyおよび公開時の
再現方法を追加で決める必要がある。

## Decision

Repository Markdownを唯一の永続的な正本として維持する。

既存Nodeのfrontmatter、typed relation、Hypothesis result、Validation Component、
Risk DecisionおよびArtifact metadataから、次の破棄可能なNavigation Projectionを
決定論的に生成する。

- 分割したAnalysis Markdown View
- `views/repository-graph.json`

JSON Graphは`projection.authority: none`を宣言し、Evidence、派生Claim、採用判断または
現在の正本として使用しない。GenAIまたはToolはGraphから候補Nodeと直接relationを
特定した後、対象Markdownを読んで解釈する。

現在の運用規則は`00_meta/analysis-projection-contract.md`を正本とする。

## Considered alternatives

### 単一のAnalysis READMEを手作業で維持する

採用しない。人間には読みやすいが、Node増加に伴って同じmetadataとrelationの転記が
増え、更新漏れとContext消費が大きくなる。

### GraphDBを永続層として追加する

現時点では採用しない。現在必要な検索は、決定論的なJSON ProjectionとSource
Markdownの読み取りで表現できる。第二の可変な永続層と同期規則を導入するだけの
実測上の必要性はまだない。

### Markdownを廃止してGraphDBを正本にする

採用しない。人間による原資料の記録、Git diff、公開、Correction履歴および
Repository単体での再現性という現在の目的と合わない。

## Consequences

### Positive

- Markdown、Gitおよび既存のReview Workflowを正本として維持できる。
- GraphDBを運用せず、Graph-shaped retrievalを利用できる。
- 生成物は削除してもSourceから再構築できる。
- Source digestと鮮度検証により、Projectionの同期状態を確認できる。
- 巨大な単一READMEを、小さな入口と目的別Viewへ分割できる。

### Negative

- 任意のGraph Queryには、JSONの走査または補助Toolが必要になる。
- Source変更後にProjectionを再生成する工程が増える。
- 複数Nodeのtitleとmetadataを集約するため、公開時には組み合わせによる再識別Riskを
  別途確認する必要がある。
- Repository-authored Navigation Viewと機械生成Viewの役割を区別して運用する必要がある。

公開安全性未確認のRaw Noteはfail-closedでProjectionから除外し、件数以外のmetadataを
複製しない。これにより、低負荷なCaptureを維持しながら、集約Projectionへの公開前情報の
流入を防ぐ。

## Revisit conditions

次のいずれかが実測上の問題になった場合、このDecisionを再検討する。

- Projection生成時間またはJSON走査時間が通常の作業を妨げる。
- GenAIのNode検索精度が、現在のmetadata Projectionでは不足する。
- 複数Writerによる同時更新やIncremental Updateが必要になる。
- 現在のJSON Schemaでは表現できないGraph Queryを継続的に使用する。
- MarkdownとProjectionの同期では満たせない外部Application連携が必要になる。

再検討時には、GraphDB導入だけでなく、Projectionの分割、検索Index、SQLite、
専用Query Toolなど、より小さい変更も比較する。
