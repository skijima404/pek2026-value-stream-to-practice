---
id: RN-20260806-213822-platform-advisor-downstream-ai-slop-signals
type: raw_note
title: "Platform AdvisorによるAI Slopの下流観測ポイント"
content_language: ja
created_at: 2026-08-06T21:38:22+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-06T21:48:38+09:00
sanitization_checked_by: agent:codex
tags: [platform-advisor, ai-slop, vsm, downstream-load, quality-guardrail, ticket-metrics, follow-up-interview, cost-transfer]
---

# メモ

## このメモの位置づけ

Platform Advisorが上流のPTやLTを短縮しても、不正確または不十分なOutputの確認・修正Costが下流へ移った場合、AI Slopが発生した可能性がある。Platform選択VSMの下流で、その影響を検知するための観測ポイントを記録する。

これは物語内の測定設計案であり、実測結果ではない。

関連するRaw Note：

- `RN-20260806-194532-platform-advisor-selection-vsm-and-mbpm`
- `RN-20260806-212832-platform-advisor-vsm-effect-hypothesis`

## 観測ポイント1：Project Owner Review

Platform Advisorが作った比較観点、判断材料、将来的なSlideまたはADR Draftは、Project Ownerとの合意形成でReviewされる。

VSMでは、この意思決定工程の手戻り率を20%と置いている。Platform Advisor導入後に、少なくともこの手戻り率が上昇しないことをQuality Guardrailとする。

ただし、手戻り率だけでは、Reviewerが初回Reviewの中で追加の確認や修正を吸収した場合のCostを捕捉できない。次も併せて観測する。

- Project Owner Reviewの手戻り率
- 再Review回数
- Reviewに要したPTおよびLT
- 追加確認または修正の件数
- 指摘理由の分類
  - Platform選択の誤り
  - 適用条件または制約の見落とし
  - 判断根拠の不足
  - 参照Sourceの誤りまたは古さ
  - 説明の追加が必要

## 観測ポイント2：利用方法詳細調査

現行ScopeのPlatform AdvisorはPlatform選択と比較観点整理までを対象とし、申請方法、Platform Teamとの役割分担、および想定作業Lead Timeの詳細調査は対象外とする。

そのため、この工程でPlatform Teamへの問い合わせが従来と同様に発生すること自体は、AI SlopのSignalとしない。

観測するのは、Platform AdvisorのOutputが不正確または不十分であったために、従来よりも追加の調査、修正、再確認または選択のやり直しが増えていないかである。

- 利用方法詳細調査の手戻り率
- 利用方法詳細調査の追加質問率
- 詳細調査のPTおよびLT
- Platform AdvisorのOutputの訂正が必要になった件数
- Platform選択まで戻ってやり直した件数
- Platform Teamへの追加確認数
- 追加確認のうち、Advisorの誤りまたは情報不足に由来する割合
- TicketあたりのPlatform Team対応PT
- Ticket発行から回答までのLT

### BaselineとGuardrail

利用方法詳細調査では、通常の問い合わせに対する追加質問と、Platform選択まで戻る手戻りを別の指標として扱う。

| 指標 | 導入前Baseline | Platform Advisor導入後のGuardrail |
| --- | ---: | --- |
| Platform選択まで戻る手戻り率 | 0% | 増加しない |
| 追加質問率 | 10% | 10%を超えない |
| TicketあたりのPlatform Team対応PT | 2h | 長時間化しない |
| Ticket発行から回答までのLT | 7h | 長時間化しない |
| 利用方法詳細調査全体のPT | 3h | 長時間化しない |
| 利用方法詳細調査全体のLT | 10h | 長時間化しない |

TicketのRoutingや担当者の空き待ちはLTに含め、Platform Teamが実際に回答を調査・作成する時間は対応PTとして分ける。Platform AdvisorのOutputの誤りや不足によってTicketの内容が複雑になった場合、手戻り率や追加質問率が上がらなくても、Ticketあたりの対応PTまたはLTが増える可能性がある。

## 観測ポイント3：環境払い出し時および払い出し後

より丁寧にAI Slopの下流影響を確認するなら、Platform選択と利用方法詳細調査の後に、実際に環境を払い出す時点と、払い出し後の利用時点まで追跡する。

確認するのは、Platform Advisorが示した候補、適用条件、判断根拠または不足Contextが、実際の払い出しと利用に進んだときに、想定外の追加作業や修正を生んでいないかである。

観測候補：

- 払い出し時に判明した想定外の制約、例外または不足情報
- 選択したPlatformまたは構成を変更した件数
- 払い出しに必要となった追加Ticket、人手の介入、例外対応および再作業
- 払い出し後に判明した設計前提の不一致
- 後続の開発、Review、運用またはSupportへ移った追加Cost
- Platform AdvisorのOutputを訂正または更新すべきと判断した件数

### 観測方法

WBSやKanbanで払い出しまでの遅延を確認することもできるが、遅延はPlatform Advisor以外の複数要因によっても発生する。そのため、遅延の有無や日数だけからAdvisorの影響を断定しない。WBSやKanbanの情報は、追跡対象のEpisodeを見つけるための補助Signalとして扱う。

主な方法は、払い出し完了後または一定期間の利用後に行う事後Interviewとする。Interviewでは、実際のEpisodeに沿って次を確認する。

- Advisorが何を示し、利用者がどのように判断したか
- 当初の想定と実際の払い出しで何が異なったか
- どの追加作業、修正、待ち時間または人手の介入が発生したか
- そのCostをどのActorが負担したか
- 発生した事象がAdvisorのOutput、別の要因、または両方に関係していたか
- AdvisorのOutputをどのように訂正または改善すべきか

事後Interviewは記憶の不正確さやInterview対象の選定に影響される。可能な範囲でTicket、WBS、Kanban、Review記録または変更履歴と照合し、Interviewの説明だけを実測事実として扱わない。

## 読み方

上流のPTやLTが改善し、下流の手戻り率が増加しない場合、その観測範囲では明確なCost移転を検出しなかったと言える。ただし、これはAI Slopが存在しないことの証明ではなく、測定できない影響や、さらに後続する開発・運用での影響は別に残る。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
