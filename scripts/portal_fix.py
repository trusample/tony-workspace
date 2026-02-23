#!/usr/bin/env python3
"""
portal_fix.py - Fix and redeploy TruSample CRM portal
Usage: python3 portal_fix.py
"""
import json, sys
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

TOKEN = '/home/mhernandez/clawd/secrets/google/token.json'
SCRIPT_ID = '1VK63CyENJLgOcinUXSUpUx9fZEx2s1-nq9U4Y6RtjG5uK3LrHuMQhw_r'
PORTAL_URL = 'https://script.google.com/a/macros/cellabios.com/s/AKfycbyaC0uYxEelIByiVwwDaQcM378OsqNOuNu-yCwvJQW4yLlQMsfu5QvzdeZL2ywSph9Ozw/exec'

with open(TOKEN) as f: d=json.load(f)
creds = Credentials(token=d['token'],refresh_token=d['refresh_token'],token_uri=d['token_uri'],client_id=d['client_id'],client_secret=d['client_secret'])
creds.refresh(Request())
svc = build('script','v1',credentials=creds)

current = svc.projects().getContent(scriptId=SCRIPT_ID).execute()
files = current['files']

for f in files:
    if f['name'] == 'PortalHTML':
        src = f['source']
        # Fix endpoint
        src = src.replace("<?= ScriptApp.getService().getUrl() ?>", PORTAL_URL)
        src = src.replace("'<?= ScriptApp.getService().getUrl() ?>'", f"'{PORTAL_URL}'")
        f['source'] = src
        print('PortalHTML endpoint fixed')
    if f['name'] == 'WebPortal':
        f['source'] = '// WebPortal - DISABLED'
        print('WebPortal disabled')

result = svc.projects().updateContent(scriptId=SCRIPT_ID, body={'files':files}).execute()
print('Files updated:', [f['name'] for f in result['files']])
print('Now redeploy via UI: Deploy -> Manage deployments -> New version')
