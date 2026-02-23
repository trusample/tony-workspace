SOP-TS-021 — Management Actions & Review
Purpose
Define the lifecycle of Management Actions, reminders, and how Management Reviews are conducted and recorded.

Scope
All management actions arising from change control, CAPA, audits, or routine QMS activities.

Procedure
1. Creation
   - Mgmt Actions created from Change (menuCreateMgmtActionFromChange) or entered manually.
   - Required fields: Action ID, Source Change ID (optional), Owner, Due Date, Priority, Description.
2. Automated Reminders
   - System identifies Due Soon and Overdue actions based on CONFIG (DUE_SOON_DAYS, OVERDUE_DAYS).
   - Reminders are sent to Owner; CC team_iso; entries logged in FRM-TS-205.
3. Execution & Closure
   - Owner updates status and provides closure evidence; automation logs into Completed_History.
4. Management Review Meetings
   - Schedule periodic reviews; include summary of open actions, CAPAs, NCRs, and audit findings.
   - Record meeting minutes and action assignments in Documents_Index.

Records
- FRM-TS-204 (Mgmt Action record)
- FRM-TS-205 (Reminder Evidence)
- Management review minutes in Documents_Index

Approvals
- Prepared by: __________________  Date: ______
- Approved by: __________________ Date: ______
