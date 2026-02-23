# EQMS Apps Script Evidence (auto)
This report is generated from Apps Script API project source (read-only).
Projects found: **6**

## 0AMooSbVaWDeSUk9PVA
- projectId: `1lVWgyYksZ7qxx0nSAavUkcbcyIBZgaBLOhwimb7hI1V22Dy2RGWgJFwx`
- modifiedTime: `2025-12-09T05:11:06.739Z`
- keyword hits: **8**

| file | match | snippet |
|---|---|---|
| `{fname}` | `{match}` | arent.createFolder("04 – Validation");   folders["05 – Risk Management"]           = parent.createFolder("05 – Risk Management");  |
| `{fname}` | `{match}` | isk Management"]           = parent.createFolder("05 – Risk Management");   folders["06 – Stability & Commutability"] = parent.cre |
| `{fname}` | `{match}` | ion",     "Validation Summary Report"   ]);    // 05 – Risk Management   addSubs(folders["05 – Risk Management"], [     "RMA-HbA1c |
| `{fname}` | `{match}` | ]);    // 05 – Risk Management   addSubs(folders["05 – Risk Management"], [     "RMA-HbA1c-001 – Risk Analysis",     "FMEA",     " |
| `{fname}` | `{match}` | );   var risk      = getOrCreateSubFolder_(root, "05 – Risk Management");   var stab      = getOrCreateSubFolder_(root, "06 – Stab |
| `{fname}` | `{match}` | , Date, Reporter, Description, Impact Assessment, Immediate Actions, Root Cause, Corrective Actions, Preventive Actions, Closu |
| `{fname}` | `{match}` | mpact Assessment, Immediate Actions, Root Cause, Corrective Actions, Preventive Actions, Closure.\n"   );    // Training / Com |
| `{fname}` | `{match}` | mediate Actions, Root Cause, Corrective Actions, Preventive Actions, Closure.\n"   );    // Training / Competency Assessment T |

## CRM SHEET - TruSample
- projectId: `1yDT7YEpAVx3OUnSBjxqTgd4OyS0XKaV0-RX4R-dnOI6vcHG2SFzSVK0e`
- modifiedTime: `2026-01-24T06:57:57.464Z`
- keyword hits: **34**

| file | match | snippet |
|---|---|---|
| `{fname}` | `{match}` | ;  const PERMISSION_MATRIX = {   'ADMIN': {     // User Management     'user.create': true,     'user.assign_role': true,   |
| `{fname}` | `{match}` | : true,     'activity.delete': true,          // Product Management     'product.create': true,     'product.edit': true,    |
| `{fname}` | `{match}` | audit.export': true   },      'APPROVER': {     // User Management     'user.create': false,     'user.assign_role': false, |
| `{fname}` | `{match}` |  true,     'activity.delete': false,          // Product Management     'product.create': false,     'product.edit': false,  |
| `{fname}` | `{match}` |  'audit.export': false   },      'SALES': {     // User Management     'user.create': false,     'user.assign_role': false, |
| `{fname}` | `{match}` |  true,     'activity.delete': false,          // Product Management     'product.create': false,     'product.edit': false,  |
| `{fname}` | `{match}` | port': false   },      'PRODUCT_MANAGER': {     // User Management     'user.create': false,     'user.assign_role': false, |
| `{fname}` | `{match}` | false,     'activity.delete': false,          // Product Management     'product.create': true,     'product.edit': true,    |
| `{fname}` | `{match}` | 'audit.export': false   },      'VIEWER': {     // User Management     'user.create': false,     'user.assign_role': false, |
| `{fname}` | `{match}` |  true,     'activity.delete': false,          // Product Management     'product.create': false,     'product.edit': false,  |
| `{fname}` | `{match}` |  }  /**  * Check if a user has permission to perform an action  * @param {string} userEmail - User email address  * @par |
| `{fname}` | `{match}` | {string} userEmail - User email address  * @param {string} action - Action to check (e.g., 'quote.create', 'order.approve')  |
| `{fname}` | `{match}` | userEmail - User email address  * @param {string} action - Action to check (e.g., 'quote.create', 'order.approve')  * @retur |
| `{fname}` | `{match}` | , false otherwise  */ function checkPermission(userEmail, action) {   const role = getUserRole(userEmail);      if (!role |
| `{fname}` | `{match}` | r inactive - log denial     logPermissionDenial(userEmail, action, 'User not found or inactive');     return false;   }    |
| `{fname}` | `{match}` |    if (!permissions) {     logPermissionDenial(userEmail, action, 'Invalid role: ' + role);     return false;   }      c |
| `{fname}` | `{match}` | return false;   }      const hasPermission = permissions[action] === true;      if (!hasPermission) {     logPermissionD |
| `{fname}` | `{match}` |   if (!hasPermission) {     logPermissionDenial(userEmail, action, 'Permission denied for role: ' + role);   }      return |
| `{fname}` | `{match}` | ing  *   * @param {string} userEmail - User who attempted action  * @param {string} action - Action attempted  * @param {s |
| `{fname}` | `{match}` | } userEmail - User who attempted action  * @param {string} action - Action attempted  * @param {string} reason - Reason for  |
| `{fname}` | `{match}` | il - User who attempted action  * @param {string} action - Action attempted  * @param {string} reason - Reason for denial   |
| `{fname}` | `{match}` | on for denial  */ function logPermissionDenial(userEmail, action, reason) {   try {     const ss = SpreadsheetApp.openById |
| `{fname}` | `{match}` | stamp,       'PERMISSION_DENIED',       userEmail,       action,       reason,       'SYSTEM'     ];          auditShe |
| `{fname}` | `{match}` | ations  *   * @param {string} userEmail - User performing action  * @param {string} action - Action performed  * @param {s |
| `{fname}` | `{match}` | ing} userEmail - User performing action  * @param {string} action - Action performed  * @param {string} details - Additional |
| `{fname}` | `{match}` | Email - User performing action  * @param {string} action - Action performed  * @param {string} details - Additional details |
| `{fname}` | `{match}` | onal details  */ function logPermissionAllowed(userEmail, action, details) {   try {     const ss = SpreadsheetApp.openByI |
| `{fname}` | `{match}` | tamp,       'PERMISSION_ALLOWED',       userEmail,       action,       details,       'SYSTEM'     ];          auditSh |
| `{fname}` | `{match}` | only)  * @param {string} adminEmail - Admin performing the action  * @param {string} targetEmail - User to assign role to   |
| `{fname}` | `{match}` | ; // Update role in column B                  // Log this action to audit         logPermissionAllowed(adminEmail, 'user.as |
| `{fname}` | `{match}` |  a guard at the start of functions  *   * @param {string} action - Action to validate  * @returns {boolean} - True if user  |
| `{fname}` | `{match}` | at the start of functions  *   * @param {string} action - Action to validate  * @returns {boolean} - True if user has permi |
| `{fname}` | `{match}` | f user has permission  */ function validateUserPermission(action) {   const userEmail = Session.getActiveUser().getEmail(); |
| `{fname}` | `{match}` | tiveUser().getEmail();   return checkPermission(userEmail, action); }  /**  * Get current user's role  * @returns {strin |

## Creates all core Docs & Sheets templates
- projectId: `1PYPNY3FjcC03SQqdACKxVXho-47p2Zxvl_82OBYyakrdCIxBmw2IDicP`
- modifiedTime: `2025-12-09T05:10:27.946Z`
- keyword hits: *(none)*

## PROJECT_HANDOFFS_IndexUpdater
- projectId: `1FL-7FHZ_u6JNiBEYqknlUmadxdg1y9PV5FYtVmqqaTwyNsQ3hdjW4u5J`
- modifiedTime: `2025-12-31T03:21:54.050Z`
- keyword hits: **10**

| file | match | snippet |
|---|---|---|
| `{fname}` | `{match}` | ndoff version doc link  *  * Safe: manual run OR time-based trigger (optional).  * Deterministic: uses folder IDs (recommended) |
| `{fname}` | `{match}` | .  * (Lightweight, safe)  */ function setupHandoffIndexDailyTrigger() {   removeHandoffIndexTriggers_();   ScriptApp.newTrigger |
| `{fname}` | `{match}` | ction setupHandoffIndexDailyTrigger() {   removeHandoffIndexTriggers_();   ScriptApp.newTrigger("updateHandoffIndexLatestLinks" |
| `{fname}` | `{match}` | offIndexDailyTrigger() {   removeHandoffIndexTriggers_();   ScriptApp.newTrigger("updateHandoffIndexLatestLinks")     .timeBased()     .ever |
| `{fname}` | `{match}` |  ScriptApp.newTrigger("updateHandoffIndexLatestLinks")     .timeBased()     .everyDays(1)     .atHour(6)     .create(); }  functi |
| `{fname}` | `{match}` |    .atHour(6)     .create(); }  function disableHandoffIndexTriggers() {   removeHandoffIndexTriggers_(); }  function removeHan |
| `{fname}` | `{match}` | unction disableHandoffIndexTriggers() {   removeHandoffIndexTriggers_(); }  function removeHandoffIndexTriggers_() {   ScriptAp |
| `{fname}` | `{match}` | emoveHandoffIndexTriggers_(); }  function removeHandoffIndexTriggers_() {   ScriptApp.getProjectTriggers().forEach(function (t) |
| `{fname}` | `{match}` | ction removeHandoffIndexTriggers_() {   ScriptApp.getProjectTriggers().forEach(function (t) {     if (t.getHandlerFunction() == |
| `{fname}` | `{match}` | tion() === "updateHandoffIndexLatestLinks") ScriptApp.deleteTrigger(t);   }); }  /** ===================== Helpers ============ |

## TECH_STACK_AutoCheckpoint
- projectId: `1jH7pB3Vn0bu9K5Xmz7TqEXsh4YDuaazwJGRh4BsWIvq4-DFtwNop-LN2`
- modifiedTime: `2025-12-30T22:50:26.995Z`
- keyword hits: **1**

| file | match | snippet |
|---|---|---|
| `{fname}` | `{match}` | oint  *  * Manual snapshot of /TECH_STACK/_handoff.md  * No triggers. No sheet dependencies.  ********************************* |

## Untitled project
- projectId: `1qKYlqKWH4Cpjh_NgDfA_G3qE-uX0d6EATZBZ2a-QtFIfVkiIcqTfQjYD`
- modifiedTime: `2026-01-25T06:40:54.849Z`
- keyword hits: *(none)*
