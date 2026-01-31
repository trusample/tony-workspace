#!/usr/bin/env python3
"""Coinbase CDP Advanced Trade REST helpers (JWT auth).

Uses the CDP API key JSON:
{
  "name": "organizations/.../apiKeys/...",
  "privateKey": "-----BEGIN EC PRIVATE KEY-----\n...\n-----END EC PRIVATE KEY-----\n"
}

Docs: https://docs.cdp.coinbase.com

Security:
- Generate a fresh JWT per request (2 min expiry)
- Never print secrets
"""

from __future__ import annotations

import json
import secrets
import time
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

import jwt
from cryptography.hazmat.primitives import serialization

BASE_HOST = "api.coinbase.com"
BASE_HTTPS = "https://api.coinbase.com"


@dataclass
class CDPKey:
    name: str
    private_key_pem: str


def load_key(path: Path) -> CDPKey:
    d = json.loads(path.read_text(encoding="utf-8"))
    return CDPKey(name=d["name"], private_key_pem=d["privateKey"])


def format_jwt_uri(method: str, path: str) -> str:
    # Coinbase expects host-only (no scheme), per coinbase-advanced-py constants.
    return f"{method.upper()} {BASE_HOST}{path}"


def build_rest_jwt(method: str, path: str, key: CDPKey) -> str:
    private_key_bytes = key.private_key_pem.encode("utf-8")
    private_key = serialization.load_pem_private_key(private_key_bytes, password=None)

    jwt_data: Dict[str, Any] = {
        "sub": key.name,
        "iss": "cdp",
        "nbf": int(time.time()),
        "exp": int(time.time()) + 120,
        "uri": format_jwt_uri(method, path),
    }

    token = jwt.encode(
        jwt_data,
        private_key,
        algorithm="ES256",
        headers={"kid": key.name, "nonce": secrets.token_hex()},
    )
    return token


def request_json(method: str, path: str, key: CDPKey, body: Optional[bytes] = None, timeout: int = 25) -> Any:
    token = build_rest_jwt(method, path, key)
    url = f"{BASE_HTTPS}{path}"
    req = urllib.request.Request(
        url,
        data=body,
        method=method.upper(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "clawdbot/coinbase-dca",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read().decode("utf-8")
        return json.loads(data) if data else {}
