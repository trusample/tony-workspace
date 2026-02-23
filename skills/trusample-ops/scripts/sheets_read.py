#!/usr/bin/env python3
"""Read a Google Sheet and output as markdown table."""
import argparse
from googleapiclient.discovery import build
from google_auth_util import get_creds

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet-id", required=True)
    ap.add_argument("--range", default="A1:Z100")
    ap.add_argument("--credentials", default="/home/mhernandez/clawd/secrets/google/credentials.json")
    ap.add_argument("--token", default="/home/mhernandez/clawd/secrets/google/token.json")
    args = ap.parse_args()

    creds = get_creds(args.credentials, args.token, SCOPES)
    service = build("sheets", "v4", credentials=creds)
    result = service.spreadsheets().values().get(
        spreadsheetId=args.sheet_id, range=args.range
    ).execute()
    rows = result.get("values", [])
    for row in rows:
        print(" | ".join(row))

if __name__ == "__main__":
    main()
