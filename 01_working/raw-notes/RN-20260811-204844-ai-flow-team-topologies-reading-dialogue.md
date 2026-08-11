---
id: RN-20260811-204844-ai-flow-team-topologies-reading-dialogue
type: raw_note
title: "AI、Value Flow、Team Topologiesに関する6資料の読書対話"
content_language: ja
created_at: 2026-08-11T20:48:44+09:00
content_origin: mixed
created_by: agent:codex
source_platform: chatgpt
capture_mode: transcript
imported_by: agent:codex
review_status: corrected
sanitization_status: not_needed
sanitization_checked_at: 2026-08-11T21:46:16+09:00
sanitization_checked_by: agent:codex
tags: [ai-capability, cognitive-load, complicated-subsystem, dora, interaction-mode, platform-product, team-topologies, value-flow, verification-tax]
---

# AI、Value Flow、Team Topologiesに関する6資料の読書対話

## この記録の位置づけ

Platform Engineering Kaigi 2026の登壇準備として、実践者がTeam TopologiesおよびDORAの
6資料を読み、AssistAと対話しながら考えた内容を、実践者のコメントを中心に再構成して保存する。

これは各外部資料をAgentが独立に再確認したExternal Inputではない。実践者が資料を読みながら
入力した抜粋、感想、過去の読書記憶および実務観と、AssistAが対話中に加えた整理が混在する。
したがって、以下では可能な限り次を区別する。

- 資料上の記述として実践者が抜粋または要約した内容
- その記述に対する実践者自身の読みと判断
- AssistAが行った接続、一般化または仮説化

このRaw Noteだけを、外部資料の正確な内容、現在のHypothesisのEvidence、または検証結果として
扱わない。外部主張を分析へ利用する場合は、対象ページを改めて確認してExternal Input化する。

## 読んだ6資料

### 資料数とJ-Curve参照元の訂正

保存後、実践者から、実際には次の資料も読んでいたという訂正があった。したがって、タイトル、
位置づけおよび本見出しにある「6資料」は「7資料」と読み替える。

7. `DORA: ROI of AI-Assisted Software Development`
   - https://dora.dev/ai/roi/report/

この資料は、J-Curve、Verification TaxおよびPipeline Adaptationの説明を確認するために読んだ。
後述のJ-Curveに関する記録は、`State of AI-assisted Software Development 2025`だけでなく、この
ROI Reportを参照した読書コメントに基づく。

1. `Why Team Topologies is the Essential Foundation for AI ROI`
   - https://teamtopologies.com/news-blogs-newsletters/why-team-topologies-is-the-essential-foundation-for-ai-roi
2. `AI Success — Team Topologies`
   - https://teamtopologies.com/ai-success
3. `Team Interaction Modeling with Team Topologies`
   - https://teamtopologies.com/key-concepts-content/team-interaction-modeling-with-team-topologies
4. `Key Concepts — Team Topologies`
   - https://teamtopologies.com/key-concepts
5. `Executive Report: The Organizational Foundation for AI ROI`
   - https://teamtopologies.com/all-mini-books/executive-report-the-organizational-foundation-for-ai-roi-with-team-topologies
6. `DORA: State of AI-assisted Software Development 2025`
   - https://dora.dev/research/2025/dora-report/

実践者は、過去に読んだ資料については斜め読みし、必要な箇所を読み直した。したがって、6資料を
同じ深さで精読した記録ではない。

## AIは組織Systemを増幅する

Team Topologiesの記事が引用するDORAの中心命題として、実践者は、AIは強力な
`amplifier`であり、AI Tool自体よりもその下にある組織Systemへ焦点を当てる必要があるという
説明を確認した。

実践者はこの説明を、掛け算にたとえた。AIと掛け合わせる既存の組織、Flowまたは仕事の質が
正であれば正の結果が増幅され、負であれば負の結果が増幅される。AI LicenseまたはTokenを
購入するだけでFinancial Returnが保証されないという記述は、当然だが明示する必要があるほど
市場の期待と実態がずれているものとして受け止めた。

ここから実践者が読み取った中心は、AI導入を特別な技術施策として始めるのではなく、既存の
組織System、Value Flow、Platform、責任分担およびFeedback Loopを先に扱うことである。
これは「AIも通常のApplication開発として扱う」という現在の立場と整合する。ただし、資料が
消費側Value Streamによる利用条件やDecision Rightまで明示したわけではない。

## Value Flowを中心にする理由は伝言ゲームの削減

