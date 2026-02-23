# TOOLS.md - Local Notes (Environment-Specific)

## Preferred messaging
- Default channel: **Telegram**

## Server / runtime
- Workspace: `/home/mhernandez/clawd`
- Host: `hernandez-server` (Ubuntu 24.04)
- Python venv: `~/.venv` or `.venv` in clawd dir

## Google Auth Pattern — ALWAYS USE THIS
```python
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

with open('/home/mhernandez/clawd/secrets/google/token.json') as f: d=json.load(f)
creds = Credentials(token=d['token'],refresh_token=d['refresh_token'],token_uri=d['token_uri'],client_id=d['client_id'],client_secret=d['client_secret'])
creds.refresh(Request())
```
Never use google_auth_util.get_creds() for Apps Script API calls.

## Google Account Situation — CRITICAL
- Primary account: m.hernandez@trusample.bio (preferred going forward)
- Legacy account: m.hernandez@cellabios.com (owns old sheets/scripts — avoid)
- Token at secrets/google/token.json = trusample.bio account
- ALL new sheets and scripts must be created under trusample.bio

## Known Spreadsheets
- eQMS Master (trusample.bio): 1XqMvZjw_5pFEJJXq9SyK6kYQhTzA2IxCz0kc8kOWlQg
- CRM Sheet (cellabios - LEGACY): 1NyYihFTchiur_Nrj5Vz0LSxw1PP4aY6ttctn4G2cT4E
- CRM Products (cellabios - LEGACY): find via Drive API
- CRM Inventory (cellabios - LEGACY): find via Drive API

## CRM Apps Script Projects
- CORRECT project (cellabios, BROKEN): 1VK63CyENJLgOcinUXSUpUx9fZEx2s1-nq9U4Y6RtjG5uK3LrHuMQhw_r
- WRONG project (ignore): 1yDT7YEpAVx3OUnSBjxqTgd4OyS0XKaV0-RX4R-dnOI6vcHG2SFzSVK0e
- Portal URL (broken, cellabios domain restricted): https://script.google.com/macros/s/AKfycbyaC0uYxEelIByiVwwDaQcM378OsqNOuNu-yCwvJQW4yLlQMsfu5QvzdeZL2ywSph9Ozw/exec

## CRM Migration Mission (PENDING)
The CRM is broken because it lives under cellabios.com account.
Goal: Migrate everything to trusample.bio and rebuild clean.

Steps Tony should execute:
1. Read all tabs from legacy CRM sheet (cellabios) and export to JSON files in ~/clawd/crm_export/
2. Create new Google Sheet under trusample.bio account titled "TruSample CRM Master"
   - Tabs: Accounts, Contacts, Quotes, Orders, Products, Inventory
3. Import exported data into new sheet
4. Create new Apps Script project bound to new sheet (via Drive API)
5. Write doGet/doPost + portal functions using google.script.run pattern
6. Push clean PortalHTML (no scriptlets - hardcode URL after first deploy)
7. Notify Maykel via Telegram with new deployment URL to authorize in browser

Scripts location: /home/mhernandez/clawd/scripts/
- send_email.py — send email
- portal_fix.py — fix portal HTML endpoint

## Email
- Send script: ~/clawd/scripts/send_email.py

## Devices
- Main PC: cellabios pc
- Server (where Tony runs): hernandez-server
