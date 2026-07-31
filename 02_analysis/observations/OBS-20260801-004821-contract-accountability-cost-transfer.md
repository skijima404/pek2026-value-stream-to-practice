---
id: OBS-20260801-004821-contract-accountability-cost-transfer
type: observation
title: "ハンドオーバーとContractとCost Transferを分ける考えが記録された"
content_language: ja
created_at: 2026-08-01T00:48:21+09:00
created_by: agent:codex
status: reviewed
reviewed_at: 2026-08-01T00:53:44+09:00
reviewed_by: human:kijima
review_scope: intent_alignment
confidence: high
relations:
  - type: derived_from
    target: RN-20260731-190847-ai-slop-paper-to-platform-service
  - type: derived_from
    target: RN-20260731-200122-handover-contract-accountability-transfer
  - type: derived_from
    target: RN-20260731-201346-platform-service-rejection-authority-and-duty
---

# 観察

## 根拠箇所

- `RN-20260731-190847-ai-slop-paper-to-platform-service` の
  「生成の自由と共有資源への投入責任」「Accountability」
- `RN-20260731-200122-handover-contract-accountability-transfer` の
  「三層への分解」「未成熟なContractがコスト転移を生む」
- `RN-20260731-201346-platform-service-rejection-authority-and-duty` の
  「Decision Authority、Duty、Accountability」の分離

## 根拠から直接言えること

作成者は、AI生成物またはPlatform Serviceを他者へ渡す場面を、次の三層に分ける
考えを記録している。

- `Handover`: 仕事または成果物を移管するEvent、Timing、手続き
- `Contract`: 期待値、前提、受入条件、保証範囲、非対象、責任境界
- `Accountability / Cost Transfer`: 理解、検証、判断、説明、失敗Riskを
  実際に誰が引き受けるか

成果物だけが渡され、Contractが不明確な場合、受け手が前提の調査、不足の補完、
利用可否の判断、失敗Riskを引き受ける状態が記録されている。形式上のHandoverが
完了していても、作成側で省かれたCostが受け手へ移る可能性がある。

また、AI生成物は共有されるまでは候補であり、PR、Document、Template、Golden
Path、Platform Serviceなどとして共有する時点で、提供者が理解、検証、採否判断、
根拠と限界の説明を引き受けるという考えが記録されている。

Platform Team内部については、未検証案を共有資源へ流さないために、次を分ける
考えも記録されている。

- `Decision Authority`: 採用、保留、棄却を決める権限
- `Duty`: 価値仮説の弱い案を未検証のまま流さない義務
- `Accountability`: 進めた、止めた、捨てた理由を説明する責任

## 曖昧さと限界

- ここでいう`Contract`は、法的契約またはAPI仕様に限定されない暫定的な概念である。
- Contractの成熟度と下流Costの因果は、実際のService比較で検証されていない。
- Decision Rightsの配置は組織ガバナンスに依存し、一般的な正解は記録されていない。
- AI Slopの原因をContract不足だけに限定する根拠はない。
- このObservationは、Contractを登壇の中心概念として採用する判断ではない。

## 公開安全性確認

- checked_at: 2026-08-01T00:53:44+09:00
- checked_by: agent:codex
- result: `not_needed`
- scope:
  このObservationの本文、frontmatter、relationの組み合わせを、
  `proposed`から`reviewed`へ変更する時点で再確認した
- finding:
  顧客、案件、非公開の個人、商用条件、内部System、認証情報、再識別に
  つながる組み合わせは確認されず、本文の変更や削除は行っていない
- limitation:
  公開安全性の確認は、Observationの内容が一般的に正しいことを意味しない
