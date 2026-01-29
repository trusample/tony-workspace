# Google APIs setup (TruSample Ops)

## What you need
- OAuth credentials JSON (preferred: **Desktop/installed**)
  - store at: `/home/mhernandez/clawd/secrets/google/credentials.json`
- Token cache (created by auth flow)
  - `/home/mhernandez/clawd/secrets/google/token.json`

## Enable APIs in Google Cloud
Enable in the *same* project as the OAuth client:
- Google Drive API
- Google Sheets API
- Google Apps Script API

Apps Script enablement doc:
- https://developers.google.com/apps-script/api/how-tos/enable

## Apps Script dashboard toggle (account-level)
Apps Script UI → Settings → enable Apps Script API access.

## Recommended read-only scopes (audit mode)
- Drive: `https://www.googleapis.com/auth/drive.readonly`
- Sheets: `https://www.googleapis.com/auth/spreadsheets.readonly`
- Script (read): `https://www.googleapis.com/auth/script.projects.readonly`

If you need deployments list/read:
- often covered by `script.projects.readonly`; if not, add minimal extra scopes.

## Shared Drives listing/search notes
When searching via Drive API, use:
- `supportsAllDrives=true`
- `includeItemsFromAllDrives=true`
- `corpora=drive` + `driveId=<sharedDriveId>` when enumerating per drive

## Common failure modes
- 403/permission: API not enabled in GCP project, or Apps Script API access not granted in dashboard.
- Service account: works only if the Shared Drive and scripts are explicitly shared with the service account.
