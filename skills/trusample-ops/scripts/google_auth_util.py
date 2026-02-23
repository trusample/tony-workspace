#!/usr/bin/env python3
import json
import os
from pathlib import Path
from typing import Sequence
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

os.environ.setdefault("OAUTHLIB_RELAX_TOKEN_SCOPE", "1")

FULL_SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/script.projects",
]

def get_creds(credentials_path: str, token_path: str, scopes: Sequence[str]) -> Credentials:
    cred_path = Path(credentials_path)
    tok_path = Path(token_path)
    tok_path.parent.mkdir(parents=True, exist_ok=True)
    creds = None
    if tok_path.exists():
        creds = Credentials.from_authorized_user_file(str(tok_path), scopes=FULL_SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
        tok_path.write_text(creds.to_json())
        return creds
    if not cred_path.exists():
        raise FileNotFoundError(f"Missing credentials JSON at {cred_path}")
    flow = InstalledAppFlow.from_client_secrets_file(str(cred_path), scopes=FULL_SCOPES)
    try:
        cfg = json.loads(cred_path.read_text())
        redirect_uris = (cfg.get("installed") or {}).get("redirect_uris") or []
        flow.redirect_uri = redirect_uris[0] if redirect_uris else "http://localhost"
    except Exception:
        flow.redirect_uri = "http://localhost"
    auth_url, _ = flow.authorization_url(prompt="consent", access_type="offline")
    print("\nOPEN THIS URL IN YOUR BROWSER:\n")
    print(auth_url)
    print("\nAfter approving, copy the code from the URL bar and paste it here.\n")
    code = input("code: ").strip()
    flow.fetch_token(code=code)
    creds = flow.credentials
    tok_path.write_text(creds.to_json())
    return creds
