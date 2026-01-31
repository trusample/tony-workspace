#!/usr/bin/env python3
"""Kraken bot dashboard (live monitoring).

Shows:
- balances (USD, BTC, ETH if present)
- open orders count

No trading actions.
"""

from __future__ import annotations

import json
from pathlib import Path

from kraken_api import get_creds, load_dotenv, private_request

ROOT = Path(__file__).resolve().parent
DOTENV = ROOT / ".env"


def main() -> int:
    load_dotenv(DOTENV)
    creds = get_creds()

    bal = private_request("POST", "Balance", creds=creds)
    oo = private_request("POST", "OpenOrders", data={"trades": "false"}, creds=creds)

    if bal.get("error"):
        print("Balance error:", bal.get("error"))
    if oo.get("error"):
        print("OpenOrders error:", oo.get("error"))

    bals = (bal.get("result") or {})
    open_orders = (oo.get("result") or {}).get("open", {})

    def show(sym: str):
        if sym in bals:
            print(f"- {sym}: {bals[sym]}")

    print("KRAKEN DASHBOARD")
    print("BALANCES")
    for sym in ["ZUSD", "XXBT", "XETH", "USDC"]:
        show(sym)

    print(f"\nOPEN ORDERS: {len(open_orders)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
