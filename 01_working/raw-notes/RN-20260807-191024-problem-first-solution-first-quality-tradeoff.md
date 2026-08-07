---
id: RN-20260807-191024-problem-first-solution-first-quality-tradeoff
type: raw_note
title: "Problem-firstの網羅性とSolution-firstの全体品質Trade-off"
content_language: ja
created_at: 2026-08-07T19:10:24+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-07T19:15:08+09:00
sanitization_checked_by: agent:codex
tags: [solution-first, problem-first, problem-analysis, workshop-quality, facilitation, participant-motivation, vsm, mbpm, cognitive-bias, platform-advisor]
---

# メモ

## このメモの目的

Problem分析を正攻法で始める方法と、Solution候補からProblemとValueを遡る方法のTrade-offを、登壇時に説明するためのメモである。

Solution-firstを、人間がProblem分析を苦手とするための妥協としてではなく、Workshopの後工程まで含む全体品質を守るための設計判断として説明する。

## 登壇での導入案

> 問題分析では、まずVSMやMBPMを見ながら、見落としがないかを確認し、問題を書き出していきます。

> ……なんですけど、これはなかなかコツがいります。問題をProblemとして表現するのは難しいですし、参加者がProblem、Challenge、やりたいことを分けられず、なかなか書けないこともあります。ファシリテーターが「今はSolutionではなくProblemを書いてください」と言い続けると、部屋の空気も冷えていきます。なので、私はあまりこの順番だけでは進めません。

> 代わりに、まず「この状況で、何をやったらよいと思いますか」と聞きます。人はProblemよりも、SolutionのIdeaなら持っていることが多いからです。出てきたIdeaから、それが改善するCurrent Stateと、その改善によって得たいBusiness Valueを遡ります。

## Problem-firstの利点とRisk

Problem-firstでは、VSMとMBPMを工程、Actor、待ち時間、手戻り、問い合わせ、属人的な工夫などの観点から順に確認できる。このため、初期のProblem分析を網羅的に進められる可能性がある。

一方、参加者がProblemを発見し、適切な粒度で表現するには経験とコツがいる。参加者が書けない状態で、ファシリテーターが正しい分類を繰り返し求めると、次のRiskが生じる。

- 発言数が減る。
- 異なる立場からの視点が出なくなる。
- 自分の表現が間違っていると思い、参加者が発言を控える。
- 出力をファシリテーターが作ったものと感じ、Ownershipを持ちにくくなる。
- Workshop後の仮説検証や改善活動へ参加しにくくなる。

Problem-firstで理論上の網羅性を得られるとしても、参加者がその進め方に乗れるかは賭けになる。序盤で部屋の空気が冷えると、後から得られる情報量、相互Reviewおよび活動へのOwnershipが減り、後工程の品質問題になり得る。

## Solution-firstで引き受けるRisk

Solution-firstでは、参加者が直感的に思い出したIdeaから始める。このため、初期のProblem分析はBiasの影響を受けやすい。

- 最近経験した事象または印象の強い事象へ偏る。
- 参加者自身の担当領域へ偏る。
- 最初に思いついたSolutionを正当化する。
- 発言力の強い参加者の関心が優先される。
- 思い出されなかったProblemが候補に現れない。

したがって、Solution-firstは、それだけで網羅的なProblem分析になる方法ではない。

## なぜSolution-firstを選ぶのか

SolutionのIdeaは参加者にとって比較的出しやすい。苦手なProblem分類から始めずに済むため、作成者が実施したWorkshopでは、参加者が楽しそうにIdeaを出していた。

参加者が発言を続けられると、次の状態を作りやすい。

- Ideaと視点の種類が増える。
- 暗黙知や違和感が表に出る。
- 参加者同士が「それは違うかもしれない」と修正できる。
- 最初のIdeaを撤回または変更しやすい。
- 分析結果にOwnershipを持ち、後続の検証を続けやすい。

この楽しさは、仮説の正しさを示すEvidenceではない。しかし、Problem構造の材料を増やし、後続の仮説検証を参加者自身が続けるための、Workshop設計上の条件になり得る。

Solution-firstは、初期のProblem分析精度を最大化する方法ではない。初期の見落としRiskを引き受ける代わりに、参加者の発言、相互作用およびOwnershipを維持し、後工程まで含む全体品質を高めることを狙う。

## 初期の見落としをどう回収するか

Solution-firstによるProblem分析の弱点は、その後に意図的に回収する。

1. Solution、改善したいCurrent State、Business ValueのReasoning Chainを確認する。
2. 「特定のSolutionがないこと」をProblemとしていないか確認する。
3. 抽出したCurrent Stateを束ねる。
4. VSMとMBPM全体へ戻り、未検討の工程、Actor、待ち時間、手戻り、問い合わせおよび工夫がないか確認する。
5. 同じProblemに対する別のSolution Optionがないか確認する。
6. ファシリテーターが、参加者の視点から抜けている領域を指摘する。
7. Problem、ValueおよびSolutionのうち、意思決定に必要な仮説を後続工程で検証する。

VSM・MBPMへの再照合とファシリテーターによる不足の指摘は、補助的な作業ではなく、Solution-firstを成立させるためのControlである。

ただし、ファシリテーター自身が見落としているProblem、参加していないActorの視点、および既存のVSM・MBPMに表現されていない情報は残り得る。このため、再照合を行っても網羅性または正しさを保証したとは扱わない。

## このTrade-offの説明

Problem-firstとSolution-firstの違いは、正しい方法と間違った方法の違いではない。

- Problem-firstは、初期の網羅的なProblem分析を狙いやすいが、参加者の発言とOwnershipを損なうRiskがある。
- Solution-firstは、初期のProblem見落としRiskがあるが、参加者の発言とOwnershipを維持しやすい。
- Solution-firstで引き受けたRiskは、VSM・MBPMへの再照合、ファシリテーターによる介入、代替Optionの確認および後続の仮説検証で回収する。
- 一度失われたWorkshopの熱量とOwnershipは、後から回収しにくい。

このため作成者は、初期成果物だけの品質ではなく、後続の仮説検証と改善活動まで含む全体品質を優先し、Solution-firstを入口として使用する。

## 短い説明案

> Solution-firstは、人間がProblem分析を苦手とするための妥協ではありません。Problem-firstには初期の網羅性がありますが、参加者が発言できなくなれば、後工程で使える情報とOwnershipを失います。Solution-firstでは、まず自然に出せるIdeaから始めます。その代わり、Problemの見落としRiskをVSM・MBPMへの再照合、ファシリテーターの指摘、代替Optionの確認、後続の仮説検証で回収します。最初の分析だけでなく、Workshop後も含めた全体品質を選んでいます。

## 関連する記録

- `RN-20260807-185019-solution-first-problem-statement-rationale-and-limits`
- `RN-20260807-181236-reasoning-chain-validation-prompt-sanitized`
- `RN-20260806-194532-platform-advisor-selection-vsm-and-mbpm`
- `OBS-20260802-230422-solution-first-hypothesis-reconstruction`
- `HYP-20260802-230423-solution-first-reconstruction-testability`

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
