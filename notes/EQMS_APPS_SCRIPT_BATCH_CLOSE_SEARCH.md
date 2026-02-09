# Apps Script search: batch close / closeout / COA / mgmt actions

## 0AMooSbVaWDeSUk9PVA
- projectId: `1lVWgyYksZ7qxx0nSAavUkcbcyIBZgaBLOhwimb7hI1V22Dy2RGWgJFwx`
- hits: **28**

| file | match | snippet |
|---|---|---|
| `Code` | `DriveApp` | C123XYZ   var parentFolderId = "0AMooSbVaWDeSUk9PVA";    try {     var parent = DriveApp.getFolderById(parentFolderId);   } catch (e) {     Logger.log("ERROR: Could not |
| `Code` | `Batch` | uts = addSubs(folders["02 – Design Outputs"], [     "SOPs",     "Formulations & Batch Calculators",     "Prototype Labels & Packaging",     "Draft IFU",     "Develop |
| `Code` | `Release` | , [     "DMR – Device Master Record",     "Manufacturing Instructions",     "QC Release Specifications",     "Supplier & Component Files"   ]);    addSubs(transfer["DM |
| `Code` | `DriveApp` | turn existing.next();   }   var ss = SpreadsheetApp.create(title);   var file = DriveApp.getFileById(ss.getId());   root.addFile(file);   DriveApp.getRootFolder().remov |
| `Code` | `DriveApp` | (title);   var file = DriveApp.getFileById(ss.getId());   root.addFile(file);   DriveApp.getRootFolder().removeFile(file);   Logger.log("Created new Dashboard: " + ss.g |
| `Code` | `DriveApp` | ssions, templates, etc.)  */ function getOrCreateRootFolder_(name) {   var it = DriveApp.getFoldersByName(name);   if (it.hasNext()) {     return it.next();   }   var f |
| `Code` | `DriveApp` | ersByName(name);   if (it.hasNext()) {     return it.next();   }   var folder = DriveApp.createFolder(name);   Logger.log("Created root folder: " + folder.getName());   |
| `Code` | `DocumentApp` | gger.log("Doc already exists, skipping: " + title);     return;   }   var doc = DocumentApp.create(title);   doc.getBody().setText(bodyText);   doc.saveAndClose();    var  |
| `Code` | `Close` | oc = DocumentApp.create(title);   doc.getBody().setText(bodyText);   doc.saveAndClose();    var file = DriveApp.getFileById(doc.getId());   folder.addFile(file);   D |
| `Code` | `DriveApp` | (title);   doc.getBody().setText(bodyText);   doc.saveAndClose();    var file = DriveApp.getFileById(doc.getId());   folder.addFile(file);   DriveApp.getRootFolder().re |
| `Code` | `DriveApp` | e();    var file = DriveApp.getFileById(doc.getId());   folder.addFile(file);   DriveApp.getRootFolder().removeFile(file);   Logger.log("Created Doc: " + title + " in " |
| `Code` | `DriveApp` | );   setupFn(ss);  // call your initializer to build headers/tabs    var file = DriveApp.getFileById(ss.getId());   folder.addFile(file);   DriveApp.getRootFolder().rem |
| `Code` | `DriveApp` | /tabs    var file = DriveApp.getFileById(ss.getId());   folder.addFile(file);   DriveApp.getRootFolder().removeFile(file);   Logger.log("Created Sheet: " + title + " in |
| `Code` | `Batch` | SOPs");   var formsFolder      = getOrCreateSubFolder_(outputs, "Formulations & Batch Calculators");   var labelsFolder     = getOrCreateSubFolder_(outputs, "Prototy |
| `Code` | `Release` | lder   = getOrCreateSubFolder_(transfer, "Manufacturing Instructions");   var qcReleaseFolder  = getOrCreateSubFolder_(transfer, "QC Release Specifications");   var su |
| `Code` | `Release` | ng Instructions");   var qcReleaseFolder  = getOrCreateSubFolder_(transfer, "QC Release Specifications");   var supplierFolder   = getOrCreateSubFolder_(transfer, "Sup |
| `Code` | `Release` | omponent Specifications\n" +     "4. Manufacturing Instructions\n" +     "5. QC Release Specifications\n" +     "6. Labeling & Packaging Requirements\n"   );    // Man |
| `Code` | `Release` |   "4. In-process Checks\n" +     "5. Documentation and Records\n"   );    // QC Release Specification   createDocTemplateIfMissing_(     qcReleaseFolder,     "QC Relea |
| `Code` | `Release` | rds\n"   );    // QC Release Specification   createDocTemplateIfMissing_(     qcReleaseFolder,     "QC Release Specifications – HbA1c Controls (Template)",     "TruSam |
| `Code` | `Release` | lease Specification   createDocTemplateIfMissing_(     qcReleaseFolder,     "QC Release Specifications – HbA1c Controls (Template)",     "TruSample – QC Release Specif |
| `Code` | `Release` |    "QC Release Specifications – HbA1c Controls (Template)",     "TruSample – QC Release Specifications\n\n" +     "Suggested Table:\n" +     "Parameter \| Spec \| Method |
| `Code` | `Batch` | n" +     "Fields:\n" +     "ECO ID, Linked ECR, Description of Change, Affected Batches, Effective Date, Implementation Plan, Required Verification, Signatures.\n"   |
| `Code` | `Batch` | (1,1,1,header.length).setValues([header]);     sh.setFrozenRows(1);   });    // Batch Record Template   createSheetTemplateIfMissing_(mfgInstrFolder, "Batch Record – |
| `Code` | `Batch` | );    // Batch Record Template   createSheetTemplateIfMissing_(mfgInstrFolder, "Batch Record – HbA1c Controls", function(ss) {     var sh = ss.getActiveSheet();      |
| `Code` | `Batch` | ls", function(ss) {     var sh = ss.getActiveSheet();     var header = [       "Batch ID","Date","Operator","Formula Version","Component","Component Lot","Target Amo |
| `Code` | `Lot` | = [       "Batch ID","Date","Operator","Formula Version","Component","Component Lot","Target Amount","Actual Amount","Checked By",       "In-Process Check","Result |
| `Code` | `Release` | tual Amount","Checked By",       "In-Process Check","Result","Final QC Result","Released By","Release Date","Comments"     ];     sh.getRange(1,1,1,header.length).setV |
| `Code` | `Release` | Checked By",       "In-Process Check","Result","Final QC Result","Released By","Release Date","Comments"     ];     sh.getRange(1,1,1,header.length).setValues([header] |

## CRM SHEET - TruSample
- projectId: `1yDT7YEpAVx3OUnSBjxqTgd4OyS0XKaV0-RX4R-dnOI6vcHG2SFzSVK0e`
- hits: **5**

| file | match | snippet |
|---|---|---|
| `Permissions` | `export` | ll': true,     'report.compliance': true,     'audit.view': true,     'audit.export': true   },      'APPROVER': {     // User Management     'user.create': f |
| `Permissions` | `export` | ': true,     'report.compliance': false,     'audit.view': false,     'audit.export': false   },      'SALES': {     // User Management     'user.create': fal |
| `Permissions` | `export` | : false,     'report.compliance': false,     'audit.view': false,     'audit.export': false   },      'PRODUCT_MANAGER': {     // User Management     'user.cr |
| `Permissions` | `export` | : false,     'report.compliance': false,     'audit.view': false,     'audit.export': false   },      'VIEWER': {     // User Management     'user.create': fa |
| `Permissions` | `export` | ': true,     'report.compliance': false,     'audit.view': false,     'audit.export': false   } };  // ======================================================== |

## Creates all core Docs & Sheets templates
- projectId: `1PYPNY3FjcC03SQqdACKxVXho-47p2Zxvl_82OBYyakrdCIxBmw2IDicP`
- hits: **0**

## PROJECT_HANDOFFS_IndexUpdater
- projectId: `1FL-7FHZ_u6JNiBEYqknlUmadxdg1y9PV5FYtVmqqaTwyNsQ3hdjW4u5J`
- hits: **8**

| file | match | snippet |
|---|---|---|
| `Code` | `ScriptApp.newTrigger` | / function setupHandoffIndexDailyTrigger() {   removeHandoffIndexTriggers_();   ScriptApp.newTrigger("updateHandoffIndexLatestLinks")     .timeBased()     .everyDays(1)     .atHour |
| `Code` | `timeBased` | fIndexTriggers_();   ScriptApp.newTrigger("updateHandoffIndexLatestLinks")     .timeBased()     .everyDays(1)     .atHour(6)     .create(); }  function disableHandoffInd |
| `Code` | `DriveApp` | Name_(folderId, folderName) {   if (folderId && String(folderId).trim()) return DriveApp.getFolderById(String(folderId).trim());   // fallback (less deterministic): fir |
| `Code` | `DriveApp` | d).trim());   // fallback (less deterministic): first folder by name   var it = DriveApp.getFoldersByName(folderName);   if (!it.hasNext()) throw new Error("Folder not  |
| `Code` | `DocumentApp` |  var f = files.next();     if (f.getMimeType() === MimeType.GOOGLE_DOCS) return DocumentApp.openById(f.getId());   }   var doc = DocumentApp.create(name);   var docFile =  |
| `Code` | `DocumentApp` | = MimeType.GOOGLE_DOCS) return DocumentApp.openById(f.getId());   }   var doc = DocumentApp.create(name);   var docFile = DriveApp.getFileById(doc.getId());   folder.addFi |
| `Code` | `DriveApp` | .openById(f.getId());   }   var doc = DocumentApp.create(name);   var docFile = DriveApp.getFileById(doc.getId());   folder.addFile(docFile);   try { DriveApp.getRootFo |
| `Code` | `DriveApp` | docFile = DriveApp.getFileById(doc.getId());   folder.addFile(docFile);   try { DriveApp.getRootFolder().removeFile(docFile); } catch (e) {}   return doc; }  function g |

