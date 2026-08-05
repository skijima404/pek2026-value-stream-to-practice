---
id: RN-20260806-011126-platform-advisor-genai-scenario-draft
type: raw_note
title: "Platform Advisor通し事例の未採用GenAI作業案"
content_language: ja
created_at: 2026-08-06T01:11:26+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-06T01:22:00+09:00
sanitization_checked_by: agent:codex
tags: [platform-advisor, worked-example, hypothesis-construction, hypothesis-validation, value-hypothesis, service-design, genai-proposal, not-adopted]
---

# Platform Advisorを使った仮説構築・検証の通し事例

## このメモの位置づけ

Platform Advisorを一つの題材として、AI Slopの問題提起から、Value Hypothesis、
Solution Hypothesis、Featureによる検証、Evidenceを受けた判断更新までを通して説明する
ためのScenarioを育てる。

## 将来このメモを読む人とGenAIへの注意

このメモは、既存の実務経験、ObservationおよびHypothesisを材料にCodexが構成した、
**未採用のGenAI作業案**である。人間は、この文書を完成したScenarioではなく、今後
Top-downでScenarioを作成する時のカンペおよびコピペ元として扱うことを確認した。

`review_status: reviewed`になっていても、確認されたのはこの記録の用途と位置づけである。
本文のScenario、登場人物、因果、Metric、検証結果および判断が、登壇内容として採用された
ことを意味しない。このメモから一部を利用する場合も、人間がProblemとBusiness Goalを
定義し、VSMを作成したうえで、Value Hypothesis、Solution Hypothesis、Feature Hypothesisへ
Top-downに構成し直す。

これは実在するPlatform Advisorの導入記録または検証結果ではない。物語内で起きる出来事を
Evidenceへ変換してはならない。採用されたScenarioまたは現在の登壇内容を探す場合は、
このRaw Noteではなく、明示的な採用判断を持つ`03_artifacts/`を確認する。

主な既存材料は次である。

- `OBS-20260802-230424-platform-choice-hidden-assumption`
- `HYP-20260802-230425-platform-choice-burden-value`
- `OBS-20260731-120412-value-and-slop-experience-decision-flow`
- `OBS-20260801-004820-coupled-platform-value-streams`
- `OBS-20260801-004821-contract-accountability-cost-transfer`
- `OBS-20260804-004531-hypothesis-validation-uncertainty-decision`

## 最初に現れるSolution

物語内のPlatform Teamは、次のIdeaから始める。

> Enterprise Architecture RepositoryやPlatform情報を会話形式で参照し、利用者の
> Contextに合うPlatform、標準Path、過去の判断および例外手続きを案内する
> Platform Advisorを作る。

技術的には作れそうで、Demoもしやすい。Teamは、利用者がPlatformを比較し、適切なものを
自分で選ぶための情報が不足していると考える。

初期の成功Signalとして、次のような局所Metricを置きたくなる。

- Advisorの利用者数
- 質問数またはSession数
- 回答までの時間
- Platform Teamへの一次問い合わせ件数
- 回答に対する肯定的評価

この時点では、利用された回答が後続の設計判断に使われたか、利用者が安全に次へ進めたか、
Review、例外対応またはSupportの負荷がどこへ移ったかは十分に扱われていない。

## 最初のReasoning Chain

```text
利用者はPlatform情報の探索と比較に時間を使っている
  ↓ Challenge
Platformを選ぶための情報を集め、意味を解釈することが難しい
  ↓ Value Hypothesis
探索と比較を容易にすれば、利用者はPlatformを適切に選びやすくなる
  ↓ Solution Hypothesis
Repositoryを参照するPlatform Advisorが、質問へ回答し選択を支援する
  ↓ Feature
自由入力のChat UIとPlatform推奨回答
```

このReasoning Chainは一見つながっているが、少なくとも次の前提を含む。

- 利用者はPlatformを自分で選びたい
- 情報不足が選択を妨げる主な原因である
- Advisorの回答があれば利用者は判断できる
- 回答を得た利用者は安全に次の作業へ進める
- Platform Teamへの問い合わせ減少は、利用者側の負荷減少も意味する

## Discoveryで見つかる隠れたValue Hypothesis

