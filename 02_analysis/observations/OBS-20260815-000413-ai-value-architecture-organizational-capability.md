---
id: OBS-20260815-000413-ai-value-architecture-organizational-capability
type: observation
title: "AI Value Architectの広い責務を個人Roleではなく分担・移管可能な組織Capabilityとして扱う案が記録された"
content_language: ja
created_at: 2026-08-15T00:04:13+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-15T00:20:04+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - external_research
  - reasoned_synthesis
relations:
  - type: derived_from
    target: EXT-20260813-224814-safe-ai-value-architect
  - type: derived_from
    target: RN-20260814-234307-ai-value-architect-reading
---

# 観察

## 知識の成立根拠

Scaled Agileの公式記事は、AI Value ArchitectにAI TechnologyとBusiness Valueの接続、Coaching、
Responsible Integration、Data-driven Measurement、組織横断の調整、継続的改善およびAdoptionを
支える広い責務を置き、一人ではなく複数人で補完できるとしている。

`EXT-20260813-224814-safe-ai-value-architect`は記事の責務とLimitを保存している。
`RN-20260814-234307-ai-value-architect-reading`は、これを万能な個人Roleではなく、方法、成果物、
判断基準およびFeedback Loopを複数Roleへ分担・移管できる組織Capabilityとして構成する案を
記録している。記事の記述を`external_research`、読者の案を`recorded_statement`、責務Catalogから
組織Capabilityへ構成する部分を`reasoned_synthesis`として扱う。

## 根拠箇所

- `EXT-20260813-224814-safe-ai-value-architect`のRole、責務、複数人による補完、
  「この資料が支え得る範囲」、「PEKおよびRepositoryとの接続に関する境界」および「限界」
- `RN-20260814-234307-ai-value-architect-reading`の「Enterprise Architectureとの近さ」、
  「責務Catalogから方法論へ」、「Platform Engineeringなどとの分担」、
  「AI Value Architectを方法論Ownerとして読む」、「個人Roleから組織Capabilityへ」および
  「Capabilityとしての完成条件」

## 根拠から直接言えること

公式記事が挙げる責務は、技術設計だけでなく、Business Outcome、Adoption、Measurement、Coaching、
Responsible AI、Governanceおよび継続的改善へ広がる。記事は、すべてを一人が担う必要はなく、
複数人がRoleを補完できるとしている。

読書記録では、既存のEnterprise Architecture、Platform Engineering、Product／Domain Team、
Enabling TeamおよびGovernanceと責務が重なるため、Role名を増やすより、探索、導入、測定および
学習を分担可能な責務と反復Processへ落とす案を提示している。

その案では、初期のBootstrap Ownerが方法、成果物、判断基準および限定された実践を整えた後、
別の担当者が次のCycleを実行でき、学びをEnterprise ArchitectureとPlatformへ戻せる状態を
組織Capabilityの完成条件としている。

## 曖昧さと限界

- 記事はRoleの責務CatalogとGuidanceであり、RoleまたはCapability導入効果の比較Researchではない。
- 分担案、反復Process、成果物、Bootstrap Ownerおよび完成条件は読者側の構想である。
- 既存RoleとのAccountability競合、必要Capacity、Staffing Model、評価基準および移管条件は
  確認していない。
- 個人Roleより組織Capabilityの方がValue Realization、Adoptionまたは継続性を改善することは
  検証していない。
- 現在のPlatform Engineeringを中心とするScopeにどこまで含めるかは未決定である。
- このObservationはRole設計、組織変更または登壇内容の採用を意味しない。

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
