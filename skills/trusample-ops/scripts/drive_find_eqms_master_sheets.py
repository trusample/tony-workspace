#!/usr/bin/env python3
"""Find authoritative TruSample eQMS master sheets across Shared Drives.

Goal
- Locate spreadsheets like:
  - TruSample eQMS MASTER
  - Documents_Index
  - GET IDs SHEET
  - TruSample_eQMS_Master_Implementation_Tracker

Then (later) use Sheets API to list tabs and extract linked folder/script IDs.

This is a stub until OAuth credentials are provided.
"""

from __future__ import annotations

import argparse
from pathlib import Path

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/script.projects.readonly",
]

DEFAULT_NAME_PATTERNS = [
    "eQMS",
    "MASTER",
    "Documents_Index",
    "GET IDs",
    "Implementation",
    "Tracker",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--credentials", default="/home/mhernandez/clawd/secrets/google/credentials.json")
    ap.add_argument("--token", default="/home/mhernandez/clawd/secrets/google/token.json")
    ap.add_argument("--out", default="/home/mhernandez/clawd/notes/EQMS_MASTER_SHEETS_MAP.md")
    ap.add_argument("--patterns", nargs="*", default=DEFAULT_NAME_PATTERNS)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    cred_path = Path(args.credentials)
    if args.dry:
        print("DRY RUN")
        print("credentials:", cred_path)
        print("token:", args.token)
        print("out:", args.out)
        print("scopes:", SCOPES)
        print("patterns:", args.patterns)
        return 0

    if not cred_path.exists():
        raise SystemExit(f"Missing credentials JSON at {cred_path}. Upload OAuth credentials first.")

    from googleapiclient.discovery import build

    from google_auth_util import get_creds

    creds = get_creds(str(cred_path), str(Path(args.token)), SCOPES)
    drive = build("drive", "v3", credentials=creds)
    sheets = build("sheets", "v4", credentials=creds)

    # Broad search for spreadsheets across all drives, filtered by name patterns.
    # Drive query doesn't support regex; we do substring checks client-side.
    q = "mimeType='application/vnd.google-apps.spreadsheet' and trashed=false"

    page_token = None
    files = []
    while True:
        resp = (
            drive.files()
            .list(
                q=q,
                fields="nextPageToken, files(id,name,driveId,owners,modifiedTime,webViewLink)",
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
                corpora="allDrives",
                pageSize=200,
                pageToken=page_token,
            )
            .execute()
        )
        files.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break

    pats = [p.lower() for p in args.patterns if p]
    candidates = []
    for f in files:
        name = (f.get("name") or "").lower()
        if all(p in name for p in ["eqms"]):
            # allow strong eqms match
            candidates.append(f)
            continue
        if any(p in name for p in pats):
            candidates.append(f)

    lines = []
    lines.append("# EQMS Master Sheets Map (auto)\n\n")
    lines.append(f"Candidates found: **{len(candidates)}**\n\n")

    for f in sorted(candidates, key=lambda x: (x.get("name") or "", x.get("id") or "")):
        fid = f["id"]
        name = f.get("name", "(no name)")
        drive_id = f.get("driveId")
        lines.append(f"## {name}\n")
        lines.append(f"- fileId: `{fid}`\n")
        if drive_id:
            lines.append(f"- driveId: `{drive_id}`\n")
        if f.get("webViewLink"):
            lines.append(f"- link: {f['webViewLink']}\n")
        lines.append(f"- modifiedTime: `{f.get('modifiedTime')}`\n")

        try:
            meta = sheets.spreadsheets().get(spreadsheetId=fid, fields="sheets(properties(title,sheetId,index))").execute()
            tabs = [s["properties"]["title"] for s in meta.get("sheets", [])]
            lines.append(f"- tabs ({len(tabs)}): {', '.join('`'+t+'`' for t in tabs[:60])}\n")
            if len(tabs) > 60:
                lines.append("  - *(tabs truncated)*\n")
        except Exception as e:
            lines.append(f"- ERROR reading tabs: `{e}`\n")

        lines.append("\n")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
