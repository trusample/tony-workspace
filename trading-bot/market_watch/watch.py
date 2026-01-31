#!/usr/bin/env python3
"""Market Watch (public data only)

Fetches candles from Coinbase public API and logs a compact snapshot.
- Computes MA(200) on daily closes
- Computes 24h change from daily closes
- Logs JSONL per run

No auth.
"""

from __future__ import annotations

import json
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(exist_ok=True)


@dataclass
class Candle:
    ts: int
    low: float
    high: float
    open: float
    close: float
    volume: float


def _get_json(url: str, timeout: int = 20) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": "clawdbot/market-watch"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_candles(product_id: str, granularity: int, days: int) -> List[Candle]:
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=days + 5)
    url = (
        "https://api.exchange.coinbase.com/products/"
        f"{product_id}/candles?granularity={granularity}&start={start.isoformat()}&end={end.isoformat()}"
    )
    raw = _get_json(url)
    candles = [Candle(int(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4]), float(r[5])) for r in raw]
    candles.sort(key=lambda c: c.ts)
    return candles


def moving_average(values: List[float], n: int) -> Optional[float]:
    if len(values) < n:
        return None
    return sum(values[-n:]) / float(n)


def log_event(event: Dict[str, Any]) -> None:
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = LOG_DIR / f"{day}.jsonl"
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")


def main() -> int:
    products = CONFIG.get("products", ["BTC-USD"])
    ma_days = int(CONFIG.get("ma_days", 200))

    out = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "source": "coinbase-public",
        "products": {},
    }

    for pid in products:
        daily = fetch_candles(pid, granularity=86400, days=max(260, ma_days + 5))
        closes = [c.close for c in daily]
        last = closes[-1]
        prev = closes[-2] if len(closes) >= 2 else last
        ma = moving_average(closes, ma_days)
        chg24 = ((last - prev) / prev) * 100 if prev else 0.0

        out["products"][pid] = {
            "last_close": last,
            "prev_close": prev,
            "chg24_pct": round(chg24, 4),
            "ma_days": ma_days,
            "ma": None if ma is None else round(ma, 6),
            "trend_ok": bool(ma is not None and last > ma),
        }

    log_event(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