資料では、Teamを継続的なValue Flowへ揃え、Team間Handoffを減らすことでMissionとPurposeを
明確にするという説明があった。また、CustomerとTeamの間に複数のManagement Layerが入り、
`game of telephone`になる例も示されていた。

実践者は、Value Flowを中心にする理由を、まずFeedback Cycleの短縮と伝言ゲームの削減として
理解した。Handoffが増えると、顧客価値だけでなく、背景、判断理由、制約、優先順位および
Feedbackが繰り返し翻訳される。その結果、情報が劣化し、Customerから遠ざかり、判断と学習が
遅くなる。`three layers`という数や特定の組織階層を深掘りするより、この力学を理解することが
重要だと判断した。

この因果関係の理論的な全体が資料に明示されていたとは確認していない。資料が明示したHandoff、
Customerとの直接接続および伝言ゲームを、DevOps Topologies由来のFeedback Loop短縮という
文脈で実践者が接続した解釈である。

## Team Topologiesは組織図ではなく観察用のレンズ

実践者は、四つのFundamental Team Topologiesを先に当てはめるのではなく、目の前の実際の
Team、責任およびInteractionを観察し、その属性を分類するときにTopologyを裏側へ薄く透かして
見るのがよいと考えた。

したがってTeam Topologiesは、正しい組織図を与えるTemplateというより、現実の組織を理解し、
立ち位置、境界およびInteraction Modeを検討するVocabularyまたは分類用のレンズである。
Topology自体を前面へ出すと、現実より分類を優先する危険がある。

`Team Interaction Modeling`では、Team Shapeを使って自組織のDiagramを作成する際の制約が
説明されていた。実践者は、現在のTeam Topologiesが静的な四分類だけでなく、実際の組織と
Communication Channelを描き、改善の対話を行うDiagram Formatへ発展していると受け止めた。

## 四つのTopologyと、その外側のSensing

実践者は、四つのTeam TypeをValue Flowを成立させる構成要素であり、System全体を観察して
適応させる主体そのものではないと整理した。

- 各Stream-aligned teamは、自分たちのFlow Efficiency、Outcome、待ち、手戻りおよび品質を
  自ら観察する。
- 複数のStream-aligned teamを横断し、共通の詰まり、局所最適、Topology変更またはEnablementの
  必要性を観察する機能は、その外側に必要となり得る。

実践者は後者をITSMにおけるSMOに似た機能として考えた。Platform team自身も観察対象である
ため、Platform teamへSystem全体の観察責任をすべて置くのは不自然である。一方、Platform teamは
自分たちのPlatform ProductがCognitive Loadを下げ、利用側のFlowを改善したかを観察する責任を
持つ。この局所的な自己観察と、複数Streamを横断するEnd-to-EndのSensingは分ける必要がある。

`Team Interaction Modeling`には`organizational sensing`という考え方があったが、実践者と
AssistAの読書範囲では、そのOwnerは明示されていないと判断した。MBPMは四つのTeam Typeの一つ
ではなく、Flowを観察し、次に変更すべきTeam境界またはInteractionを見つけるための手段として
この外側へ置く方が自然だと考えた。

## PlatformはConsumerのDeliveryを加速する内部Product

`Key Concepts`におけるPlatform teamは、Stream-aligned teamのDeliveryを加速する魅力的な
内部Productを提供するTeam群として説明されていた。実践者は、Platformの責任の中心が
Platform自体ではなく、内部Productを通じたConsumer側のDelivery加速にあると読んだ。

また、Platform teamの中に別のStreamが描かれたDiagramを確認し、過去に読んだ初期の書籍には
この図がなかったと記憶していた。実践者はこれを、Platformも継続的に改善されるProductであり、
PlatformをDeliveryするValue Streamを持つというPlatform Engineeringの意図的な反映と読んだ。
Stream-aligned team側をOperational Value Stream、Platform ProductをDeliveryするStreamを
それを支えるDevelopment Value Streamとして見ると理解しやすいと考えた。

初期書籍との図の差分および変更意図は、この対話では版比較によって検証していない。これは
実践者の読書記憶と今回の図から得た解釈である。

### Platform Wrapperに関する再確認

保存後、実践者は手元の2019年英語Kindle版を再確認した。書誌情報は次のとおりである。

- Matthew Skelton and Manuel Pais, `Team Topologies: Organizing Business and Technology Teams for
  Fast Flow`
