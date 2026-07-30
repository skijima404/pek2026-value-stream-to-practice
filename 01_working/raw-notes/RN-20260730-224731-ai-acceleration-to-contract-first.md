---
id: RN-20260730-224731-ai-acceleration-to-contract-first
type: raw_note
title: "AI高速化からContract Firstへ至る因果"
content_language: ja
created_at: 2026-07-30T22:47:31+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-30T22:52:01+09:00
sanitization_checked_by: agent:codex
tags: [presentation-planning, ai-slop, contract-first, platform-service, value-stream, handover, outcome-delivery]
---

# メモ

## このメモの位置づけ

AIによる生成・実装の高速化から、Platform ServiceのContract Firstと
Value Stream Managementへ至る因果を整理する。

これは確立済みの一般理論ではない。Leanとプロセス改善に長く関わる中での
個人的な経験、現場観察、過去事例との照合から形成された仮説である。
個々の事例や歴史的な類似は、この因果全体を実証するものではない。

## 中心となる因果

```text
AIが生成・実装を高速化する
  ↓
Value Streamの一部だけが速くなる
  ↓
後続工程とハンドオーバーが詰まる
  ↓
各チームが自分の作業中心で局所最適する
  ↓
トータルサービスのOutcomeが失われる
  ↓
だから利用者とのContractを先に設計する
  ↓
Contractから基盤・開発支援・運用を逆算する
  ↓
VSMで実際の体験とOutcomeを検証する
```

## 1. AIが高速化するのはValue Stream全体ではない

AIが直接高速化しやすいのは、Ideaの展開、文書やコードの生成、実装、
テスト作成など、Value Stream上の一部の作業である。

```text
Idea
  ↓
選定
  ↓
設計
  ↓
実装       ← AIで大きく高速化しやすい
  ↓
レビュー
  ↓
承認
  ↓
利用開始
  ↓
運用
```

実装の処理能力だけが増えても、選定、レビュー、承認、利用者への説明、
運用準備などの処理能力が同じなら、Value Stream全体のLead Timeが
同じ比率で短くなるわけではない。

むしろ、後続工程へ到着する成果物の量が増え、次のような形で
ボトルネックが移動する可能性がある。

- レビュー待ちが増える
- 判断と承認が追いつかない
- 生成物の確認負荷が増える
- 利用者への説明やEnablementが追いつかない
- 運用対象や例外対応が増える
- 価値が未検証のService候補が滞留する

ここで起きているのは、Value Stream全体の高速化ではなく、
局所的なProcess Timeの短縮と、後続工程への負荷移動である。

## 2. AgileとDevOpsに見られた構造との類似

AI Slopは完全に新しい現象ではなく、構造として繰り返されてきたものでは
ないかと考えた。

WaterfallからAgileへ移った時、Development側は小さな変更を高頻度で
出すようになった。しかし、Operations側のChange Managementや
リリース手続きが同じ速度へ変わらなければ、DevとOpsの接点が詰まる。

```text
Developmentの反復速度が上がる
  ↓
Operationsとの接点に到着する変更が増える
  ↓
既存のChange Managementが処理できない
  ↓
DevとOpsの間にConflictが生じる
```

DevOpsは、この境界を越えてFlow全体を扱うために現れたと解釈できる。

AIは、このうちAgileが高めた生成・実装・反復の速度をさらに大きくする。
したがって、AI SlopをAI生成物だけの品質問題として扱うと、
その生成物が後続工程や他チームへ渡る時に起こる構造的な問題を
見落とす可能性がある。

## 3. ハンドオーバーが未成熟だと局所最適が起きる

各チームが自分の作業を中心にScopeを定義すると、成功条件も
自分の担当物の完成へ寄りやすい。

例:

- 基盤チーム: Kubernetes Clusterを構築する
- 開発支援チーム: TemplateやPortal機能を提供する
- 運用チーム: 監視とChange Managementを整備する
- AIチーム: BotやAgentを提供する

それぞれの作業が技術的に完成しても、利用者にとって一つのServiceとして
利用可能になるとは限らない。

特にPlatform Engineeringでは、従来のPlatform Teamが基盤サービスを
中心に考えると、次の接続が後付けになりやすい。

- 社内サービスとしての利用体験
- 基盤サービス
- 開発支援サービス
- 運用サービス
- Enablement
- Supportと例外処理

これらを利用者から見たトータルサービスとして設計しなければ、
各チームは自分の成果物を完成させても、チーム間の境界で待ち時間、
意味の不一致、責任の空白、手戻りを作る。

## 4. 作業の中心ではなく、接点をScopeの中心にする

多くの場合、活動を始める時には「やること」の中心を定義する。

```text
Kubernetes Clusterを構築する
AI Advisorを作る
Platform Portalを導入する
監視基盤を整備する
```

しかし、この定義では作業の中心だけがScopeになり、利用者へ渡す境界が
Scopeの外へ押し出されやすい。

本来気にすべき中心は、利用者へどのようにハンドオーバーできるかという
接点ではないか。

その接点には、少なくとも次が含まれる。

- 利用者は何を渡せばよいか
- 何を受け取れるか
- どの前提条件が必要か
- Serviceは何を保証するか
- 誰が何に責任を持つか
- いつ利用でき、いつ応答されるか
- 標準と例外をどう判断するか
- 利用者は次の工程へ進めるか

この接点を作業Scopeの中心に置くことを、API設計になぞらえて
Contract Firstと捉える。

