---
id: RN-20260807-123008-platform-advisor-effect-measurement-observation-rationale
type: raw_note
title: "Platform Advisorの効果測定と観測点の根拠"
content_language: ja
created_at: 2026-08-07T12:30:08+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-07T13:42:35+09:00
sanitization_checked_by: agent:codex
tags: [platform-advisor, effect-measurement, vsm, mbpm, ai-slop, quality-guardrail, business-outcome, cost-transfer]
---

# メモ

## この資料の位置付け

Platform Advisorのシナリオ内で定義した、効果検証のためのMetricと、その観測点を選んだ理由を解説する。
特に、Platform Advisorが対象工程を短縮できたかと、AI Slopによる負荷が下流へ移っていないかを分けて観測可能にする。

これは物語内の測定設計であり、実測結果ではない。

## 関連資料

- `RN-20260806-212832-platform-advisor-vsm-effect-hypothesis`
- `RN-20260806-213822-platform-advisor-downstream-ai-slop-signals`
- `RN-20260806-014446-platform-advisor-business-goal-and-blind-spot`

## 観測観点とその理由

効果測定では、次の四つを分けて扱う。

1. Platform Advisorが直接対象とする工程のProcess Outcome
2. 下流工程へ負荷を移していないことを確認するQuality Guardrail
3. Business Outcomeへ至る途中のSignalであるPlatform採用率
4. 最終的なBusiness Outcomeである既存システム運用費の削減

これらを分けるのは、局所的なPTやLTの短縮だけを見て、Business Outcomeまで実現したと誤認しないためである。

### 1. 直接のProcess Outcome

Platform Advisorが直接対象とするのは、VSM上の次の工程である。

- 利用可能なインフラの情報探索
- 不明点をまとめてPlatform Teamへ問い合わせる作業
- Platformを比較する観点の整理

したがって、導入前後で対象工程のPT、LTおよび手戻り率を比較する。ここで観測するのはVSM全体ではなく、Platform Advisorが直接変更する範囲である。

`RN-20260806-212832-platform-advisor-vsm-effect-hypothesis`に記録した`PT 17h`、`LT 59h`、および手戻りを加味した単純モデルの`PT 20.1h`、`LT 82.6h`は、改善対象となり得るAddressable Costである。これらは導入後に実現する削減量そのものではない。Platform AdvisorとのChatに必要なPTとLTを実測し、Baselineとの差分を求めて初めて、対象工程での削減効果を評価できる。

### 2. 下流への負荷移転を確認するQuality Guardrail

上流のPTやLTが短くなっても、Platform AdvisorのOutputが不正確または不十分であれば、確認、修正、追加調査のCostが下流へ移る。このシナリオでは、その状態をAI Slopの発生可能性として扱う。

観測点はMBPMを使い、次の順序で選ぶ。

1. Platform AdvisorのOutputを実際に使う下流のProcess Stepを特定する
2. そのStepでOutputを使って行う判断または作業を確認する
3. Outputが誤っている、情報が不足している、または整理が不適切な場合に起きる失敗を考える
4. その失敗がPT、LT、手戻り率、追加作業または質的な変化のどれに現れるかを決める

AI Slopを下流への負荷移転と考えると、移転したCostを負担する追加作業は、典型的にはOutputが次のActorへ渡されるHandover付近に現れる。そのため、次の三つを観測点とする。

#### Project Ownerとの合意形成

Platform Advisorが作った比較観点や判断材料は、Project Ownerとの合意形成で使われる。

論点不足、説明不備または根拠不足があれば、合意形成できずに再ReviewやMeetingが増える可能性がある。そのため、次を観測する。

- 手戻り率が導入前Baselineの20%から上昇しないこと
- 再Review回数、ReviewのPTおよびLTが増加しないこと
- 指摘理由に、説明不備、論点不足、根拠不足、適用条件の見落とし、または参照情報の誤りが増えていないこと

手戻り率が変わらなくても、初回Reviewの中でReviewerが追加確認や修正を吸収する場合がある。そのため、指摘内容の分類も併せて確認する。

