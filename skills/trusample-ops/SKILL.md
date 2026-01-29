---
name: trusample-ops
description: >-
  TruSample Google Workspace operations: audit and inventory eQMS/CRM assets in Google Drive (incl. Shared Drives), identify authoritative master sheets, and verify Google Apps Script automations (management action reminders, batch close reports, COA generation) via Apps Script API + Drive/Sheets APIs. Use when Maykel asks to prove what’s implemented in TruSample eQMS/CRM, to locate key sheets/folders across Shared Drives, or to set up/operate Google Workspace connectors.
---

# TruSample Ops (Google Workspace)

Use this skill to:
- **Inventory Shared Drives** and find the *authoritative* eQMS master sheet(s).
- **Prove automation exists** by pulling Apps Script project source and searching for reminders/batch close/COA logic.

## Inputs this skill expects
- Server paths:
  - Workspace: `/home/mhernandez/clawd`
  - Google creds: `/home/mhernandez/clawd/secrets/google/credentials.json`
  - OAuth token cache: `/home/mhernandez/clawd/secrets/google/token.json`
- Existing Drive sync evidence (optional, for triangulation):
  - `/home/mhernandez/clawd/drive_shared/eqms_crm` etc.

## Workflow

### 0) Quick reality check (what access we have)
1) **rclone remote exists?**
   - `rclone listremotes` should include `gdrive1:`
2) **Shared Drives list**:
   - `rclone backend drives gdrive1: --json`

If the request is “prove the Apps Script automation exists”, rclone exports are **not enough** — go to the Apps Script API workflow.

### 1) Find the authoritative eQMS master sheet(s)
Goal: locate sheets like `TruSample eQMS MASTER`, `Documents_Index`, `MGMT_REVIEW_ACTIONS`, `GET IDs SHEET`.

Steps:
1) Use Drive API (preferred) to search across Shared Drives for spreadsheets whose names match:
   - `*eQMS*MASTER*`, `Documents_Index*`, `GET IDs*`, `*Implementation_Tracker*`
2) For each candidate sheet:
   - Use Sheets API to list **tabs**
   - Extract references to folder IDs / script IDs (often stored in CONFIG tabs)
3) Output:
   - `notes/EQMS_MASTER_SHEETS_MAP.md` with: sheet name, fileId, driveId, key tabs, linked folder IDs.

Use:
- `scripts/drive_find_eqms_master_sheets.py`

### 2) Audit Apps Script projects (prove reminders + batch close + COA)
Goal: prove code exists, not just exported docs.

Steps:
1) Discover script projects (Drive API query mimeType `application/vnd.google-apps.script`) in each Shared Drive.
2) For each project:
   - `script.projects.getContent(projectId)`
   - Search for keywords:
     - reminders/triggers, time-based triggers
     - management actions
     - batch close / close report
     - COA / certificate
3) Output:
   - `notes/EQMS_APPS_SCRIPT_EVIDENCE.md` listing:
     - project name/id
     - matched keywords
     - filenames + short snippets

Use:
- `scripts/apps_script_audit.py`

## Notes / guardrails
- Default to **read-only scopes** while auditing.
- Don’t paste OAuth tokens into chat.
- If Apps Script API calls fail, check:
  - GCP project has Apps Script API enabled
  - Apps Script dashboard has API access enabled (account-level toggle)

## References
- Setup checklist: `references/google_apis_setup.md`
