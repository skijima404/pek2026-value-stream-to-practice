#!/usr/bin/env python3
"""Focused tests for validation components and Risk Decisions."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock


MODULE_PATH = Path(__file__).with_name("validate_repository.py")
SPEC = importlib.util.spec_from_file_location("validate_repository", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidationComponentTests(unittest.TestCase):
    def write_hypothesis(self, directory: Path, row: str) -> Path:
        path = directory / "HYP-20260804-120000-example.md"
        path.write_text(
            "# 仮説\n\n"
            "## 検証対象の分解\n\n"
            "| ID | Uncertainty | Decision importance | Evidence refs | "
            "Coverage state | Finding | Applicability | Residual uncertainty |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
            f"{row}\n\n"
            "## 検証方法\n",
            encoding="utf-8",
        )
        return path

    def test_not_checked_component_has_canonical_empty_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_hypothesis(
                Path(temp_dir),
                "| U1 | 対象条件で成立するか | high | none | not_checked | "
                "unknown | unknown | 対象条件では未確認 |",
            )
            components, parse_errors = VALIDATOR.parse_validation_components(path)
            self.assertEqual([], parse_errors)
            self.assertEqual(
                [], VALIDATOR.validate_validation_components(components, set())
            )

    def test_checked_component_accepts_inconclusive_observation(self) -> None:
        evidence_id = "OBS-20260804-120001-example"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_hypothesis(
                Path(temp_dir),
                f"| U1 | 対象条件で成立するか | critical | {evidence_id} | "
                "partially_checked | inconclusive | contextual | 比較対象がない |",
            )
            components, parse_errors = VALIDATOR.parse_validation_components(path)
            self.assertEqual([], parse_errors)
            self.assertEqual(
                [],
                VALIDATOR.validate_validation_components(components, {evidence_id}),
            )

    def test_checked_component_rejects_raw_note_evidence(self) -> None:
        raw_id = "RN-20260804-120001-example"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_hypothesis(
                Path(temp_dir),
                f"| U1 | 対象条件で成立するか | high | {raw_id} | "
                "partially_checked | mixed | analogous | 適用範囲が不明 |",
            )
            components, _ = VALIDATOR.parse_validation_components(path)
            errors = VALIDATOR.validate_validation_components(components, {raw_id})
            self.assertTrue(any("must reference an Observation" in error for error in errors))


class LightweightValidationTests(unittest.TestCase):
    def write_hypothesis(
        self, directory: Path, approach: str, disposition: str = "not_decided"
    ) -> Path:
        path = directory / "HYP-20260811-120000-lightweight.md"
        path.write_text(
            "# 仮説\n\n"
            "## 検証\n\n"
            f"- アプローチ: `{approach}`\n"
            "- 学習したい問い: 小さく確認できるか\n\n"
            "## 結果\n\n"
            "`not_tested`\n\n"
            "## 次の判断\n\n"
            f"- 判断: `{disposition}`\n",
            encoding="utf-8",
        )
        return path

    def write_governed_hypothesis(
        self, directory: Path, result: str, disposition: str
    ) -> Path:
        path = directory / "HYP-20260811-120000-lightweight.md"
        path.write_text(
            f"""---
id: HYP-20260811-120000-lightweight
type: hypothesis_episode
title: "軽量な検証"
content_language: ja
created_at: 2026-08-11T12:00:00+09:00
created_by: agent:codex
hypothesis_scope: session
hypothesis_level: value
status: proposed
confidence: low
knowledge_basis:
  - explicit_validation
relations:
  - type: derived_from
    target: OBS-20260811-115959-source
---

# 仮説

## 検証

- アプローチ: `research`

## 結果

`{result}`

## 次の判断

