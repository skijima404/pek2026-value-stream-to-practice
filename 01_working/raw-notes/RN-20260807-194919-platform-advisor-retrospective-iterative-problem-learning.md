---
id: RN-20260807-194919-platform-advisor-retrospective-iterative-problem-learning
type: raw_note
title: "Platform Advisor感想戦と反復的なProblem理解"
content_language: ja
created_at: 2026-08-07T19:49:19+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-07T20:39:43+09:00
sanitization_checked_by: agent:codex
tags: [platform-advisor, retrospective, problem-understanding, iterative-learning, blind-spot, value-hypothesis, decision-rights, standard-path, selection-bias, development-value-stream]
---

# メモ

## このメモの位置づけ

Platform Advisorの物語を最後まで構成した後、作者の立場から振り返って見えたBlind Spotと、Problem理解を反復的に改善する必要性を記録する。

以下は物語内のPlatform Teamが最初から認識していた内容ではない。物語の後から棋譜を見直す感想戦として、当時の判断を責めるのではなく、次にどのような問いと観測を追加できるかを考える。

## 丁寧に進めてもProblemを取り違え得る

物語内のPlatform Teamは、思いつきだけでPlatform Advisorを選んだわけではない。

- VSMとMBPMでCurrent Stateを可視化した。
- 情報探索、問い合わせ、比較検討、合意形成および利用方法調査のPTとLTを整理した。
- Solution Optionを複数挙げた。
- Solution Prototypeを比較した。
- 導入後のPT・LTと下流の手戻りを観測する計画を置いた。
- AI SlopによってCostが後工程へ移転しないよう、Quality Guardrailを置いた。

それでも、Platform Advisorが対象とするProblemとValueを取り違える可能性が残った。

この物語が示すのは、手順が雑だったことではない。VSM、MBPM、Reasoning Chain、Prototype比較および効果測定は、それぞれ異なる対象を確認している。各確認を丁寧に行っても、その確認対象に含めなかった前提は通り抜ける。

## 感想戦で見えた三つの前提

Platform Advisorは、少なくとも次の前提を置いていた。

1. 利用者はPlatformを自分で選びたい。
2. 利用者はPlatformを自分で選べる権限を持っている。
3. 利用者は選択結果の説明責任とRiskを引き受けたい。

VSMには、担当者が比較資料を作り、Project OwnerとのMeetingを調整し、合意を得る工程があった。これは単なる待ち時間だけでなく、Platform選択が開発者だけでは完結せず、意思決定権限と説明責任を別のActorと共有しているSignalでもあった。

しかし物語内のPlatform Teamは、この工程をPlatform Advisorの対象外となる後工程として扱い、意思決定権限の構造としては読まなかった。

また、Prototype比較の対象を過去にPlatformを採用したTeamとした。この対象はPlatform選択へ関与し、Platformを利用した経験を持つため、選択支援へ価値を感じやすい可能性がある。Platformを選ばなかった人、選定へ関与しなかった人、標準Pathを受動的に利用した人、および選択自体を負担と感じる人の視点は入りにくい。

## 利用者が本当に終わらせたいJob

当初のPlatform Advisorは、利用者のJobを次のように捉えていた。

> 自分のContextに適したPlatformを比較し、選択する。

感想戦では、別のJobが候補になる。

> 組織が責任を持つ安全な標準Pathで、Platform選定へ過剰な時間と説明責任を負わず、Application開発へ進む。

> 標準Pathを利用できない場合だけ、例外条件を整理し、必要なEvidenceとともに適切な意思決定者へ相談する。

利用者の一部、特に運用条件まで自分で最適化したいExpert Userは、比較材料、Trade-offおよび選択の自由を価値と感じる。一方、そのValueを全利用者へ一般化すると、選択を望まない利用者へ判断作業と責任を課すことになる。

選択の自由は、必要な利用者へ提供するCapabilityであって、全利用者へ要求する作業ではない可能性がある。

## 対抗Solutionとしての標準Path

このProblem理解に立つと、Platform Advisor以外のSolutionが見えてくる。

- 組織が標準Platformと適用条件を定義する。
- 標準Pathを選ぶ場合は、利用者が比較検討を繰り返さなくても合意形成できるようにする。
- 標準Pathを外れる場合だけ、例外理由、制約、Riskおよび必要なEvidenceを整理する。
- 意思決定権限と責任の所在を明確にする。
- Advisorを使う場合は、複数Platformから自由に選ばせるのではなく、標準Pathの適用確認と例外時のRoutingを支援させる。

標準Pathが提供するValueは、技術情報の提供だけではない。組織が選択へ正当性を与え、個人が抱えていた比較、説明および意思決定Riskを引き取ることである。

