#!/usr/bin/env python3
"""Finalize frontmatter and safely rename an unreferenced Raw Note draft."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


RAW_NOTE_ID = re.compile(
    r"^(RN-(?P<timestamp>\d{8}-\d{6})-)(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)$"
)
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TAG = SLUG


def find_repository_root(path: Path) -> Path:
    for candidate in path.resolve().parents:
        if (candidate / "00_meta/repository-contract.md").is_file() and (
            candidate / "01_working/raw-notes"
        ).is_dir():
            return candidate
    raise RuntimeError("repository root was not found")


def split_document(document: str) -> tuple[list[str], str]:
    lines = document.splitlines()
    if not lines or lines[0] != "---":
        raise RuntimeError("Raw Note has no opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise RuntimeError("Raw Note has no closing frontmatter delimiter") from error
    return lines[1:end], "\n".join(lines[end + 1 :]) + "\n"


def replace_field(lines: list[str], key: str, value: str) -> list[str]:
    start = next(
        (index for index, line in enumerate(lines) if line.startswith(f"{key}:")),
        None,
    )
    if start is None:
        raise RuntimeError(f"required frontmatter field is missing: {key}")
    end = start + 1
    while end < len(lines) and lines[end].startswith((" ", "\t")):
        end += 1
    return lines[:start] + [f"{key}: {value}"] + lines[end:]


def read_field(lines: list[str], key: str) -> str:
    prefix = f"{key}:"
    matches = [line[len(prefix) :].strip() for line in lines if line.startswith(prefix)]
    if len(matches) != 1:
        raise RuntimeError(f"required frontmatter field is missing or duplicated: {key}")
    return matches[0].strip("\"'")


def resolve_review_status(
    requested: str,
    current: str,
    sanitization_status: str,
    content_origin: str,
    created_by: str,
    capture_mode: str,
    imported_by: str,
) -> str:
    if requested == "preserve":
        return current
    if requested in ("reviewed", "unreviewed"):
        return requested
    if current == "corrected":
        return "corrected"
    if sanitization_status == "sanitized":
        return "unreviewed"
    if (
        content_origin == "human_direct"
        and created_by.startswith("human:")
        and capture_mode in ("direct", "assisted")
        and imported_by == "none"
    ):
        return "reviewed"
    return current


def referenced_paths(root: Path, node_id: str, source: Path) -> list[Path]:
    needle = re.compile(rf"^\s*target:\s*{re.escape(node_id)}\s*$")
    matches: list[Path] = []
    for path in root.rglob("*.md"):
        if path.resolve() == source.resolve() or ".git" in path.parts:
            continue
        if any(needle.search(line) for line in path.read_text(encoding="utf-8").splitlines()):
            matches.append(path)
    return matches


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--title", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument(
        "--sanitization-status",
        required=True,
        choices=("not_needed", "sanitized"),
    )
    parser.add_argument("--checked-by", default="agent:codex")
    parser.add_argument(
        "--review-status",
        default="auto",
        choices=("auto", "preserve", "reviewed", "unreviewed"),
        help=(
            "auto reviews completed direct human-authored notes, preserves corrected "
            "notes, and otherwise preserves the current value"
        ),
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not SLUG.fullmatch(args.slug):
        parser.error("--slug must use lowercase ASCII kebab-case")
    invalid_tags = [tag for tag in args.tag if not TAG.fullmatch(tag)]
    if invalid_tags:
        parser.error("--tag values must use lowercase ASCII kebab-case")
    return args


def main() -> int:
    args = parse_args()
    path = args.path.resolve()
    if not path.is_file():
        raise RuntimeError(f"Raw Note does not exist: {path}")
    root = find_repository_root(path)
    raw_notes = (root / "01_working/raw-notes").resolve()
    if path.parent != raw_notes:
        raise RuntimeError("target must be directly inside 01_working/raw-notes")

    match = RAW_NOTE_ID.fullmatch(path.stem)
    if not match:
        raise RuntimeError("Raw Note filename does not match the naming convention")

    current_id = path.stem
    next_id = f"{match.group(1)}{args.slug}"
    target = path.with_name(f"{next_id}.md")
    if target != path and target.exists():
        raise RuntimeError(f"target filename already exists: {target.name}")
    references = referenced_paths(root, current_id, path)
    if target != path and references:
        relative = ", ".join(str(item.relative_to(root)) for item in references)
        raise RuntimeError(f"cannot rename a referenced Raw Note; references: {relative}")

    frontmatter, body = split_document(path.read_text(encoding="utf-8"))
    checked_at = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat(timespec="seconds")
    current_review_status = read_field(frontmatter, "review_status")
    content_origin = read_field(frontmatter, "content_origin")
    created_by = read_field(frontmatter, "created_by")
    capture_mode = read_field(frontmatter, "capture_mode")
    imported_by = read_field(frontmatter, "imported_by")
    next_review_status = resolve_review_status(
        args.review_status,
        current_review_status,
        args.sanitization_status,
        content_origin,
        created_by,
        capture_mode,
        imported_by,
    )

    updates = {
        "id": next_id,
        "title": json.dumps(args.title, ensure_ascii=False),
        "review_status": next_review_status,
        "sanitization_status": args.sanitization_status,
        "sanitization_checked_at": checked_at,
        "sanitization_checked_by": args.checked_by,
        "tags": f"[{', '.join(args.tag)}]" if args.tag else "[]",
    }
    if args.sanitization_status == "sanitized":
        updates["content_origin"] = "mixed"
    for key, value in updates.items():
        frontmatter = replace_field(frontmatter, key, value)
    document = "---\n" + "\n".join(frontmatter) + "\n---\n" + body

    if args.dry_run:
        print(target)
        print(document)
        return 0

    if target != path:
        path.rename(target)
    target.write_text(document, encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
