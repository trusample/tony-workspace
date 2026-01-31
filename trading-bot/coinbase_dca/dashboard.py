#!/usr/bin/env python3
"""Dashboard: live Coinbase balances + bot state + market trend.

- Live (read-only): fetch brokerage accounts via CDP key
- Paper bot: show last run + paper portfolio
- Market: show last BTC close + MA200 (from paper bot logs if available, else fresh)

Run:
  cd /home/mhernandez/clawd/trading-bot/coinbase_dca
  python3 dashboard.py
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Tuple

from coinbase_cdp import load_key, request_json

ROOT = Path(__file__).resolve().parent
KEY_PATH = ROOT / "coinbase_key.json"
STATE_PATH = ROOT / "state.json"
LOG_DIR = ROOT / "logs"


def _fmt_money(x: Any) -> str:
    try:
        return f"{float(x):,.2f}"
    except Exception:
        return str(x)


def _get_balances() -> Dict[str, Tuple[str, str]]:
    """Return map: currency -> (available, hold)"""
    if not KEY_PATH.exists():
        return {}
    key = load_key(KEY_PATH)
    data = request_json("GET", "/api/v3/brokerage/accounts", key)
    accounts = data.get("accounts", [])
    out: Dict[str, Tuple[str, str]] = {}
    for a in accounts:
        c = a.get("currency")
        code = c.get("code") if isinstance(c, dict) else c
        if not code:
            continue
        avail = (a.get("available_balance") or {}).get("value")
        hold = (a.get("hold") or {}).get("value")
        out[str(code)] = (str(avail), str(hold))
    return out


def _read_last_log() -> Dict[str, Any]:
    if not LOG_DIR.exists():
        return {}
    # read today's file if exists else latest file
    files = sorted([p for p in LOG_DIR.glob("*.jsonl")], key=lambda p: p.name)
    if not files:
        return {}
    path = files[-1]
    last = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            last = line
    return json.loads(last) if last else {}


def main() -> int:
    print("COINBASE BOT DASHBOARD")
    print("UTC:", datetime.now(timezone.utc).isoformat())

    # Live balances
    bals = _get_balances()
    if bals:
        print("\nLIVE BALANCES (available | hold)")
        for sym in ["USD", "USDC", "BTC", "ETH", "SOL"]:
            if sym in bals:
                a, h = bals[sym]
                print(f"- {sym}: {a} | {h}")
    else:
        print("\nLIVE BALANCES: (no key found / not configured)")

    # Paper state
    if STATE_PATH.exists():
        st = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        paper = st.get("paper", {})
        print("\nPAPER PORTFOLIO")
        print(f"- cash_usd: {_fmt_money(paper.get('cash_usd', 0))}")
        print(f"- asset: {paper.get('asset')}")
        print(f"- asset_qty: {paper.get('asset_qty')}")
        print(f"- avg_cost_usd: {_fmt_money(paper.get('avg_cost_usd', 0))}")
        print(f"- last_run: {st.get('last_run')}")
        ws = st.get("weekly_spend", {})
        print(f"- week_start: {ws.get('week_start')}  spent_usd: {_fmt_money(ws.get('spent_usd', 0))}")
    else:
        print("\nPAPER PORTFOLIO: (state.json not found)")

    # Last decision snapshot
    last = _read_last_log()
    if last:
        print("\nLAST BOT DECISION")
        print(f"- product: {last.get('product_id')}")
        print(f"- trend_ok: {last.get('trend_ok')}  reason: {last.get('reason')}")
        print(f"- last_close: {_fmt_money(last.get('last_close'))}  MA({last.get('ma_days')}): {_fmt_money(last.get('ma'))}")
        print(f"- buy_usd_executed: {_fmt_money(last.get('buy_usd_executed'))}")
        print(f"- ts: {last.get('ts')}")
    else:
        print("\nLAST BOT DECISION: (no logs found)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
