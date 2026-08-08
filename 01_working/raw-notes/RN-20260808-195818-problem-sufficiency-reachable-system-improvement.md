---
id: RN-20260808-195818-problem-sufficiency-reachable-system-improvement
type: raw_note
title: "定義した問題への十分性と到達可能なEnd-to-End改善"
content_language: ja
created_at: 2026-08-08T19:58:18+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-08T20:06:12+09:00
sanitization_checked_by: agent:codex
tags: [decision-sufficiency, dvs, hypothesis-validation, itsm, ovs, problem-definition, practitioner-experience, systems-thinking]
---

# メモ

`HYP-20260807-232639-dvs-learning-sustains-ovs-quality`の検証設計について、
DVSの仮説検証と学習品質、OVSへの効果、システム思考、および問題解決の十分性を
対話で整理した。

このRaw Noteは、実践者が共有した経験、約15年前のITSM事例の記憶、および対話中に
形成した整理を保存する。元のDashboard、問い合わせData、報告資料または当時の
計算式は、このRepositoryでは確認していない。

## DVSの品質が低い場合に起きること

実践者は、DVSの品質が低い場合、次の段階で失敗することが多いと説明した。

- POが企画段階で方向性を外す
- 作る段階で、実装者が悪い意味で言われた通りに作る
- POの意図が伝言ゲームによって実装へ正しく伝わらない
- MarketingまたはEnablementに失敗する

その結果、作られたものが使われないことがある。組織のRuleによって使わざるを
得ない場合でも、大きな効果が出ないことがある。したがって、Platform Serviceが
想定通りに使われる地点まで到達すること自体が、最初から高い確率で起きるとは
限らない、という実践上の認識が示された。

利用されなかった場合、「なぜ使われなかったのか」を振り返らなければ、企画、
意図伝達、実装、Marketing、Enablement、利用側ProcessまたはContextのどこに原因が
あったかを区別できない。したがって、OVSへ継続的な変化をもたらすには、DVSで
仮説検証を行い、非利用、想定外利用および効果不足を次の判断へ戻すことがMandatoryな
条件である、という実践者の見解が示された。

この見解は、同一Platform Serviceを複数のReleaseまたはContext変化にわたって比較した
検証結果ではない。実践者は、全く別のProjectの失敗事例を複数見てきた一方、同一の
Platform ServiceについてDVSの学習品質とOVS品質を追跡した記録は、現時点では
持っていないと説明した。また、日本のWaterfall型Projectに関する言及は、母集団を
測定した統計ではなく、実践者が接した事例範囲についての説明である。

## システム思考によるITSMの継続改善

実践者は、ITSMではProcessの振り返りを含めて継続的に改善した経験があり、これを
システム思考の事例として説明した。この経験範囲に関する既存記録として、
`RN-20260804-013224-itsm-metrics-analysis-practice`がある。

改善では、最初にFactをDataとして押さえ、事象のPatternを捉える。そこからActor、
Handoff、Delay、Feedbackおよび制約を把握し、事象がなぜ発生するかという因果を
分析する。そのうえで、現在操作可能な原因またはLeverage Pointへ介入する。

介入がうまくいかなかった場合は、単にSolutionを繰り返すのではなく、次のどこで
外したかを分析する。

- Dataの取得または分析
- Data分析後の利用者またはContextの深掘り
- 原因仮説
- 選択したSolution
- 適用または実行

同じ問題を解消するため、分析結果に応じて別の方法を試す。実践者の記憶では、
最初の介入で狙った効果が出る割合は当初約2割であり、経験を重ねた最終的な時期には
約7割になった。この割合の定義、分母、対象期間、Project別内訳および当時の集計資料は
現在確認できないため、独立検証済みの成功率または一般的な効果量として扱わない。

## 連休明けのPassword Reset問い合わせ

