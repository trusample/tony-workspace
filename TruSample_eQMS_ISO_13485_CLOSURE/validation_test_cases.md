Validation Test-Case Templates — Key Automations
Generated: 2026-02-11T06:31:00Z

A) COA Generator (VAL-ENG-COA-001) — Test Plan & Test Cases
- Objective: Verify generateCOAForLot_ produces correct COA documents for valid lots and handles invalid input gracefully.
- Test environment: Test spreadsheet copy; sample Lot Release Log with test lots.
- Acceptance criteria:
  1. Valid lot -> COA created with correct fields populated (Lot ID, Test Results, Pass/Fail, Signature placeholder).
  2. COA file saved to configured COA folder; Documents_Index_Cache row created with correct metadata.
  3. Invalid or missing lot -> script alerts user, does not create COA, and logs an incident in Reminder/Change log as needed.
- Test cases:
  TC-COA-001: Generate COA for valid lot with all required fields present. Expect: COA created; Index row created; file URL valid.
  TC-COA-002: Generate COA for lot with missing test result. Expect: UI alert; no COA created; error logged.
  TC-COA-003: Generate COA for lot with out-of-spec test result. Expect: COA marks 'NOT RELEASED' and includes deviation reference.
  TC-COA-004: Simulate permission error on write (Docs folder read-only). Expect: script catches error, logs failure, notifies owner.
- Evidence to collect: Screenshots, generated COA file (PDF), Documents_Index_Cache row export, script logs, sign-off.

B) Batch Closeout Generator (VAL-ENG-BATCH-001)
- Objective: Confirm BatchClose_<BatchID> creation and Batch Close Report generator produce correct reports and index entries.
- Acceptance criteria:
  1. BatchClose sheet created with correct metadata from creation form.
  2. Build Batch Close Report aggregates data and attaches evidence links.
  3. Documents_Index_Cache receives row with Batch Close Report metadata and URL.
- Test cases:
  TC-BATCH-001: Create batch with full data, run Batch Close generator. Expect: PDF report created; index entry created.
  TC-BATCH-002: Missing raw material lot numbers. Expect: generator flags missing info and fails with clear error.
  TC-BATCH-003: Include deviation entry in batch; expect deviation recorded in report and cross-linked to CAPA/NCR.
  TC-BATCH-004: Concurrent batch creation stress test: generate 10 batch close requests rapidly; expect no collisions, unique IDs, and all reports created.
- Evidence: Generated reports, index rows, logs, screenshots, test execution matrix, sign-off.

C) Management Action Reminder System (VAL-ENG-REM-001)
- Objective: Confirm reminders send correctly and only to open/unclosed actions; CC team_iso and respect DUE_SOON_DAYS/OVERDUE_DAYS.
- Acceptance criteria:
  1. Due soon and overdue actions are correctly identified by dates.
  2. Emails are sent to Owner with CC to team_iso for both cases.
  3. Closed actions are excluded from reminders.
- Test cases:
  TC-REM-001: Action with due date within DUE_SOON_DAYS. Expect: Due-soon email sent; log entry in FRM-TS-205.
  TC-REM-002: Action overdue by >OVERDUE_DAYS. Expect: Overdue email sent; escalation flag set.
  TC-REM-003: Action marked Closed prior to reminder run. Expect: No email sent for that action.
  TC-REM-004: Email system failure simulated (SMTP error). Expect: system logs failure and places a record in Completed_History referencing the failed sends.
- Evidence: Email headers/exports, FRM-TS-205 entries, script logs, screenshots.

Notes on validation artifacts
- For each test case produce:
  - Test script (steps performed)
  - Expected result
  - Actual result (with artifacts: screenshots, exported files)
  - Verdict (Pass/Fail)
  - Approver signature and date

Traceability matrix
- Map each test case to the relevant SOP/FRM and to eQMS_Master_Steps Step_IDs.