- IT Revolution Press、2019年英語Kindle版
- Kindle ISBN: `978-1-942788-83-6`
- Chapter 8: `Evolve Team Structures with Organizational Sensing`
- Figure 8.8: `Example of a "Platform Wrapper"`

Figure 8.8には、`Outer Platform`の枠内にStream-aligned teamが描かれていた。周辺説明では、
下位のServiceおよびAPIをPlatform Wrapperでまとめ、上位のBusiness Streamから一つのPlatformと
して扱えるようにすることで、Flowの予測可能性、一貫したDeveloper Experience、統合された
RoadmapおよびFlowとResource利用量のTelemetryを提供する構造が説明されていた。

したがって、「初期書籍にはPlatform内のStream-aligned teamがなく、現在のWeb図で新たに
追加された」という読みは維持できない。書籍時点ですでに、利用側から依存Service群を一つの
Platformとして扱わせるWrapperと、そのDeveloper Experienceを形成するStream-aligned teamが
描かれていた。

一方、Figure 8.8の中心は、現在のPlatform Engineering全体を定義することではなく、Serviceと
APIを統合するPlatform WrapperというArchitecture Patternである。統合Interface、Holisticな
Roadmap、一貫したDeveloper ExperienceおよびTelemetryは現在のPlatform Engineering、Platform
API、Control PlaneまたはPlatform Observabilityに近い要素を持つ。しかし、Internal Productの
継続的Discovery、DeveloperをCustomerとして扱うProduct Management、Self-Service、Golden Path、
Gitを正本とする宣言的管理またはReconciliationまでは、この説明だけでは確認できない。

実践者は、このPlatform Wrapperを現在のPlatform Engineeringを構成する原型の一つと解釈した。
ただし、Platform Wrapperから現在のPlatform Engineeringへ直接発展したという歴史的因果関係を、
書籍または公式資料が明示しているとは確認していない。

## Interactionは固定せず進化させる

初期のTeam TopologiesはInteraction Modeの説明が中心だったという読書記憶に対し、今回の
`Team Interaction Modeling`は、Team間関係を時間とともに進化させることへ焦点があると
実践者は感じた。

未知の領域では、異なる専門家が`Collaboration`によって境界を発見する必要がある。しかし、
その状態が固定されると、会議、説明、レビューおよび調整が常に必要となり、Interaction自体が
Flowを重くする。また長期のCollaborationは、異なるTeamの視点やConcernを同質化し、誰が何に
責任を持つかを曖昧にする危険がある。

実践者は、必要なのは全員が同じになることではなく、それぞれがConcernに対する専門性を保った
まま接続できることであると述べた。Capabilityと境界が安定したら、Interactionを
`X-as-a-Service`へ軽量化する。これは単なる効率化ではなく、専門性と異なる視点を維持しながら
Flowの協働Costを下げる設計である。

したがって、Interaction Modeは静的に正解を選ぶ分類ではなく、未知、境界発見、Capabilityの
安定化という状態に応じて変えるものとして読んだ。ただし、すべてのInteractionが一方向に
`X-as-a-Service`へ進む成熟度Modelであると外部資料が一般化しているかは、この記録だけでは
確認できない。

## 専門性には専門性の置き場所がある

実践者は、過去のAgileにおけるFeature Team万能論に違和感を持っていた。高度な専門性を必要と
する認証基盤のようなComponentまで、各Feature Teamが個別に扱うことは現実的ではないからで
ある。Team Topologiesが`Complicated Subsystem team`を正式なTeam Typeとして認め、専門性を
否定せず、Flowを壊さない境界とInteractionを設計する点を高く評価した。

今回確認した現在の説明には`significant mathematics`という表現が含まれていた。実践者は
手元の初期書籍を読み返し、当時の説明にはこの表現が見当たらなかったと述べた。数学的専門性の
明記を、AI、Machine LearningまたはData Scienceを新しいTeam Typeとして特別扱いせず、既存の
Complicated Subsystem teamの射程へ取り込んだ変化として読んだ。

ただし、文言追加の時期、理由または公式の変更意図は確認していない。AssistAが「AIを意識した
適用範囲の拡張」と結論づけた部分は推論であり、公式見解として扱わない。

### `significant mathematics`の確認範囲

実践者が再確認した書誌情報と位置は次のとおりである。

- 2019年英語Kindle版、Kindle ISBN `978-1-942788-83-6`
- Chapter 5: `The Four Fundamental Team Topologies`
- Section: `Complicated-Subsystem Teams`

