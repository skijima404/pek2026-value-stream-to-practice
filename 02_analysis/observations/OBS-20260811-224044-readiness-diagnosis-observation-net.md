---
id: OBS-20260811-224044-readiness-diagnosis-observation-net
type: observation
title: "AI Readinessの中心は成熟度測定ではなく混乱への事前診断と観測網である"
content_language: ja
created_at: 2026-08-11T22:40:44+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-11T22:49:00+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - reasoned_synthesis
relations:
  - type: derived_from
    target: RN-20260811-224043-readiness-diagnosis-observation-net
  - type: derived_from
    target: OBS-20260811-221400-ai-readiness-as-system-adaptation
  - type: references
    target: OBS-20260731-120412-value-and-slop-experience-decision-flow
---

# 観察

## 知識の成立根拠

`RN-20260811-224043-readiness-diagnosis-observation-net`には、実践者がReadinessの中心意図を、
組織の成熟度を測ることではなく、組織状態によってAI導入後の適応期間または混乱の大きさが
変わり得ることを前提に、事前診断と観測の「網」で効率的な対処を準備することだと明示した
コメントが記録されている。これを`recorded_statement`として扱う。

`OBS-20260811-221400-ai-readiness-as-system-adaptation`には、Outcome、Value Flow、Verificationと
Pipeline、Platformと責任、Data and Knowledge Curation、InteractionとSensingという診断候補軸と、
一律の成熟度Gateにしない境界が記録されている。

事前診断をBaseline、観測点、Signal、Trigger、Ownerおよび対処Optionへ分解し、検知から適応までの
時間をReadinessのOutcome候補として置く部分は`reasoned_synthesis`である。

## 根拠から直接言えること

実践者の意図では、Readinessの成果は、組織状態をScore化することではない。AI導入後に起こり得る
適応期間の長期化または混乱へ備え、事前に状態を診断して観測網を置くことで、問題が現れた時に
効率的に対処できる状態を作ることである。

MBPMは、この観測網を作るために、Actor、Process、Handover、待ちおよび手戻りを具体化する方法
として位置づけられている。

## 今回の整理として導けること

観測の「網」は、少なくとも次の構成要素へ分けられる可能性がある。

1. Current StateとBaseline:
   AI利用前のActor、Process、Handover、Process Time、Lead Time、待ち、手戻り、確認負荷および
   `% Complete & Accurate`
2. Likely Constraint:
   AIでVolumeまたはSpeedが変わった時に負荷が現れそうな下流工程、承認、責任境界、Data、
   Knowledge SystemまたはTeam間Interaction
3. Signal and Trigger:
   Queue、Waiting Time、Clarification、Correction、Backflow、Verification CostまたはOutcome低下の
   どれを、どの変化で対処開始のTriggerとするか
4. Owner and Response:
   誰がSignalを見て、利用範囲変更、Capacity追加、Pipeline変更、Guardrail、支援、保留または
   停止を判断するか
5. Feedback:
   対処後に同じSignalを再観測し、次に露出した制約へ更新するか

この整理では、Readinessを「問題が起きない状態」ではなく、「問題が起きた時に、どこを見て、
誰が、どのOptionを判断するかを事前に準備した状態」として検証できる。

MBPMはCurrent State、Actor間HandoverおよびProcess上のSignalを置くことに適する。一方、Business
Outcome、最終成果物の品質、原因構造、Data and Knowledge CurationまたはArchitecture上のRiskを
MBPMだけで判定できるとは限らず、必要に応じて別の観測または判断を接続する必要がある。

## 曖昧さと限界

- 組織状態がAI導入後の適応期間または混乱の大きさへ影響する因果関係を確認していない。
- 「長引く」「混乱が大きい」「効率的に対処する」を表すSignalと比較単位を確定していない。
- 事前診断によって、未知の制約をどこまで予測または早期検知できるか確認していない。
- 観測網がある場合とない場合のTime to Detect、Time to Decide、Time to Adaptまたは総Costを
  比較していない。
- MBPMの作成・維持Costと、早期対処による回避効果を比較していない。
- 本ObservationはMBPM、Readiness診断、組織変更または登壇内容の採用を意味しない。

## 公開安全性確認

- checked_at: 2026-08-11T22:49:00+09:00
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