既存の`HYP-20260802-230425-platform-choice-burden-value`では、利用者の一部はPlatformを
比較して選ぶことより、安全な標準Pathが示され、選択と説明の負荷が減ることを価値とする
可能性を置いている。

物語内のProject Teamは当初この違いに気づいていない。採用者だけでなく、Advisorを
使わなかった人、選択へ関与しなかった人、標準Pathを受動的に利用した人へ確認することで、
次の異なるJobが候補になる。

```text
最初に想定したJob
Platformを比較し、自分で適切なものを選ぶ

見つかる可能性があるJob
自分のContextで安全に使える標準Pathを知り、次の開発へ進む

例外時のJob
標準Pathを外れる必要があるかを判断し、適切な相談先へ到達する
```

この違いが確認された場合、Value Hypothesisは次のように再構成できる。

> Platform利用者の一部にとって価値があるのは、選択肢が増えることではなく、
> 自分のContextで安全に利用できる標準Path、適用条件および例外時の進み方が示され、
> 選択と説明の負荷が減ることである。

## SolutionをAIへ固定しない

Value Hypothesisを実現するSolution Optionとして、Platform Advisorだけを置かない。

- RepositoryまたはDocumentの情報設計を改善する
- Searchを改善する
- Decision Treeを明示する
- Service Catalogと標準Pathを整理する
- TemplateまたはChecklistを提供する
- TrainingまたはEnablementを行う
- Office Hours、Triageまたは人による相談を設ける
- Platform選定またはArchitecture ReviewのProcess自体を改善する
- Platform AdvisorでContextを確認し、標準PathまたはEscalation先を案内する

Platform Advisorは、これらと比較される一つのSolution Hypothesisである。

## 再構成したPlatform AdvisorのSolution Hypothesis候補

> 対象JobとSource Coverageを限定し、利用者Context、標準Pathの適用条件、根拠、
> 不足情報および例外時のEscalationを返すPlatform Advisorは、情報を検索して回答する
> Botまたは選択肢一覧だけを提供する場合より、利用者が安全に次の判断または開発へ
> 進みやすくし、選択、説明および確認の負荷を減らす。

このSolution Hypothesisには、少なくとも次の不確実性が含まれる。

| ID | 不確実性 | 外れた場合の影響 | 初期の確認方法候補 |
| --- | --- | --- | --- |
| U1 | 対象利用者にPlatform選択、標準Path確認または例外判断の負荷がある | 解くべきProblemが弱くなる | 採用者、非採用者、非選定者へのInterviewと現在の行動確認 |
| U2 | 利用者が求めるOutcomeは、比較可能性より安全に次へ進めることである | Value Hypothesisを取り違える | 実際の選定Episodeと望んだ終了状態のInterview |
| U3 | Advisorが他のSolution Optionより対象Jobを小さいCostで支援できる | AIを選ぶ理由がなくなる | 現行手段、Decision Tree、Advisor PrototypeのTask比較 |
| U4 | Advisorが適用条件、根拠、不足情報および非対応範囲を適切に示せる | 誤推奨または偽の安心を生む | Known-good、Known-bad、情報不足、例外Scenarioによる評価 |
| U5 | Advisor利用後にReview、差し戻し、再確認、Supportまたは例外対応が増えない | Costを利用者または後続Actorへ移す | DVSとOVSを接続したHand-off観測と下流Interview |
| U6 | Source更新、回答の訂正、Escalationおよび廃止を継続運用できる | 利用が増えるほど保守負債と古い回答が増える | 限定運用での更新作業、例外件数、Owner負荷の記録 |

これらは検証計画の候補であり、Validation Componentとして確定していない。

## 最小Feature候補

最初から何でも回答できるChat UIを作らない。例えば、一つの利用者Role、一つの
Platform選定Job、限定したGoverning Sourceだけを対象にする。

入力:

- 利用者Role
- 作ろうとしているServiceまたはApplicationの条件
- 必要なCapability
- 制約または例外条件

出力:

- 推奨する標準Path、または現時点では推奨できないという回答
- 適用条件
- 根拠Source
- 不足しているContext
- Advisorが判断していないこと
- 例外時の相談先または次のAction

