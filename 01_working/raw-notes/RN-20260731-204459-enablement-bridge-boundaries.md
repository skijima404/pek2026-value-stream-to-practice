---
id: RN-20260731-204459-enablement-bridge-boundaries
type: raw_note
title: "Enablementで橋を架け続けるべきでない境界"
content_language: ja
created_at: 2026-07-31T20:44:59+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: import
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-31T20:52:36+09:00
sanitization_checked_by: agent:codex
tags: [enablement, platform-service, service-contract, self-service, capacity, persona, ai-slop, presentation-scope]
---

# メモ

## このメモの位置づけ

2026年7月31日の対話から、「Enablementで橋を架けるべきでないケースは何か」
という発散テーマを抽出したRaw Note。

- 人間とAssistAの発言を分離せず、議論の流れとして再構成した
- 過度な支援をすべて否定するのではなく、Platform Service、Persona、Contract、
  Self-Serviceの境界として整理した
- この論点は以前の登壇で扱っており、PEK2026本編では主題にせず割愛するという
  Scope判断も含む
- 会話上の整理であり、検証済みの一般論または採用済みArtifactではない

## 問いの背景

Platform Teamは人数が限られることが多い。利用者とのズレが見つかるたびに、
Enablement TeamまたはPlatform Teamが個別に橋を架けると、短期的には利用を
成立させられる。

しかし、何でも引き受けると、個別支援だけでCapacityを使い切り、Platform
Serviceそのものの標準化、改善、再利用可能化へ手が回らなくなる。

会話で扱った問いは次の通り。

> Enablementはハンドオーバーの不足を埋める万能薬なのか。

> どこまでが初期導入支援で、どこからがPlatform Teamによる恒常的な
> 個別作業の肩代わりなのか。

## 過度なEnablementが起こす循環

会話では、次のような状態を想定した。

```text
利用者
「どう使うのですか」
  ↓
Platform Team
個別に説明する
  ↓
利用者
「自分たちのケースではどうすればよいですか」
  ↓
Platform Team
個別に調査・設計・補完する
  ↓
同じ種類の支援が次の利用者でも繰り返される
  ↓
Platform Serviceを改善するCapacityがなくなる
```

一見すると親切なEnablementだが、実態として次の循環になりうる。

```text
Contract不足またはPersona不一致
  ↓
人間による個別補完
  ↓
短期的には利用できる
  ↓
Service側の不足が見えにくくなる
  ↓
個別支援が常態化する
  ↓
長期的にはScaleしない
```

## Personaと利用前提の問題

例として、Architecture設計能力または技術的Literacyが十分でない組織が、
Platform Serviceを利用する場面を考えた。

既存のMonolithを段階的に分割または公開するServiceがFacade Patternを前提として
いても、利用Teamが次を行えない場合がある。

- どこを業務境界として切るか説明する
- Interfaceを設計する
- API利用者を定義する
- 非機能要件を整理する
- 既存Systemの責任範囲を説明する

この時、Platform Teamが毎回その設計を代行すれば利用は成立する。しかし、
それは当初想定したSelf-ServiceなPlatform Serviceではなく、個別のArchitecture
ConsultingまたはCoachingへ変わっている可能性がある。

一方で、利用できない原因をすべて利用者の能力不足とみなすのも適切ではない。
Persona定義時に想定した知見やSkillが実際の利用者像と合っていなければ、
Platform Service側の対象設定またはValue Hypothesisが妥当でない可能性がある。

会話では、次の連鎖として整理した。

```text
Persona定義
  ↓
利用者へ期待するSkillとKnowledge
  ↓
Service Contract
  ↓
必要なEnablement
  ↓
Self-Serviceとして成立する範囲
```

## 「レゴの最後の段を毎回綺麗にする」べきではない

人間側から、Platform Teamが利用者ごとに「レゴの最後の段を綺麗にする」ような
活動を毎回行うべきではなく、極力Self-Serviceを目指した方が双方にとって
負担が小さいという考えが示された。

レゴの比喩で分けると、Platform側の候補は次の通り。

- 再利用できるブロックを提供する
- 接続規格を明らかにする
- 説明書、Template、標準Patternを提供する
- 自動化された検証を提供する
- 必要に応じて初期Trainingまたは導入支援を用意する

一方、次を毎回引き受けるなら、別ServiceとしてScope、Capacity、責任を設計する
必要がある。

