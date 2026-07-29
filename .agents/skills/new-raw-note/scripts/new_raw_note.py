#!/usr/bin/env python3
"""Create a blank Raw Note from the repository's canonical template."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ORIGINS = ("human_direct", "assist_a_generated", "mixed")
PLATFORMS = ("local", "chatgpt", "codex", "other")
CAPTURE_MODES = ("direct", "copy_paste", "transcript", "import", "assisted")


def find_repository_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / "templates/raw-note.md").is_file() and (
            candidate / "01_working/raw-notes"
        ).is_dir():
            return candidate
    raise RuntimeError("repository root with the Raw Note template was not found")


def replace_field(document: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^{re.escape(key)}:.*$", re.MULTILINE)
    updated, count = pattern.subn(f"{key}: {value}", document, count=1)
    if count != 1:
        raise RuntimeError(f"template field is missing or duplicated: {key}")
    return updated


def build_document(template: str, args: argparse.Namespace, node_id: str) -> str:
    values = {
        "id": node_id,
        "title": json.dumps(args.title, ensure_ascii=False),
        "created_at": args.created_at.isoformat(timespec="seconds"),
        "content_origin": args.content_origin,
        "created_by": args.created_by,
        "source_platform": args.source_platform,
        "capture_mode": args.capture_mode,
        "imported_by": args.imported_by,
    }
    document = template
    for key, value in values.items():
        document = replace_field(document, key, value)
    return document


def available_path(directory: Path, timestamp: str, slug: str) -> tuple[Path, str]:
    candidate_slug = slug
    sequence = 1
    while True:
        node_id = f"RN-{timestamp}-{candidate_slug}"
        path = directory / f"{node_id}.md"
        if not path.exists():
            return path, node_id
        sequence += 1
        candidate_slug = f"{slug}-{sequence}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", default="未設定")
    parser.add_argument("--slug", default="untitled")
    parser.add_argument("--content-origin", choices=ORIGINS, default="human_direct")
    parser.add_argument("--created-by", default="human:kijima")
    parser.add_argument("--source-platform", choices=PLATFORMS, default="codex")
    parser.add_argument("--capture-mode", choices=CAPTURE_MODES, default="assisted")
    parser.add_argument("--imported-by", default="none")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the target path and document without writing a file",
    )
    args = parser.parse_args()
    if not SLUG.fullmatch(args.slug):
        parser.error("--slug must use lowercase ASCII kebab-case")
    args.created_at = datetime.now(ZoneInfo("Asia/Tokyo"))
    return args


def main() -> int:
    args = parse_args()
    root = find_repository_root()
    directory = root / "01_working/raw-notes"
    timestamp = args.created_at.strftime("%Y%m%d-%H%M%S")
    path, node_id = available_path(directory, timestamp, args.slug)
    template = (root / "templates/raw-note.md").read_text(encoding="utf-8")
    document = build_document(template, args, node_id)

    if args.dry_run:
        print(path)
        print(document)
        return 0

    path.write_text(document, encoding="utf-8")
    print(path)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
