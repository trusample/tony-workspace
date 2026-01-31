#!/usr/bin/env python3
"""Coinbase DCA Bot — Phase 1 (paper trading)

- Fetch daily candles from Coinbase public API
- Compute trend filter: price > MA(N)
- If allowed, simulate a fixed USD buy
- Enforce daily + weekly spend caps
- Log decisions (JSONL)

No API keys required in paper mode.

Safety:
- This is NOT financial advice.
- Paper mode only.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import urllib.request

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.json"
STATE_PATH = ROOT / "state.json"
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)


@dataclass
class Candle:
    ts: int  # epoch seconds
    low: float
    high: float
    open: float
    close: float
    volume: float


def _http_get_json(url: str, timeout: int = 20) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": "clawdbot/coinbase-dca"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read().decode("utf-8")
        return json.loads(data)


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, obj: Dict[str, Any]) -> None:
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def iso_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def week_start_utc(dt: datetime) -> datetime:
    # Monday 00:00 UTC
    dt0 = dt.astimezone(timezone.utc)
    start = dt0 - timedelta(days=dt0.weekday(), hours=dt0.hour, minutes=dt0.minute, seconds=dt0.second, microseconds=dt0.microsecond)
    return start


def fetch_daily_candles(product_id: str, days: int) -> List[Candle]:
    # Coinbase public candles endpoint.
    # granularity=86400 gives daily candles.
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days + 5)
    url = (
        "https://api.exchange.coinbase.com/products/"
        f"{product_id}/candles?granularity=86400&start={start.isoformat()}&end={end.isoformat()}"
    )
    raw = _http_get_json(url)

    # Response is list of [time, low, high, open, close, volume]
    candles = [Candle(int(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4]), float(r[5])) for r in raw]
    candles.sort(key=lambda c: c.ts)
    # Keep only last N days
    return candles[-days:]


def moving_average(values: List[float], n: int) -> Optional[float]:
    if len(values) < n:
        return None
    return sum(values[-n:]) / float(n)


def log_event(event: Dict[str, Any]) -> None:
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = LOG_DIR / f"{day}.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")


def simulate_buy(state: Dict[str, Any], buy_usd: float, price: float) -> Dict[str, Any]:
    paper = state["paper"]
    cash = float(paper["cash_usd"])
    qty = float(paper["asset_qty"])
    avg = float(paper["avg_cost_usd"])

    spend = min(buy_usd, cash)
    if spend <= 0:
        return state

    buy_qty = spend / price
    new_qty = qty + buy_qty
    if new_qty <= 0:
        return state

    # Weighted average cost
    new_avg = ((qty * avg) + spend) / new_qty

    paper["cash_usd"] = round(cash - spend, 8)
    paper["asset_qty"] = round(new_qty, 12)
    paper["avg_cost_usd"] = round(new_avg, 8)

    return state


def main() -> int:
    cfg = load_json(CONFIG_PATH)
    state = load_json(STATE_PATH)

    product_id = cfg.get("product_id", "BTC-USD")
    buy_usd = float(cfg.get("buy_usd", 2.0))
    max_day = float(cfg.get("max_buy_usd_per_day", buy_usd))
    max_week = float(cfg.get("max_buy_usd_per_week", 14.0))
    ma_days = int(cfg.get("trend_ma_days", 200))

    candles = fetch_daily_candles(product_id, days=max(260, ma_days + 5))
    closes = [c.close for c in candles]
    last_close = closes[-1]
    ma = moving_average(closes, ma_days)

    now = datetime.now(timezone.utc)

    # weekly spend reset
    ws = state.get("weekly_spend", {})
    ws_start = ws.get("week_start")
    cur_ws = week_start_utc(now).isoformat()
    if ws_start != cur_ws:
        ws["week_start"] = cur_ws
        ws["spent_usd"] = 0.0
    spent_week = float(ws.get("spent_usd", 0.0))

    decision = {
        "ts": iso_now(),
        "product_id": product_id,
        "last_close": last_close,
        "ma_days": ma_days,
        "ma": ma,
        "trend_ok": bool(ma is not None and last_close > ma),
        "mode": cfg.get("mode", "paper"),
        "buy_usd_requested": buy_usd,
        "buy_usd_executed": 0.0,
        "reason": "",
    }

    if ma is None:
        decision["reason"] = "insufficient candle history for MA"
        log_event(decision)
        state["last_run"] = decision["ts"]
        save_json(STATE_PATH, state)
        return 0

    if not decision["trend_ok"]:
        decision["reason"] = "trend filter off (price <= MA)"
        log_event(decision)
        state["last_run"] = decision["ts"]
        save_json(STATE_PATH, state)
        return 0

    # Enforce caps
    buy = min(buy_usd, max_day)
    if spent_week >= max_week:
        decision["reason"] = "weekly cap reached"
        log_event(decision)
        state["last_run"] = decision["ts"]
        save_json(STATE_PATH, state)
        return 0

    buy = min(buy, max_week - spent_week)

    # Simulate buy
    before = dict(state["paper"])
    state = simulate_buy(state, buy, last_close)
    after = dict(state["paper"])

    executed = float(before["cash_usd"]) - float(after["cash_usd"])
    decision["buy_usd_executed"] = round(executed, 8)
    decision["reason"] = "paper buy executed" if executed > 0 else "no cash available"
    decision["paper_before"] = before
    decision["paper_after"] = after

    ws["spent_usd"] = round(spent_week + executed, 8)
    state["weekly_spend"] = ws
    state["last_run"] = decision["ts"]

    log_event(decision)
    save_json(STATE_PATH, state)

    print(json.dumps(decision, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
