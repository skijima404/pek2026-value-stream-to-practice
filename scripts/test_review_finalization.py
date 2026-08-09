#!/usr/bin/env python3
"""Regression tests for persisted-content review boundaries."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ANALYSIS_FINALIZER = (
    ROOT
    / ".agents/skills/finalize-analysis-node/scripts/finalize_analysis_node.py"
)
RAW_FINALIZER = ROOT / ".agents/skills/finalize-raw-note/scripts/finalize_raw_note.py"


class PersistedReviewBoundaryTests(unittest.TestCase):
    def repository(self, temp_dir: str) -> Path:
        root = Path(temp_dir)
        (root / "00_meta").mkdir(parents=True)
        (root / "00_meta/repository-contract.md").write_text(
            "# Repository Contract\n", encoding="utf-8"
        )
        return root

    def run_script(
        self, script: Path, *arguments: str
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(script), *arguments],
            capture_output=True,
            text=True,
            check=False,
        )

    def write_analysis(self, root: Path) -> Path:
        node_id = "OBS-20260809-120000-review-boundary"
        path = root / "02_analysis/observations" / f"{node_id}.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            f"""---
id: {node_id}
type: observation
title: "保存済み内容の確認"
content_language: ja
created_at: 2026-08-09T12:00:00+09:00
created_by: agent:codex
status: proposed
confidence: low
knowledge_basis:
  - recorded_statement
relations: []
---

# 保存済み内容の確認
""",
            encoding="utf-8",
        )
        return path

    def write_raw_note(self, root: Path) -> Path:
        node_id = "RN-20260809-120001-review-boundary"
        path = root / "01_working/raw-notes" / f"{node_id}.md"
        path.parent.mkdir(parents=True)
        path.write_text(
            f"""---
id: {node_id}
type: raw_note
title: "保存済みRaw Note"
content_language: ja
created_at: 2026-08-09T12:00:01+09:00
content_origin: assist_a_generated
created_by: agent:codex
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: unreviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-09T12:00:02+09:00
sanitization_checked_by: agent:codex
tags: [review-boundary]
---

# 保存済みRaw Note
""",
            encoding="utf-8",
        )
        return path

    def test_analysis_review_requires_matching_persisted_id(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_analysis(self.repository(temp_dir))
            result = self.run_script(
                ANALYSIS_FINALIZER,
                str(path),
                "--confirmed-persisted-id",
                "OBS-20260809-120000-other",
                "--reviewed-by",
                "human:kijima",
                "--sanitization-result",
                "not_needed",
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn("confirmed persisted node ID", result.stderr)
            self.assertIn("status: proposed", path.read_text(encoding="utf-8"))

    def test_analysis_review_accepts_matching_persisted_id(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_analysis(self.repository(temp_dir))
            result = self.run_script(
                ANALYSIS_FINALIZER,
                str(path),
                "--confirmed-persisted-id",
                path.stem,
                "--reviewed-by",
                "human:kijima",
                "--sanitization-result",
                "not_needed",
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertIn("status: reviewed", path.read_text(encoding="utf-8"))

    def test_raw_review_requires_matching_persisted_id(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_raw_note(self.repository(temp_dir))
            result = self.run_script(
                RAW_FINALIZER,
                str(path),
                "--title",
                "保存済みRaw Note",
                "--slug",
                "review-boundary",
                "--sanitization-status",
                "not_needed",
                "--review-status",
                "reviewed",
                "--confirmed-persisted-id",
                "RN-20260809-120001-other",
                "--tag",
                "review-boundary",
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn("confirmed-persisted-id", result.stderr)
            self.assertIn("review_status: unreviewed", path.read_text(encoding="utf-8"))

    def test_raw_review_cannot_rename_confirmed_note(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_raw_note(self.repository(temp_dir))
            result = self.run_script(
                RAW_FINALIZER,
                str(path),
                "--title",
                "保存済みRaw Note",
                "--slug",
                "changed-slug",
                "--sanitization-status",
                "not_needed",
                "--review-status",
                "reviewed",
                "--confirmed-persisted-id",
                path.stem,
                "--tag",
                "review-boundary",
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn("cannot rename", result.stderr)
            self.assertTrue(path.is_file())

    def test_raw_review_cannot_change_sanitization_status(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_raw_note(self.repository(temp_dir))
            result = self.run_script(
                RAW_FINALIZER,
                str(path),
                "--title",
                "保存済みRaw Note",
                "--slug",
                "review-boundary",
                "--sanitization-status",
                "sanitized",
                "--review-status",
                "reviewed",
                "--confirmed-persisted-id",
                path.stem,
                "--tag",
                "review-boundary",
            )
            self.assertNotEqual(0, result.returncode)
            self.assertIn("cannot change sanitization status", result.stderr)
            self.assertIn("review_status: unreviewed", path.read_text(encoding="utf-8"))

    def test_raw_review_accepts_unchanged_confirmed_note(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_raw_note(self.repository(temp_dir))
            result = self.run_script(
                RAW_FINALIZER,
                str(path),
                "--title",
                "保存済みRaw Note",
                "--slug",
                "review-boundary",
                "--sanitization-status",
                "not_needed",
                "--review-status",
                "reviewed",
                "--confirmed-persisted-id",
                path.stem,
                "--tag",
                "review-boundary",
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertIn("review_status: reviewed", path.read_text(encoding="utf-8"))

    def test_direct_human_authored_note_keeps_auto_review_exception(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = self.write_raw_note(self.repository(temp_dir))
            document = path.read_text(encoding="utf-8")
            document = document.replace(
                "content_origin: assist_a_generated", "content_origin: human_direct"
            ).replace("created_by: agent:codex", "created_by: human:kijima")
            path.write_text(document, encoding="utf-8")
            result = self.run_script(
                RAW_FINALIZER,
                str(path),
                "--title",
                "保存済みRaw Note",
                "--slug",
                "review-boundary",
                "--sanitization-status",
                "not_needed",
                "--tag",
                "review-boundary",
            )
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertIn("review_status: reviewed", path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
