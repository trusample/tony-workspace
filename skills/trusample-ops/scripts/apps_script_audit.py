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

    # TODO: implement OAuth + Drive API list + Apps Script API getContent
    # Keep deterministic: emit markdown with project list + grep hits.
    raise SystemExit(
        "Not implemented yet. Next step: install google-api-python-client libs and implement OAuth + API calls."
    )


if __name__ == "__main__":
    raise SystemExit(main())
