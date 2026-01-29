# COA generation findings (as of 2026-01-29)

## What exists
- COA template doc exists:
  - `TMP-030-D – Certificate of Analysis (COA) Template`
  - fileId: `1DW5qGNMLefm8c_3ZqoHkRKyoSiZvdkfReOrJTjAH3iE`
  - lastModifyingUser: `m.hernandez@trusample.bio`
  - owner: `mhernandez@cellabios.com`
  - parent folder: `03 Templates` (folderId: `1YjC1KSb79MpQE61nAhpu7cx7FBx9PdoY`)

- COA output folder exists in Shared Drive `0AMooSbVaWDeSUk9PVA`:
  - folder name: `COAs`
  - folderId: `1ohC3j_m0r42VgRRclgdjJKeq2L4akthT`

- COA outputs exist (doc + pdf):
  - `COA – HbA1c Controls – Lot TS-HbA1c-001` (Google Doc)
  - `COA – HbA1c Controls – Lot TS-HbA1c-001.pdf`
  - In the `COAs` folder
  - lastModifyingUser shown by Drive API: `team_iso`

## What we can and cannot prove right now
- We can prove **the artifacts exist** (template, folder, outputs) and who last modified them.
- We **cannot yet prove** which Apps Script project generates COAs because:
  - none of the currently visible Apps Script project sources contains the COA folderId or templateId
  - and none contain obvious COA keyword/code paths.

## Most likely explanations
1) COA generation is currently **manual or semi-manual** (copy template → edit → export to PDF → save in COAs folder), performed under `team_iso`.
2) COA generation is automated, but the script is in a **different Apps Script project** not visible to the current token (different owner, different Shared Drive, or not indexed by our current Drive search constraints).

## Next steps to prove automation
1) Expand script discovery beyond “files with mimeType apps-script we can list” by enumerating:
   - script projects that are **container-bound** to Sheets/Docs (bound scripts)
   - scripts located in other Shared Drives / folders (driveId-focused enumeration)
2) Search for `team_iso` authored scripts and/or deployments.
3) Check `TruSample eQMS MASTER` → Extensions → Apps Script (bound project) and audit its source directly.
