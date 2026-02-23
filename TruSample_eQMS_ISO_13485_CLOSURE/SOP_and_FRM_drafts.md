SOP and FRM Drafts — TruSample eQMS (ISO 13485 closure templates)
Generated: 2026-02-11T06:30:00Z

1) SOP-TS-010: eQMS Implementation Tracker Governance
- Purpose: Define ownership, structure, versioning, and maintenance of the eQMS Master Implementation Tracker and associated tabs (Reference_Map, Automation_Index, Documents_Index_Cache, eQMS_Master_Steps).
- Scope: Applies to all personnel who create, modify, or execute actions in the Master Implementation Tracker.
- Responsibilities:
  - QMS Owner: overall governance and approvals.
  - Tracker Admin: maintain CONFIG values, ensure automation triggers are healthy.
  - Quality Reviewer: review & approve SOP/FRM links and evidence attachments.
- Procedure:
  - Creation of new reference rows: require Reference_ID, Title, Link (Doc URL), Status.
  - Versioning: update Version field in Documents_Index when a controlled doc is updated.
  - Evidence linking: all automated outputs must be recorded in Documents_Index_Cache with File URL, Generator ID, Timestamp.
- Records: Documents_Index, Completed_History, Audit packs
- Approval/Revision: signature block (Name/Role/Date/Version)

2) SOP-TS-020: Change Control Procedure
- Purpose: Manage changes to product, process, or systems impacting QMS.
- Scope: All product/process changes, software automations affecting records, and SOP revisions.
- Definitions: Change Request, Change ID, Mgmt Action
- Process Steps:
  1. Submit change in Change Log (FRM-TS-203). Assign owner, priority, due date.
  2. Triage and risk assessment (link to risk template). Determine need for validation and CAPA.
  3. Create Management Action(s) via menuCreateMgmtActionFromChange if required.
  4. Implement change; record implementation evidence (e.g., code diff, screenshots).
  5. Verification & Validation: attach FRM-TS-204 or validation artifacts.
  6. Approve and close change; update Documents_Index if new/updated controlled documents created.
- Records: FRM-TS-203, FRM-TS-204, Completed_History
- Approval block

3) SOP-TS-021: Management Actions & Reminders
- Purpose: Define lifecycle of Management Actions and how automated reminders operate.
- Procedure:
  - Creation: from Change or manual entry. Fields: Action ID, Owner, Due Date, Priority, Description.
  - Reminders: system runs Run Mgmt Action Reminders Now; identifies Due Soon (<=DUE_SOON_DAYS) and Overdue (>OVERDUE_DAYS). Sends email to Owner; CC team_iso.
  - Closure: Owner marks action Closed; automation logs into Completed_History.
- Evidence: FRM-TS-205 (Reminder Evidence / Notification Log) — store email send log, screenshots, or exported messages.
- Validation: refer to VAL-ENG-REM-001
- Approval block

4) SOP-TS-052 / SOP-TS-053: Batch Closeout Records & Batch Close Report
- Purpose: Define creation, completion, and archival of batch records and batch close reports.
- Procedure:
  - Batch creation: create BatchClose_<BatchID> via the tracker UI or script. Populate Lot metadata, materials, test results.
  - Close workflow: run Build Batch Close Report generator; generator produces Batch Close Report and writes a row to Documents_Index_Cache.
  - Archive: store final PDF/Doc in /TruSample/eQMS/Batch_Records and link to Documents_Index.
- Forms: FRM-TS-504 (Batch Close Report Template), FRM-TS-005 (Lot Release Log)
- Approval block

5) SOP-TS-060: Certificate of Analysis (COA) Generation
- Purpose: Describe COA generation, approval, and issuance for lot release.
- Procedure:
  - Trigger: menuGenerateCOAForLot prompts for Lot; generateCOAForLot_ composes COA from Lot Release Log (FRM-TS-005).
  - Review: Quality Reviewer verifies COA values and signs off (digital signature in sheet or approval row).
  - Distribution: Store COA in /TruSample/eQMS/COA and record in Documents_Index_Cache.
- Validation: VAL-ENG-COA-001
- Approval block

FRMs (short templates / fields):
- FRM-TS-203 Change Log / Change Record: Change ID, Date, Requester, Description, Risk Level, Owner, Affected Docs, Status
- FRM-TS-204 Mgmt Action Record: Action ID, Source Change ID, Owner, Due Date, Priority, Description, Status, Closure Evidence Link
- FRM-TS-205 Reminder Evidence Log: Action ID, Reminder Date, Reminder Type (DueSoon/Overdue), Recipient, Email Sent? (Y/N), Evidence Link
- FRM-TS-504 Batch Close Report Template: Batch ID, Manufacturing Steps summary, Materials lot numbers, Test results, Deviations, Release Decision, Approver, Date, Attached Evidence Links
- FRM-TS-005 Lot Release Log: Lot ID, Manufacture Date, Tests performed, Results, Acceptance Criteria, Release Decision, Approver

Notes:
- Each SOP must include Approval block (Name/Role/Date/Version) and be linked into Reference_Map with the exact SOP-TS-### ID.
- FRMs should be simple Google Sheets templates; keep them minimal to support automation parsing (consistent header names).