## 5. Contractは狙って提供する体験を定義する

「Contractは接点で起こりうる全て」という表現から議論を始めたが、
ここではContractと体験を次のように区別する。

- Contract: 利用者との接点で、Serviceが狙って提供する状態、約束、
  責任境界、意味、制約
- Experience: Contractを起点に利用者が実際に経験したこと

人はPlatformの内部実装を直接体験するのではなく、Platform Teamとの
Contractを通じてPlatformを体験する。

```text
どう使えばよいか
何を渡せばよいか
何が返ってくるか
誰が責任を持つか
例外時にどう進めるか
```

これらが不明な時、利用者からは「これ、どう使えるの？」という問いが出る。
これはEnablement不足であるだけでなく、Contractが十分に設計されていない
シグナルでもある可能性がある。

Contractを定義すれば良い体験が自動的に生まれるわけではない。
Contractは狙う体験の仮説であり、実際のExperienceとの一致は別途
観測する必要がある。

## 6. Outcome Drivenな社内サービスはContract Firstになる

成功する社内サービスでは、自分たちが提供できる機能を積み上げるのではなく、
最初に利用者と組織に必要なOutcomeを定義する。

```text
利用者と組織に必要なOutcome
  ↓
利用者とのContract
  ↓
社内サービスとして必要な体験
  ↓
基盤サービスに必要な能力
  ↓
開発支援サービスに必要な能力
  ↓
運用サービスに必要な能力
  ↓
各チームの実装と作業
```

この順番で考えると、基盤、開発支援、運用の要求は、それぞれのチームが
独立して決めるものではない。利用者にどのOutcomeと体験を提供するかから
逆算して決まる。

したがってContract Firstとは、単にInterface仕様を先に書くことではない。

> 最初に必要なOutcomeと利用者への約束を定義し、その約束を成立させる
> トータルサービスを各役割へ分解すること。

## 7. Outcomeのリマインドが技術バトルを防ぐ

個人的な経験では、Outcomeが現場へ継続的に伝えられない場合、
各チームは自分が判断できる技術や作業の論点へ戻り、技術バトルや
局所最適が起きやすい。

一方、プロジェクトポートフォリオ管理基盤の導入では、
プロジェクトオーナーが繰り返し、次のOutcomeをチームへ伝えていた。

- 一か月前の集計結果ではなく、現在の情報で意思決定したい
- 手作業の集計に人を使い続けたいわけではない
- 欲しいのはツールそのものではなく、リアルタイムに意思決定できる状態

この例では、ポートフォリオの仕組み、利用するツール、データ生成、
PMOの仕事が、一つのOutcomeから逆算されていた。

この観察からは、Visionを最初に示すだけでなく、作業の途中でも
リマインドし続けることが、Contractと日々の判断を接続する働きを
持つ可能性がある。

これは単一の経験に基づく例であり、一般的な有効性を実証するものではない。

## 8. VSMはContractと実際のExperienceの差を検証する

Contract Firstで設計するのは、狙って提供したいExperienceとOutcomeである。
実際にその体験が提供されたかは、Value Streamを観測しなければ分からない。

VSMまたはMBPMでは、作業時間だけでなく次を確認する。

- 利用者が必要な情報へ到達できたか
- 次の役割へ渡すための条件が明確だったか
- ハンドオーバーに待ち時間が発生していないか
- 責任や判断の空白がなかったか
- 後工程で確認と手戻りが増えていないか
- AI導入によるボトルネックがどこへ移動したか
- 利用者は意図したOutcomeへ近づいたか
- Platform TeamやOperationsに新しい負荷が生まれていないか

```text
Contractで狙ったExperience
  ↓
実際のValue Streamを観測
  ↓
差分、待ち時間、手戻り、責任の空白を発見
  ↓
ContractまたはService設計を更新
```

Contract Firstは事前設計、VSMは事後測定という一方向の関係ではない。
Contractを仮説として置き、実際のExperienceを観測し、Contractと
トータルサービスを更新する循環として扱う。

## セッションでの接続候補

```text
AIで何が速くなったか？
  ↓
Value Stream全体ではなく、生成・実装工程
  ↓
では、増えたOutputはどこへ渡されるか？
  ↓
ハンドオーバーと後続工程を見る
  ↓
各チームの作業完了ではなく、利用者のOutcomeを見る
  ↓
利用者とのContractを先に定義する
  ↓
Contractからトータルサービスを逆算する
  ↓
VSMでContractどおりのExperienceになったか測る
```

短い表現候補:

> AIが速くするのは作業です。価値を速くするには、作業の間にある
> Contractとハンドオーバーを設計する必要があります。

> Platform Serviceを基盤から積み上げるのではなく、利用者とのContractから
> 基盤・開発支援・運用を逆算する。

> Contractは狙う体験の仮説であり、VSMは実際の体験との差を検証する。

## 未検証の点

- AI導入時に、どのハンドオーバーが最初にボトルネックになりやすいか
- 局所的な生成・実装速度の上昇が、トータルサービスのOutcome低下へ
  つながる条件
- Contract Firstによって、責任の空白や手戻りをどの程度減らせるか
- Contractをどの粒度で記述すれば、各Serviceへ分解可能になるか
- Contractを明示した場合としなかった場合の比較
- 個人的な成功・失敗観察を、公開可能で検証可能な事例へ変換できるか
- Agile、DevOps、AI Slopの構造的類似が、説明上の比喩を超えて
  どこまで成立するか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
