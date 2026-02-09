# TruSample eQMS — Overview (Drive Sync)

Source: `gdrive1:TruSample_eQMS/TruSample_eQMS`  
Local: `/home/mhernandez/clawd/drive_sync/gdrive1/trusample_eqms/TruSample_eQMS`

## What’s currently synced
High-level directories present locally:
- `Audit_Packs/`
- `PROJECT_HANDOFFS/`
- `TECH_STACK/`
- `Versions/`
- `_state/`
- `_handoff.md.docx` (root handoff)

### Audit_Packs
Found:
- `AuditPack_20251230_1551/`
  - `MANIFEST.txt`
  - `_handoff_v20251230_1551.txt`
  - `_handoff_v20251230_1551.md.docx`
- `AuditPack_20251230_1732/`
  - `MANIFEST.txt`
  - `_handoff_v20251230_1732.txt`
  - `_handoff_v20251230_1732.md.docx`

### TECH_STACK
Found:
- `_handoff.md.docx`
- `Versions/`
  - `_handoff_v20251230_1750.md.docx`
  - `_handoff_v20251230_1756.md.docx`
  - `_handoff_v20251230_1757.md.docx`

### PROJECT_HANDOFFS
Found:
- `PROJECT HANDOFF INDEX.docx`
- `_handoff_index.md.docx`

### Versions
Found:
- `_handoff_v20251230_1551.md.docx`
- `_handoff_v20251230_1732.md.docx`

### _state
Found state pack artifacts:
- `STATE_PACK_REL-20251231-0127.json`
- `STATE_PACK_REL-20251231-0133.json`
- `STATE_PACK_REL-20251231-0142.json`
- `STATE_PACK_REL-20251231-0146.json`
- plus `STATE_PACK_REL-2025-12-001.json.docx`

## What looks incomplete / suspicious
Drive shows a directory named:
- `00_Master_Spreadsheet01_Templates/`

…but when listed via API it currently returns **0 items** (empty). That can mean:
- it’s genuinely empty, or
- it contains only Google-native items that aren’t being exported under our current settings, or
- it’s a shortcut container with no resolved targets.

If you expect templates/spreadsheets to be there, we’ll need to locate the real folder(s) or IDs.

## Next actions (recommended)
1) You tell me the intended purpose of EQMS here (FDA/CLIA/ISO13485-ish vs “internal quality system”).
2) Identify the core modules you want implemented first:
   - Document Control
   - Training
   - Deviations / Nonconformance
   - CAPA
   - Change Control
   - Risk Management
   - Supplier Management
   - Audit Management
3) Pull `00_EXECUTIVE_CONTROL` next (usually contains the “why/what” and decision log).
