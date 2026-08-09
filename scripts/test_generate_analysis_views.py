#!/usr/bin/env python3
"""Tests for deterministic repository graph and analysis view generation."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("generate_analysis_views.py")
SPEC = importlib.util.spec_from_file_location("generate_analysis_views", MODULE_PATH)
assert SPEC and SPEC.loader
GENERATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GENERATOR)


class AnalysisViewGenerationTests(unittest.TestCase):
    def write_fixture(self, root: Path) -> None:
        observation_id = "OBS-20260809-120000-source"
        hypothesis_id = "HYP-20260809-120001-example"
        observation = root / "02_analysis/observations" / f"{observation_id}.md"
        hypothesis = (
            root / "02_analysis/hypothesis-episodes" / f"{hypothesis_id}.md"
        )
        observation.parent.mkdir(parents=True)
        hypothesis.parent.mkdir(parents=True)
        (root / "02_analysis/patterns").mkdir(parents=True)
        (root / "01_working/raw-notes").mkdir(parents=True)
        (root / "04_decisions/risk-decisions").mkdir(parents=True)
        (root / "10_external-inputs").mkdir(parents=True)
        (root / "03_artifacts").mkdir(parents=True)
        observation.write_text(
            f"""---
id: {observation_id}
type: observation
title: "確認した観察"
content_language: ja
created_at: 2026-08-09T12:00:00+09:00
created_by: agent:codex
status: proposed
confidence: low
knowledge_basis:
  - recorded_statement
relations:
  - type: derived_from
    target: RN-20260809-115959-source
---

# 観察
""",
            encoding="utf-8",
        )
        hypothesis.write_text(
            f"""---
id: {hypothesis_id}
type: hypothesis_episode
title: "投影を確認する仮説"
content_language: ja
created_at: 2026-08-09T12:00:01+09:00
created_by: agent:codex
hypothesis_scope: session
hypothesis_level: value
status: proposed
confidence: low
knowledge_basis:
  - reasoned_synthesis
relations:
  - type: derived_from
    target: {observation_id}
---

# 仮説

## 検証対象の分解

| ID | Uncertainty | Decision importance | Evidence refs | Coverage state | Finding | Applicability | Residual uncertainty |
| --- | --- | --- | --- | --- | --- | --- | --- |
| U1 | 対象条件で成立するか | high | none | not_checked | unknown | unknown | 対象条件では未確認 |

## 結果

`not_tested`
""",
            encoding="utf-8",
        )

    def test_graph_projects_direct_relations_and_components(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_fixture(root)
            graph = GENERATOR.build_graph(root)
            hypothesis = next(
                node
                for node in graph["nodes"]
                if node["type"] == "hypothesis_episode"
            )
            self.assertEqual("not_tested", hypothesis["result"])
            self.assertEqual("U1", hypothesis["validation_components"][0]["id"])
            self.assertIn(
                {
                    "source": hypothesis["id"],
                    "type": "derived_from",
                    "target": "OBS-20260809-120000-source",
                },
                graph["edges"],
            )

    def test_written_outputs_are_deterministic_and_staleness_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_fixture(root)
            first = GENERATOR.render_outputs(root)
            second = GENERATOR.render_outputs(root)
            self.assertEqual(first, second)
            GENERATOR.write_outputs(root)
            self.assertEqual([], GENERATOR.stale_outputs(root))
            index = root / "02_analysis/README.md"
            index.write_text("stale\n", encoding="utf-8")
            self.assertIn("02_analysis/README.md", GENERATOR.stale_outputs(root))

    def test_flat_list_parser_accepts_inline_and_block_yaml(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            inline = root / "inline.md"
            block = root / "block.md"
            inline.write_text(
                "---\ntags: [ai-slop, value-stream, 'session-design']\n---\n",
                encoding="utf-8",
            )
            block.write_text(
                "---\ntags:\n  - ai-slop\n  - value-stream\n---\n",
                encoding="utf-8",
            )
            self.assertEqual(
                ["ai-slop", "value-stream", "session-design"],
                GENERATOR.parse_list(inline, "tags"),
            )
            self.assertEqual(
                ["ai-slop", "value-stream"],
                GENERATOR.parse_list(block, "tags"),
            )

    def test_unsanitized_raw_note_is_excluded_without_exposing_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_fixture(root)
            raw_id = "RN-20260809-115959-source"
            raw = root / "01_working/raw-notes" / f"{raw_id}.md"
            raw.write_text(
                f"""---
id: {raw_id}
type: raw_note
title: "公開確認前のタイトル"
content_language: ja
created_at: 2026-08-09T11:59:59+09:00
content_origin: human_direct
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: unreviewed
sanitization_status: not_reviewed
sanitization_checked_at: none
sanitization_checked_by: none
tags: [private-candidate]
---

