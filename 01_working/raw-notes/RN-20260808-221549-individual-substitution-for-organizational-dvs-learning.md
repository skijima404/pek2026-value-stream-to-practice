---
id: RN-20260808-221549-individual-substitution-for-organizational-dvs-learning
type: raw_note
title: "例外的な個人による組織的DVS学習Capabilityの局所代行"
content_language: ja
created_at: 2026-08-08T22:15:49+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-08T22:21:40+09:00
sanitization_checked_by: agent:codex
tags: [data-contract, dvs, individual-dependency, organizational-learning, platform-adoption, practitioner-experience, social-implementation]
---

# メモ

`HYP-20260807-232639-dvs-learning-sustains-ovs-quality`のU2とU3を検討する対話で、
組織的なDVS学習Capabilityが制度化されていなくても、Value、意思決定、Data、利用ルール、
利用者Impactおよび技術を接続できる個人が、局所的にその機能を代行することで、
一回の変更が成功する場合があるという実践者の見解が提示された。

## 基盤導入と社会実装の間にある接続

Project Portfolio ManagementやITSMの基盤は、存在すること自体がValueではない。
Processを回すだけなら、対象と規模によってはSpreadsheetなどの代替手段でも実行できる。
それでも共通基盤を導入する場合は、基盤によって得たい効果と、改善したい意思決定が
あるはずだという見解が示された。

例えばProject Portfolio Managementで、Projectを横断的に把握し、予算と人員を管理し、
制約内でPortfolio Goalへどこまで近づけるかを判断したい場合、次の接続を定義する必要がある。

1. 得たいValueと改善したい意思決定
2. 誰が、いつ、何を判断または実行するか
3. 判断に必要なData
4. Dataに必要な粒度、鮮度および品質
5. 入力・更新Owner
6. MandatoryとOptionalの境界
7. Platform設定、利用ルールおよびEnablement
8. 実際の判断とOutcome

この接続から、どのFieldを、どの粒度で、どの時点までに入力すべきかというRuleを
導けるはずである。各Fieldについて「この情報がなければ、誰が、どの判断をできなくなるか」
を説明できるなら、必要な粒度、更新頻度、入力OwnerおよびMandatory条件を決めやすい。

一方、製品にFieldがあることを出発点に入力を求めると、Mandatory FieldがValueのために
必要な情報ではなく、System上埋める必要がある欄になる可能性がある。

## 名目的な利用とValueを生む利用

技術を導入しても、利用Levelを分けず、どこまでをMandatoryとし、どこからを利用者の
選択に委ねるかを定義しなければ、利用者は組織ルールを満たす最低限のFieldだけを入力する
状態になり得る。

この対話では、利用を少なくとも次のように分ける必要があると整理した。

- 組織ルールを満たすための最低限の利用
- 業務を成立させるための利用
- 利用者がValueを感じて選ぶ任意利用
- 期待したOutcomeまたは意思決定の改善へ接続する利用

登録件数、Login数またはMandatory Fieldの入力率だけでは、期待Valueを生む利用へ
到達したかを判定できない。必要な粒度でDataが入力され、実際の判断またはActionに使われ、
別のSpreadsheetやChannelで同じ情報を再構築していないかも確認する必要がある。

## 例外的な個人による局所代行

実践者の見解では、組織がこの社会実装の接続を定義しない場合が多い。一方、ごく稀に、
得たいValueから意思決定、Data、粒度、利用ルール、利用者ImpactおよびPlatform設定までを
理解し、個人として接続できる人がいる。その個人が組織的DVS学習Capabilityを局所的に
代行すると、一回の変更では期待Valueを達成できる場合がある。

ここでいう「理解している人」は、個人属性または肩書ではなく、次の観測可能な行動を指す。

- 得たいValueと改善したい意思決定を明示する
- 意思決定に必要なDataと粒度を定義する
- Mandatory、Optional、入力Ownerおよび更新条件を定義する
- 利用者Impact、副作用およびCost移転を事前に検討する
- Platform設定、利用ルールおよびEnablementを接続する
- Outcomeを観測して十分性を判断する

この個人が行った判断、適用条件および学びが組織へ保持されなければ、担当者またはContextが
変わった時の再現性は脆い。逆に、同じ個人が複数Cycleで継続的にこの機能を果たせる場合は、
形式的な組織Processが必要条件であるという主張への反例候補になり得る。

したがって、継続的なOVS品質に必要なものを、制度または形式的Processの存在だけで
定義しない。DVSの中で、個人または仕組みが、各Cycleで学習機能を実際に果たし続けられるかを
確認する必要がある。

## この記録の位置づけ

- この内容は、実践者の経験に基づくMechanism候補である。
- 「多い」または「ごく稀」は定量的な発生率ではなく、実践者による定性的な頻度表現である。
- 例外的な個人の存在、個人依存の頻度、社会実装の成功率または因果効果を検証した記録ではない。
- 特定の製品、組織、顧客、案件または個人を示す内容は保存していない。
- このRaw Noteは、対象HypothesisのEvidence Coverage、Finding、Applicabilityまたは
  Episode全体の結果を更新するEvidenceではない。
- U2における個人によるCapability代行と、U3におけるValueからData・利用ルールへの変換を
  今後検証するためのSource候補である。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