このSectionの説明では、現在の公式Webページにある`significant mathematics`という表現を
確認できなかった。これは書籍全体に当該表現が存在しないという主張ではなく、比較対象とした
Complicated-Subsystem Teamの説明Sectionに範囲を限定した確認である。

## AIを一つの箱として分類しない

実践者は、AI ProductまたはAI Capabilityを一つのTeam Typeへ丸ごと当てはめるのではなく、
責任単位へ分解する必要があると考えた。

AI Coding Productを例にすると、利用者が直接触れるIDE上のFeatureと、背後で推論を担うModelは
異なる責任を持つ。前者は利用側に近いFeatureまたはPlatform Productの一部となり得る。一方、
Modelは高度な数学、評価、Safety、最適化および運用を必要とするため、実践者の立場では
Complicated Subsystemとして捉えるのが自然である。

ここでの中心は「AIはComplicated Subsystemである」という一括分類ではない。

```text
AIを利用するProductまたはFeature
  -> ConsumerとのInteractionおよびOutcomeを扱う

Modelその他の専門Component
  -> 専門性を持つSubsystemとして提供する
```

同一Productの中に、Stream-aligned、PlatformおよびComplicated Subsystemに対応する異なる責任が
共存し得る。Team Topologiesは製品名または技術名ではなく、責任とInteractionを見るために使う
という理解である。

## AIにはWorkloadとSoftware Systemの二つの見方がある

Executive Reportには、AIとHumanのTeamがEnd-to-EndのExecutionを担うという表現があった。
実践者は、WorkloadまたはBusiness Capabilityの観点では、AIを仕事の実行を委ねるResourceとして
扱うことに強く同意した。

一方、AI ResourceはSoftwareとして提供されるため、その背後にはModel、Inference、Gateway、
Guardrail、Evaluationおよび運用を担うSoftware Systemと、それを継続的に保守するTeamが存在する。
したがって、同じAIを次の二軸で見る必要がある。

1. WorkloadまたはCapabilityの軸:
   Human、AI、Automationまたは外部Providerの誰へ仕事を配分するか
2. Software Architectureの軸:
   AIというResourceを成立させるSoftware Productを誰が開発、運用および改善するか

実践者は、WorkloadとしてはAIをResourceと考える一方、Software SystemとしてはValue Streamから
消費される提供側Capabilityであり、その提供と保守の責任境界が必要だと考えた。現在読んだ資料は
前者をよく表現するが、後者との接続が十分に描かれていないというのが実践者の問題意識である。

## DataではなくCurationが重要

Executive Reportの要約には、組織がDataとKnowledge Systemを`curate`し、AI Agentが正確な
Business ContextへAccessできるようにするという説明があった。

実践者が重視したのは`data`そのものではなく`curate`という動詞である。Dataを収集または保存
するだけでなく、選択し、意味とContextを与え、品質を維持し、利用可能な状態へ保つ活動が必要
になる。Domain Knowledge、Capability Contract、Architecture KnowledgeおよびReasoning Chainも、
単に記録するのではなく、人間とAIが判断に使えるように継続的に整えるCuration活動として
理解した。

## Team Topologiesが決めないこと

実践者は、Team TopologiesがValue FlowへTeamを揃え、専門性とPlatformを配置し、Interactionを
進化させる方法を説明する一方、「そもそも何をするか」「どの価値へ投資するか」「何をOutcomeと
するか」を誰が決めるかは十分に説明していないと考えた。

Team Topologiesの主戦場は、Portfolioで投資対象を選ぶ段階より後にあり、決めた価値を継続的に
DeliveryするSoftware Delivery Organizationの設計である。したがって、専門家または
Complicated Subsystem teamを投入する順序は次のようになる。

```text
実現すべきOutcomeと検証すべきConcernが決まる
  -> 専門性が必要な部分を識別する
  -> 専門家が再利用可能なCapabilityまたはValidation Serviceへ実装する
```

実践者は「やることが決まったらスペシャリスト集団を投入すればよい。ただし、やることが
決まった後である」と強調した。専門性の論理が、消費側Value StreamのOutcomeを上書きしてよい
理由にはならない。

この最後のConsumer側Decision Rightは、Team Topologiesが明示したRuleではなく、実践者が
Team TopologiesへValue StreamとOutcome設計を接続して置いた主張である。

## Verification Taxは観測範囲を区別する

