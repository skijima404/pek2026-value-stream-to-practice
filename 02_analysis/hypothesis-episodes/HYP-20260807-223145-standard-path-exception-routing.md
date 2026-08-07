---
id: HYP-20260807-223145-standard-path-exception-routing
type: hypothesis_episode
title: "組織が責任を持つ標準Pathと例外Routingは選択・説明・意思決定Riskを減らす"
content_language: ja
created_at: 2026-08-07T22:31:45+09:00
created_by: agent:codex
hypothesis_scope: practice
hypothesis_level: solution
status: reviewed
reviewed_at: 2026-08-07T22:44:02+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: low
knowledge_basis:
  - recorded_statement
  - practitioner_experience
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260802-230424-platform-choice-hidden-assumption
  - type: derived_from
    target: OBS-20260807-211650-vsm-problem-causal-ambiguity
  - type: derived_from
    target: RN-20260807-194919-platform-advisor-retrospective-iterative-problem-learning
  - type: tests
    target: HYP-20260802-230425-platform-choice-burden-value
---

# 仮説

Platform利用者へ複数の選択肢から自分で選ぶことを一律に求める代わりに、組織が
標準Platformと適用条件へ責任を持ち、標準Pathを外れる場合だけ、例外理由、制約、Risk、
必要なEvidenceおよび意思決定者へのRoutingを求めれば、利用者の比較、説明および
意思決定Riskを減らし、安全にApplication開発へ進みやすくなる。

## 知識の成立根拠

作成者は、自分でPlatformを選びたい利用者と、選択を負担と感じる利用者の両方に
接した`practitioner_experience`を記録している。Platform Advisorの感想戦には、
組織が責任を持つ標準Pathと、例外時だけEvidenceを揃えて適切な意思決定者へ相談する
対抗Solutionが`recorded_statement`として記録されている。

標準Path、Decision Rights、Accountabilityおよび例外Routingを一つのSolution Mechanism
として接続し、選択負荷と意思決定Riskの減少を置く部分は`reasoned_synthesis`である。
実在するPlatform ServiceでこのSolutionを比較した結果ではない。

## Mobiusでの位置づけ

`practice` scopeの`solution`

Platform利用者の一部が、選択肢より安全な標準Pathによる選択負荷軽減を重視するという
Value Hypothesisに対し、組織が標準Pathへ責任を持ち、例外だけを適切な判断経路へ
RoutingするSolutionを置く。

ContextualなPlatform Advisorは、利用者が比較して選ぶValueを扱う別のSolution候補である。
本EpisodeはAdvisorを否定せず、対象SegmentとDecision Rightsに応じて競合または併存する
対抗Solutionとして保持する。

## このRepositoryでの扱い

このEpisodeは、Platform Advisorの物語を振り返り、最初のProblemまたはValueの解釈が
外れた場合に、別のSolutionへ戻れることを説明するHypothesis Modelとして保持する。
物語内のTeamが実際に標準Pathと例外Routingを検証した結果ではない。

現在、このRepositoryで本Episodeの検証を実施する予定はない。以下のValidation
Componentと検証方法は、物語世界の因果と未確認事項を明示し、将来別のScopeで
参照または比較する場合に再利用できる設計である。`not_tested`は、否定、検証待ちの
作業、または登壇内容への採用を意味しない。

## 期待する兆候

- 利用者が、候補比較より標準Path、適用条件および例外時の相談先を求める
- 標準条件に合う利用者が、比較資料作成や繰り返しの合意形成なしで次へ進める
- 標準Pathを外れるCaseだけが、理由、制約、RiskおよびEvidenceとともにRoutingされる
- 選択の正当性と説明責任を利用者個人ではなく、権限を持つ組織Actorが引き受ける
- 誤適用、差し戻し、Supportおよび例外対応が、選択負荷の減少と引き換えに増えない

## 反証またはChallengeとなる兆候

