# EQMS Apps Script Evidence (auto)
This report is generated from Apps Script API project source (read-only).
Projects found: **6**

## 0AMooSbVaWDeSUk9PVA
- projectId: `1lVWgyYksZ7qxx0nSAavUkcbcyIBZgaBLOhwimb7hI1V22Dy2RGWgJFwx`
- modifiedTime: `2025-12-09T05:11:06.739Z`
- keyword hits: **8**

| file | match | snippet |
|---|---|---|
| `Code` | `Management` | arent.createFolder("04 – Validation");   folders["05 – Risk Management"]           = parent.createFolder("05 – Risk Management");  |
| `Code` | `Management` | isk Management"]           = parent.createFolder("05 – Risk Management");   folders["06 – Stability & Commutability"] = parent.cre |
| `Code` | `Management` | ion",     "Validation Summary Report"   ]);    // 05 – Risk Management   addSubs(folders["05 – Risk Management"], [     "RMA-HbA1c |
| `Code` | `Management` | ]);    // 05 – Risk Management   addSubs(folders["05 – Risk Management"], [     "RMA-HbA1c-001 – Risk Analysis",     "FMEA",     " |
| `Code` | `Management` | );   var risk      = getOrCreateSubFolder_(root, "05 – Risk Management");   var stab      = getOrCreateSubFolder_(root, "06 – Stab |
| `Code` | `Action` | , Date, Reporter, Description, Impact Assessment, Immediate Actions, Root Cause, Corrective Actions, Preventive Actions, Closu |
| `Code` | `Action` | mpact Assessment, Immediate Actions, Root Cause, Corrective Actions, Preventive Actions, Closure.\n"   );    // Training / Com |
| `Code` | `Action` | mediate Actions, Root Cause, Corrective Actions, Preventive Actions, Closure.\n"   );    // Training / Competency Assessment T |

## CRM SHEET - TruSample
- projectId: `1yDT7YEpAVx3OUnSBjxqTgd4OyS0XKaV0-RX4R-dnOI6vcHG2SFzSVK0e`
- modifiedTime: `2026-01-24T06:57:57.464Z`
- keyword hits: **34**

| file | match | snippet |
|---|---|---|
| `Permissions` | `Management` | ;  const PERMISSION_MATRIX = {   'ADMIN': {     // User Management     'user.create': true,     'user.assign_role': true,   |
| `Permissions` | `Management` | : true,     'activity.delete': true,          // Product Management     'product.create': true,     'product.edit': true,    |
| `Permissions` | `Management` | audit.export': true   },      'APPROVER': {     // User Management     'user.create': false,     'user.assign_role': false, |
| `Permissions` | `Management` |  true,     'activity.delete': false,          // Product Management     'product.create': false,     'product.edit': false,  |
| `Permissions` | `Management` |  'audit.export': false   },      'SALES': {     // User Management     'user.create': false,     'user.assign_role': false, |
| `Permissions` | `Management` |  true,     'activity.delete': false,          // Product Management     'product.create': false,     'product.edit': false,  |
| `Permissions` | `Management` | port': false   },      'PRODUCT_MANAGER': {     // User Management     'user.create': false,     'user.assign_role': false, |
| `Permissions` | `Management` | false,     'activity.delete': false,          // Product Management     'product.create': true,     'product.edit': true,    |
| `Permissions` | `Management` | 'audit.export': false   },      'VIEWER': {     // User Management     'user.create': false,     'user.assign_role': false, |
| `Permissions` | `Management` |  true,     'activity.delete': false,          // Product Management     'product.create': false,     'product.edit': false,  |
| `Permissions` | `action` |  }  /**  * Check if a user has permission to perform an action  * @param {string} userEmail - User email address  * @par |
| `Permissions` | `action` | {string} userEmail - User email address  * @param {string} action - Action to check (e.g., 'quote.create', 'order.approve')  |
| `Permissions` | `Action` | userEmail - User email address  * @param {string} action - Action to check (e.g., 'quote.create', 'order.approve')  * @retur |
| `Permissions` | `action` | , false otherwise  */ function checkPermission(userEmail, action) {   const role = getUserRole(userEmail);      if (!role |
| `Permissions` | `action` | r inactive - log denial     logPermissionDenial(userEmail, action, 'User not found or inactive');     return false;   }    |
| `Permissions` | `action` |    if (!permissions) {     logPermissionDenial(userEmail, action, 'Invalid role: ' + role);     return false;   }      c |
| `Permissions` | `action` | return false;   }      const hasPermission = permissions[action] === true;      if (!hasPermission) {     logPermissionD |
| `Permissions` | `action` |   if (!hasPermission) {     logPermissionDenial(userEmail, action, 'Permission denied for role: ' + role);   }      return |
| `Permissions` | `action` | ing  *   * @param {string} userEmail - User who attempted action  * @param {string} action - Action attempted  * @param {s |
| `Permissions` | `action` | } userEmail - User who attempted action  * @param {string} action - Action attempted  * @param {string} reason - Reason for  |
| `Permissions` | `Action` | il - User who attempted action  * @param {string} action - Action attempted  * @param {string} reason - Reason for denial   |
| `Permissions` | `action` | on for denial  */ function logPermissionDenial(userEmail, action, reason) {   try {     const ss = SpreadsheetApp.openById |
| `Permissions` | `action` | stamp,       'PERMISSION_DENIED',       userEmail,       action,       reason,       'SYSTEM'     ];          auditShe |
| `Permissions` | `action` | ations  *   * @param {string} userEmail - User performing action  * @param {string} action - Action performed  * @param {s |
| `Permissions` | `action` | ing} userEmail - User performing action  * @param {string} action - Action performed  * @param {string} details - Additional |
| `Permissions` | `Action` | Email - User performing action  * @param {string} action - Action performed  * @param {string} details - Additional details |
| `Permissions` | `action` | onal details  */ function logPermissionAllowed(userEmail, action, details) {   try {     const ss = SpreadsheetApp.openByI |
| `Permissions` | `action` | tamp,       'PERMISSION_ALLOWED',       userEmail,       action,       details,       'SYSTEM'     ];          auditSh |
| `Permissions` | `action` | only)  * @param {string} adminEmail - Admin performing the action  * @param {string} targetEmail - User to assign role to   |
| `Permissions` | `action` | ; // Update role in column B                  // Log this action to audit         logPermissionAllowed(adminEmail, 'user.as |
| `Permissions` | `action` |  a guard at the start of functions  *   * @param {string} action - Action to validate  * @returns {boolean} - True if user  |
| `Permissions` | `Action` | at the start of functions  *   * @param {string} action - Action to validate  * @returns {boolean} - True if user has permi |
| `Permissions` | `action` | f user has permission  */ function validateUserPermission(action) {   const userEmail = Session.getActiveUser().getEmail(); |
| `Permissions` | `action` | tiveUser().getEmail();   return checkPermission(userEmail, action); }  /**  * Get current user's role  * @returns {strin |

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
| `Code` | `trigger` | ndoff version doc link  *  * Safe: manual run OR time-based trigger (optional).  * Deterministic: uses folder IDs (recommended) |
| `Code` | `Trigger` | .  * (Lightweight, safe)  */ function setupHandoffIndexDailyTrigger() {   removeHandoffIndexTriggers_();   ScriptApp.newTrigger |
| `Code` | `Trigger` | ction setupHandoffIndexDailyTrigger() {   removeHandoffIndexTriggers_();   ScriptApp.newTrigger("updateHandoffIndexLatestLinks" |
| `Code` | `ScriptApp.newTrigger` | offIndexDailyTrigger() {   removeHandoffIndexTriggers_();   ScriptApp.newTrigger("updateHandoffIndexLatestLinks")     .timeBased()     .ever |
| `Code` | `timeBased` |  ScriptApp.newTrigger("updateHandoffIndexLatestLinks")     .timeBased()     .everyDays(1)     .atHour(6)     .create(); }  functi |
| `Code` | `Trigger` |    .atHour(6)     .create(); }  function disableHandoffIndexTriggers() {   removeHandoffIndexTriggers_(); }  function removeHan |
| `Code` | `Trigger` | unction disableHandoffIndexTriggers() {   removeHandoffIndexTriggers_(); }  function removeHandoffIndexTriggers_() {   ScriptAp |
| `Code` | `Trigger` | emoveHandoffIndexTriggers_(); }  function removeHandoffIndexTriggers_() {   ScriptApp.getProjectTriggers().forEach(function (t) |
| `Code` | `Trigger` | ction removeHandoffIndexTriggers_() {   ScriptApp.getProjectTriggers().forEach(function (t) {     if (t.getHandlerFunction() == |
| `Code` | `Trigger` | tion() === "updateHandoffIndexLatestLinks") ScriptApp.deleteTrigger(t);   }); }  /** ===================== Helpers ============ |

## TECH_STACK_AutoCheckpoint
- projectId: `1jH7pB3Vn0bu9K5Xmz7TqEXsh4YDuaazwJGRh4BsWIvq4-DFtwNop-LN2`
- modifiedTime: `2025-12-30T22:50:26.995Z`
- keyword hits: **1**

| file | match | snippet |
|---|---|---|
| `Code` | `trigger` | oint  *  * Manual snapshot of /TECH_STACK/_handoff.md  * No triggers. No sheet dependencies.  ********************************* |

## Untitled project
- projectId: `1qKYlqKWH4Cpjh_NgDfA_G3qE-uX0d6EATZBZ2a-QtFIfVkiIcqTfQjYD`
- modifiedTime: `2026-01-25T06:40:54.849Z`
- keyword hits: *(none)*
