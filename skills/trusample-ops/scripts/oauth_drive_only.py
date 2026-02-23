#!/usr/bin/env python3
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive']

flow = InstalledAppFlow.from_client_secrets_file(
    '/home/mhernandez/clawd/secrets/google/credentials.json', 
    SCOPES,
    redirect_uri='http://localhost'
)

auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
print(auth_url)
