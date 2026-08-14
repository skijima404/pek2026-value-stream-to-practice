---
id: RN-20260813-223536-ai-innovation-pipeline-evidence-repository
type: raw_note
title: "AI Innovation PipelineとEvidence-preserving Repositoryの構造的対応"
content_language: ja
created_at: 2026-08-13T22:35:36+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-13T22:40:41+09:00
sanitization_checked_by: agent:codex
tags: [ai-native-workflow, control-plane, embedded-policy, evidence-infrastructure, handover, human-ai-collaboration, provenance, repository-design, safe]
---

# AI Innovation PipelineとEvidence-preserving Repositoryの構造的対応

## この記録の位置づけ

Platform Engineering Kaigi 2026の準備中に、Scaled Agile Frameworkの
`AI Innovation Pipeline`を読み、このRepositoryの設計思想との接点を
人間とCodexの対話で整理した。

記事の確認結果は、次のExternal Inputに保存している。

- `EXT-20260813-223151-safe-ai-innovation-pipeline`

以下の対応づけ、Repositoryの位置づけおよびPEKでの利用候補は、記事本文に
そのまま書かれた内容ではない。記事の構造と現在のRepository設計をCodexが
比較し、人間が基本的に採用して記録を依頼した対話上の解釈である。

このRaw Noteは、その解釈を今後比較、修正またはAnalysisへPromotionできる形で
残す。記事がこのRepositoryの設計を検証したこと、この整理が登壇へ採用されたこと、
または記載した対応関係が唯一の解釈であることを意味しない。

## 中心となる読み

このRepositoryの設計思想と強く重なるのは、単なる「AI活用」ではなく、
**AIが参加できる仕事の構造をどう作るか**という部分である。

記事の概念と、このRepositoryで対応すると考えた構造は次のとおりである。

| AI Innovation Pipeline | このRepositoryで対応すると考えた構造 |
| --- | --- |
| Intent・Specification・Context | 仮説、Scope、期待Signal、前提と限界 |
| Evidence | Raw Note、External Input、Observation、検証記録 |
| Insight | Evidenceから分離したHypothesisやPattern |
| Embedded Policies | `00_meta/`の契約、Schema、Promotion Policy |
| Auditable | Provenance、typed relation、変更履歴 |
| Controlled | Validation、Review条件、Adoption境界 |
| Owned | `created_by`、`reviewed_by`、判断主体 |
| Shared Platform / control plane | Repository構造、生成View、Validator |
| Workflow間のContext継承 | Intent・Decision・EvidenceをRelationで次Nodeへ渡す |

この表は名称が完全に同義であることを示すMappingではない。異なる対象と目的を持つ
二つの構造について、機能的に近い関係を比較した解釈である。

## EvidenceとInsightの分離

特にこのRepositoryらしいと感じたのは、記事がEvidenceを起きたことの記録、
InsightをEvidenceの分析から得る価値として区別している点である。

このRepositoryも、Sourceを保存しただけでは結論にせず、次のLayerを分けている。

```text
Raw Note / External Input
  -> Observation
  -> Hypothesis Episode
  -> Pattern
  -> Adopted Artifact
```

これは、記録、解釈、仮説検証、再利用可能な解釈および採用判断を分離するための
構造である。Evidenceを保存することと、そこから得たInsightを現在の正本として
採用することは同じではない。

## Hand-over ContractとしてのProvenanceとRelation

もう一つ強く重なるのは、Workflow間で成果物だけを渡さず、Intent、Current Version、
DecisionおよびEvidenceも運ぶという部分である。

これは単なるKnowledge Managementではない。次の人間またはAgentが「なぜそうなったか」を
最初から再構築せず、現在の判断に必要なContextを受け取れる状態を作る話である。

このRepositoryのtyped relationとProvenanceは、Source、Interpretation、Validation、
DecisionおよびAdoptionの接続を明示する。そのため、これらを人間とAgentの間で
判断Contextを引き渡すHand-over Contractとして読むことができる。

ただし、現在のRelation SchemaがあらゆるHand-overに十分であること、またはRelationを
記録すればContextの再構築が不要になることを確認したわけではない。

## Embedded PolicyとしてのRepository Contract

記事のEmbedded Policiesも、このRepositoryとの接点がある。

このRepositoryでは、Ruleを説明文として置くだけでなく、Schema、Validatorおよび
生成Viewへ落としている。次の変換を意図した構造と読める。

```text
Policyを文書化する
  -> Machine-readableな制約にする
  -> Workflow内で自動確認する
```

`00_meta/`のContractは、Epistemic Layer、Provenance、Relation、ReviewおよびAdoptionの
境界を定義する。Validatorは、その一部をRepositoryの状態に対して確認する。生成Viewは、
Source Nodeの宣言からNavigationを再構成する。

一方、すべてのPolicyがMachine-readableであるわけではない。公開安全性、解釈の妥当性、
人間の意図との整合およびEvidenceの適用可能性には、引き続き人間の判断が必要である。

## SAFeの記事との違い

SAFeの記事は、Product DevelopmentをFlowさせるためのOperating Modelを説明している。
一方、このRepositoryは、推論と意思決定の品質を保ちながらHuman-AI協業を成立させるための
Evidence Infrastructureとして設計されている。

したがって、両者は同一のPipelineではない。記事の構造は、このRepositoryを説明する
Vocabularyと比較対象を提供するが、このRepositoryの具体的なEpistemic Boundary、
Review Chronology、Risk DecisionおよびArtifact Adoptionの分離まで直接定義していない。

## Repositoryを説明する候補表現

このReferenceから得られる大きな補強として、次の説明候補を置く。

> このRepositoryは「AIにメモを読ませる仕組み」ではない。  
> Intent、Policy、Evidence、Insight、Decisionを明示的に運ぶ、
> AI-Native WorkflowのControl Planeである。

これは現時点の説明候補であり、採用済みArtifactではない。PEK本編の中心へ置くよりも、
Repositoryを紹介するAppendixまたはHuman-AI協業を説明する一枚で利用できる可能性がある。

## 残る確認事項

- この対応表が第三者にも理解可能か
- `control plane`という表現が、Repositoryの役割を過大に見せないか
- Evidence InfrastructureとKnowledge Managementの差を短く説明できるか
- AppendixまたはHuman-AI協業の一枚が、25分の本編を逸らさず価値を持つか
- 既存のHypothesisまたはObservationと重複せず、どこへ接続するのが適切か

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
