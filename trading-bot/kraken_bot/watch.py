#!/usr/bin/env python3
"""Kraken market watch (public data only).

Logs:
- last close (daily)
- 24h change (daily)
- MA(200) on daily closes

Writes JSONL to logs/.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from kraken_api import public_request

ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)

PAIRS = {
    "BTC-USD": "XBTUSD",
    "ETH-USD": "ETHUSD",
}


def moving_average(values: List[float], n: int) -> Optional[float]:
    if len(values) < n:
        return None
    return sum(values[-n:]) / float(n)


def fetch_daily_closes(pair: str, limit: int = 260) -> List[float]:
    # Kraken OHLC returns data plus 'last'. We use interval=1440 (daily).
    res = public_request("OHLC", params={"pair": pair, "interval": "1440"})
    if res.get("error"):
        return []
    result = res.get("result") or {}
    # Find key that matches returned pair name
    key = next((k for k in result.keys() if k != "last"), None)
    if not key:
        return []
    rows = result[key]
    # Each row: [time, open, high, low, close, vwap, volume, count]
    closes = [float(r[4]) for r in rows]
    return closes[-limit:]


def log_event(event: Dict[str, Any]) -> None:
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = LOG_DIR / f"{day}.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")


def main() -> int:
    out: Dict[str, Any] = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "source": "kraken-public",
        "products": {},
    }

    for name, pair in PAIRS.items():
        closes = fetch_daily_closes(pair, limit=400)
        if len(closes) < 3:
            continue
        last = closes[-1]
        prev = closes[-2]
        chg24 = ((last - prev) / prev) * 100 if prev else 0.0
        ma200 = moving_average(closes, 200)
        out["products"][name] = {
            "pair": pair,
            "last_close": last,
            "prev_close": prev,
            "chg24_pct": round(chg24, 4),
            "ma_days": 200,
            "ma": None if ma200 is None else round(ma200, 6),
            "trend_ok": bool(ma200 is not None and last > ma200),
        }

    log_event(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
