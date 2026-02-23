SOP-TS-010 — Document Control
Purpose
Define the process for creating, approving, distributing, revising, and retiring controlled documents within the TruSample eQMS.

Scope
Applies to all controlled documents (SOPs, forms, templates, records) managed within the TruSample eQMS and Google Drive.

Responsibilities
- QMS Owner: final approvals and governance
- Document Owner: maintain content and submit revisions
- Tracker Admin: update Reference_Map links and CONFIG values
- Quality Reviewer: review and approve revisions

Procedure
1. Document creation
   - Draft the document using the company template.
   - Assign a Reference_ID (SOP-TS-### or FRM-TS-###) and populate metadata (Title, Owner, Version, Effective Date).
2. Review and approval
   - Submit for review via the eQMS change control workflow or directly to Quality Reviewer.
   - Record approver name, role, date, and version in the document header.
3. Publication & distribution
   - Publish the final Google Doc in /TruSample/eQMS/SOPs and add an entry in Reference_Map with Link and Status=Approved.
   - Notify affected personnel via SOP release notice; record notification as evidence.
4. Revision control
   - Minor edits: increment minor version; record change summary in document history.
   - Major edits: raise a Change Request (FRM-TS-203); follow change control SOP.
5. Obsolete documents
   - Mark as Obsolete in Reference_Map; move to /TruSample/eQMS/Archive with retention metadata.

Records
- Documents_Index entry for each controlled doc
- Completed_History entries for approvals/changes

Approvals
- Prepared by: __________________  Date: ______
- Reviewed by: __________________ Date: ______
- Approved by: __________________ Date: ______

Notes
- Ensure the REF ID matches Reference_Map exactly when updating the tracker.
