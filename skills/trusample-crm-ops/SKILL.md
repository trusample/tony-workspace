---
name: trusample-crm-ops
description: >-
  Operate the TruSample CRM (quotes, orders/projects, invoices, POs) using the
  existing Google Sheets + Apps Script backend and the trusample-crm repo.
  Use this skill whenever Maykel asks you to create/update quotes, convert
  quotes to orders, generate invoices, or reason about the CRM pipeline.
---

# TruSample CRM Ops Skill

This skill defines how Tony should operate the **TruSample CRM** safely and
consistently. The CRM backend lives in:

- Google Sheets workbook (CRM): `1NyYihFTchiur_Nrj5Vz0LSxw1PP4aY6ttctn4G2cT4E`
- Apps Script project (linked via `crm_code` on CELLABIOS and `trusample-crm`
  repo on `hernandez-server`)
- Local repo on server: `/home/mhernandez/clawd/trusample-crm`
- Local repo on CELLABIOS: `G:\...\02_Database_CRM\crm_code`

## Entities

The CRM models these core entities (via Sheets tabs + scripts):

- **Accounts** – Accounts tab (`AccountID`, `AccountName`, ...)
- **Contacts** – Contacts tab (`ContactID`, `AccountID`, ...)
- **Products** – Products tab (`ProductID`, ...)
- **Quotes** – Quotes + QuoteLines tabs (header + line items)
- **Orders / Projects** – Orders + OrderLines tabs
- **Invoices** – Invoices + InvoiceLines tabs
- **Purchase Orders (POs)** – PurchaseOrders tab (+ future PO lines)

## Backends & APIs

### Sheets

When you need raw data or metrics, use the Google Sheets API (via the
`trusample-crm/dashboard` helpers) against:

- Spreadsheet ID: `1NyYihFTchiur_Nrj5Vz0LSxw1PP4aY6ttctn4G2cT4E`
- Tabs:
  - `Accounts`
  - `Contacts`
  - `Products`
  - `Quotes`, `QuoteLines`
  - `Orders`, `OrderLines`
  - `Invoices`, `InvoiceLines`
  - `PurchaseOrders`

### Apps Script (CRM logic)

Core logic is implemented in the Apps Script files in the CRM project
(and mirrored in `/home/mhernandez/clawd/trusample-crm`):

- `QuoteManagement.js`
- `OrderManagement.js`
- `AccountManagement.js`
- `ProductIntegration.js`
- `ContactLifecycle.js`
- `WebPortal.js`, `PortalHTML.html`, `Sidebar.html`, `ui_crm.js`

#### Public APIs (current)

These are entry points you can call (or design UI around):

- `crmQuoteToOrder(quoteId)`
  - Thin wrapper around `convertQuoteToOrderEnhanced(quoteId)`
  - Validates quote, checks permissions, creates Order + OrderLines and
    updates quote status to `Converted`.

> NOTE: More APIs will be added over time (quote create, invoice from order,
> PO create, etc.). When you add them, document them here.

## Safety & Permissions

- Always respect the existing permission checks in the Apps Script:
  - `checkPermission(userEmail, action)`
  - `logPermissionAllowed/Denial`
- Do **not** bypass role checks (e.g., APPROVER / ADMIN) by editing scripts
  unless Maykel explicitly asks.
- For destructive or high-impact changes (bulk status changes, deleting
  entities, etc.), ask Maykel for confirmation, or operate in **draft mode**
  (propose changes instead of applying them).

## Typical Workflows

Use this skill when Maykel asks you to operate the CRM. Default to these
patterns.

### 1) Convert an approved quote to an order/project

When asked to convert a quote:

1. Verify the quote is in `Approved` status and not expired.
2. Use `crmQuoteToOrder(quoteId)`:
   - If calling from within Apps Script, call the function directly.
   - If calling from the UI, wire a button or menu item to call it.
3. Confirm:
   - A new `OrderID` appears in `Orders`.
   - Matching lines in `OrderLines`.
   - Quote status updated to `Converted`.
4. Log the result back to Maykel (quote ID, order ID, any warnings).

### 2) Inspect CRM pipeline health

1. Use the dashboard backend (`/dashboard/server.js`) via
   `/api/crm/summary` to get counts for:
   - Quotes by status
   - Orders by status
   - Invoices (Draft/Sent/Paid/Overdue)
   - POs (Open/Closed)
2. Summarize for Maykel:
   - Where deals are stuck (e.g., many Draft quotes, few Approved).
   - Any invoices in Draft for too long.

### 3) Investigate or explain a specific quote/order/invoice

1. Use Sheets API or Apps Script helpers:
   - `getQuote(quoteId)`
   - `getQuoteLines(quoteId)`
   - Similar helpers in `OrderManagement.js` / invoice modules.
2. Present a concise view:
   - Header (account, amounts, dates, status).
   - Line items.
   - Links to Docs/Drive (proposal, invoice PDF).

## Allowed Tools

When operating under this skill on `hernandez-server`:

- `exec` (within `/home/mhernandez/clawd` only)
  - For running node/dashboard scripts, git operations on `trusample-crm`,
    and safe diagnostics.
- Google APIs via `googleapis` in the `trusample-crm` repo.
- `clawdbot cron` / `clawdbot` CLI for status and cron inspection.

Avoid:

- Editing CRM sheet structures directly (adding/removing columns) without
  explicit instruction.
- Changing Apps Script permission logic (`checkPermission`, roles) unless
  Maykel explicitly requests the change and understands the impact.

## Future Extensions

When Maykel is ready, extend this skill with:

- `crmQuoteCreate(payload)` – structured quote creation.
- `crmInvoiceCreateFromOrder(orderId)` – invoice generation.
- `crmInvoiceUpdateStatus` and `crmPOCreate`.
- UI routes in `WebPortal.js` / `PortalHTML.html` that use these APIs.

Document each new API here as you add it, so future you (and future Tony)
know the intended behaviors and safety constraints.
