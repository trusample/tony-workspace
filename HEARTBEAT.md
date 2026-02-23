# HEARTBEAT.md

## 🚨 ACTIVE MISSION: CRM Migration
Status: NOT STARTED
Priority: HIGH

The CRM portal is broken because it lives under the wrong Google account (cellabios.com).
Maykel needs a working CRM under trusample.bio.

### Your job:
1. Run ~/clawd/scripts/crm_migrate.py (create it if it doesn't exist)
2. Export data from legacy CRM sheet: 1NyYihFTchiur_Nrj5Vz0LSxw1PP4aY6ttctn4G2cT4E
   - Read tabs: Accounts, Contacts, Quotes, Orders, Products
   - Save to ~/clawd/crm_export/{tab}.json
3. Create new sheet under trusample.bio titled "TruSample CRM Master"
4. Import data into new sheet
5. Create bound Apps Script with clean portal (google.script.run pattern, NO scriptlets)
6. Telegram Maykel the new script URL so he can authorize and deploy via browser

### Reference:
- Google auth: see TOOLS.md
- Portal HTML pattern: use google.script.run NOT fetch() for server calls
- NO scriptlets (<?= ?>) — they don't work with createHtmlOutputFromFile

### Done when:
- New sheet exists under trusample.bio
- Data imported
- Script written and pushed
- Maykel notified via Telegram

Update this file with progress as you go.
