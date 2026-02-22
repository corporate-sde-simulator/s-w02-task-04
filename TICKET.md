# FINSERV-4113: Refactor legacy database migration scripts

**Status:** In Progress · **Priority:** Medium
**Sprint:** Sprint 24 · **Story Points:** 5
**Reporter:** Kavitha Rao (Data Team Lead) · **Assignee:** You (Intern)
**Due:** End of sprint (Friday)
**Labels:** `backend`, `python`, `database`, `refactor`
**Task Type:** Code Maintenance

---

## Description

The database migration script **works correctly** — it migrates records from the legacy Oracle schema to the new PostgreSQL format. The code has quality issues: no batch processing (one record at a time), no progress tracking, and schema mapping is embedded in the migration logic.

## What Needs Improvement

- `# TODO (code review):` comments mark issues
- No batch processing (inserts one record at a time — very slow for 100k+ rows)
- Schema mapping mixed into migration logic (should be separate)
- No progress reporting or resumability after failure
- Connection strings hardcoded

## Acceptance Criteria

- [ ] All `# TODO (code review):` items addressed
- [ ] Batch processing added (configurable batch size)
- [ ] Schema mapping extracted to separate function/config
- [ ] Progress reporting added
- [ ] All existing tests still pass
