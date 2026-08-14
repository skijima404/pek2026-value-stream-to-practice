---
id: OBS-20260815-000412-ai-native-workflow-evidence-control-plane
type: observation
title: "EvidenceとInsightを分離し判断Contextを運ぶAI-Native WorkflowのControl Plane構造が整理された"
content_language: ja
created_at: 2026-08-15T00:04:12+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-15T00:20:04+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: medium
knowledge_basis:
  - recorded_statement
  - external_research
  - direct_observation
  - reasoned_synthesis
relations:
  - type: derived_from
    target: EXT-20260813-223151-safe-ai-innovation-pipeline
  - type: derived_from
    target: RN-20260814-020149-ai-innovation-pipeline-reading
  - type: derived_from
    target: RN-20260813-223536-ai-innovation-pipeline-evidence-repository
---

# 観察

## 知識の成立根拠

Scaled Agileの公式Guidanceは、AI Innovation PipelineをDiscover、Specify、Build、Validate、Releaseの
Lifecycleとし、AI-Empowered Workflows、Embedded Policies、Insights and EvidenceおよびShared
Platformsを共通Capabilityとして説明する。`EXT-20260813-223151-safe-ai-innovation-pipeline`は、
その構造とLimitを保存している。

二つのRaw Noteは、Guidanceの読後理解と、このRepositoryのEpistemic Layer、Provenance、Relation、
Review、Adoption境界、生成ViewおよびValidatorとの機能的対応を記録している。Repository内の
契約とDirectoryを実際に確認できる部分を`direct_observation`、Guidanceとの対応づけを
`reasoned_synthesis`として扱う。

## 根拠箇所

- `EXT-20260813-223151-safe-ai-innovation-pipeline`の「Pipelineを支える4つのComponent」、
  「AI-Empowered Workflowの品質」、「InsightsとEvidenceについて記事が述べていること」および
  「Shared Platformについて記事が述べていること」
- `RN-20260814-020149-ai-innovation-pipeline-reading`の「OutputはEvidenceも生み出す」、
  「Shared Platformは予想より広い」、「共通化とLocal Adaptation」および「この資料の利用価値」
- `RN-20260813-223536-ai-innovation-pipeline-evidence-repository`の「中心となる読み」、
  「EvidenceとInsightの分離」、「Hand-over ContractとしてのProvenanceとRelation」、
  「Embedded PolicyとしてのRepository Contract」および「SAFeの記事との違い」

## 根拠から直接言えること

公式Guidanceは、Evidenceを人間とAgentのAction、Decisionおよび利用DataのAudit Trail、Insightを
Evidenceの分析から得られるRoot Cause、HypothesisまたはBottleneckに関する理解として区別する。
Insightは次のIntentとContextへ戻され、Shared PlatformはWorkflow、Policy、Evidence、Insight、
DataおよびActorを接続する`control plane`として説明されている。

Workflow間のHand-overでは成果物だけでなく、Intent、Current Version、DecisionおよびEvidenceを
運ぶ必要がある。AI-Empowered Workflowには、Grounded、Connected、Controlled、Auditableおよび
Ownedという5つの品質が提示されている。

Repositoryの構造を確認すると、Raw Note／External Input、Observation、Hypothesis Episode、Pattern、
Adopted Artifactが分離され、`00_meta/`のContract、typed relation、Provenance、Human Review、
Risk Decision、Artifact Adoption、Validatorおよび生成Viewが別の責任を持つ。この構造は、
Evidence保存とInsight形成、検証結果、人間の判断および採用を同一状態へ潰さず、後続の人間または
Agentへ判断Contextを渡すことを意図している。

したがって、このRepositoryを「AIがメモを読む仕組み」ではなく、Intent、Policy、Evidence、
InsightおよびDecisionを明示的に運ぶAI-Native WorkflowのControl Planeとして説明する候補がある。

## 対応関係の境界

SAFeの記事はProduct DevelopmentのOperating Modelを説明し、このRepositoryは推論、Evidence、
Validation、Risk DecisionおよびAdoptionの境界を保存するWorkspaceである。両者は同一のPipelineでは
なく、`control plane`という表現は機能的な比較である。SAFeがこのRepositoryのSchemaまたは運用を
検証したわけではない。

## 曖昧さと限界

- Scaled Agileの記事はFramework Guidanceであり、記載構造の効果を比較したResearchではない。
- Repository ContractのすべてがMachine-readableではなく、公開安全性、Source適用可能性、
  人間の意図との整合および採用には人間の判断が残る。
- Relationを記録すれば、後続者が必要なContextを十分に再構築できるとは確認していない。
- `control plane`という表現が第三者へ過大な印象を与えないか、Evidence Infrastructureまたは
  Knowledge Managementとの差を理解可能に説明できるかは未確認である。
- このObservationは、Repository説明文または登壇Appendixへの採用を意味しない。

## 公開安全性確認

- checked_at: 2026-08-15T00:20:04+09:00
- checked_by: agent:codex
- result: `not_needed`
- scope:
  この分析ノードの本文、frontmatter、relationの組み合わせを、
  人間の意図Reviewを確定する時点で再確認した
- finding:
  顧客、案件、非公開の個人、商用条件、内部System、認証情報、再識別に
  つながる組み合わせは確認されず、本文の変更や削除は行っていない
- limitation:
  公開安全性の確認は、内容の正しさ、検証完了、採用を意味しない
