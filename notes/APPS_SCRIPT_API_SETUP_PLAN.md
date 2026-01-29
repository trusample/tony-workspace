# Apps Script API connector — plan (for morning)

Goal: prove EQMS automation exists (Mgmt Action reminders, BatchClose reports, COA generator) by inspecting **Apps Script project source** + deployments.

## What we already confirmed
- The real eQMS artifacts live in **Shared Drives** (synced to `drive_shared/eqms_crm/` etc.)
- The Claude handoff claims reference Apps Script automations + specific sheet IDs/variables.

## Requirements (Google side)
### 1) Enable APIs in the correct Google Cloud Project
In Google Cloud Console for the project that owns the OAuth client:
- Enable **Google Apps Script API**
- Enable **Google Drive API**
- (Optional, later) **Google Sheets API**

Reference: https://developers.google.com/apps-script/api/how-tos/enable

### 2) Allow Apps Script API access to script projects
This is a separate global toggle per account:
- Apps Script dashboard → **Settings** → enable “Google Apps Script API” access.

(Otherwise you can get errors even after OAuth.)

## Credentials: what we need from Maykel
A single JSON file, ideally **OAuth Desktop (installed)**:
- Looks like `{ "installed": { ... } }`

If it’s `web` that’s workable but a bit more annoying.
Service account only works if the Shared Drives + scripts are explicitly shared/permissioned.

We will store it on server at:
- `/home/mhernandez/clawd/secrets/google/credentials.json`

## Server-side setup plan
### A) Install Python Google API client libs
On server:
```bash
python3 -m pip install --user \
  google-api-python-client \
  google-auth \
  google-auth-oauthlib \
  google-auth-httplib2
```

### B) Create token (interactive once)
We’ll run a script that opens device auth or prints a URL to authorize.
Token cached at:
- `/home/mhernandez/clawd/secrets/google/token.json`

### C) Discover relevant script projects
Two ways:
1) Drive API: list files with mimeType `application/vnd.google-apps.script` across shared drives (corpora=drive, driveId=<id>, includeItemsFromAllDrives/supportsAllDrives)
2) If we already know project IDs from the handoff `GET IDs SHEET`, use those.

### D) Inspect code / prove features
For each candidate project ID:
- `script.projects.getContent(projectId)`
- Search source for keywords:
  - mgmt review / reminders / triggers
  - batch close / BatchClose / close report
  - COA / certificate
  - config keys: `QMS_MASTER_SHEET_ID`, etc.
- List deployments: `script.projects.deployments.list(projectId)`

Output report:
- `notes/EQMS_APPS_SCRIPT_EVIDENCE.md`

## Notes
- Our current rclone sync exports Google-native files to xlsx/docx/pdf; it cannot reliably export Apps Script project source.
- Apps Script API is the authoritative method to confirm automation.
