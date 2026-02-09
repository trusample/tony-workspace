#!/usr/bin/env python3
import sys
sys.path.append('/home/mhernandez/clawd/skills/trusample-ops/scripts')
from google_auth_util import get_creds
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = '1NyYihFTchiur_Nrj5Vz0LSxw1PP4aY6ttctn4G2cT4E'

creds = get_creds(
    '/home/mhernandez/clawd/secrets/google/credentials.json',
    '/home/mhernandez/clawd/secrets/google/token.json',
    SCOPES
)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Get all sheet names
metadata = sheet.get(spreadsheetId=SPREADSHEET_ID).execute()
sheets = metadata.get('sheets', [])

print("=== TruSample CRM Tabs ===")
for s in sheets:
    print(f"- {s['properties']['title']}")
