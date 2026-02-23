DEPLOYMENT_CHECKLIST — Move workspace files into Google Drive and SOP creation priority
Generated: 2026-02-11T06:34:00Z

1) Exact copy/paste steps to move files from workspace to Google Drive
- For each SOP in /home/mhernandez/clawd/TruSample_eQMS_ISO_13485_CLOSURE/SOP_Google_Docs_Ready/:
  a) Open Google Drive in your browser and navigate to /TruSample/eQMS/SOPs (create if missing).
  b) Create a new Google Doc and name it exactly as the Reference_ID (e.g., "SOP-TS-010 eQMS Implementation Tracker Governance").
  c) Open the corresponding .md file in a text editor, select all, copy, and paste into the Google Doc body.
  d) Update the document header metadata: Version, Effective Date, Owner.
  e) Save and set sharing permissions (view-only for general staff; edit for Owners/Tracker Admin).
  f) In Reference_Map (Master tracker) update Link with the Google Doc URL and Status=Approved or Draft.

2) Priority order for creating SOPs (ISO 13485 readiness)
- Level 1 (do these first):
  1. SOP-TS-010 Document Control (central to all other docs)
  2. SOP-TS-020 Change Control
  3. SOP-TS-060 Lot Release & COA
  4. SOP-TS-030 CAPA & NCR
- Level 2 (next):
  5. SOP-TS-021 Management Actions & Review
  6. SOP-TS-040 Training & Competency
  7. SOP-TS-050 Records Retention & Access Control
- Level 3 (as resources allow):
  8. SOP-TS-080 Design Control & RUO (detailed DHF artifacts may take time)

Rationale: Document Control and Change Control enable controlled creation and revision of all other SOPs and evidence; COA + Batch records validation are critical for product release.

3) Quick reference mapping — which files go where in eQMS structure
- /TruSample/eQMS/SOPs
  - SOP-TS-010_...  (all SOP Google Docs)
- /TruSample/eQMS/Forms
  - FRM-TS-203 (Change Log), FRM-TS-204 (Mgmt Action), FRM-TS-005 (Lot Release Log), FRM-TS-504 (Batch Close Template)
- /TruSample/eQMS/Records
  - Documents_Index exports, Completed_History exports
- /TruSample/eQMS/Batch_Records
  - BatchClose_<BatchID> sheets and generated Batch Close Reports (PDF)
- /TruSample/eQMS/COA
  - COA PDFs
- /TruSample/eQMS/Products/Synthetic_Male_AB_Serum
  - DHF artifacts, risk assessments, V&V results
- /TruSample/eQMS/Audit_Packs
  - AuditPack_<timestamp> (MANIFEST, evidence/)

Notes
- After creating Google Docs, update Reference_Map Link and set Status appropriately.
- Populate Documents_Index_Cache via pcEnsureDocumentsIndexSheet_ or manually add entries for existing artifacts.
- Keep a running MANIFEST in each Audit_Pack folder listing files + links.