## TECH_STACK_AutoCheckpoint
- projectId: `1jH7pB3Vn0bu9K5Xmz7TqEXsh4YDuaazwJGRh4BsWIvq4-DFtwNop-LN2`
- hits: **5**

| file | match | snippet |
|---|---|---|
| `Code` | `DriveApp` | e(), "yyyyMMdd_HHmm");   var name = "_handoff_v" + stamp + ".md";    var copy = DriveApp.getFileById(handoff.getId()).makeCopy(name, versions);    logCheckpoint_(handof |
| `Code` | `DriveApp` | --- helpers ---------- */  function getOrCreateFolderByName_(name) {   var it = DriveApp.getFoldersByName(name);   return it.hasNext() ? it.next() : DriveApp.createFold |
| `Code` | `DriveApp` |   var it = DriveApp.getFoldersByName(name);   return it.hasNext() ? it.next() : DriveApp.createFolder(name); }  function getOrCreateSubfolder_(parent, name) {   var it  |
| `Code` | `DocumentApp` | me(name);   if (!files.hasNext()) return null;   var f = files.next();   return DocumentApp.openById(f.getId()); }  function logCheckpoint_(handoffUrl, versionUrl) {   var |
| `Code` | `DriveApp` |   versionUrl   ]); }  function getOrCreateLogSheet_() {   var ss;   var files = DriveApp.getFilesByName(TECH_STACK_CONFIG.LOG_SHEET_NAME);   if (files.hasNext()) {      |

## Untitled project
- projectId: `1qKYlqKWH4Cpjh_NgDfA_G3qE-uX0d6EATZBZ2a-QtFIfVkiIcqTfQjYD`
- hits: **0**
