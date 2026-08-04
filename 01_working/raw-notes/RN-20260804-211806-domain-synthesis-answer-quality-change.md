---
id: RN-20260804-211806-domain-synthesis-answer-quality-change
type: raw_note
title: "EA Repositoryの領域別Synthesis導入と回答品質変化"
content_language: ja
created_at: 2026-08-04T21:18:06+09:00
content_origin: mixed
created_by: agent:codex
source_platform: codex
capture_mode: transcript
imported_by: agent:codex
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: 2026-08-04T21:22:59+09:00
sanitization_checked_by: agent:codex
tags: [answer-quality, blind-spot, enterprise-architecture, knowledge-base, reasoning-chain, synthesis, workslop]
---

# メモ

2026年8月4日に、Enterprise ArchitectureのRepositoryをChatbot的に利用した際の
回答品質低下と、領域別Synthesis導入後の変化について振り返ったCodex上の対話を
記録する。顧客、案件、組織、日付および内部Systemを特定できる情報は保存しない。

以下の回数と品質評価は実践者の記憶に基づく。実行Log、固定質問セット、共通の
評価尺度または第三者評価を確認したものではない。

## Chatbot的な仕組みで観測した品質低下の条件

実践者は、Chatbot的な仕組みの回答品質が低下する条件として、次の二つを
実務上観測していると説明した。

- Dataが古い、または品質が悪い場合。例えば、現在の判断へそのまま適用できない
  古い情報がKnowledge Sourceへ混在する場合
- 情報と情報をどう接続するかが明示されていない場合

過去にProjectの議事録を束ねたBotを作成した際にも、回答品質が期待より低いと
感じた。議事録を集めただけでは、結論までのSynthesisが不足していた可能性が
あると振り返っている。ただし、そのBotについて原因を分離する比較は行っていない。

## EA Repositoryの利用規模

EA Repositoryでは、一週間平均で約10ファイルを追加していた。動作確認および
実際の人間のReasoningに対する情報提供を目的として、一週間あたり約20回の
問い合わせを行っていた。

Raw Noteが約80ファイルになった頃、実践者は回答品質が明らかに低下したと認識し、
Repositoryの設計を変更した。約80ファイルはこの一件で品質低下を認識した時点で
あり、一般的な上限または閾値ではない。

品質低下時には、Analysisが存在していても回答がぼやけ、深いReasoningの痕跡を
得られないと感じた。情報量が増えるだけでは、どの情報とどの情報をどう接続して
結論へ進むかが回答時に再現されなかった。

## 領域別Synthesisへの設計変更

設計変更では、領域ごとに一つのSynthesisファイルを置いた。Synthesisファイルは、
関連情報から結論までの`Chain of Thoughts`のIndexというイメージで作成した。

本Repositoryで例えると、一つのHypothesis Episodeが一つのSynthesisファイルに
相当する。関連Source、前提および結論までのReasoningを、一つの問いまたは領域に
対して追えるようにする。

EA Repositoryでは、Folder間の参照関係を広く作らなかった。例えば、Projectの
大まかな戦略を扱うFolderと、具体的なSchedule検討を扱うFolderを分け、基本的に
横参照は多くなかった。全SourceをKnowledge Graphとして接続するのではなく、
独立性の高い領域ごとにReasoningのIndexを置く設計だった。

Synthesisファイル以外の追加施策は行っていないと記憶している。

## 設計変更後の回答品質

実践者は、領域別Synthesisファイルを追加した後、回答品質が明らかに良くなったと
評価している。

導入前の仕組みは、実践者本人の盲点を指摘しなかった。導入後は、実践者が
見落としていた内容を指摘するようになった。これは、この仕組みに期待していた
Outcomeだった。

この前後差は実践者による継続利用中の評価であり、同一質問への回答を保存して
比較したものではない。指摘内容の正しさ、網羅性および第三者に対する再現性も
この対話では確認していない。

## AI Slopとの接続についての考え

対話では、AI Slopを防ぐには、このような細かい設計調整が必要なのではないかと
考えた。

「盲点を指摘してほしい」という依頼に対して、AIが未検討に見える論点候補を示し、
人間がその内容を確認できることには価値がある。一方、AIが候補を見つけなかった
ことを根拠に、本当に盲点が存在しないかを未確認のまま信じると、Slopになり得る。

AIは利用者の認識状態を直接確認できないため、「これはあなたの盲点である」または
「盲点はない」と保証するのではなく、確認したSourceとReasoningの範囲で未検討に
見える論点候補を示し、人間による検証へ戻す必要があるという考えである。

## この記録だけでは確認していないこと

- 約80ファイルが他のRepositoryでも品質低下を生むか
- 品質低下の原因がSource量、Retrieval、Model、PromptまたはSynthesis欠落の
  どれであったか
- Synthesis以外の条件が前後で完全に同一だったか
- 盲点として示された内容の正解率、網羅性および再現性
- 領域別Synthesisが一般的なChatbotの回答品質を改善するか

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
