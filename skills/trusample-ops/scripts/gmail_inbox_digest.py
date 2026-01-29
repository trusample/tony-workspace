#!/usr/bin/env python3
"""Generate a concise Gmail inbox digest (read-only).

Outputs:
- notes/GMAIL_INBOX_DIGEST.md

Requires:
- /home/mhernandez/clawd/secrets/google/credentials.json
- /home/mhernandez/clawd/secrets/google/token.json (with gmail.readonly scope)

Run:
  cd /home/mhernandez/clawd
  . .venv/bin/activate
  python skills/trusample-ops/scripts/gmail_inbox_digest.py
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
from pathlib import Path
from typing import Any

from googleapiclient.discovery import build

from google_auth_util import get_creds

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
]


def _get_header(msg: dict[str, Any], name: str) -> str | None:
    for h in msg.get("payload", {}).get("headers", []) or []:
        if h.get("name", "").lower() == name.lower():
            return h.get("value")
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--credentials", default="/home/mhernandez/clawd/secrets/google/credentials.json")
    ap.add_argument("--token", default="/home/mhernandez/clawd/secrets/google/token.json")
    ap.add_argument("--out", default="/home/mhernandez/clawd/notes/GMAIL_INBOX_DIGEST.md")
    ap.add_argument("--max", type=int, default=25)
    ap.add_argument(
        "--query",
        default="in:inbox is:unread",
        help="Gmail search query (default: unread inbox)",
    )
    args = ap.parse_args()

    creds = get_creds(args.credentials, args.token, SCOPES)
    gmail = build("gmail", "v1", credentials=creds)

    # list messages
    resp = (
        gmail.users()
        .messages()
        .list(userId="me", q=args.query, maxResults=args.max)
        .execute()
    )
    msgs = resp.get("messages", []) or []

    lines: list[str] = []
    lines.append("# Gmail inbox digest (auto)\n\n")
    lines.append(f"Query: `{args.query}`\n\n")
    lines.append(f"Unread found: **{len(msgs)}** (showing up to {args.max})\n\n")

    for m in msgs:
        mid = m["id"]
        full = (
            gmail.users()
            .messages()
            .get(userId="me", id=mid, format="metadata", metadataHeaders=["From", "To", "Subject", "Date"])
            .execute()
        )
        subject = _get_header(full, "Subject") or "(no subject)"
        from_ = _get_header(full, "From") or "(unknown)"
        date = _get_header(full, "Date") or ""
        snippet = (full.get("snippet") or "").replace("\n", " ")

        lines.append(f"## {subject}\n")
        lines.append(f"- From: {from_}\n")
        if date:
            lines.append(f"- Date: {date}\n")
        lines.append(f"- Message ID: `{mid}`\n")
        if snippet:
            lines.append(f"- Snippet: {snippet}\n")
        lines.append("\n")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
