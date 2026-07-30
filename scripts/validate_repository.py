#!/usr/bin/env python3
"""Validate governed Markdown structure without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NODE_DIRS = {
    "01_working/raw-notes": ("raw_note", r"RN-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*"),
    "02_analysis/observations": (
        "observation",
        r"OBS-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
    ),
    "02_analysis/hypothesis-episodes": (
        "hypothesis_episode",
        r"HYP-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
    ),
    "02_analysis/patterns": (
        "pattern",
        r"PAT-\d{8}-\d{6}-[a-z0-9]+(?:-[a-z0-9]+)*",
    ),
}
TEMPLATE_SPECS = {
    "templates/raw-note.md": "raw_note",
    "templates/observation.md": "observation",
    "templates/hypothesis-episode.md": "hypothesis_episode",
    "templates/pattern.md": "pattern",
}
RAW_REQUIRED = {
    "id",
    "type",
    "title",
    "content_language",
    "created_at",
    "content_origin",
    "created_by",
    "source_platform",
    "capture_mode",
    "imported_by",
    "review_status",
    "sanitization_status",
    "sanitization_checked_at",
    "sanitization_checked_by",
    "tags",
}
DERIVED_REQUIRED = {
    "id",
    "type",
    "title",
    "content_language",
    "created_at",
    "created_by",
    "status",
    "confidence",
    "relations",
}
ENUMS = {
    "content_language": {"ja"},
    "content_origin": {"human_direct", "assist_a_generated", "mixed"},
    "source_platform": {"local", "chatgpt", "codex", "other"},
    "capture_mode": {"direct", "copy_paste", "transcript", "import", "assisted"},
    "review_status": {"unreviewed", "reviewed", "corrected"},
    "sanitization_status": {"not_reviewed", "not_needed", "sanitized"},
    "status": {"proposed", "reviewed", "accepted", "rejected", "superseded"},
    "confidence": {"low", "medium", "high", "not_assessed"},
    "hypothesis_level": {"value", "solution", "feature", "not_assessed"},
}
RELATION_TYPES = {
    "derived_from",
    "tests",
    "supports",
    "challenges",
    "adopted_from",
    "corrects",
    "supersedes",
    "rejected_by",
    "superseded_by",
    "references",
}
TIMESTAMP = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:Z|[+-]\d{2}:\d{2})$"
)
JAPANESE_TEXT = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    if not lines or lines[0] != "---":
        return {}, ["missing opening YAML frontmatter delimiter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, ["missing closing YAML frontmatter delimiter"]

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line.startswith((" ", "\t", "#")):
            continue
        match = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if match:
            fields[match.group(1)] = (match.group(2) or "").strip().strip("\"'")
    return fields, errors


def parse_relations(path: Path) -> list[tuple[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        end = lines.index("---", 1)
    except (ValueError, IndexError):
        return []

    relations: list[tuple[str, str]] = []
    in_relations = False
    relation_type = ""
    for line in lines[1:end]:
        if line == "relations:":
            in_relations = True
            continue
        if in_relations and line and not line.startswith((" ", "\t")):
            break
        type_match = re.match(r"^\s+- type:\s*([a-z_]+)\s*$", line)
        if in_relations and type_match:
            relation_type = type_match.group(1)
            continue
        target_match = re.match(r"^\s+target:\s*([A-Za-z0-9-]+)\s*$", line)
        if in_relations and target_match and relation_type:
            relations.append((relation_type, target_match.group(1)))
            relation_type = ""
    return relations


def contains_japanese_content(path: Path) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines and lines[0] == "---":
        try:
            lines = lines[lines.index("---", 1) + 1 :]
        except ValueError:
            return False
    return JAPANESE_TEXT.search("\n".join(lines)) is not None


def discover_node_ids() -> tuple[set[str], list[tuple[Path, str]]]:
    node_ids: set[str] = set()
    failures: list[tuple[Path, str]] = []
    search_roots = [ROOT / relative_dir for relative_dir in NODE_DIRS]
    for directory in search_roots:
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            fields, _ = parse_frontmatter(path)
            node_id = fields.get("id")
            if not node_id:
                continue
            if node_id in node_ids:
                failures.append((path, f"duplicate node id: {node_id}"))
            node_ids.add(node_id)
    external_inputs = ROOT / "10_external-inputs"
    if external_inputs.is_dir():
        for path in sorted(external_inputs.rglob("*.md")):
            if path.name == "README.md":
                continue
            fields, _ = parse_frontmatter(path)
            node_id = fields.get("id")
            if not node_id:
                continue
            if node_id in node_ids:
                failures.append((path, f"duplicate node id: {node_id}"))
            node_ids.add(node_id)
    return node_ids, failures


def validate_node(
    path: Path, expected_type: str, id_pattern: str, node_ids: set[str]
) -> list[str]:
    fields, errors = parse_frontmatter(path)
    if errors:
        return errors
    required = RAW_REQUIRED if expected_type == "raw_note" else DERIVED_REQUIRED
    missing = sorted(required - fields.keys())
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")

    node_id = fields.get("id", "")
    if node_id != path.stem:
        errors.append(f"id must match filename stem: {path.stem}")
    if node_id and not re.fullmatch(id_pattern, node_id):
        errors.append("id does not match naming convention")
    if fields.get("type") != expected_type:
        errors.append(f"type must be {expected_type}")
    if fields.get("created_at") and not TIMESTAMP.fullmatch(fields["created_at"]):
        errors.append("created_at must be ISO 8601 with timezone")
    if fields.get("content_language") == "ja" and not contains_japanese_content(path):
        errors.append("content_language is ja but body contains no Japanese text")
    for field, allowed in ENUMS.items():
        value = fields.get(field)
        if value is not None and value not in allowed:
            errors.append(f"{field} has non-canonical value: {value}")
    if expected_type == "raw_note":
        sanitization_status = fields.get("sanitization_status")
        checked_at = fields.get("sanitization_checked_at")
        checked_by = fields.get("sanitization_checked_by")
        if sanitization_status == "not_reviewed":
            if checked_at != "none" or checked_by != "none":
                errors.append(
                    "not_reviewed sanitization must have no checker or timestamp"
                )
        elif sanitization_status in {"not_needed", "sanitized"}:
            if not checked_at or not TIMESTAMP.fullmatch(checked_at):
                errors.append(
                    "completed sanitization check requires an ISO 8601 timestamp"
                )
            if not checked_by or checked_by == "none":
                errors.append("completed sanitization check requires a checker")
    if expected_type == "hypothesis_episode" and "hypothesis_level" not in fields:
        errors.append("hypothesis episode requires hypothesis_level")
    if expected_type != "raw_note":
        relations = parse_relations(path)
        if not relations:
            errors.append("derived node must contain at least one relation")
        for relation_type, target in relations:
            if relation_type not in RELATION_TYPES:
                errors.append(f"unknown relation type: {relation_type}")
            if target not in node_ids:
                errors.append(f"relation target does not exist: {target}")
    return errors


def main() -> int:
    node_ids, failures = discover_node_ids()
    checked = 0
    templates_checked = 0
    for relative_path, expected_type in TEMPLATE_SPECS.items():
        path = ROOT / relative_path
        if not path.is_file():
            failures.append((path, "required template is missing"))
            continue
        fields, errors = parse_frontmatter(path)
        for error in errors:
            failures.append((path, error))
        required = RAW_REQUIRED if expected_type == "raw_note" else DERIVED_REQUIRED
        missing = sorted(required - fields.keys())
        if missing:
            failures.append(
                (path, f"template missing required fields: {', '.join(missing)}")
            )
        if fields.get("type") != expected_type:
            failures.append((path, f"template type must be {expected_type}"))
        if (
            expected_type == "hypothesis_episode"
            and "hypothesis_level" not in fields
        ):
            failures.append((path, "hypothesis template requires hypothesis_level"))
        if not contains_japanese_content(path):
            failures.append((path, "template body must contain Japanese text"))
        templates_checked += 1

    for path in sorted((ROOT / "03_artifacts").rglob("*.md")):
        fields, errors = parse_frontmatter(path)
        for error in errors:
            failures.append((path, error))
        if fields.get("content_language") != "ja":
            failures.append((path, "artifact Markdown must declare content_language: ja"))
        if not contains_japanese_content(path):
            failures.append((path, "artifact Markdown body must contain Japanese text"))

    for relative_dir, (expected_type, id_pattern) in NODE_DIRS.items():
        directory = ROOT / relative_dir
        if not directory.is_dir():
            failures.append((directory, "required directory is missing"))
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            checked += 1
            for error in validate_node(path, expected_type, id_pattern, node_ids):
                failures.append((path, error))

    if failures:
        for path, error in failures:
            print(f"ERROR {path.relative_to(ROOT)}: {error}")
        print(
            "Validation failed: "
            f"{len(failures)} error(s), {checked} node(s), "
            f"{templates_checked} template(s) checked."
        )
        return 1
    print(
        "Validation passed: "
        f"{checked} governed node(s), {templates_checked} template(s) checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
