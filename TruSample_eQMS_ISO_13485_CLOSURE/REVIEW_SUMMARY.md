TruSample eQMS — Review Package Summary
Generated: 2026-02-11T06:40:00Z

Contents (brief descriptions)
- missing_links_report.txt
  - List of Reference_Map entries where Link is empty; items to populate with Google Drive URLs.

- SOP_and_FRM_drafts.md
  - Consolidated SOP and form drafts covering Document Control, Change Control, CAPA, Training, COA, Batch Close processes and FRM field suggestions.

- validation_test_cases.md
  - Validation test-plan templates and test cases for COA generator, Batch Close generator, and Management Action Reminder system; includes acceptance criteria and evidence list.

- internal_audit_checklist_and_auditpack_skeleton.md
  - Internal audit checklist focused on ISO 13485 essentials and a skeleton for Audit Pack (what to collect).

- Audit_Pack_SKELETON/ (folder)
  - MANIFEST.txt — audit pack manifest template
  - audit_report.md — internal audit report skeleton
  - evidence/.placeholder — place to add exported evidence files
  - signoffs.md — signoff template
  - internal_audit_checklist_filled.md — placeholder to paste completed checklist
  - state_pack.json and STATE_PACK_REL-20251231-0146.json — actual state pack copied from mounted eQMS (snapshot of Master Implementation Tracker)

- SOP_Google_Docs_Ready/ (folder with one .md file per SOP)
  - SOP-TS-010_Document_Control.md
  - SOP-TS-020_Change_Control.md
  - SOP-TS-021_Management_Review.md
  - SOP-TS-030_CAPA_NCR.md
  - SOP-TS-040_Training.md
  - SOP-TS-050_Records_Retention.md
  - SOP-TS-060_Lot_Release_COA.md
  - SOP-TS-080_Design_Control_RUO.md
  - Each file is formatted for direct copy/paste into a Google Doc (includes Purpose, Scope, Procedure, Records, Approval block).

- DEPLOYMENT_CHECKLIST.md
  - Exact copy/paste steps to move files from workspace to Google Drive, priority order for SOP creation, and quick mapping of files to eQMS folders.

Package location
- /home/mhernandez/clawd/TruSample_eQMS_ISO_13485_CLOSURE/review_package.zip (contains all files and folders listed above)

Priority order for deployment
1. SOP-TS-010 Document Control
2. SOP-TS-020 Change Control
3. SOP-TS-060 Lot Release & COA
4. SOP-TS-030 CAPA & NCR
5. SOP-TS-021 Management Actions & Review
6. SOP-TS-040 Training & Competency
7. SOP-TS-050 Records Retention & Access Control
8. SOP-TS-080 Design Control & RUO

Next immediate steps for ISO 13485 closure
1. Review and approve SOP-TS-010 (Document Control) — this enables controlled publication of all other SOPs.
2. Populate Reference_Map Link fields for existing controlled documents (use missing_links_report as guide).
3. Create Google Docs for the Level 1 SOPs (follow DEPLOYMENT_CHECKLIST copy/paste steps) and update Reference_Map.
4. Execute validation test cases for COA, Batch Close, and Reminders; save evidence into Audit_Pack_SKELETON/evidence/.
5. Complete Training Matrix and link sample training records.
6. Run internal mock audit using internal_audit_checklist_and_auditpack_skeleton.md; record findings and CAPAs.
7. Assemble final Audit Pack with evidence and manifest; perform final management review and signoffs.

How to review
- Unzip the review_package.zip locally and open the SOP markdown files for content review.
- When ready, tell me which SOPs to publish first; I can either (A) create Google Docs automatically (needs Google creds) or (B) generate copy-ready exports for manual paste.

Contact
- If you want changes to any SOP text, tell me the SOP ID and the edits and I'll update the markdown files here.
