#!/usr/bin/env python3
from google_auth_oauthlib.flow import InstalledAppFlow
import json

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/script.projects'
]

flow = InstalledAppFlow.from_client_secrets_file(
    '/home/mhernandez/clawd/secrets/google/credentials.json',
    SCOPES,
    redirect_uri='http://localhost'
)

creds = flow.run_local_server(port=8080)

# Save token
token_data = {
    'token': creds.token,
    'refresh_token': creds.refresh_token,
    'token_uri': creds.token_uri,
    'client_id': creds.client_id,
    'client_secret': creds.client_secret,
    'scopes': creds.scopes
}

with open('/home/mhernandez/clawd/secrets/google/token.json', 'w') as f:
    json.dump(token_data, f, indent=2)

print("Token saved successfully!")
