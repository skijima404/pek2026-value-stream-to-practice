---
id: RN-20260807-185019-solution-first-problem-statement-rationale-and-limits
type: raw_note
title: "Solution-firstでProblem Statementを再構成する理由と限界"
content_language: ja
created_at: 2026-08-07T18:50:19+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-07T18:54:51+09:00
sanitization_checked_by: agent:codex
tags: [solution-first, problem-statement, reasoning-chain, vsm, mbpm, generative-ai, cognitive-bias, facilitation, platform-advisor]
---

# メモ

## このメモの目的

Platform Advisorの通し事例で使用した、Solution候補からProblemとValueを遡って再構成する方法について、採用する理由、具体的な進め方、GenAIの役割および方法上の限界を整理する。

このメモは方法の解説であり、Solution-firstが他の方法より優れていることを検証した結果ではない。

## 前提となるDomain Knowledge

Platform Advisorの物語では、参加者は事前にVSMとMBPMを作成している。このため、次のDomain Knowledgeはすでに共有されている。

- Current Stateを構成する工程
- 各工程のPTとLT
- 手戻り、問い合わせおよび待ち時間
- 担当者が行っている工夫
- 担当者が感じている摩擦
- 改善可能な工程と、そのおおよその規模

したがって、この物語でSolution-firstを使う主な理由は、Domain Knowledgeが不足しているからではない。

## なぜSolutionから始めるのか

正攻法では、Current Stateを分析し、ProblemまたはChallengeを言語化し、それを解消した時のValue Hypothesisを置いてから、複数のSolution Hypothesisを考える。

しかし、人間が実際に考える順序は必ずしもこの通りではない。Domain Knowledgeがあっても、「これをやったらよいのではないか」というSolutionのIdeaが先に思い浮かぶ。

先に出たIdeaを止めてProblemへ戻すよう求めても、参加者にとってProblem、Challenge、Solutionおよびやりたいことの区別は難しい。ファシリテーターが正しい分類を求め続けると、参加者が発言しにくくなり、議論の熱量が下がることもある。

そこで、思いついた順序を否定せず、Solution候補を入口として、その背後にあるCurrent StateとBusiness Valueを遡って言語化する。

この方法は、Solutionを先に決めることを正当化するものではない。Solutionとして表出した参加者のDomain Knowledgeを、検証可能なProblemとValueの仮説候補へ変換するためのFacilitationである。

## 基本の進め方

参加者は、一つのIdeaについて次の三点を書く。

1. 自分がこの状況で実施したらよいと思うことは何か。
2. それは、VSMまたはMBPM上のどのようなCurrent Stateを改善すると思うか。
3. そのCurrent Stateが改善すると、組織または利用者にどのような望ましい変化が生じるか。

三点は、それぞれ次の候補として扱う。

| 入力 | 仮説上の位置づけ |
| --- | --- |
| 実施したらよいと思うこと | Solution OptionまたはSolution Hypothesis候補 |
| 改善したいCurrent State | Problem構造の一端またはChallenge候補 |
| 望ましい変化 | Value HypothesisまたはBusiness Value候補 |

GenAIには、三点が同じReasoning Chainとして論理的につながっているかを確認させる。

特に、改善したいCurrent Stateを「特定のSolutionがないこと」と表現するのは禁じ手とする。それはSolutionの裏返しまたは正当化であり、観測されたProblemではない。代わりに、それがないことでActorにどのような困った事象が起きているかを書く。

個々のReasoning Chainを確認した後、集まったCurrent Stateを束ね、Problem Statementの候補を作る。Problem Statementは問題構造のすべてを含む文章ではなく、共有したDomain Knowledgeの中心を思い出すための短いRepresentationとして扱う。

参加者は、最初に出したSolution案へコミットしない。IdeaはProblem構造を探索する入口であり、そのまま採用対象になるとは限らない。

## 三種類の確認を分ける

この方法では、「検証」という言葉が指す対象を分ける必要がある。

### 1. Reasoning Chainの構造確認

個々のSolution候補、改善したいCurrent StateおよびBusiness Valueが、論理的につながるかを確認する。

確認する主な観点は次の通りである。

- Actorが途中で変わっていないか。
- 問題領域、目的または成果がすり替わっていないか。
- Current StateがSolutionの言い換えになっていないか。
- Business ValueがSolutionの実施完了または中間能力で止まっていないか。
- 因果関係が遠い場合に、途中のLogicを説明できるか。