- 判断: `{disposition}`
""",
            encoding="utf-8",
        )
        return path

    def test_accepts_outcome_delivery_approaches(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            for approach in ("experiment", "research", "interview", "not_selected"):
                path = self.write_hypothesis(Path(temp_dir), approach)
                self.assertEqual(
                    (approach, []), VALIDATOR.parse_validation_approach(path)
                )

    def test_rejects_noncanonical_approach(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_hypothesis(Path(temp_dir), "expert_review")
            approach, errors = VALIDATOR.parse_validation_approach(path)
            self.assertEqual("expert_review", approach)
            self.assertIn(
                "non-canonical validation approach: expert_review", errors
            )

    def test_accepts_canonical_dispositions(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            for disposition in (
                "proceed",
                "revise",
                "validate_further",
                "stop_for_current_scope",
                "not_decided",
            ):
                path = self.write_hypothesis(
                    Path(temp_dir), "research", disposition
                )
                self.assertEqual(
                    (disposition, []),
                    VALIDATOR.parse_validation_disposition(path),
                )

    def test_rejects_noncanonical_disposition(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_hypothesis(
                Path(temp_dir), "research", "accept"
            )
            disposition, errors = VALIDATOR.parse_validation_disposition(path)
            self.assertEqual("accept", disposition)
            self.assertIn(
                "non-canonical validation disposition: accept", errors
            )

    def test_completed_result_requires_decided_disposition(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_governed_hypothesis(
                Path(temp_dir), "supports", "not_decided"
            )
            errors = VALIDATOR.validate_node(
                path,
                "hypothesis_episode",
                r"HYP-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
                {path.stem, "OBS-20260811-115959-source"},
            )
            self.assertIn(
                "completed lightweight validation requires a decided disposition",
                errors,
            )

    def test_inconclusive_can_close_for_current_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_governed_hypothesis(
                Path(temp_dir), "inconclusive", "stop_for_current_scope"
            )
            errors = VALIDATOR.validate_node(
                path,
                "hypothesis_episode",
                r"HYP-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
                {path.stem, "OBS-20260811-115959-source"},
            )
            self.assertEqual([], errors)


class RiskDecisionTests(unittest.TestCase):
    def test_proceed_with_risk_targets_existing_component(self) -> None:
        hypothesis_id = "HYP-20260804-120000-example"
        observation_id = "OBS-20260804-120001-example"
        risk_id = "RSK-20260804-120002-example"
        with tempfile.TemporaryDirectory() as temp_dir:
            directory = Path(temp_dir)
            hypothesis = ValidationComponentTests().write_hypothesis(
                directory,
                f"| U1 | 対象条件で成立するか | high | {observation_id} | "
                "partially_checked | inconclusive | contextual | 適用範囲が不明 |",
            )
            risk = directory / f"{risk_id}.md"
            risk.write_text(
                f"""---
id: {risk_id}
type: risk_decision
title: "限定範囲で先へ進む"
content_language: ja
created_at: 2026-08-04T12:00:02+09:00
created_by: agent:codex
decision_status: current
target_node: {hypothesis_id}
target_component_id: U1
risk_response: proceed_with_risk
decision_sufficiency: sufficient_with_conditions
decided_by: human:kijima
decided_at: 2026-08-04T12:00:02+09:00
relations:
  - type: evaluates
    target: {hypothesis_id}
  - type: informed_by
    target: {observation_id}
---

# 判断

限定した範囲で先へ進む。
""",
                encoding="utf-8",
            )
            with mock.patch.object(
                VALIDATOR, "find_hypothesis_path", return_value=hypothesis
            ):
                errors = VALIDATOR.validate_node(
                    risk,
                    "risk_decision",
                    r"RSK-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
                    {hypothesis_id, observation_id, risk_id},
                )
            self.assertEqual([], errors)


class HypothesisScopeTests(unittest.TestCase):
    def write_hypothesis(self, directory: Path, scope_line: str) -> Path:
        hypothesis_id = "HYP-20260804-120000-example"
        path = directory / f"{hypothesis_id}.md"
        path.write_text(
            f"""---
id: {hypothesis_id}
type: hypothesis_episode
title: "Scopeを確認する仮説"
content_language: ja
created_at: 2026-08-04T12:00:00+09:00
created_by: agent:codex
{scope_line}
hypothesis_level: value
status: proposed
confidence: low
knowledge_basis:
  - reasoned_synthesis
relations:
  - type: derived_from
    target: OBS-20260804-120001-example
---

# 仮説

Scopeの検証対象となる仮説である。

## 結果

`not_tested`
""",
            encoding="utf-8",
        )
        return path

    def validate(self, path: Path) -> list[str]:
        return VALIDATOR.validate_node(
            path,
            "hypothesis_episode",
            r"HYP-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
            {path.stem, "OBS-20260804-120001-example"},
        )

    def test_hypothesis_requires_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_hypothesis(Path(temp_dir), "")
            errors = self.validate(path)
            self.assertIn("hypothesis episode requires hypothesis_scope", errors)

    def test_hypothesis_rejects_noncanonical_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_hypothesis(
                Path(temp_dir), "hypothesis_scope: presentation"
            )
            errors = self.validate(path)
            self.assertIn(
                "hypothesis_scope has non-canonical value: presentation", errors
            )

    def test_hypothesis_test_edge_rejects_cross_scope_parent(self) -> None:
        errors = VALIDATOR.validate_hypothesis_test_edge(
            "HYP-20260804-120002-feature",
            {"hypothesis_scope": "session", "hypothesis_level": "feature"},
            "HYP-20260804-120001-solution",
            {"hypothesis_scope": "practice", "hypothesis_level": "solution"},
        )
        self.assertTrue(any("one hypothesis_scope" in error for error in errors))

    def test_hypothesis_test_edge_rejects_same_level_parent(self) -> None:
        errors = VALIDATOR.validate_hypothesis_test_edge(
            "HYP-20260804-120002-solution",
            {"hypothesis_scope": "practice", "hypothesis_level": "solution"},
            "HYP-20260804-120001-solution",
            {"hypothesis_scope": "practice", "hypothesis_level": "solution"},
        )
        self.assertTrue(any("immediately higher level" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
