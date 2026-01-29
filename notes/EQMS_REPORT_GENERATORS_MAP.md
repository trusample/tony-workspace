# EQMS report generators map (auto)

Goal: locate where 'Batch Close' and/or 'COA' are generated (menu items, PDF/Doc exports, Drive outputs).

## 0AMooSbVaWDeSUk9PVA
- projectId: `1lVWgyYksZ7qxx0nSAavUkcbcyIBZgaBLOhwimb7hI1V22Dy2RGWgJFwx`
- modifiedTime: `2025-12-09T05:11:06.739Z`
- candidate generator files: **1**

### Code (score 3)
- signals: doc_create, batch, release
- batch: ]);    // 02 – Design Outputs   var outputs = addSubs(folders["02 – Design Outputs"], [     "SOPs",     "Formulations & Batch Calculators",     "Prototype Labels & Packaging",     "Draft IFU",     "Development Reports"   ]);    addSubs(outputs["SOPs"], [     "SOP-001 – Hb0 Stock Prep",     "SOP-002 – HbA-high Prep",     "SOP-003 – Formulation 
- release: r = addSubs(folders["07 – Design Transfer"], [     "DMR – Device Master Record",     "Manufacturing Instructions",     "QC Release Specifications",     "Supplier & Component Files"   ]);    addSubs(transfer["DMR – Device Master Record"], [     "Formulation Master",     "Component Specifications",     "Filling & Packaging Instructions",     "Labelin
- doc_create: (title);   if (files.hasNext()) {     Logger.log("Doc already exists, skipping: " + title);     return;   }   var doc = DocumentApp.create(title);   doc.getBody().setText(bodyText);   doc.saveAndClose();    var file = DriveApp.getFileById(doc.getId());   folder.addFile(file);   DriveApp.getRootFolder().removeFile(file);   Logger.log("Created Doc: " + title 

## CRM SHEET - TruSample
- projectId: `1yDT7YEpAVx3OUnSBjxqTgd4OyS0XKaV0-RX4R-dnOI6vcHG2SFzSVK0e`
- modifiedTime: `2026-01-24T06:57:57.464Z`
- candidate generator files: *(none)*

## Creates all core Docs & Sheets templates
- projectId: `1PYPNY3FjcC03SQqdACKxVXho-47p2Zxvl_82OBYyakrdCIxBmw2IDicP`
- modifiedTime: `2025-12-09T05:10:27.946Z`
- candidate generator files: *(none)*

## PROJECT_HANDOFFS_IndexUpdater
- projectId: `1FL-7FHZ_u6JNiBEYqknlUmadxdg1y9PV5FYtVmqqaTwyNsQ3hdjW4u5J`
- modifiedTime: `2025-12-31T03:21:54.050Z`
- candidate generator files: **1**

### Code (score 1)
- signals: doc_create
- doc_create: e(name);   while (files.hasNext()) {     var f = files.next();     if (f.getMimeType() === MimeType.GOOGLE_DOCS) return DocumentApp.openById(f.getId());   }   var doc = DocumentApp.create(name);   var docFile = DriveApp.getFileById(doc.getId());   folder.addFile(docFile);   try { DriveApp.getRootFolder().removeFile(docFile); } catch (e) {}   return doc; }  fu

## TECH_STACK_AutoCheckpoint
- projectId: `1jH7pB3Vn0bu9K5Xmz7TqEXsh4YDuaazwJGRh4BsWIvq4-DFtwNop-LN2`
- modifiedTime: `2025-12-30T22:50:26.995Z`
- candidate generator files: **1**

### Code (score 2)
- signals: doc_create, file_create
- doc_create: ame) {   var files = folder.getFilesByName(name);   if (!files.hasNext()) return null;   var f = files.next();   return DocumentApp.openById(f.getId()); }  function logCheckpoint_(handoffUrl, versionUrl) {   var ss = getOrCreateLogSheet_();   ss.appendRow([     new Date(),     Session.getActiveUser().getEmail() \|\| "unknown",     handoffUrl,     versionUrl   ]
- file_create: one(), "yyyyMMdd_HHmm");   var name = "_handoff_v" + stamp + ".md";    var copy = DriveApp.getFileById(handoff.getId()).makeCopy(name, versions);    logCheckpoint_(handoff.getUrl(), copy.getUrl());    return {     handoff: handoff.getUrl(),     version: copy.getUrl()   }; }  /* ---------- helpers ---------- */  function getOrCreateFolderByName_(na

## Untitled project
- projectId: `1qKYlqKWH4Cpjh_NgDfA_G3qE-uX0d6EATZBZ2a-QtFIfVkiIcqTfQjYD`
- modifiedTime: `2026-01-25T06:40:54.849Z`
- candidate generator files: *(none)*