- 対象利用者の大半が、自分で比較し選択できることをValueとしている
- 標準Pathが利用者Contextへ適合せず、誤適用、迂回または例外申請を増やす
- 例外Routingが新しい承認Queueとなり、判断Lead Timeと説明負荷を増やす
- 組織が標準Pathの更新、Risk、廃止および例外判断へ責任を持てない
- 選択負荷の原因がDecision Rightsではなく、Platformの品質、信頼または利用可能性にある

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | 標準Pathと適用条件が、対象利用者の比較、説明および合意形成負荷を減らす | critical | none | not_checked | unknown | unknown | 標準Pathあり・なしの選定行動、PT、LTおよび説明作業を比較していない |
| U2 | 標準Pathを外れるCaseだけを、必要なEvidenceとともに正しい意思決定者へRoutingできる | critical | none | not_checked | unknown | unknown | 例外の検知、必要Evidence、Routing精度および判断Lead Timeを確認していない |
| U3 | 組織が選択の正当性、更新、Riskおよび廃止へのAccountabilityを引き受けられる | critical | none | not_checked | unknown | unknown | Decision Rights、Owner、運営Capacityおよび責任受容を実在組織で確認していない |
| U4 | 選択負荷を減らしても、誤適用、差し戻し、Supportおよび例外対応の下流負荷が増えない | high | none | not_checked | unknown | unknown | 利用開始後のOutcome、下流作業およびPlatform Team負荷を追跡していない |

## 検証方法

以下は、将来このHypothesis Modelを実在するPracticeで検証する場合の方法候補であり、
このRepositoryにおける現在の実施計画ではない。

### 方法と対象範囲

- 方法:
  Platformを自分で比較した人、標準Pathを利用した人、選定へ関与しなかった人、
  標準Pathを外れた人へのInterviewと、実際の選定、合意形成、例外判断および利用開始の
  記録を組み合わせる。可能であれば、自由比較型案内と標準Path＋例外Routingを限定比較する。
- 対象・資料:
  未選定。特定のPlatform Advisor実装またはMandatoryな利用を前提にしない。
- 選定方法:
  選択へ関心が高い利用者だけに偏らず、標準Pathを受動的に利用した人、非採用者、
  例外Caseおよび意思決定者を含める。
- 実施規模:
  一つの標準Pathと少人数の異なる選択行動から開始する。

### GenAIの利用

- 利用内容:
  Interview Guide、標準適用Case、例外Case、Decision Rightsおよび下流Signalの整理を支援する。
- GenAIだけで実施しないこと:
  架空Personaの選好、架空のRouting結果または生成した組織構造をEvidenceとして扱う。
- 実際に確認した資料・記録:
  現時点ではrelationで示したRepository Nodeのみ。

## 結果

`not_tested`

### 実際に観測したこと

作成者は、Platformを選びたい利用者と、選択を負担と感じる利用者がいるという経験を
記録している。Platform Advisorの感想戦では、標準Pathと例外Routingが対抗Solutionとして
整理された。

標準Pathを実際に導入した場合の選択負荷、Decision Rights、例外Routing、下流負荷または
利用者Outcomeを確認した記録は、このEpisodeの検証Evidenceとして保存されていない。

## 解釈

このSolutionの中心は、技術情報を整理することだけではない。組織が標準選択へ正当性を
与え、利用者個人が抱えていた比較、説明および意思決定Riskを引き取ることである。

選択の自由は、必要な利用者へ提供するCapabilityになり得る。一方、全利用者へ比較作業を
要求すると、選択を望まない利用者へ作業とAccountabilityを戻す可能性がある。

## 限界

- 選定上の偏り:
  作成者の経験と架空Scenarioの感想戦を起点としており、対象Segmentを選定していない。
- 未確認の証拠:
  利用者行動、Decision Rights、例外Routing、総Costおよび利用開始後のOutcome。
- 一般化できない範囲:
  Expert User、高度な最適化が必要なCase、標準化が困難なPlatform Job。
- 残存リスクと影響を受ける判断:
  U1からU4を確認するまで、標準Pathを自由比較型案内またはPlatform Advisorより優先できない。
- このEpisodeは、標準Path、例外Routingまたは登壇内容の採用決定ではない。
- 記載した検証方法は将来の再利用候補であり、現在の実施予定を表さない。

## 公開安全性確認

- checked_at: 2026-08-07T22:44:02+09:00
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
