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


if __name__ == "__main__":
    unittest.main()
