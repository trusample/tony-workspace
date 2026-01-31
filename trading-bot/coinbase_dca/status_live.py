#!/usr/bin/env python3
"""Live status (Coinbase Advanced Trade) — read-only.

Prints:
- number of accounts
- BTC account (if present) balance summary

Requires: coinbase_key.json in the same folder.
"""

from __future__ import annotations

from pathlib import Path

from coinbase_cdp import load_key, request_json

ROOT = Path(__file__).resolve().parent
KEY_PATH = ROOT / "coinbase_key.json"


def main() -> int:
    if not KEY_PATH.exists():
        print("coinbase_key.json not found")
        return 2

    key = load_key(KEY_PATH)
    data = request_json("GET", "/api/v3/brokerage/accounts", key)

    accounts = data.get("accounts", [])
    print(f"accounts: {len(accounts)}")

    # Try to find BTC
    btc = None
    for a in accounts:
        c = a.get("currency")
        cur = c.get("code") if isinstance(c, dict) else c
        if cur == "BTC":
            btc = a
            break

    if btc:
        avail = ((btc.get("available_balance") or {}).get("value"))
        hold = ((btc.get("hold") or {}).get("value"))
        print(f"BTC available: {avail}")
        print(f"BTC hold: {hold}")
    else:
        print("BTC account not found in response")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