約15年前、あるIT ServiceのSupport Centerでは、月曜日の午前中、特に9時から11時頃に
問い合わせが集中していた。問い合わせ傾向を分析したところ、約6割がPassword Resetに
関するものだった。Password Resetだけを時系列で見ると、連休明けの9時から11時に
特に問い合わせが多かった。

追加分析では、連休中にPasswordの有効期限を迎え、休み明けに利用できなくなることが、
問い合わせ集中の発生要因として特定された。当時の関心事はSupport CenterのCostだった。
月曜日午前のPeakに合わせて人員を配置すると、月曜日午後や週後半の午後などの平常時に
人員余剰が生じる。そのため、問い合わせ需要の平準化を目的とした。

当時利用できる手段には制約があった。連休前にPasswordの有効期限へ注意するよう促す
Campaignを実施したところ、実践者の記憶ではPassword Reset問い合わせが従来の半分以下に
減った。実践者は、定義した問題であるPeak需要と余剰Capacityに伴うCostに照らして、
この減少は妥当な効果だったと評価している。

当時の報告資料には、連休明けのPassword Reset集中、月曜日午前の需要Peak、Peak基準の
人員配置による余剰Cost、連休前Campaignによる平準化という因果と介入内容を記載していたと、
資料作成者本人が確認した。報告資料自体は現在残っておらず、このRepositoryでは
再確認できない。

このCaseでPassword認証または有効期限という深い原因を完全に解消するには、当時の
手段を超える変更が必要だった可能性がある。現在から見れば、より深い解消はPasskeyなどの
認証方式まで到達し得る。一方、当時の目的は認証問題全体の根治ではなく、Support Centerの
需要Peakを平準化してCostを抑えることだった。

問い合わせが時間帯間で移動したのか、総件数も減ったのか、実際の人員配置またはCostが
どこまで変化したのか、利用者の作業、業務開始Delay、別Channelへの移動またはSecurityへの
影響がどうだったかは、現在の記憶とRepository内の資料からは確認できない。

## 手の届く限りのEnd-to-End

実践者は、根本原因へ毎回完全に到達することが、常に最善とは限らないと説明した。
根本原因は深い構造にあり、現在の権限、技術、時間またはCostでは完全な解消が難しい場合が
ある。そのため、自分たちが手を伸ばせる価値のEnd-to-Endでシステム思考を行う。

最初に、到達可能な範囲で一度効果を出す。その方が早く、確実な場合がある。その効果が
限定的であり、さらに価値が見込める場合は、次のCycleで観測または介入の境界を広げる。

この整理では、問題解決の品質を、最深部の根本原因を完全に除去したかだけでは評価しない。
定義した問題と現在の意思決定Scopeに対して、介入が十分な効果を生んだかを評価する。
同時に、残存問題、制約、Cost移転、適用範囲および次に境界を広げる条件を明示する。

実践者は、問題解決に慣れていない人が、最初に定義した問題の内容を途中で忘れ、問題を
どこまでも解決しようとすることがあると指摘した。その場合、現在必要な価値へ早く到達する
代わりに、変更困難な根本原因または広すぎるSystem全体を解こうとしてしまう。

## この記録の位置づけ

- ITSM Caseは、Platform ServiceのDVSとOVSを直接比較したCaseではない。
- Caseの数値は、当時Dataを分析して報告した内容に関する実践者の記憶であり、元資料を
  現在確認した結果ではない。
- 仮説検証がOVSの継続的改善にMandatoryであるという説明は、
  `practitioner_experience`に基づく見解であり、このRepositoryで独立検証した結論ではない。
- Problem、Value、介入、期待Signalおよび判断十分性を接続する考えは、今後のU1
  Operational Definition候補であり、現時点のEvidence CoverageまたはFindingではない。
- 「定義した問題に対して十分か」という判断は、完全な根治、技術的な理想状態、
  OVS品質の達成そのもの、およびArtifact採用とは区別する必要がある。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