- 利用者固有の業務境界を定義する
- 利用者のArchitectureを完成させる
- 利用者の不足Skillを恒久的に補う
- 利用者固有の例外を都度Platform Teamが解決する
- 利用者の成果物が完成するまで伴走し続ける

会話上の比喩では、Platform Teamが毎回利用者の現場へ行き、その人の家の壁を
一緒に完成させるところまでを、標準Platform Serviceの当然の責任にはしない。

## 橋を架け続けるべきでない兆候

会話から読み取った候補を、未検証のチェック項目として残す。

### 同じ摩擦を繰り返し人が補完している

繰り返し発生する質問、判断、作業を個別対応し続けている場合、それは
Documentation、Template、自動化、ContractまたはService設計へ戻す候補である。

### 個別支援がPlatform Service改善を止めている

利用支援のために、標準化、改善、品質向上、廃止判断へ使うCapacityがなくなって
いるなら、Enablementが別のボトルネックになっている。

### 想定Personaと実利用者の差を人力で隠している

利用者が前提Skillを持たないことを毎回個別Coachingで埋めると、Personaまたは
Service Contractの妥当性を見直す機会を失う。

### Platform Teamが利用者の本来の責任まで引き受けている

Platform利用を可能にする支援を越えて、利用者固有の業務判断、Architecture、
成果物完成まで代行している場合、責任境界が変わっている可能性がある。

### 支援終了後に利用者が自律できない

同じ利用者が次回も同じ支援を必要とする場合、Enablementが学習または自律へ
つながっていない可能性がある。

## Enablementが必要なケースまで否定しない

この議論は、Enablementを不要とするものではない。

会話では、次の役割を区別した。

```text
Enablement
=
最初の学習、導入、移行を支援する

Platform Service
=
繰り返し発生する判断または作業を再利用可能にする

利用者
=
前提条件を満たし、支援後は自律的に利用する
```

利用者に前提Skillが不足する場合も、Training、Enablement、Architecture Coachingを
別の選択肢として提供できる。ただし、それをPlatform Serviceに無制限に内包せず、
別Serviceとして扱うか、どの条件で利用するかを明らかにする。

## AI Slopとの接続

AIによってPlatform Service候補、Template、Documentation、Advisorを大量に
生成できても、次が曖昧なら、後からPlatform Teamが人力で補完することになる。

- 誰向けか
- 何を保証するか
- 利用者へ何を求めるか
- どこまでがSelf-Serviceか
- どこからがTraining、Coaching、個別支援か

この時、AIによる生成の高速化は、Enablement TeamまたはPlatform Teamへの
問い合わせ、説明、調整、個別設計を増やす可能性がある。

会話では、個別支援の増加自体を、別のSlopシグナルとして見る案が出た。

> 繰り返し発生する摩擦はPlatform Service側へ取り込む候補であり、個別支援の
> 増加は、ContractまたはService設計が人力補完に依存している兆候になりうる。

これは、すべての個別支援がSlopであるという主張ではない。初期導入、学習、
例外探索、変化の検知には人による支援が必要になる。観測した支援が一時的な橋か、
恒常的な人力依存かを区別する必要がある。

## セッションScopeの判断

この論点は重要だが、PEK2026の中心線には含めない。

理由:

- 過度な支援とSelf-Serviceの境界は、以前の登壇で扱った
- Persona、Skill、Training、Coachingまで説明すると25分の本筋から外れる
- 今回の中心はValue Hypothesis、Release前の選別、AI Slopの観測、MBPMである

本編で触れる場合の候補は一言に留める。

> すべての摩擦をEnablementで解決することも正解ではありません。繰り返し
> 発生する摩擦はPlatform Service側へ戻す候補であり、個別支援の増加は別の
> Slopシグナルになります。

詳細はRaw NoteまたはAppendix候補として残す。

## 現時点の短い整理

```text
Enablementで一時的な橋を架ける
  ↓
利用者が次へ進める
  ↓
摩擦を学習として回収する
  ↓
Contract、Service、Trainingへ反映する
  ↓
次回は人力補完を減らす
```

次の状態なら、橋を架け続ける方法を見直す。

```text
個別支援する
  ↓
同じ摩擦が繰り返される
  ↓
利用者が自律しない
  ↓
Platform Serviceも改善されない
  ↓
Platform TeamのCapacityだけが減る
```

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
