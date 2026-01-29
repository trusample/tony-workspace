#!/usr/bin/env python3
"""Shared OAuth helper for TruSample Ops scripts.

Creates/loads an OAuth token at /home/mhernandez/clawd/secrets/google/token.json
using the credentials at /home/mhernandez/clawd/secrets/google/credentials.json.

Auth flow is interactive (paste code). Intended for server/CLI use.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Sequence

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def get_creds(credentials_path: str, token_path: str, scopes: Sequence[str]) -> Credentials:
    cred_path = Path(credentials_path)
    tok_path = Path(token_path)
    tok_path.parent.mkdir(parents=True, exist_ok=True)

    creds: Credentials | None = None
    if tok_path.exists():
        creds = Credentials.from_authorized_user_file(str(tok_path), scopes=scopes)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        tok_path.write_text(creds.to_json())
        return creds

    if not cred_path.exists():
        raise FileNotFoundError(f"Missing credentials JSON at {cred_path}")

    flow = InstalledAppFlow.from_client_secrets_file(str(cred_path), scopes=scopes)

    # Headless/server-friendly flow using an installed-app redirect URI.
    # We set redirect_uri explicitly so Google doesn't reject the request.
    try:
        cfg = json.loads(cred_path.read_text())
        redirect_uris = (cfg.get("installed") or {}).get("redirect_uris") or []
        flow.redirect_uri = redirect_uris[0] if redirect_uris else "http://localhost"
    except Exception:
        flow.redirect_uri = "http://localhost"

    auth_url, _ = flow.authorization_url(prompt="consent", access_type="offline")
    print("\nOPEN THIS URL IN YOUR BROWSER:\n")
    print(auth_url)
    print(
        "\nAfter approving, your browser will redirect to localhost and likely show a connection error."
        " That's expected. Copy the `code` parameter from the URL bar and paste it here.\n"
    )
    code = input("code: ").strip()
    flow.fetch_token(code=code)
    creds = flow.credentials

    tok_path.write_text(creds.to_json())
    return creds
