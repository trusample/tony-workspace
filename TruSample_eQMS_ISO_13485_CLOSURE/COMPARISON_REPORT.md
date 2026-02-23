COMPARISON_REPORT — Existing eQMS vs Prepared Deliverables
Generated: 2026-02-11T06:50:00Z
Source: /opt/trusample/trusample_eqms/TruSample_eQMS/_state/STATE_PACK_REL-20251231-0146.json

Summary
I audited the mounted eQMS snapshot (STATE_PACK) and the workspace deliverables you asked me to prepare. Below is a side-by-side comparison of what currently exists in the eQMS (per the state pack and folder exports) vs. what was prepared in the review package, with recommendations for reuse, completion, or fresh creation.

1) SOPs (proposed list vs existing)
Proposed SOPs prepared:
- SOP-TS-010 Document Control (prepared)
- SOP-TS-020 Change Control (prepared)
- SOP-TS-021 Management Actions & Review (prepared)
- SOP-TS-030 CAPA & NCR (prepared)
- SOP-TS-040 Training (prepared)
- SOP-TS-050 Records Retention (prepared)
- SOP-TS-060 Lot Release & COA (prepared)
- SOP-TS-080 Design Control & RUO (prepared)

What exists (from Reference_Map in state pack):
- Reference_Map contains entries for SOP-TS-010 through SOP-TS-080, but the Link field is EMPTY for all of them and Status=Pending.
- There are step entries in eQMS_Master_Steps that reference some SOP IDs, but they point to empty links (Evidence_Link often empty).

Assessment:
- None of the SOP Google Docs appear to be present in Drive (or at least not linked in Reference_Map). Therefore: SOP documents are effectively missing in Drive even though they are registered as Reference IDs.
- Reuse: The state pack contains SOP references and expected FRM mapping. Use these as authoritative IDs and titles — reuse the IDs and text in the prepared SOPs.
- Action: Create the SOP Docs in Google Drive and update Reference_Map Link fields. Do NOT recreate IDs — use the registered IDs.

Status category:
- "Exists": Registered in Reference_Map but Link missing -> treat as MISSING (no usable doc)
- Recommendation: Create/publish SOPs from SOP_Google_Docs_Ready files and set Reference_Map.Link accordingly.

2) Forms (FRM-*)
What exists (state pack):
- FRM entries listed (FRM-TS-203, FRM-TS-204, FRM-TS-205, FRM-TS-301.., FRM-TS-504, FRM-TS-005) — Link fields empty and Status=Pending.

Assessment:
- Forms are registered but not linked; likely templates are not present or not linked into Reference_Map.
- Reuse: FRM IDs and titles in state pack are authoritative. Prepared FRM field templates in SOP_and_FRM_drafts.md can be converted to Google Sheets or Docs.
- Status category: Missing (registered but no document present).

3) Google Sheets (Master Tracker, validation records, etc.)
What exists:
- Master Implementation Tracker: name/id present in schema_pack: TruSample_eQMS_Master_Implementation_Tracker (id: 19Wu8fUT3v7G8ETFL5j2o4UgeSW9vxSF0d1HSzinM2Ng). Tabs present include eQMS_Master_Steps, MGMT_REVIEW_ACTIONS, Completed_History, Assignable_Task_View, Reference_Map, Automation_Index, CONFIG, LOOKUPS, Dashboard, Documents_Index_Cache.
- STATE_PACK JSON includes many exported rows from these tabs (modules list, automation registry, lookups, config KV).

Assessment:
- The Master Tracker spreadsheet is present and well-populated. This is a major reusable asset — do NOT replace; only augment by adding Links to SOP Google Docs and FRM templates.
- Documents_Index_Cache exists and is being written by automation (referenced in steps). Use it as the primary evidence index.
- Completed_History provides an audit trail — present and should be preserved.

Status category:
- "Exists and Reusable": Master Tracker, Documents_Index_Cache, Automation_Index entries present.
- What's 80% done: Automation_Index and many automations implemented; some validation artifacts referenced are missing (evidence links).

4) Reference_Map in Master Tracker
What exists:
- Reference_Map lists SOPs, FRMs, VALs, SCRIPTS, but Link fields are empty and Status often Pending.

Assessment:
- Reference_Map structure is correct and is the central place to store doc links. The missing Links are the key gap. Populating Link and Status fields is high-priority and low-effort once SOPs/FRMs are created.

Status category:
- "Exists but incomplete": needs Link population and Status updates.

5) Automations / Apps Script
What exists (from Automation_Index and registries):
- Implemented functions (bound scripts) include:
  - onEditHandler (Tracker)
  - menuCreateMgmtActionFromChange
  - Run Mgmt Action Reminders Now
  - menuConvertQuoteToOrder, menuCreateBlankPO
  - pcShowShipWorkflowWizardSidebar (Shipments)
  - pcEnsureDocumentsIndexSheet_
  - menuGenerateCOAForLot, generateCOAForLot_
- Automation behaviors claimed live: management reminders (email), COA generation, Batch Close creation, Documents_Index write, CRM menu functions, shipment wizard.

Assessment:
- Automations are implemented and appear functional. The state pack includes Automation_Index rows and modules references. This is a major reusable asset.
- Missing: Validation evidence for automations (VAL-ENG-COA-001, VAL-ENG-BATCH-001, VAL-ENG-REM-001) — entries exist but links empty.