Featureの目的はAdvisorを完成させることではなく、U3、U4およびU5の一部を小さく
確認することである。

## 検証方法の組み合わせ

### ProblemとValueの確認

- 実際にPlatformを採用した人だけでなく、採用しなかった人、選定へ関与しなかった人、
  標準Pathを受動的に利用した人を含める
- 「Advisorが欲しいか」ではなく、直近の選定または利用開始Episodeを聞く
- 何を比較したか、どこで止まったか、誰へ説明したか、最終的に何ができれば終了だったかを
  確認する

### Solution比較

同じTaskを、次の手段で実施して比較する。

1. 現在のDocumentまたは人への問い合わせ
2. 整理したDecision TreeまたはService Catalog
3. 限定したPlatform Advisor Prototype

時間だけでなく、判断根拠、見落とし、追加確認、安心して次へ進めるか、および後続Reviewで
修正された内容を残す。

### Advisorの当たり前品質

- Known-good Scenario
- Known-bad Scenario
- Context不足Scenario
- Sourceに記載がないScenario
- 対応範囲外Scenario
- 高Riskで人へEscalationすべきScenario
- Source更新後のRegression

回答の流暢さではなく、正しく回答すること、質問へ戻すこと、保留すること、拒否すること、
Escalationすることを区別して確認する。

### Value Stream上のOutcome

提供側DVSだけでなく、利用者側OVSと後続Actorまで観測する。

```text
Platform Team
Source更新 → Advisor提供 → 回答 → 訂正・改善

利用者
相談 → 回答理解 → 選択・例外判断 → 設計 → Review → 開発・運用
```

利用数または一次問い合わせ減少だけで成功と判断しない。Review差し戻し、再確認、
例外対応、Support、利用中止および人による意味変換がどこで増減したかを見る。

## 判断を更新するScenario候補

物語では、Platform Advisor導入後に次が観測される。

- Advisorの利用者数は増えた
- 一次問い合わせは減った
- 回答までの時間は短くなった
- 一方、Architecture Reviewでの差し戻しが増えた
- 一部の利用者は、Advisor回答を判断材料ではなく公式承認として扱った
- Advisorを使わなかった人は、Platformを比較したいのではなく標準Pathだけを知りたかった

この結果から、単純に成功または失敗とは判定しない。

- 利用と速度のSignalは、Featureが使われたことを示す
- 差し戻し増加は、確認Costが後続へ移った可能性を示す
- 公式承認としての利用は、Service ContractのMismatchを示す可能性がある
- 非利用者の回答は、最初のValue Hypothesisが対象Jobを取り違えた可能性を示す

次の判断候補は、一つに固定しない。

- 対象Jobを標準Path確認へ狭める
- 例外判断は人へEscalationする
- 推奨ではなく根拠探索だけへScopeを戻す
- AdvisorではなくDecision TreeまたはService Catalogへ切り替える
- 追加Evidenceを得るまで拡大を保留する
- 下流負荷が許容できない場合は停止する

## この事例で示したい仮説検証

この事例の目的は、「Platform Advisorを正しく作る方法」を示すことだけではない。

```text
便利そうなAI Featureが先に現れる
  ↓
Reasoning Chainを再構成する
  ↓
隠れたValue Hypothesisに気づく
  ↓
複数の不確実性へ分解する
  ↓
不確実性ごとに異なる方法で確認する
  ↓
局所Metricと下流Outcomeを分けて読む
  ↓
作る、狭める、変える、保留する、捨てるという判断を更新する
```

仮説検証はPlatform Advisorを正当化する活動ではない。最初のProblem、Value、Solution、
Featureおよび測定方法のどこを更新すべきかを見つける活動として扱う。

## 現時点で未確定の設計

- 最初の対象利用者Role
- 最初に扱う具体的なPlatform選定Job
- Advisorが参照するSourceの種類
- 物語内で最初に取得するEvidence
- どのEvidenceによって隠れたValue Hypothesisへ気づくか
- 最終的にAdvisorを狭めて継続するか、別Solutionへ切り替えるか
- 25分の本編でどこまで扱い、何をRepositoryへ残すか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
