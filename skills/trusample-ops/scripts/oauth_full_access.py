#!/usr/bin/env python3
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/script.projects'
]

flow = InstalledAppFlow.from_client_secrets_file(
    '/home/mhernandez/clawd/secrets/google/credentials.json', SCOPES)
print(flow.authorization_url(prompt='consent')[0])
