---
name: finalize-raw-note
description: Finalize a human-authored Raw Note in this repository by sanitizing publication-sensitive customer or project information, updating provenance and tags, and renaming an unreferenced draft to a safe content-based filename. Use when the user says a Raw Note has been filled in, asks to finish, clean, sanitize, review, or rename a Raw Note, or requests checks for Red Hat Consulting client or Platform Engineering engagement information before publication.
---

# Finalize a Raw Note

Read the required `00_meta/` contracts before editing.

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

8. Run `python3 scripts/validate_repository.py`.
9. Summarize changed metadata and removed information by category only. Return
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
`content_origin: mixed`. A publication-safety review is not a human factual
review, so do not set `review_status: reviewed`.
