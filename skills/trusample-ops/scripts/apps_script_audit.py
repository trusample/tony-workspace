#!/usr/bin/env python3
"""Audit Apps Script projects for TruSample eQMS automation evidence.

Usage (after credentials are installed):
  python3 apps_script_audit.py --out /home/mhernandez/clawd/notes/EQMS_APPS_SCRIPT_EVIDENCE.md

This script is designed to:
1) Discover Apps Script projects in Shared Drives (Drive API)
2) Fetch project source (Apps Script API projects.getContent)
3) Grep for key automation signals:
   - reminders / triggers
   - management actions
   - batch close report generation
   - COA generation

NOTE: This is intentionally minimal until OAuth credentials are provided.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable

SCOPES = [
    "https://www.googleapis.com/auth/drive.readonly",
    "https://www.googleapis.com/auth/script.projects.readonly",
]

DEFAULT_KEYWORDS = [
    "reminder",
    "trigger",
    "ScriptApp.newTrigger",
    "timeBased",
    "MGMT",
    "management",
    "action",
    "BatchClose",
    "batch close",
    "close report",
    "COA",
    "Certificate of Analysis",
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--credentials", default="/home/mhernandez/clawd/secrets/google/credentials.json")
    ap.add_argument("--token", default="/home/mhernandez/clawd/secrets/google/token.json")
    ap.add_argument("--out", default="/home/mhernandez/clawd/notes/EQMS_APPS_SCRIPT_EVIDENCE.md")
    ap.add_argument("--keywords", nargs="*", default=DEFAULT_KEYWORDS)
    ap.add_argument("--dry", action="store_true", help="Do not call APIs; only print planned actions")
    args = ap.parse_args()

    cred_path = Path(args.credentials)
    tok_path = Path(args.token)
    out_path = Path(args.out)

    if args.dry:
        print("DRY RUN")
        print("credentials:", cred_path)
        print("token:", tok_path)
        print("out:", out_path)
        print("scopes:", SCOPES)
        print("keywords:", args.keywords)
        return 0

    if not cred_path.exists():
        raise SystemExit(
            f"Missing credentials JSON at {cred_path}. Upload OAuth credentials first.\n"
            "See references/google_apis_setup.md"
        )

    from googleapiclient.discovery import build

    from google_auth_util import get_creds

    creds = get_creds(str(cred_path), str(tok_path), SCOPES)

    drive = build("drive", "v3", credentials=creds)
    script = build("script", "v1", credentials=creds)

    # Find Apps Script projects across all drives
    q = "mimeType='application/vnd.google-apps.script' and trashed=false"
    page_token = None
    projects = []
    while True:
        resp = (
            drive.files()
            .list(
                q=q,
                fields="nextPageToken, files(id,name,driveId,owners,modifiedTime)",
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
                corpora="allDrives",
                pageSize=200,
                pageToken=page_token,
            )
            .execute()
        )
        projects.extend(resp.get("files", []))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break

    keywords = [k for k in args.keywords if k]
    key_re = re.compile("|".join(re.escape(k) for k in keywords), re.IGNORECASE) if keywords else None

    lines = []
    lines.append("# EQMS Apps Script Evidence (auto)\n")
    lines.append("This report is generated from Apps Script API project source (read-only).\n")
    lines.append(f"Projects found: **{len(projects)}**\n")

    for p in sorted(projects, key=lambda x: (x.get("name") or "", x.get("id") or "")):
        pid = p["id"]
        name = p.get("name", "(no name)")
        drive_id = p.get("driveId")
        lines.append(f"\n## {name}\n")
        lines.append(f"- projectId: `{pid}`\n")
        if drive_id:
            lines.append(f"- driveId: `{drive_id}`\n")
        lines.append(f"- modifiedTime: `{p.get('modifiedTime')}`\n")

        try:
            content = script.projects().getContent(scriptId=pid).execute()
        except Exception as e:
            lines.append(f"- ERROR fetching content: `{e}`\n")
            continue

        files = content.get("files", [])
        hits = []
        for f in files:
            fname = f.get("name", "(unnamed)")
            src = f.get("source", "") or ""
            if not src or not key_re:
                continue
            for m in key_re.finditer(src):
                # grab a short surrounding snippet
                start = max(m.start() - 60, 0)
                end = min(m.end() + 60, len(src))
                snippet = src[start:end].replace("\n", " ")
                hits.append((fname, m.group(0), snippet))

        if not hits:
            lines.append("- keyword hits: *(none)*\n")
        else:
            lines.append(f"- keyword hits: **{len(hits)}**\n")
            lines.append("\n| file | match | snippet |\n|---|---|---|\n")
            for fname, match, snippet in hits[:80]:
                safe = snippet.replace("|", "\\|")
                lines.append(f"| `{fname}` | `{match}` | {safe} |\n")
            if len(hits) > 80:
                lines.append(f"\n*(truncated; {len(hits)} total hits)*\n")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
