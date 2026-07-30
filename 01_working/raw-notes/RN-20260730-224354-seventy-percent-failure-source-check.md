---
id: RN-20260730-224354-seventy-percent-failure-source-check
type: raw_note
title: "70%失敗説の出典探索と不採用判断"
content_language: ja
created_at: 2026-07-30T22:43:54+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-07-30T22:46:57+09:00
sanitization_checked_by: agent:codex
tags: [presentation-planning, external-research, failure-definition, scaled-agile, business-outcome]
---

# メモ

## 出発点

次のような一般論をどこかで見た記憶があり、出典候補を探索した。

> プロジェクトの7割はBusiness Outcomeを達成できず失敗する。

本だった可能性や、Scaled Agileが参照している資料だった可能性を考えた。

ただし、「70%」という数字は次の異なる対象や失敗定義で繰り返し
使われているため、同じ主張として扱わない。

- プロジェクト
- 戦略的施策
- 組織変革、Change Effort、Transformation
- Digital Transformation
- 期限、予算、成果物の達成
- 当初目標、Business Intent、Business Outcomeの達成

## 確認した候補

### Scaled Agileの「70%以上」

Scaled Agileの `Why SAFe?` には、次の記述がある。

> Research shows that more than 70 percent of transformations fail.

参照先:

- https://scaledagile.com/what-is-safe/why-safe/

ここで対象になっているのは、個々のプロジェクトやPlatform Serviceではなく
`transformations` である。Business Outcome未達率として直接利用できる
記述ではない。

会話の最後には、記憶にあった数字はこの主張だった可能性が高いと考えた。

### PMI Pulse of the Profession 2017

PMIの2017年調査では、69%のプロジェクトが `original goals and business
intent` を達成したと報告されている。

参照先:

- https://www.pmi.org/learning/thought-leadership/pulse/pulse-of-the-profession-2017

これは「約7割が未達」ではなく、「約7割が達成」であり、探していた主張とは
逆だった。一時はこの資料の記憶かと考えたが、その後取り下げた。

この資料は、プロジェクト成功を期限や予算だけでなく、当初目標や
Business Intentまで含めて見る考え方の参照候補にはなる。ただし、
「7割がBusiness Outcomeを達成できない」という根拠にはならない。

### プロジェクトの目的未達に関する書籍の表現

書籍の序文には、約70%のプロジェクトが目的を達成できていないという
表現も見つかった。

> Today, about 70 percent of projects fail to deliver their objectives.

ただし、ここで使われているのは `objectives` であり、
`Business Outcome` と同じ定義であることは確認できなかった。また、
今回探していた記憶の出典であるとも確定しなかった。

### Standish CHAOSを使ったSAFe上の解説

SAFe Fellow Blogには、Standish CHAOS 2020を用いたAgileとWaterfallの
比較がある。

参照先:

- https://framework.scaledagile.com/blog/safe-fellow-blog-improving-decision-latency/

ここでは成功を `On Time, On Budget, with a satisfactory result`、
失敗を `cancelled or results not used` と定義している。

したがって、この数字もBusiness Outcome未達率とは区別する必要がある。

## 今回の判断

「変革の70%以上が失敗する」というScaled Agileの記述は確認できたが、
今回のセッションには入れない。

理由:

- Platform ServiceやプロジェクトのBusiness Outcome未達を直接示す数字ではない
- `transformation` の失敗定義が、今回検証したい価値仮説の定義と一致しない
- BCGの10-20-70 Ruleと並べると、別の意味を持つ二つの「70」が混同されやすい
- 数字のインパクトに対して、今回の主張を直接支える力が弱い
- 25分の本編で失敗率の定義に説明時間を使うより、価値仮説と
  Value Streamの実践へ時間を使いたい

この探索結果は、本編で採用する外部根拠ではなく、候補を確認して
不採用にした判断ログとして残す。

## この探索から残った注意点

「プロジェクトの70%が失敗する」という表現を使う場合は、少なくとも
次を明示する必要がある。

- 調査対象は何か
- 何を失敗と定義しているか
- 期限、予算、成果物、利用、目的、Business Outcomeのどれを測っているか
- 調査年、母集団、回答者は誰か
- Project、Change、Transformationのどれを対象にしているか

今回のセッションでは、外部の失敗率を根拠にするのではなく、
「成果物を作ることと、意図したOutcomeを達成することは同じではない」
という構造を、価値仮説とValue Streamを使って説明する。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
