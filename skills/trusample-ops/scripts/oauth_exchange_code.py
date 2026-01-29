#!/usr/bin/env python3
"""Exchange an OAuth authorization code for a token and write token.json.

Usage:
  cd /home/mhernandez/clawd
  . .venv/bin/activate
  python skills/trusample-ops/scripts/oauth_exchange_code.py \
    --scopes drive,sheets,script,gmail,calendar \
    --code "4/0ASc..."

Writes:
- /home/mhernandez/clawd/secrets/google/token.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPE_MAP = {
    "drive": "https://www.googleapis.com/auth/drive.readonly",
    "sheets": "https://www.googleapis.com/auth/spreadsheets.readonly",
    "script": "https://www.googleapis.com/auth/script.projects.readonly",
    "gmail": "https://www.googleapis.com/auth/gmail.readonly",
    "calendar": "https://www.googleapis.com/auth/calendar.readonly",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--credentials", default="/home/mhernandez/clawd/secrets/google/credentials.json")
    ap.add_argument("--token", default="/home/mhernandez/clawd/secrets/google/token.json")
    ap.add_argument(
        "--scopes",
        default="drive,sheets,script",
        help="Comma-separated keys from: " + ",".join(SCOPE_MAP.keys()),
    )
    ap.add_argument("--code", required=True)
    args = ap.parse_args()

    scopes = [SCOPE_MAP[k.strip()] for k in args.scopes.split(",") if k.strip()]

    cred_path = Path(args.credentials)
    cfg = json.loads(cred_path.read_text())
    redirect_uris = (cfg.get("installed") or {}).get("redirect_uris") or []

    flow = InstalledAppFlow.from_client_secrets_file(str(cred_path), scopes=scopes)
    flow.redirect_uri = redirect_uris[0] if redirect_uris else "http://localhost"

    flow.fetch_token(code=args.code.strip())
    creds = flow.credentials

    tok_path = Path(args.token)
    tok_path.parent.mkdir(parents=True, exist_ok=True)
    tok_path.write_text(creds.to_json())
    print(f"Wrote: {tok_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
