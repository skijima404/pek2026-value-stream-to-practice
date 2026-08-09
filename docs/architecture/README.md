# Repository Architecture

このディレクトリには、このRepositoryを運営する仕組みのArchitectureと、
その設計判断の履歴を置きます。登壇内容、Evidence、Hypothesisまたは採用済みの
登壇成果物を置く場所ではありません。

## Current operating truth

現在のAgent動作、Provenance、Promotion、RelationおよびProjectionの規則は
`00_meta/`を正本とします。このディレクトリのADRは、現在の規則を決めた理由を
説明しますが、現在の運用契約を上書きしません。

## Architecture Decision Records

`decisions/`には、Repository Architectureに関する重要な判断を保存します。

- ADRは、判断時点のContext、検討した選択肢、決定、結果および再検討条件を記録する。
- 現在の実装または運用規則は、ADRではなく`00_meta/`とSource Codeで確認する。
- 後続判断で置き換える場合は、古いADRを削除せず`superseded`として参照関係を残す。
- セッション内容の採用判断やHypothesisの残存リスク判断をADRへ記録しない。

## Records

- [ADR-0001: Markdownを正本としてGraph Projectionを生成する](./decisions/ADR-0001-markdown-source-with-generated-graph-projection.md)
