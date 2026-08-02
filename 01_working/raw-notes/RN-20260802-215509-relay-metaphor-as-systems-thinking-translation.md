---
id: RN-20260802-215509-relay-metaphor-as-systems-thinking-translation
type: raw_note
title: "リレー比喩でシステム思考を説明する設計判断"
content_language: ja
created_at: 2026-08-02T21:55:09+09:00
content_origin: human_direct
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-02T22:11:12+09:00
sanitization_checked_by: agent:codex
tags: [presentation-design, relay-metaphor, systems-thinking, handover, vsm, mbpm, metric-based-improvement, rejected-alternative]
---

# メモ

リレーの表現はシステム思考の例えなんだけども、今回は「システム思考」の言葉を使わない。  
「システム思考」といった瞬間にシステム思考の説明をしないといけなくなるんだけども、今回はシステム思考を全面に押し出したいわけじゃないので、イメージだけつけば良い。

今回は、改善策がシステム全体へ与えた影響を検証するため、主要な観測ポイントをメトリックで計測する。個別のStepが速くなったことではなく、全体の所要時間や後続工程の手戻りまで含めて改善したかを確認する。

リレーの例で例えると、「全体のタイムが縮んだけど、これが今回のSolutionのおかげかどうかわからない」というのは、不確実性を高めて、その後の改善活動が混乱するので。  
早くなったなら、改善策、例えばバトンパスのやり方を変えたことが全体のタイムに影響したのかどうかがわかるようにしないといけない。

バトンパスのやり方を変えても、例えばバトンパスの後で失速する要因を逆に作っているようであれば問題なので (例えばバトンの持ち替えとかね)、主要な観測ポイントと全体の所要時間は計測する。

VSMやMBPMを使うのはそのためです。LT/PT/手戻り率などで数字的に表現できるし、明らかに数字の大きな場所など、改善したらインパクトが大きそうなところにより検討時間を割くことで、効率的に効果を出しにいける。

ただ比喩はやっぱり比喩で、本来ならまあKnowledge Workerの仕事の方が複雑。そういう意味ではこの比喩には限界はある。

リレー以外だと、F1レースとか、その中でも特にピットインかなあ。  
ただこれ
- わからない人はわからない。
- ハンドオーバーの話ができなさそう。(社内サービスだとかのレイヤーの違いが表現できない。)


## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
