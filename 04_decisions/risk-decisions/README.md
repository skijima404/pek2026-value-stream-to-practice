# Risk Decisions

Hypothesis Episode内の特定の検証対象に残るリスクへ、人間がどう対応すると判断したかを
記録します。未決定の状態ではNodeを作りません。判断を変更した場合は上書きせず、
新しいNodeから古いNodeを`supersedes`で参照します。

作成時は`templates/risk-decision.md`を使い、判断対象、範囲、理由、条件、再評価Triggerを
記録してください。`proceed_with_risk`は、限定した範囲で先へ進む判断であり、仮説を
支持するEvidenceやArtifactへの採用ではありません。
