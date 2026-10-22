# naming-conventions.md — the filing system (this replaces a database)

One job carries one slug across every file it touches. Names tell you the state — no database needed.

## Slugs
- Lowercase, hyphenated, short: `terrific-loads-ads`, `birthday-site-build`, `sermon-framework-db`.
- The same slug is reused for the brief, the draft, and the output.

## Briefs
- `projects\active\YYYY-MM-DD_<slug>_brief.md`
- Example: `projects\active\2026-06-05_terrific-loads-ads_brief.md`

## Working drafts and finals
- Draft: `projects\active\<slug>_draft.md` (or `_v2`, `_v3`)
- Final: `projects\outputs\<slug>_final.md`

## When a job is done
- Move the final to `projects\outputs\`. Leave the brief in `active\` only while it's live; archive
  with the output once shipped.

## Dates
- Always ISO: `YYYY-MM-DD`. Convert any relative date ("Friday", "next week") to the real date.