この確認だけでは、Problemの実在、Valueの妥当性、Solutionの有効性または全体の抜け漏れは分からない。

### 2. VSM・MBPMに対する網羅性Review

Reasoning Chainを通過したCurrent Stateを束ねた後、VSMとMBPM全体へ戻り、偏りと抜け漏れをReviewする。

- 扱われていない工程またはActorはないか。
- 見落としている待ち時間、手戻り、問い合わせまたは属人的な工夫はないか。
- 一部の参加者または職務の関心だけに偏っていないか。
- 同じProblemに対する別のSolution Optionはないか。
- Problem Statement候補に含めなかった重要なProblem構造はないか。

これは、仮説が正しいことを確かめる実証的なValidationではなく、既知のDomain Knowledgeに対する網羅性Reviewである。

### 3. Problem・Value・Solutionの仮説検証

構造と網羅性を確認した後、意思決定に必要な仮説を、Interview、行動観測、既存Data、Prototypeまたは限定的なExperimentで検証する。

- Problemは対象Actorに実在するか。
- Problemは対応する価値があるほど重要か。
- Actorは想定したValueを望んでいるか。
- 選んだSolutionはProblemとValueに対して有効か。
- 対象外のActorまたは母集団へ一般化してよいか。

Reasoning Chainが通過したことは、この検証の代わりにならない。

## この方法の弱点

Solution-firstは、参加者が直感的に思い出したIdeaから始まる。このため、Biasの影響を強く受ける。

- 最近経験した事象または印象の強い事象が優先される。
- 自分の担当領域で見えるProblemに偏る。
- 最初に思いついたSolutionを正当化する情報を集める。
- 発言力の強い参加者の関心が全体のProblemに見える。
- 参加していないActorのProblemとValueを見落とす。
- 思い出されなかったProblemは、個々のReasoning Chain確認では検出できない。

GenAIもこの弱点を自動的に解消しない。GenAIは、偏った前提からでも論理的に整った説明を生成できる。その結果、Biasを含むIdeaが、もっともらしいReasoning Chainとして補強される危険がある。

したがってGenAIへ依頼するのは、Reasoning Chainの飛躍、Solutionの混入、暗黙の前提および代替Optionの指摘までとする。Problemの実在、Valueの妥当性および検証結果をGenAIの生成内容から判断しない。

## 楽しく参加できることの意味

この方法は、参加者にとって苦手なProblem分類から始めるのではなく、比較的思いつきやすいSolutionのIdeaから始められる。作成者の認識では、実施したWorkshopで参加者は楽しそうにIdeaを出していた。

この楽しさは、仮説が正しいことまたは方法の効果が検証されたことを意味しない。一方で、参加者が発言を続け、異なる視点を出し、Problem構造の材料を増やすためのFacilitation上の価値になり得る。

正しい順番を守らせることよりも、参加者が自然に考えられる入口を使い、後から仮説の役割を分離し、検証可能な形へ直すことを優先する。

## Platform Advisor物語で残ったBlind Spot

Platform Advisorの物語では、VSMとMBPMによって情報探索、問い合わせ、比較検討などの摩擦を確認し、Solution Optionを複数挙げ、Platform Advisorの対象工程と効果仮説を整理した。

しかし、Reasoning Chainの構造確認とVSM・MBPMに対する網羅性Reviewを行っても、「利用者は自分でPlatformを選びたいか」というValue Hypothesisは確認できない。

さらに、Platformを採用したTeamを対象にPrototypeを比較したため、Platformを選ばなかった人または選択自体を望まない人の視点が入りにくい。このBlind Spotは、Solution-firstにおけるBiasと、構造確認を実際の仮説検証と混同する危険を示す。

## 関連する記録と参照

- `RN-20260807-181236-reasoning-chain-validation-prompt-sanitized`
- `RN-20260807-140147-platform-advisor-story-solution-first-mobius`
- `RN-20260806-194532-platform-advisor-selection-vsm-and-mbpm`
- `OBS-20260802-230422-solution-first-hypothesis-reconstruction`
- `HYP-20260802-230423-solution-first-reconstruction-testability`
- Discoveryワークショップ設計メモ:
  https://note.com/skijima/n/nfd3e0353f496

ブログは、より広いDiscovery Workshopの設計を扱う。このメモでは、そのうちSolution候補からProblem構造とBusiness Valueを遡る部分だけを参照し、Platform AdvisorのVSM・MBPMを前提とする説明へ限定した。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
