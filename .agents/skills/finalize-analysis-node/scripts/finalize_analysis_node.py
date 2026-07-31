#!/usr/bin/env python3
"""Finalize a human-reviewed analysis node without changing epistemic results."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ANALYSIS_DIRS = {
    "observations": "observation",
    "hypothesis-episodes": "hypothesis_episode",
    "patterns": "pattern",
}
HUMAN_ID = re.compile(r"^human:[a-z0-9]+(?:[-_][a-z0-9]+)*$")


def find_repository_root(path: Path) -> Path:
    for candidate in path.resolve().parents:
        if (candidate / "00_meta/repository-contract.md").is_file() and (
            candidate / "02_analysis"
        ).is_dir():
            return candidate
    raise RuntimeError("repository root was not found")


def split_document(document: str) -> tuple[list[str], str]:
    lines = document.splitlines()
    if not lines or lines[0] != "---":
        raise RuntimeError("analysis node has no opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise RuntimeError("analysis node has no closing frontmatter delimiter") from error
    body = "\n".join(lines[end + 1 :])
    return lines[1:end], body + ("\n" if body else "")


def read_field(lines: list[str], key: str) -> str:
    prefix = f"{key}:"
    values = [line[len(prefix) :].strip() for line in lines if line.startswith(prefix)]
    if len(values) != 1:
        raise RuntimeError(f"required frontmatter field is missing or duplicated: {key}")
    return values[0].strip("\"'")


def upsert_field(lines: list[str], key: str, value: str, after: str) -> list[str]:
    prefix = f"{key}:"
    indexes = [index for index, line in enumerate(lines) if line.startswith(prefix)]
    if len(indexes) > 1:
        raise RuntimeError(f"frontmatter field is duplicated: {key}")
    if indexes:
        lines[indexes[0]] = f"{key}: {value}"
        return lines
    anchor = next(
        (index for index, line in enumerate(lines) if line.startswith(f"{after}:")),
        None,
    )
    if anchor is None:
        raise RuntimeError(f"frontmatter insertion anchor is missing: {after}")
    return lines[: anchor + 1] + [f"{key}: {value}"] + lines[anchor + 1 :]


def safety_section(timestamp: str, checker: str, result: str) -> str:
    if result == "not_needed":
        finding = (
            "  顧客、案件、非公開の個人、商用条件、内部System、認証情報、再識別に\n"
            "  つながる組み合わせは確認されず、本文の変更や削除は行っていない"
        )
    else:
        finding = (
            "  公開対象に不要な識別情報をCategory単位で削除または一般化し、削除値は\n"
            "  Repository、訂正履歴、Filename、Logへ保存していない"
        )
    return (
        "## 公開安全性確認\n\n"
        f"- checked_at: {timestamp}\n"
        f"- checked_by: {checker}\n"
        f"- result: `{result}`\n"
        "- scope:\n"
        "  この分析ノードの本文、frontmatter、relationの組み合わせを、\n"
        "  人間の意図Reviewを確定する時点で再確認した\n"
        "- finding:\n"
        f"{finding}\n"
        "- limitation:\n"
        "  公開安全性の確認は、内容の正しさ、検証完了、採用を意味しない\n"
    )


def replace_safety_section(body: str, section: str) -> str:
    marker = "## 公開安全性確認"
    if marker not in body:
        return body.rstrip() + "\n\n" + section
    start = body.index(marker)
    next_heading = body.find("\n## ", start + len(marker))
    end = len(body) if next_heading == -1 else next_heading + 1
    return body[:start].rstrip() + "\n\n" + section + body[end:]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--reviewed-by", required=True)
    parser.add_argument("--checked-by", default="agent:codex")
    parser.add_argument(
        "--sanitization-result",
        required=True,
        choices=("not_needed", "sanitized"),
    )
    parser.add_argument(
        "--human-confirmed-after-sanitization",
        action="store_true",
        help="required when sanitization changed the node wording",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not HUMAN_ID.fullmatch(args.reviewed_by):
        parser.error("--reviewed-by must be a stable human:* identifier")
    if (
        args.sanitization_result == "sanitized"
        and not args.human_confirmed_after_sanitization
    ):
        parser.error(
            "sanitized wording requires --human-confirmed-after-sanitization"
        )
    return args


def main() -> int:
    args = parse_args()
    path = args.path.resolve()
    if not path.is_file():
        raise RuntimeError(f"analysis node does not exist: {path}")
    root = find_repository_root(path)
    analysis_root = (root / "02_analysis").resolve()
    try:
        relative = path.relative_to(analysis_root)
    except ValueError as error:
        raise RuntimeError("target must be inside 02_analysis") from error
    if len(relative.parts) != 2 or relative.parent.name not in ANALYSIS_DIRS:
        raise RuntimeError("target must be directly inside a governed analysis directory")
    if path.name == "README.md":
        raise RuntimeError("analysis README files cannot be finalized")

    frontmatter, body = split_document(path.read_text(encoding="utf-8"))
    expected_type = ANALYSIS_DIRS[relative.parent.name]
    if read_field(frontmatter, "type") != expected_type:
        raise RuntimeError(f"type must be {expected_type}")
    if read_field(frontmatter, "id") != path.stem:
        raise RuntimeError("id must match the filename stem")
    current_status = read_field(frontmatter, "status")
    if current_status in {"rejected", "superseded"}:
        raise RuntimeError(f"cannot finalize a {current_status} analysis node")
    if current_status not in {"proposed", "reviewed"}:
        raise RuntimeError(f"unsupported analysis status: {current_status}")

    complete_review = all(
        any(line.startswith(f"{key}:") for line in frontmatter)
        for key in ("reviewed_at", "reviewed_by", "review_scope")
    )
    complete_safety = "## 公開安全性確認" in body and (
        f"- result: `{args.sanitization_result}`" in body
    )
    if current_status == "reviewed" and complete_review and complete_safety:
        print(f"unchanged: {path}")
        return 0

    timestamp = datetime.now(ZoneInfo("Asia/Tokyo")).isoformat(timespec="seconds")
    preserve_existing_review = (
        current_status == "reviewed"
        and complete_review
        and args.sanitization_result == "not_needed"
    )
    reviewed_at = (
        read_field(frontmatter, "reviewed_at")
        if preserve_existing_review
        else timestamp
    )
    reviewed_by = (
        read_field(frontmatter, "reviewed_by")
        if preserve_existing_review
        else args.reviewed_by
    )
    frontmatter = upsert_field(frontmatter, "status", "reviewed", "created_by")
    frontmatter = upsert_field(frontmatter, "reviewed_at", reviewed_at, "status")
    frontmatter = upsert_field(
        frontmatter, "reviewed_by", reviewed_by, "reviewed_at"
    )
    frontmatter = upsert_field(
        frontmatter, "review_scope", "intent_alignment", "reviewed_by"
    )
    body = replace_safety_section(
        body,
        safety_section(timestamp, args.checked_by, args.sanitization_result),
    )
    document = "---\n" + "\n".join(frontmatter) + "\n---\n" + body

    if args.dry_run:
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
