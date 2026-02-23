Internal Audit Checklist + Audit Pack Skeleton
Generated: 2026-02-11T06:32:00Z

A) Internal Audit Checklist (focused on ISO 13485 essentials for current eQMS)
- Document Control
  - Are all controlled documents listed in Reference_Map with valid links and status? (Y/N)
  - Do controlled documents have version, effective date, and approver recorded? (Y/N)
  - Is Documents_Index_Cache capturing generated artifacts with metadata? (Y/N)
- Change Control
  - Are change records (FRM-TS-203) complete and linked to Mgmt Actions? (Y/N)
  - Are changes risk-assessed and validated where needed? (Y/N)
- CAPA/NCR
  - Is a CAPA/NCR log present and populated with evidence of root cause and closure? (Y/N)
- Training & Competency
  - Is Training Matrix present and populated? (Y/N)
  - Are training records linked to individuals and timestamped? (Y/N)
- Production & Batch Records
  - Are batch records generated and stored with required metadata? (Y/N)
  - Are Batch Close Reports present in Documents_Index? (Y/N)
- COA & Lot Release
  - Are COAs generated and linked to Lot Release Log? (Y/N)
  - Are approval/signature records present? (Y/N)
- Automation & Validation
  - Are automations registered (Automation_Index) and documented? (Y/N)
  - Are validation packages present for critical automations? (Y/N)
- Records Retention & Access
  - Is storage location and retention period documented? (Y/N)
  - Are access permissions controlled and documented? (Y/N)
- Internal Audit Evidence
  - Is there evidence of prior internal audits and closure of findings? (Y/N)

B) Audit Pack Skeleton (folder/file list to include in an Audit Pack)
- AuditPack_<timestamp>/
  - MANIFEST.txt (metadata + links)
  - audit_report.md (internal audit findings + summary)
  - evidence/
    - documents_index_export.csv
    - state_pack.json (copy of STATE_PACK_REL-...json)
    - COA_examples/ (sample COA PDFs + index rows)
    - BatchClose_examples/ (sample Batch Close Reports + index rows)
    - Validation/ (validation packages for COA, Batch Close, Reminders)
    - Change_Control/ (selected change records + mgmt actions + closure evidence)
    - Training/ (Training Matrix + sample training records)
    - Scripts/ (exported Apps Script project files or links)
  - signoffs.md (list of approvers and dates)
  - internal_audit_checklist_filled.md

C) Recommended immediate evidence collection actions
1. Export Documents_Index_Cache to CSV and add to evidence/
2. Export latest STATE_PACK_REL-*.json into evidence/
3. Gather example COA PDFs and batch close PDFs (place in respective example folders)
4. Collect validation run outputs (test case pass/fail, screenshots)
5. Add MANIFEST.txt with links and timestamp

I can optionally build the AuditPack folder and populate it with skeleton files and copies of the STATE_PACK from _state into /home/mhernandez/clawd/TruSample_eQMS_ISO_13485_CLOSURE/Audit_Pack_SKELETON/ — say 'build auditpack' if you want that now.