DORAの説明として実践者が確認した`Verification Tax`は、AI OutputをDeveloperがReviewする
時間として定義されていた。したがって、DORA上の語義はDeveloperに近い限定された範囲である。

一方、実践者が問題にしているVerification Costは、Developer Reviewだけでなく、Architecture、
Security、QA、Acceptance、ReleaseおよびOperationsまで含むEnd-to-EndのValue Streamに及ぶ。
同じ`Verification Tax`という語を使う場合でも、観測範囲を明示しなければならない。

AssistAは、この広い範囲を`Enterprise版Verification Tax`と表現した。しかし、DORAの正式な
用語拡張ではない。今後の分析では、DORAの限定された定義を保ち、実践者の広い概念には
`End-to-End Verification Cost`など別の表現を使う余地がある。

## Pipeline Adaptationは次の制約を露出させる

DORAの`Pipeline adaptation`について、実践者は、個々のDeveloperがより速くCodeを生成すると、
TestingやChange Approvalなどの下流Processも増加したVolumeを扱えるようScaleする必要があり、
既存の制約を除去する機会が現れるという説明を確認した。

実践者は、Verification Taxよりもこの説明の方が、以前から述べていた「モグラ叩き」に近いと
判断した。

```text
AIで局所工程が高速化する
  -> 下流の既存制約が露出する
  -> Pipelineを適応させる
  -> 制約を改善すると次の制約が現れる
```

DORAが明示したのは、局所的なCode生成の高速化によってTestingまたはChange ApprovalのScaleが
必要となり、Legacy Constraintを除去する機会が現れるところまでである。改善後にさらに次の
制約が現れ続けるという反復的な「モグラ叩き」への一般化は、実践者のSystems Thinkingである。

したがって、以前の「AIはボトルネックを移動させる」という表現より、「AIは既存の
ボトルネックを露出させ、その改善によって次のボトルネックが支配的になる」と分けて表現する方が
Sourceと解釈の境界を保ちやすい。

## J-Curveは個人の学習だけではない

DORAのJ-Curveは、AI導入初期に一時的な生産性低下と不安定な期間が生じるという説明であり、
実践者は図中にLearning Curve、Verification TaxおよびPipeline Adaptationが並んでいることを
確認した。

これにより実践者は、J-Curveを人がAIに慣れるまでの学習Costだけではなく、検証負荷と
OrganizationまたはPipeline全体の適応Costを含むものとして読んだ。AIによる局所的な高速化が
下流制約を露出させ、Systemがそれへ適応する間に全体性能が一時的に低下し得る。

ただし、反復的な制約移動全体をDORAのJ-Curveそのものが説明しているとまでは確認していない。
J-Curveが示す最初の適応と、改善を繰り返す実践者のModelを区別する。

### J-Curve出典に関する補足

この節で扱ったJ-Curveの図と、Learning Curve、Verification TaxおよびPipeline Adaptationの
三要因は、実践者が`ROI of AI-Assisted Software Development`を読み直して確認した内容である。
元の記録がJ-Curveの確認元を`State of AI-assisted Software Development 2025`だけに見える形で
整理していた点を訂正する。

## 資料ごとの有用性に関する判断

- `Why Team Topologies is the Essential Foundation for AI ROI`:
  AIをAmplifierとして捉え、Mission、Verification、PlatformおよびValue Flowを組織Systemとして
  扱う土台になった。
- `AI Success — Team Topologies`:
  実践者が期待した組織設計または責任境界の説明ではなく、提供可能な支援を紹介するCatalogに
  近く、今回の問いに対する新しい内容は少なかった。
- `Team Interaction Modeling with Team Topologies`:
  CollaborationからX-as-a-Serviceへの関係進化、Fit for Purposeでなければ消費しない判断、
  Platform内のStreamおよびOrganizational Sensingが有用だった。
- `Key Concepts — Team Topologies`:
  Team TypeとInteraction Modeの用語確認に加え、Team TopologiesをFlow中心の観察用レンズとして
  読み直す起点になった。
- `Executive Report`:
  DataではなくCuration、Knowledge System、AIとHumanによるExecution、およびPlatform as a
  Productという経営向けの公式整理が有用だった。
- `DORA: State of AI-assisted Software Development 2025`:
  Verification Taxの限定された定義、J-Curveの複数要因およびPipeline Adaptationによる下流制約の
  露出を確認する上流Sourceとなった。
- `DORA: ROI of AI-Assisted Software Development`:
  J-Curveの図、Verification Taxの定義およびPipeline AdaptationによるLegacy Constraintの露出を
  直接確認する資料として読んだ。

