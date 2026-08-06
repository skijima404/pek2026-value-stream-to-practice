---
id: RN-20260806-194532-platform-advisor-selection-vsm-and-mbpm
type: raw_note
title: "Platform Advisor物語のPlatform選択VSMとMBPM"
content_language: ja
created_at: 2026-08-06T19:45:32+09:00
content_origin: mixed
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
# Blank scaffolds remain unreviewed until their human author fills and finalizes them.
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-06T20:39:38+09:00
sanitization_checked_by: agent:codex
tags: [platform-advisor, vsm, mbpm, platform-engineering, process-analysis, user-research, selection-bias]
---

# メモ

Platform Advisorの続きとして、Platformの選択までのVSMを次のように置く。

## VSM初期案

1. システムの構想スタート
2. 利用可能なインフラ調査
   - ここはMBPMで深掘りする
   - ドキュメントを読んで情報収集（PT 4h、LT 9h、手戻り率 40%）
   - わからない点をまとめてPlatform Teamに聞く（PT 3h、LT 1週間、手戻り率 50%）
3. インフラサービス決定
   - 比較観点整理（PT 10h、LT 10h）
   - 意思決定（PT 3h、LT 1週間、手戻り率 20%）
   - ADR記述（PT 1h、LT 1h）
4. 利用方法詳細調査
   - 申請方法調査&確認（PT 3h、LT 10h）
5. スケジュール想定作成

## MBPMでの深掘り

### 担当者：ドキュメントを探す

- PTは4hだが、ドキュメントが探しきれなくて他の人にドキュメントのありかを聞いたりしている。そのため、聞いて回って場所を特定する時間があり、返答待ちなどで時間がかかっている。
- PTの内訳は、自分での調査が2h程度、読む時間が2h程度。
- 読んだ結果として求めていた情報が足りず、さらに追跡調査が40%発生する。例えば、社内資料を読んだ後、Cloud Serviceのドキュメントなどで調査する。

### 担当者：わからない点をまとめてPlatform Teamに聞く

- 質問リストのまとめと、メールのやり取りまたはMeetingに3h程度かかる。まとめそのものにはそれほど時間はかからないが、まとめる時間を確保するまでに2日かかる。
- 一往復で終わらないPatternが50%ある。
- Platform Teamはメールを受け取り、返答を返すまでにおおよそ3日かかる。
- 1週間は5 business daysとする。

### インフラサービス決定

- 比較検討整理は資料作成。
- 意思決定のPT 3hの内訳は、資料作成が2h、Meetingが1h。
- MeetingではProject Ownerとの合意形成が必要。MeetingのScheduleを調整し、おおよそ1週間、Meetingまで待つ。
- 20%の確率でProject Ownerの合意が得られず、再度Meetingを実施する。
- ADR記述は1h。

### 利用方法詳細調査

- 申請方法、Platform Teamとの役割分担、想定作業Lead Timeなどを調査する。PT 3hは実際に調査をしている時間。
- Platform Teamへの問い合わせが発生し、回答までの経過時間は7h。担当者の調査PT 3hと合わせ、この工程全体のLTを10hとする。
- Platform Teamでは問い合わせを受けておおよそ2hの作業で返答する。ただし、TicketのRoutingや担当者の空き待ちで5hかかる。

## Interview対象のSelection Bias候補

Platform Teamは、たまたまそのPlatformを使ったTeamにInterviewしたのかもしれない。

Platformを採用できたTeamは、情報探索や比較、Platform Teamとのやり取りに苦労しながらも、最終的に選択と採用まで到達したTeamである。そのため、彼らの回答からは「どのPlatformをどのような場合に使えばよいか分からない」という課題が強く見える。

一方で、Platformを使わなかったTeam、比較を始めなかったTeam、または自分で選びたいと思っていない利用者はInterview対象に入っていない。この対象選定の偏りによって、「利用者に選択のための情報を与えればよい」というPlatform Teamの初期仮説が強化された可能性がある。

## 訂正履歴

<!-- 誤りを直す場合は元の記述を消さず、provenance-schema.mdの形式で追記する。 -->
