# Coinbase DCA Bot (Phase 1: Paper Trading)

## What it does
- Once per day, checks BTC-USD trend filter (price > 200-day moving average)
- If trend is positive, simulates buying a fixed USD amount (default $2)
- Logs every run and updates a paper portfolio

## Files
- `bot.py` — main runner
- `config.json` — strategy config
- `state.json` — paper portfolio + last run
- `logs/` — JSONL logs per run

## Run
```bash
cd /home/mhernandez/clawd/trading-bot/coinbase_dca
python3 bot.py
```

## Notes
- Paper mode: no API keys required.
- When Maykel is ready, we can add Coinbase Advanced Trade authenticated trading.