## 現在のHypothesisへの含意候補

この読書対話から、次の分析候補が見える。ただし、いずれもこのRaw Noteを保存しただけでは
Hypothesisを支持またはChallengeするEvidenceにならない。

1. AI Capabilityを一つのTopologyへ丸ごと分類せず、Workload、Product Feature、Model、
   Evaluation、GuardrailおよびPlatform Serviceなどの責任単位へ分解する必要がある。
2. Complicated Subsystem teamまたはPlatform teamは専門Capabilityを提供し得るが、その存在だけで
   Consumer側のOutcome、Concernまたは利用判断を上書きするDecision Rightは導けない。
3. U4の検証では、提供Topologyの違いだけでなく、WorkloadとしてAIをResource扱いするViewと、
   AIをDeliveryするSoftware SystemのViewを同時に確認する必要がある。
4. U3の経済妥当性では、Developer Review時間としてのVerification Taxと、Architecture、Security、
   QA、ReleaseおよびOperationsを含むEnd-to-End Verification Costを分けて測る必要がある。
5. AIによる局所的な高速化の効果は、その工程だけでなく、下流Constraintの露出、Pipeline Adaptation、
   次の制約およびSystem全体のOutcomeまで追わなければ判断できない。
6. Capability Contractまたは責任境界は、四つのTeam Typeを正解として当てはめるためではなく、
   実際の責任、Interaction、ConsumerのFit for Purpose判断および例外を表すために使う必要がある。

## この記録だけでは分からないこと

- 各外部資料の正確な全文、Sectionごとの文脈および版更新履歴
- `significant mathematics`の追加時期と、その変更がAIまたはMachine Learningを意図したものか
- Platform team内にStreamを描いた図の初出、初期書籍との差分および公式の変更理由
- Team TopologiesがInteraction Modeを一方向の成熟度Modelとして一般化しているか
- `organizational sensing`を誰が所有し、どの指標とDecision Rightで運用するか
- AIをWorkload上のResourceとSoftware Productの両方として扱う二軸Modelが、Team Topologiesの
  公式整理として存在するか
- Consumer側がOutcome、Concern、Acceptance Criteriaおよび最終利用判断を所有するという
  境界原則を、外部資料または実Caseが支持するか
- DORAのJ-Curveが反復的なConstraint移動をどこまで含むか
- End-to-End Verification Costをどの単位、期間および比較対象で測定できるか
- 6資料の主張同士が、同じ定義、対象組織および観測範囲を共有しているか

### 保存後の再確認で限定できたこと

- 手元の書籍は2019年英語Kindle版、Kindle ISBN `978-1-942788-83-6`として特定できた。
- Chapter 8のFigure 8.8には、Outer Platform内のStream-aligned teamとPlatform Wrapperが
  描かれていた。
- Platform Wrapperの説明には、一貫したDeveloper Experience、統合RoadmapおよびFlowとResource
  利用量のTelemetryが含まれていた。
- Chapter 5の`Complicated-Subsystem Teams`では、`significant mathematics`という表現を
  確認できなかった。
- Platform Wrapperと現在のPlatform Engineeringの歴史的な発展関係、および
  `significant mathematics`の追加理由は引き続き未確認である。

## 訂正履歴

### CR-20260811-205152

- corrected_at: 2026-08-11T20:51:52+09:00
- corrected_by: human:kijima
- target: タイトル、位置づけ、`読んだ6資料`およびJ-Curveの参照元
- correction: 実際に読んだ資料は7資料であり、`ROI of AI-Assisted Software Development`を
  J-Curve、Verification TaxおよびPipeline Adaptationの確認元として追加する
- reason: 保存後、実践者から読了資料とJ-Curve参照元の記載漏れが明示されたため

### CR-20260811-214114

- corrected_at: 2026-08-11T21:41:14+09:00
- corrected_by: human:kijima
- target: Platform内のStream-aligned teamに関する初期書籍との差分、および
  `significant mathematics`の書籍確認範囲
- correction: 2019年英語Kindle版のChapter 8、Figure 8.8にはOuter Platform内の
  Stream-aligned teamが存在し、Platform Wrapperとして説明されていた。またChapter 5の
  `Complicated-Subsystem Teams`では`significant mathematics`という表現を確認できなかった
- reason: 実践者が手元のKindle版を、書誌情報、Chapter、SectionおよびFigure単位で再確認したため