Status category:
- "Exists and functioning": scripts and triggers mostly present.
- "Needs validation evidence": create validation reports and attach to Reference_Map and Documents_Index.

6) Training records / Competency matrices
What exists:
- eQMS_Master_Steps references a Training Matrix as an active module; Training Matrix is listed in earlier handoff notes.
- STATE_PACK does not include detailed Training Matrix rows or links; no FRM or link entries found for training records.

Assessment:
- Training Matrix structure may exist as a tab or planned sheet, but records are not populated / evidence not linked.

Status category:
- "Partially present / 20%": requires population with personnel and completion evidence.

7) Audit packs / evidence
What exists:
- Audit_Packs folder exists with two AuditPack_20251230_* packs containing handoff exports and MANIFESTs.
- _state contains multiple STATE_PACK JSON snapshots (we copied one into audit skeleton).

Assessment:
- Some audit-pack exports exist (hand-off text). However, core evidence items (COA PDFs, Batch Close PDFs, validation test run artifacts) are not present in mounted folder evidence lists.

Status category:
- "Partially present": audit pack skeletons exist; need to populate with exported evidence files.

Side-by-side comparison table (high level)
- SOP-TS-010 Document Control: Registered (Reference_Map) — Link empty -> Prepared in workspace -> Action: CREATE doc and link (Priority 1)
- SOP-TS-020 Change Control: Registered -> Prepared -> Action: CREATE doc and link (Priority 2)
- SOP-TS-021 Mgmt Actions: Registered -> Prepared -> Action: CREATE doc and link (Priority 5)
- SOP-TS-030 CAPA/NCR: Registered -> Prepared -> Action: CREATE doc and link (Priority 4)
- SOP-TS-040 Training: Registered (sheet reference exists but not populated) -> Prepared -> Action: Populate Training Matrix + create SOP doc (Priority 6)
- SOP-TS-050 Records Retention: Registered -> Prepared -> Action: CREATE doc and link (Priority 7)
- SOP-TS-060 COA/Lot Release: Registered, automation implemented (COA generator) -> Prepared -> Action: COMPLETE validation evidence and create SOP doc (Priority 3)
- SOP-TS-080 Design Control RUO: Registered -> Prepared -> Action: Create doc + attach DHF artifacts (Priority 8)

What's 80% done (quick wins)
- Automations: Implemented (onEditHandler, COA generation, batch generators, docs index). Need validation evidence only — creates a fast path to compliance once validation artifacts are produced.
- Documents_Index & Tracker: Tabs and structure present; need Link population and minor evidence attachments.

What's genuinely missing / must-create
- Actual SOP documents in Drive linked from Reference_Map (none present)
- FRM templates (Google Sheets / Docs) linked in Reference_Map
- Validation packages (detailed test results, screenshots, sign-offs) for COA, Batch Close, Reminders
- Training records population
- Evidence artifacts: COA PDFs, Batch Close Reports exported and placed into Audit_Packs/evidence

Reuse vs Create Fresh
- Reuse: Master Tracker, Automation code, Documents_Index, Completed_History, MANIFEST templates, Reference IDs/IDs/naming conventions.
- Create Fresh: Google Doc SOP files (from prepared .md), FRM Google Sheets (templates), validation evidence documents (test reports), completed Training Matrix entries.

Priority order for finishing vs creating (recommended)
Immediate (0–2 days):
1. Create SOP-TS-010 Document Control doc and publish -> update Reference_Map Link.
2. Create FRM templates required for Change Control and Mgmt Actions (FRM-TS-203, FRM-TS-204, FRM-TS-205) and link them.
3. Populate Reference_Map Links for any existing documents you already have (use missing_links_report as guide).

Short term (3–7 days):
4. Execute validation test cases for Reminder system and COA generator; collect evidence and attach to Documents_Index and Reference_Map (VAL-ENG-REM-001, VAL-ENG-COA-001).
5. Create SOP-TS-020 Change Control and SOP-TS-060 COA docs (publish + link).
6. Populate Training Matrix with sample records; create SOP-TS-040 doc and link.

Medium term (1–3 weeks):
7. Complete CAPA/NCR process docs and evidence (SOP-TS-030 + FRM templates), run a mock NCR/CAPA case and attach evidence.
8. Assemble Audit Pack: export Documents_Index CSV, include STATE_PACK JSON, attach COA/Batch sample PDFs, validation packages, and internal audit report.

Longer term (ongoing):
9. Design Control DHF population and SOP-TS-080 finalization; supplier controls and retention schedules.

Recommendations & next actions I can run for you
- Auto-create Google Docs for the SOPs and FRM Google Sheet templates (requires Google API credentials). I will then update Reference_Map Link fields in the Master Tracker (also needs Drive/Sheets API access).
- Run validation test runners (if you want automated test runs against a test copy of the tracker). This will generate the VAL artifacts automatically.
- Populate Documents_Index_Cache export into the Audit_Pack_SKELETON/evidence/ folder (I can extract rows from the STATE_PACK JSON into CSV now).

Shall I extract Documents_Index_Cache into CSV and place it in the Audit_Pack_SKELETON/evidence/ folder now? (yes/no)