#### 利用方法詳細調査

現行ScopeのPlatform Advisorは、申請方法、Platform Teamとの役割分担、および想定作業Lead Timeの詳細調査を対象外とする。したがって、この工程で通常の問い合わせが発生すること自体はAI SlopのSignalではない。

観測するのは、必要事項の不足、非機能要件とPlatformの不整合、または利用者の誤解によって、従来より追加質問、訂正、再確認またはPlatform選択のやり直しが増えていないかである。

- Platform選択まで戻る手戻り率がBaselineの0%から増加しないこと
- 追加質問率がBaselineの10%を超えないこと
- TicketあたりのPlatform Team対応PTがBaselineの2hから長時間化しないこと
- Ticket発行から回答までのLTがBaselineの7hから長時間化しないこと
- 利用方法詳細調査全体のPT 3hおよびLT 10hが長時間化しないこと
- Advisorの誤り、情報不足または利用者の誤解に由来する問い合わせが増えていないこと

#### 環境払い出し時および払い出し後

Process上のMetricだけでは、実際に環境を払い出した時点や利用開始後に判明する想定外の制約、追加作業または設計前提の不一致を見落とす可能性がある。

WBSやKanbanの遅延は複数要因の影響を受けるため、Advisorの影響を断定するMetricにはしない。追跡対象を見つける補助Signalとして使い、払い出し完了後または一定期間の利用後に事後Interviewを行う。Ticket、Review記録または変更履歴とも照合し、AdvisorのOutputに由来する追加作業、修正、人手の介入または例外対応がなかったかを確認する。

### 3. Platform採用率は中間Signalとして扱う

Platform Advisorによって利用者が判断しやすくなれば、対象ProjectのうちPlatformを採用する割合が上がる可能性がある。このPlatform採用率は、Platform AdvisorからBusiness Outcomeへ至る途中のSignalであり、Advisorが直接短縮するProcess Outcomeではない。

採用率を観測する場合は、対象Projectと「採用」の定義、集計期間および比較条件を定める必要がある。また、採用率の上昇だけでは、利用者が価値を得たこと、運用が標準化されたこと、または運用費が減ったことを意味しない。

### 4. 最終的なBusiness Outcome

この物語のBusiness Goalは、基準時点でIT投資総額の50%を占める既存システム運用費を半減し、IT投資総額が一定の場合に構成比を25%へ下げることである。そのために、省力的に運用できるKubernetes基盤の活用と運用の標準化を進める動機がある。

想定する因果は次の通りである。

```text
Platform選択の負担が減る
  ↓
Platformの採用が増える
  ↓
運用が標準化される
  ↓
既存システム運用費が減る
```

各矢印は別の仮説であり、Platform Advisorの対象工程でPTやLTが短縮されたことから、運用費削減までを直接結論づけない。特に「利用者は自分でPlatformを選びたい」という前提は、この物語で意図的に残しているBlind Spotである。

既存システム運用費への効果を確認するには、Platform Advisorの局所Metricとは別に、Platform採用後の運用工数、標準化された運用の割合、例外対応、Support Costおよび既存システム運用費を継続的に観測する必要がある。これらはPlatform Advisor単独の効果として直ちに帰属できない。

## なぜ観測点を事前に決めるのか

観測点を導入前に決めるのは、導入後に改善したMetricだけを選んで成功と判断することを避けるためである。また、期待する直接効果と、起きてほしくない負荷移転を同時に定義することで、効果仮説を反証可能にする。

- 対象工程のPTとLTが改善し、下流Guardrailが悪化しない場合：観測範囲では直接効果があり、明確なCost移転を検出しなかった
- 対象工程のPTとLTが改善し、下流の手戻りや追加作業が増えた場合：局所的な高速化と下流へのCost移転が同時に起きた可能性がある
- 対象工程のPTとLTが改善しない場合：想定した直接効果を確認できない

いずれの場合も、その観測だけでPlatform採用率の上昇やBusiness Goalの達成までを結論づけない。


## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
