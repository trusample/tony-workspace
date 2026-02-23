SOP-TS-060 — Lot Release & Certificate of Analysis (COA)
Purpose
Define lot release criteria, COA generation, approval, and distribution.

Scope
Applies to all manufacturing lots and the COA generation process.

Procedure
1. Lot Release Log (FRM-TS-005)
   - Record Lot ID, manufacture date, tests performed, results, acceptance criteria, and recommended release status.
2. COA Generation
   - Use menuGenerateCOAForLot to generate COA from Lot Release Log via generateCOAForLot_.
   - COA must include Lot ID, test results, pass/fail, release decision, and approver signature block.
3. Approval
   - Quality Reviewer verifies COA and records approval (name/date/version) in the COA or in Documents_Index.
4. Distribution & Archival
   - Save COA in /TruSample/eQMS/COA; create Documents_Index entry linking COA to Lot ID, file URL, and approver.

Records
- Lot Release Log (FRM-TS-005)
- COA PDF/document in Drive
- Documents_Index entry for each COA

Approvals
- Prepared by: __________________  Date: ______
- Approved by: __________________ Date: ______
