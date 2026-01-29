#!/usr/bin/env python3
"""Generate a next-events digest from Google Calendar (read-only).

Outputs:
- notes/CALENDAR_NEXT_7_DAYS.md

Requires token with calendar.readonly scope.

Run:
  cd /home/mhernandez/clawd
  . .venv/bin/activate
  python skills/trusample-ops/scripts/calendar_upcoming.py
"""

from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

from googleapiclient.discovery import build

from google_auth_util import get_creds

SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
]


def _iso(dtobj: dt.datetime) -> str:
    return dtobj.replace(microsecond=0).isoformat() + "Z"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--credentials", default="/home/mhernandez/clawd/secrets/google/credentials.json")
    ap.add_argument("--token", default="/home/mhernandez/clawd/secrets/google/token.json")
    ap.add_argument("--out", default="/home/mhernandez/clawd/notes/CALENDAR_NEXT_7_DAYS.md")
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--max", type=int, default=50)
    ap.add_argument(
        "--calendarId",
        default="primary",
        help="Calendar ID (default: primary)",
    )
    args = ap.parse_args()

    creds = get_creds(args.credentials, args.token, SCOPES)
    cal = build("calendar", "v3", credentials=creds)

    now = dt.datetime.utcnow()
    end = now + dt.timedelta(days=args.days)

    events = (
        cal.events()
        .list(
            calendarId=args.calendarId,
            timeMin=_iso(now),
            timeMax=_iso(end),
            maxResults=args.max,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
        .get("items", [])
    )

    lines: list[str] = []
    lines.append("# Calendar next events (auto)\n\n")
    lines.append(f"Window (UTC): `{_iso(now)}` → `{_iso(end)}`\n\n")
    lines.append(f"Events: **{len(events)}** (showing up to {args.max})\n\n")

    for e in events:
        start = e.get("start", {}).get("dateTime") or e.get("start", {}).get("date")
        endt = e.get("end", {}).get("dateTime") or e.get("end", {}).get("date")
        summary = e.get("summary") or "(no title)"
        loc = e.get("location")
        lines.append(f"## {summary}\n")
        lines.append(f"- When: {start} → {endt}\n")
        if loc:
            lines.append(f"- Location: {loc}\n")
        if e.get("htmlLink"):
            lines.append(f"- Link: {e['htmlLink']}\n")
        lines.append("\n")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(lines), encoding="utf-8")
    print(f"Wrote: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
