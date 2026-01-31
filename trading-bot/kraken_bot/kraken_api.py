#!/usr/bin/env python3
"""Minimal Kraken REST client (public + private) for bot automation.

Security:
- Reads API key/secret from environment (.env) but never prints them.
- Use IP restriction on the API key (recommended).

Refs:
- https://docs.kraken.com/rest/
"""

from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

API_BASE = "https://api.kraken.com"


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())


@dataclass
class KrakenCreds:
    api_key: str
    api_secret_b64: str


def _http_post_json(url: str, data: Dict[str, str], headers: Dict[str, str], timeout: int = 25) -> Any:
    body = urllib.parse.urlencode(data).encode("utf-8")
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def _http_get_json(url: str, timeout: int = 25) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": "clawdbot/kraken-bot"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8")
        return json.loads(raw) if raw else {}


def sign_kraken(path: str, data: Dict[str, str], secret_b64: str) -> str:
    """Kraken private endpoint signing.

    API-Sign = base64( HMAC-SHA512( base64_decode(secret), path + SHA256(nonce + postdata) ) )
    """
    postdata = urllib.parse.urlencode(data)
    nonce = data.get("nonce", "")
    sha256 = hashlib.sha256((nonce + postdata).encode("utf-8")).digest()
    msg = path.encode("utf-8") + sha256
    secret = base64.b64decode(secret_b64)
    sig = hmac.new(secret, msg, hashlib.sha512).digest()
    return base64.b64encode(sig).decode("utf-8")


def get_creds(dotenv_path: Optional[Path] = None) -> KrakenCreds:
    if dotenv_path:
        load_dotenv(dotenv_path)
    k = os.environ.get("KRAKEN_API_KEY", "").strip()
    s = os.environ.get("KRAKEN_API_SECRET", "").strip()
    if not k or not s:
        raise RuntimeError("Missing KRAKEN_API_KEY or KRAKEN_API_SECRET")
    return KrakenCreds(api_key=k, api_secret_b64=s)


def private_request(method: str, endpoint: str, data: Optional[Dict[str, str]] = None, creds: Optional[KrakenCreds] = None) -> Any:
    if method.upper() != "POST":
        raise ValueError("Kraken private endpoints use POST")
    if creds is None:
        creds = get_creds()

    path = f"/0/private/{endpoint}"
    url = f"{API_BASE}{path}"

    payload = dict(data or {})
    payload.setdefault("nonce", str(int(time.time() * 1000)))

    sig = sign_kraken(path, payload, creds.api_secret_b64)
    headers = {
        "API-Key": creds.api_key,
        "API-Sign": sig,
        "User-Agent": "clawdbot/kraken-bot",
    }
    return _http_post_json(url, payload, headers=headers)


def public_request(endpoint: str, params: Optional[Dict[str, str]] = None) -> Any:
    qs = ""
    if params:
        qs = "?" + urllib.parse.urlencode(params)
    url = f"{API_BASE}/0/public/{endpoint}{qs}"
    return _http_get_json(url)
