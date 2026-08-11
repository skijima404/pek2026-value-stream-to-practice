---
id: ADR-0002
status: accepted
date: 2026-08-11
decision_scope: repository-architecture
---

# Lightweight Hypothesis Validationを標準にする

## Context

このRepositoryはHypothesisを厳密に分解し、Evidence Coverage、Finding、Applicability、
残存リスクおよびHuman Risk Decisionを分離できる。一方、30分の登壇準備で扱う小さな
仮説すべてにこの拡張形式を適用すると、学習より記録と判断管理の負荷が大きくなる。

Mobius Outcome Deliveryでは、Experiment、Research、Interviewのいずれかで次の学びへ
進める。今回のRepositoryでも、検証の厳密さを失わず、意思決定に必要な範囲へ作業量を
比例させる必要がある。

## Decision

通常のHypothesis EpisodeはLightweight形式とする。

- 現在の学習Stepでは`experiment`、`research`、`interview`から一つを選ぶ。
- 学習したい問い、前へ進むSignal、実施範囲、実際の観測、結果、主要な限界を記録する。
- 結果とは別に、`proceed`、`revise`、`validate_further`、
  `stop_for_current_scope`のいずれかで現在Episodeの扱いを決める。
- Research資料の著名さをEvidence品質とみなさず、資料が支えられる主張と適用範囲を
  記録する。
- Validation ComponentsとEvidence Coverageは、複数の重要な不確実性を別々に扱う場合だけ
  追加する。
- Risk Decisionは、Extended Componentに残る重要な不確実性がArtifact採用などの現在判断へ
  影響し、人間が正式な対応を決めた場合だけ作成する。

既存のExtended Hypothesis Episodeは履歴として維持し、Lightweight形式へ機械的に
書き換えない。

## Consequences

### Positive

- 小さな仮説を短い学習Cycleで進められる。
- 登壇準備の規模に対して、記録とRisk管理の負荷を比例させられる。
- 重要な主張には従来のExtended形式とRisk Decisionを引き続き使用できる。
- 既存HYPのComponent ID、Review状態および検証履歴を保持できる。

### Negative

- 既存HYPと今後のHYPで本文構造が異なる。
- Lightweight HYPへ正式なRisk Decisionが必要になった場合、先にExtended Componentを
  追加して人間Reviewを行うStepが必要になる。
- Approachを本文に記録するため、古いHYPには値が存在しない。

## Revisit conditions

- Lightweight HYPで重要な不確実性を見落とす事例が繰り返し発生する。
- Risk DecisionのためにExtended化する作業が通常化する。
- Experiment、Research、Interview以外の独立したApproachが継続的に必要になる。
- 30分登壇を越えて、継続的なProductまたはPlatform運営へRepositoryの目的を変更する。
