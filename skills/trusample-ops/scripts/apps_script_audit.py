#!/usr/bin/env python3
"""Audit Apps Script projects for extracted function names.

Usage:
  python3 apps_script_audit.py

This script will:
1) Authenticate using google_auth_util.
2) List all Apps Script projects via Drive API.
3) Fetch source code using getContent.
4) Extract every function's name and save to a Markdown file.
"""

from __future__ import annotations

import json
from pathlib import Path
from googleapiclient.discovery import build
from google_auth_util import get_creds

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/script.projects.readonly",
]

def main() -> int:
    creds = get_creds(
        '/home/mhernandez/clawd/secrets/google/credentials.json',
        '/home/mhernandez/clawd/secrets/google/token.json',
        SCOPES
    )

    # Build the Drive API service
    drive_service = build('drive', 'v3', credentials=creds)
    script_service = build('script', 'v1', credentials=creds)

    # Find Apps Script projects across all drives
    q = "mimeType='application/vnd.google-apps.script' and trashed=false"
    projects = []
    page_token = None
    while True:
        response = drive_service.files().list(
            q=q,
            fields="nextPageToken, files(id,name)",
            supportsAllDrives=True,
            includeItemsFromAllDrives=True,
            pageSize=100,
            pageToken=page_token
        ).execute()

        projects.extend(response.get('files', []))
        page_token = response.get('nextPageToken')
        if not page_token:
            break

    functions_list = []

    for project in projects:
        project_id = project['id']
        project_name = project.get('name', 'Unnamed Project')

        # Fetch the content of each project
        content = script_service.projects().getContent(scriptId=project_id).execute()
        files = content.get('files', [])

        for file in files:
            source = file.get('source', '')
            # Extract function names
            for line in source.split('\n'):
                if line.startswith('function '):
                    functions_list.append(line.strip())

    # Save to notes/CRM_FUNCTIONS.md
    output_path = Path('/home/mhernandez/clawd/notes/CRM_FUNCTIONS.md')
    output_path.write_text('\n'.join(functions_list), encoding='utf-8')
    print(f'Functions extracted to: {output_path}')  

if __name__ == '__main__':
    # Run the Apps Script APIs commands
    raise SystemExit(main())