Platform Advisorが多数の選択肢を提示するだけなら、かえって開発者へ判断責任を戻す可能性がある。Advisorの回答を使っても、Project Ownerへ選択理由を説明する責任は開発者に残るためである。

## 最初のProblem理解が難しい理由

Problem理解では、観測された現象と、その現象を生む構造を区別する必要がある。

物語内では、情報探索、問い合わせ、資料作成およびMeeting待ちが観測された。しかし、それらが次のどの構造から生じているかは、Process Metricだけでは決まらない。

- 情報が不足または分散している。
- 選択肢が多すぎる。
- 利用者が判断に必要なSkillを持っていない。
- 利用者に意思決定権限がない。
- 選択結果のRiskと説明責任が個人へ偏っている。
- 組織が安全な標準Pathを提供していない。
- 承認者と利用者が異なるValueまたは制約を持っている。

同じVSMとMBPMを見ても、どの構造をProblemと読むかによってValue HypothesisとSolution Optionは変わる。

さらに、Teamが認識できるProblemは、参加者、Interview対象、過去の経験、現在の関心および言語化できる範囲に影響される。Unknown Unknownは、最初の分析時点で問いとして置くこと自体が難しい。

それくらい、最初にProblemの状況を正しく把握することは難しい。

## 最初からすべてを当てようとしない

仮説検証を用いても、最初から正しいProblem、ValueおよびSolutionをすべて特定できるわけではない。仮説検証は正解を保証する方法ではなく、外れ方を観測し、次の判断を更新できるようにする方法である。

初期段階では、次を明確にする。

- 現時点で何をProblemと解釈しているか。
- その解釈が依存する前提は何か。
- 何を観測すれば前提をChallengeできるか。
- 外れた場合に、どの判断を見直すか。
- Teamの視野に入っていないActorまたは利用者Segmentは誰か。

実装または限定導入後には、想定した成功Signalだけでなく、次も観測する。

- Advisorを利用しなかった人と、その理由。
- 利用したが意思決定へ使わなかった人。
- 標準Pathを望み、比較を避けた人。
- Project Ownerが合意または差し戻しに用いた判断基準。
- Advisor利用後に増えた説明、確認、Supportまたは例外対応。
- 想定していなかった利用方法と、利用されなくなった理由。

観測からUnknown Unknownの手掛かりが得られたら、Problem Statement、Value Hypothesis、Solution Hypothesis、対象ActorおよびMetricを更新する。

品質は、最初の分析を完璧にすることで一度に作るものではない。観測、解釈、仮説、実験および振り返りを繰り返し、Problem理解と意思決定の品質を上げていくものとして扱う。

## 感想戦の意味

後からBlind Spotを指摘することは簡単である。しかし、当時のTeamへUnknown Unknownを最初から認識するよう求めるのは現実的ではない。

感想戦では、当時の判断を失敗として断罪するのではなく、次を振り返る。

- どのSignalはすでに見えていたか。
- 当時はそのSignalをどのように解釈したか。
- なぜ別の解釈が候補にならなかったか。
- どのActorまたは利用者Segmentが確認対象から抜けていたか。
- 次回はどの問い、観測点および反証条件を追加できるか。

丁寧に進めても外すことはある。重要なのは、外したことを観測でき、ProblemとValueの理解へ戻り、次の仮説を更新できるDevelopment Value Streamを持つことである。

## 登壇用の短い説明案

> ここからは作者による感想戦です。物語内のTeamは、VSMとMBPMを作り、複数のSolutionを比較し、効果測定まで設計しました。それでも「利用者はPlatformを選びたいのか」「選べる権限があるのか」「その責任を負いたいのか」という前提を見落としました。最初のProblem理解は、それくらい難しいものです。最初からすべてを当てようとするのではなく、何を仮説として置いたか、何を観測すれば外れたと分かるかを決め、繰り返しながら理解の品質を上げる方が現実的です。

## 関連する記録

- `RN-20260806-014446-platform-advisor-business-goal-and-blind-spot`
- `RN-20260806-194532-platform-advisor-selection-vsm-and-mbpm`
- `RN-20260806-210946-platform-advisor-fictional-validation`
- `RN-20260807-123008-platform-advisor-effect-measurement-observation-rationale`
- `RN-20260807-140147-platform-advisor-story-solution-first-mobius`
- `RN-20260807-185019-solution-first-problem-statement-rationale-and-limits`
- `OBS-20260802-230424-platform-choice-hidden-assumption`
- `HYP-20260802-230425-platform-choice-burden-value`

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