# メモ
""",
                encoding="utf-8",
            )
            graph = GENERATOR.build_graph(root)
            serialized = str(graph)
            self.assertNotIn(raw_id, serialized)
            self.assertNotIn("公開確認前のタイトル", serialized)
            self.assertNotIn("private-candidate", serialized)
            self.assertFalse(
                any(edge["target"] == raw_id for edge in graph["edges"])
            )
            self.assertEqual(
                {"raw_note_sanitization_not_reviewed": 1},
                graph["projection"]["excluded_sources"],
            )
            self.assertEqual(
                {"target_not_projected": 1},
                graph["projection"]["excluded_edges"],
            )

    def test_raw_note_path_excludes_missing_or_invalid_type(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_fixture(root)
            raw_directory = root / "01_working/raw-notes"
            invalid_documents = {
                "RN-20260809-115957-missing-type.md": """---
id: RN-20260809-115957-missing-type
title: "Type欠落"
sanitization_status: not_needed
---

# メモ
""",
                "RN-20260809-115958-invalid-type.md": """---
id: RN-20260809-115958-invalid-type
type: observation
title: "Type不正"
sanitization_status: not_needed
---

# メモ
""",
            }
            for filename, document in invalid_documents.items():
                (raw_directory / filename).write_text(document, encoding="utf-8")
            graph = GENERATOR.build_graph(root)
            serialized = str(graph)
            self.assertNotIn("RN-20260809-115957-missing-type", serialized)
            self.assertNotIn("RN-20260809-115958-invalid-type", serialized)
            self.assertNotIn("Type欠落", serialized)
            self.assertNotIn("Type不正", serialized)
            self.assertEqual(
                {"raw_note_invalid_metadata": 2},
                graph["projection"]["excluded_sources"],
            )

    def test_completed_sanitization_requires_valid_checker_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_fixture(root)
            raw_id = "RN-20260809-115956-invalid-sanitization-check"
            raw = root / "01_working/raw-notes" / f"{raw_id}.md"
            raw.write_text(
                f"""---
id: {raw_id}
type: raw_note
title: "不正な公開安全性Metadata"
content_language: ja
created_at: 2026-08-09T11:59:56+09:00
content_origin: human_direct
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: reviewed
sanitization_status: sanitized
sanitization_checked_at: none
sanitization_checked_by: none
tags: [private-candidate]
---

# メモ
""",
                encoding="utf-8",
            )
            graph = GENERATOR.build_graph(root)
            serialized = str(graph)
            self.assertNotIn(raw_id, serialized)
            self.assertNotIn("不正な公開安全性Metadata", serialized)
            self.assertNotIn("private-candidate", serialized)
            self.assertEqual(
                {"raw_note_invalid_metadata": 1},
                graph["projection"]["excluded_sources"],
            )

    def test_raw_note_with_required_metadata_missing_is_excluded(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_fixture(root)
            raw_id = "RN-20260809-115955-required-fields-missing"
            raw = root / "01_working/raw-notes" / f"{raw_id}.md"
            raw.write_text(
                f"""---
id: {raw_id}
type: raw_note
title: "必須Metadata欠落"
content_language: ja
created_at: 2026-08-09T11:59:55+09:00
sanitization_status: not_needed
sanitization_checked_at: 2026-08-09T12:00:00+09:00
sanitization_checked_by: agent:codex
tags: [private-candidate]
---

# メモ
""",
                encoding="utf-8",
            )
            graph = GENERATOR.build_graph(root)
            serialized = str(graph)
            self.assertNotIn(raw_id, serialized)
            self.assertNotIn("必須Metadata欠落", serialized)
            self.assertNotIn("private-candidate", serialized)
            self.assertEqual(
                {"raw_note_invalid_metadata": 1},
                graph["projection"]["excluded_sources"],
            )

    def test_sanitized_raw_note_projects_inline_tags(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self.write_fixture(root)
            raw_id = "RN-20260809-115959-safe-note"
            raw = root / "01_working/raw-notes" / f"{raw_id}.md"
            raw.write_text(
                f"""---
id: {raw_id}
type: raw_note
title: "公開確認済みのメモ"
content_language: ja
created_at: 2026-08-09T11:59:59+09:00
content_origin: human_direct
created_by: human:kijima
source_platform: codex
capture_mode: assisted
imported_by: none
review_status: reviewed
sanitization_status: not_needed
sanitization_checked_at: 2026-08-09T12:00:00+09:00
sanitization_checked_by: agent:codex
tags: [ai-slop, value-stream]
---

# メモ
""",
                encoding="utf-8",
            )
            graph = GENERATOR.build_graph(root)
            projected = next(node for node in graph["nodes"] if node["key"] == raw_id)
            self.assertEqual(["ai-slop", "value-stream"], projected["tags"])
            self.assertEqual({}, graph["projection"]["excluded_sources"])


if __name__ == "__main__":
    unittest.main()
