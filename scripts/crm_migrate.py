#!/usr/bin/env python3
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

with open('/home/mhernandez/clawd/secrets/google/token.json') as f:
    d = json.load(f)
creds = Credentials(
    token=d['token'],
    refresh_token=d['refresh_token'],
    token_uri=d['token_uri'],
    client_id=d['client_id'],
    client_secret=d['client_secret'],
)
creds.refresh(Request())

sheets = build('sheets', 'v4', credentials=creds)

LEGACY = '1NyYihFTchiur_Nrj5Vz0LSxw1PP4aY6ttctn4G2cT4E'
NEW = '1tqloBarpMEF-wM7MRf9rMs5vdy6x0ha_Jb8pH4OqFJ0'
TABS = ['Accounts', 'Contacts', 'Quotes', 'Orders', 'Products']

for tab in TABS:
    try:
        result = sheets.spreadsheets().values().get(spreadsheetId=LEGACY, range=tab).execute()
        values = result.get('values', [])
        if values:
            sheets.spreadsheets().values().update(
                spreadsheetId=NEW,
                range=f'{tab}!A1',
                valueInputOption='RAW',
                body={'values': values},
            ).execute()
            print(f'{tab}: {len(values)-1} rows copied')
        else:
            print(f'{tab}: empty')
    except Exception as e:
        print(f'{tab}: ERROR - {e}')

print('Migration complete')