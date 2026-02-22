# PR Review - Legacy database migration script (by Sneha Jain)

## Reviewer: Neha Sharma
---

**Overall:** Good foundation but critical bugs need fixing before merge.

### `dataMigrator.py`

> **Bug #1:** Foreign key references use old table IDs instead of new auto-generated IDs after migration
> This is the higher priority fix. Check the logic carefully and compare against the design doc.

### `schemaMapper.py`

> **Bug #2:** Date format conversion assumes MM/DD/YYYY but legacy system uses DD/MM/YYYY so months and days are swapped
> This is more subtle but will cause issues in production. Make sure to add a test case for this.

---

**Sneha Jain**
> Acknowledged. I have documented the issues for whoever picks this up.
