---
name: new-raw-note
description: Create a blank, timestamped Raw Note with valid provenance in this repository. Use when the user asks for a blank Raw Note, says phrases such as "ファイルくださいな", "Raw Noteをください", or "メモ用ファイルを作って", or wants to start capturing a note without manually writing frontmatter.
---

# Create a Raw Note

1. Run `python3 .agents/skills/new-raw-note/scripts/new_raw_note.py`.
2. Do not add interpretations, hypotheses, or inferred content to the new file.
3. Return a clickable absolute link to the created file.
4. Run `python3 scripts/validate_repository.py`.

The default provenance means that a human will author the content while Codex
assisted with capture:

- `content_origin: human_direct`
- `created_by: human:kijima`
- `source_platform: codex`
- `capture_mode: assisted`
- `imported_by: none`

When the user provides a title or slug, pass `--title` or `--slug`. Use only
lowercase ASCII kebab-case for a slug. Override provenance flags only when the
user's actual capture context differs from the defaults.

Never overwrite an existing file. Never fill a blank note with guessed content.
