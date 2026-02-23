#!/usr/bin/env python3
"""Quick CRM queries for Tony to use"""
import sys
sys.path.append('/home/mhernandez/clawd/skills/trusample-ops/scripts')
from google_auth_util import get_creds
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1NyYihFTchiur_Nrj5Vz0LSxw1PP4aY6ttctn4G2cT4E'

creds = get_creds('/home/mhernandez/clawd/secrets/google/credentials.json', 
                  '/home/mhernandez/clawd/secrets/google/token.json', SCOPES)
service = build('sheets', 'v4', credentials=creds)

def count_rows(sheet_name):
    try:
        result = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID, range=f'{sheet_name}!A:A').execute()
        rows = result.get('values', [])
        return len(rows) - 1  # Subtract header
    except Exception as e:
        return f"Error: {e}"

print("=== TruSample CRM Status ===")
print(f"Quotes: {count_rows('Quotes')}")
print(f"Orders: {count_rows('Orders')}")
print(f"Invoices: {count_rows('Invoices')}")
print(f"Accounts: {count_rows('Accounts')}")
print(f"Contacts: {count_rows('Contacts')}")
print(f"Products: {count_rows('Products')}")
