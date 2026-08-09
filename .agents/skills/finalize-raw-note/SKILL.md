---
name: finalize-raw-note
description: Finalize a Raw Note by sanitizing publication-sensitive information, updating provenance and tags, and safely renaming an unreferenced draft. Use for Raw Note cleanup, sanitization, rename, or review. Record review automatically only for unchanged direct human-authored persisted wording, or after a later human message explicitly confirms the saved content of an exact Raw Note ID or link. Do not treat permission to create, update, finish, sanitize, or proceed, pre-persistence approval, or the same assistant turn that changed wording as review.
---

# Finalize a Raw Note

Read the required `00_meta/` contracts before editing.

## Review chronology

- Authorization to create, update, finish, sanitize, rename, or proceed is not
  review of persisted content.
- Agent-produced, imported, copied, transcribed, mixed, meaning-changed, or
  sanitized wording must remain `unreviewed` when first persisted. Hand off its
  exact resulting node ID or link and stop.
- Set such a note to `reviewed` only after a later human message explicitly
  confirms that persisted content and the node has not meaningfully changed
  since the handoff. Never change wording and record that review in one assistant
  turn.
- Preserve the schema's narrow direct-human-author exception when finalization
  does not alter the human author's saved meaning.

## Workflow

1. Identify exactly one Raw Note. Ask only if the target is ambiguous.
2. Inspect Git status and history without printing sensitive text.
3. Check whether any suspected sensitive value exists in a committed revision.
   If it does, stop and report that Git history remediation is required. Do not
   repeat the value.
4. Sanitize the working copy using the rules below.
5. Infer a concise Japanese title, safe lowercase ASCII kebab-case slug, and
   stable tags from the sanitized content.
6. Check that no repository file references the current node ID. If referenced,
   keep the ID and filename unchanged.
7. Run:

   ```bash
   python3 .agents/skills/finalize-raw-note/scripts/finalize_raw_note.py \
     <path> --title '<Japanese title>' --slug <safe-slug> \
     --sanitization-status <not_needed|sanitized> \
     --tag <tag>
   ```

   The script uses `--review-status auto` by default. It sets `reviewed` only
   for completed notes directly authored by their human author
   (`human_direct`, `direct` or `assisted`, and `imported_by: none`). It
   preserves `corrected`, and it does not automatically review imported,
   copied, transcribed, mixed, or GenAI-authored wording. Newly sanitized
   wording returns to `unreviewed` until a human confirms it.

   For agent-produced, imported, copied, transcribed, mixed, meaning-changed, or
   sanitized wording in the current turn, pass `--review-status unreviewed`
   explicitly. Return the resulting exact ID or link and stop. Do not reuse the
   request that authorized this workflow as review.

   After a later human message explicitly confirms that unchanged persisted
   content, a review-only invocation may use:

   ```bash
   python3 .agents/skills/finalize-raw-note/scripts/finalize_raw_note.py \
     <path> --title '<existing-title>' --slug <existing-slug> \
     --sanitization-status <existing-not_needed|sanitized> \
     --review-status reviewed --confirmed-persisted-id <RN-ID> \
     --tag <existing-tag>
   ```

   Explicit review mode refuses a rename or sanitization-status change so the
   confirmation remains bound to the previously handed-off node.

8. Run `python3 scripts/generate_analysis_views.py`. A Raw Note enters the
   projection only after its `sanitization_status` is `not_needed` or `sanitized`.
9. Run `python3 scripts/validate_repository.py` and `git diff --check`.
10. Summarize changed metadata and removed information by category only. Return
   a clickable absolute file link. Never quote removed values.

## Sanitization rules

Remove or safely generalize:

- customer, partner, engagement, project, opportunity, case, and contract names
  or identifiers;
- non-public person names, emails, phone numbers, and identifying job details;
- internal URLs, repositories, documents, systems, hostnames, IP addresses,
  account or subscription IDs, cluster names, and environment identifiers;
- commercial terms, staffing details, schedules, and exact quantities that
  could identify an engagement;
- credentials, tokens, secrets, or authentication material;
- combinations of otherwise ordinary details that can re-identify a customer
  or engagement.

Preserve only the analytical meaning needed for the session. General wording
such as `Red Hat ConsultingのPlatform Engineering案件` is allowed when it
cannot identify a customer or specific engagement.

Use Japanese category placeholders such as `[顧客情報を削除]`,
`[案件識別情報を削除]`, `[個人情報を削除]`, or `[内部URLを削除]`. Do not use
reversible hashes or realistic pseudonyms.

Do not add removed values to correction history. When sanitization changes the
wording, use `sanitization_status: sanitized`; the script will set
`content_origin: mixed`. A publication-safety review is not a human intent
review. Do not explicitly override `review_status` to `reviewed` unless the
human confirmed that the record matches their intent.
