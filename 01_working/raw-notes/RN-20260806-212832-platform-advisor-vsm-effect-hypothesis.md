---
id: RN-20260806-212832-platform-advisor-vsm-effect-hypothesis
type: raw_note
title: "Platform AdvisorのVSM上の効果仮説"
content_language: ja
created_at: 2026-08-06T21:28:32+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-06T21:34:45+09:00
sanitization_checked_by: agent:codex
tags: [platform-advisor, vsm, effect-hypothesis, process-improvement, lead-time, decision-support, adr, human-ai-collaboration]
---

# メモ

## このメモの位置づけ

Platform AdvisorによってVSMがどのように変化するかの効果仮説を記録する。現時点では検証済みの効果ではない。

比較元とするRaw Note：

- `RN-20260806-194532-platform-advisor-selection-vsm-and-mbpm`

## 現行Scopeの効果仮説

Platform Advisorによって、VSMの「利用可能なインフラ調査」に含まれるすべての工程をChat上で実施できるようにする。

- ドキュメントを探す
- ドキュメントを読んで必要な情報を収集する
- わからない点をまとめる
- Platform Teamへ確認していた内容を得る

さらに、次の「インフラサービス決定」のうち、比較観点の整理までをChat上で実施できるようにする。

これによって、分散した情報の探索、返答待ち、手作業による情報のまとめ、比較資料を作る前の観点整理を一つの会話に統合し、対象工程のPT、LTおよび手戻りを減らせると仮説を置く。削減幅の目標値はまだ設定しない。

## VSM上の数値計算

### 入力値

Platform Advisorが対象とする現在工程の入力値は次の通り。

| 工程 | PT | LT | 手戻り率 |
| --- | ---: | ---: | ---: |
| ドキュメントを読んで情報収集 | 4h | 9h | 40% |
| わからない点をまとめてPlatform Teamに聞く | 3h | 1週間 | 50% |
| 比較観点整理 | 10h | 10h | 未設定 |

### 手戻りを加味しない合計

- PT：`4h + 3h + 10h = 17h`
- LT：`9h + 1週間 + 10h = 1週間 + 19h`
- 1週間を5 business days、1 business dayを8hとする参考換算：`40h + 19h = 59h`

この`PT 17h`と`LT 1週間 + 19h`が、現行ScopeのPlatform Advisorが対象とする名目上のAddressable Costである。

### 手戻りを加味した単純モデル

参考計算として、手戻りが発生した場合に該当工程を1回だけ同じPTおよびLTで再実施すると仮定する。実際の追跡調査や追加往復の時間は未計測のため、この仮定は簡略化である。

- PT：`4h × 1.4 + 3h × 1.5 + 10h = 20.1h`
- LT：`9h × 1.4 + 1週間 × 1.5 + 10h = 1.5週間 + 22.6h`
- 1週間を40hとする参考換算：`60h + 22.6h = 82.6h`

この単純モデルでは、Platform Advisorが対象とするAddressable Costは`PT 20.1h`、`LT 82.6h`となる。

### Platform Advisor導入後の削減式

Platform AdvisorとのChatに必要なPTを`A`、LTを`B`とする。現時点で`A`と`B`の目標値は未設定である。

- 名目値に対するPT削減：`17h - A`
- 名目値に対するLT削減：`59h - B`
- 手戻り込み単純モデルに対するPT削減：`20.1h - A`
- 手戻り込み単純モデルに対するLT削減：`82.6h - B`

Platform AdvisorのPrototype検証で`A`と`B`を実測した後に、削減量と削減率を計算する。

## 現行Scopeに含めない工程

Platform Advisorは判断材料と比較観点を提供するが、現行Scopeでは次の工程を代替しない。

- Project Ownerとの合意形成を含む意思決定
- ADRの記述
- 利用方法の詳細調査
- スケジュール想定の作成

## 将来Scope

将来は、Platform Advisorとの会話で得た情報、比較観点、候補および判断根拠を使い、意思決定用のSlideとADR Draftを作成できるようにする。

SlideおよびADR Draftの作成を支援する場合も、ADRの最終確定、意思決定、およびProject Ownerとの合意形成は人間が行う。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
